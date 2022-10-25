#@title ## **▶️ Run Stable Diffusion Deluxe** - Flet/Flutter WebUI App
import flet, webbrowser
#from flet import Page, View, Column, Row, Container, Text, Stack, TextField, Checkbox, Switch, Image, ElevatedButton, IconButton, Markdown, Tab, Tabs, Divider, VerticalDivider, SnackBar, AnimatedSwitcher
from flet import *
from flet import icons, dropdown, colors, padding, margin, alignment, border_radius, theme, animation
from flet import Image as Img
import io, shutil
from contextlib import redirect_stdout

status = {
    'installed_diffusers': False,
    'installed_txt2img': False,
    'installed_img2img': False,
    'installed_stability': False,
    'installed_megapipe': False,
    'installed_interpolation': False,
    'installed_clip': False,
    'installed_ESRGAN': False,
    'installed_OpenAI': False,
    'installed_TextSynth': False,
    'changed_settings': False,
    'changed_installers': False,
    'changed_parameters': False,
    'changed_prompts': False,
    'changed_prompt_generator': False,
    'changed_prompt_remixer': False,
    'changed_prompt_brainstormer': False,
    'changed_prompt_writer': False,
    'initialized': False,
}

def save_settings_file(page):
  page.app_icon_save()
  if not os.path.isfile(saved_settings_json):
    settings_path = saved_settings_json.rpartition('/')[0]
    os.makedirs(settings_path, exist_ok=True)
  with open(saved_settings_json, "w") as write_file:
    json.dump(prefs, write_file, indent=4)

current_tab = 0
def tab_on_change (e):
    t = e.control
    global current_tab
    #print (f"tab changed from {current_tab} to: {t.selected_index}")
    #print(str(t.tabs[t.selected_index].text))
    if current_tab == 0:
      if not status['initialized']:
        initState(e.page)
        status['initialized'] = True
      if status['changed_settings']:
        save_settings_file(e.page)
        status['changed_settings'] = False
        #print(len(e.page.Settings.content.controls))
        #save_settings(e.page.Settings.content.controls)
    if current_tab == 1:
      if status['changed_installers']:
        save_settings_file(e.page)
        status['changed_installers'] = False
        #print("Saving Installers")
    if current_tab == 2:
      if status['changed_parameters']:
        update_args()
        e.page.update_prompts()
        save_settings_file(e.page)
        status['changed_parameters'] = False
    if current_tab == 3:
      if status['changed_prompts']:
        e.page.save_prompts()
        save_settings_file(e.page)
        status['changed_prompts'] = False
    if current_tab == 5:
      if status['changed_prompt_generator']:
        save_settings_file(e.page)
        status['changed_prompt_generator'] = False
    
    current_tab = t.selected_index
    if current_tab == 1:
      refresh_installers(e.page.Installers.content.controls)
      #page.Installers.init_boxes()
    if current_tab == 2:
      update_parameters(e.page)
      #for p in e.page.Parameters.content.controls:
      #  p.update()
      e.page.Parameters.content.update()
      e.page.Parameters.update()

    e.page.update()

def buildTabs(page):
    page.Settings = buildSettings(page)
    page.Installers = buildInstallers(page)
    page.Parameters = buildParameters(page)
    page.PromptsList = buildPromptsList(page)
    page.PromptHelpers = buildPromptHelpers(page)
    page.Images = buildImages(page)
    page.Extras = buildExtras(page)
    
    t = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(text="Settings", content=page.Settings, icon=icons.SETTINGS_OUTLINED),
            Tab(text="Installation", content=page.Installers, icon=icons.INSTALL_DESKTOP),
            Tab(text="Image Parameters", content=page.Parameters, icon=icons.DISPLAY_SETTINGS),
            Tab(text="Prompts List", content=page.PromptsList, icon=icons.FORMAT_LIST_BULLETED),
            Tab(text="Generate Images", content=page.Images, icon=icons.IMAGE_OUTLINED),
            Tab(text="Prompt Helpers", content=page.PromptHelpers, icon=icons.BUBBLE_CHART_OUTLINED),
            Tab(text="Extras", content=page.Extras, icon=icons.ALL_INBOX),
        ],
        expand=1,
        #on_change=tab_on_change
    )
    page.tabs = t
    #page.load_prompts()
    return t

def b_style():
    return ButtonStyle(elevation=8)
def dict_diff(dict1, dict2):
    return {k: v for k, v in dict1.items() if k in dict2 and v != dict2[k]}
def arg_diffs(dict1, dict2):
    diff = dict_diff(dict1, dict2)
    if len(diff) > 0:
      dif = []
      for k, v in diff.items():
        dif.append(f'{k}: {v}')
      return ', '.join(dif)
    else: return None
def get_color(color):
    if color == "green": return colors.GREEN
    elif color == "blue": return colors.BLUE
    elif color == "indigo": return colors.INDIGO
    elif color == "red": return colors.RED
    elif color == "purple": return colors.DEEP_PURPLE
    elif color == "orange": return colors.ORANGE
    elif color == "amber": return colors.AMBER
    elif color == "brown": return colors.BROWN
    elif color == "teal": return colors.TEAL

def initState(page):
    if os.path.isdir(os.path.join(root_dir, 'Real-ESRGAN')):
      status['installed_ESRGAN'] = True
    page.load_prompts()
    page.snd_alert = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-alert.mp3?raw=true", autoplay=False)
    page.snd_delete = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-delete.mp3?raw=true", autoplay=False)
    page.snd_error = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-error.mp3?raw=true", autoplay=False)
    page.snd_done = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-done.mp3?raw=true", autoplay=False)
    page.snd_notification = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-notification.mp3?raw=true", autoplay=False)
    page.overlay.append(page.snd_alert)
    page.overlay.append(page.snd_delete)
    page.overlay.append(page.snd_error)
    page.overlay.append(page.snd_done)
    page.overlay.append(page.snd_notification)

