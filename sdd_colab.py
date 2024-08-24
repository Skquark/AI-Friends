import os, subprocess, sys, shutil, re, argparse
import random as rnd
from typing import Optional
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--storage_type", type=str, default="Colab Google Drive")
parser.add_argument("--saved_settings_json", type=str, default="/content/drive/MyDrive/AI/Stable_Diffusion/sdd-settings.json")
parser.add_argument("--tunnel_type", type=str, default="localtunnel")
parser.add_argument("--auto_launch_website", default=False, action='store_true')
flags = parser.parse_args()
storage_type = flags.storage_type
saved_settings_json = flags.saved_settings_json
if not bool(saved_settings_json): saved_settings_json = "/content/drive/MyDrive/AI/Stable_Diffusion/sdd-settings.json"
tunnel_type = flags.tunnel_type
auto_launch_website = flags.auto_launch_website
save_to_GDrive = True
force_updates = True
newest_flet = True
upgrade_torch = True
SDD_version = "v1.9.0"
from IPython.display import clear_output
root_dir = '/content/'
dist_dir = root_dir
is_Colab = True
try:
  import google.colab
  from google.colab import output
  output.enable_custom_widget_manager()
  root_dir = '/content/'
except:
  root_dir = os.getcwd()
  dist_dir = os.path.join(root_dir, 'dist', 'Stable-Diffusion-Deluxe')
  if not os.path.isdir(dist_dir):
    dist_dir = root_dir
  print(f'Root: {root_dir} Dist:{dist_dir}')
  is_Colab = False
  pass
stable_dir = root_dir
env = os.environ.copy()
def run_sp(cmd_str: str or list, cwd: str = None, realtime: bool = False, output_column=None):
  cmd_list = cmd_str if isinstance(cmd_str, list) else cmd_str.split()
  if cmd_list[0] == "python":
    import sys
    if sys.prefix != sys.base_prefix:
      python_exe = sys.executable
      if ' ' in python_exe:
        python_exe = f'"{python_exe}"'
      cmd_list[0] = python_exe
  cwd_arg = {} if cwd is None else {'cwd': cwd}
  try:
    if realtime or output_column != None:
      process = subprocess.Popen(cmd_str, shell=False, env=env, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='utf-8', errors='replace', **cwd_arg) 
      while True:
        realtime_output = process.stdout.readline()
        if realtime_output == '' and process.poll() is not None:
          break
        if realtime_output:
          if not output_column:
              print(realtime_output.strip(), flush=False)
          else:
              from flet import Text
              output_column.controls.append(Text(realtime_output.strip()))
              output_column.update()
          sys.stdout.flush()
    else:
      returned = subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env, shell=False, **cwd_arg).stdout.decode('utf-8')
      if 'ERROR' in returned:
        print(f"Error Running {cmd_str} - {returned}")
      return returned
  except Exception as e:
      print(f"Error Running {cmd_str}: {e}")
      return e

save_to_GDrive = storage_type == "Colab Google Drive"
if save_to_GDrive:
  if not os.path.isdir(f'{root_dir}drive'):
    from google.colab import drive
    drive.mount('/content/drive')
elif storage_type == "PyDrive Google Drive":
  "pip install PyDrive2"
stable_dir = os.path.join(root_dir, 'Stable_Diffusion')
if not os.path.exists(stable_dir):
  os.makedirs(stable_dir)
uploads_dir = os.path.join(root_dir, "uploads")
if not os.path.exists(uploads_dir):
  os.makedirs(uploads_dir)
sample_data = '/content/sample_data'
if os.path.exists(sample_data):
  for f in os.listdir(sample_data):
    os.remove(os.path.join(sample_data, f))
  os.rmdir(sample_data)
