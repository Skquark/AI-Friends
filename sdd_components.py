
from collections import namedtuple
from typing import Optional, Callable
import flet as ft
import flet.canvas as cv
import os, re, time, base64, threading, cv2

class SizeAwareControl(cv.Canvas):
    def __init__(self, content: Optional[ft.Control] = None, resize_interval: int=100, on_resize: Optional[Callable]=None, **kwargs):
        """
        :param content: A child Control contained by the SizeAwareControl. Defaults to None.
        :param resize_interval: The resize interval. Defaults to 100.
        :param on_resize: The callback function for resizing. Defaults to None.
        :param kwargs: Additional keyword arguments(see Canvas properties).
        Taken from: https://github.com/ndonkoHenri/Flet-Custom-Controls/commit/e1958e998ef0b16449cb58a13a94251f38ab2dac
        MIT license: https://github.com/ndonkoHenri/Flet-Custom-Controls/commit/8a8e920f0382734eef09734ea87a4c18d2cd21ed#diff-c693279643b8cd5d248172d9c22cb7cf4ed163a3c98c8a3f69c2717edd3eacb7
        """
        super().__init__(**kwargs)
        self.content = content
        self.resize_interval = resize_interval
        self.on_resize = self.__handle_canvas_resize
        self.resize_callback = on_resize
        self.size = namedtuple("size", ["width", "height"], defaults=[0, 0])

    def __handle_canvas_resize(self, e):
        """
        Called every resize_interval when the canvas is resized.
        If a resize_callback was given, it is called.
        """
        self.size = (int(e.width), int(e.height))
        self.update()
        if self.resize_callback:
            self.resize_callback(e)
#from size_aware_control import SizeAwareControl