def buildSettings(page):
  def open_url(e):
    page.launch_url(e.data)
  def save_settings(e):
    save_settings_file(e.page)
    page.snack_bar = SnackBar(content=Text(f"Saving all settings to {saved_settings_json.rpartition('/')[2]}"))
    page.snack_bar.open = True
    page.tabs.selected_index = 1
    page.tabs.update()
    page.update()
  def changed(e, pref=None):
      if pref is not None:
        prefs[pref] = e.control.value
      has_changed = True
      page.update()
      status['changed_settings'] = True
  def change_theme_mode(e):
    prefs['theme_mode'] = e.control.value
    if prefs['theme_mode'].lower() == "dark":
      page.dark_theme = Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    else:
      page.theme = theme.Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    page.theme_mode = prefs['theme_mode'].lower()
    page.update()
  def change_theme_color(e):
    prefs['theme_color'] = e.control.value
    if prefs['theme_mode'].lower() == "dark":
      page.dark_theme = Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    else:
      page.theme = theme.Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    page.update()
  def toggle_nsfw(e):
    retry_attempts.width = 0 if e.control.value else None
    retry_attempts.update()
    changed(e, 'disable_nsfw_filter')
  #haschanged = False
  #save_to_GDrive = Checkbox(label="Save to Google Drive", value=prefs['save_to_GDrive'])
  image_output = TextField(label="Image Output Path", value=prefs['image_output'], on_change=lambda e:changed(e, 'image_output'))
  file_prefix = TextField(label="Filename Prefix",  value=prefs['file_prefix'], on_change=lambda e:changed(e, 'file_prefix'))
  file_suffix_seed = Checkbox(label="Filename Suffix Seed", tooltip="Appends -seed# to the end of the image name", value=prefs['file_suffix_seed'], on_change=lambda e:changed(e, 'file_suffix_seed'))
  file_allowSpace = Checkbox(label="Filename Allow Space", tooltip="Otherwise will replace spaces with _ underscores ", value=prefs['file_allowSpace'], on_change=lambda e:changed(e, 'file_allowSpace'))
  file_max_length = TextField(label="Filename Max Length", tooltip="How long can the name taken from prompt text be? Max 250", value=prefs['file_max_length'], keyboard_type="number", on_change=lambda e:changed(e, 'file_max_length'))
  save_image_metadata = Checkbox(label="Save Image Metadata in png", tooltip="Embeds your Artist Name & Copyright in the file's EXIF", value=prefs['save_image_metadata'], on_change=lambda e:changed(e, 'save_image_metadata'))
  meta_ArtistName = TextField(label="Artist Name Metadata", value=prefs['meta_ArtistName'], keyboard_type="name", on_change=lambda e:changed(e, 'meta_ArtistName'))
  meta_Copyright = TextField(label="Copyright Metadata", value=prefs['meta_Copyright'], keyboard_type="name", on_change=lambda e:changed(e, 'meta_Copyright'))
  save_config_in_metadata = Checkbox(label="Save Config in Metadata", tooltip="Embeds all prompt parameters in the file's EXIF to recreate", value=prefs['save_config_in_metadata'], on_change=lambda e:changed(e, 'save_config_in_metadata'))
  save_config_json = Checkbox(label="Save Config JSON files", tooltip="Creates a json text file with all prompt parameters with each image", value=prefs['save_config_json'], on_change=lambda e:changed(e, 'save_config_json'))
  theme_mode = Dropdown(label="Theme Mode", width=200, options=[dropdown.Option("Dark"), dropdown.Option("Light")], value=prefs['theme_mode'], on_change=change_theme_mode)
  theme_color = Dropdown(label="Accent Color", width=200, options=[dropdown.Option("Green"), dropdown.Option("Blue"), dropdown.Option("Red"), dropdown.Option("Indigo"), dropdown.Option("Purple"), dropdown.Option("Orange"), dropdown.Option("Amber"), dropdown.Option("Brown"), dropdown.Option("Teal")], value=prefs['theme_color'], on_change=change_theme_color)
  enable_sounds = Checkbox(label="Enable UI Sound Effects", tooltip="Turn on for audible errors, deletes and generation done notifications", value=prefs['enable_sounds'], on_change=lambda e:changed(e, 'enable_sounds'))
  disable_nsfw_filter = Checkbox(label="Disable NSFW Filters", value=prefs['disable_nsfw_filter'], on_change=toggle_nsfw)
  retry_attempts = Container(NumberPicker(label="Retry Attempts if Not Safe", min=0, max=8, value=prefs['retry_attempts'], on_change=lambda e:changed(e, 'retry_attempts')), padding=padding.only(left=20), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  retry_attempts.width = 0 if prefs['disable_nsfw_filter'] else None
  api_instructions = Container(height=115, content=Markdown("Get **HuggingFace API key** from https://huggingface.co/settings/tokens and accept the cards for [1.5 model](https://huggingface.co/runwayml/stable-diffusion-v1-5), [1.4 model](https://huggingface.co/CompVis/stable-diffusion-v1-4),  & [Inpainting model](https://huggingface.co/runwayml/stable-diffusion-inpainting).\n\nGet **Stability-API key** from https://beta.dreamstudio.ai/membership?tab=apiKeys then API key\n\nGet **OpenAI GPT-3 API key** from https://beta.openai.com, user menu, View API Keys\n\nGet **TextSynth GPT-J key** from https://TextSynth.com, login, Setup", extension_set="gitHubWeb", on_tap_link=open_url))
  HuggingFace_api = TextField(label="HuggingFace API Key", value=prefs['HuggingFace_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'HuggingFace_api_key'))
  Stability_api = TextField(label="Stability.ai API Key", value=prefs['Stability_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'Stability_api_key'))
  OpenAI_api = TextField(label="OpenAI API Key", value=prefs['OpenAI_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'OpenAI_api_key'))
  TextSynth_api = TextField(label="TextSynth API Key", value=prefs['TextSynth_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'TextSynth_api_key'))
  save_button = ElevatedButton(content=Text(value="💾  Save Settings", size=20), on_click=save_settings, style=b_style())
  
  c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text ("⚙️   Deluxe Stable Diffusion Settings & Preferences", style="titleLarge"),
        Divider(thickness=1, height=4),
        #save_to_GDrive,
        image_output,
        #VerticalDivider(thickness=2),
        file_prefix,
        file_suffix_seed,
        file_allowSpace,
        file_max_length,
        #Row([disable_nsfw_filter, retry_attempts]),
        #VerticalDivider(thickness=2, width=1),
        save_image_metadata,
        meta_ArtistName,
        meta_Copyright,
        save_config_in_metadata,
        save_config_json,
        Row([theme_mode, theme_color]),
        enable_sounds,
        #VerticalDivider(thickness=2, width=1),
        api_instructions,
        HuggingFace_api,
        Stability_api,
        OpenAI_api,
        TextSynth_api,
        #save_button,
        Container(content=None, height=8),
      ], scroll="auto",
  ))
  return c

def run_process(cmd_str, cwd=None, realtime=True, page=None, close_at_end=False):
  cmd_list = cmd_str if type(cmd_str) is list else cmd_str.split()
  if realtime:
    if cwd is None:
      process = subprocess.Popen(cmd_str, shell = True, env=env, bufsize = 1, stdout=subprocess.PIPE, stderr = subprocess.STDOUT, encoding='utf-8', errors = 'replace' ) 
    else:
      process = subprocess.Popen(cmd_str, shell = True, cwd=cwd, env=env, bufsize = 1, stdout=subprocess.PIPE, stderr = subprocess.STDOUT, encoding='utf-8', errors = 'replace' ) 
    while True:
      realtime_output = process.stdout.readline()
      if realtime_output == '' and process.poll() is not None:
        break
      if realtime_output:
        #print(realtime_output.strip(), flush=False)
        page.banner.content.controls.append(Text(realtime_output.strip()))
        page.update()
        sys.stdout.flush()
    if close_at_end:
      page.banner.open = False
      page.update()
  else:
    if cwd is None:
      #return subprocess.run(cmd_list, stdout=subprocess.PIPE).stdout.decode('utf-8')
      return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    else:
      return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env, cwd=cwd).stdout.decode('utf-8')

def close_alert_dlg(e):
      e.page.alert_dlg.open = False
      e.page.update()
def alert_msg(page, msg):
      okay = ElevatedButton(" OKAY ", on_click=close_alert_dlg)
      page.alert_dlg = AlertDialog(title=Text(msg), actions=[okay], actions_alignment="end")
      page.dialog = page.alert_dlg
      page.alert_dlg.open = True
      page.update()

def save_installers(controls):
  for c in controls:
    if isinstance(c, Switch):
      #print(f"elif c.value == '{c.label}': prefs[''] = c.value")
      if c.value == 'Install HuggingFace Diffusers Pipeline': prefs['install_diffusers'] = c.value
      elif c.value == 'Install Stability-API DreamStudio Pipeline': prefs['install_Stability_api'] = c.value
      elif c.value == 'Install Real-ESRGAN AI Upscaler': prefs['install_ESRGAN'] = c.value
      elif c.value == 'Install OpenAI GPT-3 Text Engine': prefs['install_OpenAI'] = c.value
      elif c.value == 'Install TextSynth GPT-J Text Engine': prefs['install_TextSynth'] = c.value
    elif isinstance(c, Container):
      '''try:
        for i in c.content.controls:
          if isinstance(i, Switch):
            print(f"elif i.value == '{c.label}': prefs[''] = i.value")
      except: continue'''
def refresh_installers(controls):
  for c in controls:
    if isinstance(c, Switch):
      c.update()

def buildInstallers(page):
  def changed(e, pref=None):
      if pref is not None:
        prefs[pref] = e.control.value
      page.update()
      status['changed_installers'] = True
    #has_changed = True
    #page.update()
  def changed_status(e, stat=None):
      if stat is not None:
        status[stat] = e.control.value
  #has_changed = False
  #save_to_GDrive = Checkbox(label="Save to Google Drive", value=prefs['save_to_GDrive'])

  def toggle_diffusers(e):
    prefs['install_diffusers'] = install_diffusers.value
    diffusers_settings.height=None if prefs['install_diffusers'] else 0
    diffusers_settings.update()
    status['changed_installers'] = True
  install_diffusers = Switch(label="Install HuggingFace Diffusers Pipeline", value=prefs['install_diffusers'], disabled=status['installed_diffusers'], on_change=toggle_diffusers)

  scheduler_mode = Dropdown(label="Scheduler/Sampler Mode", hint_text="They're very similar, with minor differences in the noise", width=200,
            options=[
                dropdown.Option("DDIM"),
                dropdown.Option("K-LMS"),
                dropdown.Option("PNDM"),
            ], value=prefs['scheduler_mode'], autofocus=False, on_change=lambda e:changed(e, 'scheduler_mode'),
        )
  model_ckpt = Dropdown(label="Model Checkpoint", hint_text="Make sure you accepted the HuggingFace Model Cards first", width=350, options=[dropdown.Option("Stable Diffusion v1.5"), dropdown.Option("Stable Diffusion v1.4")], value=prefs['model_ckpt'], autofocus=False, on_change=lambda e:changed(e, 'model_ckpt'))
  higher_vram_mode = Checkbox(label="Higher VRAM Mode", tooltip="Adds a bit more precision but takes longer & uses much more GPU memory. Not recommended.", value=prefs['higher_vram_mode'], on_change=lambda e:changed(e, 'higher_vram_mode'))
  enable_attention_slicing = Checkbox(label="Enable Attention Slicing", tooltip="Saves VRAM while creating images so you can go bigger without running out of mem.", value=prefs['enable_attention_slicing'], on_change=lambda e:changed(e, 'enable_attention_slicing'))
  #install_megapipe = Switch(label="Install Stable Diffusion txt2image, img2img & Inpaint Mega Pipeline", value=prefs['install_megapipe'], disabled=status['installed_megapipe'], on_change=lambda e:changed(e, 'install_megapipe'))
  install_text2img = Switch(label="Install Stable Diffusion text2image Pipeline", value=prefs['install_text2img'], disabled=status['installed_txt2img'], on_change=lambda e:changed(e, 'install_txt2img'))
  install_img2img = Switch(label="Install Stable Diffusion image2image & Inpaint Pipeline", value=prefs['install_img2img'], disabled=status['installed_img2img'], on_change=lambda e:changed(e, 'install_img2img'))
  install_interpolation = Switch(label="Install Stable Diffusion Walk Interpolation Pipeline", value=prefs['install_interpolation'], disabled=status['installed_interpolation'], on_change=lambda e:changed(e, 'install_interpolation'))
  
  def toggle_clip(e):
      prefs['install_CLIP_guided'] = install_CLIP_guided.value
      status['changed_installers'] = True
      clip_settings.height=None if prefs['install_CLIP_guided'] else 0
      clip_settings.update()
  install_CLIP_guided = Switch(label="Install Stable Diffusion CLIP-Guided Pipeline", value=prefs['install_CLIP_guided'], disabled=status['installed_clip'], on_change=toggle_clip)
  clip_model_id = Dropdown(label="CLIP Model ID", hint_text="Hard to explain, but they take up more VRAM, so may need to make images smaller", width=350,
            options=[
                dropdown.Option("laion/CLIP-ViT-B-32-laion2B-s34B-b79K"),
                dropdown.Option("laion/CLIP-ViT-L-14-laion2B-s32B-b82K"),
                dropdown.Option("laion/CLIP-ViT-H-14-laion2B-s32B-b79K"),
                dropdown.Option("laion/CLIP-ViT-g-14-laion2B-s12B-b42K"),
                dropdown.Option("openai/clip-vit-base-patch32"),
                dropdown.Option("openai/clip-vit-base-patch16"),
                dropdown.Option("openai/clip-vit-large-patch14"),
            ], value=prefs['clip_model_id'], autofocus=False, on_change=lambda e:changed(e, 'clip_model_id'),
        )
  clip_settings = Container(animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge", padding=padding.only(left=32, top=4), content=Column([clip_model_id]))

  diffusers_settings = Container(animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge", content=
                                 Column([Container(Column([scheduler_mode, model_ckpt, higher_vram_mode, enable_attention_slicing]), padding=padding.only(left=32, top=4)),
                                         install_text2img, install_img2img, #install_megapipe, 
                                         install_interpolation, install_CLIP_guided, clip_settings]))
  def toggle_stability(e):
    prefs['install_Stability_api'] = install_Stability_api.value
    has_changed=True
    #print(f"Toggle Stability {prefs['install_Stability_api']}")
    stability_settings.height=None if prefs['install_Stability_api'] else 0
    stability_settings.update()
    page.update()
    #stability_box.content = stability_settings if prefs['install_stability'] else Container(content=None)
    #stability_box.update()
  install_Stability_api = Switch(label="Install Stability-API DreamStudio Pipeline", value=prefs['install_Stability_api'], disabled=status['installed_stability'], on_change=toggle_stability)
  use_Stability_api = Checkbox(label="Use Stability-api by default", value=prefs['use_Stability_api'], on_change=lambda e:changed(e, 'use_Stability_api'))
  model_checkpoint = Dropdown(label="Model Checkpoint", hint_text="", width=350,
            options=[
                dropdown.Option("stable-diffusion-v1-5"),
                dropdown.Option("stable-diffusion-v1.4"),
            ], value=prefs['model_checkpoint'], autofocus=False, on_change=lambda e:changed(e, 'model_checkpoint'),
        )
  generation_sampler = Dropdown(label="generation_sampler", hint_text="", width=350,
            options=[
                dropdown.Option("ddim"),
                dropdown.Option("plms"),
                dropdown.Option("k_euler"),
                dropdown.Option("k_euler_ancestral"),
                dropdown.Option("k_heun"),
                dropdown.Option("k_dpm_2"),
                dropdown.Option("k_dpm_2_ancestral"),
                dropdown.Option("k_lms"),
            ], value=prefs['generation_sampler'], autofocus=False, on_change=lambda e:changed(e, 'generation_sampler'),
        )

  stability_settings = Container(animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge", padding=padding.only(left=32), content=Column([use_Stability_api, model_checkpoint, generation_sampler]))
  
  install_ESRGAN = Switch(label="Install Real-ESRGAN AI Upscaler", value=prefs['install_ESRGAN'], disabled=status['installed_ESRGAN'], on_change=lambda e:changed(e, 'install_ESRGAN'))
  install_OpenAI = Switch(label="Install OpenAI GPT-3 Text Engine", value=prefs['install_OpenAI'], disabled=status['installed_OpenAI'], on_change=lambda e:changed(e, 'install_OpenAI'))
  install_TextSynth = Switch(label="Install TextSynth GPT-J Text Engine", value=prefs['install_TextSynth'], disabled=status['installed_TextSynth'], on_change=lambda e:changed(e, 'install_TextSynth'))
  diffusers_settings.height = None if prefs['install_diffusers'] else 0
  stability_settings.height = None if prefs['install_Stability_api'] else 0
  clip_settings.height = None if prefs['install_CLIP_guided'] else 0
  
  
  def run_installers(e):
      def console_clear():
        page.banner.content.controls = []
        page.update()
      def console_msg(msg, clear=True, show_progress=True):
        if clear:
          page.banner.content.controls = []
        if show_progress:
          page.banner.content.controls.append(Stack([Container(content=Text(msg.strip() + "  ", weight="bold", color=colors.ON_SECONDARY_CONTAINER, size=18), alignment=alignment.bottom_left), Container(content=ProgressRing(), alignment=alignment.center)]))
          #page.banner.content.controls.append(Row([Text(msg.strip() + "  ", weight="bold", color=colors.GREEN_600), ProgressRing()]))
        else:
          page.banner.content.controls.append(Text(msg.strip(), weight="bold", color=colors.GREEN_600))
        page.update()
      if prefs['install_diffusers'] and not bool(prefs['HuggingFace_api_key']):
        alert_msg(e.page, "You must provide your HuggingFace API Key to use Diffusers.")
        return
      if prefs['install_Stability_api'] and not bool(prefs['Stability_api_key']):
        alert_msg(e.page, "You must have your DreamStudio.ai Stability-API Key to use Stability.  Note that it will use your tokens.")
        return
      if prefs['install_OpenAI'] and not bool(prefs['OpenAI_api_key']):
        alert_msg(e.page, "You must have your OpenAI API Key to use GPT-3 Text AI.")
        return
      if prefs['install_TextSynth'] and not bool(prefs['TextSynth_api_key']):
        alert_msg(e.page, "You must have your TextSynth API Key to use GPT-J Text AI.")
        return
      page.banner.content = Column([], scroll="auto", auto_scroll=True, tight=True, spacing=0, alignment="end")
      page.banner.open = True
      page.update()
      if prefs['install_diffusers']:
        console_msg("Installing Hugging Face Diffusers Pipeline...")
        run_diffusers(page)
        status['installed_diffusers'] = True

      if prefs['install_text2img'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Text2Image Pipeline...")
        with io.StringIO() as buf, redirect_stdout(buf):
          #print('redirected')
          get_text2image(page)
          output = buf.getvalue()
          page.banner.content.controls.append(Text(output.strip()))
          page.update()
        status['installed_txt2img'] = True
      if prefs['install_img2img'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Image2Image Pipeline...")
        get_image2image(page)
        status['installed_img2img'] = True
        page.img_block.height = None
        page.img_block.update()
      '''if prefs['install_megapipe'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Unified Mega Pipeline...")
        get_text2image(page)
        status['installed_megapipe'] = True
        page.img_block.height = None
        page.img_block.update()'''
      if prefs['install_interpolation'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Walk Interpolation Pipeline...")
        get_interpolation(page)
        status['installed_interpolation'] = True
        page.interpolation_block.visible = True
        page.interpolation_block.update()
      if prefs['install_CLIP_guided'] and prefs['install_diffusers'] and not status['installed_clip']:
        console_msg("Downloading Stable Diffusion CLIP-Guided Pipeline...")
        get_clip(page)
        status['installed_clip'] = True
        page.clip_block.height = None
        page.clip_block.update()
      if prefs['install_Stability_api']:
        console_msg("Installing Stability-API DreamStudio.ai Pipeline...")
        get_stability(page)
        status['installed_stability'] = True
      if prefs['install_ESRGAN'] and not status['installed_ESRGAN']:
        console_msg("Installing Real-ESRGAN Upscaler...")
        if not os.path.isdir(os.path.join(root_dir, 'Real-ESRGAN')):
          get_ESRGAN(page)
        status['installed_ESRGAN'] = True
        page.ESRGAN_block.height = None
        page.ESRGAN_block.update()
      if prefs['install_OpenAI'] and not status['installed_OpenAI']:
        console_msg("Installing OpenAI GPT-3 Libraries...")
        try:
          import openai
        except ImportError as e:
          run_process("pip install openai -qq", page=page)
          pass
        status['installed_OpenAI'] = True
      if prefs['install_TextSynth'] and not status['installed_TextSynth']:
        console_msg("Installing TextSynth GPT-J Libraries...")
        try:
          from textsynthpy import TextSynth, Complete
        except ImportError as e:
          run_process("pip install textsynthpy -qq", page=page)
          
        status['installed_TextSynth'] = True
      #print('Done Installing...')
      if prefs['enable_sounds']: page.snd_done.play()
      console_clear()
      page.banner.open = False
      page.banner.update()
      page.update()
      install_diffusers.update()
      #install_text2img.update()
      #install_img2img.update()
      install_Stability_api.update()
      install_CLIP_guided.update()
      install_ESRGAN.update()
      install_OpenAI.update()
      install_TextSynth.update()
      update_parameters(page)
      page.Parameters.content.update()
      #page.Parameters.updater()
      page.Installers.content.update()
      page.Installers.update()
      page.tabs.selected_index = 2
      page.tabs.update()
      page.update()

  install_button = ElevatedButton(content=Text(value="⏬   Run Installations", size=20), on_click=run_installers)
  #image_output = TextField(label="Image Output Path", value=prefs['image_output'], on_change=changed)
  c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text ("📥  Stable Diffusion Required & Optional Installers", style="titleLarge"),
        Divider(thickness=1, height=4),
        install_diffusers,
        diffusers_settings,
        #install_text2img,
        #install_img2img,
        install_Stability_api,
        stability_settings,
        #install_CLIP_guided,
        #clip_settings,
        install_ESRGAN,
        install_OpenAI,
        install_TextSynth,
        install_button,
      ], scroll="auto",
  ))
  def init_boxes():
    diffusers_settings.height = None if prefs['install_diffusers'] else 0
    stability_settings.height = None if prefs['install_Stability_api'] else 0
    clip_settings.height = None if prefs['install_CLIP_guided'] else 0
    diffusers_settings.update()
    stability_settings.update()
    clip_settings.update()
    page.update()
  #init_boxes()
  return c

def update_parameters(page):
  page.img_block.height = None if status['installed_img2img'] or status['installed_megapipe'] or status['installed_stability'] else 0
  page.clip_block.height = None if status['installed_clip'] else 0
  page.ESRGAN_block.height = None if status['installed_ESRGAN'] else 0
  page.img_block.update()
  page.clip_block.update()
  page.ESRGAN_block.update()
  page.Parameters.update()
  #print("Updated Parameters")

if is_Colab:
    from google.colab import files
def buildParameters(page):
  def changed(e, pref=None, asInt=False):
      if pref is not None:
        prefs[pref] = e.control.value if not asInt else int(e.control.value)
      if not status['changed_parameters']:
        apply_changes_button.visible = len(prompts) > 0
        apply_changes_button.update()
      status['changed_parameters'] = True
      #page.update()
  def run_parameters(e):
      save_parameters()
      #page.tabs.current_tab = 3
      page.tabs.selected_index = 3
      page.tabs.update()
      page.update()
  def save_parameters():
      update_args()
      page.update_prompts()
      save_settings_file(page)
      status['changed_parameters'] = False
  def apply_to_prompts(e):
      update_args()
      page.apply_changes(e)
      apply_changes_button.visible = False
      apply_changes_button.update()
  def pick_files_result(e: FilePickerResultEvent):
      # TODO: This is not working on Colab, maybe it can get_upload_url on other platform?
      if e.files:
        img = e.files
        uf = []
        fname = img[0]
        #print(os.path.join(fname.path, fname.name))
        #src_path = os.path.join(fname.path, fname.name)
        src_path = page.get_upload_url(fname.name, 600),
        uf.append(FilePickerUploadFile(fname.name, upload_url=src_path))
        pick_files_dialog.upload(uf)
        print(str(src_path))
        #src_path = ''.join(src_path)
        print(str(uf[0]))
        dst_path = os.path.join(root_dir, fname.name)
        print(f'Copy {src_path} to {dst_path}')
        #shutil.copy(src_path, dst_path)
        # TODO: is init or mask?
        init_image.value = dst_path
      #selected_files.value = (", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!")
      #selected_files.update()

  pick_files_dialog = FilePicker(on_result=pick_files_result)
  page.overlay.append(pick_files_dialog)
  #selected_files = Text()

  #page.overlay.append(pick_files_dialog)
  def pick_init(e):
      if False:
      #if is_Colab:
          # Not the best solution because you need to press Browse from Colab side
          uploaded = files.upload()
          for filename in uploaded.keys():
            if not os.path.isfile(filename):
              #print("Skipping " + filename)
              continue
            fname = filename.rpartition('/')[2] if '/' in filename else filename
            dst_path = os.path.join(root_dir, fname)
            #print(f'Copy {filename} to {dst_path}')
            shutil.copy(filename, dst_path)
            if e.control.label == "Init Image":
              init_image.value = dst_path
              init_image.update()
            elif e.control.label == "Mask Image":
              mask_image.value = dst_path
              mask_image.update()
      else:
          pick_files_dialog.pick_files(allow_multiple=False)
  def toggle_ESRGAN(e):
      ESRGAN_settings.height = None if e.control.value else 0
      prefs['apply_ESRGAN_upscale'] = e.control.value
      ESRGAN_settings.update()
      has_changed = True
  def change_guidance(e):
      guidance_value.value = f" {e.control.value}"
      guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      guidance.update()
      changed(e, 'guidance_scale')
  def change_width(e):
      width_slider.controls[1].value = f" {int(e.control.value)}px"
      width_slider.update()
      changed(e, 'width', asInt=True)
  def change_height(e):
      height_slider.controls[1].value = f" {int(e.control.value)}px"
      height_slider.update()
      changed(e, 'height', asInt=True)
  def toggle_interpolation(e):
      interpolation_steps_slider.height = None if e.control.value else 0
      changed(e, 'use_interpolation')
      interpolation_steps_slider.update()
  def change_interpolation_steps(e):
      interpolation_steps_value.value = f" {int(e.control.value)} steps"
      interpolation_steps_value.update()
      changed(e, 'num_interpolation_steps', asInt=True)
  def change_enlarge_scale(e):
      enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
      enlarge_scale_slider.update()
      changed(e, 'enlarge_scale')
  def change_strength(e):
      strength_value.value = f" {int(e.control.value * 100)}"
      strength_value.update()
      guidance.update()
      changed(e, 'init_image_strength')
  has_changed = False
  batch_folder_name = TextField(label="Batch Folder Name", value=prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
  batch_size = TextField(label="Batch Size", value=prefs['batch_size'], keyboard_type="number", on_change=lambda e:changed(e,'batch_size'))
  n_iterations = TextField(label="Number of Iterations", value=prefs['n_iterations'], keyboard_type="number", on_change=lambda e:changed(e,'n_iterations'))
  steps = TextField(label="Steps", value=prefs['steps'], keyboard_type="number", on_change=lambda e:changed(e,'steps', asInt=True))
  eta = TextField(label="DDIM ETA", value=prefs['eta'], keyboard_type="number", on_change=lambda e:changed(e,'eta'))
  seed = TextField(label="Seed", value=prefs['seed'], keyboard_type="number", on_change=lambda e:changed(e,'seed'))
  param_rows = Row([Column([batch_folder_name, batch_size, n_iterations]), Column([steps, eta, seed])])
  guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=prefs['guidance_scale'], on_change=change_guidance, expand=True)
  guidance_value = Text(f" {prefs['guidance_scale']}", weight="bold")
  guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
  width = Slider(min=256, max=1280, divisions=16, label="{value}px", value=prefs['width'], on_change=change_width, expand=True)
  width_value = Text(f" {int(prefs['width'])}px", weight="bold")
  width_slider = Row([Text(f"Width: "), width_value, width])
  height = Slider(min=256, max=1280, divisions=16, label="{value}px", value=prefs['height'], on_change=change_height, expand=True)
  height_value = Text(f" {int(prefs['height'])}px", weight="bold")
  height_slider = Row([Text(f"Height: "), height_value, height])

  init_image = TextField(label="Init Image", value=prefs['init_image'], on_change=lambda e:changed(e,'init_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
  mask_image = TextField(label="Mask Image", value=prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_init))
  init_image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=prefs['init_image_strength'], on_change=change_strength, expand=True)
  strength_value = Text(f" {int(prefs['init_image_strength'] * 100)}%", weight="bold")
  strength_slider = Row([Text("Init Image Strength: "), strength_value, init_image_strength])
  centipede_prompts_as_init_images = Checkbox(label="Centipede Prompts as Init Images", value=prefs['centipede_prompts_as_init_images'], on_change=lambda e:changed(e,'centipede_prompts_as_init_images'))
  use_interpolation = Switch(label="Use Interpolation to Walk Latent Space between Prompts", value=prefs['use_interpolation'], on_change=toggle_interpolation)
  interpolation_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=prefs['num_interpolation_steps'], on_change=change_interpolation_steps, expand=True)
  interpolation_steps_value = Text(f" {int(prefs['num_interpolation_steps'])} steps", weight="bold")
  interpolation_steps_slider = Container(Row([Text(f"Number of Interpolation Steps between Prompts: "), interpolation_steps_value, interpolation_steps]), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  Row([Text(f"Number of Interpolation Steps between Prompts: "), interpolation_steps_value, interpolation_steps])
  if not bool(prefs['use_interpolation']):
    interpolation_steps_slider.height = 0
  page.interpolation_block = Column([use_interpolation, interpolation_steps_slider])
  if not status['installed_interpolation']:
    page.interpolation_block.visible = False
  page.img_block = Container(Column([Row([init_image, mask_image]), strength_slider, centipede_prompts_as_init_images, Divider(height=9, thickness=2)]), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  use_clip_guided_model = Checkbox(label="Use CLIP-Guided Model", value=prefs['use_clip_guided_model'], on_change=lambda e:changed(e,'use_clip_guided_model'))
  clip_guidance_scale = Slider(min=1, max=5000, divisions=5000, label="{value}", value=prefs['clip_guidance_scale'], on_change=lambda e:changed(e,'clip_guidance_scale'), expand=True)
  clip_guidance_scale_slider = Row([Text("CLIP Guidance Scale: "), clip_guidance_scale])
  use_cutouts = Checkbox(label="Use Cutouts", value=prefs['use_cutouts'], on_change=lambda e:changed(e,'use_cutouts'))
  num_cutouts = TextField(label="Number of Cutouts", value=prefs['num_cutouts'], keyboard_type="number", on_change=lambda e:changed(e,'num_cutouts', asInt=True))
  unfreeze_unet = Checkbox(label="Unfreeze UNET", value=prefs['unfreeze_unet'], on_change=lambda e:changed(e,'unfreeze_unet'))
  unfreeze_vae = Checkbox(label="Unfreeze VAE", value=prefs['unfreeze_vae'], on_change=lambda e:changed(e,'unfreeze_vae'))
  page.clip_block = Container(Column([use_clip_guided_model, clip_guidance_scale_slider, use_cutouts, unfreeze_unet, unfreeze_vae, Divider(height=9, thickness=2)]), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=prefs['apply_ESRGAN_upscale'], on_change=toggle_ESRGAN)
  enlarge_scale_value = Text(f" {float(prefs['enlarge_scale'])}x", weight="bold")
  enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
  enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
  face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=prefs['face_enhance'], on_change=lambda e:changed(e,'face_enhance'))
  display_upscaled_image = Checkbox(label="Display Upscaled Image", value=prefs['display_upscaled_image'], on_change=lambda e:changed(e,'display_upscaled_image'))
  ESRGAN_settings = Container(Column([enlarge_scale_slider, face_enhance, display_upscaled_image], spacing=0), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  page.ESRGAN_block = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, "bounceOut"), clip_behavior="hardEdge")
  page.img_block.height = None if status['installed_img2img'] or status['installed_stability'] else 0
  page.clip_block.height = None if status['installed_clip'] else 0
  page.ESRGAN_block.height = None if status['installed_ESRGAN'] else 0
  if not prefs['apply_ESRGAN_upscale']:
    ESRGAN_settings.height = 0
  parameters_button = ElevatedButton(content=Text(value="📜   Continue to Image Prompts", size=20), on_click=run_parameters)
  apply_changes_button = ElevatedButton(content=Text(value="🔀   Apply Changes to Current Prompts", size=20), on_click=apply_to_prompts)
  apply_changes_button.visible = len(prompts) > 0 and status['changed_parameters']
  parameters_row = Row([parameters_button, apply_changes_button], alignment="spaceBetween")
  def updater():
      #parameters.update()
      c.update()
      page.update()
      #print("Updated Parameters Page")

  c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text ("📝  Stable Diffusion Image Parameters", style="titleLarge"),
        Divider(thickness=1, height=4),
        param_rows, guidance, width_slider, height_slider, #Divider(height=9, thickness=2), 
        page.interpolation_block, page.img_block, page.clip_block, page.ESRGAN_block,
        #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
        parameters_row,
      ], scroll="auto",
  ))#batch_folder_name, batch_size, n_iterations, steps, eta, seed, 
  return c

prompts = []
args = {}

def update_args():
    global args
    args = {
        "batch_size": int(prefs['batch_size']),
        "n_iterations":int(prefs['n_iterations']),
        "steps":int(prefs['steps']),
        "eta":float(prefs['eta']),
        "width":int(prefs['width']),
        "height":int(prefs['height']),
        "guidance_scale":float(prefs['guidance_scale']),
        "seed":int(prefs['seed']),
        "precision":prefs['precision'],
        "init_image": prefs['init_image'],
        "init_image_strength": prefs['init_image_strength'],
        "mask_image": prefs['mask_image'],
        "prompt2": None,
        "tweens": 10,
        "negative_prompt": None,
        "use_clip_guided_model": prefs['use_clip_guided_model'],
        "clip_prompt": "",
        "clip_guidance_scale": float(prefs['clip_guidance_scale']),
        "use_cutouts": prefs['use_cutouts'],
        "num_cutouts": int(prefs['num_cutouts']),
        "unfreeze_unet": prefs['unfreeze_unet'],
        "unfreeze_vae": prefs['unfreeze_vae'],
        "use_Stability": False,
    }
update_args()

class Dream: 
    def __init__(self, prompt, **kwargs):
        self.prompt = prompt
        self.arg = args.copy()
        for key, value in kwargs.items():
          if key=='arg': self.arg = value
          elif key=="batch_size": self.arg[key] = int(value)
          elif key=="n_iterations": self.arg[key] = int(value)
          elif key=="steps": self.arg[key] = int(value)
          elif key=="eta": self.arg[key] = float(value)
          elif key=="width": self.arg[key] = int(value)
          elif key=="height": self.arg[key] = int(value)
          elif key=="guidance_scale": self.arg[key] = float(value)
          elif key=="seed": self.arg[key] = int(value)
          elif key=="precision": self.arg[key] = value
          elif key=="init_image": self.arg[key] = value
          elif key=="init_image_strength": self.arg[key] = value
          elif key=="mask_image": self.arg[key] = value
          elif key=="prompt2": self.arg[key] = value
          elif key=="tweens": self.arg[key] = int(value)
          elif key=="negative_prompt": self.arg[key] = value
          elif key=="clip_prompt": self.arg[key] = value
          elif key=="use_clip_guided_model": self.arg[key] = value
          elif key=="clip_guidance_scale": self.arg[key] = float(value)
          elif key=="use_cutouts": self.arg[key] = value
          elif key=="num_cutouts": self.arg[key] = int(value)
          elif key=="unfreeze_unet": self.arg[key] = value
          elif key=="unfreeze_vae": self.arg[key] = value
          elif key=="use_Stability": self.arg[key] = value
          elif key=="prompt": self.prompt = value
          else: print(f"{Color.RED2}Unknown argument: {key} = {value}{Color.END}")
        #self.arg = arg
    #arg = args
#print(str(args))
import string
from collections import ChainMap
def format_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    if not prefs['file_allowSpace']: filename = filename.replace(' ','_')
    return filename[:int(prefs['file_max_length'])]

def merge_dict(*dicts):
    all_keys  = set(k for d in dicts for k in d.keys())
    chain_map = ChainMap(*reversed(dicts))
    return {k: chain_map[k] for k in all_keys}
import copy

def buildPromptsList(page):
  parameter = Ref[ListTile]()
  def changed(e):
      status['changed_prompts'] = True
      page.update()
  
  def edit_prompt(e):
      idx = prompts.index(e.control.data)
      open_dream = e.control.data
      def changed_tweening(e):
          status['changed_prompts'] = True
          tweening_params.height = None if e.control.value else 0
          tweening_params.update()
          #prompt2.visible = e.control.value
          #tweens.visible = e.control.value
          prompt_tweening = e.control.value
          page.update()
      def close_dlg(e):
          dlg_modal.open = False
          page.update()
      def save_dlg(e):
          dream = open_dream #e.control.data
          dream.prompt = edit_text.value
          arg['batch_size'] = int(batch_size.value)
          arg['n_iterations'] = int(n_iterations.value)
          arg['steps'] = int(steps.value)
          arg['eta'] = float(eta.value)
          arg['seed'] = int(seed.value)
          arg['guidance_scale'] = float(guidance_scale.value)
          arg['width'] = int(width.value)
          arg['height'] = int(height.value)
          arg['init_image'] = init_image.value
          arg['mask_image'] = mask_image.value
          arg['init_image_strength'] = float(init_image_strength.value)
          arg['prompt2'] = prompt2.value if bool(use_prompt_tweening.value) else None
          arg['tweens'] = int(tweens.value)
          arg['negative_prompt'] = negative_prompt.value if bool(negative_prompt.value) else None
          dream.arg = arg
          diffs = arg_diffs(arg, args)
          if bool(diffs):
            prompts_list.controls[idx].subtitle = Text("    " + diffs)
          else:
            prompts_list.controls[idx].subtitle = None
          prompts_list.controls[idx].title.value = dream.prompt # = Text(edit_text.value)
          status['changed_prompts'] = True
          dlg_modal.open = False
          page.update()
      arg = open_dream.arg #e.control.data.arg
      edit_text = TextField(label="Prompt Text", expand=3, value=open_dream.prompt, multiline=True)
      negative_prompt = TextField(label="Negative Prompt Text", expand=1, value=str((arg['negative_prompt'] or '') if 'negative_prompt' in arg else ''), on_change=changed)
      #batch_folder_name = TextField(label="Batch Folder Name", value=arg['batch_folder_name'], on_change=changed)
      #print(str(arg))
      prompt_tweening = bool(arg['prompt2']) if 'prompt2' in arg else False
      use_prompt_tweening = Switch(label="Prompt Tweening", value=prompt_tweening, on_change=changed_tweening)
      prompt2 = TextField(label="Prompt 2 Transition Text", expand=True, value=arg['prompt2'] if 'prompt2' in arg else '', on_change=changed)
      tweens = TextField(label="# of Tweens", value=str(arg['tweens'] if 'tweens' in arg else 8), keyboard_type="number", on_change=changed, width = 90)
      #prompt2.visible = prompt_tweening
      #tweens.visible = prompt_tweening
      tweening_params = Container(Row([Container(content=None, width=8), prompt2, tweens]), animate_size=animation.Animation(1000, "easeOut"), clip_behavior="hardEdge")
      tweening_params.height = None if prompt_tweening else 0
      tweening_row = Row([use_prompt_tweening, ])#tweening_params

      batch_size = TextField(label="Batch Size", value=str(arg['batch_size']), keyboard_type="number", on_change=changed)
      n_iterations = TextField(label="Number of Iterations", value=str(arg['n_iterations']), keyboard_type="number", on_change=changed)
      steps = TextField(label="Steps", value=str(arg['steps']), keyboard_type="number", on_change=changed)
      eta = TextField(label="DDIM ETA", value=str(arg['eta']), keyboard_type="number", hint_text="Amount of Noise (only with DDIM sampler)", on_change=changed)
      seed = TextField(label="Seed", value=str(arg['seed']), keyboard_type="number", hint_text="0 or -1 picks a Random seed", on_change=changed)
      guidance_scale = TextField(label="Guidance Scale", value=str(arg['guidance_scale']), keyboard_type="number", on_change=changed)
      param_columns = Row([Column([batch_size, n_iterations, steps]), Column([guidance_scale, seed, eta])])
      #guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=arg['guidance_scale'], expand=True)
      #guidance = Row([Text("Guidance Scale: "), guidance_scale])
      width = Slider(min=256, max=1280, divisions=16, label="{value}px", value=float(arg['width']), expand=True)
      width_slider = Row([Text("Width: "), width])
      height = Slider(min=256, max=1280, divisions=16, label="{value}px", value=float(arg['height']), expand=True)
      height_slider = Row([Text("Height: "), height])
      init_image = TextField(label="Init Image", value=arg['init_image'], on_change=changed, height=50)
      mask_image = TextField(label="Mask Image", value=arg['mask_image'], on_change=changed, height=40)
      init_image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=float(arg['init_image_strength']), expand=True)
      strength_slider = Row([Text("Init Image Strength: "), init_image_strength])
      img_block = Column([init_image, mask_image, strength_slider])
      dlg_modal = AlertDialog(
          modal=False,
          title=Text("📝  Edit Prompt Dream Parameters"),
          #content=Container(
          content=Container(Column([
            Container(content=None, height=7),
            Row([
              edit_text,
              negative_prompt,
            ]),
            #Text("Override any Default Parameters"),
            tweening_row,
            tweening_params,
            #batch_size, n_iterations, steps, eta, seed, guidance, 
            param_columns, 
            width_slider, height_slider, (img_block if (status['installed_img2img'] or status['installed_stability']) else Container(content=None))
            #Row([Column([batch_size, n_iterations, steps, eta, seed,]), Column([guidance, width_slider, height_slider, Divider(height=9, thickness=2), (img_block if prefs['install_img2img'] else Container(content=None))])],),
            ], alignment="start", tight=True, width=page.width - 240, height=page.height - 100, scroll="auto"), width=page.width - 240, height=page.height - 100),
          actions=[
              TextButton("Cancel", on_click=close_dlg),
              ElevatedButton(content=Text(value="💾  Save Prompt ", size=19, weight="bold"), on_click=save_dlg),
          ],
          actions_alignment="end",
          #on_dismiss=lambda e: print("Modal dialog dismissed!"),
      )
      page.dialog = dlg_modal
      dlg_modal.open = True
      page.update()
      
  def delete_prompt(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      idx = prompts.index(e.control.data)
      prompts.pop(idx)
      prompts_list.controls.pop(idx)
      prompts_list.update()
      status['changed_prompts'] = True
  def duplicate_prompt(e):
      #print("Duplicate " + str(e.control))
      idx = prompts.index(e.control.data)
      new_dream = copy.copy(e.control.data)
      prompts.insert(idx, new_dream)
      diffs = arg_diffs(e.control.data.arg, args)
      subtitle = None
      if bool(diffs): subtitle = Text("    " + diffs)
      prompts_list.controls.insert(idx, ListTile(title=Text(new_dream.prompt, max_lines=3, style="bodyLarge"), dense=True, data=new_dream, subtitle=subtitle, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[
              PopupMenuItem(icon=icons.EDIT, text="Edit Prompt", on_click=edit_prompt, data=new_dream),
              PopupMenuItem(icon=icons.DELETE, text="Delete Prompt", on_click=delete_prompt, data=new_dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Prompt", on_click=duplicate_prompt, data=new_dream),
              PopupMenuItem(icon=icons.ARROW_UPWARD, text="Move Up", on_click=move_up, data=new_dream),
              PopupMenuItem(icon=icons.ARROW_DOWNWARD, text="Move Down", on_click=move_down, data=new_dream),
          ],
      )))
      prompts_list.update()
      status['changed_prompts'] = True
  def move_down(e):
      idx = prompts.index(e.control.data)
      if idx < (len(prompts) - 1):
        d = prompts.pop(idx)
        prompts.insert(idx+1, d)
        dr = prompts_list.controls.pop(idx)
        prompts_list.controls.insert(idx+1, dr)
        prompts_list.update()
  def move_up(e):
      idx = prompts.index(e.control.data)
      if idx > 0:
        d = prompts.pop(idx)
        prompts.insert(idx-1, d)
        dr = prompts_list.controls.pop(idx)
        prompts_list.controls.insert(idx-1, dr)
        prompts_list.update()
  def add_prompt(e):
      add_to_prompts(prompt_text.value)
  def add_to_prompts(p, arg=None):
      dream = Dream(p)
      if arg is not None:
        if 'prompt' in arg: del arg['prompt']
        arg = merge_dict(arg, args)
        dream.arg = arg
      prompts.append(dream)
      prompts_list.controls.append(ListTile(title=Text(p, max_lines=3, style="bodyLarge"), dense=True, data=dream, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[
              PopupMenuItem(icon=icons.EDIT, text="Edit Prompt", on_click=edit_prompt, data=dream),
              PopupMenuItem(icon=icons.DELETE, text="Delete Prompt", on_click=delete_prompt, data=dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Prompt", on_click=duplicate_prompt, data=dream),
              PopupMenuItem(icon=icons.ARROW_UPWARD, text="Move Up", on_click=move_up, data=dream),
              PopupMenuItem(icon=icons.ARROW_DOWNWARD, text="Move Down", on_click=move_down, data=dream),
          ],
      )))
      #prompts_list.controls.append(Text("Prompt 1 added to the list of prompts"))
      prompts_list.update()
      if prompts_buttons.visible==False:
          prompts_buttons.visible=True
          prompts_buttons.update()
      if arg is not None:
        update_prompts()
      else:
        prompt_text.focus()
      page.update()
      status['changed_prompts'] = True
  page.add_to_prompts = add_to_prompts

  def save_prompts():
      if len(prompts) > 0:
          #print("Saving your Prompts List")
          prompts_prefs = []
          for d in prompts:
            a = d.arg
            a['prompt'] = d.prompt
            if 'batch_size' in a: del a['batch_size']
            if 'n_iterations' in a: del a['n_iterations']
            if 'precision' in a: del a['precision']
            #a['prompt'] = pr[0] if type(pr) == list else pr
            a['sampler'] = prefs['generation_sampler'] if prefs['use_Stability_api'] else prefs['scheduler_mode']
            if prefs['use_Stability_api']: del a['eta']
            if 'use_Stability' in a: del a['use_Stability']
            if 'negative_prompt' in a:
              if not bool(a['negative_prompt']): del a['negative_prompt']
            if 'prompt2' in a:
              if not bool(a['prompt2']):
                del a['prompt2']
                del a['tweens']
            if not bool(a['init_image']):
              del a['init_image']
              del a['init_image_strength']
            if not bool(a['mask_image']):
              del a['mask_image']
            if not bool(a['use_clip_guided_model']):
              del a["use_clip_guided_model"]
              del a["clip_prompt"]
              del a["clip_guidance_scale"]
              del a["num_cutouts"]
              del a["use_cutouts"]
              del a["unfreeze_unet"]
              del a["unfreeze_vae"]
            else:
              a["clip_model_id"] = prefs['clip_model_id']

            prompts_prefs.append(a)
            #j = json.dumps(a)
          prefs['prompts'] = prompts_prefs
  page.save_prompts = save_prompts
  def load_prompts():
      saved_prompts = prefs['prompts']
      if len(saved_prompts) > 1:
          for d in saved_prompts:
            #print(f'Loading {d}')
            if 'prompt' not in d: continue
            #dream = Dream(d['prompt'])
            p = d['prompt']
            #del d['prompt']
            page.add_to_prompts(p, d)
            #dream.arg = d
            #prompts.append(dream)
            #prompts_list.controls.append(ListTile(title=Text(dream.prompt, max_lines=3, style="bodyLarge"), dense=True, data=dream, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
            #  items=[
            #      PopupMenuItem(icon=icons.EDIT, text="Edit Prompt", on_click=edit_prompt, data=dream),
            #      PopupMenuItem(icon=icons.DELETE, text="Delete Prompt", on_click=delete_prompt, data=dream),
            #      PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Prompt", on_click=duplicate_prompt, data=dream),
            #  ],
            #)))
          #prompts_list.update()
          #prompts_buttons.visible=True
          #prompts_buttons.update()
          #update_prompts()
          page.update()

  page.load_prompts = load_prompts

  def update_prompts():
      #print("Update prompts")
      if len(prompts_list.controls) > 0:
        for p in prompts_list.controls:
          diffs = arg_diffs(p.data.arg, args)
          if bool(diffs):
            subtitle = Text("    " + diffs)
          else: subtitle = None
          p.subtitle = subtitle
          p.update()
        prompts_list.update()
  page.update_prompts = update_prompts
  def apply_changes(e):
      if len(prompts_list.controls) > 0:
        i = 0
        for p in prompts_list.controls:
          prompts[i].arg = merge_dict(prompts[i].arg, args)
          p.data = prompts[i]
          i += 1
        update_prompts()
  page.apply_changes = apply_changes
  def clear_prompt(e):
      prompt_text.value = ""
      prompt_text.update()
  def clear_list(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      prompts_list.controls = []
      prompts = []
      prefs['prompts'] = []
      prompts_list.update()
      prompts_buttons.visible=False
      prompts_buttons.update()
      status['changed_prompts'] = True
  def on_keyboard (e: KeyboardEvent):
      if e.key == "Escape":
        clear_prompt(None)
  page.on_keyboard_event = on_keyboard
  def run_diffusion(e):
      if not status['installed_diffusers'] and not status['installed_stability']:
        alert_msg(e.page, "You must Install the required Diffusers or Stability api first...")
        return
      if prefs['use_interpolation'] and prefs['install_interpolation'] and not status['installed_interpolation']:
        alert_msg(e.page, "You must Install Walk Interpolation Pipeline first...")
        return
      page.tabs.selected_index = 4
      page.tabs.update()
      if status['changed_prompts']:
        page.save_prompts()
        save_settings_file(page)
        status['changed_prompts'] = False
      page.update()
      start_diffusion(page)
  has_changed = False
  prompts_list = Column([],spacing=1)
  prompt_text = TextField(label="Prompt Text", expand=True, suffix=IconButton(icons.CLEAR, on_click=clear_prompt), autofocus=True, on_submit=add_prompt)
  add_prompt_button = ElevatedButton(content=Text(value="➕  Add Prompt", size=17, weight="bold"), on_click=add_prompt)
  prompt_row = Row([prompt_text, add_prompt_button])
  diffuse_prompts_button = ElevatedButton(content=Text(value="▶️    Run Diffusion on Prompts ", size=20), on_click=run_diffusion)
  clear_prompts_button = ElevatedButton("❌   Clear Prompts List", on_click=clear_list)
  prompts_buttons = Row([diffuse_prompts_button, clear_prompts_button], alignment="spaceBetween")
  #page.load_prompts()
  if len(prompts_list.controls) < 1:
    prompts_buttons.visible=False
  c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text("🗒️   List of Prompts to Diffuse", style="titleLarge"),
        Divider(thickness=1, height=4),
        #add_prompt_button,
        prompt_row,
        prompts_list,
        prompts_buttons,
      ], scroll="auto",
  ))
  return c

def buildImages(page):
    auto_scroll = True
    def auto_scrolling(auto):
      page.imageColumn.auto_scroll = auto
      page.imageColumn.update()
      c.update()
    page.auto_scrolling = auto_scrolling
    page.imageColumn = Column([
        Text("▶️   Get ready to make your images, run from Prompts List", style="titleLarge"),
        Divider(thickness=1, height=4),
      ], scroll="auto", auto_scroll=True
    )
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=page.imageColumn)
    return c