#os.chdir(stable_dir)
#loaded_Stability_api = False
#loaded_img2img = False
#use_Stability_api = False
def version_checker():
  response = requests.get("https://raw.githubusercontent.com/Skquark/AI-Friends/main/DSD_version.txt")
  current_v = response.text.strip()
  if current_v != SDD_version:
    print(f'A new update is available. You are running {SDD_version} and {current_v} is up. We recommended refreshing Stable Diffusion Deluxe for the latest cool features or fixes.\nhttps://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb\nChangelog if interested: https://github.com/Skquark/AI-Friends/commits/main/Stable_Diffusion_Deluxe.ipynb')
def ng():
  response = requests.get("https://raw.githubusercontent.com/Skquark/AI-Friends/main/_ng")
  ng_list = response.text.strip().split('\n')
  _ng = rnd.choice(ng_list).partition('_')
  return _ng[2]+_ng[1]+_ng[0]

from urllib.parse import urlparse, unquote
def download_file(url: str, to: Optional[str] = None, filename: Optional[str] = None, 
                  raw: bool = True, ext: str = "png", replace: bool = False) -> str:
    if filename is None:
        parsed_url = urlparse(url)
        filename = os.path.basename(unquote(parsed_url.path))
        if not filename:
            filename = "downloaded_file"
        if '?' in filename:
            filename = filename.split('?')[0]
    if '.' not in filename:
        filename = f"{filename}.{ext}"
    to = to or uploads_dir#os.getcwd()
    local_filename = os.path.join(to, filename)
    os.makedirs(to, exist_ok=True)
    if os.path.isfile(local_filename) and not replace:
        return local_filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            if raw:
                shutil.copyfileobj(r.raw, f)
            else:
                f.write(r.content)
    return local_filename

def wget(url, to):
    res = subprocess.run(['wget', '-q', url, '-O', to], stdout=subprocess.PIPE).stdout.decode('utf-8')

try:
  import flet
  from packaging import version
  if version.parse(flet.version.version) < version.parse("0.23.1"):
    raise ImportError("Must upgrade Flet")
except ImportError as e:
  if newest_flet:
    run_sp("pip install --upgrade --quiet flet==0.23.1", realtime=False)
    #run_sp("pip install --upgrade flet==0.22.1", realtime=False)
    #0.19.0, 0.21.2, 0.22.0, 0.22.1, 0.23.0.dev2664, 0.23.0.dev2665, 0.23.0.dev2666, 0.23.0.dev2679, 0.23.0.dev2697, 0.23.0.dev2734, 0.23.0.dev2744, 0.23.0.dev2766, 0.23.0.dev2768, 0.23.0.dev2868, 0.23.0.dev2870, 0.23.0.dev2872, 0.23.0.dev2880)
  else:
    run_sp("pip install --upgrade flet==0.3.2", realtime=False)
  #run_sp("pip install -i https://test.pypi.org/simple/ flet")
  #run_sp("pip install --upgrade git+https://github.com/flet-dev/flet.git@controls-s3#egg=flet-dev")
  #run_sp("pip install --upgrade flet_ivid")
  pass
if is_Colab:
  try:
    import nest_asyncio
  except ModuleNotFoundError:
    run_sp("pip install nest_asyncio", realtime=False)
  finally:
    import nest_asyncio
    nest_asyncio.apply()
    pass
'''try:
  from flet_ivid import VideoContainer
except ModuleNotFoundError:
  run_sp("pip install --upgrade flet_ivid")
  from flet_ivid import VideoContainer
  pass'''
try:
  import requests
except ModuleNotFoundError:
  run_sp("pip install -q requests", realtime=True)
  import requests
  pass
try:
  from emoji import emojize
except ImportError as e:
  run_sp("pip install emoji --quiet", realtime=False)
  from emoji import emojize
  pass
if 'url' not in locals():
  url=""
if tunnel_type == "ngrok":
  try:
    import pyngrok
  except ImportError as e:
    run_sp("pip install pyngrok --quiet", realtime=False)
    #run_sp(f"ngrok authtoken {ng()}", realtime=False)
    run_sp(f"ngrok config add-authtoken {ng()}", realtime=False)
    run_sp("ngrok config upgrade", realtime=False)
    import pyngrok
    pass