"""Implements a pan and zoom control for flet UI framework."""
class PanZoom(ft.UserControl):
    """Pan and zoom control for flet UI framework.

    This control can be used to display a large image or other content that can be larger than the
    viewport.

    Important: the width and the height of the content must be specified in the constructor, since
    it is a write-only property. Use PIL (pillow) to figure out the width and height of an image.

    By default, the content is centered in the viewport, and scaled to fit in the viewport with
    padding added to the sides or top and bottom if necessary.

    No warranty, no support, use at your own risk, etc.
    """
    content_with_padding: ft.Container or None

    def __init__(self, content: ft.Control, content_width: int, content_height: int,
                 width: int = None, height: int = None, padding_color=ft.colors.TRANSPARENT,
                 on_pan_update=None, on_scroll=None, on_click=None, max_scale=300.0, min_scale=0.1,
                 start_scale=None, expand=False, scroll_to_scale_factor=0.001):

        super().__init__()
        self.main_control = None
        self.expand = expand
        content.scroll = None
        content.expand = False
        if isinstance(content, ft.Image):
            content.fit = ft.ImageFit.COVER  # cover the whole area even if stretching the image
        self.inner_content = content
        self.scroll_to_scale_factor = scroll_to_scale_factor
        self.padding_color = padding_color
        self.content_with_padding = None
        self.width = width
        self.height = height
        self.innerstack = None
        self.start_scale = start_scale
        self.max_scale = max_scale
        self.min_scale = min_scale
        self.on_scroll_callback = on_scroll
        self.on_click_callback = on_click
        self.on_pan_update_callback = on_pan_update
        self.content_height = content_height
        self.content_width = content_width
        self.scale = 1.0 if start_scale is None else start_scale
        self.previous_scale = self.scale
        self.offset_x = 0
        self.offset_y = 0
        self.zoom_x = None
        # the x coordinate of the point within the content where the mouse was when the zoom
        # was triggered
        self.zoom_y = None
        # the proper implementation should scale up and down around this point
        # not the center or corner of the content
        self.border_x = None
        self.border_y = None
        self.viewport_height = None
        self.viewport_width = None

    def build(self):
        """Builds the control.

        :return: the main control of the pan and zoom
        """
        content_column = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            expand=self.expand,
            controls=[
                ft.Row(
                    controls=[self.inner_content],
                    expand=self.expand,
                    alignment=ft.MainAxisAlignment.CENTER
                    )]
            )
        self.content_with_padding = ft.Container(
            height=self.content_height,
            width=self.content_width,
            bgcolor=self.padding_color,
            expand=self.expand,
            content=content_column
        )
        self.innerstack = ft.Stack(
            controls=[self.content_with_padding, ft.GestureDetector(
                on_pan_update=self.on_pan_update,
                on_scroll=self.on_scroll_update,
                on_tap_up=self.click_content
            )],
            left=0,
            top=0,
            width=self.width,
            height=self.height,
            expand=self.expand
        )
        self.main_control = SizeAwareControl(
            content=ft.Stack(controls=[self.innerstack]),
            expand=self.expand,
            on_resize=self.content_resize,
            width=self.width,
            height=self.height
        )
        return self.main_control

    def reset_content_dimensions(self):
        """Resets the content dimensions.

        This method is called when the viewport size changes.
        """
        self.scale = None
        self.update_content_pos_and_scale()

    def update_content_pos_and_scale(self):
        """Updates the position and scale of the content.

        This method is called when any parameter size, scale or position changes.
        It calculates the new position and sets it on the content.
        """
        if (self.viewport_width is None or self.viewport_height is None or
                self.viewport_height == 0 or self.content_height == 0):
            return
        viewport_ratio = self.viewport_width / self.viewport_height
        content_ratio = self.content_width / self.content_height
        # we want to pad the image with a border on the sides or on top and
        # below so that the resulting object has the same ratio as the viewport.
        # This is necessary to avoid inactive zones on the sides or top and bottom
        # (pan should work everywhere, not only on the image itself if it is very wide or tall)
        if viewport_ratio > content_ratio:
            # viewport is wider than image, so we pad the image with a border
            self.border_x = (self.content_height * viewport_ratio) - self.content_width
            self.border_y = 0
        else:
            # viewport is taller than image, so we pad the image with a border on the top and bottom
            # note: it is possible that both borders are zero
            self.border_y = (self.content_width / viewport_ratio) - self.content_height
            self.border_x = 0

        self.calculate_scale()

        stack_width = (self.content_width + self.border_x) * self.scale
        # the width of the full content scaled including the border
        stack_height = (self.content_height + self.border_y) * self.scale
        # the height of the full content scaled including the border
        stack_overflow_x = max(stack_width - self.viewport_width, 0)
        # the amount of pixels that are outside the viewport for the stack (the range of offset_x)
        stack_overflow_y = max(stack_height - self.viewport_height, 0)
        # the amount of pixels that are outside the viewport for the stack (the range of offset_y)
        content_overflow_x = max(self.content_width * self.scale - self.viewport_width, 0)
        # the amount of content pixels that are outside the viewport (the range of offset_x)
        content_overflow_y = max(self.content_height * self.scale - self.viewport_height, 0)
        # the amount of content pixels that are outside the viewport (the range of offset_y)

        self.adjust_offset_with_zoom_point(stack_height, stack_width)

        # Let's figure out the valid range for offset_x and offset_y
        # Both are negative since we are aiming with the top left corner outside the viewport
        # We have to aim the whole stack, not just the content
        # We know the movement range, which is content_overflow_x and content_overflow_y
        balance_x = min(stack_overflow_x / 2, self.border_x * self.scale / 2)
        balance_y = min(stack_overflow_y / 2, self.border_y * self.scale / 2)
        self.offset_x = self.clamp(self.offset_x, -content_overflow_x - balance_x, -balance_x)
        self.offset_y = self.clamp(self.offset_y, -content_overflow_y - balance_y, -balance_y)
        self.inner_content.width = self.content_width * self.scale
        self.inner_content.height = self.content_height * self.scale
        # TODO In theory, using scale would be enough and might even scale text
        #  better than using width and height. But scaling had strange artifacts,
        #  and strange offsets with strange overlays and erratic behaviour
        # self.inner_content.offset = ft.Offset(x=-0.0, y=-0.0)
        # self.inner_content.scale = self.scale

        self.innerstack.width = stack_width
        self.innerstack.height = stack_height
        self.content_with_padding.width = stack_width
        self.content_with_padding.height = stack_height
        self.innerstack.left = self.offset_x
        self.innerstack.top = self.offset_y
        self.innerstack.update()

    def adjust_offset_with_zoom_point(self, stack_height, stack_width):
        """Adjusts the offset according to the zoom point at zoom event.

        :param stack_height: the height of the stack
        :param stack_width: the width of the stack

        """

        if self.scale != self.previous_scale:
            if self.zoom_x is not None and self.innerstack.width is not None:
                # we have a zoom point, so we want to zoom in on that point
                # (where the mouse is when zooming)
                # we calculate the amount of size change and then adjust the offsets to match
                # the zoom point to the same position in the new image
                prevstack_width = (self.content_width + self.border_x) * self.previous_scale
                prevstack_height = (self.content_height + self.border_y) * self.previous_scale
                size_delta_x = stack_width - prevstack_width
                size_delta_y = stack_height - prevstack_height
                of_x = size_delta_x * (self.zoom_x / self.innerstack.width)  # offset of offset_x
                of_y = size_delta_y * (self.zoom_y / self.innerstack.height)  # offset of offset_y
                self.offset_x -= of_x  # offset is negative or zero since 0,0 is top left and we
                # want to move the content to the left and up only
                self.offset_y -= of_y
                self.zoom_x = None
                self.zoom_y = None
            self.previous_scale = self.scale

    def calculate_scale(self):
        """Calculates the scale of the content.

        The scale is calculated so that the content fits in the viewport with padding.
        """
        minimum_scale = min(
            self.viewport_width / (self.content_width + self.border_x),
            self.viewport_height / (self.content_height + self.border_y)
        )
        # we can't zoom out more than the full image in the viewport
        if self.scale is None:
            self.scale = self.start_scale if self.start_scale is not None else minimum_scale
            # start_scale is the preferred value, but if it is None, use the fully zoomed out
        self.scale = self.clamp(self.scale, max(minimum_scale, self.min_scale), self.max_scale)

    def content_resize(self, event: ft.canvas.CanvasResizeEvent):
        """
        :type event: ft.canvas.CanvasResizeEvent
        :param event: the event that triggered the resize
        """
        self.viewport_width = event.width
        self.viewport_height = event.height
        self.reset_content_dimensions()

    def on_pan_update(self, event: ft.DragUpdateEvent):
        """
        :type event: ft.DragUpdateEvent
        :param event: the event that triggered the pan
        """
        self.offset_x += event.delta_x
        self.offset_y += event.delta_y
        self.update_content_pos_and_scale()
        if self.on_pan_update_callback is not None:
            self.on_pan_update_callback(event)

    def on_scroll_update(self, event: ft.ScrollEvent):
        """
        :type event: ft.ScrollEvent
        :param event: scroll event
        """
        self.scale = self.scale * (1 + (event.scroll_delta_y * self.scroll_to_scale_factor))
        self.zoom_x = event.local_x
        self.zoom_y = event.local_y
        self.update_content_pos_and_scale()
        if self.on_scroll_callback is not None:
            self.on_scroll_callback(event)

    def clamp(self, value: float, min_value: float, max_value: float) -> float:
        """Clamps the value between min_value and max_value."""
        return min_value if value < min_value else max_value if value > max_value else value

    def click_content(self, event: ft.ControlEvent):
        """Handles click events on the content.

        :type event: ft.ControlEvent
        :param event: click event
        """
        # we don't need to handle offset_x and y since they are relative to the control
        x = event.local_x / self.scale - self.border_x / 2
        y = event.local_y / self.scale - self.border_y / 2
        if self.on_click_callback is not None:
            if 0 <= x < self.content_width and 0 <= y < self.content_height:
                event.local_x = x
                event.local_y = y
                self.on_click_callback(event)
     
     