def buildPromptHelpers(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs[pref] = e.control.value
      status['changed_prompt_helpers'] = True
    page.generator = buildPromptGenerator(page)
    page.remixer = buildPromptRemixer(page)
    page.brainstormer = buildPromptBrainstormer(page)
    page.writer = buildPromptWriter(page)
    promptTabs = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(text="Prompt Generator", content=page.generator, icon=icons.CLOUD),
            Tab(text="Prompt Remixer", content=page.remixer, icon=icons.CLOUD_SYNC_ROUNDED),
            Tab(text="Prompt Brainstormer", content=page.brainstormer, icon=icons.CLOUDY_SNOWING),
            Tab(text="Prompt Writer", content=page.writer, icon=icons.CLOUD_CIRCLE),
        ],
        expand=1,
        #on_change=tab_on_change
    )
    return promptTabs

def buildPromptGenerator(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs['prompt_generator'][pref] = e.control.value
      status['changed_prompt_generator'] = True
    page.prompt_generator_list = Column([], spacing=0)
    def add_to_prompt_generator(p):
      page.prompt_generator_list.controls.append(ListTile(title=Text(p, max_lines=3, style="bodyLarge"), dense=True, on_click=lambda _: page.add_to_prompts(p)))
      page.prompt_generator_list.update()
      generator_list_buttons.visible = True
      generator_list_buttons.update()
    page.add_to_prompt_generator = add_to_prompt_generator
    def click_prompt_generator(e):
      if status['installed_OpenAI']:
        run_prompt_generator(page)
      else:
        alert_msg(page, "You must Install OpenAI GPT-3 Library first before using...")
    def add_to_list(e):
      for p in page.prompt_generator_list.controls:
        page.add_to_prompts(p.title.value)
    def clear_prompts(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.prompt_generator_list.controls = []
      page.prompt_generator_list.update()
      prompts = []
      generator_list_buttons.visible = False
      generator_list_buttons.update()
    def changed_request(e):
      request_slider.label = generator_request_modes[int(request_slider.value)]
      request_slider.update()
      changed(e, 'request_mode')
    request_slider = Slider(label="{value}", min=0, max=7, divisions=7, expand=True, value=prefs['prompt_generator']['request_mode'], on_change=changed_request)
    generator_list_buttons = Row([ElevatedButton(content=Text("➕  Add All Prompts to List", size=18), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment="spaceBetween")
    if len(page.prompt_generator_list.controls) < 1:
      generator_list_buttons.visible = False
      #generator_list_buttons.update()
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text("🧠  OpenAI Prompt Genenerator", style="titleLarge"),
        Text("Enter a phrase each prompt should start with and the amount of prompts to generate. 'Subject Details' is optional to influence the output. 'Phase as subject' makes it about phrase and subject detail. 'Request mode' is the way it asks for the visual description. Just experiment, AI will continue to surprise.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([TextField(label="Subject Phrase", expand=True, value=prefs['prompt_generator']['phrase'], on_change=lambda e: changed(e, 'phrase')), TextField(label="Subject Detail", expand=True, hint_text="Optional about detail", value=prefs['prompt_generator']['subject_detail'], on_change=lambda e: changed(e, 'subject_detail')), Checkbox(label="Phrase as Subject", value=prefs['prompt_generator']['phrase_as_subject'], on_change=lambda e: changed(e, 'phrase_as_subject'))]),
        Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_generator']['amount'], on_change=lambda e: changed(e, 'amount')),
             NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_generator']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),
             NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_generator']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
             Checkbox(label="Permutate Artists", value=prefs['prompt_generator']['permutate_artists'], on_change=lambda e: changed(e, 'permutate_artists'))], alignment="spaceBetween"),        
        Row([Text("Request Mode:"), request_slider, Text(" AI Temperature:"), Slider(label="{value}", min=0, max=1, divisions=10, expand=True, value=prefs['prompt_generator']['AI_temperature'], on_change=lambda e: changed(e, 'AI_temperature'))]),
        ElevatedButton(content=Text("💭   Generate Prompts", size=18), on_click=click_prompt_generator),
        page.prompt_generator_list,
        generator_list_buttons,
      ], scroll="auto",
    ))
    return c

def buildPromptRemixer(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs['prompt_remixer'][pref] = e.control.value
      status['changed_prompt_remixer'] = True
    page.prompt_remixer_list = Column([], spacing=0)
    def click_prompt_remixer(e):
      if status['installed_OpenAI']:
        run_prompt_remixer(page)
      else:
        alert_msg(page, "You must Install OpenAI GPT-3 Library first before using...")
    def add_to_prompt_remixer(p):
      page.prompt_remixer_list.controls.append(ListTile(title=Text(p, max_lines=3, style="bodyLarge"), dense=True, on_click=lambda _: page.add_to_prompts(p)))
      page.prompt_remixer_list.update()
      remixer_list_buttons.visible = True
      remixer_list_buttons.update()
    page.add_to_prompt_remixer = add_to_prompt_remixer
    def add_to_list(e):
      for p in page.prompt_remixer_list.controls:
        page.add_to_prompts(p.title.value)
    def clear_prompts(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.prompt_remixer_list.controls = []
      page.prompt_remixer_list.update()
      remixer_list_buttons.visible = False
      remixer_list_buttons.update()
    def changed_request(e):
      request_slider.label = remixer_request_modes[int(request_slider.value)]
      request_slider.update()
      changed(e, 'request_mode')
    request_slider = Slider(label="{value}", min=0, max=8, divisions=8, expand=True, value=prefs['prompt_remixer']['request_mode'], on_change=changed_request)
    remixer_list_buttons = Row([ElevatedButton(content=Text("Add All Prompts to List", size=18), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment="spaceBetween")
    if len(page.prompt_remixer_list.controls) < 1:
      remixer_list_buttons.visible = False
    
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Row([Text("🔄  Prompt Remixer - GPT-3 AI Helper", style="titleLarge"), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page))], alignment="spaceBetween"),
        Text("Enter a complete prompt you've written that is well worded and descriptive, and get variations of it with our AI friend. Experiment.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([TextField(label="Seed Prompt", expand=True, value=prefs['prompt_remixer']['seed_prompt'], on_change=lambda e: changed(e, 'seed_prompt')), TextField(label="Optional About Detail", expand=True, hint_text="Optional about detail", value=prefs['prompt_remixer']['optional_about_influencer'], on_change=lambda e: changed(e, 'optional_about_influencer'))]),
        Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_remixer']['amount'], on_change=lambda e: changed(e, 'amount')),
             NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_remixer']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),
             NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_remixer']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
             Checkbox(label="Permutate Artists", value=prefs['prompt_remixer']['permutate_artists'], on_change=lambda e: changed(e, 'permutate_artists'))], alignment="spaceBetween"),
        Row([Text("Request Mode:"), request_slider, 
             Text(" AI Temperature:"), Slider(label="{value}", min=0, max=1, divisions=10, expand=True, value=prefs['prompt_remixer']['AI_temperature'], on_change=lambda e: changed(e, 'AI_temperature'))]),
        ElevatedButton(content=Text("🍹   Remix Prompts", size=18), on_click=click_prompt_remixer),
        page.prompt_remixer_list,
        remixer_list_buttons,
      ], scroll="auto",
    ))
    return c

def buildPromptBrainstormer(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs['prompt_brainstormer'][pref] = e.control.value
      status['changed_prompt_brainstormer'] = True
    def click_prompt_brainstormer(e):
      if prefs['prompt_brainstormer']['AI_engine'] == "OpenAI GPT-3":
        if status['installed_OpenAI']:
          run_prompt_brainstormer(page)
        else: alert_msg(page, "You must Install OpenAI GPT-3 Library first before using this Request Mode...")
      elif prefs['prompt_brainstormer']['AI_engine'] == "TextSynth GPT-J":
        if status['installed_TextSynth']:
          run_prompt_brainstormer(page)
        else: alert_msg(page, "You must Install TextSynth GPT-J Library first before using this Request Mode...")
      elif prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Bloom 176B":
        if bool(prefs['HuggingFace_api_key']):
          run_prompt_brainstormer(page)
        else: alert_msg(page, "You must provide your HuggingFace API Key in settings first before using this Request Mode...")
    page.prompt_brainstormer_list = Column([], spacing=0)
    def add_to_prompt_brainstormer(p):
      page.prompt_brainstormer_list.controls.append(Text(p, max_lines=3, style="bodyLarge", selectable=True))
      page.prompt_brainstormer_list.update()
      brainstormer_list_buttons.visible = True
      brainstormer_list_buttons.update()
    page.add_to_prompt_brainstormer = add_to_prompt_brainstormer
    def add_to_prompts(e):
      page.add_to_prompts(new_prompt_text.value)
    def clear_prompts(e):
      page.prompt_brainstormer_list.controls = []
      page.prompt_brainstormer_list.update()
      brainstormer_list_buttons.visible = False
      brainstormer_list_buttons.update()
    def clear_prompt_text(e):
      new_prompt_text.value = ""
      new_prompt_text.update()

    new_prompt_text = TextField(label="New Prompt Text", expand=True, suffix=IconButton(icons.CLEAR, on_click=clear_prompt_text), autofocus=True, on_submit=add_to_prompts)
    add_to_prompts_button = ElevatedButton("➕  Add to Prompts", icon=icons.ADD_ROUNDED, on_click=add_to_prompts)
    brainstormer_list_buttons = Row([
        new_prompt_text, add_to_prompts_button,
        ElevatedButton(content=Text("❌   Clear Brainstorms"), on_click=clear_prompts),
    ], alignment="end")
    
    if len(page.prompt_brainstormer_list.controls) < 1:
      brainstormer_list_buttons.visible = False
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Row([Text("🤔  Prompt Brainstormer - TextSynth GPT-J-6B, OpenAI GPT-3 & HuggingFace Bloom AI", style="titleLarge"), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page))], alignment="spaceBetween"),
        Text("Enter a complete prompt you've written that is well worded and descriptive, and get variations of it with our AI friends. Experiment, each has different personalities.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([Dropdown(label="AI Engine", width=250, options=[dropdown.Option("TextSynth GPT-J"), dropdown.Option("OpenAI GPT-3"), dropdown.Option("HuggingFace Bloom 176B")], value=prefs['prompt_brainstormer']['AI_engine'], on_change=lambda e: changed(e, 'AI_engine')),
          Dropdown(label="Request Mode", width=250, options=[dropdown.Option("Brainstorm"), dropdown.Option("Write"), dropdown.Option("Rewrite"), dropdown.Option("Edit"), dropdown.Option("Story"), dropdown.Option("Description"), dropdown.Option("Picture"), dropdown.Option("Raw Request")], value=prefs['prompt_brainstormer']['request_mode'], on_change=lambda e: changed(e, 'request_mode')),
        ], alignment="start"),
        Row([TextField(label="About Prompt", expand=True, value=prefs['prompt_brainstormer']['about_prompt'], on_change=lambda e: changed(e, 'about_prompt')),]),
        ElevatedButton(content=Text("⛈️    Brainstorm Prompt", size=18), on_click=lambda _: run_prompt_brainstormer(page)),
        page.prompt_brainstormer_list,
        brainstormer_list_buttons,
      ], scroll="auto",
    ))
    return c

def buildPromptWriter(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs['prompt_writer'][pref] = e.control.value
      status['changed_prompt_writer'] = True
    page.prompt_writer_list = Column([], spacing=0)
    def add_to_prompt_writer(p):
      page.prompt_writer_list.controls.append(ListTile(title=Text(p, max_lines=3, style="bodyLarge"), dense=True, on_click=lambda _: page.add_to_prompts(p)))
      page.prompt_writer_list.update()
      writer_list_buttons.visible = True
      writer_list_buttons.update()
    page.add_to_prompt_writer = add_to_prompt_writer

    def add_to_list(e):
      for p in page.prompt_writer_list.controls:
        page.add_to_prompts(p.title.value)
    def clear_prompts(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.prompt_writer_list.controls = []
      page.prompt_writer_list.update()
      writer_list_buttons.visible = False
      writer_list_buttons.update()
    writer_list_buttons = Row([ElevatedButton(content=Text("➕  Add All Prompts to List", size=18), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment="spaceBetween")
    if len(page.prompt_writer_list.controls) < 1:
      writer_list_buttons.visible = False

    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Row([Text("📜 Advanced Prompt Writer with NSP random variables ", style="titleLarge"), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page)),]),
        Text("Construct your Stable Diffusion Art descriptions easier, with all the extras you need to engineer perfect prompts faster. Note, you don't have to use any randoms if you rather do all custom.", style="titleSmall"),
        Divider(thickness=1, height=5),
        TextField(label="Arts Subjects", value=prefs['prompt_writer']['art_Subjects'], on_change=lambda e: changed(e, 'art_Subjects')),
        Row([TextField(label="by Artists", value=prefs['prompt_writer']['by_Artists'], on_change=lambda e: changed(e, 'by_Artists')),
             TextField(label="Art Styles", value=prefs['prompt_writer']['art_Styles'], on_change=lambda e: changed(e, 'art_Styles')),]),
        Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_writer']['amount'], on_change=lambda e: changed(e, 'amount')),
            NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_writer']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),
            NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_writer']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
            Checkbox(label="Permutate Artists", value=prefs['prompt_writer']['permutate_artists'], on_change=lambda e: changed(e, 'permutate_artists'))], alignment="spaceBetween"),
        ElevatedButton(content=Text("✍️   Write Prompts", size=18), on_click=lambda _: run_prompt_writer(page)),
        page.prompt_writer_list,
        writer_list_buttons,
      ], scroll="auto",
    ))
    return c

def NSP_instructions(page):
    def open_url(e):
        page.launch_url(e.data)
    NSP_markdown = '''To use a term database, simply use any of the keys below. 

For example if you wanted beauty adjective, you would write `_adj-beauty_` in your prompt. 

## Terminology Keys (by [@WAS](https://rebrand.ly/easy-diffusion))

### Adjective Types
   - `_adj-architecture_` - A list of architectural adjectives and styles
   - `_adj-beauty_` - A list of beauty adjectives for people (maybe things?)
   - `_adj-general_` - A list of general adjectives for people/things.
   - `_adj-horror_` - A list of horror adjectives
### Art Types
   - `_artist_` - A comprehensive list of artists by [**MisterRuffian**](https://docs.google.com/spreadsheets/d/1_jgQ9SyvUaBNP1mHHEzZ6HhL_Es1KwBKQtnpnmWW82I/edit) (Discord _Misterruffian#2891_)
   - `_color_` - A comprehensive list of colors
   - `_portrait-type_` - A list of common portrait types/poses
   - `_style_` - A list of art styles and mediums
### Computer Graphics Types
   - `_3d-terms_` - A list of 3D graphics terminology
   - `_color-palette_` - A list of computer and video game console color palettes
   - `_hd_` - A list of high definition resolution terms
### Miscellaneous Types
   - `_details_` - A list of detail descriptors
   - `_site_` - A list of websites to query
   - `_gen-modififer_` - A list of general modifiers adopted from [Weird Wonderful AI Art](https://weirdwonderfulai.art/)
   - `_neg-weight_` - A lsit of negative weight ideas
   - `_punk_` - A list of punk modifier (eg. cyberpunk)
   - ` _pop-culture_` - A list of popular culture movies, shows, etc
   - `_pop-location_` - A list of popular tourist locations
   - `_fantasy-setting_` - A list of fantasy location settings
   - `_fantasy-creature_` - A list of fantasy creatures
   - `_animals_` - A list of modern animals
### Noun Types
   - `_noun-beauty_` - A list of beauty related nouns
   - `_noun-emote_` - A list of emotions and expressions
   - `_noun-fantasy_` - A list of fantasy nouns
   - `_noun-general_` - A list of general nouns
   - `_noun-horror_` - A list of horror nouns
### People Types
   - `_bodyshape_` - A list of body shapes
   - `_celeb_` - A list of celebrities
   - `_eyecolor_` - A list of eye colors
   - `_hair_` - A list of hair types
   - `_nationality_` - A list of nationalities
   - `_occputation_` A list of occupation types
   - `_skin-color_` - A list of skin tones
   - `_identity-young_` A list of young identifiers
   - `_identity-adult_` A list of adult identifiers
   - `_identity_` A list of general identifiers
### Photography / Image / Film Types
   - `_aspect-ratio_` - A list of common aspect ratios
   - `_cameras_` - A list of camera models *(including manufactuerer)*
   - `_camera-manu_` - A list of camera manufacturers
   - `_f-stop_` - A list of camera aperture f-stop
   - `_focal-length_` - A list of focal length ranges
   - `_photo-term_` - A list of photography terms relating to photos

So in Subject try something like: `A _color_ _noun-general_ that is _adj-beauty_ and _adj-general_ with a _noun-emote_ _noun-fantasy_`
'''
    def close_NSP_dlg(e):
      instruction_alert.open = False
      page.update()
    instruction_alert = AlertDialog(title=Text("🍜  Noodle Soup Prompt Variables Instructions"), content=Column([Markdown(NSP_markdown, extension_set="gitHubWeb", on_tap_link=open_url)], scroll="auto"), actions=[TextButton("Good Soup!", on_click=close_NSP_dlg)], actions_alignment="end",)
    page.dialog = instruction_alert
    instruction_alert.open = True
    page.update()