elif tunnel_type == "localtunnel":
  if not bool(url):
    import re
    run_sp("npm install -g -q localtunnel", realtime=False)
    #localtunnel = subprocess.Popen(['lt', '--port', '80', 'http'], stdout=subprocess.PIPE)
    #url = str(localtunnel.stdout.readline())
    #url = (re.search("(?P<url>https?:\/\/[^\s]+loca.lt)", url).group("url"))
    #print(url)

gdrive = None
if storage_type == "PyDrive Google Drive":
  if not os.path.isfile(Google_OAuth_client_secret_json):
    raise ValueError("Couldn't locate your client_secret.json file to authenticate. Follow instructions below then copy certificate to your root dir.")
  try:
    from pydrive2.auth import GoogleAuth, ServiceAccountCredentials
    from pydrive2.drive import GoogleDrive
    from oauth2client.contrib.gce import AppAssertionCredentials
  except ImportError as e:
    run_sp("pip install PyDrive2 -q")
    from pydrive2.auth import GoogleAuth, ServiceAccountCredentials
    from pydrive2.drive import GoogleDrive
    from oauth2client.contrib.gce import AppAssertionCredentials
    pass
  import httplib2

  old_local_webserver_auth = GoogleAuth.LocalWebserverAuth
  def LocalWebServerAuth(self, *args, **kwargs):
      if isinstance(self.credentials, AppAssertionCredentials):
          self.credentials.refresh(httplib2.Http())
          return
      return old_local_webserver_auth(self, *args, **kwargs)
  GoogleAuth.LocalWebserverAuth = LocalWebServerAuth

  #scope = 'https://www.googleapis.com/auth/drive'
  #credentials = ServiceAccountCredentials.from_json_keyfile_name(Google_OAuth_client_secret_json, scope)
  gauth = GoogleAuth()
  gauth.LoadCredentialsFile(Google_OAuth_client_secret_json)
  #gauth.LocalWebserverAuth()
  if is_Colab: gauth.CommandLineAuth()
  else:
    gauth.LocalWebserverAuth()
    gauth.SaveCredentialsFile(Google_OAuth_client_secret_json)
  gdrive = GoogleDrive(gauth)
slash = '/'
from pathlib import Path
if not is_Colab:
    image_output = os.path.join(Path.home(), "Pictures", "Stable_Diffusion")
    if "\\" in image_output:
        slash = '\\'
else:
    image_output = '/content/drive/MyDrive/AI/Stable_Diffusion/images_out'

favicon = os.path.join(root_dir, "favicon.png")
loading_animation = os.path.join(root_dir, "icons", "loading-animation.png")
assets = os.path.join(root_dir, "assets")
if not os.path.isfile(favicon):
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/favicon.png?raw=true")
if not os.path.isfile(loading_animation):
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/loading-animation.png?raw=true", to=os.path.join(root_dir, "icons"))
if not os.path.exists(assets):
    os.makedirs(assets)
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/snd-alert.mp3?raw=true", to=assets)
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/snd-delete.mp3?raw=true", to=assets)
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/snd-error.mp3?raw=true", to=assets)
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/snd-done.mp3?raw=true", to=assets)
    download_file("https://github.com/Skquark/AI-Friends/blob/main/assets/snd-drop.mp3?raw=true", to=assets)
#clear_output()