class VideoContainer(ft.Container):
    """This will show a video you choose."""
    def __init__(
            self,
            video_path: str,
            fps: int = 0,
            play_after_loading=True,
            video_frame_fit_type: ft.ImageFit = None,
            video_progress_bar=True,
            video_play_button=True,
            exec_after_full_loaded=None,
            only_show_cover=False,
            content=None,
            ref=None,
            key=None,
            width=None,
            height=None,
            left=None,
            top=None,
            right=None,
            bottom=None,
            expand=None,
            col=None,
            opacity=None,
            rotate=None,
            scale=None,
            offset=None,
            aspect_ratio=None,
            animate_opacity=None,
            animate_size=None,
            animate_position=None,
            animate_rotation=None,
            animate_scale=None,
            animate_offset=None,
            on_animation_end=None,
            tooltip=None,
            visible=None,
            disabled=None,
            data=None,
            padding=None,
            margin=None,
            alignment=None,
            bgcolor=None,
            gradient=None,
            blend_mode=ft.BlendMode.SCREEN,
            border=None,
            border_radius=None,
            image_src=None,
            image_src_base64=None,
            image_repeat=None,
            image_fit=None,
            image_opacity=1.0,#OptionalNumber = None,
            shape=None,
            clip_behavior=None,
            ink=None,
            animate=None,
            blur=None,
            shadow=None,
            url=None,
            url_target=None,
            theme=None,
            theme_mode=None,
            on_click=None,
            on_long_press=None,
            on_hover=None
    ):
        super().__init__(content, ref, key, width, height, left, top, right, bottom, expand, col, opacity, rotate,
                         scale, offset, aspect_ratio, animate_opacity, animate_size, animate_position, animate_rotation,
                         animate_scale, animate_offset, on_animation_end, tooltip, visible, disabled, data, padding,
                         margin, alignment, bgcolor, gradient, blend_mode, border, border_radius, image_src,
                         image_src_base64, image_repeat, image_fit, image_opacity, shape, clip_behavior, ink, animate,
                         blur, shadow, url, url_target, theme, theme_mode, on_click, on_long_press, on_hover)
        self.__cur_play_frame = 0
        self.__video_pause_button = None
        self.__video_play_button = None
        self.__video_is_play = False
        self.vid_duration = None
        self.fps = fps
        self.__video_is_full_loaded = None
        self.video_frames = None
        self.exec_after_full_loaded = exec_after_full_loaded
        if not os.path.isfile(video_path):
            raise FileNotFoundError("Cannot find the video at the path you set.")
        self.all_frames_of_video = []
        self.frame_length = 0
        self.__video_played = False
        self.video_progress_bar = video_progress_bar
        self.video_play_button = video_play_button
        if video_frame_fit_type is None:
            self.video_frame_fit_type = ft.ImageFit.CONTAIN
        self.__ui()
        if only_show_cover:
            self.read_video_cover(video_path)
            return
        if play_after_loading:
            print("Please wait the video is loading..\nThis will take a time based on your video size...")
            self.read_the_video(video_path)
        else:
            threading.Thread(target=self.read_the_video, args=[video_path], daemon=True).start()
        self.audio_path = None
        self.__audio_path = None
        self.get_video_duration(video_path)
        self.__frame_per_sleep = 1.0 / self.fps

    def show_play(self):
        self.__video_is_play = False
        self.__video_play_button.visible = True
        self.__video_pause_button.visible = False
        self.__video_play_button.update()
        self.__video_pause_button.update()

    def show_pause(self):
        self.__video_is_play = True
        self.__video_play_button.visible = False
        self.__video_pause_button.visible = True
        self.__video_play_button.update()
        self.__video_pause_button.update()

    def __ui(self):
        # the video tools control
        self.video_tool_stack = ft.Stack(expand=False)
        self.content = self.video_tool_stack
        self.image_frames_viewer = ft.Image(expand=True, visible=False, fit=self.video_frame_fit_type)
        self.video_tool_stack.controls.append(ft.Row([self.image_frames_viewer], alignment=ft.MainAxisAlignment.CENTER))
        self.__video_progress_bar = ft.Container(height=2, bgcolor=ft.colors.BLUE_200)
        self.video_tool_stack.controls.append(ft.Row([self.__video_progress_bar], alignment=ft.MainAxisAlignment.START))

        def play_video(e):
            print(e)
            if self.__video_is_play:
                self.pause()
                self.show_play()
            else:
                self.show_pause()
                self.play()

        self.__video_play_button = ft.IconButton(
            icon=ft.icons.SMART_DISPLAY,
            icon_color=ft.colors.WHITE54,
            icon_size=60,
            data=0,
            style=ft.ButtonStyle(
                elevation=4,
            ),
            on_click=play_video,
            visible=True
        )
        self.__video_pause_button = ft.IconButton(
            icon=ft.icons.PAUSE_PRESENTATION,
            icon_color=ft.colors.WHITE54,
            icon_size=60,
            data=0,
            style=ft.ButtonStyle(
                elevation=4,
            ),
            on_click=play_video,
            visible=False
        )
        self.video_tool_stack.controls.append(
            ft.Container(
                content=ft.Row(
                    controls=[
                        self.__video_play_button,
                        self.__video_pause_button
                    ]
                ),
                padding=ft.padding.only(25, 10, 10, 10),
                left=0,
                bottom=0,
            ),
        )
        if not self.video_progress_bar:
            self.__video_progress_bar.visible = False
        if not self.video_play_button:
            self.__video_play_button.visible = False

    def update_video_progress(self, frame_number):
        if not self.video_progress_bar:
            return
        percent_of_progress = frame_number / self.video_frames * 1
        if self.width:
            self.__video_progress_bar.width = percent_of_progress * 1 * self.width
        else:
            self.__video_progress_bar.width = percent_of_progress * 1 * self.page.width
        if self.__video_progress_bar.page is not None:
            try:
                self.__video_progress_bar.update()
            except Exception as e:
                pattern = r"control with ID '(.*)' not found"
                match = re.search(pattern, e.args[0])
                if not match:
                    print(e)
                return

    def update(self):
        self.image_frames_viewer.fit = self.video_frame_fit_type
        self.__video_progress_bar.visible = self.video_progress_bar
        return super().update()

    def play(self):
        """Play the video. (it's not blocking, because its on thread)."""
        if self.page is None:
            raise Exception("The control must be on page first.")
        self.__video_played = True
        threading.Thread(target=self.__play, daemon=True).start()

    def __play(self):
        self.image_frames_viewer.visible = True
        num = self.__cur_play_frame
        video_frames_len = len(self.all_frames_of_video)
        for index, i in enumerate(self.all_frames_of_video[self.__cur_play_frame:-1]):
            if not self.__video_played:
                self.__cur_play_frame = self.__cur_play_frame + index
                break
            if index + self.__cur_play_frame == video_frames_len - 2:
                self.__cur_play_frame = 0
            threading.Thread(target=self.update_video_progress, args=[num], daemon=True).start()
            self.image_frames_viewer.src_base64 = i
            try:
                self.image_frames_viewer.update()
            except Exception as e:
                pattern = r"control with ID '(.*)' not found"
                match = re.search(pattern, e.args[0])
                if not match:
                    print(e)
                return
            time.sleep(self.__frame_per_sleep)
            num += 1
        self.show_play()

    def pause(self):
        self.__video_played = False

    def read_video_cover(self, video_path):
        video = cv2.VideoCapture(video_path)
        frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
        slice_frame_num = frame_count / 2
        video.set(cv2.CAP_PROP_POS_FRAMES, slice_frame_num)
        success, frame = video.read()
        _, buffer = cv2.imencode('.jpg', frame)
        encoded_frame = base64.b64encode(buffer).decode('utf-8')
        if self.image_frames_viewer.src_base64 is None:
            self.image_frames_viewer.src_base64 = encoded_frame
            self.image_frames_viewer.visible = True
            if self.image_frames_viewer.page is not None:
                self.image_frames_viewer.update()
        video.release()

    def read_the_video(self, video_path):
        video = cv2.VideoCapture(video_path)
        success, frame = video.read()
        while success:
            _, buffer = cv2.imencode('.jpg', frame)
            encoded_frame = base64.b64encode(buffer).decode('utf-8')
            self.all_frames_of_video.append(encoded_frame)
            if self.image_frames_viewer.src_base64 is None:
                self.image_frames_viewer.src_base64 = encoded_frame
                self.image_frames_viewer.visible = True
                if self.image_frames_viewer.page is not None:
                    self.image_frames_viewer.update()
            success, frame = video.read()
        video.release()
        self.__video_is_full_loaded = True
        if self.exec_after_full_loaded:
            self.exec_after_full_loaded()
        self.frame_length = len(self.all_frames_of_video)
        return self.all_frames_of_video

    def get_video_duration(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error opening video file")
            return
        if self.fps == 0:
            fps = cap.get(cv2.CAP_PROP_FPS)
            self.fps = fps
        total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.video_frames = total_frames
        duration = total_frames / fps
        self.vid_duration = duration
        cap.release()

''' Sample alt Object format
class Component(UserControl):
    def __init__(self):
        super().__init__()
        self.build()
    def search(self, e):
        pass
    def build(self):
        self.expand = True
        #self.table
        self.parameter = Ref[TextField]()
        return Column(controls=[])
class Main:
    def __init__(self):
        self.page = None
    def __call__(self, page: Page):
        self.page = page
        page.title = "Alternative Boot experiment"
        self.add_stuff()
    def add_stuff(self):
        self.page.add(Text("Some text", size=20), color=colors.ON_PRIMARY_CONTAINER, bgcolor=colors.PRIMARY_CONTAINER, height=45)
        self.page.update()
main = Main()'''