def buildExtras(page):
    page.ESRGAN_upscaler = buildESRGANupscaler(page)
    page.RetrievePrompts = buildRetrievePrompts(page)
    page.InitFolder = buildInitFolder(page)
    promptTabs = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(text="Real-ESRGAN Batch Upscaler", content=page.ESRGAN_upscaler, icon=icons.PHOTO_SIZE_SELECT_LARGE),
            Tab(text="Retrieve Prompt from Image", content=page.RetrievePrompts, icon=icons.PHOTO_LIBRARY_OUTLINED),
            Tab(text="Init Images from Folder", content=page.InitFolder, icon=icons.FOLDER_SPECIAL),
        ],
        expand=1,
        #on_change=tab_on_change
    )
    return promptTabs

ESRGAN_prefs = {
    'enlarge_scale': 1.5,
    'face_enhance': False,
    'image_path': '',
    'save_to_GDrive': True,
    'upload_file': False,
    'download_locally': False,
    'display_image': False,
    'dst_image_path': '',
    'filename_suffix': '',
    'split_image_grid': False,
    'rows': 3,
    'cols': 3,
}
def buildESRGANupscaler(page):
    def changed(e, pref=None):
      if pref is not None:
        ESRGAN_prefs[pref] = e.control.value
    def pick_path(e):
      print(e.control.value)
      #TODO: File picker that uploads to root
    def add_to_ESRGAN_output(o):
      ESRGAN_output.controls.append(o)
      ESRGAN_output.update()
      if clear_button.visible == False:
        clear_button.visible = True
        clear_button.update()
      #generator_list_buttons.visible = True
      #generator_list_buttons.update()
    page.add_to_ESRGAN_output = add_to_ESRGAN_output
    enlarge_scale_value = Text(f" {float(ESRGAN_prefs['enlarge_scale'])}x", weight="bold")
    def change_enlarge_scale(e):
        enlarge_scale_value.value = f" {int(e.control.value) if e.control.value.is_integer() else float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale')
    def toggle_split(e):
      split_container.height = None if e.control.value else 0
      changed(e, 'split_image_grid')
      split_container.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      ESRGAN_output.controls = []
      ESRGAN_output.update()
      clear_button.visible = False
      clear_button.update()
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=ESRGAN_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=ESRGAN_prefs['face_enhance'], on_change=lambda e:changed(e,'face_enhance'))
    image_path = TextField(label="Image File or Folder Path", value=ESRGAN_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_path), expand=1)
    dst_image_path = TextField(label="Destination Image Path", value=ESRGAN_prefs['dst_image_path'], on_change=lambda e:changed(e,'dst_image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED), expand=1)
    filename_suffix = TextField(label="Optional Filename Suffix", value=ESRGAN_prefs['filename_suffix'], on_change=lambda e:changed(e,'filename_suffix'), width=260)
    download_locally = Checkbox(label="Download Images Locally", value=ESRGAN_prefs['download_locally'], on_change=lambda e:changed(e,'download_locally'))
    display_image = Checkbox(label="Display Upscaled Image", value=ESRGAN_prefs['display_image'], on_change=lambda e:changed(e,'display_image'))
    split_image_grid = Switch(label="Split Image Grid", value=ESRGAN_prefs['split_image_grid'], on_change=toggle_split)
    rows = NumberPicker(label="Rows: ", min=1, max=8, value=ESRGAN_prefs['rows'], on_change=lambda e: changed(e, 'rows'))
    cols = NumberPicker(label="Columns: ", min=1, max=8, value=ESRGAN_prefs['cols'], on_change=lambda e: changed(e, 'cols'))
    split_container = Container(Row([rows, Container(content=None, width=25), cols]), animate_size=animation.Animation(800, "bounceOut"), clip_behavior="hardEdge", padding=padding.only(left=28), height=0)
    ESRGAN_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment="end")
    clear_button.visible = len(ESRGAN_output.controls) > 0
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text("↕️  Real-ESRGAN AI Upscale Enlarging", style="titleLarge"),
        Text("Select one or more files, or give path to image or folder. Save to your Google Drive and/or Download."),
        Divider(thickness=1, height=5),
        enlarge_scale_slider,
        face_enhance,
        Row([# I can't get them to stretch without crashing!
        image_path,
        dst_image_path,], width=page.width - 80),
        filename_suffix,
        download_locally,
        display_image,
        #Divider(thickness=2, height=4),
        split_image_grid,
        split_container,
        ElevatedButton(content=Text("🐘  Run AI Upscaling", size=18), on_click=lambda _: run_upscaling(page)),
        ESRGAN_output,
        clear_button,
      ], scroll="auto",
    ))
    return c

retrieve_prefs = {
    'image_path': '',
    'add_to_prompts': True,
    'display_full_metadata': False,
    'display_image': False,
    'upload_file': False,
}
def buildRetrievePrompts(page):
    def changed(e, pref=None):
        if pref is not None:
          retrieve_prefs[pref] = e.control.value
    def add_to_retrieve_output(o):
      retrieve_output.controls.append(o)
      retrieve_output.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      retrieve_output.controls = []
      retrieve_output.update()
      clear_button.visible = False
      clear_button.update()
    page.add_to_retrieve_output = add_to_retrieve_output
    image_path = TextField(label="Image File or Folder Path", value=retrieve_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD))
    add_to_prompts = Checkbox(label="Add to Prompts", value=retrieve_prefs['add_to_prompts'], on_change=lambda e:changed(e,'add_to_prompts'))
    display_full_metadata = Checkbox(label="Display Full Metadata", value=retrieve_prefs['display_full_metadata'], on_change=lambda e:changed(e,'display_full_metadata'))
    display_image = Checkbox(label="Display Image", value=retrieve_prefs['display_image'], on_change=lambda e:changed(e,'display_image'))
    retrieve_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment="end")
    clear_button.visible = len(retrieve_output.controls) > 0
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text("📰  Retrieve Dream Prompts from Image Metadata", style="titleLarge"),
        Text("Give it images made here and gives you all parameters used to recreate it. Either upload png file(s) or paste path to image or folder or config.json to revive your dreams.."),
        Divider(thickness=1, height=5),
        image_path,
        add_to_prompts,
        display_full_metadata,
        display_image,
        ElevatedButton(content=Text("😴  Retrieve Dream", size=18), on_click=lambda _: run_retrieve(page)),
        retrieve_output,
        clear_button,
      ], scroll="auto",
    ))
    return c

initfolder_prefs = {
    'prompt_string': '',
    'init_folder': '',
    'include_strength': True,
    'image_strength': 0.5,
}
def buildInitFolder(page):
    def changed(e, pref=None):
        if pref is not None:
          initfolder_prefs[pref] = e.control.value
    def add_to_initfolder_output(o):
      initfolder_output.controls.append(o)
      initfolder_output.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      initfolder_output.controls = []
      initfolder_output.update()
      clear_button.visible = False
      clear_button.update()
    page.add_to_initfolder_output = add_to_initfolder_output
    prompt_string = TextField(label="Prompt Text", value=initfolder_prefs['prompt_string'], on_change=lambda e:changed(e,'prompt_string'))
    init_folder = TextField(label="Init Image Folder Path", value=initfolder_prefs['init_folder'], on_change=lambda e:changed(e,'init_folder'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD))
    include_strength = Checkbox(label="Include Strength", value=initfolder_prefs['include_strength'], on_change=lambda e:changed(e,'image_strength'))
    image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=float(initfolder_prefs['image_strength']), expand=True)
    strength_container = Container(Row([Text("Init Image Strength: "), image_strength]))
    initfolder_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment="end")
    clear_button.visible = len(initfolder_output.controls) > 0
    c = Container(
      padding=padding.only(18, 12, 0, 8),
      content=Column([
        Text("📂 Generate Prompts from Folder as Init Images", style="titleLarge"),
        Text("Provide a Folder with a collection of images that you want to automatically add to prompts list with init_image overides..."),
        Divider(thickness=1, height=4),
        init_folder,
        prompt_string,
        include_strength,
        image_strength,
        ElevatedButton(content=Text("➕  Add to Prompts", size=18), on_click=lambda _: run_initfolder(page)),
        initfolder_output,
        clear_button,
      ], scroll="auto"
    ))
    return c

use_custom_scheduler = False
retry_attempts_if_NSFW = 3

unet = None
pipe = None
pipe_img2img = None
pipe_interpolation = None
pipe_clip_guided = None
stability_api = None
model_path = "CompVis/stable-diffusion-v1-4"
inpaint_model = "runwayml/stable-diffusion-inpainting"
scheduler = None
scheduler_clip = None
if is_Colab:
  from google.colab import output
  output.enable_custom_widget_manager()

def run_diffusers(page):
    global scheduler, use_custom_scheduler, model_path, prefs
    try:
      from huggingface_hub import notebook_login, HfApi, HfFolder
      from diffusers import StableDiffusionPipeline
    except ImportError as e:
      run_process("pip install --upgrade -q git+https://github.com/Skquark/diffusers.git@main#egg=diffusers", page=page)
      run_process("pip install -q transformers scipy ftfy", page=page)
      run_process('pip install -qq "ipywidgets>=7,<8"', page=page)
      run_process("git config --global credential.helper store", page=page)
      from huggingface_hub import notebook_login, HfApi, HfFolder
      pass
    if not os.path.exists(HfFolder.path_token):
        from huggingface_hub.commands.user import _login
        _login(HfApi(), token=prefs['HuggingFace_api_key'])
    if prefs['model_ckpt'] == "Stable Diffusion v1.5": model_path =  "runwayml/stable-diffusion-v1-5"
    else: model_path =  "CompVis/stable-diffusion-v1-4"
    scheduler_mode = prefs['scheduler_mode']
    if scheduler_mode == "K-LMS":
      from diffusers import LMSDiscreteScheduler
      scheduler = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
      #(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, timestep_values=None, tensor_format="pt")
    if scheduler_mode == "PNDM":
      from diffusers import PNDMScheduler
      scheduler = PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
      #scheduler = PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", skip_prk_steps=True), #(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", tensor_format="pt", skip_prk_steps=False)
    if scheduler_mode == "DDIM":
      from diffusers import DDIMScheduler
      scheduler = DDIMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", clip_sample=False, set_alpha_to_one=False) #(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, timestep_values=None, clip_sample=True, set_alpha_to_one=True, tensor_format="pt")
    if scheduler_mode == "Score-SDE-Vp":
      from diffusers import ScoreSdeVpScheduler
      scheduler = ScoreSdeVpScheduler() #(num_train_timesteps=2000, beta_min=0.1, beta_max=20, sampling_eps=1e-3, tensor_format="np")
      use_custom_scheduler = True
    if scheduler_mode == "Score-SDE-Ve":
      from diffusers import ScoreSdeVeScheduler
      scheduler = ScoreSdeVeScheduler() #(num_train_timesteps=2000, snr=0.15, sigma_min=0.01, sigma_max=1348, sampling_eps=1e-5, correct_steps=1, tensor_format="pt"
      use_custom_scheduler = True
    if scheduler_mode == "DDPM":
      from diffusers import DDPMScheduler
      scheduler = DDPMScheduler(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, variance_type="fixed_small", clip_sample=True, tensor_format="pt")
      use_custom_scheduler = True
    if scheduler_mode == "Karras-Ve":
      from diffusers import KarrasVeScheduler
      scheduler = KarrasVeScheduler() #(sigma_min=0.02, sigma_max=100, s_noise=1.007, s_churn=80, s_min=0.05, s_max=50, tensor_format="pt")
      use_custom_scheduler = True
    if scheduler_mode == "LMS":
      from diffusers import LMSScheduler
      scheduler = LMSScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
      #(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, timestep_values=None, tensor_format="pt")
      use_custom_scheduler = True
    #print(f"Loaded Schedueler {scheduler_mode} {type(scheduler)}")

torch_device = "cuda"
import torch, gc
from torch.amp.autocast_mode import autocast
from random import random
import time

pb = ProgressBar(width=420, bar_height=8)
total_steps = args['steps']
def callback_fn(step: int, timestep: int, latents: torch.FloatTensor) -> None:
    callback_fn.has_been_called = True
    global total_steps, pb
    percent = (step +1)/ total_steps
    pb.value = percent
    pb.tooltip = f"{step +1} / {total_steps}"
    #print(f"step: {step}, total: {total_steps}")
    #if step == 0:
        #latents = latents.detach().cpu().numpy()
        #assert latents.shape == (1, 4, 64, 64)
        #latents_slice = latents[0, -3:, -3:, -1]
        #expected_slice = np.array([1.8285, 1.2857, -0.1024, 1.2406, -2.3068, 1.0747, -0.0818, -0.6520, -2.9506])
        #assert np.abs(latents_slice.flatten() - expected_slice).max() < 1e-3
        #prt(pb)
    pb.update()

def get_text2image(page):
    os.chdir(root_dir)
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    from diffusers import StableDiffusionPipeline
    global pipe, unet, scheduler, prefs

    if pipe is not None:
        #print("Clearing the ol' pipe first...")
        del pipe
        gc.collect()
        torch.cuda.empty_cache()
        pipe = None
    try:
      if use_custom_scheduler:
        from transformers import CLIPTextModel, CLIPTokenizer
        from diffusers import AutoencoderKL, UNet2DConditionModel
        # 1. Load the autoencoder model which will be used to decode the latents into image space. 
        vae = AutoencoderKL.from_pretrained(model_path, subfolder="vae", use_auth_token=True)
        # 2. Load the tokenizer and text encoder to tokenize and encode the text. 
        tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
        text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")
        if prefs['higher_vram_mode']:
          unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", use_auth_token=True)
        else:
          unet = UNet2DConditionModel.from_pretrained(model_path, revision="fp16", torch_dtype=torch.float16, subfolder="unet", use_auth_token=True)
        vae = vae.to(torch_device)
        text_encoder = text_encoder.to(torch_device)
        #if enable_attention_slicing:
        #  unet.enable_attention_slicing() #slice_size
        unet = unet.to(torch_device)
      else:
        pipe = get_txt2img_pipe()
    except EnvironmentError:
      alert_msg(page, f'{Color.RED}ERROR: Looks like you need to accept the HuggingFace Stable-Diffusion-v1-4 Model Card to use Checkpoint{Color.END}\nhttps://huggingface.co/CompVis/stable-diffusion-v1-4')