import json
prefs = {}
def load_settings_file():
  global prefs
  if os.path.isfile(saved_settings_json):
    with open(saved_settings_json) as settings:
      prefs = json.load(settings)
    print("Successfully loaded settings json...")
  else:
    print("Settings file not found, starting with defaults...")
    prefs = {
      'save_to_GDrive': True,
      'image_output': image_output,
      'file_prefix': 'sd-',
      'file_suffix_seed': False,
      'file_max_length': 220,
      'file_allowSpace': False,
      'file_datetime': False,
      'file_from_1': False,
      'save_image_metadata': True,
      'meta_ArtistName':'',
      'meta_Copyright': '',
      'save_config_in_metadata': True,
      'save_config_json': False,
      'theme_mode': 'Dark',
      'theme_color': 'Green',
      'theme_custom_color': '#69d9ab',
      'enable_sounds': True,
      'show_stats': False,
      'stats_used': True,
      'stats_update': 5,
      'start_in_installation': False,
      'slider_stack': False,
      'disable_nsfw_filter': True,
      'retry_attempts': 3,
      'HuggingFace_api_key': "",
      'Stability_api_key': "",
      'OpenAI_api_key': "",
      'PaLM_api_key': "",
      'Anthropic_api_key': "",
      'TextSynth_api_key': "",
      'Replicate_api_key': "",
      'Ideogram_api_key': "",
      'AIHorde_api_key': "0000000000",
      'Perplexity_api_key': "",
      'luma_api_key': "",
      'HuggingFace_username': "",
      'scheduler_mode': "DDIM",
      'higher_vram_mode': False,
      'enable_xformers': False,
      'enable_attention_slicing': True,
      'enable_bitsandbytes': False,
      'memory_optimization': "None",
      'sequential_cpu_offload': False,
      'vae_slicing': True,
      'vae_tiling': False,
      'enable_torch_compile': False,
      'enable_stable_fast': False,
      'enable_tome': False,
      'tome_ratio': 0.5,
      'enable_freeu': False,
      'freeu_args': {'b1': 1.2, 'b2':1.4, 's1':0.9, 's2':0.2},
      'enable_hidiffusion': False,
      'enable_deepcache': False,
      'cache_dir': '',
      'install_diffusers': True,
      'install_interpolation': False,
      'install_text2img': False,
      'install_img2img': False,
      'install_SDXL': True,
      'install_SD3': False,
      'install_megapipe': True,
      'install_CLIP_guided': False,
      'install_OpenAI': False,
      'install_TextSynth': False,
      'install_dreamfusion': False,
      'install_repaint': False,
      'install_imagic': False,
      'install_composable': False,
      'install_safe': False,
      'install_versatile': False,
      'install_depth2img': False,
      'install_alt_diffusion': False,
      'install_attend_and_excite': False,
      'install_SAG': False,
      'install_panorama': False,
      'install_upscale': False,
      'upscale_method': 'Real-ESRGAN',
      'upscale_model': 'realesr-general-x4v3',
      'AuraSR_overlapped': False,
      'AuraSR_keep_loaded': False,
      'safety_config': 'Strong',
      'use_imagic': False,
      'SD_compel': False,
      'use_SDXL': False,
      'SDXL_high_noise_frac': 0.7,
      'SDXL_negative_conditions': False,
      'SDXL_compel': False,
      'SDXL_watermark': False,
      'SDXL_model': 'SDXL-Base v1',
      'SDXL_custom_model': '',
      'SDXL_custom_models': [],
      'use_SD3': True,
      'SD3_compel': False,
      'SD3_model': 'Stable Diffusion 3 Medium',
      'SD3_custom_model': '',
      'SD3_custom_models': [],
      'SD3_cpu_offload': True,
      'SD3_bitsandbytes_8bit': False,
      'SD3_use_pag': False,
      'SD3_pag_scale': 4.0,
      'SD3_applied_layers': ['8'],
      'use_composable': False,
      'use_safe': False,
      'use_versatile': False,
      'use_alt_diffusion': False,
      'use_attend_and_excite': False,
      'max_iter_to_alter': 25,
      'use_SAG': False,
      'sag_scale': 0.75,
      'use_panorama': False,
      'panorama_width': 2048,
      'panorama_circular_padding': False,
      'use_upscale': False,
      'upscale_noise_level': 20,
      'install_conceptualizer': False,
      'use_conceptualizer': False,
      'concepts_model': 'cat-toy',
      'use_ip_adapter': False,
      'ip_adapter_image': '',
      'ip_adapter_model': 'SD v1.5',
      'ip_adapter_SDXL_model': 'SDXL',
      'ip_adapter_strength': 0.8,
      'model_ckpt': 'Stable Diffusion v1.5',
      'finetuned_model': 'Midjourney v4 style',
      'dreambooth_model': 'disco-diffusion-style',
      'custom_model': '',
      'custom_models': [],
      'tortoise_custom_voices': [],
      'custom_dance_diffusion_models': [],
      'clip_model_id': "laion/CLIP-ViT-B-32-laion2B-s34B-b79K",
      'install_Stability_api': False,
      'use_Stability_api': False,
      'model_checkpoint': "Stable Diffusion 3",
      'generation_sampler': "K_EULER_ANCESTRAL",
      'clip_guidance_preset': "FAST_BLUE",
      'install_AIHorde_api': False,
      'use_AIHorde_api': False,
      'AIHorde_model': 'stable_diffusion',
      'AIHorde_sampler': 'k_euler_a',
      'AIHorde_post_processing': "None",
      'AIHorde_karras': False,
      'AIHorde_tiling': False,
      'AIHorde_transparent': False,
      'AIHorde_hires_fix': False,
      'AIHorde_strip_background': False,
      'AIHorde_lora_layer': 'Horde Aesthetics Improver',
      'AIHorde_lora_layer_alpha': 1.0,
      'AIHorde_custom_lora_layer': '',
      'custom_CivitAI_LoRA_models': [],
      'AIHorde_lora_map': [],
      'AIHorde_use_controlnet': False,
      'AIHorde_controlnet': "Canny",
      'install_ESRGAN': True,
      'batch_folder_name': "",
      'batch_size': 1,
      'n_iterations': 1,
      'steps': 50,
      'eta': 0.4,
      'seed': 0,
      'guidance_scale': 8,
      'width': 960,
      'height': 512,
      'init_image': "",
      'mask_image': "",
      'init_image_strength': 0.25,
      'alpha_mask': False,
      'invert_mask': False,
      'negative_prompt': "",
      'precision': 'autocast',
      'use_inpaint_model': False,
      'centipede_prompts_as_init_images': False,
      'multi_schedulers': False,
      'use_depth2img': False,
      'use_LoRA_model': False,
      'LoRA_model': 'Von Platen LoRA',
      'active_LoRA_layers': [],
      'active_SDXL_LoRA_layers': [],
      'active_SD3_LoRA_layers': [],
      'custom_LoRA_models': [],
      'custom_LoRA_model': "",
      'SDXL_LoRA_model': 'Papercut SDXL',
      'custom_SDXL_LoRA_models': [],
      'custom_SDXL_LoRA_model': "",
      'SD3_LoRA_model': 'Celebrities',
      'custom_SD3_LoRA_models': [],
      'custom_SD3_LoRA_model': "",
      'custom_Flux_LoRA_models': [],
      'custom_Flux_LoRA_model': "",
      'use_interpolation': False,
      'num_interpolation_steps': 22,
      'use_clip_guided_model': False,
      'clip_guidance_scale': 571,
      'use_cutouts': True,
      'num_cutouts': 4,
      'unfreeze_unet': True,
      'unfreeze_vae': True,
      'apply_ESRGAN_upscale': True,
      'enlarge_scale': 1.5,
      'face_enhance':False,
      'display_upscaled_image': False,
      'negatives': ["Blurry"],
      'custom_negatives': "",
      'prompt_styler': '',
      'prompt_style': 'cinematic-default',
      'prompt_styles': ['cinematic-default'],
      'prompt_styler_multi': False,
      'prompt_list': [],
      'prompt_generator': {
          'phrase': '',
          'subject_detail': '',
          'phrase_as_subject': False,
          'amount': 10,
          'random_artists': 0,
          'random_styles': 0,
          'permutate_artists': False,
          'request_mode': 3,
          'AI_temperature': 0.8,
          'AI_engine': "OpenAI ChatGPT",
          'OpenAI_model': 'GPT-4 Turbo',
          'AIHorde_model': "LLaMA-13B-Psyfighter2",
          'Perplexity_model': "llama-3-sonar-small-32k-chat",
          'economy_mode': True,
      },
      'prompt_remixer': {
          'seed_prompt': '',
          'optional_about_influencer': '',
          'amount': 10,
          'random_artists': 0,
          'random_styles': 0,
          'permutate_artists': False,
          'request_mode': 3,
          'AI_temperature': 0.8,
          'AI_engine': "OpenAI ChatGPT",
          'OpenAI_model': 'GPT-4 Turbo',
          'AIHorde_model': "LLaMA-13B-Psyfighter2",
          'Perplexity_model': "llama-3-sonar-small-32k-chat",
      },
      'prompt_brainstormer': {
          'AI_engine': 'OpenAI ChatGPT',
          'about_prompt': '',
          'request_mode': 'Brainstorm',
          'AI_temperature': 0.8,
          'OpenAI_model': 'GPT-4 Turbo',
          'AIHorde_model': "LLaMA-13B-Psyfighter2",
          'Perplexity_model': "llama-3-sonar-small-32k-chat",
      },
      'prompt_writer': {
          'art_Subjects': '',
          'negative_prompt': '',
          'by_Artists': '',
          'art_Styles': '',
          'amount': 10,
          'random_artists': 2,
          'random_styles': 1,
          'permutate_artists': False,
      },
    }