# I thought it's what I wanted, but current implementation does same as mine but doesn't clear memory between
def get_mega_pipe():
  global pipe, scheduler, model_path, prefs
  from diffusers import StableDiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  if prefs['higher_vram_mode']:
    pipe = DiffusionPipeline.from_pretrained(model_path, community="stable_diffusion_mega", scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  else:
    pipe = DiffusionPipeline.from_pretrained(model_path, community="stable_diffusion_mega", scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  if prefs['enable_attention_slicing']:
    pipe.enable_attention_slicing()
  pipe.set_progress_bar_config(disable=True)
  pipe = pipe.to(torch_device)
  return pipe

def get_txt2img_pipe():
  global pipe, scheduler, model_path, prefs
  from diffusers import StableDiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  if prefs['higher_vram_mode']:
    pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  else:
    pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  if prefs['enable_attention_slicing']:
    pipe.enable_attention_slicing()
  pipe.set_progress_bar_config(disable=True)
  pipe = pipe.to(torch_device)
  return pipe

def get_unet_pipe():
  global unet, scheduler, model_path, prefs
  from transformers import CLIPTextModel, CLIPTokenizer
  from diffusers import AutoencoderKL, UNet2DConditionModel
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  # 1. Load the autoencoder model which will be used to decode the latents into image space. 
  vae = AutoencoderKL.from_pretrained(model_path, subfolder="vae")
  # 2. Load the tokenizer and text encoder to tokenize and encode the text. 
  tokenizer = CLIPTokenizer.from_pretrained("openai/clip-vit-large-patch14")
  text_encoder = CLIPTextModel.from_pretrained("openai/clip-vit-large-patch14")
  if prefs['higher_vram_mode']:
    unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  else:
    unet = UNet2DConditionModel.from_pretrained(model_path, revision="fp16", torch_dtype=torch.float16, subfolder="unet", safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  vae = vae.to(torch_device)
  text_encoder = text_encoder.to(torch_device)
  #if enable_attention_slicing:
  #  unet.enable_attention_slicing() #slice_size
  unet = unet.to(torch_device)
  return unet

def get_interpolation(page):
    from diffusers import DDIMScheduler, PNDMScheduler, LMSDiscreteScheduler
    import torch, gc
    global pipe_interpolation
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if pipe_interpolation is not None:
      #print("Clearing the ol' pipe first...")
      del pipe_interpolation
      gc.collect()
      torch.cuda.empty_cache()
      pipe_interpolation = None

    pipe_interpolation = get_interpolation_pipe()
    run_process("pip install watchdog", page=page)
    status['loaded_interpolation'] = True

def get_interpolation_pipe():
    global pipe_interpolation, scheduler, model_path, prefs
    from diffusers import StableDiffusionPipeline
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
    os.chdir(root_dir)
    if not os.path.isfile(os.path.join(root_dir, 'clip_guided_stable_diffusion.py')):
      run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/Skquark/diffusers/main/examples/community/interpolate_stable_diffusion.py")
    from interpolate_stable_diffusion import StableDiffusionWalkPipeline
    if prefs['higher_vram_mode']:
      pipe_interpolation = StableDiffusionWalkPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
      #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    else:
      pipe_interpolation = StableDiffusionWalkPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
      #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    if prefs['enable_attention_slicing']:
      pipe_interpolation.enable_attention_slicing()
    pipe_interpolation.set_progress_bar_config(disable=True)
    pipe_interpolation = pipe_interpolation.to(torch_device)
    return pipe_interpolation

def get_image2image(page):
    from diffusers import StableDiffusionInpaintPipeline, DDIMScheduler, PNDMScheduler, LMSDiscreteScheduler
    import torch, gc
    global pipe_img2img
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if pipe_img2img is not None:
      #print("Clearing the ol' pipe first...")
      del pipe_img2img
      gc.collect()
      torch.cuda.empty_cache()
      pipe_img2img = None

    pipe_img2img = get_img2img_pipe()
    loaded_img2img = True

def get_img2img_pipe():
  global pipe_img2img, scheduler, model_path, inpaint_model, prefs, callback_fn
  from diffusers import StableDiffusionInpaintPipeline, DDIMScheduler, PNDMScheduler, LMSDiscreteScheduler
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  if isinstance(scheduler, DDIMScheduler) or isinstance(scheduler, PNDMScheduler) or isinstance(scheduler, LMSDiscreteScheduler):
    scheduler_img2img = scheduler
  else:
    scheduler_img2img = DDIMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", clip_sample=False, set_alpha_to_one=False)
  #StableDiffusionImg2ImgPipeline
  if prefs['higher_vram_mode']:
    pipe_img2img = StableDiffusionInpaintPipeline.from_pretrained(
        inpaint_model,
        scheduler=scheduler,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
    )
  else:
      pipe_img2img = StableDiffusionInpaintPipeline.from_pretrained(
      inpaint_model,
      scheduler=scheduler,
      revision="fp16", 
      torch_dtype=torch.float16,
      safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  if prefs['enable_attention_slicing']:
    pipe_img2img.enable_attention_slicing() #slice_size
  pipe_img2img.set_progress_bar_config(disable=True)
  pipe_img2img.to(torch_device)
  def dummy(images, **kwargs): return images, False
  pipe_img2img.safety_checker = dummy
  return pipe_img2img

def get_clip(page):
    global pipe_clip_guided, model_path
    os.chdir(root_dir)
    if not os.path.isfile(os.path.join(root_dir, 'clip_guided_stable_diffusion.py')):
      run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/Skquark/diffusers/c16761e9d94a3374710110ba5e3087cb9f8ba906/examples/community/clip_guided_stable_diffusion.py")
    #from clip_guided_stable_diffusion import *

    if pipe_clip_guided is not None:
        #print("Clearing out old CLIP Guided pipeline before reloading.")
        del pipe_clip_guided
        gc.collect()
        torch.cuda.empty_cache()
    pipe_clip_guided = get_clip_guided_pipe()

def get_clip_guided_pipe():
    global pipe_clip_guided, scheduler_clip, prefs
    from diffusers import LMSDiscreteScheduler, PNDMScheduler, StableDiffusionPipeline
    from clip_guided_stable_diffusion import CLIPModel, CLIPFeatureExtractor, CLIPGuidedStableDiffusion
    pipeline = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        revision="fp16",
    )
    if isinstance(scheduler, LMSDiscreteScheduler) or isinstance(scheduler, PNDMScheduler):
      scheduler_clip = scheduler
    else:
      scheduler_clip = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")

    clip_model = CLIPModel.from_pretrained(prefs['clip_model_id'], torch_dtype=torch.float16)
    feature_extractor = CLIPFeatureExtractor.from_pretrained(prefs['clip_model_id'], torch_dtype=torch.float16)

    pipe_clip_guided = CLIPGuidedStableDiffusion(
        unet=pipeline.unet,
        vae=pipeline.vae,
        tokenizer=pipeline.tokenizer,
        text_encoder=pipeline.text_encoder,
        scheduler=scheduler_clip,
        clip_model=clip_model,
        feature_extractor=feature_extractor,
    )
    if prefs['enable_attention_slicing']:
      pipe_clip_guided.enable_attention_slicing()
    return pipe_clip_guided.to("cuda")

SD_sampler = None
def get_stability(page):
    global SD_sampler, stability_api, prefs
    try:
      from stability_sdk import client
      import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
    except ImportError as e:
      run_process("pip install stability-sdk -q", page=page)
      from stability_sdk import client
      import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
      pass
    stability_api = client.StabilityInference(
        key=prefs['Stability_api_key'], 
        verbose=True,
        engine=prefs['model_checkpoint'] if prefs['model_checkpoint'] == "stable-diffusion-v1-5" else "stable-diffusion-v1",
    )
    SD_sampler = client.get_sampler_from_str(prefs['generation_sampler'])
    status['installed_stability'] = True

def get_ESRGAN(page):
    os.chdir(root_dir)
    run_process("git clone https://github.com/xinntao/Real-ESRGAN.git -q", page=page)
    os.chdir(os.path.join(root_dir, 'Real-ESRGAN'))
    run_process("pip install basicsr --quiet", page=page)
    run_process("pip install facexlib --quiet", page=page)
    run_process("pip install gfpgan --quiet", page=page)
    run_process("pip install -r requirements.txt --quiet", page=page, realtime=False)
    run_process("python setup.py develop --quiet", page=page, realtime=False)
    run_process("wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P experiments/pretrained_models --quiet", page=page)
    os.chdir(root_dir)

def clear_img2img_pipe():
  global pipe_img2img
  if pipe_img2img is not None:
    #print("Clearing out img2img pipeline for more VRAM")
    del pipe_img2img
    gc.collect()
    torch.cuda.empty_cache()
    pipe_img2img = None
def clear_txt2img_pipe():
  global pipe
  if pipe is not None:
    #print("Clearing out text2img pipeline for more VRAM")
    del pipe
    gc.collect()
    torch.cuda.empty_cache()
    pipe = None
def clear_unet_pipe():
  global unet
  if unet is not None:
    #print("Clearing out unet custom pipeline for more VRAM")
    del unet
    gc.collect()
    torch.cuda.empty_cache()
    unet = None
def clear_clip_guided_pipe():
  global pipe_clip_guided
  if pipe_clip_guided is not None:
    #print("Clearing out CLIP Guided pipeline for more VRAM")
    del pipe_clip_guided
    gc.collect()
    torch.cuda.empty_cache()
    pipe_clip_guided = None

def available_file(folder, name, idx):
  available = False
  while not available:
    # Todo, check if using PyDrive2
    if os.path.isfile(os.path.join(folder, f'{name}-{idx}.png')):
      idx += 1
    else: available = True
  return os.path.join(folder, f'{name}-{idx}.png')

def start_diffusion(page):
  global pipe, unet, pipe_img2img, pipe_clip_guided, pipe_interpolation, SD_sampler, stability_api, total_steps, pb, prefs, args, total_steps
  def prt(line):
    if type(line) == str:
      line = Text(line)
    page.Images.content.controls.append(line)
    page.Images.content.update()
    page.Images.update()
  def clear_last():
    del page.Images.content.controls[-1]
    page.Images.content.update()
    page.Images.update()
  page.Images.content.controls = []
  pb.width=page.width - 50
  prt(Text("▶️  Running Stable Diffusion on Batch Prompts List", style="titleLarge"),)
  import string, shutil, random, gc, io, json
  from collections import ChainMap
  import PIL
  from PIL import Image as PILImage
  from PIL.PngImagePlugin import PngInfo
  import numpy as np
  from contextlib import contextmanager, nullcontext
  import copy

  if status['installed_diffusers']:
    from diffusers import StableDiffusionPipeline
  os.chdir(stable_dir)
  generator = None
  output_files = []
  retry_attempts_if_NSFW = prefs['retry_attempts']
  last_seed = args['seed']
  if args['seed'] < 1 or args['seed'] is None:
    rand_seed = random.randint(0,4294967295)
    if not prefs['use_Stability_api']:
      if use_custom_scheduler:
        generator = torch.manual_seed(rand_seed)
      else:
        generator = torch.Generator("cuda").manual_seed(rand_seed)
    last_seed = rand_seed
  else:
    if not prefs['use_Stability_api']:
      if use_custom_scheduler:
        generator = torch.manual_seed(args['seed'])
      else:
        generator = torch.Generator("cuda").manual_seed(args['seed'])
  strikes = 0
  p_idx = 0
  if prefs['centipede_prompts_as_init_images']:
    os.makedirs(os.path.join(root_dir, 'init_images'), exist_ok=True)
  last_image = None
  updated_prompts = []

  if not (prefs["use_interpolation"] and status['installed_interpolation']):
    for p in prompts:
      pr = None
      arg = {}
      if type(p) == list or type(p) == str:
        pr = p
        arg = args.copy()
      elif isinstance(p, Dream):
        pr = p.prompt
        arg = merge_dict(args, p.arg)
      else: prt(f'Unknown item in list of type {type(p)}')
      #print(str(arg))
      arg['width'] = int(arg['width'])
      arg['height'] = int(arg['height'])
      arg['seed'] = int(arg['seed'])
      arg['guidance_scale'] = float(arg['guidance_scale'])
      arg['batch_size'] = int(arg['batch_size'])
      arg['n_iterations'] = int(arg['n_iterations'])
      arg['steps'] = int(arg['steps'])
      arg['eta'] = float(arg['eta'])
      arg['init_image_strength'] = float(arg['init_image_strength'])
      p.arg = arg
      iterations = arg['n_iterations']
      updated_prompts.append(p)
      if iterations > 1:
        #print(f"Iterating {iterations} times - {pr}")
        for d in range(iterations - 1):
          new_dream = None
          if isinstance(p, Dream):
            new_dream = copy.copy(p)
            new_dream.prompt = pr[0] if type(pr) == list else pr
            new_arg = new_dream.arg.copy()
            new_arg['seed'] = random.randint(0,4294967295)
            new_arg['n_iterations'] = 1
            new_dream.arg = new_arg
            #new_dream.arg['seed'] = random.randint(0,4294967295)
          else:
            new_dream = Dream(p, seed=random.randint(0,4294967295), n_iterations=1)
          new_dream.arg['n_iterations'] = 1
          #prompts.insert(p_idx+1, new_dream)
          updated_prompts.append(new_dream)

    for p in updated_prompts:
      pr = ""
      images = None
      usable_image = True
      arg = {}
      if type(p) == list or type(p) == str:
        pr = p
        arg = args.copy()
      elif isinstance(p, Dream):
        pr = p.prompt
        arg = merge_dict(args, p.arg)
      else: prt(f"Unknown object {type(p)} in the prompt list")
      if arg['batch_size'] > 1:
        pr = [pr] * arg['batch_size']
        if bool(arg['negative_prompt']):
          arg['negative_prompt'] = [arg['negative_prompt']] * arg['batch_size']
      if last_seed != arg['seed']:
        if arg['seed'] < 1 or arg['seed'] is None:
          rand_seed = random.randint(0,4294967295)
          if not prefs['use_Stability_api']:
            if use_custom_scheduler:
              generator = torch.manual_seed(rand_seed)
            else:
              generator = torch.Generator("cuda").manual_seed(rand_seed)
          arg['seed'] = rand_seed
        else:
          if not prefs['use_Stability_api']:
            if use_custom_scheduler:
              generator = torch.manual_seed(arg['seed'])
            else:
              generator = torch.Generator("cuda").manual_seed(arg['seed'])
        last_seed = arg['seed']
      if prefs['centipede_prompts_as_init_images'] and last_image is not None:
        arg['init_image'] = last_image
      p_count = f'[{p_idx + 1} of {len(updated_prompts)}]  '
      #if p_idx % 30 == 0 and p_idx > 1:
      #  clear_output()
      #  print(f"{Color.BEIGE2}Cleared console display due to memory limit in console logging.  Images still saving.{Color.END}")
      page.auto_scrolling(False)
      prt(Divider(height=6, thickness=2))
      prt(Row([Text(p_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight="bold"), Text(f'seed: {arg["seed"]}')]))
      #prt(p_count + ('─' * 90))
      #prt(f'{pr[0] if type(pr) == list else pr} - seed:{arg["seed"]}')
      total_steps = arg['steps']
      
      if prefs['use_Stability_api'] or bool(arg['use_Stability']):    
        if not status['loaded_stability_']:
          print(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: To use Stability-API, you must run the init block above")
        else:
          prt('Stablity API Diffusion ' + ('─' * 100))
          #print(f'"{SD_prompt}", height={SD_height}, width={SD_width}, steps={SD_steps}, cfg_scale={SD_guidance_scale}, seed={SD_seed}, sampler={generation_sampler}')
          #strikes = 0
          images = []
          if bool(arg['mask_image']):
            if not bool(arg['init_image']):
              prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: You have not selected an init_image to go with your image mask..")
              continue
            import requests
            from io import BytesIO
            if arg['init_image'].startswith('http'):
              response = requests.get(arg['init_image'])
              init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
            else:
              if os.path.isfile(arg['init_image']):
                init_img = PILImage.open(arg['init_image'])
              else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your init_image {arg['init_image']}")
            init_img = init_img.resize((arg['width'], arg['height']))
            #init_image = preprocess(init_img)
            if arg['mask_image'].startswith('http'):
              response = requests.get(arg['mask_image'])
              mask_img = PILImage.open(BytesIO(response.content)).convert("RGB")
            else:
              if os.path.isfile(arg['mask_image']):
                mask_img = PILImage.open(arg['mask_image'])
              else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your mask_image {arg['mask_image']}")
            mask = mask_img.resize((arg['width'], arg['height']))
            answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], mask_image=mask, init_image=init_img, start_schedule= 1 - arg['init_image_strength'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], safety=not prefs["disable_nsfw_filter"], sampler=SD_sampler)
          elif bool(arg['init_image']):
            import requests
            from io import BytesIO
            if arg['init_image'].startswith('http'):
              response = requests.get(arg['init_image'])
              init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
            else:
              if os.path.isfile(arg['init_image']):
                init_img = PILImage.open(arg['init_image']).convert("RGB")
              else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your init_image {arg['init_image']}")
            init_img = init_img.resize((arg['width'], arg['height']))
            answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], init_image=init_img, start_schedule= 1 - arg['init_image_strength'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], safety=not prefs["disable_nsfw_filter"], sampler=SD_sampler)
          else:
            answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], safety=False, sampler=SD_sampler)
          for resp in answers:
            for artifact in resp.artifacts:
              #print("Artifact reason: " + str(artifact.finish_reason))
              if artifact.finish_reason == generation.FILTER:         
                usable_image = False
              if artifact.finish_reason == generation.ARTIFACT_TEXT:         
                usable_image = False
                print(f"{Color.RED}{Color.BOLD}Couldn't process NSFW text in prompt.{Color.END} Can't retry so change your request.")
              if artifact.type == generation.ARTIFACT_IMAGE:
                images.append(PILImage.open(io.BytesIO(artifact.binary)))

      else:
        #from torch.amp.autocast_mode import autocast
        #precision_scope = autocast if prefs['precision']=="autocast" else nullcontext
        try:
          if use_custom_scheduler and not bool(arg['init_image']) and not bool(arg['mask_image']) and not bool(arg['prompt2']):
            text_input = tokenizer(pr[0] if type(pr) == list else pr, padding="max_length", max_length=tokenizer.model_max_length, truncation=True, return_tensors="pt")

            with torch.no_grad():
              text_embeddings = text_encoder(text_input.input_ids.to(torch_device))[0]# We'll also get the unconditional text embeddings for classifier-free guidance, which are just the embeddings for the padding token (empty text). They need to have the same shape as the conditional text_embeddings (batch_size and seq_length)
            max_length = text_input.input_ids.shape[-1]
            uncond_input = tokenizer([""] * arg['batch_size'], padding="max_length", max_length=max_length, return_tensors="pt")
            with torch.no_grad():
              uncond_embeddings = text_encoder(uncond_input.input_ids.to(torch_device))[0]   #For classifier-free guidance, we need to do two forward passes. One with the conditioned input (`text_embeddings`), and another with the unconditional embeddings (`uncond_embeddings`). In practice, we can concatenate both into a single batch to avoid doing two forward passes.

            text_embeddings = torch.cat([uncond_embeddings, text_embeddings])#Generate the intial random noise.
            #if generator:
            #latents = torch.randn((arg['batch_size'], unet.in_channels, arg['height'], arg['width']), generator=generator)
            latents = torch.randn((arg['batch_size'], unet.in_channels, arg['height'] // 8,  arg['width'] // 8), generator=generator)
            #else:
            #  latents = torch.randn((batch_size, unet.in_channels, arg['height'] // 8, arg['width'] // 8))
            latents = latents.to(torch_device)
            latents.shape
            #Cool  64×64  is expected. The model will transform this latent representation (pure noise) into a 512 × 512 image later on.
            #Next, we initialize the scheduler with our chosen num_inference_steps. This will compute the sigmas and exact time step values to be used during the denoising process.
            scheduler.set_timesteps(arg['steps'])#The K-LMS scheduler needs to multiple the `latents` by its `sigma` values. Let's do this here
            if prefs['scheduler_mode'] == "K-LMS" or prefs['scheduler_mode'] == "Score-SDE-Vp":
              latents = latents * scheduler.sigmas[0]#We are ready to write the denoising loop.
            from tqdm.auto import tqdm
            clear_img2img_pipe()
            clear_txt2img_pipe()
            clear_clip_guided_pipe()
            if unet is None:
              unet = get_unet_pipe()
            #with precision_scope("cuda"):
            #with autocast("cuda"):
            for i, t in tqdm(enumerate(scheduler.timesteps)):
              # expand the latents if we are doing classifier-free guidance to avoid doing two forward passes.
              latent_model_input = torch.cat([latents] * 2)
              if prefs['scheduler_mode'] == "K-LMS" or prefs['scheduler_mode'] == "Score-SDE-Vp":
                sigma = scheduler.sigmas[i]
                latent_model_input = latent_model_input / ((sigma**2 + 1) ** 0.5)
              # predict the noise residual
              if prefs['scheduler_mode'] == "DDPM":
                #TODO: Work in progress, still not perfect
                noisy_sample = torch.randn(1, unet.config.in_channels, unet.config.sample_size, unet.config.sample_size)
                noisy_residual = unet(sample=noisy_sample, timestep=2)["sample"]
                less_noisy_sample = scheduler.step(model_output=noisy_residual, timestep=2, sample=noisy_sample)["prev_sample"]
                less_noisy_sample.shape
              with torch.no_grad():
                noise_pred = unet(latent_model_input, t, encoder_hidden_states=text_embeddings).images
              # perform guidance
              noise_pred_uncond, noise_pred_text = noise_pred.chunk(2)
              noise_pred = noise_pred_uncond + arg['guidance_scale'] * (noise_pred_text - noise_pred_uncond)
              # compute the previous noisy sample x_t -> x_t-1
              latents = scheduler.step(noise_pred, i, latents)["prev_sample"]#We now use the vae to decode the generated latents back into the image.
            # scale and decode the image latents with vae
            latents = 1 / 0.18215 * latents
            with torch.no_grad():
              image = vae.decode(latents)
            image = (image / 2 + 0.5).clip(0, 1)
            image = image.detach().cpu().permute(0, 2, 3, 1).numpy()
            uint8_images = (image * 255).round().astype("uint8")
            #for img in uint8_images: images.append(Image.fromarray(img))
            images = [PILImage.fromarray(img) for img in uint8_images]
          else:
            if bool(arg['use_clip_guided_model']):
              if bool(arg['init_image']) or bool(arg['mask_image']):
                raise ValueError("Cannot use CLIP Guided Model with init or mask image yet.")
              clear_txt2img_pipe()
              clear_img2img_pipe()
              clear_unet_pipe()
              if pipe_clip_guided is None:
                pipe_clip_guided = get_clip_guided_pipe()
              clip_prompt = arg["clip_prompt"] if arg["clip_prompt"].strip() != "" else None
              if bool(arg["unfreeze_unet"]):
                pipe_clip_guided.unfreeze_unet()
              else:
                pipe_clip_guided.freeze_unet()
              if bool(arg["unfreeze_vae"]):
                pipe_clip_guided.unfreeze_vae()
              else:
                pipe_clip_guided.freeze_vae()
              images = pipe_clip_guided(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], clip_prompt=clip_prompt, clip_guidance_scale=arg["clip_guidance_scale"], num_cutouts=arg["num_cutouts"], use_cutouts=arg["use_cutouts"], generator=generator).images
              '''if prefs['precision'] == "autocast":
                with autocast("cuda"):
                  images = pipe_clip_guided(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], clip_prompt=clip_prompt, clip_guidance_scale=arg["clip_guidance_scale"], num_cutouts=arg["num_cutouts"], use_cutouts=arg["use_cutouts"], generator=generator).images
              else:
                with autocast("cuda"):
                  with torch.no_grad():
                    images = pipe_clip_guided(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], clip_prompt=clip_prompt, clip_guidance_scale=arg["clip_guidance_scale"], num_cutouts=arg["num_cutouts"], use_cutouts=arg["use_cutouts"], generator=generator).images'''
            elif bool(arg['mask_image']):
              if not bool(arg['init_image']):
                prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: You have not selected an init_image to go with your image mask..")
                continue
              clear_txt2img_pipe()
              clear_unet_pipe()
              clear_clip_guided_pipe()
              #clear_img2img_pipe()
              #if pipe_inpainting is None:
              #  pipe_inpainting = get_inpainting_pipe()
              if pipe_img2img is None:
                try:
                  pipe_img2img = get_img2img_pipe()
                except NameError:
                  prt(f"{Color.RED}You must install the image2image Pipeline above.{Color.END}")
                finally:
                  raise NameError("You must install the image2image Pipeline above")
              import requests
              from io import BytesIO
              if arg['init_image'].startswith('http'):
                response = requests.get(arg['init_image'])
                init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
              else:
                if os.path.isfile(arg['init_image']):
                  init_img = PILImage.open(arg['init_image'])
                else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your init_image {arg['init_image']}")
              init_img = init_img.resize((arg['width'], arg['height']))
              #init_image = preprocess(init_img)
              mask_img = None
              if arg['mask_image'].startswith('http'):
                response = requests.get(arg['mask_image'])
                mask_img = PILImage.open(BytesIO(response.content)).convert("RGB")
              else:
                if os.path.isfile(arg['mask_image']):
                  mask_img = PILImage.open(arg['mask_image'])
                else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your mask_image {arg['mask_image']}")
              mask_img = mask_img.convert("L")
              mask_img = mask_img.resize((arg['width'], arg['height']), resample=PILImage.LANCZOS).convert("RGB")
              #mask = mask_img.resize((arg['width'], arg['height']))
              #mask = np.array(mask).astype(np.float32) / 255.0
              #mask = np.tile(mask,(4,1,1))
              #mask = mask[None].transpose(0, 1, 2, 3)
              #mask[np.where(mask != 0.0 )] = 1.0 #make sure mask is actually valid
              #mask_img = torch.from_numpy(mask)
              page.auto_scrolling(False)
              prt(pb)
              #with autocast("cuda"):
              images = pipe_img2img(prompt=pr, negative_prompt=arg['negative_prompt'], mask_image=mask_img, init_image=init_img, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1)["sample"]
              clear_last()
              page.auto_scrolling(True)
            elif bool(arg['init_image']):
              if not status['installed_img2img']:
                prt(f"{Color.RED}{Color.BOLD}CRITICAL ERROR{Color.END}: You have not installed the image2image pipeline yet.  Run cell above..")
                continue
              clear_txt2img_pipe()
              clear_unet_pipe()
              clear_clip_guided_pipe()
              if pipe_img2img is None:
                try:
                  pipe_img2img = get_img2img_pipe()
                except NameError:
                  prt(f"{Color.RED}You must install the image2image Pipeline above.{Color.END}")
                  raise NameError("You must install the image2image Pipeline above")
                #finally:
              import requests
              from io import BytesIO
              if arg['init_image'].startswith('http'):
                response = requests.get(arg['init_image'])
                init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
              else:
                if os.path.isfile(arg['init_image']):
                  init_img = PILImage.open(arg['init_image']).convert("RGB")
                else: prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Couldn't find your init_image {arg['init_image']}")
              init_img = init_img.resize((arg['width'], arg['height']))
              #init_image = preprocess(init_img)
              white_mask = PILImage.new("RGB", (arg['width'], arg['height']), (255, 255, 255))
              page.auto_scrolling(False)
              prt(pb)
              #with autocast("cuda"):
              images = pipe_img2img(prompt=pr, negative_prompt=arg['negative_prompt'], init_image=init_img, mask_image=white_mask, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              clear_last()
              page.auto_scrolling(True)
            elif bool(arg['prompt2']):
              clear_img2img_pipe()
              clear_unet_pipe()
              clear_clip_guided_pipe()
              if pipe is None:
                pipe = get_txt2img_pipe()
              #with precision_scope("cuda"):
              #    with torch.no_grad():
              images_tween = pipe.lerp_between_prompts(pr, arg["prompt2"], length = arg['tweens'], save=False, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator)
              #print(str(images_tween))
              images = images_tween['images']
              #images = pipe(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator)["sample"]
            else:
              clear_img2img_pipe()
              clear_unet_pipe()
              clear_clip_guided_pipe()
              if pipe is None:
                pipe = get_txt2img_pipe()
              '''with io.StringIO() as buf, redirect_stdout(buf):
                get_text2image(page)
                output = buf.getvalue()
                page.Images.content.controls.append(Text(output.strip())
                page.Images.content.update()
                page.Images.update()
                page.update()'''
              total_steps = arg['steps']
              page.auto_scrolling(False)
              prt(pb)
              images = pipe(pr, negative_prompt=arg['negative_prompt'], height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              '''if prefs['precision'] == "autocast":
                with autocast("cuda"):
                  images = pipe(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], seed = arg['seed'], generator=generator, callback=callback_fn, callback_steps=1)["sample"]
              else:
                with precision_scope("cuda"):
                  with torch.no_grad():
                    images = pipe(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], seed = arg['seed'], generator=generator, callback=callback_fn, callback_steps=1)["sample"]'''
              clear_last()
              page.auto_scrolling(True)
        except RuntimeError as e:
          if 'out of memory' in str(e):
            prt(f"{Color.RED}{Color.BOLD}CRITICAL ERROR{Color.END}: GPU ran out of memory! Flushing memory to save session...")
            pass
        finally:
          gc.collect()
          torch.cuda.empty_cache()

      txt2img_output = stable_dir #f'{stable_dir}/stable-diffusion/outputs/txt2img-samples'
      batch_output = prefs['image_output']
      if bool(prefs['batch_folder_name']):
        txt2img_output = os.path.join(stable_dir, prefs['batch_folder_name'])
        if not os.path.exists(txt2img_output):
          os.makedirs(txt2img_output)
        if save_to_GDrive:
          batch_output = os.path.join(prefs['image_output'], prefs['batch_folder_name'])
          if not os.path.exists(batch_output):
            os.makedirs(batch_output)
        if storage_type == "PyDrive Google Drive":
          newFolder = gdrive.CreateFile({'title': prefs['batch_folder_name'], "parents": [{"kind": "drive#fileLink", "id": prefs['image_output']}],"mimeType": "application/vnd.google-apps.folder"})
          newFolder.Upload()
          batch_output = newFolder

      filename = format_filename(pr[0] if type(pr) == list else pr)
      idx = 0
      if images is None:
        prt(f"{Color.RED}{Color.BOLD}ERROR{Color.END}: Problem generating images, check your settings and run above blocks again, or report the error to Skquark if it really seems broken.")
        images = []

      for image in images:
        cur_seed = arg['seed']
        if idx > 0:
          cur_seed += idx
          i_count = f'  ({idx + 1} of {len(images)})  '
          prt(Row([Text(i_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight="bold"), Text(f'seed: {cur_seed}')]))
          #prt(f'{pr[0] if type(pr) == list else pr} - seed:{cur_seed}')
        seed_suffix = "" if not prefs['file_suffix_seed'] else f"-{cur_seed}"
        fname = f'{prefs["file_prefix"]}{filename}{seed_suffix}'
        image_path = available_file(txt2img_output, fname, idx)
        idx = int(image_path.rpartition('-')[2].partition('.')[0])
        #image_path = os.path.join(txt2img_output, f'{fname}-{idx}.png')
        image.save(image_path)
        #print(f'size:{os.path.getsize(f"{fname}-{idx}.png")}')
        if os.path.getsize(image_path) < 2000 or not usable_image: #False: #not sum(image.convert("L").getextrema()) in (0, 2): #image.getbbox():#
          os.remove(os.path.join(txt2img_output, f'{fname}-{idx}.png'))
          if strikes >= retry_attempts_if_NSFW:
            if retry_attempts_if_NSFW != 0: prt("Giving up on finding safe image...")
            strikes = 0
            continue
          else: strikes += 1
          new_dream = None
          if isinstance(p, Dream):
            new_dream = p
            new_dream.prompt = pr[0] if type(pr) == list else pr
            new_dream.arg['seed'] = random.randint(0,4294967295)
          else:
            new_dream = Dream(p, arg=dict(seed=random.randint(0,4294967295)))
          updated_prompts.insert(p_idx+1, new_dream)
          prt(f"Filtered NSFW image, retrying prompt with new seed. Attempt {strikes} of {retry_attempts_if_NSFW}...")
          continue
        else: strikes = 0
        #if not prefs['display_upscaled_image'] or not prefs['apply_ESRGAN_upscale']:
          #print(f"Image path:{image_path}")
          #time.sleep(0.4)
          #prt(Row([Img(src=image_path, width=arg['width'], height=arg['height'], fit="fill", gapless_playback=True)], alignment="center"))
          #display(image)
        #if bool(batch_folder_name):
        #  fpath = os.path.join(txt2img_output, batch_folder_name, f'{fname}-{idx}.png')
        #fpath = os.path.join(txt2img_output, f'{fname}-{idx}.png')
        #fpath = available_file(txt2img_output, fname, idx)
        fpath = image_path
        #print(f'fpath: {fpath} - idx: {idx}')
        if prefs['centipede_prompts_as_init_images']:
          shutil.copy(fpath, os.path.join(root_dir, 'init_images'))
          last_image = os.path.join(root_dir, 'init_images', f'{fname}-{idx}.png')
        if not prefs['display_upscaled_image'] or not prefs['apply_ESRGAN_upscale']:
          #print(f"Image path:{image_path}")
          time.sleep(0.1)
          prt(Row([Img(src=fpath, width=arg['width'], height=arg['height'], fit="fill", gapless_playback=True)], alignment="center"))
          #display(image)
        if prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
          os.chdir(f'{root_dir}Real-ESRGAN')
          upload_folder = 'upload'
          result_folder = 'results'     
          if os.path.isdir(upload_folder):
              shutil.rmtree(upload_folder)
          if os.path.isdir(result_folder):
              shutil.rmtree(result_folder)
          os.mkdir(upload_folder)
          os.mkdir(result_folder)
          short_name = f'{fname[:80]}-{idx}.png'
          dst_path = os.path.join(f'{root_dir}Real-ESRGAN/{upload_folder}', short_name)
          #print(f'Moving {fpath} to {dst_path}')
          #shutil.move(fpath, dst_path)
          shutil.copy(fpath, dst_path)
          faceenhance = ' --face_enhance' if prefs["face_enhance"] else ''
          #python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {enlarge_scale}{faceenhance}
          run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {prefs["enlarge_scale"]}{faceenhance}', cwd=f'{root_dir}Real-ESRGAN', realtime=False)
          out_file = short_name.rpartition('.')[0] + '_out.png'
          #print(f'move {root_dir}Real-ESRGAN/{result_folder}/{out_file} to {fpath}')
          #shutil.move(f'{root_dir}Real-ESRGAN/{result_folder}/{out_file}', fpath)
          shutil.move(f'{root_dir}Real-ESRGAN/{result_folder}/{out_file}', fpath)
          # !python inference_realesrgan.py --model_path experiments/pretrained_models/RealESRGAN_x4plus.pth --input upload --netscale 4 --outscale 3.5 --half --face_enhance
          os.chdir(stable_dir)
        
        config_json = arg.copy()
        del config_json['batch_size']
        del config_json['n_iterations']
        del config_json['precision']
        config_json['prompt'] = pr[0] if type(pr) == list else pr
        config_json['sampler'] = prefs['generation_sampler'] if prefs['use_Stability_api'] else prefs['scheduler_mode']
        if bool(prefs['meta_ArtistName']): config_json['artist'] = prefs['meta_ArtistName']
        if bool(prefs['meta_Copyright']): config_json['copyright'] = prefs['meta_Copyright']
        if prefs['use_Stability_api']: del config_json['eta']
        del config_json['use_Stability']
        if not bool(config_json['negative_prompt']): del config_json['negative_prompt']
        if not bool(config_json['prompt2']):
          del config_json['prompt2']
          del config_json['tweens']
        if not bool(config_json['init_image']):
          del config_json['init_image']
          del config_json['init_image_strength']
        if not bool(config_json['mask_image']):
          del config_json['mask_image']
        if not bool(config_json['use_clip_guided_model']):
          del config_json["use_clip_guided_model"]
          del config_json["clip_prompt"]
          del config_json["clip_guidance_scale"]
          del config_json["num_cutouts"]
          del config_json["use_cutouts"]
          del config_json["unfreeze_unet"]
          del config_json["unfreeze_vae"]
        else:
          config_json["clip_model_id"] = prefs['clip_model_id']
        if prefs['apply_ESRGAN_upscale']:
          config_json['upscale'] = f"Upscaled {prefs['enlarge_scale']}x with ESRGAN" + (" with GFPGAN Face-Enhance" if prefs['face_enhance'] else "")
        if prefs['save_image_metadata']:
          img = PILImage.open(fpath)
          metadata = PngInfo()
          metadata.add_text("artist", prefs['meta_ArtistName'])
          metadata.add_text("copyright", prefs['meta_Copyright'])
          metadata.add_text("software", "Stable Diffusion 1.4" + f", upscaled {prefs['enlarge_scale']}x with ESRGAN" if prefs['apply_ESRGAN_upscale'] else "")
          metadata.add_text("title", pr[0] if type(pr) == list else pr)
          if prefs['save_config_in_metadata']:
            config = f"prompt: {pr[0] if type(pr) == list else pr}, seed: {cur_seed}, steps: {arg['steps']}, CGS: {arg['guidance_scale']}, iterations: {arg['n_iterations']}" + f", eta: {arg['eta']}" if not prefs['use_Stability_api'] else ""
            sampler_str = prefs['generation_sampler'] if prefs['use_Stability_api'] else prefs['scheduler_mode']
            config += f", sampler: {sampler_str}"
            if bool(arg['init_image']): config += f", init_image: {arg['init_image']}, init_image_strength: {arg['init_image_strength']}"
            metadata.add_text("config", config)
            #metadata.add_text("prompt", p)
            metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
          img.save(fpath, pnginfo=metadata)

        new_file = available_file(batch_output if save_to_GDrive else txt2img_output, fname, idx)
        #new_file = fname #.rpartition('.')[0] #f'{file_prefix}{filename}'
        #if os.path.isfile(os.path.join(batch_output if save_to_GDrive else txt2img_output, f'{new_file}-{idx}.png')):
        #  new_file += '-' + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        #new_file += f'-{idx}.png'
        if save_to_GDrive:
          shutil.copy(fpath, os.path.join(batch_output, new_file))
          #shutil.move(fpath, os.path.join(batch_output, new_file))
        elif storage_type == "PyDrive Google Drive":
          #batch_output
          out_file = gdrive.CreateFile({'title': new_file})
          out_file.SetContentFile(fpath)
          out_file.Upload()
        elif bool(prefs['image_output']):
          shutil.copy(fpath, os.path.join(batch_output, new_file))
        if prefs['save_config_json']:
          json_file = new_file.rpartition('.')[0] + '.json'
          with open(f"{stable_dir}/{json_file}", "w") as f:
            json.dump(config_json, f, ensure_ascii=False, indent=4)
          if save_to_GDrive:
            shutil.copy(f'{stable_dir}/{json_file}', os.path.join(batch_output, json_file))
          elif storage_type == "PyDrive Google Drive":
            #batch_output
            out_file = gdrive.CreateFile({'title': json_file})
            out_file.SetContentFile(f'{stable_dir}/{json_file}')
            out_file.Upload()
        output_files.append(os.path.join(batch_output if save_to_GDrive else txt2img_output, new_file))
        if prefs['display_upscaled_image'] and prefs['apply_ESRGAN_upscale']:
          upscaled_path = os.path.join(batch_output if save_to_GDrive else txt2img_output, new_file)
          time.sleep(0.4)
          prt(Row([Img(src=upscaled_path, width=arg['width'] * float(prefs["enlarge_scale"]), height=arg['height'] * float(prefs["enlarge_scale"]), fit="contain", gapless_playback=True)], alignment="center"))
          #prt(Img(src=upscaled_path))
          #upscaled = PILImage.open(os.path.join(batch_output, new_file))
          #display(upscaled)
        #else:
          #time.sleep(0.4)
          #prt(Row([Img(src=new_file, width=arg['width'], height=arg['height'], fit="fill", gapless_playback=True)], alignment="center"))
        prt(Row([Text(fpath.rpartition('/')[2])], alignment="center"))
        idx += 1
      p_idx += 1
    if prefs['enable_sounds']: page.snd_alert.play()
  else:
    clear_txt2img_pipe()
    clear_img2img_pipe()
    clear_unet_pipe()
    clear_clip_guided_pipe()
    if pipe_interpolation is None:
      pipe_interpolation = get_interpolation_pipe()
    txt2img_output = os.path.join(stable_dir, prefs['batch_folder_name'] if bool(prefs['batch_folder_name']) else 'dreams')
    batch_output = prefs['image_output']
    if not os.path.exists(txt2img_output):
      os.makedirs(txt2img_output)
    #dream_name = prefs['batch_folder_name'] if bool(prefs['batch_folder_name']) else None
    #first = prompts[0]
    arg = args.copy()
    arg['width'] = int(arg['width'])
    arg['height'] = int(arg['height'])
    arg['seed'] = int(arg['seed'])
    arg['guidance_scale'] = float(arg['guidance_scale'])
    arg['steps'] = int(arg['steps'])
    arg['eta'] = float(arg['eta'])
    walk_prompts = []
    walk_seeds = []
    for p in prompts:
      walk_prompts.append(p.prompt)
      if int(p.arg['seed']) < 1 or arg['seed'] is None:
        walk_seeds.append(random.randint(0,4294967295))
      else:
        walk_seeds.append(int(p.arg['seed']))
    img_idx = 0
    from watchdog.observers import Observer
    from watchdog.events import LoggingEventHandler
    class Handler(FileSystemEventHandler):
      def __init__(self):
        super().__init__()
      def on_created(self,event):
        nonlocal img_idx
        if event.is_directory:
          return None
        elif event.event_type == 'created':
          clear_last()
          page.auto_scrolling(True)
          #p_count = f'[{img_idx + 1} of {len(walk_prompts)}]  '
          #prt(Divider(height=6, thickness=2))
          #prt(Row([Text(p_count), Text(walk_prompts[img_idx], expand=True, weight="bold"), Text(f'seed: {walk_seeds[img_idx]}')]))
          prt(Row([Img(src=event.src_path, width=arg['width'], height=arg['height'], fit="fill", gapless_playback=True)], alignment="center"))
          prt(Row([Text(f'{event.src_path}')], alignment="center"))
          page.auto_scrolling(False)
          prt(pb)
          img_idx += 1
    image_handler = Handler()
    observer = Observer()
    observer.schedule(image_handler, txt2img_output, recursive = True)
    observer.start()
    page.auto_scrolling(False)
    prt(f"Interpolating latent space between {len(walk_prompts)} prompts with {int(prefs['num_interpolation_steps'])} steps between each.")
    prt(Divider(height=6, thickness=2))
    prt(pb)
    #prt(Row([Text(p_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight="bold"), Text(f'seed: {arg["seed"]}')]))
    images = pipe_interpolation.walk(prompts=walk_prompts, seeds=walk_seeds, num_interpolation_steps=int(prefs['num_interpolation_steps']), batch_size=int(prefs['batch_size']), output_dir=txt2img_output, width=arg['width'], height=arg['height'], guidance_scale=arg['guidance_scale'], num_inference_steps=int(arg['steps']), eta=arg['eta'], callback=callback_fn, callback_steps=1)
    observer.stop()
    clear_last()
    fpath = images[0].rpartition('/')[0]
    bfolder = fpath.rpartition('/')[2]
    if prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
      prt('Applying Real-ESRGAN Upscaling to images...')
      os.chdir(f'{root_dir}Real-ESRGAN')
      upload_folder = 'upload'
      result_folder = 'results'     
      if os.path.isdir(upload_folder):
          shutil.rmtree(upload_folder)
      if os.path.isdir(result_folder):
          shutil.rmtree(result_folder)
      os.mkdir(upload_folder)
      os.mkdir(result_folder)
      for i in images:
        fname = i.rpartition('/')[2]
        dst_path = os.path.join(f'{root_dir}Real-ESRGAN/{upload_folder}', fname)
        shutil.move(i, dst_path)
      faceenhance = ' --face_enhance' if prefs["face_enhance"] else ''
      run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {prefs["enlarge_scale"]}{faceenhance}', cwd=f'{root_dir}Real-ESRGAN', realtime=False)
      filenames = os.listdir(f'{root_dir}/Real-ESRGAN/results')
      for oname in filenames:
        fparts = oname.rpartition('_out')
        fname_clean = fparts[0] + filename_suffix + fparts[2]
        opath = os.path.join(fpath, fname_clean)
        shutil.move(f'{root_dir}Real-ESRGAN/{result_folder}/{oname}', opath)
      os.chdir(stable_dir)
    os.makedir(os.path.join(batch_output, bfolder), exist_ok=True)
    imgs = os.listdir(fpath)
    for i in imgs:
      #prt(f'Created {i}')
      #fname = i.rpartition('/')[2]
      if save_to_GDrive:
        shutil.copy(os.path.join(fpath, i), os.path.join(batch_output, bfolder, i))
      elif storage_type == "PyDrive Google Drive":
        #batch_output
        out_file = gdrive.CreateFile({'title': i})
        out_file.SetContentFile(fpath)
        out_file.Upload()
      elif bool(prefs['image_output']):
        shutil.copy(os.path.join(fpath, i), os.path.join(batch_output, i))
    if prefs['enable_sounds']: page.snd_alert.play()



artists = ( "Ivan Aivazovsky", "Beeple", "Zdzislaw Beksinski", "Albert Bierstadt", "Noah Bradley", "Jim Burns", "John Harris", "John Howe", "Thomas Kinkade", "Gediminas Pranckevicius", "Andreas Rocha", "Marc Simonetti", "Simon Stalenhag", "Yuumei", "Asher Brown Durand", "Tyler Edlin", "Jesper Ejsing", "Peter Mohrbacher", "RHADS", "Greg Rutkowski", "H.P. Lovecraft", "George Lucas", "Benoit B. Mandelbrot", "Edwin Austin Abbey", "Ansel Adams", "Arthur Adams", "Charles Addams", "Alena Aenami", "Pieter Aertsen", "Hilma af Klint", "Affandi", "Leonid Afremov", "Eileen Agar", "Ivan Aivazovsky", "Anni Albers", "Josef Albers", "Ivan Albright", "Yoshitaka Amano", "Cuno Amiet", "Sophie Anderson", "Wes Anderson", "Esao Andrews", "Charles Angrand", "Sofonisba Anguissola", "Hirohiko Araki", "Nobuyoshi Araki", "Shinji Aramaki", "Diane Arbus", "Giuseppe Arcimboldo", "Steve Argyle", "Jean Arp", "Artgerm", "John James Audubon", "Frank Auerbach", "Milton Avery", "Tex Avery", "Harriet Backer", "Francis Bacon", "Peter Bagge", "Tom Bagshaw", "Karol Bak", "Christopher Balaskas", "Hans Baldung", "Ronald Balfour", "Giacomo Balla", "Banksy", "Cicely Mary Barker", "Carl Barks", "Wayne Barlowe", "Jean-Michel Basquiat", "Jules Bastien-Lepage", "David Bates", "John Bauer", "Aubrey Beardsley", "Jasmine Becket-Griffith", "Max Beckmann", "Beeple", "Zdzislaw Beksinski", "Zdzisław Beksiński", "Julie Bell", "Hans Bellmer", "John Berkey", "Émile Bernard", "Elsa Beskow", "Albert Bierstadt", "Enki Bilal", "Ivan Bilibin", "Simon Bisley", "Charles Blackman", "Thomas Blackshear", "Mary Blair", "Quentin Blake", "William Blake", "Antoine Blanchard", "John Blanche", "Pascal Blanché", "Karl Blossfeldt", "Don Bluth", "Umberto Boccioni", "Arnold Böcklin", "Chesley Bonestell", "Franklin Booth", "Guido Borelli da Caluso", "Marius Borgeaud", "Hieronymous Bosch", "Hieronymus Bosch", "Sam Bosma", "Johfra Bosschart", "Sandro Botticelli", "William-Adolphe Bouguereau", "Louise Bourgeois", "Eleanor Vere Boyle", "Noah Bradley", "Victor Brauner", "Austin Briggs", "Raymond Briggs", "Mark Briscoe", "Romero Britto", "Gerald Brom", "Mark Brooks", "Patrick Brown", "Pieter Bruegel the Elder", "Bernard Buffet", "Laurel Burch", "Charles E. Burchfield", "David Burdeny", "Richard Burlet", "David Burliuk", "Edward Burne-Jones", "Jim Burns", "William S. Burroughs", "Gaston Bussière", "Kaethe Butcher", "Jack Butler Yeats", "Bob Byerley", "Alexandre Cabanel", "Ray Caesar", "Claude Cahun", "Zhichao Cai", "Randolph Caldecott", "Alexander Milne Calder", "Clyde Caldwell", "Eddie Campbell", "Pascale Campion", "Canaletto", "Caravaggio", "Annibale Carracci", "Carl Gustav Carus", "Santiago Caruso", "Mary Cassatt", "Paul Cézanne", "Marc Chagall", "Marcel Chagall", "Yanjun Cheng", "Sandra Chevrier", "Judy Chicago", "James C. Christensen", "Frederic Church", "Mikalojus Konstantinas Ciurlionis", "Pieter Claesz", "Amanda Clark", "Harry Clarke", "Thomas Cole", "Mat Collishaw", "John Constable", "Cassius Marcellus Coolidge", "Richard Corben", "Lovis Corinth", "Joseph Cornell", "Camille Corot", "cosmic nebulae", "Gustave Courbet", "Lucas Cranach the Elder", "Walter Crane", "Craola", "Gregory Crewdson", "Henri-Edmond Cross", "Robert Crumb", "Tivadar Csontváry Kosztka", "Krenz Cushart", "Leonardo da Vinci", "Richard Dadd", "Louise Dahl-Wolfe", "Salvador Dalí", "Farel Dalrymple", "Geof Darrow", "Honoré Daumier", "Jack Davis", "Marc Davis", "Stuart Davis", "Craig Davison", "Walter Percy Day", "Pierre Puvis de Chavannes", "Giorgio de Chirico", "Pieter de Hooch", "Elaine de Kooning", "Willem de Kooning", "Evelyn De Morgan", "Henri de Toulouse-Lautrec", "Richard Deacon", "Roger Dean", "Michael Deforge", "Edgar Degas", "Lise Deharme", "Eugene Delacroix", "Beauford Delaney", "Sonia Delaunay", "Nicolas Delort", "Paul Delvaux", "Jean Delville", "Martin Deschambault", "Brian Despain", "Vincent Di Fate", "Steve Dillon", "Walt Disney", "Tony DiTerlizzi", "Steve Ditko", "Anna Dittmann", "Otto Dix", "Óscar Domínguez", "Russell Dongjun Lu", "Stanley Donwood", "Gustave Doré", "Dave Dorman", "Arthur Dove", "Richard Doyle", "Tim Doyle", "Philippe Druillet", "Joseph Ducreux", "Edmund Dulac", "Asher Brown Durand", "Albrecht Dürer", "Thomas Eakins", "Eyvind Earle", "Jeff Easley", "Tyler Edlin", "Jason Edmiston", "Les Edwards", "Bob Eggleton", "Jesper Ejsing", "El Greco", "Olafur Eliasson", "Harold Elliott", "Dean Ellis", "Larry Elmore", "Peter Elson", "Ed Emshwiller", "Kilian Eng", "James Ensor", "Max Ernst", "Elliott Erwitt", "M.C. Escher", "Richard Eurich", "Glen Fabry", "Anton Fadeev", "Shepard Fairey", "John Philip Falter", "Lyonel Feininger", "Joe Fenton", "Agustín Fernández", "Roberto Ferri", "Hugh Ferriss", "David Finch", "Virgil Finlay", "Howard Finster", "Anton Otto Fischer", "Paul Gustav Fischer", "Paul Gustave Fischer", "Art Fitzpatrick", "Dan Flavin", "Kaja Foglio", "Phil Foglio", "Chris Foss", "Hal Foster", "Jean-Honoré Fragonard", "Victoria Francés", "Lisa Frank", "Frank Frazetta", "Kelly Freas", "Lucian Freud", "Caspar David Friedrich", "Brian Froud", "Wendy Froud", "Ernst Fuchs", "Goro Fujita", "Henry Fuseli", "Thomas Gainsborough", "Emile Galle", "Stephen Gammell", "Hope Gangloff", "Antoni Gaudi", "Antoni Gaudí", "Jack Gaughan", "Paul Gauguin", "Giovanni Battista Gaulli", "Nikolai Ge", "Emma Geary", "Anne Geddes", "Jeremy Geddes", "Artemisia Gentileschi", "Justin Gerard", "Jean-Leon Gerome", "Jean-Léon Gérôme", "Atey Ghailan", "Alberto Giacometti", "Donato Giancola", "Dave Gibbons", "H. R. Giger", "James Gilleard", "Jean Giraud", "Milton Glaser", "Warwick Goble", "Andy Goldsworthy", "Hendrick Goltzius", "Natalia Goncharova", "Rob Gonsalves", "Josan Gonzalez", "Edward Gorey", "Arshile Gorky", "Francisco Goya", "J. J. Grandville", "Jane Graverol", "Mab Graves", "Laurie Greasley", "Kate Greenaway", "Alex Grey", "Peter Gric", "Carne Griffiths", "John Atkinson Grimshaw", "Henriette Grindat", "Matt Groening", "William Gropper", "George Grosz", "Matthias Grünewald", "Rebecca Guay", "James Gurney", "Philip Guston", "Sir James Guthrie", "Zaha Hadid", "Ernst Haeckel", "Sydney Prior Hall", "Asaf Hanuka", "Tomer Hanuka", "David A. Hardy", "Keith Haring", "John Harris", "Lawren Harris", "Marsden Hartley", "Ryohei Hase", "Jacob Hashimoto", "Martin Johnson Heade", "Erich Heckel", "Michael Heizer", "Steve Henderson", "Patrick Heron", "Ryan Hewett", "Jamie Hewlett", "Brothers Hildebrandt", "Greg Hildebrandt", "Tim Hildebrandt", "Miho Hirano", "Adolf Hitler", "Hannah Hoch", "David Hockney", "Filip Hodas", "Howard Hodgkin", "Ferdinand Hodler", "William Hogarth", "Katsushika Hokusai", "Carl Holsoe", "Winslow Homer", "Edward Hopper", "Aaron Horkey", "Kati Horna", "Ralph Horsley", "John Howe", "John Hoyland", "Arthur Hughes", "Edward Robert Hughes", "Friedensreich Regentag Dunkelbunt Hundertwasser", "Hundertwasser", "William Henry Hunt", "Louis Icart", "Ismail Inceoglu", "Bjarke Ingels", "George Inness", "Shotaro Ishinomori", "Junji Ito", "Johannes Itten", "Ub Iwerks", "Alexander Jansson", "Jarosław Jaśnikowski", "James Jean", "Ruan Jia", "Martine Johanna", "Richard S. Johnson", "Jeffrey Catherine Jones", "Peter Andrew Jones", "Kim Jung Gi", "Joe Jusko", "Frida Kahlo", "M.W. Kaluta", "Wassily Kandinsky", "Terada Katsuya", "Audrey Kawasaki", "Hasui Kawase", "Zhang Kechun", "Felix Kelly", "John Frederick Kensett", "Rockwell Kent", "Hendrik Kerstens", "Brian Kesinger", "Jeremiah Ketner", "Adonna Khare", "Kitty Lange Kielland", "Thomas Kinkade", "Jack Kirby", "Ernst Ludwig Kirchner", "Tatsuro Kiuchi", "Mati Klarwein", "Jon Klassen", "Paul Klee", "Yves Klein", "Heinrich Kley", "Gustav Klimt", "Daniel Ridgway Knight", "Nick Knight", "Daniel Ridgway Knights", "Ayami Kojima", "Oskar Kokoschka", "Käthe Kollwitz", "Satoshi Kon", "Jeff Koons", "Konstantin Korovin", "Leon Kossoff", "Hugh Kretschmer", "Barbara Kruger", "Alfred Kubin", "Arkhyp Kuindzhi", "Kengo Kuma", "Yasuo Kuniyoshi", "Yayoi Kusama", "Ilya Kuvshinov", "Chris LaBrooy", "Raphael Lacoste", "Wilfredo Lam", "Mikhail Larionov", "Abigail Larson", "Jeffrey T. Larson", "Carl Larsson", "Dorothy Lathrop", "John Lavery", "Edward Lear", "André Leblanc", "Bastien Lecouffe-Deharme", "Alan Lee", "Jim Lee", "Heinrich Lefler", "Paul Lehr", "Edmund Leighton", "Frederick Lord Leighton", "Jeff Lemire", "Isaac Levitan", "J.C. Leyendecker", "Roy Lichtenstein", "Rob Liefeld", "Malcolm Liepke", "Jeremy Lipking", "Filippino Lippi", "Laurie Lipton", "Michal Lisowski", "Scott Listfield", "Cory Loftis", "Travis Louie", "George Luks", "Dora Maar", "August Macke", "Margaret Macdonald Mackintosh", "Clive Madgwick", "Lee Madgwick", "Rene Magritte", "Don Maitz", "Kazimir Malevich", "Édouard Manet", "Jeremy Mann", "Sally Mann", "Franz Marc", "Chris Mars", "Otto Marseus van Schrieck", "John Martin", "Masaaki Masamoto", "André Masson", "Henri Matisse", "Leiji Matsumoto", "Taiyō Matsumoto", "Roberto Matta", "Rodney Matthews", "David B. Mattingly", "Peter Max", "Marco Mazzoni", "Robert McCall", "Todd McFarlane", "Ryan McGinley", "Dave McKean", "Kelly McKernan", "Angus McKie", "Ralph McQuarrie", "Ian McQue", "Syd Mead", "Józef Mehoffer", "Eddie Mendoza", "Adolph Menzel", "Maria Sibylla Merian", "Daniel Merriam", "Jean Metzinger", "Michelangelo", "Mike Mignola", "Frank Miller", "Ian Miller", "Russ Mills", "Victor Adame Minguez", "Joan Miro", "Kentaro Miura", "Paula Modersohn-Becker", "Amedeo Modigliani", "Moebius", "Peter Mohrbacher", "Piet Mondrian", "Claude Monet", "Jean-Baptiste Monge", "Kent Monkman", "Alyssa Monks", "Sailor Moon", "Chris Moore", "Gustave Moreau", "William Morris", "Igor Morski", "John Kenn Mortensen", "Victor Moscoso", "Grandma Moses", "Robert Motherwell", "Alphonse Mucha", "Craig Mullins", "Augustus Edwin Mulready", "Dan Mumford", "Edvard Munch", "Gabriele Münter", "Gerhard Munthe", "Takashi Murakami", "Patrice Murciano", "Go Nagai", "Hiroshi Nagai", "Tibor Nagy", "Ted Nasmith", "Alice Neel", "Odd Nerdrum", "Mikhail Nesterov", "C. R. W. Nevinson", "Helmut Newton", "Victo Ngai", 
           "Dustin Nguyen", "Kay Nielsen", "Tsutomu Nihei", "Yasushi Nirasawa", "Sidney Nolan", "Emil Nolde", "Sven Nordqvist", "Earl Norem", "Marianne North", "Georgia O'Keeffe", "Terry Oakes", "Takeshi Obata", "Eiichiro Oda", "Koson Ohara", "Noriyoshi Ohrai", "Marek Okon", "Méret Oppenheim", "Katsuhiro Otomo", "Shohei Otomo", "Siya Oum", "Ida Rentoul Outhwaite", "James Paick", "David Palumbo", "Michael Parkes", "Keith Parkinson", "Maxfield Parrish", "Alfred Parsons", "Max Pechstein", "Agnes Lawrence Pelton", "Bruce Pennington", "John Perceval", "Gaetano Pesce", "Coles Phillips", "Francis Picabia", "Pablo Picasso", "Mauro Picenardi", "Anton Pieck", "Bonnard Pierre", "Yuri Ivanovich Pimenov", "Robert Antoine Pinchon", "Giovanni Battista Piranesi", "Camille Pissarro", "Patricia Polacco", "Jackson Pollock", "Lyubov Popova", "Candido Portinari", "Beatrix Potter", "Beatrix Potter", "Gediminas Pranckevicius", "Dod Procter", "Howard Pyle", "Arthur Rackham", "Alice Rahon", "Paul Ranson", "Raphael", "Robert Rauschenberg", "Man Ray", "Odilon Redon", "Pierre-Auguste Renoir", "Ilya Repin", "RHADS", "Gerhard Richter", "Diego Rivera", "Hubert Robert", "Andrew Robinson", "Charles Robinson", "W. Heath Robinson", "Andreas Rocha", "Norman Rockwell", "Nicholas Roerich", "Conrad Roset", "Bob Ross", "Jessica Rossier", "Ed Roth", "Mark Rothko", "Georges Rouault", "Henri Rousseau", "Luis Royo", "Jakub Rozalski", "Joao Ruas", "Peter Paul Rubens", "Mark Ryden", "Jan Pietersz Saenredam", "Pieter Jansz Saenredam", "Kay Sage", "Apollonia Saintclair", "John Singer Sargent", "Martiros Saryan", "Masaaki Sasamoto", "Thomas W Schaller", "Miriam Schapiro", "Yohann Schepacz", "Egon Schiele", "Karl Schmidt-Rottluff", "Charles Schulz", "Charles Schulz", "Carlos Schwabe", "Sean Scully", "Franz Sedlacek", "Maurice Sendak", "Zinaida Serebriakova", "Georges Seurat", "Ben Shahn", "Barclay Shaw", "E. H. Shepard", "Cindy Sherman", "Makoto Shinkai", "Yoji Shinkawa", "Chiharu Shiota", "Masamune Shirow", "Ivan Shishkin", "Bill Sienkiewicz", "Greg Simkins", "Marc Simonetti", "Kevin Sloan", "Adrian Smith", "Douglas Smith", "Jeffrey Smith", "Pamela Coleman Smith", "Zack Snyder", "Simeon Solomon", "Joaquín Sorolla", "Ettore Sottsass", "Chaïm Soutine", "Austin Osman Spare", "Sparth ", "Art Spiegelman", "Simon Stalenhag", "Ralph Steadman", "William Steig", "Joseph Stella", "Irma Stern", "Anne Stokes", "James Stokoe", "William Stout", "George Stubbs", "Tatiana Suarez", "Ken Sugimori", "Hiroshi Sugimoto", "Brian Sum", "Matti Suuronen", "Raymond Swanland", "Naoko Takeuchi", "Rufino Tamayo", "Shaun Tan", "Yves Tanguay", "Henry Ossawa Tanner", "Dorothea Tanning", "Ben Templesmith", "theCHAMBA", "Tom Thomson", "Storm Thorgerson", "Bridget Bate Tichenor", "Louis Comfort Tiffany", "Tintoretto", "James Tissot", "Titian", "Akira Toriyama", "Ross Tran", "Clovis Trouille", "J.M.W. Turner", "James Turrell", "Daniela Uhlig", "Boris Vallejo", "Gustave Van de Woestijne", "Frits Van den Berghe", "Anthony van Dyck", "Jan van Eyck", "Vincent Van Gogh", "Willem van Haecht", "Rembrandt van Rijn", "Jacob van Ruisdael", "Salomon van Ruysdael", "Theo van Rysselberghe", "Remedios Varo", "Viktor Vasnetsov", "Kuno Veeber", "Diego Velázquez", "Giovanni Battista Venanzi", "Johannes Vermeer", "Alexej von Jawlensky", "Marianne von Werefkin", "Hendrick Cornelisz Vroom", "Mikhail Vrubel", "Louis Wain", "Ron Walotsky", "Andy Warhol", "John William Waterhouse", "Jean-Antoine Watteau", "George Frederic Watts", "Max Weber", "Gerda Wegener", "Edward Weston", "Michael Whelan", "James Abbott McNeill Whistler", "Tim White", "Coby Whitmore", "John Wilhelm", "Robert Williams", "Al Williamson", "Carel Willink", "Mike Winkelmann", "Franz Xaver Winterhalter", "Klaus Wittmann", "Liam Wong", "Paul Wonner", "Ashley Wood", "Grant Wood", "Patrick Woodroffe", "Frank Lloyd Wright", "Bernie Wrightson", "Andrew Wyeth", "Qian Xuan", "Takato Yamamoto", "Liu Ye", "Jacek Yerka", "Akihiko Yoshida", "Hiroshi Yoshida", "Skottie Young", "Konstantin Yuon", "Yuumei", "Amir Zand", "Fenghua Zhong", "Nele Zirnite", "Anders Zorn") 
styles = ( "1970s era", "2001: A Space Odyssey", "60s kitsch and psychedelia", "Aaahh!!! Real Monsters", "abstract illusionism", "afrofuturism", "alabaster", "alhambresque", "ambrotype", "american romanticism", "amethyst", "amigurumi", "anaglyph effect", "anaglyph filter", "Ancient Egyptian", "ancient Greek architecture", "anime", "art nouveau", "astrophotography", "at dawn", "at dusk", "at high noon", "at night", "atompunk", "aureolin", "avant-garde", "Avatar The Last Airbender", "Babylonian", "Baker-Miller pink", "Baroque", "Bauhaus", "biopunk", "bismuth", "Blade Runner 2049", "blueprint", "bokeh", "bonsai", "bright", "bronze", "brutalism", "burgundy", "Byzantine", "calotype", "Cambrian", "camcorder effect", "carmine", "cassette futurism", "cassettepunk", "catholicpunk", "cerulean", "chalk art", "chartreuse", "chiaroscuro", "chillwave", "chromatic aberration", "chrome", "Cirque du Soleil", "claymation", "clockpunk", "cloudpunk", "cobalt", "colored pencil art", "Concept Art World", "copper patina", "copper verdigris", "Coraline", "cosmic horror", "cottagecore", "crayon art", "crimson", "CryEngine", "crystalline lattice", "cubic zirconia", "cubism", "cyanotype", "cyber noir", "cyberpunk", "cyclopean masonry", "daguerreotype", "Danny Phantom", "dark academia", "dark pastel", "dark rainbow", "DayGlo", "decopunk", "Dexter's Lab", "diamond", "dieselpunk", "Digimon", "digital art", "doge", "dollpunk", "Doom engine", "Dreamworks", "dutch golden age", "Egyptian", "eldritch", "emerald", "empyrean", "Eraserhead", "ethereal", "expressionism", "Fantastic Planet", "Fendi", "figurativism", "fire", "fisheye lens", "fluorescent", "forestpunk", "fractal manifold", "fractalism", "fresco", "fuchsia", "futuresynth", "Game of Thrones", "german romanticism", "glitch art", "glittering", "golden", "golden hour", "gothic", "gothic art", "graffiti", "graphite", "grim dark", "Harry Potter", "holography", "Howl’s Moving Castle", "hygge", "hyperrealism", "icy", "ikebana", "impressionism", "in Ancient Egypt", "in Egypt", "in Italy", "in Japan", "in the Central African Republic", "in the desert", "in the jungle", "in the swamp", "in the tundra", "incandescent", "indigo", "infrared", "Interstellar", "inverted colors", "iridescent", "iron", "islandpunk", "isotype", "Kai Fine Art", "khaki", "kokedama", "Korean folk art", "lapis lazuli", "Lawrence of Arabia", "leather", "leopard print", "lilac", "liminal space", "long exposure", "Lord of the Rings", "Louis Vuitton", "Lovecraftian", "low poly", "mac and cheese", "macro lens", "magenta", "magic realism", "manga", "mariachi", "marimekko", "maroon", "Medieval", "Mediterranean", "modernism", "Monster Rancher", "moonstone", "Moulin Rouge!", "multiple exposure", "Myst", "nacreous", "narrative realism", "naturalism", "neon", "Nosferatu", "obsidian", "oil and canvas", "opalescent", "optical illusion", "optical art", "organometallics", "ossuary", "outrun", "Paleolithic", "Pan's Labyrinth", "pastel", "patina", "pearlescent", "pewter", "Pixar", "Play-Doh", "pointillism", "Pokemon", "polaroid", "porcelain", "positivism", "postcyberpunk", "Pride & Prejudice", "prismatic", "pyroclastic flow", "Quake engine", "quartz", "rainbow", "reflective", "Renaissance", "retrowave", "Rococo", "rococopunk", "ruby", "rusty", "Salad Fingers", "sapphire", "scarlet", "shimmering", "silk", "sketched", "Slenderman", "smoke", "snakeskin", "Spaceghost Coast to Coast", "stained glass", "Star Wars", "steampunk", "steel", "steelpunk", "still life", "stonepunk", "Stranger Things", "street art", "stuckism", "Studio Ghibli", "Sumerian", "surrealism", "symbolism", "synthwave", "telephoto lens", "thalassophobia", "thangka", "the matrix", "tiger print", "tilt-shift", "tintype", "tonalism", "Toonami", "turquoise", "Ukiyo-e", "ultramarine", "ultraviolet", "umber", "underwater photography", "Unreal Engine", "vantablack", "vaporwave", "verdigris", "Versacci", "viridian", "wabi-sabi", "watercolor painting", "wooden", "x-ray photography", "minimalist", "dadaist", "neo-expressionist", "post-impressionist", "hyper real", "Art brut", "3D rendering", "uncanny valley", "fractal landscape", "fractal flames", "Mandelbulb", "inception dream", "waking life", "occult inscriptions", "barr relief", "marble sculpture", "wood carving", "church stained glass", "Japanese jade", "Zoetrope", "beautiful", "wide-angle", "Digital Painting", "glossy reflections", "cinematic", "spooky", "Digital paint concept art", "dramatic", "global illumination", "immaculate", "woods", ) 

#Code a function in Python programming language named list_variations, which takes a list and returns a set of lists with possible permutations of the list. Example list_variations([1,2,3]) returns [[1,2,3],[1,2],[1,3],[2,3],[1],[2],[3]] */
def list_variations(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result
#print(str(list_variations([1,2,3])))
def and_list(lst):
  return " and ".join([", ".join(lst[:-1]),lst[-1]] if len(lst) > 2 else lst)

generator_request_modes = ["visually detailed",
  "with long detailed colorful interesting artistic scenic visual descriptions",
  "that is highly detailed, artistically interesting, describes a scene, colorful poetic language, with intricate visual descriptions",
  "that are strange, descriptive, graphically visual, full of interesting subjects described in great detail, painted by an artist",
  "that is technical, wordy, extra detailed, confusingly tangental, colorfully worded, dramatically narrative",
  "that is creative, imaginative, funny, interesting, scenic, dark, witty, visual, unexpected, wild",
  "that includes many subjects with descriptions, color details, artistic expression, point of view",
  "complete sentence using many words to describe a landscape in an epic fantasy genre that includes a lot adjectives",]

def run_prompt_generator(page):
  import random as rnd
  global artists, styles
  try:
    import openai
    openai.api_key = prefs['OpenAI_api_key']
  except:
    pass
  prompts_gen = []
  prompt_results = []
  subject = ""
  if bool(prefs['prompt_generator']['subject_detail']):
      subject = ", and " + prefs['prompt_generator']['subject_detail']

  def prompt_gen():
    prompt = f'''Write a list of {prefs['prompt_generator']['amount'] if prefs['prompt_generator']['phrase_as_subject'] else (prefs['prompt_generator']['amount'] + 4)} image generation prompts about "{prefs['prompt_generator']['phrase']}"{subject}, {generator_request_modes[int(prefs['prompt_generator']['request_mode'])]}, and unique without repetition:

'''
    #print(prompt)
    if prefs['prompt_generator']['phrase_as_subject']:
      prompt += "\n*"
    else:
      prompt += f"""* A beautiful painting of a serene landscape with a river running through it, lush trees, golden sun illuminating
* Fireflies illuminating autumnal woods, an Autumn in the Brightwood glade, with warm yellow lantern lights
* The Fabric of spacetime continuum over a large cosmological vista, pieces of dark matter, space dust and nebula doted with small dots that seem to form fractal patterns and glowing bright lanterns in distances, also with an stardust effect towards the plane of the galaxy
* Midnight landscape painting of a city under a starry sky, owl in the shaman forest knowing the ways of magic, warm glow over the buildings
* {prefs['prompt_generator']['phrase']}"""
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2400, temperature=prefs['prompt_generator']['AI_temperature'], presence_penalty=1)
    #print(response)
    result = response["choices"][0]["text"].strip()
    #if result[-1] == '.': result = result[:-1]
    #print(str(result))
    for p in result.split('\n'):
      pr = p.strip()
      if not bool(pr): continue
      if pr[-1] == '.': pr = pr[:-1]
      if pr[0] == '*': pr = pr[2:]
      elif '.' in pr: # Sometimes got 1. 2.
        pr = pr.partition('.')[2].strip()
      if '"' in pr: pr = pr.replace('"', '')
      prompt_results.append(pr)
  #print(f"Request mode influence: {request_modes[prefs['prompt_generator']['request_mode']]}\n")
  
  prompt_gen()
  if len(prompt_results) < prefs['prompt_generator']['amount']:
    additional = prefs['prompt_generator']['amount'] - len(prompt_results)
    print(f"Didn't make enough prompts.. Needed {additional} more.")
  n=1
  for p in prompt_results:
    random_artist=[]
    for a in range(prefs['prompt_generator']['random_artists']):
      random_artist.append(rnd.choice(artists))
    #print(list_variations(random_artist))
    artist = " and ".join([", ".join(random_artist[:-1]),random_artist[-1]] if len(random_artist) > 2 else random_artist)
    random_style = []
    for s in range(prefs['prompt_generator']['random_styles']):
      random_style.append(rnd.choice(styles))
    style = ", ".join(random_style)
    if not prefs['prompt_generator']['phrase_as_subject'] and n == 1:
      p = prefs['prompt_generator']['phrase'] + " " + p
    text_prompt = p
    if prefs['prompt_generator']['random_artists'] > 0: text_prompt += f", by {artist}"
    if prefs['prompt_generator']['random_styles'] > 0: text_prompt += f", style of {style}"
    if prefs['prompt_generator']['random_styles'] != 0 and prefs['prompt_generator']['permutate_artists']:
      prompts_gen.append(text_prompt)
    if prefs['prompt_generator']['permutate_artists']:
      for a in list_variations(random_artist):
        prompt_variation = p + f", by {and_list(a)}"
        prompts_gen.append(prompt_variation)
      if prefs['prompt_generator']['random_styles'] > 0:
        prompts_gen.append(p + f", style of {style}")
    else: prompts_gen.append(text_prompt)
    n += 1
  for item in prompts_gen:
    page.add_to_prompt_generator(item)
    #print(f'   "{item}",')

remixer_request_modes = [
      "visually detailed wording, flowing sentences, extra long descriptions",
      "that is similar but with more details, themes, imagination, interest, subjects, artistic style, poetry, tone, settings, adjectives, visualizations",
      "that is completely rewritten, inspired by, paints a complete picture of an artistic seen",
      "with detailed colorful interesting artistic scenic visual descriptions, described to a blind person",
      "that is highly detailed, artistically interesting, describes a scene, colorful poetic language, with intricate visual descriptions",
      "that replaces every noun, adjective, verb, pronoun, with related words",
      "that is strange, descriptive, graphically visual, full of interesting subjects described in great detail, painted by an artist",
      "that is highly technical, extremely wordy, extra detailed, confusingly tangental, colorfully worded, dramatically narrative",
      "that is creative, imaginative, funny, interesting, scenic, dark, witty, visual, unexpected, wild",
      "that includes more subjects with descriptions, textured color details, expressive",]
      #"complete sentence using many words to describe a landscape in an epic fantasy genre that includes a lot adjectives",

def run_prompt_remixer(page):
  import random as rnd
  global artists, styles
  try:
    import openai
    openai.api_key = prefs['OpenAI_api_key']
  except:
    pass
  if '_' in prefs['prompt_remixer']['seed_prompt'] or '_' in prefs['prompt_remixer']['optional_about_influencer']:
    try:
        import nsp_pantry
        from nsp_pantry import nsp_parse
    except ImportError:
        run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py")
    finally:
        import nsp_pantry
        from nsp_pantry import nsp_parse
  prompts_remix = []
  prompt_results = []
  
  if '_' in prefs['prompt_remixer']['seed_prompt']:
    seed_prompt = nsp_parse(prefs['prompt_remixer']['seed_prompt'])
  else:
    seed_prompt = prefs['prompt_remixer']['seed_prompt']
  if '_' in prefs['prompt_remixer']['optional_about_influencer']:
    optional_about_influencer = nsp_parse(prefs['prompt_remixer']['optional_about_influencer'])
  else:
    optional_about_influencer = prefs['prompt_remixer']['optional_about_influencer']
  about =  f" about {optional_about_influencer}" if bool(optional_about_influencer) else ""
  prompt = f'Write a list of {prefs["prompt_remixer"]["amount"]} remixed variations from the following image generation prompt{about}, "{prefs["prompt_remixer"]["seed_prompt"]}", {remixer_request_modes[int(prefs["prompt_remixer"]["request_mode"])]}, and unique without repetition:\n\n*'
  prompt_results = []
  
  def prompt_remix():
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=2400, temperature=prefs["prompt_remixer"]['AI_temperature'], presence_penalty=1)
    #print(response)
    result = response["choices"][0]["text"].strip()
    #if result[-1] == '.': result = result[:-1]
    #print(str(result))
    for p in result.split('\n'):
      pr = p.strip()
      if not bool(pr): continue
      if pr[-1] == '.': pr = pr[:-1]
      if pr[0] == '*': pr = pr[2:]
      elif '.' in pr: # Sometimes got 1. 2.
        pr = pr.partition('.')[2].strip()
      prompt_results.append(pr)
  page.prompt_remixer_list.controls.append(Text(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else "") + f"\nRequest mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n"))
  page.prompt_remixer_list.update()
  #page.add_to_prompt_remixer(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else "") + f"\nRequest mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n")
  #print(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else ""))
  #print(f"Request mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n")
  prompt_remix()
  for p in prompt_results:
    random_artist=[]
    for a in range(prefs['prompt_remixer']['random_artists']):
      random_artist.append(rnd.choice(artists))
    #print(list_variations(random_artist))
    artist = " and ".join([", ".join(random_artist[:-1]),random_artist[-1]] if len(random_artist) > 2 else random_artist)
    random_style = []
    for s in range(prefs['prompt_remixer']['random_styles']):
      random_style.append(rnd.choice(styles))
    style = ", ".join(random_style)
    text_prompt = p
    if prefs['prompt_remixer']['random_artists'] > 0: text_prompt += f", by {artist}"
    if prefs['prompt_remixer']['random_styles'] > 0: text_prompt += f", style of {style}"
    if prefs['prompt_remixer']['random_styles'] == 0 and prefs['prompt_remixer']['permutate_artists']:
      prompts_remix.append(text_prompt)
    if prefs['prompt_remixer']['permutate_artists']:
      for a in list_variations(random_artist):
        prompt_variation = p + f", by {and_list(a)}"
        prompts_remix.append(prompt_variation)
      if prefs['prompt_remixer']['random_styles'] > 0:
        prompts_remix.append(p + f", style of {style}")
    else: prompts_remix.append(text_prompt)
  for item in prompts_remix:
    page.add_to_prompt_remixer(item)

brainstorm_request_modes = {
    "Brainstorm":"Brainstorm visual ideas for an image prompt about ",
    "Write":"Write an interesting visual scene about ",
    "Rewrite":"Rewrite new variations of ",
    "Edit":"Edit this text to improve details and structure: ",
    "Story":"Write an interesting story with visual details and poetic subjects about ",
    "Description":"Describe in graphic detail ",
    "Picture":"Paint a picture with words about ",
    "Raw Request":"",
}

def run_prompt_brainstormer(page):
    import random as rnd
    global artists, styles, brainstorm_request_modes
    textsynth_engine = "gptj_6B" #param ["gptj_6B", "boris_6B", "fairseq_gpt_13B", "gptneox_20B", "m2m100_1_2B"]
    #markdown HuggingFace Bloom AI Settings
    max_tokens_length = 128 #param {type:'slider', min:1, max:64, step:1}
    seed = int(2222 * prefs['prompt_brainstormer']['AI_temperature']) #param {type:'integer'}
    API_URL = "https://api-inference.huggingface.co/models/bigscience/bloom"

    good_key = True
    if prefs['prompt_brainstormer']['AI_engine'] == "TextSynth GPT-J":
      try: 
        if not bool(prefs['TextSynth_api_key']): good_key = False
      except NameError: good_key = False
      if not good_key:
        print(f"\33[91mMissing TextSynth_api_key...\33[0m Define your key up above.")
      else:
        try:
          from textsynthpy import TextSynth, Complete
        except ImportError:
          run_sp("pip install textsynthpy")
          clear_output()
        finally:
          from textsynthpy import TextSynth, Complete
        textsynth = TextSynth(prefs['TextSynth_api_key'], engine=textsynth_engine) # Insert your API key in the previous cell
    if prefs['prompt_brainstormer']['AI_engine'] == "OpenAI GPT-3":
      try:
        if not bool(prefs['OpenAI_api_key']): good_key = False
      except NameError: good_key = False
      if not good_key:
        print(f"\33[91mMissing OpenAI_api_key...\33[0m Define your key up above.")
      else:
        try:
          import openai
        except ImportError:
          run_sp("pip install openai -qq")
          #clear_output()
        finally:
          import openai
        openai.api_key = prefs['OpenAI_api_key']
    if prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Bloom 176B":
      try:
        if not bool(prefs['HuggingFace_api_key']): good_key = False
      except NameError: good_key = False
      if not good_key:
        print(f"\33[91mMissing HuggingFace_api_key...\33[0m Define your key up above.")
    if '_' in prefs['prompt_brainstormer']['about_prompt']:
      try:
        import nsp_pantry
        from nsp_pantry import nsp_parse
      except ImportError:
        run_sp("wget -qq --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py")
      finally:
        import nsp_pantry
        from nsp_pantry import nsp_parse
    #ask_OpenAI_instead = False #@param {type:'boolean'}

    prompt_request_modes = [
        "visually detailed wording, flowing sentences, extra long descriptions",
        "that is similar but with more details, themes, imagination, interest, subjects, artistic style, poetry, tone, settings, adjectives, visualizations",
        "that is completely rewritten, inspired by, paints a complete picture of an artistic seen",
        "with detailed colorful interesting artistic scenic visual descriptions, described to a blind person",
        "that is highly detailed, artistically interesting, describes a scene, colorful poetic language, with intricate visual descriptions",
        "that replaces every noun, adjective, verb, pronoun, with related words",
        "that is strange, descriptive, graphically visual, full of interesting subjects described in great detail, painted by an artist",
        "that is highly technical, extremely wordy, extra detailed, confusingly tangental, colorfully worded, dramatically narrative",
        "that is creative, imaginative, funny, interesting, scenic, dark, witty, visual, unexpected, wild",
        "that includes more subjects with descriptions, textured color details, expressive",]
        #"complete sentence using many words to describe a landscape in an epic fantasy genre that includes a lot adjectives",
    
    request = f'{brainstorm_request_modes[int(prefs["prompt_brainstormer"]["request_mode"])]}"{prefs["prompt_brainstormer"]["about_prompt"]}":' if prefs['prompt_brainstormer']['request_mode'] != "Raw Request" else prefs['prompt_brainstormer']['about_prompt']

    def query(payload):
        #print(payload)
        response = requests.request("POST", API_URL, json=payload, headers={"Authorization": f"Bearer {prefs['HuggingFace_api_key']}"})
        #print(response.text)
        return json.loads(response.content.decode("utf-8"))

    def bloom_request(input_sentence):
        parameters = {
            "max_new_tokens": max_tokens_length,
            "do_sample": False,
            "seed": seed,
            "early_stopping": False,
            "length_penalty": 0.0,
            "eos_token_id": None,}
        payload = {"inputs": input_sentence, "parameters": parameters,"options" : {"use_cache": False} }
        data = query(payload)
        if "error" in data:
            return f"\33[31mERROR: {data['error']}\33[0m"

        generation = data[0]["generated_text"].split(input_sentence, 1)[1]
        #return data[0]["generated_text"]
        return generation
    
    def prompt_brainstormer():
      #(prompt=prompt, temperature=AI_temperature, presence_penalty=1, stop= "\n")
      if prefs['prompt_brainstormer']['AI_engine'] == "TextSynth GPT-J":
        response = textsynth.text_complete(prompt=request, max_tokens=200, temperature=prefs['prompt_brainstormer']['AI_temperature'], presence_penalty=1)
        #print(str(response))
        result = response.text.strip()
      elif prefs['prompt_brainstormer']['AI_engine'] == "OpenAI GPT-3":
        response = openai.Completion.create(engine="text-davinci-002", prompt=request, max_tokens=2400, temperature=prefs['prompt_brainstormer']['AI_temperature'], presence_penalty=1)
        result = response["choices"][0]["text"].strip()
      elif prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Bloom 176B":
        result = bloom_request(request) 
      page.add_to_prompt_brainstormer(str(result) + '\n')
    #print(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else ""))
    if good_key:
      #print(request)
      prompt_brainstormer()

def run_prompt_writer(page):
    try:
        import nsp_pantry
        from nsp_pantry import nsp_parse
    except ModuleNotFoundError:
        run_sp("wget -qq --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py")
        #print(subprocess.run(['wget', '-q', '--show-progress', '--no-cache', '--backups=1', 'https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
    finally:
        import nsp_pantry
        from nsp_pantry import nsp_parse
    import random as rnd
    def generate_prompt():
      text_prompts = []
      global art_Subjects, by_Artists, art_Styles
      nsSubjects = nsp_parse(prefs['prompt_writer']['art_Subjects'])
      nsArtists = nsp_parse(prefs['prompt_writer']['by_Artists'])
      nsStyles = nsp_parse(prefs['prompt_writer']['art_Styles'])
      prompt = nsSubjects
      random_artist=[]
      if nsArtists: random_artist.append(nsArtists)
      for a in range(prefs['prompt_writer']['random_artists']):
        random_artist.append(rnd.choice(artists))
      artist = and_list(random_artist)
      #artist = random.choice(artists) + " and " + random.choice(artists)
      random_style = []
      if prefs['prompt_writer']['art_Styles']: random_style.append(nsStyles)
      for s in range(prefs['prompt_writer']['random_styles']):
        random_style.append(rnd.choice(styles))
      style = ", ".join(random_style)
      subject_prompt = prompt
      if len(artist) > 0: prompt += f", by {artist}"
      if len(style) > 0: prompt += f", style of {style}"
      if not prefs['prompt_writer']['permutate_artists']:
        return prompt
      if prefs['prompt_writer']['random_styles'] > 0 and prefs['prompt_writer']['permutate_artists']:
        text_prompts.append(prompt)
      if prefs['prompt_writer']['permutate_artists']:
        for a in list_variations(random_artist):
          prompt_variation = subject_prompt + f", by {and_list(a)}"
          text_prompts.append(prompt_variation)
        if prefs['prompt_writer']['random_styles'] > 0:
          text_prompts.append(subject_prompt + f", style of {style}")
        return text_prompts
      #if mod_Custom and mod_Custom.strip(): prompt += mod_Custom)
      #return prompt
    prompts_writer = []
    for p in range(prefs['prompt_writer']['amount']):
      prompts_writer.append(generate_prompt())
    for item in prompts_writer:
      if type(item) is str:
        page.add_to_prompt_writer(item)
      if type(item) is list:
        for i in item:
          page.add_to_prompt_writer(i)

def run_upscaling(page):
    #print(str(ESRGAN_prefs))
    if not status['installed_ESRGAN']:
      alert_msg(page, "You must Install Real-ESRGAN first")
      return
    import os, shutil
    import re
    from collections import Counter
    from PIL import Image as PILImage
    enlarge_scale = ESRGAN_prefs['enlarge_scale']
    face_enhance = ESRGAN_prefs['face_enhance']
    image_path = ESRGAN_prefs['image_path']
    save_to_GDrive = ESRGAN_prefs['save_to_GDrive']
    upload_file = ESRGAN_prefs['upload_file']
    download_locally = ESRGAN_prefs['download_locally']
    display_image = ESRGAN_prefs['display_image']
    dst_image_path = ESRGAN_prefs['dst_image_path']
    filename_suffix = ESRGAN_prefs['filename_suffix']
    split_image_grid = ESRGAN_prefs['split_image_grid']
    rows = ESRGAN_prefs['rows']
    cols = ESRGAN_prefs['cols']
    def split(im, rows, cols, img_path, should_cleanup=False):
        im_width, im_height = im.size
        row_width = int(im_width / rows)
        row_height = int(im_height / cols)
        n = 0
        for i in range(0, cols):
            for j in range(0, rows):
                box = (j * row_width, i * row_height, j * row_width +
                      row_width, i * row_height + row_height)
                outp = im.crop(box)
                name, ext = os.path.splitext(img_path)
                outp_path = name + "-" + str(n) + ext
                #print("Exporting image tile: " + outp_path)
                outp.save(outp_path)
                n += 1
        if should_cleanup:
            #print("Cleaning up: " + img_path)
            os.remove(img_path)
    
    os.chdir(f'{root_dir}/Real-ESRGAN')
    upload_folder = 'upload'
    result_folder = 'results'
    if os.path.isdir(upload_folder):
        shutil.rmtree(upload_folder)
    if os.path.isdir(result_folder):
        shutil.rmtree(result_folder)
    os.mkdir(upload_folder)
    os.mkdir(result_folder)

    uploaded = None
    if not upload_file:
      if not image_path:
         alert_msg(page, 'Provide path to image, local or url')
         return
      if '.' in image_path:
        if os.path.exists(image_path):
          uploaded = {image_path: image_path.rpartition('/')[2]}
        else:
          alert_msg(page, 'File does not exist')
          return
      else:
        if os.path.isdir(image_path):
          uploaded = {}
          for f in os.listdir(image_path):
            uploaded[ os.path.join(image_path, f)] = f
        else:
          alert_msg(page, 'Image Path directory does not exist')
          return
    else:
      uploaded = files.upload()
    page.add_to_ESRGAN_output(Text(f"Upscaling {len(uploaded)} images.."))
    for filename in uploaded.keys():
      if not os.path.isfile(filename):
        #print("Skipping " + filename)
        continue
      fname = filename.rpartition('/')[2] if '/' in filename else filename
      dst_path = os.path.join(upload_folder, fname)
      #print(f'Copy {filename} to {dst_path}')
      shutil.copy(filename, dst_path)
      if split_image_grid:
        img = PILImage.open(dst_path)
        split(img, rows, cols, dst_path, True)
    os.chdir(f'{root_dir}/Real-ESRGAN')
    faceenhance = ' --face_enhance' if face_enhance else ''
    run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i {upload_folder} --outscale {enlarge_scale}{faceenhance}', cwd=f'{root_dir}Real-ESRGAN', realtime=False)
    os.chdir(root_dir)
    if is_Colab:
      from google.colab import files
    if not bool(dst_image_path.strip()):
      if os.path.isdir(image_path):
          dst_image_path = image_path
      else:
          dst_image_path = image_path.rpartition('/')[0]
    filenames = os.listdir(f'{root_dir}/Real-ESRGAN/results')
    for fname in filenames:
      fparts = fname.rpartition('_out')
      fname_clean = fparts[0] + filename_suffix + fparts[2]
      #print(f'Copying {fname_clean}')
      if save_to_GDrive:
        if not os.path.isdir(dst_image_path):
          os.makedirs(dst_image_path)
        shutil.copy(os.path.join(f'{root_dir}/Real-ESRGAN/results', fname), os.path.join(dst_image_path, fname_clean))
      if download_locally:
        files.download(f'{root_dir}/Real-ESRGAN/results/'+fname)
      if display_image:
        page.add_to_ESRGAN_output(Image(src=os.path.join(f'{root_dir}/Real-ESRGAN/results', fname)))
      page.add_to_ESRGAN_output(Row([Text(fname_clean)], alignment="center"))

def run_retrieve(page):
    upload_file = retrieve_prefs['upload_file']
    image_path = retrieve_prefs['image_path']
    display_full_metadata = retrieve_prefs['display_full_metadata']
    display_image = retrieve_prefs['display_image']
    add_to_prompts = retrieve_prefs['add_to_prompts']

    import os, json
    import PIL
    from PIL import Image as PILImage
    if is_Colab:
      from google.colab import files
    def meta_dream(meta):
      if meta is not None and len(meta) > 1:
          #d = Dream(meta["prompt"])
          print(str(meta))
          arg = {}
          p = ''
          dream = '    Dream('
          if meta.get('title'):
            dream += f'"{meta["title"]}"'
            p = meta["title"]
          if meta.get('prompt'):
            dream += f'"{meta["prompt"]}"'
            p = meta["prompt"]
          if meta.get('config'):
            meta = meta['config']
          if meta.get('prompt'):
            #dream += f'"{meta["prompt"]}"'
            p = meta["prompt"]
          if meta.get('prompt2'):
            dream += f', prompt2="{meta["prompt2"]}"'
            arg["prompt2"] = meta["prompt2"]
          if meta.get('tweens'):
            dream += f', tweens={meta["tweens"]}'
            arg["tweens"] = meta["tweens"]
          if meta.get('width'):
            dream += f', width={meta["width"]}'
            arg["width"] = meta["width"]
          if meta.get('height'):
            dream += f', height={meta["height"]}'
            arg["height"] = meta["height"]
          if meta.get('guidance_scale'):
            dream += f', guidance_scale={meta["guidance_scale"]}'
            arg["guidance_scale"] = meta["guidance_scale"]
          elif meta.get('CGS'):
            dream += f', guidance_scale={meta["CGS"]}'
            arg["guidance_scale"] = meta["CGS"]
          if meta.get('steps'):
            dream += f', steps={meta["steps"]}'
            arg["steps"] = meta["steps"]
          if meta.get('eta'):
            dream += f', eta={meta["eta"]}'
            arg["eta"] = meta["eta"]
          if meta.get('seed'):
            dream += f', seed={meta["seed"]}'
            arg["seed"] = meta["seed"]
          if meta.get('init_image'):
            dream += f', init_image="{meta["init_image"]}"'
            arg["init_image"] = meta["init_image"]
          if meta.get('mask_image'):
            dream += f', mask_image="{meta["mask_image"]}"'
            arg["mask_image"] = meta["mask_image"]
          if meta.get('init_image_strength'):
            dream += f', init_image_strength={meta["init_image_strength"]}'
            arg["init_image_strength"] = meta["init_image_strength"]
          dream += '),'
          page.add_to_retrieve_output(Text(dream, selectable=True))
          if display_full_metadata:
            page.add_to_retrieve_output(Text(str(metadata)))
          if add_to_prompts:
            page.add_to_prompts(p, arg)
      else:
          alert_msg(page, 'Problem reading your config json image meta data.')
          return
    uploaded = {}
    if not upload_file:
      if not bool(image_path):
        alert_msg(page, 'Provide path to image, local or url')
        return
      if '.' in image_path:
        if os.path.exists(image_path):
          uploaded = {image_path: image_path.rpartition('/')[2]}
        else:
          alert_msg(page, 'File does not exist')
          return
      else:
        if os.path.isdir(image_path):
          uploaded = {}
          for f in os.listdir(image_path):
            uploaded[ os.path.join(image_path, f)] = f
        else:
          alert_msg(page, 'The image_path directory does not exist')
          return
    else:
      if not is_Colab:
        uploaded = files.upload()
        alert_msg(page, "Can't upload an image easily from non-Colab systems")
        return
    if len(uploaded) > 1:
      page.add_to_retrieve_output(Text(f"Revealing Dream of {len(uploaded)} images..\n"))
    for filename in uploaded.keys():
      if not os.path.isfile(filename):
        #print("Skipping subfolder " + filename)
        continue
      print(filename)
      if filename.rpartition('.')[2] == 'json':
        meta = json.load(filename)
        meta_dream(meta)
      elif filename.rpartition('.')[2] == 'png':
        img = PILImage.open(filename)
        metadata = img.info
        if display_image:
          page.add_to_retrieve_output(Image(src=filename))
          #display(img)
        if metadata is None or len(metadata) < 1:
          alert_msg(page, 'Sorry, image has no exif data.')
          return
          #print(metadata)
        else:
          if metadata.get('config_json'):
            json_txt = metadata['config_json']
            #print(json_txt)
            meta = json.loads(json_txt)
            meta_dream(meta)
          elif metadata.get('config'):
            config = metadata['config']
            meta = {}
            key = ""
            val = ""
            if metadata.get('title'):
              meta['prompt'] = metadata['title']
            for col in config.split(':'):
              #print(col.strip())
              if ',' not in col:
                key = col
              else:
                parts = col.rpartition(',')
                val = parts[0].strip()
                if bool(key) and bool(val):
                  meta[key] = val
                  val = ''
                key = parts[2].strip()
            #print(meta)
            meta_dream(meta)
            #print(dream)
          else:
            alert_msg(page, "No Enhanced Stable Diffusion config metadata found inside image.")

def run_initfolder(page):
    prompt_string = initfolder_prefs['prompt_string']
    init_folder = initfolder_prefs['init_folder']
    include_strength = initfolder_prefs['include_strength']
    image_strength = initfolder_prefs['image_strength']
    #init_image='/content/ pic.png', init_image_strength=0.4
    if bool(prompt_string):
      p_str = f'"{prompt_string.strip()}"'
      skip_str = f', init_image_strength={image_strength}' if bool(include_strength) else ''
      if os.path.isdir(init_folder):
        arg = {}
        #print("prompts = [")
        for f in os.listdir(init_folder):
          init_path = os.path.join(init_folder, f)
          if os.path.isdir(init_path): continue
          if f.lower().endswith(('.png', '.jpg', '.jpeg')):
            page.add_to_initfolder_output(Text(f'    Dream({p_str}, init_image="{init_path}"{skip_str}),'))
            arg['init_image'] = init_path
            if bool(include_strength):
              arg['init_image_strength'] = image_strength
            page.add_to_prompts(prompt_string, arg)
        if not bool(status['installed_img2img']):
          alert_msg(page, 'Make sure you Install the Image2Image module before running Stable Diffusion on prompts...')
       # print("]")
      else:
        alert_msg(page, 'The init_folder directory does not exist.')
    else: alert_msg(page, 'Your prompt_string is empty. What do you want to apply to images?')

def main(page: Page):
    page.title = "Stable Diffusion Deluxe - FletUI"
    #page.scroll="auto"
    #page.auto_scroll=True
    def open_help_dlg(e):
        page.dialog = help_dlg
        help_dlg.open = True
        page.update()
    def close_help_dlg(e):
        help_dlg.open = False
        page.update()
    def open_url(e):
        page.launch_url(e.data)
    def exit_disconnect(e):
        save_settings_file(page)
        if is_Colab:
          #run_sp("install pyautogui", realtime=False)
          #import pyautogui
          #pyautogui.hotkey('ctrl', 'w')
          #import keyboard
          #keyboard.press_and_release('ctrl+w')
          #time.sleep(1.5)
          from google.colab import runtime
          runtime.unassign()
          #import time
    help_dlg = AlertDialog(
        title=Text("💁   Help/Information"), content=Column([Text("If you don't now what Stable Diffusion is, you're in for a surprise.. If you're already familiar, you're gonna love how easy it is to be an artist with the help of our AI friends with our pretty interface."),
              Text("Simply go through the self-explanitory tabs step-by-step and set your preferences to get started. The default values are good for most, but you can have some fun experimenting. All values are automatically saved as you make changes and change tabs."),
              Text("Each time you open the app, you should start in the Installers section, turn on all the components you plan on using in you session, then Run the Installers and let them download. You can multitask and work in other tabs while it's installing."),
              Text("In the Prompts List, add as many text prompts as you can think of, and edit any prompt to override any default Image Parameter.  Once you're ready, run diffusion on your prompts list and watch it fill your Google Drive.."),
              Text("Try out any and all of our Prompt Helpers to use practical text AIs to make unique descriptive prompts fast, with our Generator, Remixer, Brainstormer and Advanced Writer.  You'll never run out of inspiration again..."),
        ], scroll="auto"),
        actions=[TextButton("Thanks!", on_click=close_help_dlg)], actions_alignment="end",
    )
    def open_credits_dlg(e):
        page.dialog = credits_dlg
        credits_dlg.open = True
        page.update()
    def close_credits_dlg(e):
        credits_dlg.open = False
        page.update()
    credits_markdown = '''This notebook is an Open-Source side project by [Skquark, Inc.](https://Skquark.com), primarily created by Alan Bedian for fun and functionality.

The real credit goes to the team at [Stability.ai](https://Stability.ai) for making Stable Diffusion so great, and [HuggingFace](https://HuggingFace.co) for their work on the Diffusers Pipeline.

For the great app UI framework, we thank [Flet](https://Flet.dev) with the amazing Flutter based Python library with a very functional dev platform that made this possible.

For the brains behind our Prompt Helpers, we thank our friend [OpenAI GPT-3](https://beta.OpenAI.com), [Bloom-AI](https://huggingface.co/bigscience/bloom) and [TextSynth](https://TextSynth.com) for making an AI so fun to talk to and use.

Shoutouts to the Discord Community of [Disco Diffusion](https://discord.gg/d5ZVbAfm), [Stable Diffusion](https://discord.gg/stablediffusion), and [Flet](https://discord.gg/nFqy742h) for their support and user contributions.'''
    credits_dlg = AlertDialog(
        title=Text("🙌   Credits/Acknowledgments"), content=Column([Markdown(credits_markdown, extension_set="gitHubWeb", on_tap_link=open_url)
        ], scroll="auto"),
        actions=[TextButton("Good Stuff...", on_click=close_credits_dlg)], actions_alignment="end",
    )
    page.theme_mode = prefs['theme_mode'].lower()
    if prefs['theme_mode'] == 'Dark':
      page.dark_theme = theme.Theme(color_scheme_seed=prefs['theme_color'].lower())#, use_material3=True)
    else:
      page.theme = theme.Theme(color_scheme_seed=prefs['theme_color'].lower())
    app_icon_color = colors.AMBER_800
    
    appbar=AppBar(title=Text("👨‍🎨️  Stable Diffusion - Deluxe Edition  🖌️"),elevation=20,
      center_title=True,
          bgcolor=colors.SURFACE_VARIANT,
          leading=IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Save Settings File", on_click=lambda _: app_icon_save()),
          #leading_width=40,
          actions=[
              PopupMenuButton(
                  items=[
                      PopupMenuItem(text="🤔  Help/Info", on_click=open_help_dlg),
                      PopupMenuItem(text="👏  Credits", on_click=open_credits_dlg),
                      PopupMenuItem(text="📨  Email Skquark", on_click=lambda _:page.launch_url("mailto:Alan@Skquark.com")),
                      PopupMenuItem(text="🤑  Offer Donation", on_click=lambda _:page.launch_url("https://paypal.me/StarmaTech")),
                      PopupMenuItem(),
                      PopupMenuItem(text="❎  Exit/Disconnect Runtime", on_click=exit_disconnect) if is_Colab else PopupMenuItem(),
                  ]
              ),
          ])
    page.appbar = appbar
    def app_icon_save():
      app_icon_color = colors.GREEN_800
      appbar.leading = IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Saving Settings File")
      appbar.update()
      time.sleep(0.7)
      #print("Saved Settings")
      #appbar.leading.update()
      app_icon_color = colors.AMBER_800
      appbar.leading = IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Save Settings File", on_click=lambda _: app_icon_save())
      appbar.update()
    page.app_icon_save = app_icon_save
    page.vertical_alignment = "start"
    page.horizontal_alignment = "start"
    t = buildTabs(page)
    t.on_change = tab_on_change
    #(t,page)
    def close_banner(e):
        page.banner.open = False
        page.update()

    page.banner = Banner(bgcolor=colors.SECONDARY_CONTAINER, leading=Icon(icons.DOWNLOADING, color=colors.AMBER, size=40), content=Column([]), actions=[TextButton("Close", on_click=close_banner)])
    def show_banner_click(e):
        page.banner.open = True
        page.update()

    #edit_prompts = Container(Text("Edit Prompt"))
    #page.install_text2img = prefs['install_text2img']
    #page.add(Row([t, IconButton(icon=icons.SAVE)]))
    page.add(t)
    #page.add(ElevatedButton("Show Banner", on_click=show_banner_click))
    #page.add (Text ("Enhanced Stable Diffusion Deluxe by Skquark, Inc."))

class NumberPicker(UserControl):
    def __init__(self, label="", value=1, min=0, max=20, on_change=None):
        super().__init__()
        self.value = value
        self.min = min
        self.max = max
        self.label = label
        self.on_change = on_change
        self.build()
    def build(self):
        def changed(e):
            self.value = int(e.control.value)
            if self.value < self.min:
              self.value = self.min
              self.txt_number.value = self.value
              self.txt_number.update()
            if self.value > self.max:
              self.value = self.max
              self.txt_number.value = self.value
              self.txt_number.update()
            if self.on_change is not None:
              e.control = self
              self.on_change(e)
        def minus_click(e):
            v = int(self.value)
            if v > self.min:
              self.value -= 1
              self.txt_number.value = self.value
              self.txt_number.update()
              e.control = self
              if self.on_change is not None:
                self.on_change(e)
        def plus_click(e):
            v = int(self.value)
            if v < self.max:
              self.value += 1
              self.txt_number.value = self.value
              self.txt_number.update()
              e.control = self
              if self.on_change is not None:
                self.on_change(e)
        self.txt_number = TextField(value=str(self.value), text_align="center", width=55, height=42, content_padding=padding.only(top=4), keyboard_type="number", on_change=changed)
        return Row([Text(self.label), IconButton(icons.REMOVE, on_click=minus_click), self.txt_number, IconButton(icons.ADD, on_click=plus_click)], spacing=1)

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
        return Column(
            controls=[
            ],
        )
class Main:
    def __init__(self):
        self.page = None
    def __call__(self, page: Page):
        self.page = page
        page.title = "Alternative Boot experiment"
        self.add_stuff()
    def add_stuff(self):
        self.page.add(
            Text("Some text", size=20),
        )
        self.page.update()
main = Main()'''

port = 8510
if tunnel_type == "ngrok":
  from pyngrok import ngrok
  public_url = ngrok.connect(port = str(port)).public_url
elif tunnel_type == "localtunnel":
  import re
  localtunnel = subprocess.Popen(['lt', '--port', '80', 'http'], stdout=subprocess.PIPE)
  url = str(localtunnel.stdout.readline())
  public_url = (re.search("(?P<url>https?:\/\/[^\s]+loca.lt)", url).group("url"))

print("Open URL in browser: " + str(public_url))

from IPython.display import Javascript
#await google.colab.kernel.proxyPort(%s)
# Still not working to display app in Colab console, but tried.
def show_port(adr, height=500):
  display(Javascript("""
  (async ()=>{
    fm = document.createElement('iframe')
    fm.src = '%s'
    fm.width = '100%%'
    fm.height = '%d'
    fm.frameBorder = 0
    document.body.append(fm)
  })();
  """ % (adr, height) ))
#import requests
#r = requests.get('http://localhost:4040/api/tunnels')
#url = r.json()['tunnels'][0]['public_url']
#print(url)
#await google.colab.kernel.proxyPort(%s)
#get_ipython().system_raw('python3 -m http.server 8888 &') 
#get_ipython().system_raw('./ngrok http 8501 &')
#show_port(public_url.public_url, port)
#show_port(public_url.public_url)
#run_sp(f'python -m webbrowser -t "{public_url.public_url}"')
#webbrowser.open(public_url.public_url, new=0, autoraise=True)
#webbrowser.open_new_tab(public_url.public_url)
if auto_launch_website:
  display(Javascript('window.open("{url}");'.format(url=public_url)))
flet.app(target=main, view=flet.WEB_BROWSER, port=80, assets_dir=root_dir, upload_dir="uploads", web_renderer="html")
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host=socket_host)
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host=host_address)
#flet.app(target=main, view=flet.WEB_BROWSER, port=80, host=public_url.public_url)
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host="0.0.0.0")