load_settings_file()
#version_checker()





def run_kandinsky_video(page):
    global kandinsky_video_prefs, prefs, status, pipe_kandinsky_video
    if not check_diffusers(page): return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.KandinskyVideo.controls.append(line)
      page.KandinskyVideo.update()
    def clear_last(lines=1):
      clear_line(page.KandinskyVideo, lines=lines)
    def clear_list():
      page.KandinskyVideo.controls = page.KandinskyVideo.controls[:1]
    def autoscroll(scroll=True):
      page.KandinskyVideo.auto_scroll = scroll
      page.KandinskyVideo.update()
    progress = ProgressBar(bar_height=8)
    total_steps = kandinsky_video_prefs['num_inference_steps']
    def callback_fnc(pipe, step, timestep, callback_kwargs):
      callback_fnc.has_been_called = True
      nonlocal progress, total_steps
      #total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps}  Timestep: {timestep:.1f}"
      progress.update()
    clear_list()
    autoscroll(True)
    installer = Installing("Installing Kandinsky Video Text-To-Video Pipeline...")
    prt(installer)
    KandinskyVideo_dir = os.path.join(root_dir, "KandinskyVideo")
    if not os.path.exists(KandinskyVideo_dir):
        installer.status("...cloning ai-forever/KandinskyVideo")
        run_sp("git clone https://github.com/ai-forever/KandinskyVideo.git", cwd=root_dir)
    if KandinskyVideo_dir not in sys.path:
        sys.path.append(KandinskyVideo_dir)
    pip_install("pytorch_lightning==1.7.5 setuptools==59.5.0 omegaconf datasets einops webdataset fsspec s3fs hydra-core scikit-image|skimage matplotlib wandb albumentations bezier av sentencepiece", installer=installer)
    model_id = "https://huggingface.co/ai-forever/KandinskyVideo_1_1"
    device_map = 'cuda:0'
    clear_pipes('kandinsky_video')
    if pipe_kandinsky_video == None:
        installer.status(f"...initialize Pipeline")
        try:
            from kandinsky_video import get_T2V_pipeline
            pipe_kandinsky_video = get_T2V_pipeline(device_map)
        except Exception as e:
            clear_last()
            alert_msg(page, f"ERROR Initializing KandinskyVideo_1_1...", content=Column([Text(str(e)), Text(str(traceback.format_exc()), selectable=True)]))
            return
    init_img = None
    init_image = kandinsky_video_prefs['init_image']
    if bool(init_image):
        from PIL import ImageOps
        import requests
        if init_image.startswith('http'):
            init_img = PILImage.open(requests.get(init_image, stream=True).raw)
        else:
            if os.path.isfile(init_image):
                init_img = PILImage.open(init_image)
            else:
                alert_msg(page, f"ERROR: Couldn't find your init_image {init_image}")
                return
        init_img = init_img.resize((width, height), resample=PILImage.Resampling.LANCZOS)
        init_img = ImageOps.exif_transpose(init_img).convert("RGB")
        #init_img.save(init_file)
    clear_last()
    import imageio.v2 as iio
    def frames2video(frames: np.ndarray, extension: str = 'mp4', fps: int = 24, codec: str = 'h264') -> bytes:
        output = io.BytesIO()
        writer = iio.get_writer(output, extension, fps=fps, codec=codec)
        for frame in frames:
            writer.append_data(np.array(frame))
        writer.close()
        return output.getvalue()
    batch_output = os.path.join(prefs['image_output'], kandinsky_video_prefs['batch_folder_name'])
    makedir(batch_output)
    for n in range(kandinsky_video_prefs['num_images']):
        prt("Generating Kandinsky Video from your Prompt...")
        prt(progress)
        autoscroll(False)
        width = kandinsky_video_prefs['width']
        height = kandinsky_video_prefs['height']
        try:
            video = pipe_kandinsky_video(
                kandinsky_video_prefs['prompt'],
                negative_prompt=kandinsky_video_prefs['negative_prompt'],
                width=width, height=height, 
                image=init_img,
                fps=kandinsky_video_prefs['fps'].lower(), 
                motion=kandinsky_video_prefs['motion'].lower(),
                key_frame_guidance_scale=kandinsky_video_prefs['key_frame_guidance_scale'],
                guidance_weight_prompt=kandinsky_video_prefs['prompt_guidance_scale'],
                guidance_weight_image=kandinsky_video_prefs['image_guidance_scale'],
                interpolation_guidance_scale=kandinsky_video_prefs['interpolation_guidance_scale'],
            )
        except Exception as e:
          clear_last(2)
          alert_msg(page, f"ERROR: KandinskyVideo Text-To-Video failed for some reason. Possibly out of memory or something wrong with the code...", content=Column([Text(str(e)), Text(str(traceback.format_exc()), selectable=True)]))
          return
        clear_last(2)
        autoscroll(True)
        fname = f"{format_filename(kandinsky_video_prefs['prompt'])}"
        gif_file = available_file(batch_output, fname, no_num=True, ext="gif")
        video_file = available_file(batch_output, fname, no_num=True, ext="mp4")
        video.save(gif_file,
            save_all=True, append_images=video[1:], duration=int(5500/len(video)), loop=0
        )
        prt(Row([ImageButton(src=gif_file, width=width, height=height, data=gif_file, page=page)], alignment=MainAxisAlignment.CENTER))
        fps = switchcase(kandinsky_video_prefs['fps'].lower(), {'low':2, 'medium':8, 'high':30})
        with open(video_path, "wb") as file:
            file.write(frames2video(video, fps=fps))
        autoscroll(True)
        export_to_video(video, video_file, fps=kandinsky_video_prefs['fps'])
        #prt(Row([VideoContainer(video_file)], alignment=MainAxisAlignment.CENTER))
        prt(Markdown(f"Video saved to [{video_file}]({filepath_to_url(video_file)})", on_tap_link=lambda e: e.page.launch_url(e.data)))
    #prt(f"Done creating video... Check {batch_output}")
    autoscroll(False)
    play_snd(Snd.ALERT, page)
