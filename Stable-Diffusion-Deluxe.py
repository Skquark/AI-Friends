#@title ## ⚙️ Install Python Desktop Flet Framework & Initiallize Settings
#markdown If you're running on Google Colab, authorize Google Drive with the popup to connect storage. If you're on a local or cloud Jupyter Notebook, you must get a OAuth json using instructions below to save images to GDrive, however the feature is not currently working and in progress. When set, continue to run the Web UI and experiment away..
#@markdown We'll connect to your Google Drive and save all of your preferences in realtime there, as well as your created images. This is the folder location and file name we recommend in your mounted gdrive, will be created if you're new, but you can save elsewhere.  Launches webpage with localtunnel, but in case it's down you can use ngrok instead.
#pyinstaller Stable-Diffusion-Deluxe.py --hidden-import=requests --hidden-import=torch --hidden-import=huggingface-hub --hidden-import=transformers[dev] --hidden-import=tqdm --hidden-import=regex  --hidden-import=git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch] --collect-all=tqdm --collect-all=git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]  --collect-all=transformers --collect-all=regex
#pyinstaller Stable-Diffusion-Deluxe.spec -y

storage_type = "Local Drive" #@param ["Colab Google Drive", "PyDrive Google Drive", "Local Drive"]
Google_OAuth_client_secret_json = "/content/client_secrets.json" #param {'type': 'string'}
save_to_GDrive = False #param {'type': 'boolean'}
saved_settings_json = '.\sdd-settings.json' #@param {'type': 'string'}
tunnel_type = "desktop" #@param ["localtunnel", "ngrok"] 
#, "cloudflared"
auto_launch_website = False #@param {'type': 'boolean'}
version = "v1.6.0"
import os, subprocess, sys, shutil
root_dir = '/content/'
dist_dir = root_dir
is_Colab = True
try:
  import google.colab
  root_dir = '/content/'
except:
  root_dir = os.getcwd()
  dist_dir = os.path.join(root_dir, 'dist', 'Stable-Diffusion-Deluxe')
  if not os.path.isdir(dist_dir):
    dist_dir = root_dir
  #print(f'Root: {root_dir} Dist:{dist_dir}')
  is_Colab = False
  pass
stable_dir = root_dir
save_to_GDrive = storage_type == "Colab Google Drive"
if save_to_GDrive:
  if not os.path.isdir(os.path.join(root_dir, 'drive')):
    from google.colab import drive
    drive.mount(os.path.join(root_dir, 'drive'))
elif storage_type == "PyDrive Google Drive":
  "pip install PyDrive2"
stable_dir = os.path.join(root_dir, 'Stable_Diffusion')
if not os.path.exists(stable_dir):
  os.makedirs(stable_dir)
#if not os.path.exists(image_output):
#  os.makedirs(image_output)
sample_data = '/content/sample_data'
if os.path.exists(sample_data):
  for f in os.listdir(sample_data):
    os.remove(os.path.join(sample_data, f))
  os.rmdir(sample_data)
os.chdir(stable_dir)
from IPython.display import clear_output
#loaded_Stability_api = False
#loaded_img2img = False
#use_Stability_api = False

import requests
import random as rnd
def version_checker():
  try:
    response = requests.get("https://raw.githubusercontent.com/Skquark/AI-Friends/main/DSD_version.txt")
    current_v = response.text.strip()
    if current_v != version:
      print(f'A new update is available. You are running {version} and {current_v} is up. We recommended refreshing Stable Diffusion Deluxe for the latest cool features or fixes.\nhttps://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb\nChangelog if interested: https://github.com/Skquark/AI-Friends/commits/main/Stable_Diffusion_Deluxe.ipynb')
  except: pass #Probably offline
def ng():
  response = requests.get("https://raw.githubusercontent.com/Skquark/AI-Friends/main/_ng")
  ng_list = response.text.strip().split('\n')
  _ng = rnd.choice(ng_list).partition('_')
  return _ng[2]+_ng[1]+_ng[0]

env = os.environ.copy()
def run_sp(cmd_str, cwd=None, realtime=True):
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
        print(realtime_output.strip(), flush=False)
        sys.stdout.flush()
  else:
    if cwd is None:
      return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
    else:
      return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env, cwd=cwd).stdout.decode('utf-8')
try:
  import flet
except ImportError as e:
  run_sp("pip install flet --upgrade --quiet")
  #run_sp("pip install -i https://test.pypi.org/simple/ flet")
  #run_sp("pip install --upgrade git+https://github.com/flet-dev/flet.git@controls-s3#egg=flet-dev")
  pass

try:
  from emoji import emojize
except ImportError as e:
  run_sp("pip install emoji --quiet")
  from emoji import emojize
  pass
if 'url' not in locals():
  url=""
if tunnel_type == "ngrok":
  try:
    import pyngrok
  except ImportError as e:
    run_sp("pip install pyngrok --quiet", realtime=False)
    run_sp(f"ngrok authtoken {ng()}", realtime=False)
    import pyngrok
    pass
elif tunnel_type == "localtunnel":
  if not bool(url):
    import re
    run_sp("npm install -g -q localtunnel")
    localtunnel = subprocess.Popen(['lt', '--port', '80', 'http'], stdout=subprocess.PIPE)
    url = str(localtunnel.stdout.readline())
    url = (re.search("(?P<url>https?:\/\/[^\s]+loca.lt)", url).group("url"))
    print(url)

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
    
clear_output()

import json
if 'prefs' not in locals():
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
      'save_image_metadata': True,
      'meta_ArtistName':'',
      'meta_Copyright': '',
      'save_config_in_metadata': True,
      'save_config_json': False,
      'theme_mode': 'Dark',
      'theme_color': 'Green',
      'enable_sounds': True,
      'start_in_installation': False,
      'disable_nsfw_filter': True,
      'retry_attempts': 3,
      'HuggingFace_api_key': "",
      'Stability_api_key': "",
      'OpenAI_api_key': "",
      'TextSynth_api_key': "",
      'Replicate_api_key': "",
      'api_key_file': '/content/drive/MyDrive/AI/Stable_Diffusion/sd_api_keys.txt',
      'scheduler_mode': "DDIM",
      'higher_vram_mode': False,
      'enable_attention_slicing': True,
      'memory_optimization': 'Attention Slicing',
      'sequential_cpu_offload': False,
      'vae_slicing': False,
      'cache_dir': '',
      'install_diffusers': True,
      'install_interpolation': False,
      'install_text2img': True,
      'install_img2img': False,
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
      'install_upscale': False,
      'safety_config': 'Strong',
      'use_imagic': False,
      'use_composable': False,
      'use_safe': False,
      'use_versatile': False,
      'use_upscale': False,
      'upscale_noise_level': 20,
      'install_conceptualizer': False,
      'use_conceptualizer': False,
      'concepts_model': 'cat-toy',
      'model_ckpt': 'Stable Diffusion v1.5',
      'finetuned_model': 'Midjourney v4 style',
      'dreambooth_model': 'disco-diffusion-style',
      'custom_model': '',
      'custom_models': [],
      'clip_model_id': "laion/CLIP-ViT-B-32-laion2B-s34B-b79K",
      'install_Stability_api': False,
      'use_Stability_api': False,
      'model_checkpoint': "stable-diffusion-768-v2-1",
      'generation_sampler': "K_EULER_ANCESTRAL",
      'clip_guidance_preset': "FAST_BLUE",
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
      'precision': 'autocast',
      'use_inpaint_model': False,
      'centipede_prompts_as_init_images': False,
      'use_depth2img': False,
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
      'prompt_list': [],
      'prompt_generator': {
          'phrase': '',
          'subject_detail': '',
          'phrase_as_subject': False,
          'amount': 10,
          'random_artists': 2,
          'random_styles': 1,
          'permutate_artists': False,
          'request_mode': 3,
          'AI_temperature': 0.9,
          'economy_mode': True,
      },
      'prompt_remixer': {
          'seed_prompt': '',
          'optional_about_influencer': '',
          'amount': 10,
          'random_artists': 2,
          'random_styles': 1,
          'permutate_artists': False,
          'request_mode': 3,
          'AI_temperature': 0.9,
      },
      'prompt_brainstormer': {
          'AI_engine': 'OpenAI GPT-3',
          'about_prompt': '',
          'request_mode': 'Brainstorm',
          'AI_temperature': 0.9,
      },
      'prompt_writer': {
          'art_Subjects': '',
          'by_Artists': '',
          'art_Styles': '',
          'amount': 10,
          'random_artists': 2,
          'random_styles': 1,
          'permutate_artists': False,
      },
    }
if prefs == {}:
  load_settings_file()
version_checker()



#@title ## **▶️ Run Stable Diffusion Deluxe** - Flet/Flutter WebUI App
import flet
#from flet import *
from flet import Page, View, Column, Row, ResponsiveRow, Container, Text, Stack, TextField, Checkbox, Switch, Image, ElevatedButton, IconButton, Markdown, Tab, Tabs, AppBar, Divider, VerticalDivider, GridView, Tooltip, SnackBar, AnimatedSwitcher, ButtonStyle, FloatingActionButton, Audio, Theme, Dropdown, Slider, ListTile, ListView, TextButton, PopupMenuButton, PopupMenuItem, AlertDialog, Banner, Icon, ProgressBar, ProgressRing, GestureDetector, KeyboardEvent, FilePicker, FilePickerResultEvent, FilePickerUploadFile, FilePickerUploadEvent, UserControl, Ref
from flet import icons, dropdown, colors, padding, margin, alignment, border_radius, theme, animation, KeyboardType, TextThemeStyle, AnimationCurve
from flet.types import TextAlign, FontWeight, ClipBehavior, MainAxisAlignment, CrossAxisAlignment, ScrollMode, ImageFit, ThemeMode
from flet import Image as Img
try:
    import PIL
except Exception:
    run_sp("pip install Pillow", realtime=False)
    run_sp("pip install image", realtime=False)
    import PIL
    pass
from PIL import Image as PILImage # Avoids flet conflict
import random as rnd
import io, shutil
from contextlib import redirect_stdout

if 'prefs' not in locals():
    raise ValueError("Setup not initialized. Run the previous code block first and authenticate your Drive storage.")
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
    'installed_conceptualizer': False,
    'installed_dreamfusion': False,
    'installed_repaint': False,
    'installed_imagic': False,
    'installed_composable': False,
    'installed_safe': False,
    'installed_versatile': False,
    'installed_depth2img': False,
    'installed_upscale': False,
    'finetuned_model': False,
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

def save_settings_file(page, change_icon=True):
  if change_icon:
    page.app_icon_save()
  if not os.path.isfile(saved_settings_json):
    settings_path = saved_settings_json.rpartition(slash)[0]
    os.makedirs(settings_path, exist_ok=True)
  with open(saved_settings_json, "w") as write_file:
    json.dump(prefs, write_file, indent=4)

current_tab = 0
def tab_on_change (e):
    t = e.control
    global current_tab, status
    #print (f"tab changed from {current_tab} to: {t.selected_index}")
    #print(str(t.tabs[t.selected_index].text))
    if current_tab == 0:
      #if not status['initialized']:
      #  initState(e.page)
      #  status['initialized'] = True
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
      e.page.show_install_fab(False)
    if current_tab == 2:
      if status['changed_parameters']:
        update_args()
        e.page.update_prompts()
        save_settings_file(e.page)
        status['changed_parameters'] = False
      e.page.show_apply_fab(False)
    if current_tab == 3:
      if status['changed_prompts']:
        e.page.save_prompts()
        save_settings_file(e.page)
        status['changed_prompts'] = False
      e.page.show_run_diffusion_fab(False)
    if current_tab == 5:
      if status['changed_prompt_generator']:
        save_settings_file(e.page)
        status['changed_prompt_generator'] = False
    
    current_tab = t.selected_index
    if current_tab == 1:
      refresh_installers(e.page.Installers.controls[0].content.controls)
      e.page.show_install_fab(True)
      #page.Installers.init_boxes()
    if current_tab == 2:
      update_parameters(e.page)
      #for p in e.page.Parameters.content.controls:
      e.page.Parameters.controls[0].content.update()
      e.page.Parameters.update()
      e.page.show_apply_fab(len(prompts) > 0 and status['changed_parameters'])
    if current_tab == 3:
      e.page.show_run_diffusion_fab(len(prompts) > 0)
    e.page.update()

def buildTabs(page):
    page.Settings = buildSettings(page)
    page.Installers = buildInstallers(page)
    page.Parameters = buildParameters(page)
    page.PromptsList = buildPromptsList(page)
    page.PromptHelpers = buildPromptHelpers(page)
    page.Images = buildImages(page)
    page.StableDiffusers = buildStableDiffusers(page)
    page.Extras = buildExtras(page)
    
    t = Tabs(selected_index=0, animation_duration=300, expand=1,
        tabs=[
            Tab(text="Settings", content=page.Settings, icon=icons.SETTINGS_OUTLINED),
            Tab(text="Installation", content=page.Installers, icon=icons.INSTALL_DESKTOP),
            Tab(text="Image Parameters", content=page.Parameters, icon=icons.DISPLAY_SETTINGS),
            Tab(text="Prompts List", content=page.PromptsList, icon=icons.FORMAT_LIST_BULLETED),
            Tab(text="Generate Images", content=page.Images, icon=icons.IMAGE_OUTLINED),
            Tab(text="Prompt Helpers", content=page.PromptHelpers, icon=icons.BUBBLE_CHART_OUTLINED),
            Tab(text="Stable Diffusers", content=page.StableDiffusers, icon=icons.PALETTE),
            Tab(text="Extras", content=page.Extras, icon=icons.ALL_INBOX),
        ],
    )
    page.tabs = t
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
    elif color == "yellow": return colors.YELLOW

# Delete these after everyone's updated
if 'install_conceptualizer' not in prefs: prefs['install_conceptualizer'] = False
if 'use_conceptualizer' not in prefs: prefs['use_conceptualizer'] = False
if 'concepts_model' not in prefs: prefs['concepts_model'] = 'cat-toy'
if 'memory_optimization' not in prefs: prefs['memory_optimization'] = 'Attention Slicing'
if 'sequential_cpu_offload' not in prefs: prefs['sequential_cpu_offload'] = False
if 'vae_slicing' not in prefs: prefs['vae_slicing'] = False
if 'use_inpaint_model' not in prefs: prefs['use_inpaint_model'] = False
if 'cache_dir' not in prefs: prefs['cache_dir'] = ''
if 'Replicate_api_key' not in prefs: prefs['Replicate_api_key'] = ''
if 'install_dreamfusion' not in prefs: prefs['install_dreamfusion'] = False
if 'install_repaint' not in prefs: prefs['install_repaint'] = False
if 'finetuned_model' not in prefs: prefs['finetuned_model'] = 'Midjourney v4 style'
if 'dreambooth_model' not in prefs: prefs['dreambooth_model'] = 'disco-diffusion-style'
if 'custom_model' not in prefs: prefs['custom_model'] = ''
if 'custom_models' not in prefs: prefs['custom_models'] = []
if 'start_in_installation' not in prefs: prefs['start_in_installation'] = False
if 'install_imagic' not in prefs: prefs['install_imagic'] = False
if 'use_imagic' not in prefs: prefs['use_imagic'] = False
if 'install_composable' not in prefs: prefs['install_composable'] = False
if 'use_composable' not in prefs: prefs['use_composable'] = False
if 'install_safe' not in prefs: prefs['install_safe'] = False
if 'use_safe' not in prefs: prefs['use_safe'] = False
if 'safety_config' not in prefs: prefs['safety_config'] = "Strong"
if 'install_versatile' not in prefs: prefs['install_versatile'] = False
if 'use_versatile' not in prefs: prefs['use_versatile'] = False
if 'install_depth2img' not in prefs: prefs['install_depth2img'] = False
if 'use_depth2img' not in prefs: prefs['use_depth2img'] = False
if 'install_upscale' not in prefs: prefs['install_upscale'] = False
if 'use_upscale' not in prefs: prefs['use_upscale'] = False
if 'upscale_noise_level' not in prefs: prefs['upscale_noise_level'] = 20
if 'alpha_mask' not in prefs: prefs['alpha_mask'] = False
if 'invert_mask' not in prefs: prefs['invert_mask'] = False
if 'clip_guidance_preset' not in prefs: prefs['clip_guidance_preset'] = "FAST_BLUE"

def initState(page):
    global status, current_tab
    if os.path.isdir(os.path.join(root_dir, 'Real-ESRGAN')):
      status['installed_ESRGAN'] = True
    page.load_prompts()
    # TODO: Try to load from assets folder
    page.snd_alert = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-alert.mp3?raw=true", autoplay=False)
    page.snd_delete = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-delete.mp3?raw=true", autoplay=False)
    page.snd_error = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-error.mp3?raw=true", autoplay=False)
    page.snd_done = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-done.mp3?raw=true", autoplay=False)
    #page.snd_notification = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-notification.mp3?raw=true", autoplay=False)
    page.snd_drop = Audio(src="https://github.com/Skquark/AI-Friends/blob/main/assets/snd-drop.mp3?raw=true", autoplay=False)
    page.overlay.append(page.snd_alert)
    page.overlay.append(page.snd_delete)
    page.overlay.append(page.snd_error)
    page.overlay.append(page.snd_done)
    #page.overlay.append(page.snd_notification)
    page.overlay.append(page.snd_drop)
    #print("Running Init State")
    if prefs['start_in_installation']:
      page.tabs.selected_index = 1
      page.tabs.update()
      page.show_install_fab(True)
      page.update()
      current_tab = 1

def buildSettings(page):
  global prefs, status
  def open_url(e):
    page.launch_url(e.data)
  def save_settings(e):
    save_settings_file(e.page)
    page.snack_bar = SnackBar(content=Text(f"Saving all settings to {saved_settings_json.rpartition(slash)[2]}"))
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
    status['changed_settings'] = True
  def change_theme_color(e):
    prefs['theme_color'] = e.control.value
    if prefs['theme_mode'].lower() == "dark":
      page.dark_theme = Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    else:
      page.theme = theme.Theme(color_scheme_seed=get_color(prefs['theme_color'].lower()))
    page.update()
    status['changed_settings'] = True
  def toggle_nsfw(e):
    retry_attempts.width = 0 if e.control.value else None
    retry_attempts.update()
    changed(e, 'disable_nsfw_filter')
  #haschanged = False
  #save_to_GDrive = Checkbox(label="Save to Google Drive", value=prefs['save_to_GDrive'])
  def default_cache_dir(e):
    default_dir = prefs['image_output'].strip()
    if default_dir.endswith(slash):
      default_dir = default_dir[:-1]
    default_dir = default_dir.rpartition(slash)[0]
    default_dir = os.path.join(default_dir, 'models')
    prefs['cache_dir'] = default_dir
    optional_cache_dir.value = default_dir
    optional_cache_dir.update()
  image_output = TextField(label="Image Output Path", value=prefs['image_output'], on_change=lambda e:changed(e, 'image_output'), col={"md":12, "lg":6}, suffix=IconButton(icon=icons.FOLDER_OUTLINED))
  optional_cache_dir = TextField(label="Optional Cache Directory (saves large models to GDrive)", hint_text="(button on right inserts recommended folder)", value=prefs['cache_dir'], on_change=lambda e:changed(e, 'cache_dir'), suffix=IconButton(icon=icons.ARCHIVE, tooltip="Insert recommended models cache path", on_click=default_cache_dir), col={"md":12, "lg":6})
  file_prefix = TextField(label="Filename Prefix",  value=prefs['file_prefix'], width=150, height=60, on_change=lambda e:changed(e, 'file_prefix'))
  file_suffix_seed = Checkbox(label="Filename Suffix Seed   ", tooltip="Appends -seed# to the end of the image name", value=prefs['file_suffix_seed'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'file_suffix_seed'))
  file_allowSpace = Checkbox(label="Filename Allow Space", tooltip="Otherwise will replace spaces with _ underscores", value=prefs['file_allowSpace'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'file_allowSpace'))
  file_max_length = TextField(label="Filename Max Length", tooltip="How long can the name taken from prompt text be? Max 250", value=prefs['file_max_length'], keyboard_type=KeyboardType.NUMBER, width=150, height=60, on_change=lambda e:changed(e, 'file_max_length'))
  save_image_metadata = Checkbox(label="Save Image Metadata in png", tooltip="Embeds your Artist Name & Copyright in the file's EXIF", value=prefs['save_image_metadata'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'save_image_metadata'))
  meta_ArtistName = TextField(label="Artist Name Metadata", value=prefs['meta_ArtistName'], keyboard_type=KeyboardType.NAME, on_change=lambda e:changed(e, 'meta_ArtistName'))
  meta_Copyright = TextField(label="Copyright Metadata", value=prefs['meta_Copyright'], keyboard_type=KeyboardType.NAME, on_change=lambda e:changed(e, 'meta_Copyright'))
  save_config_in_metadata = Checkbox(label="Save Config in Metadata    ", tooltip="Embeds all prompt parameters in the file's EXIF to recreate", value=prefs['save_config_in_metadata'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'save_config_in_metadata'))
  save_config_json = Checkbox(label="Save Config JSON files", tooltip="Creates a json text file with all prompt parameters with each image", value=prefs['save_config_json'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'save_config_json'))
  theme_mode = Dropdown(label="Theme Mode", width=200, options=[dropdown.Option("Dark"), dropdown.Option("Light")], value=prefs['theme_mode'], on_change=change_theme_mode)
  theme_color = Dropdown(label="Accent Color", width=200, options=[dropdown.Option("Green"), dropdown.Option("Blue"), dropdown.Option("Red"), dropdown.Option("Indigo"), dropdown.Option("Purple"), dropdown.Option("Orange"), dropdown.Option("Amber"), dropdown.Option("Brown"), dropdown.Option("Teal"), dropdown.Option("Yellow")], value=prefs['theme_color'], on_change=change_theme_color)
  enable_sounds = Checkbox(label="Enable UI Sound Effects    ", tooltip="Turn on for audible errors, deletes and generation done notifications", value=prefs['enable_sounds'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'enable_sounds'))
  start_in_installation = Checkbox(label="Start in Installation Page", tooltip="When launching app, switch to Installer tab. Saves time..", value=prefs['start_in_installation'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'start_in_installation'))
  disable_nsfw_filter = Checkbox(label="Disable NSFW Filters", value=prefs['disable_nsfw_filter'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=toggle_nsfw)
  retry_attempts = Container(NumberPicker(label="Retry Attempts if Not Safe", min=0, max=8, value=prefs['retry_attempts'], on_change=lambda e:changed(e, 'retry_attempts')), padding=padding.only(left=20), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  retry_attempts.width = 0 if prefs['disable_nsfw_filter'] else None
  api_instructions = Container(height=170, content=Markdown("Get **HuggingFace API key** from https://huggingface.co/settings/tokens and accept the cards for [1.5 model](https://huggingface.co/runwayml/stable-diffusion-v1-5), [1.4 model](https://huggingface.co/CompVis/stable-diffusion-v1-4) & [Inpainting model](https://huggingface.co/runwayml/stable-diffusion-inpainting).\n\nGet **Stability-API key** from https://beta.dreamstudio.ai/membership?tab=apiKeys then API key\n\nGet **OpenAI GPT-3 API key** from https://beta.openai.com, user menu, View API Keys\n\nGet **TextSynth GPT-J key** from https://TextSynth.com, login, Setup\n\nGet **Replicate API Token** from https://replicate.com/account, for Material Diffusion", extension_set="gitHubWeb", on_tap_link=open_url))
  HuggingFace_api = TextField(label="HuggingFace API Key", value=prefs['HuggingFace_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'HuggingFace_api_key'))
  Stability_api = TextField(label="Stability.ai API Key", value=prefs['Stability_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'Stability_api_key'))
  OpenAI_api = TextField(label="OpenAI API Key", value=prefs['OpenAI_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'OpenAI_api_key'))
  TextSynth_api = TextField(label="TextSynth API Key", value=prefs['TextSynth_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'TextSynth_api_key'))
  Replicate_api = TextField(label="Replicate API Key", value=prefs['Replicate_api_key'], password=True, can_reveal_password=True, on_change=lambda e:changed(e, 'Replicate_api_key'))
  #save_button = ElevatedButton(content=Text(value="💾  Save Settings", size=20), on_click=save_settings, style=b_style())
  
  c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text ("⚙️   Deluxe Stable Diffusion Settings & Preferences", style=TextThemeStyle.TITLE_LARGE),
        Divider(thickness=1, height=4),
        #save_to_GDrive,
        ResponsiveRow([image_output, optional_cache_dir], run_spacing=2),
        #VerticalDivider(thickness=2),
        Row([file_prefix, file_suffix_seed]) if page.width > 500 else Column([file_prefix, file_suffix_seed]),
        Row([file_max_length, file_allowSpace]),
        #file_allowSpace,
        #file_max_length,
        #Row([disable_nsfw_filter, retry_attempts]),
        #VerticalDivider(thickness=2, width=1),
        save_image_metadata,
        Row([meta_ArtistName, meta_Copyright]) if page.width > 712 else Column([meta_ArtistName, meta_Copyright]),
        Row([save_config_in_metadata, save_config_json,]),
        Row([theme_mode, theme_color]),
        Row([enable_sounds, start_in_installation]),
        #VerticalDivider(thickness=2, width=1),
        HuggingFace_api,
        Stability_api,
        OpenAI_api,
        TextSynth_api,
        Replicate_api,
        api_instructions,
        #save_button,
        Container(content=None, height=32),
      ],  
  ))], scroll=ScrollMode.AUTO,)
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
def alert_msg(page, msg, content=None, okay=""):
      if prefs['enable_sounds']: page.snd_error.play()
      okay = ElevatedButton("👌  OKAY " if okay == "" else okay, on_click=close_alert_dlg)
      page.alert_dlg = AlertDialog(title=Text(msg), content=content, actions=[okay], actions_alignment=MainAxisAlignment.END)
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
  global prefs, status, model_path
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
      prefs['install_diffusers'] = install_diffusers.content.value
      diffusers_settings.height=None if prefs['install_diffusers'] else 0
      diffusers_settings.update()
      status['changed_installers'] = True
  install_diffusers = Tooltip(message="Required Libraries for most Image Generation functionality", content=Switch(label="Install HuggingFace Diffusers Pipeline", value=prefs['install_diffusers'], disabled=status['installed_diffusers'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_diffusers))

  scheduler_mode = Dropdown(label="Scheduler/Sampler Mode", hint_text="They're very similar, with minor differences in the noise", width=200,
            options=[
                dropdown.Option("DDIM"),
                dropdown.Option("K-LMS"),
                dropdown.Option("PNDM"),
                #dropdown.Option("DDPM"),
                dropdown.Option("DPM Solver"),
                dropdown.Option("DPM Solver++"),
                dropdown.Option("K-Euler Discrete"),
                dropdown.Option("K-Euler Ancestrial"),
                #dropdown.Option("Heun Discrete"),
                #dropdown.Option("K-DPM2 Ancestral"),
                #dropdown.Option("K-DPM2 Discrete"),
            ], value=prefs['scheduler_mode'], autofocus=False, on_change=lambda e:changed(e, 'scheduler_mode'),
        )
  def changed_model_ckpt(e):
      changed(e, 'model_ckpt')
      model = get_model(e.control.value)
      model_card.value = f"  [**Model Card**](https://huggingface.co/{model['path']})"
      model_card.update()
      if e.control.value.startswith("Stable"):
        custom_area.content = model_card
      elif e.control.value == "Community Finetuned Model":
        custom_area.content = Row([finetuned_model, model_card])
      elif e.control.value == "DreamBooth Library Model":
        custom_area.content = Row([dreambooth_library, model_card])
      elif e.control.value == "Custom Model Path":
        custom_area.content = Row([custom_model, model_card])
      custom_area.update()
  def changed_finetuned_model(e):
      changed(e, 'finetuned_model')
      model = get_finetuned_model(e.control.value)
      model_card.value = f"  [**Model Card**](https://huggingface.co/{model['path']})"
      model_card.update()
  def changed_dreambooth_library(e):
      changed(e, 'dreambooth_model')
      model = get_dreambooth_model(e.control.value)
      model_card.value = f"  [**Model Card**](https://huggingface.co/{model['path']})"
      model_card.update()
  def changed_custom_model(e):
      changed(e, 'custom_model')
      model = {'name': 'Custom Model', 'path': e.control.value, 'prefix': ''}
      model_card.value = f"  [**Model Card**](https://huggingface.co/{model['path']})"
      model_card.update()
  def toggle_safe(e):
      changed(e, 'install_safe')
      safety_config.visible = e.control.value
      safety_config.update()
  model = get_model(prefs['model_ckpt'])
  model_path = model['path']
  model_ckpt = Container(Dropdown(label="Model Checkpoint", width=262, options=[
      dropdown.Option("Stable Diffusion v2.1 x768"), dropdown.Option("Stable Diffusion v2.1 x512"), 
      dropdown.Option("Stable Diffusion v2.0 x768"), dropdown.Option("Stable Diffusion v2.0 x512"), dropdown.Option("Stable Diffusion v1.5"), dropdown.Option("Stable Diffusion v1.4"), 
      dropdown.Option("Community Finetuned Model"), dropdown.Option("DreamBooth Library Model"), dropdown.Option("Custom Model Path")], value=prefs['model_ckpt'], tooltip="Make sure you accepted the HuggingFace Model Cards first", autofocus=False, on_change=changed_model_ckpt), col={'xs':9, 'lg':4}, width=262)
  finetuned_model = Dropdown(label="Finetuned Model", tooltip="Make sure you accepted the HuggingFace Model Cards first", width=370, options=[], value=prefs['finetuned_model'], autofocus=False, on_change=changed_finetuned_model, col={'xs':10, 'lg':4})
  model_card = Markdown(f"  [**Model Card**](https://huggingface.co/{model['path']})", on_tap_link=lambda e: e.page.launch_url(e.data))
  for mod in finetuned_models:
      finetuned_model.options.append(dropdown.Option(mod["name"]))
  dreambooth_library = Dropdown(label="DreamBooth Library", hint_text="", width=370, options=[], value=prefs['dreambooth_model'], autofocus=False, on_change=changed_dreambooth_library, col={'xs':10, 'md':4})
  for db in dreambooth_models:
      dreambooth_library.options.append(dropdown.Option(db["name"]))
  custom_model = TextField(label="Custom Model Path", value=prefs['custom_model'], width=370, on_change=changed_custom_model)
  #custom_area = AnimatedSwitcher(model_card, transition="scale", duration=500, reverse_duration=200, switch_in_curve=AnimationCurve.EASE_OUT, switch_out_curve="easeIn")
  custom_area = Container(model_card, col={'xs':4, 'lg':2})
  if prefs['model_ckpt'].startswith("Stable"):
      custom_area.content = model_card
  elif prefs['model_ckpt'] == "Community Finetuned Model":
      custom_area.content = Row([finetuned_model, model_card], col={'xs':9, 'lg':4})
  elif prefs['model_ckpt'] == "DreamBooth Library Model":
      custom_area.content = Row([dreambooth_library, model_card], col={'xs':9, 'lg':4})
  elif prefs['model_ckpt'] == "Custom Model Path":
      custom_area.content = Row([custom_model, model_card], col={'xs':9, 'lg':4})
  model_row = ResponsiveRow([model_ckpt, custom_area], run_spacing=8)
  memory_optimization = Dropdown(label="Enable Memory Optimization", width=350, options=[dropdown.Option("None"), dropdown.Option("Attention Slicing"), dropdown.Option("Xformers Mem Efficient Attention")], value=prefs['memory_optimization'], on_change=lambda e:changed(e, 'memory_optimization'))
  higher_vram_mode = Checkbox(label="Higher VRAM Mode", tooltip="Adds a bit more precision but takes longer & uses much more GPU memory. Not recommended.", value=prefs['higher_vram_mode'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'higher_vram_mode'))
  sequential_cpu_offload = Checkbox(label="Enable Sequential CPU Offload", tooltip="Offloads all models to CPU using accelerate, significantly reducing memory usage.", value=prefs['sequential_cpu_offload'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'sequential_cpu_offload'))
  enable_attention_slicing = Checkbox(label="Enable Attention Slicing", tooltip="Saves VRAM while creating images so you can go bigger without running out of mem.", value=prefs['enable_attention_slicing'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'enable_attention_slicing'))
  enable_vae_slicing = Checkbox(label="Enable VAE Slicing", tooltip="Sliced VAE decode latents for larger batches of images with limited VRAM. Splits the input tensor in slices to compute decoding in several steps", value=prefs['vae_slicing'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'vae_slicing'))
  #install_megapipe = Switch(label="Install Stable Diffusion txt2image, img2img & Inpaint Mega Pipeline", value=prefs['install_megapipe'], disabled=status['installed_megapipe'], on_change=lambda e:changed(e, 'install_megapipe'))
  install_text2img = Tooltip(message="The best general purpose component. Create images with long prompts, weights & models", content=Switch(label="Install Stable Diffusion text2image, image2image & Inpaint Pipeline (/w Long Prompt Weighting)", value=prefs['install_text2img'], disabled=status['installed_txt2img'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_text2img')))
  install_img2img = Tooltip(message="Gets more coherant results modifying Inpaint init & mask images", content=Switch(label="Install Stable Diffusion Specialized Inpainting Model for image2image & Inpaint Pipeline", value=prefs['install_img2img'], disabled=status['installed_img2img'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_img2img')))
  #install_repaint = Tooltip(message="Without using prompts, redraw masked areas to remove and repaint.", content=Switch(label="Install Stable Diffusion RePaint Pipeline", value=prefs['install_repaint'], disabled=status['installed_repaint'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_repaint')))
  install_interpolation = Tooltip(message="Create multiple tween images between prompts latent space. Almost animation.", content=Switch(label="Install Stable Diffusion Prompt Walk Interpolation Pipeline", value=prefs['install_interpolation'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_interpolation'], on_change=lambda e:changed(e, 'install_interpolation')))
  #install_dreamfusion = Tooltip(message="Generate interesting mesh .obj, texture and preview video from a prompt.", content=Switch(label="Install Stable Diffusion DreamFusion 3D Pipeline", value=prefs['install_dreamfusion'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_dreamfusion'], on_change=lambda e:changed(e, 'install_dreamfusion')))
  install_imagic = Tooltip(message="Edit your image according to the prompted instructions like magic.", content=Switch(label="Install Stable Diffusion iMagic image2image Pipeline", value=prefs['install_imagic'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_imagic'], on_change=lambda e:changed(e, 'install_imagic')))
  install_depth2img = Tooltip(message="Uses Depth-map of init image for text-guided image to image generation.", content=Switch(label="Install Stable Diffusion Depth2Image Pipeline", value=prefs['install_depth2img'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_depth2img'], on_change=lambda e:changed(e, 'install_depth2img')))
  install_composable = Tooltip(message="Craft your prompts with precise weights and composed together components.", content=Switch(label="Install Stable Diffusion Composable text2image Pipeline", value=prefs['install_composable'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_composable'], on_change=lambda e:changed(e, 'install_composable')))
  install_safe = Tooltip(message="Use a content quality tuned safety model, providing levels of NSFW protection.", content=Switch(label="Install Stable Diffusion Safe text2image Pipeline", value=prefs['install_safe'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_safe'], on_change=toggle_safe))
  safety_config = Container(Dropdown(label="Model Safety Level", width=350, options=[dropdown.Option("Weak"), dropdown.Option("Medium"), dropdown.Option("Strong"), dropdown.Option("Max")], value=prefs['safety_config'], on_change=lambda e:changed(e, 'safety_config')), padding=padding.only(left=32))
  safety_config.visible = prefs['install_safe']
  install_versatile = Tooltip(message="Multi-flow model that provides both image and text data streams and conditioned on both text and image.", content=Switch(label="Install Versatile Diffusion text2image, Dual Guided & Image Variation Pipeline", value=prefs['install_versatile'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_versatile'], on_change=lambda e:changed(e, 'install_versatile')))
  
  def toggle_clip(e):
      prefs['install_CLIP_guided'] = install_CLIP_guided.content.value
      status['changed_installers'] = True
      clip_settings.height=None if prefs['install_CLIP_guided'] else 0
      clip_settings.update()
  install_CLIP_guided = Tooltip(message="Uses alternative LAION & OpenAI ViT diffusion. Takes more VRAM, so may need to make images smaller", content=Switch(label="Install Stable Diffusion CLIP-Guided Pipeline", value=prefs['install_CLIP_guided'], disabled=status['installed_clip'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_clip))
  clip_model_id = Dropdown(label="CLIP Model ID", width=350,
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
  clip_settings = Container(animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE, padding=padding.only(left=32, top=4), content=Column([clip_model_id]))
  
  def toggle_conceptualizer(e):
      changed(e, 'install_conceptualizer')
      conceptualizer_settings.height = None if e.control.value else 0
      conceptualizer_settings.update()
  def change_concepts_model(e):
      nonlocal concept
      changed(e, 'concepts_model')
      concept = get_concept(e.control.value)
      concepts_info.value = f"To use the concept, include keyword token **<{concept['token']}>** in your Prompts. Info at [https://huggingface.co/sd-concepts-library/{concept['name']}](https://huggingface.co/sd-concepts-library/{concept['name']})"
      concepts_info.update()
  def open_url(e):
      page.launch_url(e.data)
  def copy_token(e):
      nonlocal concept
      page.set_clipboard(f"<{concept['token']}>")
      page.snack_bar = SnackBar(content=Text(f"📋  Token <{concept['token']}> copied to clipboard... Paste as word in your Prompt Text."))
      page.snack_bar.open = True
      page.update()
  install_conceptualizer = Tooltip(message="Loads specially trained concept models to include in prompt with token", content=Switch(label="Install Stable Diffusion Textual-Inversion Conceptualizer Pipeline", value=prefs['install_conceptualizer'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_conceptualizer))
  concept = get_concept(prefs['concepts_model'])
  concepts_model = Dropdown(label="SD-Concepts Library Model", hint_text="Specially trained community models made with Textual-Inversion", width=451, options=[], value=prefs['concepts_model'], on_change=change_concepts_model)
  copy_token_btn = IconButton(icon=icons.CONTENT_COPY, tooltip="Copy Token to Clipboard", on_click=copy_token)
  concepts_row = Row([concepts_model, copy_token_btn])
  concepts_info = Markdown(f"To use the concept, include keyword token **<{concept['token']}>** in your Prompts. Info at [https://huggingface.co/sd-concepts-library/{concept['name']}](https://huggingface.co/sd-concepts-library/{concept['name']})", selectable=True, on_tap_link=open_url)
  conceptualizer_settings = Container(animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE, padding=padding.only(left=32, top=5), content=Column([concepts_row, concepts_info]))
  conceptualizer_settings.height = None if prefs['install_conceptualizer'] else 0
  for c in concepts: concepts_model.options.append(dropdown.Option(c['name']))
  install_upscale = Tooltip(message="Allows you to enlarge images with prompts. Note: Will run out of mem for images larger than 512px, start small.", content=Switch(label="Install Stable Diffusion v2 Upscale 4X Pipeline", value=prefs['install_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, disabled=status['installed_upscale'], on_change=lambda e:changed(e, 'install_upscale')))

  diffusers_settings = Container(animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE, content=
                                 Column([Container(Column([model_row, Container(content=None, height=4), scheduler_mode, higher_vram_mode, 
                                 #memory_optimization, sequential_cpu_offload,
                                 enable_attention_slicing, enable_vae_slicing]), padding=padding.only(left=32, top=4)),
                                         install_text2img, install_img2img, #install_repaint, #install_megapipe, 
                                         install_interpolation, install_CLIP_guided, clip_settings, install_conceptualizer, conceptualizer_settings, install_safe, safety_config, 
                                         install_versatile, install_imagic, install_depth2img, install_composable, install_upscale]))
  def toggle_stability(e):
      prefs['install_Stability_api'] = install_Stability_api.content.value
      has_changed=True
      #print(f"Toggle Stability {prefs['install_Stability_api']}")
      stability_settings.height=None if prefs['install_Stability_api'] else 0
      stability_settings.update()
      page.update()
      #stability_box.content = stability_settings if prefs['install_stability'] else Container(content=None)
      #stability_box.update()
  install_Stability_api = Tooltip(message="Use DreamStudio.com servers without your GPU to create images on CPU.", content=Switch(label="Install Stability-API DreamStudio Pipeline", value=prefs['install_Stability_api'], disabled=status['installed_stability'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_stability))
  use_Stability_api = Checkbox(label="Use Stability-ai API by default", tooltip="Instead of using Diffusers, generate images in their cloud. Can toggle to compare batches..", value=prefs['use_Stability_api'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e, 'use_Stability_api'))
  model_checkpoint = Dropdown(label="Model Checkpoint", hint_text="", width=350, options=[dropdown.Option("stable-diffusion-768-v2-1"), dropdown.Option("stable-diffusion-512-v2-1"), dropdown.Option("stable-diffusion-768-v2-0"), dropdown.Option("stable-diffusion-512-v2-0"), dropdown.Option("stable-diffusion-v1-5"), dropdown.Option("stable-diffusion-v1"), dropdown.Option("stable-inpainting-512-v2-0"), dropdown.Option("stable-inpainting-v1-0")], value=prefs['model_checkpoint'], autofocus=False, on_change=lambda e:changed(e, 'model_checkpoint'))
  clip_guidance_preset = Dropdown(label="Clip Guidance Preset", width=350, options=[dropdown.Option("SIMPLE"), dropdown.Option("FAST_BLUE"), dropdown.Option("FAST_GREEN"), dropdown.Option("SLOW"), dropdown.Option("SLOWER"), dropdown.Option("SLOWEST"), dropdown.Option("NONE")], value=prefs['clip_guidance_preset'], autofocus=False, on_change=lambda e:changed(e, 'clip_guidance_preset'))
  #generation_sampler = Dropdown(label="Generation Sampler", hint_text="", width=350, options=[dropdown.Option("ddim"), dropdown.Option("plms"), dropdown.Option("k_euler"), dropdown.Option("k_euler_ancestral"), dropdown.Option("k_heun"), dropdown.Option("k_dpm_2"), dropdown.Option("k_dpm_2_ancestral"), dropdown.Option("k_lms")], value=prefs['generation_sampler'], autofocus=False, on_change=lambda e:changed(e, 'generation_sampler'))
  generation_sampler = Dropdown(label="Generation Sampler", hint_text="", width=350, options=[dropdown.Option("DDIM"), dropdown.Option("DDPM"), dropdown.Option("K_EULER"), dropdown.Option("K_EULER_ANCESTRAL"), dropdown.Option("K_HEUN"), dropdown.Option("K_DPMPP_2M"), dropdown.Option("K_DPM_2_ANCESTRAL"), dropdown.Option("K_LMS"), dropdown.Option("K_DPMPP_2S_ANCESTRAL"), dropdown.Option("K_DPM_2")], value=prefs['generation_sampler'], autofocus=False, on_change=lambda e:changed(e, 'generation_sampler'))
  #"K_EULER" "K_DPM_2" "K_LMS" "K_DPMPP_2S_ANCESTRAL" "K_DPMPP_2M" "DDIM" "DDPM" "K_EULER_ANCESTRAL" "K_HEUN" "K_DPM_2_ANCESTRAL"
  stability_settings = Container(animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE, padding=padding.only(left=32), content=Column([use_Stability_api, model_checkpoint, generation_sampler, clip_guidance_preset]))
  
  install_ESRGAN = Tooltip(message="Recommended to enlarge & sharpen all images as they're made.", content=Switch(label="Install Real-ESRGAN AI Upscaler", value=prefs['install_ESRGAN'], disabled=status['installed_ESRGAN'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_ESRGAN')))
  install_OpenAI = Tooltip(message="Use advanced AI to help make creative prompts. Also enables DALL-E 2 generation.", content=Switch(label="Install OpenAI GPT-3 Text Engine", value=prefs['install_OpenAI'], disabled=status['installed_OpenAI'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_OpenAI')))
  install_TextSynth = Tooltip(message="Alternative Text AI for brainstorming & rewriting your prompts. Pretty smart..", content=Switch(label="Install TextSynth GPT-J Text Engine", value=prefs['install_TextSynth'], disabled=status['installed_TextSynth'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e, 'install_TextSynth')))
  diffusers_settings.height = None if prefs['install_diffusers'] else 0
  stability_settings.height = None if prefs['install_Stability_api'] else 0
  clip_settings.height = None if prefs['install_CLIP_guided'] else 0
  
  
  def run_installers(e):
      def console_clear():
        page.banner.content.controls = []
        page.update()
      def console_msg(msg, clear=True, show_progress=True):
        if not page.banner.open:
          page.banner.open = True
        if clear:
          page.banner.content.controls = []
        if show_progress:
          page.banner.content.controls.append(Row([Stack([Icon(icons.DOWNLOADING, color=colors.AMBER, size=48), Container(content=ProgressRing(), padding=padding.only(top=6, left=6), alignment=alignment.center)]), Container(content=Text("  " + msg.strip() , weight=FontWeight.BOLD, color=colors.ON_SECONDARY_CONTAINER, size=18), alignment=alignment.bottom_left, padding=padding.only(top=6)) ]))
          #page.banner.content.controls.append(Stack([Container(content=Text(msg.strip() + "  ", weight=FontWeight.BOLD, color=colors.ON_SECONDARY_CONTAINER, size=18), alignment=alignment.bottom_left, padding=padding.only(top=6)), Container(content=ProgressRing(), alignment=alignment.center if page.width > 768 else alignment.center_right)]))
          #page.banner.content.controls.append(Stack([Container(content=Text(msg.strip() + "  ", weight=FontWeight.BOLD, color=colors.ON_SECONDARY_CONTAINER, size=18), alignment=alignment.bottom_left, padding=padding.only(top=6)), Container(content=ProgressRing(), alignment=alignment.center)]))
          #page.banner.content.controls.append(Row([Text(msg.strip() + "  ", weight=FontWeight.BOLD, color=colors.GREEN_600), ProgressRing()]))
        else:
          page.banner.content.controls.append(Text(msg.strip(), weight=FontWeight.BOLD, color=colors.GREEN_600))
        page.update()
      page.console_msg = console_msg
      if status['changed_installers']:
        save_settings_file(page, change_icon=False)
        status['changed_installers'] = False
      # Temporary until I get Xformers to work
      prefs['memory_optimization'] = 'Attention Slicing' if prefs['enable_attention_slicing'] else 'None'
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
      page.banner.content = Column([], scroll=ScrollMode.AUTO, auto_scroll=True, tight=True, spacing=0, alignment=MainAxisAlignment.END)
      page.banner.open = True
      page.update()
      if prefs['install_diffusers']:
        console_msg("Installing Hugging Face Diffusers Pipeline...")
        get_diffusers(page)
        status['installed_diffusers'] = True
      if prefs['install_text2img'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Text2Image, Image2Image & Inpaint Pipeline...")
        #with io.StringIO() as buf, redirect_stdout(buf):
        #print('redirected')
        get_text2image(page)
        #output = buf.getvalue()
        #page.banner.content.controls.append(Text(output.strip()))
        status['installed_txt2img'] = True
        page.img_block.height = None
        page.img_block.update()
        page.update()
      if prefs['install_img2img'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion Inpaint Model & Image2Image Pipeline...")
        get_image2image(page)
        status['installed_img2img'] = True
        page.img_block.height = None
        page.img_block.update()
        page.use_inpaint_model.visible = True
        page.use_inpaint_model.update()
        if not status['installed_txt2img']:
          prefs['use_inpaint_model'] = True
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
      if prefs['install_CLIP_guided'] and prefs['install_diffusers']:
        console_msg("Downloading Stable Diffusion CLIP-Guided Pipeline...")
        get_clip(page)
        status['installed_clip'] = True
        page.use_clip_guided_model.visible = True
        page.use_clip_guided_model.update()
        page.clip_block.height = None if prefs['use_clip_guided_model'] else 0
        page.clip_block.update()
        if prefs['use_clip_guided_model']:
          page.img_block.height = 0
          page.img_block.update()
      if prefs['install_conceptualizer'] and prefs['install_diffusers']:
        console_msg("Installing SD Concepts Library Textual Inversion Pipeline...")
        get_conceptualizer(page)
        page.use_conceptualizer_model.visible = True
        page.use_conceptualizer_model.update()
        if prefs['use_conceptualizer']:
          page.img_block.height = 0
          page.img_block.update()
        status['installed_conceptualizer'] = True
      if prefs['install_repaint'] and not status['installed_repaint'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion RePaint Pipeline...")
        get_repaint(page)
        status['installed_repaint'] = True
      if prefs['install_depth2img'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion 2 Depth2Image Pipeline...")
        get_depth2img(page)
        status['installed_depth2img'] = True
        if not status['installed_txt2img']:
          page.img_block.height = None
          page.img_block.update()
        page.use_depth2img.visible = True
        page.use_depth2img.update()
      if prefs['install_imagic'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion iMagic image2image Pipeline...")
        get_imagic(page)
        status['installed_imagic'] = True
        if not status['installed_txt2img']:
          page.img_block.height = None
          page.img_block.update()
        page.use_imagic.visible = True
        page.use_imagic.update()
      if prefs['install_composable'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion Composable text2image Pipeline...")
        get_composable(page)
        status['installed_composable'] = True
        page.use_composable.visible = True
        page.use_composable.update()
      if prefs['install_versatile'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion Versatile text2image, Variation & Inpaint Pipeline...")
        get_versatile(page)
        status['installed_versatile'] = True
        if not status['installed_txt2img']:
          page.img_block.height = None
          page.img_block.update()
        page.use_versatile.visible = True
        page.use_versatile.update()
      if prefs['install_safe'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion Safe text2image Pipeline...")
        get_safe(page)
        status['installed_safe'] = True
        page.use_safe.visible = True
        page.use_safe.update()
      if prefs['install_upscale'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion 4X Upscale Pipeline...")
        get_upscale(page)
        status['installed_upscale'] = True
        page.use_upscale.visible = True
        page.use_upscale.update()
      if prefs['install_dreamfusion'] and not status['installed_dreamfusion'] and prefs['install_diffusers']:
        console_msg("Installing Stable Diffusion DreamFusion 3D Pipeline...")
        get_dreamfusion(page) # No longer installing from here
        status['installed_dreamfusion'] = True
      if prefs['install_Stability_api']:
        console_msg("Installing Stability-API DreamStudio.ai Pipeline...")
        get_stability(page)
        status['installed_stability'] = True
      if prefs['install_ESRGAN'] and not status['installed_ESRGAN']:
        if not os.path.isdir(os.path.join(dist_dir, 'Real-ESRGAN')):
          get_ESRGAN(page)
          console_msg("Installing Real-ESRGAN Upscaler...")
        status['installed_ESRGAN'] = True
      if prefs['install_ESRGAN']:
        page.ESRGAN_block.height = None
        page.ESRGAN_block_material.height = None
        page.ESRGAN_block_dalle.height = None
        page.ESRGAN_block_kandinsky.height = None
        page.ESRGAN_block_unCLIP.height = None
        page.ESRGAN_block_unCLIP_image_variation.height = None
        page.ESRGAN_block_magic_mix.height = None
        page.ESRGAN_block.update()
        page.ESRGAN_block_material.update()
        page.ESRGAN_block_dalle.update()
        page.ESRGAN_block_kandinsky.update()
        page.ESRGAN_block_unCLIP.update()
        page.ESRGAN_block_unCLIP_image_variation.update()
        page.ESRGAN_block_magic_mix.update()
      if prefs['install_OpenAI'] and not status['installed_OpenAI']:
        try:
          import openai
        except ImportError as e:
          console_msg("Installing OpenAI GPT-3 Libraries...")
          run_process("pip install openai -qq", page=page)
          pass
        status['installed_OpenAI'] = True
      if prefs['install_TextSynth'] and not status['installed_TextSynth']:
        try:
          from textsynthpy import TextSynth, Complete
        except ImportError as e:
          console_msg("Installing TextSynth GPT-J Libraries...")
          run_process("pip install textsynthpy -qq", page=page)
          pass
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
      page.Parameters.controls[0].content.update()
      #page.Parameters.updater()
      page.Installers.controls[0].content.update()
      page.Installers.update()
      page.show_install_fab(False)
      page.tabs.selected_index = 2
      page.tabs.update()
      page.update()
  def show_install_fab(show = True):
    if show:
      page.floating_action_button = FloatingActionButton(icon=icons.FILE_DOWNLOAD, text="Run Installations", on_click=run_installers)
      page.update()
    else:
      if page.floating_action_button is not None:
        page.floating_action_button = None
        page.update()
  page.show_install_fab = show_install_fab
  install_button = ElevatedButton(content=Text(value="⏬   Run Installations ", size=20), on_click=run_installers)
  
  #image_output = TextField(label="Image Output Path", value=prefs['image_output'], on_change=changed)
  c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
                content=Column([
        Text ("📥  Stable Diffusion Required & Optional Installers", style=TextThemeStyle.TITLE_LARGE),
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
        #install_button,
        Container(content=None, height=32),
      ],
  ))], scroll=ScrollMode.AUTO)
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
  #page.img_block.height = None if status['installed_img2img'] or status['installed_megapipe'] or status['installed_stability'] else 0
  page.img_block.height = None if (status['installed_txt2img'] or status['installed_stability']) and not (status['installed_clip'] and prefs['use_clip_guided_model']) else 0
  page.clip_block.height = None if status['installed_clip']  and prefs['use_clip_guided_model'] else 0
  page.ESRGAN_block.height = None if status['installed_ESRGAN'] else 0
  page.img_block.update()
  page.clip_block.update()
  page.ESRGAN_block.update()
  page.Parameters.update()
  #print("Updated Parameters")

if is_Colab:
    from google.colab import files
def buildParameters(page):
  global prefs, status, args
  def changed(e, pref=None, asInt=False):
      if pref is not None:
        prefs[pref] = e.control.value if not asInt else int(e.control.value)
      if page.floating_action_button is None:
        show_apply_fab(len(prompts) > 0)
      #if apply_changes_button.visible != (len(prompts) > 0): #status['changed_parameters']:
      #  apply_changes_button.visible = len(prompts) > 0
      #  apply_changes_button.update()
      status['changed_parameters'] = True
      #page.update()
  def run_parameters(e):
      save_parameters()
      #page.tabs.current_tab = 3
      page.show_apply_fab(False)
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
      save_settings_file(page)
      show_apply_fab(False)
      #apply_changes_button.visible = False
      #apply_changes_button.update()
  def pick_files_result(e: FilePickerResultEvent):
      # TODO: This is not working on Colab, maybe it can get_upload_url on other platform?
      if e.files:
        img = e.files
        uf = []
        fname = img[0]
        print(", ".join(map(lambda f: f.name, e.files)))
        #print(os.path.join(fname.path, fname.name))
        #src_path = os.path.join(fname.path, fname.name)
        #for f in pick_files_dialog.result.files:
        src_path = page.get_upload_url(fname.name, 600)
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

  def file_picker_result(e: FilePickerResultEvent):
      if e.files != None:
        upload_files(e)
  def on_upload_progress(e: FilePickerUploadEvent):
    nonlocal pick_type
    if e.progress == 1:
      fname = os.path.join(root_dir, e.file_name)
      if pick_type == "init":
        init_image.value = fname
        init_image.update()
        prefs['init_image'] = fname
      elif pick_type == "mask":
        mask_image.value = fname
        mask_image.update()
        prefs['mask_image'] = fname
      page.update()
  file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
  def upload_files(e):
      uf = []
      if file_picker.result != None and file_picker.result.files != None:
          for f in file_picker.result.files:
              uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
          file_picker.upload(uf)
  page.overlay.append(file_picker)
  pick_type = ""
  #page.overlay.append(pick_files_dialog)
  def pick_init(e):
      nonlocal pick_type
      pick_type = "init"
      file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File")
  def pick_mask(e):
      nonlocal pick_type
      pick_type = "mask"
      file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Black & White Mask Image")
  def toggle_ESRGAN(e):
      ESRGAN_settings.height = None if e.control.value else 0
      prefs['apply_ESRGAN_upscale'] = e.control.value
      ESRGAN_settings.update()
      has_changed = True
  def toggle_clip(e):
      if e.control.value:
        page.img_block.height = 0
        page.clip_block.height = None if status['installed_clip'] else 0
      else:
        page.img_block.height = None if status['installed_txt2img'] or status['installed_stability'] else 0
        page.clip_block.height = 0
      page.img_block.update()
      page.clip_block.update()
      changed(e, 'use_clip_guided_model')
  def change_use_cutouts(e):
      num_cutouts.visible = e.control.value
      num_cutouts.update()
      changed(e, 'use_cutouts')
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
      interpolation_steps_slider.update()
      if e.control.value: page.img_block.height = 0
      else: page.img_block.height = None if status['installed_txt2img'] or status['installed_stability'] else 0
      page.img_block.update()
      changed(e, 'use_interpolation')
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
  def toggle_conceptualizer(e):
      if e.control.value:
        page.img_block.height = 0
      else:
        page.img_block.height = None if status['installed_txt2img'] or status['installed_stability'] else 0
      page.img_block.update()
      changed(e, 'use_conceptualizer')
  def toggle_centipede(e):
      changed(e,'centipede_prompts_as_init_images')
      image_pickers.height = None if not e.control.value else 0
      image_pickers.update()
  has_changed = False
  batch_folder_name = TextField(label="Batch Folder Name", value=prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
  batch_size = TextField(label="Batch Size", value=prefs['batch_size'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'batch_size'))
  n_iterations = TextField(label="Number of Iterations", value=prefs['n_iterations'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'n_iterations'))
  steps = TextField(label="Steps", value=prefs['steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'steps', asInt=True))
  eta = TextField(label="DDIM ETA", value=prefs['eta'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'eta'))
  seed = TextField(label="Seed", value=prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'seed'))
  param_rows = Row([Column([batch_folder_name, batch_size, n_iterations]), Column([steps, eta, seed])])
  guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=prefs['guidance_scale'], on_change=change_guidance, expand=True)
  guidance_value = Text(f" {prefs['guidance_scale']}", weight=FontWeight.BOLD)
  guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
  width = Slider(min=256, max=1280, divisions=64, label="{value}px", value=prefs['width'], on_change=change_width, expand=True)
  width_value = Text(f" {int(prefs['width'])}px", weight=FontWeight.BOLD)
  width_slider = Row([Text(f"Width: "), width_value, width])
  height = Slider(min=256, max=1280, divisions=64, label="{value}px", value=prefs['height'], on_change=change_height, expand=True)
  height_value = Text(f" {int(prefs['height'])}px", weight=FontWeight.BOLD)
  height_slider = Row([Text(f"Height: "), height_value, height])

  init_image = TextField(label="Init Image", value=prefs['init_image'], on_change=lambda e:changed(e,'init_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
  mask_image = TextField(label="Mask Image", value=prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask))
  alpha_mask = Checkbox(label="Alpha Mask", value=prefs['alpha_mask'], tooltip="Use Transparent Alpha Channel of Init as Mask", fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'alpha_mask'))
  invert_mask = Checkbox(label="Invert Mask", value=prefs['invert_mask'], tooltip="Reverse Black & White of Image Mask", fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'))
  image_pickers = Container(content=ResponsiveRow([Row([init_image, alpha_mask], col={"lg":6}), Row([mask_image, invert_mask], col={"lg":6})]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  image_pickers.height = None if not prefs['centipede_prompts_as_init_images'] else 0
  init_image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=prefs['init_image_strength'], on_change=change_strength, expand=True)
  strength_value = Text(f" {int(prefs['init_image_strength'] * 100)}%", weight=FontWeight.BOLD)
  strength_slider = Row([Text("Init Image Strength: "), strength_value, init_image_strength])
  page.use_inpaint_model = Tooltip(message="When using init_image and/or mask, use the newer pipeline for potentially better results", content=Switch(label="Use Specialized Inpaint Model Instead", tooltip="When using init_image and/or mask, use the newer pipeline for potentially better results", value=prefs['use_inpaint_model'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_inpaint_model')))
  page.use_inpaint_model.visible = status['installed_img2img']
  page.use_versatile = Tooltip(message="Dual Guided between prompt & image, or create Image Variation", content=Switch(label="Use Versatile Pipeline Model Instead", value=prefs['use_versatile'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_versatile')))
  page.use_versatile.visible = status['installed_versatile']
  centipede_prompts_as_init_images = Tooltip(message="Feeds each image to the next prompt sequentially down the line", content=Switch(label="Centipede Prompts as Init Images", tooltip="Feeds each image to the next prompt sequentially down the line", value=prefs['centipede_prompts_as_init_images'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_centipede))
  use_interpolation = Tooltip(message="Creates animation frames transitioning, but it's not always perfect.", content=Switch(label="Use Interpolation to Walk Latent Space between Prompts", tooltip="Creates animation frames transitioning, but it's not always perfect.", value=prefs['use_interpolation'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_interpolation))
  interpolation_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=prefs['num_interpolation_steps'], on_change=change_interpolation_steps, expand=True)
  interpolation_steps_value = Text(f" {int(prefs['num_interpolation_steps'])} steps", weight=FontWeight.BOLD)
  interpolation_steps_slider = Container(Row([Text(f"Number of Interpolation Steps between Prompts: "), interpolation_steps_value, interpolation_steps]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  Row([Text(f"Number of Interpolation Steps between Prompts: "), interpolation_steps_value, interpolation_steps])
  if not bool(prefs['use_interpolation']):
    interpolation_steps_slider.height = 0
  page.interpolation_block = Column([use_interpolation, interpolation_steps_slider])
  page.img_block = Container(Column([image_pickers, strength_slider, page.use_inpaint_model, centipede_prompts_as_init_images, Divider(height=9, thickness=2)]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  if not status['installed_interpolation']:
    page.interpolation_block.visible = False
  elif bool(prefs['use_interpolation']):
    page.img_block.height = 0
  page.use_clip_guided_model = Tooltip(message="Uses more VRAM, so you'll probably need to make image size smaller", content=Switch(label="Use CLIP-Guided Model", tooltip="Uses more VRAM, so you'll probably need to make image size smaller", value=prefs['use_clip_guided_model'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_clip))
  clip_guidance_scale = Slider(min=1, max=5000, divisions=4999, label="{value}", value=prefs['clip_guidance_scale'], on_change=lambda e:changed(e,'clip_guidance_scale'), expand=True)
  clip_guidance_scale_slider = Row([Text("CLIP Guidance Scale: "), clip_guidance_scale])
  use_cutouts = Checkbox(label="Use Cutouts", value=bool(prefs['use_cutouts']), fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=change_use_cutouts)
  num_cutouts = NumberPicker(label="    Number of Cutouts: ", min=1, max=10, value=prefs['num_cutouts'], on_change=lambda e: changed(e, 'num_cutouts', asInt=True))
  num_cutouts.visible = bool(prefs['use_cutouts'])
  #num_cutouts = TextField(label="Number of Cutouts", value=prefs['num_cutouts'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_cutouts', asInt=True))
  unfreeze_unet = Checkbox(label="Unfreeze UNET", value=prefs['unfreeze_unet'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'unfreeze_unet'))
  unfreeze_vae = Checkbox(label="Unfreeze VAE", value=prefs['unfreeze_vae'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'unfreeze_vae'))
  page.clip_block = Container(Column([clip_guidance_scale_slider, Row([use_cutouts, num_cutouts], expand=False), unfreeze_unet, unfreeze_vae, Divider(height=9, thickness=2)]), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  page.use_conceptualizer_model = Tooltip(message="Use Textual-Inversion Community Model Concepts", content=Switch(label="Use Custom Conceptualizer Model", tooltip="Use Textual-Inversion Community Model", value=prefs['use_conceptualizer'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_conceptualizer))
  page.use_conceptualizer_model.visible = bool(status['installed_conceptualizer'])
  page.use_depth2img = Tooltip(message="To use, provide init_image with a good composition and prompts to approximate same depth.", content=Switch(label="Use Depth2Image Pipeline for img2img init image generation", value=prefs['use_depth2img'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_depth2img')))
  page.use_depth2img.visible = bool(status['installed_depth2img'])
  page.use_imagic = Tooltip(message="Allows you to edit an image with prompt text.", content=Switch(label="Use iMagic for img2img init image editing", value=prefs['use_imagic'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_imagic')))
  page.use_imagic.visible = bool(status['installed_imagic'])
  page.use_composable = Tooltip(message="Allows conjunction and negation operators for compositional generation with conditional diffusion models", content=Switch(label="Use Composable Prompts for txt2img Weight | Segments", value=prefs['use_composable'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_composable')))
  page.use_composable.visible = bool(status['installed_composable'])
  page.use_safe = Tooltip(message="Models trained only on Safe images", content=Switch(label="Use Safe Diffusion Pipeline instead", value=prefs['use_safe'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_safe')))
  page.use_safe.visible = bool(status['installed_safe'])
  page.use_upscale = Tooltip(message="Enlarges your Image Generations guided by the same Prompt.", content=Switch(label="Upscale 4X with Stable Diffusion 2", value=prefs['use_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=lambda e:changed(e,'use_upscale')))
  page.use_upscale.visible = bool(status['installed_upscale'])
  apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
  enlarge_scale_value = Text(f" {float(prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
  enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
  enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
  face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
  display_upscaled_image = Checkbox(label="Display Upscaled Image", value=prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
  ESRGAN_settings = Container(Column([enlarge_scale_slider, face_enhance, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  page.ESRGAN_block = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
  page.img_block.height = None if status['installed_txt2img'] or status['installed_stability'] else 0
  page.use_clip_guided_model.visible = status['installed_clip']
  page.clip_block.height = None if status['installed_clip'] and prefs['use_clip_guided_model'] else 0
  page.ESRGAN_block.height = None if status['installed_ESRGAN'] else 0
  if not prefs['apply_ESRGAN_upscale']:
    ESRGAN_settings.height = 0
  parameters_button = ElevatedButton(content=Text(value="📜   Continue to Image Prompts", size=20), on_click=run_parameters)
  #apply_changes_button = ElevatedButton(content=Text(value="🔀   Apply Changes to Current Prompts", size=20), on_click=apply_to_prompts)
  #apply_changes_button.visible = len(prompts) > 0 and status['changed_parameters']
  def show_apply_fab(show = True):
    if show:
      page.floating_action_button = FloatingActionButton(icon=icons.TRANSFORM, text="Apply Changes to Current Prompts", on_click=apply_to_prompts)
      page.update()
    else:
      if page.floating_action_button is not None:
        page.floating_action_button = None
        page.update()
  show_apply_fab(len(prompts) > 0 and status['changed_parameters'])
  page.show_apply_fab = show_apply_fab
  parameters_row = Row([parameters_button], alignment=MainAxisAlignment.SPACE_BETWEEN)
  def updater():
      #parameters.update()
      c.update()
      page.update()
      #print("Updated Parameters Page")

  c = Column([Container(
      padding=padding.only(18, 14, 20, 10), content=Column([
        Text ("📝  Stable Diffusion Image Parameters", style=TextThemeStyle.TITLE_LARGE),
        Divider(thickness=1, height=4),
        param_rows, guidance, width_slider, height_slider, #Divider(height=9, thickness=2), 
        page.interpolation_block, page.use_safe, page.img_block, page.use_clip_guided_model, page.clip_block, page.use_versatile, page.use_conceptualizer_model, page.use_imagic, page.use_depth2img, page.use_composable, page.use_upscale, page.ESRGAN_block,
        #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
        #parameters_row,
      ],
  ))], scroll=ScrollMode.AUTO)#batch_folder_name, batch_size, n_iterations, steps, eta, seed, 
  return c

prompts = []
args = {}

def update_args():
    global args
    args = {
        "batch_size":int(prefs['batch_size']),
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
        "alpha_mask": prefs['alpha_mask'],
        "invert_mask": prefs['invert_mask'],
        "prompt2": None, "tweens": 10,
        "negative_prompt": None,
        "use_clip_guided_model": prefs['use_clip_guided_model'],
        "clip_prompt": "",
        "clip_guidance_scale": float(prefs['clip_guidance_scale']),
        "use_cutouts": bool(prefs['use_cutouts']),
        "num_cutouts": int(prefs['num_cutouts']),
        "unfreeze_unet": prefs['unfreeze_unet'],
        "unfreeze_vae": prefs['unfreeze_vae'],
        "use_Stability": False,
        "use_conceptualizer": False} 

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
          elif key=="alpha_mask": self.arg[key] = value
          elif key=="invert_mask": self.arg[key] = value
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
          elif key=="use_conceptualizer": self.arg[key] = value
          elif key=="prompt": self.prompt = value
          else: print(f"Unknown argument: {key} = {value}")
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
  global prompts, args, prefs
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
      def changed_tweens(e):
          prefs['tweens'] = int(e.control.value)
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
          arg['alpha_mask'] = alpha_mask.value
          arg['invert_mask'] = invert_mask.value
          arg['prompt2'] = prompt2.value if bool(use_prompt_tweening.value) else None
          arg['tweens'] = int(tweens.value)
          arg['negative_prompt'] = negative_prompt.value if bool(negative_prompt.value) else None
          arg['use_clip_guided_model'] = use_clip_guided_model.content.value
          arg['clip_guidance_scale'] = float(clip_guidance_scale.value)
          arg['use_cutouts'] = use_cutouts.value
          arg['num_cutouts'] = int(num_cutouts.value)
          arg['unfreeze_unet'] = unfreeze_unet.value
          arg['unfreeze_vae'] = unfreeze_vae.value
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
      def file_picker_result(e: FilePickerResultEvent):
          if e.files != None:
            upload_files(e)
      def on_upload_progress(e: FilePickerUploadEvent):
        nonlocal pick_type
        if e.progress == 1:
          fname = os.path.join(root_dir, e.file_name)
          if pick_type == "init":
            init_image.value = fname
            init_image.update()
            prefs['init_image'] = fname
          elif pick_type == "mask":
            mask_image.value = fname
            mask_image.update()
            prefs['mask_image'] = fname
          page.update()
      file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
      def upload_files(e):
          uf = []
          if file_picker.result != None and file_picker.result.files != None:
              for f in file_picker.result.files:
                  uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
              file_picker.upload(uf)
      page.overlay.append(file_picker)
      pick_type = ""
      #page.overlay.append(pick_files_dialog)
      def pick_init(e):
          nonlocal pick_type
          pick_type = "init"
          file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File")
      def pick_mask(e):
          nonlocal pick_type
          pick_type = "mask"
          file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Black & White Mask Image")
      def change_width(e):
          width_slider.controls[1].value = f" {int(e.control.value)}px"
          width_slider.update()
      def change_height(e):
          height_slider.controls[1].value = f" {int(e.control.value)}px"
          height_slider.update()
      def toggle_clip(e):
          if e.control.value:
            img_block.height = 0
            clip_block.height = None if status['installed_clip'] else 0
          else:
            img_block.height = None if status['installed_txt2img'] or status['installed_stability'] else 0
            clip_block.height = 0
          img_block.update()
          clip_block.update()
          changed(e)
      arg = open_dream.arg #e.control.data.arg
      edit_text = TextField(label="Composable | Prompt | Text" if prefs['use_composable'] and status['installed_composable'] else "Prompt Text", expand=3, value=open_dream.prompt, multiline=True)
      negative_prompt = TextField(label="Segmented Weights 1 | -0.7 | 1.2" if prefs['use_composable'] and status['installed_composable'] else "Negative Prompt Text", expand=1, value=str((arg['negative_prompt'] or '') if 'negative_prompt' in arg else ''), on_change=changed)
      #batch_folder_name = TextField(label="Batch Folder Name", value=arg['batch_folder_name'], on_change=changed)
      #print(str(arg))
      prompt_tweening = bool(arg['prompt2']) if 'prompt2' in arg else False
      use_prompt_tweening = Switch(label="Prompt Tweening", value=prompt_tweening, active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=changed_tweening)
      prompt2 = TextField(label="Prompt 2 Transition Text", expand=True, value=arg['prompt2'] if 'prompt2' in arg else '', on_change=changed)
      tweens = TextField(label="# of Tweens", value=str(arg['tweens'] if 'tweens' in arg else 8), keyboard_type=KeyboardType.NUMBER, on_change=changed, width = 90)
      #tweens =  NumberPicker(label="# of Tweens: ", min=2, max=300, value=int(arg['tweens'] if 'tweens' in arg else 8), on_change=changed_tweens),
      #prompt2.visible = prompt_tweening
      #tweens.visible = prompt_tweening
      tweening_params = Container(Row([Container(content=None, width=8), prompt2, tweens]), padding=padding.only(top=4, bottom=3), animate_size=animation.Animation(1000, AnimationCurve.EASE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
      tweening_params.height = None if prompt_tweening else 0
      tweening_row = Row([use_prompt_tweening, ])#tweening_params

      batch_size = TextField(label="Batch Size", value=str(arg['batch_size']), keyboard_type=KeyboardType.NUMBER, on_change=changed)
      n_iterations = TextField(label="Number of Iterations", value=str(arg['n_iterations']), keyboard_type=KeyboardType.NUMBER, on_change=changed)
      steps = TextField(label="Steps", value=str(arg['steps']), keyboard_type=KeyboardType.NUMBER, on_change=changed)
      eta = TextField(label="DDIM ETA", value=str(arg['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise (only with DDIM sampler)", on_change=changed)
      seed = TextField(label="Seed", value=str(arg['seed']), keyboard_type=KeyboardType.NUMBER, hint_text="0 or -1 picks a Random seed", on_change=changed)
      guidance_scale = TextField(label="Guidance Scale", value=str(arg['guidance_scale']), keyboard_type=KeyboardType.NUMBER, on_change=changed)
      param_columns = Row([Column([batch_size, n_iterations, steps]), Column([guidance_scale, seed, eta])])
      #guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=arg['guidance_scale'], expand=True)
      #guidance = Row([Text("Guidance Scale: "), guidance_scale])
      width = Slider(min=256, max=1280, divisions=64, label="{value}px", value=float(arg['width']), expand=True, on_change=change_width)
      width_value = Text(f" {int(arg['width'])}px", weight=FontWeight.BOLD)
      width_slider = Row([Text("Width: "), width_value, width])
      height = Slider(min=256, max=1280, divisions=64, label="{value}px", value=float(arg['height']), expand=True, on_change=change_height)
      height_value = Text(f" {int(arg['height'])}px", weight=FontWeight.BOLD)
      height_slider = Row([Text("Height: "), height_value, height])
      init_image = TextField(label="Init Image", value=arg['init_image'], expand=1, on_change=changed, height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
      mask_image = TextField(label="Mask Image", value=arg['mask_image'], expand=1, on_change=changed, height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask))
      alpha_mask = Checkbox(label="Alpha Mask", value=arg['alpha_mask'], tooltip="Use Transparent Alpha Channel of Init as Mask", fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=changed)
      invert_mask = Checkbox(label="Invert Mask", value=arg['invert_mask'], tooltip="Reverse Black & White of Image Mask", fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=changed)
      image_row = ResponsiveRow([Row([init_image, alpha_mask], col={"lg":6}), Row([mask_image, invert_mask], col={"lg":6})])
      init_image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=float(arg['init_image_strength']), expand=True)
      strength_slider = Row([Text("Init Image Strength: "), init_image_strength])
      img_block = Container(content=Column([image_row, strength_slider]), padding=padding.only(top=4, bottom=3), animate_size=animation.Animation(1000, AnimationCurve.EASE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
      img_block.height = None if (status['installed_txt2img'] or status['installed_stability']) else 0
      use_clip_guided_model = Tooltip(message="Uses more VRAM, so you'll probably need to make image size smaller", content=Switch(label="Use CLIP-Guided Model", tooltip="Uses more VRAM, so you'll probably need to make image size smaller", value=arg['use_clip_guided_model'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_clip))
      clip_guidance_scale = Slider(min=1, max=5000, divisions=4999, label="{value}", value=arg['clip_guidance_scale'], on_change=changed, expand=True)
      clip_guidance_scale_slider = Row([Text("CLIP Guidance Scale: "), clip_guidance_scale])
      use_cutouts = Checkbox(label="Use Cutouts", value=bool(arg['use_cutouts']), fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=changed)
      num_cutouts = NumberPicker(label="    Number of Cutouts: ", min=1, max=10, value=arg['num_cutouts'], on_change=changed)
      #num_cutouts.visible = bool(prefs['use_cutouts'])
      #num_cutouts = TextField(label="Number of Cutouts", value=prefs['num_cutouts'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_cutouts', asInt=True))
      unfreeze_unet = Checkbox(label="Unfreeze UNET", value=arg['unfreeze_unet'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=changed)
      unfreeze_vae = Checkbox(label="Unfreeze VAE", value=arg['unfreeze_vae'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=changed)
      clip_block = Container(Column([clip_guidance_scale_slider, Row([use_cutouts, num_cutouts], expand=False), unfreeze_unet, unfreeze_vae, Divider(height=9, thickness=2)]), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
      if not status['installed_clip']:
        use_clip_guided_model.visible = False
        clip_block.height = 0
      elif not arg['use_clip_guided_model']:
        clip_block.height = 0
      dlg_modal = AlertDialog(modal=False, title=Text("📝  Edit Prompt Dream Parameters"), content=Container(Column([
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
            width_slider, height_slider, img_block,
            use_clip_guided_model, clip_block,
            #Row([Column([batch_size, n_iterations, steps, eta, seed,]), Column([guidance, width_slider, height_slider, Divider(height=9, thickness=2), (img_block if prefs['install_img2img'] else Container(content=None))])],),
          ], alignment=MainAxisAlignment.START, tight=True, width=page.width - 200, height=page.height - 100, scroll=ScrollMode.AUTO), width=page.width - 200, height=page.height - 100), actions=[TextButton("Cancel", on_click=close_dlg), ElevatedButton(content=Text(value=emojize(":floppy_disk:") + "  Save Prompt ", size=19, weight=FontWeight.BOLD), on_click=save_dlg)], actions_alignment=MainAxisAlignment.END)
      e.page.dialog = dlg_modal
      dlg_modal.open = True
      e.page.update()
  def prompt_help(e):
      def close_help_dlg(e):
        nonlocal prompt_help_dlg
        prompt_help_dlg.open = False
        page.update()
      prompt_help_dlg = AlertDialog(title=Text("💁   Help with Prompt Creations"), content=Column([
          Text("You can keep your text prompts simple, or get really complex with it. Just describe the image you want it to dream up with as many details as you can think of. Add artists, styles, colors, adjectives and get creative..."),
          Text('Now you can add prompt weighting, so you can emphasize the strength of certain words between parentheses, and de-emphasize words between brackets. For example: "A (hyper realistic) painting of (magical:1.8) owl with the face of a cat, without [tail], in a [twisted:0.6] tree, by Thomas Kinkade"'),
          Text('After adding your prompts, click on a prompt line to edit all the parameters of it. There you can add negative prompts like "lowres, bad_anatomy, error_body, bad_fingers, missing_fingers, error_lighting, jpeg_artifacts, signature, watermark, username, blurry" or anything else you don\'t want'),
          Text('Then you can override all the parameters for each individual prompt, playing with variations of sizes, steps, guidance scale, init & mask image, seeds, etc.  In the prompts list, you can press the ... options button to duplicate, delete and move prompts in the batch queue.  When ready, Run Diffusion on Prompts...')
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😀  Very nice... ", on_click=close_help_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = prompt_help_dlg
      prompt_help_dlg.open = True
      page.update()
  def paste_prompts(e):
      def save_prompts_list(e):
        plist = enter_text.value.strip()
        prompts_list = plist.split('\n')
        for pr in prompts_list:
          if bool(pr.strip()):
            add_to_prompts(pr.strip())
        close_dlg(e)
      def close_dlg(e):
          dlg_paste.open = False
          page.update()
      enter_text = TextField(label="Enter Prompts List with multiple lines", expand=True, multiline=True)
      dlg_paste = AlertDialog(modal=False, title=Text("📝  Paste or Write Prompts List from Simple Text"), content=Container(Column([enter_text], alignment=MainAxisAlignment.START, tight=True, width=page.width - 180, height=page.height - 100, scroll="none"), width=page.width - 180, height=page.height - 100), actions=[TextButton("Cancel", on_click=close_dlg), ElevatedButton(content=Text(value=emojize(":floppy_disk:") + "  Save to Prompts List ", size=19, weight=FontWeight.BOLD), on_click=save_prompts_list)], actions_alignment=MainAxisAlignment.END)
      page.dialog = dlg_paste
      dlg_paste.open = True
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
      open_dream = e.control.data
      add_to_prompts(open_dream.prompt, open_dream.arg)
      '''idx = prompts.index(e.control.data)
      new_dream = copy.copy(e.control.data)
      prompts.insert(idx, new_dream)
      diffs = arg_diffs(e.control.data.arg, args)
      subtitle = None
      if bool(diffs): subtitle = Text("    " + diffs)
      prompts_list.controls.insert(idx, ListTile(title=Text(new_dream.prompt, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, data=new_dream, subtitle=subtitle, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[
              PopupMenuItem(icon=icons.EDIT, text="Edit Prompt", on_click=edit_prompt, data=new_dream),
              PopupMenuItem(icon=icons.DELETE, text="Delete Prompt", on_click=delete_prompt, data=new_dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Prompt", on_click=duplicate_prompt, data=new_dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Multiple", on_click=duplicate_multiple, data=new_dream),
              PopupMenuItem(icon=icons.ARROW_UPWARD, text="Move Up", on_click=move_up, data=new_dream),
              PopupMenuItem(icon=icons.ARROW_DOWNWARD, text="Move Down", on_click=move_down, data=new_dream),
          ],
      )))
      prompts_list.update()
      status['changed_prompts'] = True'''
  def duplicate_multiple(e):
      open_dream = e.control.data
      num_times = 2
      def close_dlg(e):
          duplicate_modal.open = False
          page.update()
      def save_dlg(e):
          for i in range(num_times):
            add_to_prompts(open_dream.prompt, open_dream.arg)
          duplicate_modal.open = False
          page.update()
      def change_num(e):
          nonlocal num_times
          num_times = int(e.control.value)
      duplicate_modal = AlertDialog(modal=False, title=Text("🌀  Duplicate Prompt Multiple Times"), content=Container(Column([
            Container(content=None, height=7),
            NumberPicker(label="Number of Copies: ", min=1, max=99, value=num_times, on_change=change_num),
          ], alignment=MainAxisAlignment.START, tight=True, scroll=ScrollMode.AUTO)), actions=[TextButton("Cancel", on_click=close_dlg), ElevatedButton(content=Text(value=emojize(":bowling:") + "  Duplicate Prompt ", size=19, weight=FontWeight.BOLD), on_click=save_dlg)], actions_alignment=MainAxisAlignment.END)
      e.page.dialog = duplicate_modal
      duplicate_modal.open = True
      e.page.update()
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
      positive_prompt = prompt_text.value
      negative_prompt = negative_prompt_text.value
      if '_' in positive_prompt:
        positive_prompt = nsp_parse(positive_prompt)
      if bool(negative_prompt):
        if '_' in negative_prompt:
          negative_prompt = nsp_parse(negative_prompt)
        add_to_prompts(positive_prompt, {'negative_prompt': negative_prompt})
      else:
        add_to_prompts(positive_prompt)
  def add_to_prompts(p, arg=None):
      global prompts
      dream = Dream(p)
      if arg is not None:
        if 'prompt' in arg: del arg['prompt']
        arg = merge_dict(args, arg)
        dream.arg = arg
      prompts.append(dream)
      prompts_list.controls.append(ListTile(title=Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, data=dream, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[
              PopupMenuItem(icon=icons.EDIT, text="Edit Prompt", on_click=edit_prompt, data=dream),
              PopupMenuItem(icon=icons.DELETE, text="Delete Prompt", on_click=delete_prompt, data=dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE, text="Duplicate Prompt", on_click=duplicate_prompt, data=dream),
              PopupMenuItem(icon=icons.CONTROL_POINT_DUPLICATE_SHARP, text="Duplicate Multiple", on_click=duplicate_multiple, data=dream),
              PopupMenuItem(icon=icons.ARROW_UPWARD, text="Move Up", on_click=move_up, data=dream),
              PopupMenuItem(icon=icons.ARROW_DOWNWARD, text="Move Down", on_click=move_down, data=dream),
          ],
      )))
      #prompts_list.controls.append(Text("Prompt 1 added to the list of prompts"))
      prompts_list.update()
      if prompts_buttons.visible==False:
          prompts_buttons.visible=True
          prompts_buttons.update()
          if current_tab == 3:
            show_run_diffusion_fab(True)
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
            a = d.arg.copy()
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
            if 'init_image' in a:
              if not bool(a['init_image']):
                del a['init_image']
                del a['init_image_strength']
                del a['invert_mask']
              elif bool(a['mask_image']):
                del a['alpha_mask']
            if 'mask_image' in a:
              if not bool(a['mask_image']):
                del a['mask_image']
            if 'use_clip_guided_model' in a:
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
            if 'use_conceptualizer' in a:
              if not bool(a['use_conceptualizer']):
                del a['use_conceptualizer']
            prompts_prefs.append(a)
            #j = json.dumps(a)
          prefs['prompt_list'] = prompts_prefs
  page.save_prompts = save_prompts
  def load_prompts():
      saved_prompts = prefs['prompt_list']
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
            #prompts_list.controls.append(ListTile(title=Text(dream.prompt, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, data=dream, on_click=edit_prompt, trailing=PopupMenuButton(icon=icons.MORE_VERT,
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
      global prompts
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
  def clear_negative_prompt(e):
      negative_prompt_text.value = ""
      negative_prompt_text.update()
  def clear_list(e):
      global prompts
      if prefs['enable_sounds']: page.snd_delete.play()
      prompts_list.controls = []
      prompts_list.update()
      prompts = []
      prefs['prompt_list'] = []
      prompts_buttons.visible=False
      prompts_buttons.update()
      show_run_diffusion_fab(False)
      e.page.save_prompts()
      save_settings_file(e.page)
      #status['changed_prompts'] = True
  def on_keyboard (e: KeyboardEvent):
      if e.key == "Escape":
        if current_tab == 3:
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
      page.show_run_diffusion_fab(False)
      if status['changed_prompts']:
        page.save_prompts()
        save_settings_file(page)
        status['changed_prompts'] = False
      page.update()
      start_diffusion(page)
  has_changed = False
  prompts_list = Column([],spacing=1)
  prompt_text = TextField(label="Prompt Text", suffix=IconButton(icons.CLEAR, on_click=clear_prompt), autofocus=True, on_submit=add_prompt, col={'lg':9})
  negative_prompt_text = TextField(label="Segmented Weights 1 | -0.7 | 1.2" if prefs['use_composable'] and status['installed_composable'] else "Negative Prompt Text", suffix=IconButton(icons.CLEAR, on_click=clear_negative_prompt), col={'lg':3})
  add_prompt_button = ElevatedButton(content=Text(value="➕  Add" + (" Prompt" if page.width > 720 else ""), size=17, weight=FontWeight.BOLD), on_click=add_prompt)
  prompt_help_button = IconButton(icons.HELP_OUTLINE, tooltip="Help with Prompt Creation", on_click=prompt_help)
  paste_prompts_button = IconButton(icons.CONTENT_PASTE, tooltip="Create Prompts from Plain-Text List", on_click=paste_prompts)
  prompt_row = Row([ResponsiveRow([prompt_text, negative_prompt_text], expand=True), add_prompt_button])
  #diffuse_prompts_button = ElevatedButton(content=Text(value="▶️    Run Diffusion on Prompts ", size=20), on_click=run_diffusion)
  clear_prompts_button = ElevatedButton("❌   Clear Prompts List", on_click=clear_list)
  prompts_buttons = Row([clear_prompts_button], alignment=MainAxisAlignment.SPACE_BETWEEN)
  def show_run_diffusion_fab(show = True):
    if show:
      page.floating_action_button = FloatingActionButton(icon=icons.PLAY_ARROW, text="Run Diffusion on Prompts", on_click=run_diffusion)
      page.update()
    else:
      if page.floating_action_button is not None:
        page.floating_action_button = None
        page.update()
  page.show_run_diffusion_fab = show_run_diffusion_fab
  show_run_diffusion_fab(len(prompts_list.controls) > 0)
  #page.load_prompts()
  if len(prompts_list.controls) < 1:
    prompts_buttons.visible=False
  c = Column([Container(
      padding=padding.only(18, 14, 20, 10), content=Column([
        Row([Text("🗒️   List of Prompts to Diffuse", style=TextThemeStyle.TITLE_LARGE), Row([prompt_help_button, paste_prompts_button])], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Divider(thickness=1, height=4),
        #add_prompt_button,
        prompt_row,
        prompts_list,
        prompts_buttons,
      ],
  ))], scroll=ScrollMode.AUTO)
  return c

def buildImages(page):
    auto_scroll = True
    def auto_scrolling(auto):
      page.imageColumn.auto_scroll = auto
      page.imageColumn.update()
      c.update()
    page.auto_scrolling = auto_scrolling
    page.imageColumn = Column([Text("▶️   Get ready to make your images, run from Prompts List", style=TextThemeStyle.TITLE_LARGE), Divider(thickness=1, height=4)], scroll=ScrollMode.AUTO, auto_scroll=True)
    c = Container(padding=padding.only(18, 12, 0, 0), content=page.imageColumn)
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
            Tab(text="Prompt Writer", content=page.writer, icon=icons.CLOUD_CIRCLE),
            Tab(text="Prompt Generator", content=page.generator, icon=icons.CLOUD),
            Tab(text="Prompt Remixer", content=page.remixer, icon=icons.CLOUD_SYNC_ROUNDED),
            Tab(text="Prompt Brainstormer", content=page.brainstormer, icon=icons.CLOUDY_SNOWING),
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
    def add_to_prompt_list(p):
      page.add_to_prompts(p)
      if prefs['enable_sounds']: page.snd_drop.play()
    def add_to_prompt_generator(p):
      page.prompt_generator_list.controls.append(ListTile(title=Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, on_click=lambda _: add_to_prompt_list(p)))
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
      if prefs['enable_sounds']: page.snd_drop.play()
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
    generator_list_buttons = Row([ElevatedButton(content=Text("➕  Add All Prompts to List", size=20), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment=MainAxisAlignment.SPACE_BETWEEN)
    if len(page.prompt_generator_list.controls) < 1:
      generator_list_buttons.visible = False
      #generator_list_buttons.update()
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("🧠  OpenAI Prompt Genenerator", style=TextThemeStyle.TITLE_LARGE),
        Text("Enter a phrase each prompt should start with and the amount of prompts to generate. 'Subject Details' is optional to influence the output. 'Phase as subject' makes it about phrase and subject detail. 'Request mode' is the way it asks for the visual description. Just experiment, AI will continue to surprise.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([TextField(label="Subject Phrase", expand=True, value=prefs['prompt_generator']['phrase'], on_change=lambda e: changed(e, 'phrase')), TextField(label="Subject Detail", expand=True, hint_text="Optional about detail", value=prefs['prompt_generator']['subject_detail'], on_change=lambda e: changed(e, 'subject_detail')), Checkbox(label="Phrase as Subject", value=prefs['prompt_generator']['phrase_as_subject'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e: changed(e, 'phrase_as_subject'))]),
        ResponsiveRow([
          Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_generator']['amount'], on_change=lambda e: changed(e, 'amount')),
              NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_generator']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
          Row([NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_generator']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
              Checkbox(label="Permutate Artists", value=prefs['prompt_generator']['permutate_artists'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e: changed(e, 'permutate_artists'))], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
        ]),
        ResponsiveRow([
          Row([Text("Request Mode:"), request_slider,], col={'lg':6}),
          Row([Text(" AI Temperature:"), Slider(label="{value}", min=0, max=1, divisions=10, expand=True, value=prefs['prompt_generator']['AI_temperature'], on_change=lambda e: changed(e, 'AI_temperature'))], col={'lg':6}),
        ]),
        ElevatedButton(content=Text("💭   Generate Prompts", size=20), on_click=click_prompt_generator),
        page.prompt_generator_list,
        generator_list_buttons,
      ],
    ))], scroll=ScrollMode.AUTO)
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
    def add_to_prompt_list(p):
      page.add_to_prompts(p)
      if prefs['enable_sounds']: page.snd_drop.play()
    def add_to_prompt_remixer(p):
      page.prompt_remixer_list.controls.append(ListTile(title=Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, on_click=lambda _: add_to_prompt_list(p)))
      page.prompt_remixer_list.update()
      remixer_list_buttons.visible = True
      remixer_list_buttons.update()
    page.add_to_prompt_remixer = add_to_prompt_remixer
    def add_to_list(e):
      if prefs['enable_sounds']: page.snd_drop.play()
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
    remixer_list_buttons = Row([ElevatedButton(content=Text("Add All Prompts to List", size=20), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment=MainAxisAlignment.SPACE_BETWEEN)
    if len(page.prompt_remixer_list.controls) < 1:
      remixer_list_buttons.visible = False
    
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🔄  Prompt Remixer - GPT-3 AI Helper", style=TextThemeStyle.TITLE_LARGE), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page))], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Enter a complete prompt you've written that is well worded and descriptive, and get variations of it with our AI friend. Experiment.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([TextField(label="Seed Prompt", expand=True, value=prefs['prompt_remixer']['seed_prompt'], on_change=lambda e: changed(e, 'seed_prompt')), TextField(label="Optional About Detail", expand=True, hint_text="Optional about detail", value=prefs['prompt_remixer']['optional_about_influencer'], on_change=lambda e: changed(e, 'optional_about_influencer'))]),
        ResponsiveRow([
          Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_remixer']['amount'], on_change=lambda e: changed(e, 'amount')),
              NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_remixer']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
          Row([NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_remixer']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
              Checkbox(label="Permutate Artists", value=prefs['prompt_remixer']['permutate_artists'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e: changed(e, 'permutate_artists'))], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
        ]),
        ResponsiveRow([
          Row([Text("Request Mode:"), request_slider,], col={'lg':6}),
          Row([Text(" AI Temperature:"), Slider(label="{value}", min=0, max=1, divisions=10, expand=True, value=prefs['prompt_remixer']['AI_temperature'], on_change=lambda e: changed(e, 'AI_temperature'))], col={'lg':6}),
        ]),
        ElevatedButton(content=Text("🍹   Remix Prompts", size=20), on_click=click_prompt_remixer),
        page.prompt_remixer_list,
        remixer_list_buttons,
      ],
    ))], scroll=ScrollMode.AUTO)
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
      elif prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Flan-T5 XXL":
        if bool(prefs['HuggingFace_api_key']):
          run_prompt_brainstormer(page)
        else: alert_msg(page, "You must provide your HuggingFace API Key in settings first before using this Request Mode...")
    page.prompt_brainstormer_list = Column([], spacing=0)
    def add_to_prompt_brainstormer(p):
      page.prompt_brainstormer_list.controls.append(Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE, selectable=True))
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
    add_to_prompts_button = ElevatedButton("➕  Add to Prompts", on_click=add_to_prompts)#, icon=icons.ADD_ROUNDED
    brainstormer_list_buttons = Row([
        new_prompt_text, add_to_prompts_button,
        ElevatedButton(content=Text("❌   Clear Brainstorms"), on_click=clear_prompts),
    ], alignment=MainAxisAlignment.END)
    
    if len(page.prompt_brainstormer_list.controls) < 1:
      brainstormer_list_buttons.visible = False
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🤔  Prompt Brainstormer - TextSynth GPT-J-6B, OpenAI GPT-3 & HuggingFace Bloom AI", style=TextThemeStyle.TITLE_LARGE), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page))], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Enter a complete prompt you've written that is well worded and descriptive, and get variations of it with our AI friends. Experiment, each has different personalities.", style="titleSmall"),
        Divider(thickness=1, height=5),
        Row([Dropdown(label="AI Engine", width=250, options=[dropdown.Option("TextSynth GPT-J"), dropdown.Option("OpenAI GPT-3"), dropdown.Option("HuggingFace Bloom 176B"), dropdown.Option("HuggingFace Flan-T5 XXL")], value=prefs['prompt_brainstormer']['AI_engine'], on_change=lambda e: changed(e, 'AI_engine')),
          Dropdown(label="Request Mode", width=250, options=[dropdown.Option("Brainstorm"), dropdown.Option("Write"), dropdown.Option("Rewrite"), dropdown.Option("Edit"), dropdown.Option("Story"), dropdown.Option("Description"), dropdown.Option("Picture"), dropdown.Option("Raw Request")], value=prefs['prompt_brainstormer']['request_mode'], on_change=lambda e: changed(e, 'request_mode')),
        ], alignment=MainAxisAlignment.START),
        Row([TextField(label="About Prompt", expand=True, value=prefs['prompt_brainstormer']['about_prompt'], on_change=lambda e: changed(e, 'about_prompt')),]),
        ElevatedButton(content=Text("⛈️    Brainstorm Prompt", size=20), on_click=lambda _: run_prompt_brainstormer(page)),
        page.prompt_brainstormer_list,
        brainstormer_list_buttons,
      ],
    ))], scroll=ScrollMode.AUTO)
    return c

def buildPromptWriter(page):
    def changed(e, pref=None):
      if pref is not None:
        prefs['prompt_writer'][pref] = e.control.value
      status['changed_prompt_writer'] = True
    page.prompt_writer_list = Column([], spacing=0)
    def add_to_prompt_list(p):
      page.add_to_prompts(p)
      if prefs['enable_sounds']: page.snd_drop.play()
    def add_to_prompt_writer(p):
      page.prompt_writer_list.controls.append(ListTile(title=Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, on_click=lambda _: add_to_prompt_list(p)))
      page.prompt_writer_list.update()
      writer_list_buttons.visible = True
      writer_list_buttons.update()
    page.add_to_prompt_writer = add_to_prompt_writer

    def add_to_list(e):
      if prefs['enable_sounds']: page.snd_drop.play()
      for p in page.prompt_writer_list.controls:
        page.add_to_prompts(p.title.value)
    def clear_prompts(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.prompt_writer_list.controls = []
      page.prompt_writer_list.update()
      writer_list_buttons.visible = False
      writer_list_buttons.update()
    writer_list_buttons = Row([ElevatedButton(content=Text("➕  Add All Prompts to List", size=20), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment=MainAxisAlignment.SPACE_BETWEEN)
    if len(page.prompt_writer_list.controls) < 1:
      writer_list_buttons.visible = False

    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("📜 Advanced Prompt Writer with Noodle Soup Prompt random variables ", style=TextThemeStyle.TITLE_LARGE), ElevatedButton(content=Text("🍜  NSP Instructions", size=18), on_click=lambda _: NSP_instructions(page)),], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Construct your Stable Diffusion Art descriptions easier, with all the extras you need to engineer perfect prompts faster. Note, you don't have to use any randoms if you rather do all custom.", style="titleSmall"),
        Divider(thickness=1, height=5),
        TextField(label="Arts Subjects", value=prefs['prompt_writer']['art_Subjects'], on_change=lambda e: changed(e, 'art_Subjects')),
        Row([TextField(label="by Artists", value=prefs['prompt_writer']['by_Artists'], on_change=lambda e: changed(e, 'by_Artists')),
             TextField(label="Art Styles", value=prefs['prompt_writer']['art_Styles'], on_change=lambda e: changed(e, 'art_Styles')),]),
        ResponsiveRow([
          Row([NumberPicker(label="Amount: ", min=1, max=20, value=prefs['prompt_writer']['amount'], on_change=lambda e: changed(e, 'amount')),
              NumberPicker(label="Random Artists: ", min=0, max=10, value=prefs['prompt_writer']['random_artists'], on_change=lambda e: changed(e, 'random_artists')),], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
          Row([NumberPicker(label="Random Styles: ", min=0, max=10, value=prefs['prompt_writer']['random_styles'], on_change=lambda e: changed(e, 'random_styles')),
              Checkbox(label="Permutate Artists", value=prefs['prompt_writer']['permutate_artists'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e: changed(e, 'permutate_artists'))], col={'lg':6}, alignment=MainAxisAlignment.SPACE_BETWEEN),
        ]),
        ElevatedButton(content=Text("✍️   Write Prompts", size=18), on_click=lambda _: run_prompt_writer(page)),
        page.prompt_writer_list,
        writer_list_buttons,
      ],
    ))], scroll=ScrollMode.AUTO)
    return c

def NSP_instructions(page):
    def open_url(e):
        if e.data.startswith('http'):
          page.launch_url(e.data)
        else:
          page.set_clipboard(e.data)
          page.snack_bar = SnackBar(content=Text(f"📋   NSP variable {e.data} copied to clipboard..."))
          page.snack_bar.open = True
          page.update()
    NSP_markdown = '''To use a term database, simply use any of the keys below in sentence. Copy to Clipboard with click. 

For example if you wanted beauty adjective, you would write `_adj-beauty_` in your prompt. 

## Terminology Keys (by [@WAS](https://rebrand.ly/easy-diffusion))

### Adjective Types
   - [\_adj-architecture\_](_adj-architecture_) - A list of architectural adjectives and styles
   - [\_adj-beauty\_](_adj-beauty_) - A list of beauty adjectives for people (maybe things?)
   - [\_adj-general\_](_adj-general_) - A list of general adjectives for people/things.
   - [\_adj-horror\_](_adj-horror_) - A list of horror adjectives
### Art Types
   - [\_artist\_](_artist_) - A comprehensive list of artists by [**MisterRuffian**](https://docs.google.com/spreadsheets/d/1_jgQ9SyvUaBNP1mHHEzZ6HhL_Es1KwBKQtnpnmWW82I/edit) (Discord _Misterruffian#2891_)
   - [\_color\_](_color_) - A comprehensive list of colors
   - [\_portrait-type\_](_portrait-type_) - A list of common portrait types/poses
   - [\_style\_](_style_) - A list of art styles and mediums
### Computer Graphics Types
   - [\_3d-terms\_](_3d-terms_) - A list of 3D graphics terminology
   - [\_color-palette\_](_color-palette_) - A list of computer and video game console color palettes
   - [\_hd\_](_hd_) - A list of high definition resolution terms
### Miscellaneous Types
   - [\_details\_](_details_) - A list of detail descriptors
   - [\_site\_](_site_) - A list of websites to query
   - [\_gen-modififer\_](_gen-modififer_) - A list of general modifiers adopted from [Weird Wonderful AI Art](https://weirdwonderfulai.art/)
   - [\_neg-weight\_](_neg-weight_) - A lsit of negative weight ideas
   - [\_punk\_](_punk_) - A list of punk modifier (eg. cyberpunk)
   - [ _pop-culture\_](_pop-culture_) - A list of popular culture movies, shows, etc
   - [\_pop-location\_](_pop-location_) - A list of popular tourist locations
   - [\_fantasy-setting\_](_fantasy-setting_) - A list of fantasy location settings
   - [\_fantasy-creature\_](_fantasy-creature_) - A list of fantasy creatures
   - [\_animals\_](_animals_) - A list of modern animals
### Noun Types
   - [\_noun-beauty\_](_noun-beauty_) - A list of beauty related nouns
   - [\_noun-emote\_](_noun-emote_) - A list of emotions and expressions
   - [\_noun-fantasy\_](_noun-fantasy_) - A list of fantasy nouns
   - [\_noun-general\_](_noun-general_) - A list of general nouns
   - [\_noun-horror\_](_noun-horror_) - A list of horror nouns
### People Types
   - [\_bodyshape\_](_bodyshape_) - A list of body shapes
   - [\_celeb\_](_celeb_) - A list of celebrities
   - [\_eyecolor\_](_eyecolor_) - A list of eye colors
   - [\_hair\_](_hair_) - A list of hair types
   - [\_nationality\_](_nationality_) - A list of nationalities
   - [\_occputation\_](_occputation_) A list of occupation types
   - [\_skin-color\_](_skin-color_) - A list of skin tones
   - [\_identity-young\_](_identity-young_) A list of young identifiers
   - [\_identity-adult\_](_identity-adult_) A list of adult identifiers
   - [\_identity\_](_identity_) A list of general identifiers
### Photography / Image / Film Types
   - [\_aspect-ratio\_](_aspect-ratio_) - A list of common aspect ratios
   - [\_cameras\_](_cameras_) - A list of camera models *(including manufactuerer)*
   - [\_camera-manu\_](_camera-manu_) - A list of camera manufacturers
   - [\_f-stop\_](_f-stop_) - A list of camera aperture f-stop
   - [\_focal-length\_](_focal-length_) - A list of focal length ranges
   - [\_photo-term\_](_photo-term_) - A list of photography terms relating to photos

So in Subject try something like: `A _color_ _noun-general_ that is _adj-beauty_ and _adj-general_ with a _noun-emote_ _noun-fantasy_`
'''
    def close_NSP_dlg(e):
      instruction_alert.open = False
      page.update()
    instruction_alert = AlertDialog(title=Text("🍜  Noodle Soup Prompt Variables Instructions"), content=Column([Markdown(NSP_markdown, extension_set="gitHubWeb", on_tap_link=open_url)], scroll=ScrollMode.AUTO), actions=[TextButton("🍲  Good Soup! ", on_click=close_NSP_dlg)], actions_alignment=MainAxisAlignment.END,)
    page.dialog = instruction_alert
    instruction_alert.open = True
    page.update()

def buildStableDiffusers(page):
    page.DanceDiffusion = buildDanceDiffusion(page)
    page.RePainter = buildRepainter(page)
    page.unCLIP = buildUnCLIP(page)
    page.unCLIPImageVariation = buildUnCLIPImageVariation(page)
    page.ImageVariation = buildImageVariation(page)
    page.CLIPstyler = buildCLIPstyler(page)
    page.MagicMix = buildMagicMix(page)
    page.PaintByExample = buildPaintByExample(page)
    page.MaterialDiffusion = buildMaterialDiffusion(page)
    page.MaskMaker = buildDreamMask(page)
    page.DreamFusion = buildDreamFusion(page)
    page.DreamBooth = buildDreamBooth(page)
    page.TexualInversion = buildTextualInversion(page)
    diffusersTabs = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(text="unCLIP", content=page.unCLIP, icon=icons.ATTACHMENT_SHARP),
            Tab(text="unCLIP Image Variation", content=page.unCLIPImageVariation, icon=icons.AIRLINE_STOPS),
            Tab(text="Image Variation", content=page.ImageVariation, icon=icons.FORMAT_COLOR_FILL),
            Tab(text="RePainter", content=page.RePainter, icon=icons.FORMAT_PAINT),
            Tab(text="MagicMix", content=page.MagicMix, icon=icons.BLENDER),
            Tab(text="Paint-by-Example", content=page.PaintByExample, icon=icons.FORMAT_SHAPES),
            Tab(text="CLIP-Styler", content=page.CLIPstyler, icon=icons.STYLE),
            Tab(text="Material Diffusion", content=page.MaterialDiffusion, icon=icons.TEXTURE),
            Tab(text="DreamBooth", content=page.DreamBooth, icon=icons.PHOTO),
            Tab(text="Texual-Inversion", content=page.TexualInversion, icon=icons.PHOTO_ALBUM),
            Tab(text="DreamFusion 3D", content=page.DreamFusion, icon=icons.THREED_ROTATION),
            Tab(text="HarmonAI Dance Diffusion", content=page.DanceDiffusion, icon=icons.QUEUE_MUSIC),
            #Tab(text="Dream Mask Maker", content=page.MaskMaker, icon=icons.GRADIENT),
        ],
        expand=1,
        #on_change=tab_on_change
    )
    return diffusersTabs

def buildExtras(page):
    page.ESRGAN_upscaler = buildESRGANupscaler(page)
    page.RetrievePrompts = buildRetrievePrompts(page)
    page.InitFolder = buildInitFolder(page)
    page.CachedModelManager = buildCachedModelManager(page)
    page.Image2Text = buildImage2Text(page)
    page.DallE2 = buildDallE2(page)
    page.Kandinsky = buildKandinsky(page)
    extrasTabs = Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            Tab(text="Real-ESRGAN Batch Upscaler", content=page.ESRGAN_upscaler, icon=icons.PHOTO_SIZE_SELECT_LARGE),
            Tab(text="Retrieve Prompt from Image", content=page.RetrievePrompts, icon=icons.PHOTO_LIBRARY_OUTLINED),
            Tab(text="Init Images from Folder", content=page.InitFolder, icon=icons.FOLDER_SPECIAL),
            Tab(text="Cache Manager", content=page.CachedModelManager, icon=icons.CACHED),
            Tab(text="Image2Text Interrogator", content=page.Image2Text, icon=icons.WRAP_TEXT),
            Tab(text="OpenAI Dall-E 2", content=page.DallE2, icon=icons.BLUR_CIRCULAR),
            Tab(text="Kandinsky 2", content=page.Kandinsky, icon=icons.AC_UNIT),
        ],
        expand=1,
        #on_change=tab_on_change
    )
    return extrasTabs

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
    def add_to_ESRGAN_output(o):
      ESRGAN_output.controls.append(o)
      ESRGAN_output.update()
      if clear_button.visible == False:
        clear_button.visible = True
        clear_button.update()
      #generator_list_buttons.visible = True
      #generator_list_buttons.update()
    page.add_to_ESRGAN_output = add_to_ESRGAN_output
    enlarge_scale_value = Text(f" {float(ESRGAN_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
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
    page.clear_ESRGAN_output = clear_output
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        fname = os.path.join(root_dir, e.file_name)
        image_path.value = fname
        image_path.update()
        ESRGAN_prefs['image_path'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def pick_path(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Image File to Enlarge")
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    def pick_destination(e):
        alert_msg(page, "Switch to Colab tab and press Files button on the Left & Find the Path you want to Save Images into, Right Click and Copy Path, then Paste here")
    page.overlay.append(file_picker)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=ESRGAN_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=ESRGAN_prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
    image_path = TextField(label="Image File or Folder Path", value=ESRGAN_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_path), expand=1)
    dst_image_path = TextField(label="Destination Image Path", value=ESRGAN_prefs['dst_image_path'], on_change=lambda e:changed(e,'dst_image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_destination), expand=1)
    filename_suffix = TextField(label="Optional Filename Suffix", hint_text="-big", value=ESRGAN_prefs['filename_suffix'], on_change=lambda e:changed(e,'filename_suffix'), width=260)
    download_locally = Checkbox(label="Download Images Locally", value=ESRGAN_prefs['download_locally'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'download_locally'))
    display_image = Checkbox(label="Display Upscaled Image", value=ESRGAN_prefs['display_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_image'))
    split_image_grid = Switch(label="Split Image Grid", value=ESRGAN_prefs['split_image_grid'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_split)
    rows = NumberPicker(label="Rows: ", min=1, max=8, value=ESRGAN_prefs['rows'], on_change=lambda e: changed(e, 'rows'))
    cols = NumberPicker(label="Columns: ", min=1, max=8, value=ESRGAN_prefs['cols'], on_change=lambda e: changed(e, 'cols'))
    split_container = Container(Row([rows, Container(content=None, width=25), cols]), animate_size=animation.Animation(800, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE, padding=padding.only(left=28), height=0)
    ESRGAN_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(ESRGAN_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("↕️   Real-ESRGAN AI Upscale Enlarging", style=TextThemeStyle.TITLE_LARGE),
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
        ElevatedButton(content=Text("🐘  Run AI Upscaling", size=20), on_click=lambda _: run_upscaling(page)),
        ESRGAN_output,
        clear_button,
      ],
    ))], scroll=ScrollMode.AUTO)
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
    def pick_image(e):
        alert_msg(page, "Switch to Colab tab and press Files button on the Left & Find the Path you want to Retrieve, Right Click and Copy Path, then Paste here")
    page.add_to_retrieve_output = add_to_retrieve_output
    image_path = TextField(label="Image File or Folder Path", value=retrieve_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_image))
    add_to_prompts = Checkbox(label="Add to Prompts", value=retrieve_prefs['add_to_prompts'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'add_to_prompts'))
    display_full_metadata = Checkbox(label="Display Full Metadata", value=retrieve_prefs['display_full_metadata'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_full_metadata'))
    display_image = Checkbox(label="Display Image", value=retrieve_prefs['display_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_image'))
    retrieve_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(retrieve_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("📰  Retrieve Dream Prompts from Image Metadata", style=TextThemeStyle.TITLE_LARGE),
        Text("Give it images made here and gives you all parameters used to recreate it. Either upload png file(s) or paste path to image or folder or config.json to revive your dreams.."),
        Divider(thickness=1, height=5),
        image_path,
        add_to_prompts,
        display_full_metadata,
        display_image,
        ElevatedButton(content=Text("😴  Retrieve Dream", size=20), on_click=lambda _: run_retrieve(page)),
        retrieve_output,
        clear_button,
      ],
    ))], scroll=ScrollMode.AUTO)
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
    def pick_init(e):
        alert_msg(page, "Switch to Colab tab and press Files button on the Left & Find the Path you want to use as Init Folder, Right Click and Copy Path, then Paste here")
    def toggle_strength(e):
      changed(e,'include_strength')
      strength_row.visible = e.control.value
      strength_row.update()
    page.add_to_initfolder_output = add_to_initfolder_output
    prompt_string = TextField(label="Prompt Text", value=initfolder_prefs['prompt_string'], on_change=lambda e:changed(e,'prompt_string'))
    init_folder = TextField(label="Init Image Folder Path", value=initfolder_prefs['init_folder'], on_change=lambda e:changed(e,'init_folder'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
    include_strength = Checkbox(label="Include Strength", value=initfolder_prefs['include_strength'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=toggle_strength)
    image_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=float(initfolder_prefs['image_strength']), expand=True)
    strength_row = Row([Text("Image Strength:"), image_strength])
    strength_row.visible = initfolder_prefs['include_strength']
    strength_container = Container(Row([Text("Init Image Strength: "), image_strength]))
    initfolder_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(initfolder_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("📂 Generate Prompts from Folder as Init Images", style=TextThemeStyle.TITLE_LARGE),
        Text("Provide a Folder with a collection of images that you want to automatically add to prompts list with init_image overides..."),
        Divider(thickness=1, height=4),
        init_folder,
        prompt_string,
        include_strength,
        strength_row,
        ElevatedButton(content=Text("➕  Add to Prompts", size=20), on_click=lambda _: run_initfolder(page)),
        initfolder_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

image2text_prefs = {
    'mode': 'best',
    'folder_path': '',
    'image_path': '',
    'max_size': 768,
    'save_csv': False,
    'images': [],
}

def buildImage2Text(page):
    global prefs, image2text_prefs
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          image2text_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          image2text_prefs[pref] = float(e.control.value)
        else:
          image2text_prefs[pref] = e.control.value
    def add_to_image2text_output(o):
      page.image2text_output.controls.append(o)
      page.image2text_output.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.image2text_output.controls = []
      page.image2text_output.update()
      save_dir = os.path.join(root_dir, 'image2text')
      if os.path.exists(save_dir):
        for f in os.listdir(save_dir):
            os.remove(os.path.join(save_dir, f))
        os.rmdir(save_dir)
      page.image2text_file_list.controls = []
      page.image2text_file_list.update()
      image2text_list_buttons.visible = False
      image2text_list_buttons.update()
    def i2t_help(e):
      def close_i2t_dlg(e):
        nonlocal i2t_help_dlg
        i2t_help_dlg.open = False
        page.update()
      i2t_help_dlg = AlertDialog(title=Text("💁   Help with Image2Text CLIP Interrogator"), content=Column([
          Text(""),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😪  Okay then... ", on_click=close_i2t_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = i2t_help_dlg
      i2t_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        save_dir = os.path.join(root_dir, 'image2text')
        if not os.path.exists(save_dir):
          os.mkdir(save_dir)
        image2text_prefs['folder_path'] = save_dir
        fname = os.path.join(root_dir, e.file_name)
        fpath = os.path.join(save_dir, e.file_name)
        original_img = PILImage.open(fname)
        width, height = original_img.size
        width, height = scale_dimensions(width, height, image2text_prefs['max_size'])
        original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
        original_img.save(fpath)
        shutil.move(fname, fpath)
        page.image2text_file_list.controls.append(ListTile(title=Text(fpath), dense=True))
        page.image2text_file_list.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def pick_path(e):
        file_picker.pick_files(allow_multiple=True, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Image File to Enlarge")
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def add_image(e):
        save_dir = os.path.join(root_dir, 'image2text')
        if not os.path.exists(save_dir):
          os.mkdir(save_dir)
        image2text_prefs['folder_path'] = save_dir
        if image_path.value.startswith('http'):
          import requests
          from io import BytesIO
          response = requests.get(image_path.value)
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          original_img = PILImage.open(BytesIO(response.content)).convert("RGB")
          width, height = original_img.size
          width, height = scale_dimensions(width, height, image2text_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          page.image2text_file_list.controls.append(ListTile(title=Text(fpath), dense=True))
          page.image2text_file_list.update()
        elif os.path.isfile(image_path.value):
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          original_img = PILImage.open(image_path.value)
          width, height = original_img.size
          width, height = scale_dimensions(width, height, image2text_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          #shutil.copy(image_path.value, fpath)
          page.image2text_file_list.controls.append(ListTile(title=Text(fpath), dense=True))
          page.image2text_file_list.update()
        elif os.path.isdir(image_path.value):
          for f in os.listdir(image_path.value):
            file_path = os.path.join(image_path.value, f)
            if os.path.isdir(file_path): continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
              fpath = os.path.join(save_dir, f)
              original_img = PILImage.open(file_path)
              width, height = original_img.size
              width, height = scale_dimensions(width, height, image2text_prefs['max_size'])
              original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
              original_img.save(fpath)
              #shutil.copy(file_path, fpath)
              page.image2text_file_list.controls.append(ListTile(title=Text(fpath), dense=True))
              page.image2text_file_list.update()
        else:
          if bool(image_path.value):
            alert_msg(page, "Couldn't find a valid File, Path or URL...")
          else:
            pick_path(e)
          return
        image_path.value = ""
        image_path.update()
    page.image2text_list = Column([], spacing=0)
    def add_to_prompt_list(p):
      page.add_to_prompts(p)
      if prefs['enable_sounds']: page.snd_drop.play()
    def add_to_image2text(p):
      page.image2text_list.controls.append(ListTile(title=Text(p, max_lines=3, style=TextThemeStyle.BODY_LARGE), dense=True, on_click=lambda _: add_to_prompt_list(p)))
      page.image2text_list.update()
      image2text_list_buttons.visible = True
      image2text_list_buttons.update()
    page.add_to_image2text = add_to_image2text
    def add_to_list(e):
      if prefs['enable_sounds']: page.snd_drop.play()
      for p in page.image2text_list.controls:
        page.add_to_prompts(p.title.value)
    def clear_prompts(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.image2text_list.controls = []
      page.image2text_list.update()
      prompts = []
      image2text_list_buttons.visible = False
      image2text_list_buttons.update()
    image2text_list_buttons = Row([ElevatedButton(content=Text("➕  Add All Prompts to List", size=20), on_click=add_to_list),
        ElevatedButton(content=Text("❌   Clear Prompts"), on_click=clear_prompts),
    ], alignment=MainAxisAlignment.SPACE_BETWEEN)
    if len(page.image2text_list.controls) < 1:
      image2text_list_buttons.visible = False

    mode = Dropdown(label="Interrogation Mode", width=250, options=[dropdown.Option("best"), dropdown.Option("classic"), dropdown.Option("fast")], value=image2text_prefs['mode'], on_change=lambda e: changed(e, 'mode'))
    max_size = Slider(min=256, max=1024, divisions=12, label="{value}px", value=float(image2text_prefs['max_size']), expand=True, on_change=lambda e:changed(e,'max_size', ptype='int'))
    save_csv = Checkbox(label="Save CSV file of Prompts", tooltip="", value=image2text_prefs['save_csv'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'save_csv'))
    max_row = Row([Text("Max Resolution Size: "), max_size])
    image_path = TextField(label="Image File or Folder Path or URL to Train", value=image2text_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_path), expand=1)
    add_image_button = ElevatedButton(content=Text("Add File or Folder"), on_click=add_image)
    page.image2text_file_list = Column([], tight=True, spacing=0)
    page.image2text_output = Column([])
    #clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    #clear_button.visible = len(page.image2text_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("😶‍🌫️  Image2Text CLIP-Interrogator", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with Image2Text Interrogator", on_click=i2t_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Create prompts by describing input images..."),
        Divider(thickness=1, height=4),
        mode,
        max_row,
        Row([image_path, add_image_button]),
        page.image2text_file_list,
        page.image2text_list,
        image2text_list_buttons,
        ElevatedButton(content=Text("👨‍🎨️  Get Prompts from Images", size=20), on_click=lambda _: run_image2text(page)),
        page.image2text_output,
      ],
    ))], scroll=ScrollMode.AUTO)
    return c

dance_prefs = {
    'dance_model': 'maestro-150k',
    'installed_model': None,
    'inference_steps': 50,
    'batch_size': 1,
    'seed': 0,
    'audio_length_in_s': 4.5,
    'community_model': 'LCD Soundsystem',
}
community_models = [
    {'name': 'LCD Soundsystem', 'download': 'https://drive.google.com/uc?id=1WX8nL4_x49h0OJE5iGrjXJnIJ0yvsTxI', 'ckpt':'lcd-soundsystem-200k.ckpt'},
    {'name': 'Vague phrases', 'download': 'https://drive.google.com/uc?id=1nUn2qydqU7hlDUT-Skq_Ionte_8-Vdjr', 'ckpt': 'SingingInFepoch=1028-step=195500-pruned.ckpt'}, 
    {'name': 'Gesaffelstein', 'download': 'https://drive.google.com/uc?id=1-BuDzz4ajX-ufVByEX_fCkOtB00DVygB', 'ckpt':'Gesaffelstein_epoch=2537-step=445000.ckpt'},
    {'name': 'Smash Mouth Vocals', 'download': 'https://drive.google.com/uc?id=1h3fkJnByw3mKpXUiNPWKoYtzmpeg1QEt', 'ckpt':'epoch=773-step=191500.ckpt'},
    {'name': 'Daft Punk', 'download': 'https://drive.google.com/uc?id=1CZjWIcL528zbZa6GrS_triob0hUy6KEs', 'ckpt':'daft-punk-241.5k.ckpt'},
]
dance_pipe = None
def buildDanceDiffusion(page):
    global dance_pipe, dance_prefs
    def changed(e, pref=None, isInt=False):
        if pref is not None:
          if isInt:
            dance_prefs[pref] = int(e.control.value)
          else:
            dance_prefs[pref] = e.control.value
    def changed_model(e):
      dance_prefs['dance_model'] = e.control.value
      if e.control.value == 'Community':
        community_model.visible = True
        community_model.update()
      else:
        if community_model.visible:
          community_model.visible = False
          community_model.update()
    dance_model = Dropdown(label="Dance Model", width=250, options=[dropdown.Option("maestro-150k"), dropdown.Option("glitch-440k"), dropdown.Option("jmann-small-190k"), dropdown.Option("jmann-large-580k"), dropdown.Option("unlocked-250k"), dropdown.Option("honk-140k"), dropdown.Option("gwf-440k"), dropdown.Option("Community")], value=dance_prefs['dance_model'], on_change=changed_model)
    community_model = Dropdown(label="Community Model", width=250, options=[], value=dance_prefs['community_model'], on_change=lambda e: changed(e, 'community_model'))
    for c in community_models:
      community_model.options.append(dropdown.Option(c['name']))
    if not dance_prefs['dance_model'] == 'Community':
      community_model.visible = False
    inference_steps = Slider(min=10, max=200, divisions=190, label="{value}", value=float(dance_prefs['inference_steps']), expand=True)
    inference_row = Row([Text("Number of Inference Steps: "), inference_steps])
    batch_size = TextField(label="Batch Size", value=dance_prefs['batch_size'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'batch_size', isInt=True), width = 90)
    seed = TextField(label="Random Seed", value=dance_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', isInt=True), width = 110)
    audio_length_in_s = TextField(label="Audio Length in Seconds", value=dance_prefs['audio_length_in_s'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'audio_length_in_s'), width = 190)
    number_row = Row([batch_size, seed, audio_length_in_s])
    page.dance_output = Column([])
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("👯 Create experimental music or sounds with HarmonAI trained audio models", style=TextThemeStyle.TITLE_LARGE),
        Text("Tools to train a generative model on arbitrary audio samples..."),
        Divider(thickness=1, height=4),
        Row([dance_model, community_model]),
        inference_row,
        number_row,
        ElevatedButton(content=Text("🎵  Run Dance Diffusion", size=20), on_click=lambda _: run_dance_diffusion(page)),
        page.dance_output,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

dreamfusion_prefs = {
    'prompt_text': '', 
    'training_iters': 5000,
    'learning_rate': 0.001,
    'training_nerf_resolution': 64,
    'seed': 0,
    'lambda_entropy': 0.0001,
    'max_steps': 512,
    'checkpoint': 'latest',
    'workspace': 'trial',
}

def buildDreamFusion(page):
    global prefs, dreamfusion_prefs
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          dreamfusion_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          dreamfusion_prefs[pref] = float(e.control.value)
        else:
          dreamfusion_prefs[pref] = e.control.value
    def add_to_dreamfusion_output(o):
      page.dreamfusion_output.controls.append(o)
      page.dreamfusion_output.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.dreamfusion_output.controls = []
      page.dreamfusion_output.update()
      clear_button.visible = False
      clear_button.update()
    def df_help(e):
      def close_df_dlg(e):
        nonlocal df_help_dlg
        df_help_dlg.open = False
        page.update()
      df_help_dlg = AlertDialog(title=Text("💁   Help with DreamFusion"), content=Column([
          Text("It's difficult to explain exactly what all these parameters do, but keep it close to defaults, keep prompt simple, or experiment to see what's what, we don't know."),
          Text('It takes about 0.7s per training step, so the default 5000 training steps take around 1 hour to finish. A larger Training_iters usually leads to better results.'),
          Text('If CUDA OOM, try to decrease Max_steps and Training_nerf_resolution.'),
          Text('If the NeRF fails to learn anything (empty scene, only background), try to decrease Lambda_entropy which regularizes the learned opacity.')
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😊  So Exciting... ", on_click=close_df_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = df_help_dlg
      df_help_dlg.open = True
      page.update()
    prompt_text = TextField(label="Prompt Text", value=dreamfusion_prefs['prompt_text'], on_change=lambda e:changed(e,'prompt_text'))
    training_iters = TextField(label="Training Iterations", value=dreamfusion_prefs['training_iters'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'training_iters', ptype='int'), width = 160)
    learning_rate = TextField(label="Learning Rate", value=dreamfusion_prefs['learning_rate'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'learning_rate', ptype='float'), width = 160)
    training_nerf_resolution = TextField(label="Training NERF Res", value=dreamfusion_prefs['training_nerf_resolution'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'training_nerf_resolution', ptype='int'), width = 160)
    seed = TextField(label="Seed", value=dreamfusion_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', ptype='int'), width = 160)
    lambda_entropy = TextField(label="Lambda Entropy", value=dreamfusion_prefs['lambda_entropy'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'lambda_entropy', ptype='float'), width = 160)
    max_steps = TextField(label="Max Steps", value=dreamfusion_prefs['max_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'max_steps', ptype='int'), width = 160)
    workspace = TextField(label="Workspace Folder", value=dreamfusion_prefs['workspace'], on_change=lambda e:changed(e,'workspace'))
    page.dreamfusion_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.dreamfusion_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🗿  Create experimental DreamFusion 3D Model and Video", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with DreamFusion Settings", on_click=df_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Provide a prompt to render a model. Warning: May take over an hour to run the training..."),
        Divider(thickness=1, height=4),
        prompt_text,
        Row([training_iters,learning_rate, lambda_entropy]),
        Row([seed, training_nerf_resolution, max_steps]),
        Row([workspace]),
        ElevatedButton(content=Text("🔨  Run DreamFusion", size=20), on_click=lambda _: run_dreamfusion(page)),
        page.dreamfusion_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

repaint_prefs = {
    'original_image': '',
    'mask_image': '',
    'num_inference_steps': 500,
    'eta': 0.0,
    'jump_length': 10,
    'jump_n_sample': 10,
    'seed': 0,
    'file_name': '',
    'max_size': 1024,
    'invert_mask': False,
}
def buildRepainter(page):
    global repaint_prefs, prefs, pipe_repaint
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          repaint_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          repaint_prefs[pref] = float(e.control.value)
        else:
          repaint_prefs[pref] = e.control.value
    def add_to_repaint_output(o):
      page.repaint_output.controls.append(o)
      page.repaint_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.repaint_output.controls = []
      page.repaint_output.update()
      clear_button.visible = False
      clear_button.update()
    def repaint_help(e):
      def close_repaint_dlg(e):
        nonlocal repaint_help_dlg
        repaint_help_dlg.open = False
        page.update()
      repaint_help_dlg = AlertDialog(title=Text("💁   Help with Repainter"), content=Column([
          Text("It's difficult to explain exactly what all these parameters do, but keep it close to defaults, keep prompt simple, or experiment to see what's what, we don't know."),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😪  Okay then... ", on_click=close_repaint_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = repaint_help_dlg
      repaint_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      nonlocal pick_type
      if e.progress == 1:
        repaint_prefs['file_name'] = e.file_name.rpartition('.')[0]
        fname = os.path.join(root_dir, e.file_name)
        if pick_type == "original":
          original_image.value = fname
          original_image.update()
          repaint_prefs['original_image'] = fname
        elif pick_type == "mask":
          mask_image.value = fname
          mask_image.update()
          repaint_prefs['mask_image'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_original(e):
        nonlocal pick_type
        pick_type = "original"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Original Image File")
    def pick_mask(e):
        nonlocal pick_type
        pick_type = "mask"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Black & White Mask Image")
    def change_num_inference_steps(e):
        changed(e, 'num_inference_steps', ptype="int")
        num_inference_steps_value.value = f" {repaint_prefs['num_inference_steps']}"
        num_inference_steps_value.update()
        num_inference_row.update()
    def change_eta(e):
        changed(e, 'eta', ptype="float")
        eta_value.value = f" {repaint_prefs['eta']}"
        eta_value.update()
        eta_row.update()
    def change_max_size(e):
        changed(e, 'max_size', ptype="int")
        max_size_value.value = f" {repaint_prefs['max_size']}px"
        max_size_value.update()
        max_row.update()
    original_image = TextField(label="Original Image", value=repaint_prefs['original_image'], expand=1, on_change=lambda e:changed(e,'original_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_original))
    mask_image = TextField(label="Mask Image", value=repaint_prefs['mask_image'], expand=1, on_change=lambda e:changed(e,'mask_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask))
    invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=repaint_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'))
    jump_length = TextField(label="Jump Length", tooltip="The number of steps taken forward in time before going backward in time for a single jump", value=repaint_prefs['jump_length'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'jump_length', ptype='int'))
    jump_n_sample = TextField(label="Jump Number of Sample", tooltip="The number of times we will make forward time jump for a given chosen time sample.", value=repaint_prefs['jump_n_sample'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'jump_n_sample', ptype='int'))
    seed = TextField(label="Seed", value=str(repaint_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))
    #num_inference_steps = TextField(label="Inference Steps", value=str(repaint_prefs['num_inference_steps']), keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_inference_steps', ptype='int'))
    num_inference_steps = Slider(min=10, max=3000, divisions=2990, label="{value}", value=float(repaint_prefs['num_inference_steps']), tooltip="The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_num_inference_steps)
    num_inference_steps_value = Text(f" {repaint_prefs['num_inference_steps']}", weight=FontWeight.BOLD)
    num_inference_row = Row([Text("Number of Inference Steps: "), num_inference_steps_value, num_inference_steps])
    #eta = TextField(label="ETA", value=str(repaint_prefs['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'eta', ptype='float'))
    eta = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(repaint_prefs['eta']), tooltip="The weight of noise for added noise in a diffusion step. Its value is between 0.0 and 1.0 - 0.0 is DDIM and 1.0 is DDPM scheduler respectively.", expand=True, on_change=change_eta)
    eta_value = Text(f" {repaint_prefs['eta']}", weight=FontWeight.BOLD)
    eta_row = Row([Text("ETA:"), eta_value, Text("  DDIM"), eta, Text("DDPM")])
    max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=float(repaint_prefs['max_size']), expand=True, on_change=change_max_size)
    max_size_value = Text(f" {repaint_prefs['max_size']}px", weight=FontWeight.BOLD)
    max_row = Row([Text("Max Resolution Size: "), max_size_value, max_size])
    page.repaint_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.repaint_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("💅  Repaint masked areas of an image", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with Repainter Settings", on_click=repaint_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Fills in areas of picture with what it thinks it should be, without a prompt..."),
        Divider(thickness=1, height=4),
        Row([original_image, mask_image, invert_mask]),
        num_inference_row,
        eta_row,
        max_row,
        Row([jump_length, jump_n_sample, seed]),
        ElevatedButton(content=Text("🖌️  Run Repainter", size=20), on_click=lambda _: run_repainter(page)),
        page.repaint_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

image_variation_prefs = {
    'init_image': '',
    'guidance_scale': 7.5,
    'num_inference_steps': 50,
    'eta': 0.4,
    'seed': 0,
    'num_images': 1,
    'file_name': '',
    'max_size': 1024,
    'width': 960,
    'height': 512,
}
def buildImageVariation(page):
    global image_variation_prefs, prefs, pipe_image_variation
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          image_variation_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          image_variation_prefs[pref] = float(e.control.value)
        else:
          image_variation_prefs[pref] = e.control.value
    def add_to_image_variation_output(o):
      page.image_variation_output.controls.append(o)
      page.image_variation_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    page.add_to_image_variation_output = add_to_image_variation_output
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.image_variation_output.controls = []
      page.image_variation_output.update()
      clear_button.visible = False
      clear_button.update()
    def image_variation_help(e):
      def close_image_variation_dlg(e):
        nonlocal image_variation_help_dlg
        image_variation_help_dlg.open = False
        page.update()
      image_variation_help_dlg = AlertDialog(title=Text("🙅   Help with Image Variations"), content=Column([
          Text("Give it any of your favorite images and create variations of it.... Simple as that, no prompt needed."),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("🤗  Sounds Fun... ", on_click=close_image_variation_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = image_variation_help_dlg
      image_variation_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        image_variation_prefs['file_name'] = e.file_name.rpartition('.')[0]
        fname = os.path.join(root_dir, e.file_name)
        init_image.value = fname
        init_image.update()
        image_variation_prefs['init_image'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def pick_init(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick init Image File")
    def change_num_inference_steps(e):
      changed(e, 'num_inference_steps', ptype="int")
      num_inference_steps_value.value = f" {image_variation_prefs['num_inference_steps']}"
      num_inference_steps_value.update()
      num_inference_row.update()
    def change_max_size(e):
      changed(e, 'max_size', ptype="int")
      max_size_value.value = f" {image_variation_prefs['max_size']}px"
      max_size_value.update()
      max_row.update()
    def change_guidance(e):
      guidance_value.value = f" {e.control.value}"
      guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      guidance.update()
      changed(e, 'guidance_scale', ptype="float")
    guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=image_variation_prefs['guidance_scale'], on_change=change_guidance, expand=True)
    guidance_value = Text(f" {image_variation_prefs['guidance_scale']}", weight=FontWeight.BOLD)
    guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
    init_image = TextField(label="Initial Image", value=image_variation_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
    seed = TextField(label="Seed", width=90, value=str(image_variation_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))
    
    #num_inference_steps = TextField(label="Inference Steps", value=str(image_variation_prefs['num_inference_steps']), keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_inference_steps', ptype='int'))
    num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(image_variation_prefs['num_inference_steps']), tooltip="The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_num_inference_steps)
    num_inference_steps_value = Text(f" {magic_mix_prefs['num_inference_steps']}", weight=FontWeight.BOLD)
    num_inference_row = Row([Text("Number of Inference Steps: "), num_inference_steps_value, num_inference_steps])
    #eta = TextField(label="ETA", value=str(image_variation_prefs['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'eta', ptype='float'))
    eta = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(image_variation_prefs['eta']), tooltip="The weight of noise for added noise in a diffusion step. Its value is between 0.0 and 1.0 - 0.0 is DDIM and 1.0 is DDPM scheduler respectively.", expand=True, on_change=lambda e:changed(e,'eta', ptype='float'))
    eta_row = Row([Text("DDIM ETA: "), eta])
    max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=int(image_variation_prefs['max_size']), expand=True, on_change=change_max_size)
    max_size_value = Text(f" {image_variation_prefs['max_size']}px", weight=FontWeight.BOLD)
    max_row = Row([Text("Max Resolution Size: "), max_size_value, max_size])
    page.image_variation_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.image_variation_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🪩  Image Variations of any Init Image", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with Image Variation Settings", on_click=image_variation_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Creates a new version of your picture, without a prompt..."),
        Divider(thickness=1, height=4),
        init_image,
        #Row([init_image, mask_image, invert_mask]),
        num_inference_row,
        guidance,
        eta_row,
        max_row,
        Row([NumberPicker(label="Number of Images: ", min=1, max=8, value=image_variation_prefs['num_images'], on_change=lambda e: changed(e, 'num_images')), seed]),
        ElevatedButton(content=Text("🖍️  Get Image Variation", size=20), on_click=lambda _: run_image_variation(page)),
        page.image_variation_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO, auto_scroll=True)
    return c

unCLIP_prefs = {
    'prompt': '',
    'batch_folder_name': '',
    'prior_guidance_scale': 4.0,
    'decoder_guidance_scale': 8.0,
    'prior_num_inference_steps': 25,
    'decoder_num_inference_steps': 25,
    'super_res_num_inference_steps': 7,
    'seed': 0,
    'num_images': 1,
    #'variance_type': 'learned_range',#fixed_small_log
    #'num_train_timesteps': 1000,
    #'prediction_type': 'epsilon',#sample
    #'clip_sample': True,
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": 4.0,
    "display_upscaled_image": True,
}
def buildUnCLIP(page):
    global unCLIP_prefs, prefs, pipe_unCLIP
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          unCLIP_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          unCLIP_prefs[pref] = float(e.control.value)
        else:
          unCLIP_prefs[pref] = e.control.value
    def add_to_unCLIP_output(o):
      page.unCLIP_output.controls.append(o)
      page.unCLIP_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    page.add_to_unCLIP_output = add_to_unCLIP_output
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.unCLIP_output.controls = []
      page.unCLIP_output.update()
      clear_button.visible = False
      clear_button.update()
    def unCLIP_help(e):
      def close_unCLIP_dlg(e):
        nonlocal unCLIP_help_dlg
        unCLIP_help_dlg.open = False
        page.update()
      unCLIP_help_dlg = AlertDialog(title=Text("🙅   Help with unCLIP Pipeline"), content=Column([
          Text("Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style. To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding. We show that explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity. Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation. Moreover, the joint embedding space of CLIP enables language-guided image manipulations in a zero-shot fashion. We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples."),
          Text("The scheduler is a modified DDPM that has some minor variations in how it calculates the learned range variance and dynamically re-calculates betas based off the timesteps it is skipping. The scheduler also uses a slightly different step ratio when computing timesteps to use for inference."),
          Markdown("The unCLIP model in diffusers comes from kakaobrain's karlo and the original codebase can be found [here](https://github.com/kakaobrain/karlo). Additionally, lucidrains has a DALL-E 2 recreation [here](https://github.com/lucidrains/DALLE2-pytorch)."),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😕  Tricky... ", on_click=close_unCLIP_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = unCLIP_help_dlg
      unCLIP_help_dlg.open = True
      page.update()
    
    def change_prior_guidance(e):
      prior_guidance_value.value = f" {e.control.value}"
      prior_guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      prior_guidance.update()
      changed(e, 'prior_guidance_scale', ptype="float")
    prior_guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=unCLIP_prefs['prior_guidance_scale'], on_change=change_prior_guidance, expand=True)
    prior_guidance_value = Text(f" {unCLIP_prefs['prior_guidance_scale']}", weight=FontWeight.BOLD)
    prior_guidance = Row([Text("Prior Guidance Scale: "), prior_guidance_value, prior_guidance_scale])

    def change_decoder_guidance(e):
      decoder_guidance_value.value = f" {e.control.value}"
      decoder_guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      decoder_guidance.update()
      changed(e, 'decoder_guidance_scale', ptype="float")
    decoder_guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=unCLIP_prefs['decoder_guidance_scale'], on_change=change_decoder_guidance, expand=True)
    decoder_guidance_value = Text(f" {unCLIP_prefs['decoder_guidance_scale']}", weight=FontWeight.BOLD)
    decoder_guidance = Row([Text("Decoder Guidance Scale: "), decoder_guidance_value, decoder_guidance_scale])
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        unCLIP_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    prompt = TextField(label="Prompt Text", value=unCLIP_prefs['prompt'], on_change=lambda e:changed(e,'prompt'))
    seed = TextField(label="Seed", width=90, value=str(unCLIP_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))
    def change_prior_num_inference(e):
      changed(e, 'prior_num_inference_steps', ptype="int")
      prior_num_inference_value.value = f" {unCLIP_prefs['prior_num_inference_steps']}"
      prior_num_inference_value.update()
      prior_num_inference_row.update()
    def change_decoder_num_inference(e):
      changed(e, 'decoder_num_inference_steps', ptype="int")
      decoder_num_inference_value.value = f" {unCLIP_prefs['decoder_num_inference_steps']}"
      decoder_num_inference_value.update()
      decoder_num_inference_row.update()
    def change_super_res_num_inference(e):
      changed(e, 'super_res_num_inference_steps', ptype="int")
      super_res_num_inference_value.value = f" {unCLIP_prefs['super_res_num_inference_steps']}"
      super_res_num_inference_value.update()
      super_res_num_inference_row.update()
    #prior_num_inference_steps = TextField(label="Inference Steps", value=str(unCLIP_prefs['prior_num_inference_steps']), keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'prior_num_inference_steps', ptype='int'))
    prior_num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(unCLIP_prefs['prior_num_inference_steps']), tooltip="The number of Prior denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_prior_num_inference)
    decoder_num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(unCLIP_prefs['decoder_num_inference_steps']), tooltip="The number of Decoder denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_decoder_num_inference)
    super_res_num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(unCLIP_prefs['super_res_num_inference_steps']), tooltip="The number of Super-Res denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_super_res_num_inference)
    prior_num_inference_value = Text(f" {unCLIP_prefs['prior_num_inference_steps']}", weight=FontWeight.BOLD)
    decoder_num_inference_value = Text(f" {unCLIP_prefs['decoder_num_inference_steps']}", weight=FontWeight.BOLD)
    super_res_num_inference_value = Text(f" {unCLIP_prefs['super_res_num_inference_steps']}", weight=FontWeight.BOLD)
    prior_num_inference_row = Row([Text("Number of Prior Inference Steps: "), prior_num_inference_value, prior_num_inference_steps])
    decoder_num_inference_row = Row([Text("Number of Decoder Inference Steps: "), decoder_num_inference_value, decoder_num_inference_steps])
    super_res_num_inference_row = Row([Text("Number of Super-Res Inference Steps: "), super_res_num_inference_value, super_res_num_inference_steps])
    batch_folder_name = TextField(label="Batch Folder Name", value=unCLIP_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    #eta = TextField(label="ETA", value=str(unCLIP_prefs['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'eta', ptype='float'))
    #eta = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(unCLIP_prefs['eta']), tooltip="The weight of noise for added noise in a diffusion step. Its value is between 0.0 and 1.0 - 0.0 is DDIM and 1.0 is DDPM scheduler respectively.", expand=True, on_change=lambda e:changed(e,'eta', ptype='float'))
    #eta_row = Row([Text("DDIM ETA: "), eta])
    #max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=int(unCLIP_prefs['max_size']), expand=True, on_change=lambda e:changed(e,'max_size', ptype='int'))
    #max_row = Row([Text("Max Resolution Size: "), max_size])
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=unCLIP_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(unCLIP_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=unCLIP_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=unCLIP_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_unCLIP = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_unCLIP.height = None if status['installed_ESRGAN'] else 0
    if not unCLIP_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    page.unCLIP_output = Column([], auto_scroll=True)
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.unCLIP_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🌐  unCLIP Text-to-Image Generator", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with unCLIP Settings", on_click=unCLIP_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Hierarchical Text-Conditional Image Generation with CLIP Latents.  Similar results to DALL-E 2..."),
        Divider(thickness=1, height=4),
        prompt,
        #Row([prompt, mask_image, invert_mask]),
        prior_num_inference_row, decoder_num_inference_row, super_res_num_inference_row,
        prior_guidance, decoder_guidance,
        #eta_row, max_row,
        Row([NumberPicker(label="Number of Images: ", min=1, max=20, value=unCLIP_prefs['num_images'], on_change=lambda e: changed(e, 'num_images')), seed, batch_folder_name]),
        page.ESRGAN_block_unCLIP,
        Row([ElevatedButton(content=Text("🖇️   Get unCLIP Generation", size=20), on_click=lambda _: run_unCLIP(page)), 
             ElevatedButton(content=Text(value="📜   Run from Prompts List", size=20), on_click=lambda _: run_unCLIP(page, from_list=True))]),
        
      ]
    )), page.unCLIP_output,
        clear_button,
    ], scroll=ScrollMode.AUTO, auto_scroll=True)
    return c

unCLIP_image_variation_prefs = {
    'init_image': '',
    'file_name': '',
    'batch_folder_name': '',
    'decoder_guidance_scale': 8.0,
    'decoder_num_inference_steps': 25,
    'super_res_num_inference_steps': 7,
    'seed': 0,
    'num_images': 1,
    #'variance_type': 'learned_range',#fixed_small_log
    #'num_train_timesteps': 1000,
    #'prediction_type': 'epsilon',#sample
    #'clip_sample': True,
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": 4.0,
    "display_upscaled_image": True,
}
def buildUnCLIPImageVariation(page):
    global unCLIP_image_variation_prefs, prefs, pipe_unCLIP_image_variation
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          unCLIP_image_variation_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          unCLIP_image_variation_prefs[pref] = float(e.control.value)
        else:
          unCLIP_image_variation_prefs[pref] = e.control.value
    def add_to_unCLIP_image_variation_output(o):
      page.unCLIP_image_variation_output.controls.append(o)
      page.unCLIP_image_variation_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    page.add_to_unCLIP_image_variation_output = add_to_unCLIP_image_variation_output
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.unCLIP_image_variation_output.controls = []
      page.unCLIP_image_variation_output.update()
      clear_button.visible = False
      clear_button.update()
    def unCLIP_image_variation_help(e):
      def close_unCLIP_image_variation_dlg(e):
        nonlocal unCLIP_image_variation_help_dlg
        unCLIP_image_variation_help_dlg.open = False
        page.update()
      unCLIP_image_variation_help_dlg = AlertDialog(title=Text("🙅   Help with unCLIP Image Variation Pipeline"), content=Column([
          Text("Contrastive models like CLIP have been shown to learn robust representations of images that capture both semantics and style. To leverage these representations for image generation, we propose a two-stage model: a prior that generates a CLIP image embedding given a text caption, and a decoder that generates an image conditioned on the image embedding. We show that explicitly generating image representations improves image diversity with minimal loss in photorealism and caption similarity. Our decoders conditioned on image representations can also produce variations of an image that preserve both its semantics and style, while varying the non-essential details absent from the image representation. Moreover, the joint embedding space of CLIP enables language-guided image manipulations in a zero-shot fashion. We use diffusion models for the decoder and experiment with both autoregressive and diffusion models for the prior, finding that the latter are computationally more efficient and produce higher-quality samples."),
          Text("The scheduler is a modified DDPM that has some minor variations in how it calculates the learned range variance and dynamically re-calculates betas based off the timesteps it is skipping. The scheduler also uses a slightly different step ratio when computing timesteps to use for inference."),
          Markdown("The unCLIP Image Variation model in diffusers comes from kakaobrain's karlo and the original codebase can be found [here](https://github.com/kakaobrain/karlo). Additionally, lucidrains has a DALL-E 2 recreation [here](https://github.com/lucidrains/DALLE2-pytorch)."),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("🐇  We'll see... ", on_click=close_unCLIP_image_variation_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = unCLIP_image_variation_help_dlg
      unCLIP_image_variation_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        unCLIP_image_variation_prefs['file_name'] = e.file_name.rpartition('.')[0]
        fname = os.path.join(root_dir, e.file_name)
        init_image.value = fname
        init_image.update()
        unCLIP_image_variation_prefs['init_image'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def pick_init(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Init Image File")
    init_image = TextField(label="Initial Image", value=unCLIP_image_variation_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))

    def change_decoder_guidance(e):
      decoder_guidance_value.value = f" {e.control.value}"
      decoder_guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      decoder_guidance.update()
      changed(e, 'decoder_guidance_scale', ptype="float")
    decoder_guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=unCLIP_image_variation_prefs['decoder_guidance_scale'], on_change=change_decoder_guidance, expand=True)
    decoder_guidance_value = Text(f" {unCLIP_image_variation_prefs['decoder_guidance_scale']}", weight=FontWeight.BOLD)
    decoder_guidance = Row([Text("Decoder Guidance Scale: "), decoder_guidance_value, decoder_guidance_scale])
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        unCLIP_image_variation_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    #prompt = TextField(label="Prompt Text", value=unCLIP_image_variation_prefs['prompt'], on_change=lambda e:changed(e,'prompt'))
    seed = TextField(label="Seed", width=90, value=str(unCLIP_image_variation_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))

    def change_decoder_num_inference(e):
      changed(e, 'decoder_num_inference_steps', ptype="int")
      decoder_num_inference_value.value = f" {unCLIP_image_variation_prefs['decoder_num_inference_steps']}"
      decoder_num_inference_value.update()
      decoder_num_inference_row.update()
    def change_super_res_num_inference(e):
      changed(e, 'super_res_num_inference_steps', ptype="int")
      super_res_num_inference_value.value = f" {unCLIP_image_variation_prefs['super_res_num_inference_steps']}"
      super_res_num_inference_value.update()
      super_res_num_inference_row.update()
    decoder_num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(unCLIP_image_variation_prefs['decoder_num_inference_steps']), tooltip="The number of Decoder denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_decoder_num_inference)
    super_res_num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(unCLIP_image_variation_prefs['super_res_num_inference_steps']), tooltip="The number of Super-Res denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_super_res_num_inference)
    decoder_num_inference_value = Text(f" {unCLIP_image_variation_prefs['decoder_num_inference_steps']}", weight=FontWeight.BOLD)
    super_res_num_inference_value = Text(f" {unCLIP_image_variation_prefs['super_res_num_inference_steps']}", weight=FontWeight.BOLD)
    decoder_num_inference_row = Row([Text("Number of Decoder Inference Steps: "), decoder_num_inference_value, decoder_num_inference_steps])
    super_res_num_inference_row = Row([Text("Number of Super-Res Inference Steps: "), super_res_num_inference_value, super_res_num_inference_steps])
    batch_folder_name = TextField(label="Batch Folder Name", value=unCLIP_image_variation_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    #eta = TextField(label="ETA", value=str(unCLIP_image_variation_prefs['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'eta', ptype='float'))
    #eta = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(unCLIP_image_variation_prefs['eta']), tooltip="The weight of noise for added noise in a diffusion step. Its value is between 0.0 and 1.0 - 0.0 is DDIM and 1.0 is DDPM scheduler respectively.", expand=True, on_change=lambda e:changed(e,'eta', ptype='float'))
    #eta_row = Row([Text("DDIM ETA: "), eta])
    #max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=int(unCLIP_image_variation_prefs['max_size']), expand=True, on_change=lambda e:changed(e,'max_size', ptype='int'))
    #max_row = Row([Text("Max Resolution Size: "), max_size])
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=unCLIP_image_variation_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(unCLIP_image_variation_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=unCLIP_image_variation_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=unCLIP_image_variation_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_unCLIP_image_variation = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_unCLIP_image_variation.height = None if status['installed_ESRGAN'] else 0
    if not unCLIP_image_variation_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    page.unCLIP_image_variation_output = Column([], auto_scroll=True)
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.unCLIP_image_variation_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🎆  unCLIP Image Variation Generator", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with unCLIP Image Variation Settings", on_click=unCLIP_image_variation_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Generate Variations from an input image using unCLIP"),
        Divider(thickness=1, height=4),
        init_image,
        #Row([prompt, mask_image, invert_mask]),
        decoder_num_inference_row, super_res_num_inference_row,
        decoder_guidance,
        #eta_row, max_row,
        Row([NumberPicker(label="Number of Images: ", min=1, max=20, value=unCLIP_image_variation_prefs['num_images'], on_change=lambda e: changed(e, 'num_images')), seed, batch_folder_name]),
        page.ESRGAN_block_unCLIP_image_variation,
        Row([ElevatedButton(content=Text("🦄   Get unCLIP Image Variation", size=20), on_click=lambda _: run_unCLIP_image_variation(page)), 
             ElevatedButton(content=Text(value="📜   Run from Prompts List", size=20), on_click=lambda _: run_unCLIP_image_variation(page, from_list=True))]),
        
      ]
    )), page.unCLIP_image_variation_output,
        clear_button,
    ], scroll=ScrollMode.AUTO, auto_scroll=True)
    return c

magic_mix_prefs = {
    'init_image': '',
    'prompt': '',
    'guidance_scale': 7.5,
    'num_inference_steps': 50,
    'mix_factor': 0.5,
    'kmin': 0.3,
    'kmax': 0.6,
    'seed': 0,
    'num_images': 1,
    'max_size': 1024,
    'scheduler_mode': 'DDIM',
    'scheduler_last': '',
    'batch_folder_name': '',
    'file_name': '',
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": 4.0,
    "display_upscaled_image": True,
}
def buildMagicMix(page):
    global magic_mix_prefs, prefs, pipe_magic_mix
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          magic_mix_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          magic_mix_prefs[pref] = float(e.control.value)
        else:
          magic_mix_prefs[pref] = e.control.value
    def add_to_magic_mix_output(o):
      page.magic_mix_output.controls.append(o)
      page.magic_mix_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    page.add_to_magic_mix_output = add_to_magic_mix_output
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.magic_mix_output.controls = []
      page.magic_mix_output.update()
      clear_button.visible = False
      clear_button.update()
    def magic_mix_help(e):
      def close_magic_mix_dlg(e):
        nonlocal magic_mix_help_dlg
        magic_mix_help_dlg.open = False
        page.update()
      magic_mix_help_dlg = AlertDialog(title=Text("🙅   Help with MagicMix"), content=Column([
          Text("Have you ever imagined what a corgi-alike coffee machine or a tiger-alike rabbit would look like? In this work, we attempt to answer these questions by exploring a new task called semantic mixing, aiming at blending two different semantics to create a new concept (e.g., corgi + coffee machine -- > corgi-alike coffee machine). Unlike style transfer, where an image is stylized according to the reference style without changing the image content, semantic blending mixes two different concepts in a semantic manner to synthesize a novel concept while preserving the spatial layout and geometry. To this end, we present MagicMix, a simple yet effective solution based on pre-trained text-conditioned diffusion models. Motivated by the progressive generation property of diffusion models where layout/shape emerges at early denoising steps while semantically meaningful details appear at later steps during the denoising process, our method first obtains a coarse layout (either by corrupting an image or denoising from a pure Gaussian noise given a text prompt), followed by injection of conditional prompt for semantic mixing. Our method does not require any spatial mask or re-training, yet is able to synthesize novel objects with high fidelity. To improve the mixing quality, we further devise two simple strategies to provide better control and flexibility over the synthesized content. With our method, we present our results over diverse downstream applications, including semantic style transfer, novel object synthesis, breed mixing, and concept removal, demonstrating the flexibility of our method."),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("🧙  Sounds like magic... ", on_click=close_magic_mix_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = magic_mix_help_dlg
      magic_mix_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        magic_mix_prefs['file_name'] = e.file_name.rpartition('.')[0]
        fname = os.path.join(root_dir, e.file_name)
        init_image.value = fname
        init_image.update()
        magic_mix_prefs['init_image'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def pick_init(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Init Image File")
    prompt = TextField(label="Prompt Text", value=magic_mix_prefs['prompt'], on_change=lambda e:changed(e,'prompt'))
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        magic_mix_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    def change_num_inference_steps(e):
      changed(e, 'num_inference_steps', ptype="int")
      num_inference_steps_value.value = f" {magic_mix_prefs['num_inference_steps']}"
      num_inference_steps_value.update()
      num_inference_row.update()
    def change_mix_factor(e):
      changed(e, 'mix_factor', ptype="float")
      mix_factor_value.value = f" {magic_mix_prefs['mix_factor']}"
      mix_factor_value.update()
      mix_factor_row.update()
    def change_kmin(e):
      changed(e, 'kmin', ptype="float")
      kmin_value.value = f" {magic_mix_prefs['kmin']}"
      kmin_value.update()
      kmin_row.update()
    def change_kmax(e):
      changed(e, 'kmax', ptype="float")
      kmax_value.value = f" {magic_mix_prefs['kmax']}"
      kmax_value.update()
      kmax_row.update()
    def change_max_size(e):
      changed(e, 'max_size', ptype="int")
      max_size_value.value = f" {magic_mix_prefs['max_size']}px"
      max_size_value.update()
      max_row.update()
    def change_guidance(e):
      guidance_value.value = f" {e.control.value}"
      guidance_value.update()
      #guidance.controls[1].value = f" {e.control.value}"
      guidance.update()
      changed(e, 'guidance_scale', ptype="float")
    guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=magic_mix_prefs['guidance_scale'], on_change=change_guidance, expand=True)
    guidance_value = Text(f" {magic_mix_prefs['guidance_scale']}", weight=FontWeight.BOLD)
    guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
    init_image = TextField(label="Initial Image", value=magic_mix_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init))
    seed = TextField(label="Seed", width=90, value=str(magic_mix_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))
    scheduler_mode = Dropdown(label="Scheduler/Sampler Mode", hint_text="They're very similar, with minor differences in the noise", width=200,
            options=[
                dropdown.Option("DDIM"),
                dropdown.Option("K-LMS"),
                dropdown.Option("PNDM"),
            ], value=magic_mix_prefs['scheduler_mode'], autofocus=False, on_change=lambda e:changed(e, 'scheduler_mode'),
        )
    #num_inference_steps = TextField(label="Inference Steps", value=str(magic_mix_prefs['num_inference_steps']), keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_inference_steps', ptype='int'))
    num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=int(magic_mix_prefs['num_inference_steps']), tooltip="The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_num_inference_steps)
    num_inference_steps_value = Text(f" {magic_mix_prefs['num_inference_steps']}", weight=FontWeight.BOLD)
    num_inference_row = Row([Text("Number of Inference Steps: "), num_inference_steps_value, num_inference_steps])
    #mix_factor = TextField(label="ETA", value=str(magic_mix_prefs['mix_factor']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'mix_factor', ptype='float'))
    mix_factor = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(magic_mix_prefs['mix_factor']), tooltip="Interpolation constant used in the layout generation phase. The greater the value of `mix_factor`, the greater the influence of the prompt on the layout generation process.", expand=True, on_change=change_mix_factor)
    mix_factor_value = Text(f" {magic_mix_prefs['mix_factor']}", weight=FontWeight.BOLD)
    mix_factor_row = Row([Text("Mix Factor: "), mix_factor_value, mix_factor])
    kmin = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(magic_mix_prefs['kmin']), tooltip="Determine the range for the layout and content generation process. A higher value of kmin results in more steps for content generation process.", expand=True, on_change=change_kmin)
    kmin_value = Text(f" {magic_mix_prefs['kmin']}", weight=FontWeight.BOLD)
    kmin_row = Row([Text("k-Min: "), kmin_value, kmin])
    kmax = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(magic_mix_prefs['kmax']), tooltip="Determine the range for the layout and content generation process. A higher value of kmax results in loss of more information about the layout of the original image", expand=True, on_change=change_kmax)
    kmax_value = Text(f" {magic_mix_prefs['kmax']}", weight=FontWeight.BOLD)
    kmax_row = Row([Text("k-Max: "), kmax_value, kmax])
    max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=int(magic_mix_prefs['max_size']), expand=True, on_change=change_max_size)
    max_size_value = Text(f" {magic_mix_prefs['max_size']}px", weight=FontWeight.BOLD)
    max_row = Row([Text("Max Resolution Size: "), max_size_value, max_size])
    batch_folder_name = TextField(label="Batch Folder Name", value=magic_mix_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=magic_mix_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(magic_mix_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=magic_mix_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=magic_mix_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_magic_mix = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_magic_mix.height = None if status['installed_ESRGAN'] else 0
    if not unCLIP_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0

    page.magic_mix_output = Column([], auto_scroll=True)
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.magic_mix_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🧚  MagicMix Init Image with Prompt", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with MagicMix Settings", on_click=magic_mix_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Diffusion Pipeline for semantic mixing of an image and a text prompt..."),
        Divider(thickness=1, height=4),
        init_image,
        prompt,
        scheduler_mode,
        num_inference_row,
        guidance,
        mix_factor_row,
        kmin_row, kmax_row,
        max_row,
        Row([NumberPicker(label="Number of Images: ", min=1, max=8, value=magic_mix_prefs['num_images'], on_change=lambda e: changed(e, 'num_images')), seed, batch_folder_name]),
        page.ESRGAN_block_magic_mix,
        Row([ElevatedButton(content=Text("🪄  Make MagicMix", size=20), on_click=lambda _: run_magic_mix(page)), 
             ElevatedButton(content=Text(value="📜   Run from Prompts List", size=20), on_click=lambda _: run_magic_mix(page, from_list=True))]),
        page.magic_mix_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO, auto_scroll=True)
    return c

paint_by_example_prefs = {
    'original_image': '',
    'mask_image': '',
    'example_image': '',
    'num_inference_steps': 50,
    'guidance_scale': 7.5,
    'eta': 0.0,
    'seed': 0,
    'max_size': 1024,
    'alpha_mask': False,
    'invert_mask': False,
    'num_images': 1,
    'batch_folder_name': '',
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": 4.0,
    "display_upscaled_image": True,
}
def buildPaintByExample(page):
    global paint_by_example_prefs, prefs, pipe_paint_by_example
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          paint_by_example_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          paint_by_example_prefs[pref] = float(e.control.value)
        else:
          paint_by_example_prefs[pref] = e.control.value
    def add_to_paint_by_example_output(o):
      page.paint_by_example_output.controls.append(o)
      page.paint_by_example_output.update()
      if not clear_button.visible:
        clear_button.visible = True
        clear_button.update()
    def clear_output(e):
      if prefs['enable_sounds']: page.snd_delete.play()
      page.paint_by_example_output.controls = []
      page.paint_by_example_output.update()
      clear_button.visible = False
      clear_button.update()
    def paint_by_example_help(e):
      def close_paint_by_example_dlg(e):
        nonlocal paint_by_example_help_dlg
        paint_by_example_help_dlg.open = False
        page.update()
      paint_by_example_help_dlg = AlertDialog(title=Text("💁   Help with Paint-by-Example"), content=Column([
          Text("Language-guided image editing has achieved great success recently. In this pipeline, we use exemplar-guided image editing for more precise control. We achieve this goal by leveraging self-supervised training to disentangle and re-organize the source image and the exemplar. However, the naive approach will cause obvious fusing artifacts. We carefully analyze it and propose an information bottleneck and strong augmentations to avoid the trivial solution of directly copying and pasting the exemplar image. Meanwhile, to ensure the controllability of the editing process, we design an arbitrary shape mask for the exemplar image and leverage the classifier-free guidance to increase the similarity to the exemplar image. The whole framework involves a single forward of the diffusion model without any iterative optimization. We demonstrate that our method achieves an impressive performance and enables controllable editing on in-the-wild images with high fidelity.  Credit goes to https://github.com/Fantasy-Studio/Paint-by-Example"),
        ], scroll=ScrollMode.AUTO), actions=[TextButton("😸  Sweetness... ", on_click=close_paint_by_example_dlg)], actions_alignment=MainAxisAlignment.END)
      page.dialog = paint_by_example_help_dlg
      paint_by_example_help_dlg.open = True
      page.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      nonlocal pick_type
      if e.progress == 1:
        paint_by_example_prefs['file_name'] = e.file_name.rpartition('.')[0]
        fname = os.path.join(root_dir, e.file_name)
        if pick_type == "original":
          original_image.value = fname
          original_image.update()
          paint_by_example_prefs['original_image'] = fname
        elif pick_type == "mask":
          mask_image.value = fname
          mask_image.update()
          paint_by_example_prefs['mask_image'] = fname
        elif pick_type == "example":
          example_image.value = fname
          example_image.update()
          paint_by_example_prefs['example_image'] = fname
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_original(e):
        nonlocal pick_type
        pick_type = "original"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Original Image File")
    def pick_mask(e):
        nonlocal pick_type
        pick_type = "mask"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Black & White Mask Image")
    def pick_example(e):
        nonlocal pick_type
        pick_type = "example"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Example Style Image")
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        paint_by_example_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    def change_num_inference_steps(e):
        changed(e, 'num_inference_steps', ptype="int")
        num_inference_steps_value.value = f" {paint_by_example_prefs['num_inference_steps']}"
        num_inference_steps_value.update()
        num_inference_row.update()
    def change_guidance(e):
        guidance_value.value = f" {e.control.value}"
        guidance_value.update()
        #guidance.controls[1].value = f" {e.control.value}"
        guidance.update()
        changed(e, 'guidance_scale', ptype="float")
    def change_eta(e):
        changed(e, 'eta', ptype="float")
        eta_value.value = f" {paint_by_example_prefs['eta']}"
        eta_value.update()
        eta_row.update()
    def change_max_size(e):
        changed(e, 'max_size', ptype="int")
        max_size_value.value = f" {paint_by_example_prefs['max_size']}px"
        max_size_value.update()
        max_row.update()
    original_image = TextField(label="Original Image", value=paint_by_example_prefs['original_image'], expand=1, on_change=lambda e:changed(e,'original_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_original))
    mask_image = TextField(label="Mask Image", value=paint_by_example_prefs['mask_image'], expand=1, on_change=lambda e:changed(e,'mask_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask))
    alpha_mask = Checkbox(label="Alpha Mask", value=paint_by_example_prefs['alpha_mask'], tooltip="Use Transparent Alpha Channel of Init as Mask", fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'alpha_mask'))
    invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=paint_by_example_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'))
    example_image = TextField(label="Example Style Image", value=paint_by_example_prefs['example_image'], on_change=lambda e:changed(e,'example_image'), height=60, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_example))
    seed = TextField(label="Seed", width=90, value=str(paint_by_example_prefs['seed']), keyboard_type=KeyboardType.NUMBER, tooltip="0 or -1 picks a Random seed", on_change=lambda e:changed(e,'seed', ptype='int'))
    #num_inference_steps = TextField(label="Inference Steps", value=str(paint_by_example_prefs['num_inference_steps']), keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_inference_steps', ptype='int'))
    num_inference_steps = Slider(min=1, max=100, divisions=99, label="{value}", value=float(paint_by_example_prefs['num_inference_steps']), tooltip="The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.", expand=True, on_change=change_num_inference_steps)
    num_inference_steps_value = Text(f" {paint_by_example_prefs['num_inference_steps']}", weight=FontWeight.BOLD)
    num_inference_row = Row([Text("Number of Inference Steps: "), num_inference_steps_value, num_inference_steps])
    guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=paint_by_example_prefs['guidance_scale'], on_change=change_guidance, expand=True)
    guidance_value = Text(f" {paint_by_example_prefs['guidance_scale']}", weight=FontWeight.BOLD)
    guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
    #eta = TextField(label="ETA", value=str(paint_by_example_prefs['eta']), keyboard_type=KeyboardType.NUMBER, hint_text="Amount of Noise", on_change=lambda e:changed(e,'eta', ptype='float'))
    eta = Slider(min=0.0, max=1.0, divisions=20, label="{value}", value=float(paint_by_example_prefs['eta']), tooltip="The weight of noise for added noise in a diffusion step. Its value is between 0.0 and 1.0 - 0.0 is DDIM and 1.0 is DDPM scheduler respectively.", expand=True, on_change=change_eta)
    eta_value = Text(f" {paint_by_example_prefs['eta']}", weight=FontWeight.BOLD)
    eta_row = Row([Text("ETA:"), eta_value, Text("  DDIM"), eta, Text("DDPM")])
    max_size = Slider(min=256, max=1280, divisions=64, label="{value}px", value=float(paint_by_example_prefs['max_size']), expand=True, on_change=change_max_size)
    max_size_value = Text(f" {paint_by_example_prefs['max_size']}px", weight=FontWeight.BOLD)
    max_row = Row([Text("Max Resolution Size: "), max_size_value, max_size])
    batch_folder_name = TextField(label="Batch Folder Name", value=paint_by_example_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=paint_by_example_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(paint_by_example_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=paint_by_example_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=paint_by_example_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_paint_by_example = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_paint_by_example.height = None if status['installed_ESRGAN'] else 0
    page.paint_by_example_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.paint_by_example_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("🦁  Paint-by-Example", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with Paint-by-Example Settings", on_click=paint_by_example_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Image-guided Inpainting using an Example Image to Transfer Subject to Masked area..."),
        Divider(thickness=1, height=4),
        ResponsiveRow([Row([original_image, alpha_mask], col={'lg':6}), Row([mask_image, invert_mask], col={'lg':6})]),
        example_image,
        num_inference_row,
        guidance,
        eta_row,
        max_row,
        Row([NumberPicker(label="Number of Images: ", min=1, max=8, value=paint_by_example_prefs['num_images'], on_change=lambda e: changed(e, 'num_images')), seed, batch_folder_name]),
        page.ESRGAN_block_paint_by_example,
        #Row([jump_length, jump_n_sample, seed]),
        ElevatedButton(content=Text("🐾  Run Paint-by-Example", size=20), on_click=lambda _: run_paint_by_example(page)),
        page.paint_by_example_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

materialdiffusion_prefs = {
    "material_prompt": '',
    "batch_folder_name": '',
    "file_prefix": "material-",
    "num_outputs": 1,
    "steps":50,
    "eta":0.4,
    "width": 512,
    "height":512,
    "guidance_scale":7.5,
    "seed":0,
    "init_image": '',
    "prompt_strength": 0.5,
    "mask_image": '',
    "invert_mask": False,
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": prefs['enlarge_scale'],
    #"face_enhance": prefs['face_enhance'],
    "display_upscaled_image": prefs['display_upscaled_image'],
}

def buildMaterialDiffusion(page):
    global prefs, materialdiffusion_prefs, status

    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          materialdiffusion_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          materialdiffusion_prefs[pref] = float(e.control.value)
        else:
          materialdiffusion_prefs[pref] = e.control.value
    def pick_files_result(e: FilePickerResultEvent):
        if e.files:
            img = e.files
            uf = []
            fname = img[0]
            print(", ".join(map(lambda f: f.name, e.files)))
            src_path = page.get_upload_url(fname.name, 600)
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

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    #selected_files = Text()

    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
            upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
        nonlocal pick_type
        if e.progress == 1:
            fname = os.path.join(root_dir, e.file_name)
            if pick_type == "init":
                init_image.value = fname
                init_image.update()
                materialdiffusion_prefs['init_image'] = fname
            elif pick_type == "mask":
                mask_image.value = fname
                mask_image.update()
                materialdiffusion_prefs['mask_image'] = fname
            page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_init(e):
        nonlocal pick_type
        pick_type = "init"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File")
    def pick_mask(e):
        nonlocal pick_type
        pick_type = "mask"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Black & White Mask Image")
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        materialdiffusion_prefs['apply_ESRGAN_upscale'] = e.control.value
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
        changed(e, 'width', ptype="int")
    def change_height(e):
        height_slider.controls[1].value = f" {int(e.control.value)}px"
        height_slider.update()
        changed(e, 'height', ptype="int")
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    def change_strength(e):
        strength_value.value = f" {int(e.control.value * 100)}"
        strength_value.update()
        guidance.update()
        changed(e, 'prompt_strength', ptype="float")

    material_prompt = TextField(label="Material Prompt", value=materialdiffusion_prefs['material_prompt'], on_change=lambda e:changed(e,'material_prompt'))
    batch_folder_name = TextField(label="Batch Folder Name", value=materialdiffusion_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    file_prefix = TextField(label="Filename Prefix", value=materialdiffusion_prefs['file_prefix'], on_change=lambda e:changed(e,'file_prefix'))
    #num_outputs = NumberPicker(label="Num of Outputs", min=1, max=4, step=4, value=materialdiffusion_prefs['num_outputs'], on_change=lambda e:changed(e,'num_outputs', ptype="int"))
    #num_outputs = TextField(label="num_outputs", value=materialdiffusion_prefs['num_outputs'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_outputs', ptype="int"))
    #n_iterations = TextField(label="Number of Iterations", value=materialdiffusion_prefs['n_iterations'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'n_iterations', ptype="int"))
    steps = TextField(label="Inference Steps", value=materialdiffusion_prefs['steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'steps', ptype="int"))
    eta = TextField(label="DDIM ETA", value=materialdiffusion_prefs['eta'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'eta', ptype="float"))
    seed = TextField(label="Seed", value=materialdiffusion_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'seed', ptype="int"))
    param_rows = ResponsiveRow([Column([batch_folder_name, file_prefix, NumberPicker(label="Output Images", min=1, max=4, step=3, value=materialdiffusion_prefs['num_outputs'], on_change=lambda e:changed(e,'num_outputs', ptype="int"))], col={'xs':12, 'md':6}), 
                      Column([steps, eta, seed], col={'xs':12, 'md':6})])
    guidance_scale = Slider(min=0, max=50, divisions=100, label="{value}", value=materialdiffusion_prefs['guidance_scale'], on_change=change_guidance, expand=True)
    guidance_value = Text(f" {materialdiffusion_prefs['guidance_scale']}", weight=FontWeight.BOLD)
    guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
    width = Slider(min=128, max=1024, divisions=14, label="{value}px", value=materialdiffusion_prefs['width'], on_change=change_width, expand=True)
    width_value = Text(f" {int(materialdiffusion_prefs['width'])}px", weight=FontWeight.BOLD)
    width_slider = Row([Text(f"Width: "), width_value, width])
    height = Slider(min=128, max=1024, divisions=14, label="{value}px", value=materialdiffusion_prefs['height'], on_change=change_height, expand=True)
    height_value = Text(f" {int(materialdiffusion_prefs['height'])}px", weight=FontWeight.BOLD)
    height_slider = Row([Text(f"Height: "), height_value, height])

    init_image = TextField(label="Init Image", value=materialdiffusion_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init), col={'xs':12, 'md':6})
    mask_image = TextField(label="Mask Image", value=materialdiffusion_prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask), col={'xs':10, 'md':5})
    invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=materialdiffusion_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'), col={'xs':2, 'md':1})
    image_pickers = Container(content=ResponsiveRow([init_image, mask_image, invert_mask]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    prompt_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=materialdiffusion_prefs['prompt_strength'], on_change=change_strength, expand=True)
    strength_value = Text(f" {int(materialdiffusion_prefs['prompt_strength'] * 100)}%", weight=FontWeight.BOLD)
    strength_slider = Row([Text("Prompt Strength: "), strength_value, prompt_strength])
    img_block = Container(Column([image_pickers, strength_slider, Divider(height=9, thickness=2)]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=materialdiffusion_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(materialdiffusion_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=materialdiffusion_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    #face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=materialdiffusion_prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=materialdiffusion_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_material = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_material.height = None if status['installed_ESRGAN'] else 0
    if not materialdiffusion_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    parameters_button = ElevatedButton(content=Text(value="💨   Run Material Diffusion", size=20), on_click=lambda _: run_materialdiffusion(page))

    parameters_row = Row([parameters_button], alignment=MainAxisAlignment.SPACE_BETWEEN)
    page.materialdiffusion_output = Column([])
    c = Column([Container(
        padding=padding.only(18, 14, 20, 10), content=Column([
            Text ("🧱  Replicate Material Diffusion", style=TextThemeStyle.TITLE_LARGE),
            Text ("Create Seamless Tiled Textures with your Prompt. Requires account at Replicate.com and your Key."),
            Divider(thickness=1, height=4),
            material_prompt,
            param_rows, guidance, width_slider, height_slider, #Divider(height=9, thickness=2), 
            img_block, page.ESRGAN_block_material,
            #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
            parameters_row,
            page.materialdiffusion_output
        ],
    ))], scroll=ScrollMode.AUTO)#batch_folder_name, batch_size, n_iterations, steps, eta, seed, 
    return c

dall_e_prefs = {
    'prompt': '',
    'size': '512x512',
    'num_images': 1,
    'init_image': '',
    'mask_image': '',
    'variation': False,
    "invert_mask": False,
    'file_prefix': 'dalle-',
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": prefs['enlarge_scale'],
    "face_enhance": prefs['face_enhance'],
    "display_upscaled_image": prefs['display_upscaled_image'],
    "batch_folder_name": '',
}

def buildDallE2(page):
    global dall_e_prefs
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          dall_e_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          dall_e_prefs[pref] = float(e.control.value)
        else:
          dall_e_prefs[pref] = e.control.value
    def pick_files_result(e: FilePickerResultEvent):
        if e.files:
            img = e.files
            dalle = []
            fname = img[0]
            print(", ".join(map(lambda f: f.name, e.files)))
            src_path = page.get_upload_url(fname.name, 600)
            dalle.append(FilePickerUploadFile(fname.name, upload_url=src_path))
            pick_files_dialog.upload(dalle)
            print(str(src_path))
            #src_path = ''.join(src_path)
            print(str(dalle[0]))
            dst_path = os.path.join(root_dir, fname.name)
            print(f'Copy {src_path} to {dst_path}')
            #shutil.copy(src_path, dst_path)
            # TODO: is init or mask?
            init_image.value = dst_path

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    #selected_files = Text()

    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
            upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
        nonlocal pick_type
        if e.progress == 1:
            fname = os.path.join(root_dir, e.file_name)
            if pick_type == "init":
                init_image.value = fname
                init_image.update()
                dall_e_prefs['init_image'] = fname
            elif pick_type == "mask":
                mask_image.value = fname
                mask_image.update()
                dall_e_prefs['mask_image'] = fname
            page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        dalle = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                dalle.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(dalle)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_init(e):
        nonlocal pick_type
        pick_type = "init"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File")
    def pick_mask(e):
        nonlocal pick_type
        pick_type = "mask"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Black & White Mask Image")
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        dall_e_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
        has_changed = True
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")

    prompt = TextField(label="Prompt Text", value=dall_e_prefs['prompt'], on_change=lambda e:changed(e,'prompt'))
    batch_folder_name = TextField(label="Batch Folder Name", value=dall_e_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    file_prefix = TextField(label="Filename Prefix", value=dall_e_prefs['file_prefix'], on_change=lambda e:changed(e,'file_prefix'))
    #num_images = NumberPicker(label="Num of Outputs", min=1, max=4, step=4, value=dall_e_prefs['num_images'], on_change=lambda e:changed(e,'num_images', ptype="int"))
    #num_images = TextField(label="num_images", value=dall_e_prefs['num_images'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_images', ptype="int"))
    #n_iterations = TextField(label="Number of Iterations", value=dall_e_prefs['n_iterations'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'n_iterations', ptype="int"))
    #steps = TextField(label="Inference Steps", value=dall_e_prefs['steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'steps', ptype="int"))
    #eta = TextField(label="DDIM ETA", value=dall_e_prefs['eta'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'eta', ptype="float"))
    #seed = TextField(label="Seed", value=dall_e_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'seed', ptype="int"))
    size = Dropdown(label="Image Size", width=180, options=[dropdown.Option("256x256"), dropdown.Option("512x512"), dropdown.Option("1024x1024")], value=dall_e_prefs['size'], on_change=lambda e:changed(e,'size'))
    param_rows = Row([Row([batch_folder_name, file_prefix, size, NumberPicker(label="Number of Images", min=1, max=10, step=1, value=dall_e_prefs['num_images'], on_change=lambda e:changed(e,'num_images', ptype="int"))])])
    
    #width = Slider(min=128, max=1024, divisions=6, label="{value}px", value=dall_e_prefs['width'], on_change=change_width, expand=True)
    #width_value = Text(f" {int(dall_e_prefs['width'])}px", weight=FontWeight.BOLD)
    #width_slider = Row([Text(f"Width: "), width_value, width])
    #height = Slider(min=128, max=1024, divisions=6, label="{value}px", value=dall_e_prefs['height'], on_change=change_height, expand=True)
    #height_value = Text(f" {int(dall_e_prefs['height'])}px", weight=FontWeight.BOLD)
    #height_slider = Row([Text(f"Height: "), height_value, height])
    init_image = TextField(label="Init Image", value=dall_e_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init, col={"*":1, "md":3}))
    mask_image = TextField(label="Mask Image", value=dall_e_prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask, col={"*":1, "md":3}))
    variation = Checkbox(label="Variation   ", tooltip="Creates Variation of Init Image. Disregards the Prompt and Mask.", value=dall_e_prefs['variation'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'variation'))
    invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=dall_e_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'))
    image_pickers = Container(content=ResponsiveRow([Row([init_image, variation], col={"md":6}), Row([mask_image, invert_mask], col={"md":6})], run_spacing=2), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    #prompt_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=dall_e_prefs['prompt_strength'], on_change=change_strength, expand=True)
    #strength_value = Text(f" {int(dall_e_prefs['prompt_strength'] * 100)}%", weight=FontWeight.BOLD) 
    #strength_slider = Row([Text("Prompt Strength: "), strength_value, prompt_strength])
    img_block = Container(Column([image_pickers, Divider(height=9, thickness=2)]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=dall_e_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(dall_e_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=dall_e_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=dall_e_prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=dall_e_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, face_enhance, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_dalle = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_dalle.height = None if status['installed_ESRGAN'] else 0
    if not dall_e_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    list_button = ElevatedButton(content=Text(value="📜   Run from Prompts List", size=20), on_click=lambda _: run_dall_e(page, from_list=True))
    parameters_button = ElevatedButton(content=Text(value="🖼️   Run Dall-E 2", size=20), on_click=lambda _: run_dall_e(page))

    parameters_row = Row([parameters_button, list_button], spacing=22)#, alignment=MainAxisAlignment.SPACE_BETWEEN)
    page.dall_e_output = Column([])
    c = Column([Container(
        padding=padding.only(18, 14, 20, 10), content=Column([
            Text ("👺  OpenAI Dall-E 2", style=TextThemeStyle.TITLE_LARGE),
            Text ("Generates Images using your OpenAI API Key. Note: Uses same credits as official website."),
            Divider(thickness=1, height=4),
            prompt,
            param_rows,
            img_block, page.ESRGAN_block_dalle,
            #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
            parameters_row,
            page.dall_e_output
        ],
    ))], scroll=ScrollMode.AUTO)
    return c

kandinsky_prefs = {
    "prompt": '',
    "batch_folder_name": '',
    "file_prefix": "kandinsky-",
    "num_images": 1,
    "steps":100,
    "ddim_eta":0.05,
    "width": 512,
    "height":512,
    "guidance_scale":8,
    "dynamic_threshold_v":99.5,
    "sampler": "ddim_sampler",
    "denoised_type": "dynamic_threshold",
    "init_image": '',
    "strength": 0.5,
    "mask_image": '',
    "invert_mask": False,
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": prefs['enlarge_scale'],
    "face_enhance": prefs['face_enhance'],
    "display_upscaled_image": prefs['display_upscaled_image'],
}

def buildKandinsky(page):
    global prefs, kandinsky_prefs, status

    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          kandinsky_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          kandinsky_prefs[pref] = float(e.control.value)
        else:
          kandinsky_prefs[pref] = e.control.value
    def pick_files_result(e: FilePickerResultEvent):
        if e.files:
            img = e.files
            uf = []
            fname = img[0]
            print(", ".join(map(lambda f: f.name, e.files)))
            src_path = page.get_upload_url(fname.name, 600)
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

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    #selected_files = Text()

    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
            upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
        nonlocal pick_type
        if e.progress == 1:
            fname = os.path.join(root_dir, e.file_name)
            if pick_type == "init":
                init_image.value = fname
                init_image.update()
                kandinsky_prefs['init_image'] = fname
            elif pick_type == "mask":
                mask_image.value = fname
                mask_image.update()
                kandinsky_prefs['mask_image'] = fname
            page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_init(e):
        nonlocal pick_type
        pick_type = "init"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File")
    def pick_mask(e):
        nonlocal pick_type
        pick_type = "mask"
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Black & White Mask Image")
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        kandinsky_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
    def change_guidance(e):
        guidance_value.value = f" {int(e.control.value)}"
        guidance_value.update()
        #guidance.controls[1].value = f" {e.control.value}"
        guidance.update()
        changed(e, 'guidance_scale', ptype="int")
    def change_width(e):
        width_slider.controls[1].value = f" {int(e.control.value)}px"
        width_slider.update()
        changed(e, 'width', ptype="int")
    def change_height(e):
        height_slider.controls[1].value = f" {int(e.control.value)}px"
        height_slider.update()
        changed(e, 'height', ptype="int")
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")
    def change_strength(e):
        strength_value.value = f" {e.control.value}"
        strength_value.update()
        guidance.update()
        changed(e, 'strength', ptype="float")

    prompt = TextField(label="Prompt Text", value=kandinsky_prefs['prompt'], on_change=lambda e:changed(e,'prompt'))
    batch_folder_name = TextField(label="Batch Folder Name", value=kandinsky_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    file_prefix = TextField(label="Filename Prefix", value=kandinsky_prefs['file_prefix'], on_change=lambda e:changed(e,'file_prefix'))
    #num_outputs = NumberPicker(label="Num of Outputs", min=1, max=4, step=4, value=kandinsky_prefs['num_outputs'], on_change=lambda e:changed(e,'num_outputs', ptype="int"))
    #num_outputs = TextField(label="num_outputs", value=kandinsky_prefs['num_outputs'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_outputs', ptype="int"))
    #n_iterations = TextField(label="Number of Iterations", value=kandinsky_prefs['n_iterations'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'n_iterations', ptype="int"))
    steps = TextField(label="Number of Steps", value=kandinsky_prefs['steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'steps', ptype="int"))
    ddim_eta = TextField(label="DDIM ETA", value=kandinsky_prefs['ddim_eta'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'ddim_eta', ptype="float"))
    dynamic_threshold_v = TextField(label="Dynamic Threshold", value=kandinsky_prefs['dynamic_threshold_v'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'dynamic_threshold_v', ptype="float"))
    param_rows = ResponsiveRow([Column([batch_folder_name, file_prefix, NumberPicker(label="Number of Images", min=1, max=9, step=1, value=kandinsky_prefs['num_images'], on_change=lambda e:changed(e,'num_images', ptype="int"))], col={'xs':12, 'md':6}), 
                      Column([steps, ddim_eta, dynamic_threshold_v], col={'xs':12, 'md':6})])
    sampler = Dropdown(label="Sampler", width=180, options=[dropdown.Option("ddim_sampler"), dropdown.Option("p_sampler")], value=kandinsky_prefs['sampler'], on_change=lambda e:changed(e,'sampler'), col={'xs':12, 'md':6})
    denoised_type = Dropdown(label="Denoised Type", width=180, options=[dropdown.Option("dynamic_threshold"), dropdown.Option("clip_denoised")], value=kandinsky_prefs['denoised_type'], on_change=lambda e:changed(e,'denoised_type'), col={'xs':12, 'md':6})
    dropdown_row = ResponsiveRow([sampler, denoised_type])
    guidance_scale = Slider(min=0, max=50, divisions=50, label="{value}", value=kandinsky_prefs['guidance_scale'], on_change=change_guidance, expand=True)
    guidance_value = Text(f" {kandinsky_prefs['guidance_scale']}", weight=FontWeight.BOLD)
    guidance = Row([Text("Guidance Scale: "), guidance_value, guidance_scale])
    width = Slider(min=128, max=1024, divisions=14, label="{value}px", value=kandinsky_prefs['width'], on_change=change_width, expand=True)
    width_value = Text(f" {int(kandinsky_prefs['width'])}px", weight=FontWeight.BOLD)
    width_slider = Row([Text(f"Width: "), width_value, width])
    height = Slider(min=128, max=1024, divisions=14, label="{value}px", value=kandinsky_prefs['height'], on_change=change_height, expand=True)
    height_value = Text(f" {int(kandinsky_prefs['height'])}px", weight=FontWeight.BOLD)
    height_slider = Row([Text(f"Height: "), height_value, height])

    init_image = TextField(label="Init Image", value=kandinsky_prefs['init_image'], on_change=lambda e:changed(e,'init_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_init), col={'xs':12, 'md':6})
    mask_image = TextField(label="Mask Image", value=kandinsky_prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask), col={'xs':10, 'md':5})
    invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=kandinsky_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'), col={'xs':2, 'md':1})
    image_pickers = Container(content=ResponsiveRow([init_image, mask_image, invert_mask]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}", value=kandinsky_prefs['strength'], on_change=change_strength, expand=True)
    strength_value = Text(f" {kandinsky_prefs['strength']}", weight=FontWeight.BOLD)
    strength_slider = Row([Text("Init Image Strength: "), strength_value, strength])
    img_block = Container(Column([image_pickers, strength_slider, Divider(height=9, thickness=2)]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=kandinsky_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(kandinsky_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=kandinsky_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=kandinsky_prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=kandinsky_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, face_enhance, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_kandinsky = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_kandinsky.height = None if status['installed_ESRGAN'] else 0
    if not kandinsky_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    parameters_button = ElevatedButton(content=Text(value="✨   Run Kandinsky 2", size=20), on_click=lambda _: run_kandinsky(page))

    parameters_row = Row([parameters_button], alignment=MainAxisAlignment.SPACE_BETWEEN)
    page.kandinsky_output = Column([])
    c = Column([Container(
        padding=padding.only(18, 14, 20, 10), content=Column([
            Text ("🎎  Kandinsky 2.0", style=TextThemeStyle.TITLE_LARGE),
            Text ("A Latent Diffusion model with two Multilingual text encoders, supports 100+ languages, made in Russia."),
            Divider(thickness=1, height=4),
            prompt,
            param_rows, dropdown_row, guidance, width_slider, height_slider, #Divider(height=9, thickness=2), 
            img_block, page.ESRGAN_block_kandinsky,
            #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
            parameters_row,
            page.kandinsky_output
        ],
    ))], scroll=ScrollMode.AUTO)#batch_folder_name, batch_size, n_iterations, steps, ddim_eta, seed, 
    return c


CLIPstyler_prefs = {
    'source':'a photo',
    'prompt_text': 'Detailed oil painting',
    'batch_folder_name': 'clipstyler',
    'crop_size': 128,
    'num_crops': 64,
    'original_image': '',
    'image_dir': "",
    'training_iterations': 100,
    'width': 512,
    'height': 512,
    "apply_ESRGAN_upscale": prefs['apply_ESRGAN_upscale'],
    "enlarge_scale": prefs['enlarge_scale'],
    "display_upscaled_image": prefs['display_upscaled_image'],
}

def buildCLIPstyler(page):
    global CLIPstyler, prefs
    def changed(e, pref=None, ptype="str"):
      if pref is not None:
        if ptype == "int":
          CLIPstyler_prefs[pref] = int(e.control.value)
        elif ptype == "float":
          CLIPstyler_prefs[pref] = float(e.control.value)
        else:
          CLIPstyler_prefs[pref] = e.control.value
    def pick_files_result(e: FilePickerResultEvent):
        if e.files:
            img = e.files
            uf = []
            fname = img[0]
            print(", ".join(map(lambda f: f.name, e.files)))
            src_path = page.get_upload_url(fname.name, 600)
            uf.append(FilePickerUploadFile(fname.name, upload_url=src_path))
            pick_files_dialog.upload(uf)
            print(str(src_path))
            #src_path = ''.join(src_path)
            print(str(uf[0]))
            dst_path = os.path.join(root_dir, fname.name)
            print(f'Copy {src_path} to {dst_path}')
            #shutil.copy(src_path, dst_path)
            # TODO: is original or mask?
            original_image.value = dst_path

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    page.overlay.append(pick_files_dialog)
    #selected_files = Text()

    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
            upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
        if e.progress == 1:
            fname = os.path.join(root_dir, e.file_name)
            original_image.value = fname
            original_image.update()
            CLIPstyler_prefs['original_image'] = fname
            page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    pick_type = ""
    #page.overlay.append(pick_files_dialog)
    def pick_original(e):
        file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick original Image File")
    def toggle_ESRGAN(e):
        ESRGAN_settings.height = None if e.control.value else 0
        CLIPstyler_prefs['apply_ESRGAN_upscale'] = e.control.value
        ESRGAN_settings.update()
        has_changed = True
    def change_iterations(e):
        changed(e, 'training_iterations', ptype="int")
        iterations_value.value = f" {int(e.control.value)}"
        iterations_value.update()
        #iterations.controls[1].value = f" {e.control.value}"
        iterations.update()
    def change_width(e):
        width_slider.controls[1].value = f" {int(e.control.value)}px"
        width_slider.update()
        changed(e, 'width', ptype="int")
    def change_height(e):
        height_slider.controls[1].value = f" {int(e.control.value)}px"
        height_slider.update()
        changed(e, 'height', ptype="int")
    def change_enlarge_scale(e):
        enlarge_scale_slider.controls[1].value = f" {float(e.control.value)}x"
        enlarge_scale_slider.update()
        changed(e, 'enlarge_scale', ptype="float")

    prompt_text = TextField(label="Stylized Prompt Text", value=CLIPstyler_prefs['prompt_text'], on_change=lambda e:changed(e,'prompt_text'))
    batch_folder_name = TextField(label="Batch Folder Name", value=CLIPstyler_prefs['batch_folder_name'], on_change=lambda e:changed(e,'batch_folder_name'))
    source = TextField(label="Source Type", value=CLIPstyler_prefs['source'], on_change=lambda e:changed(e,'source'))
    #training_iterations = TextField(label="Training Iterations", value=CLIPstyler_prefs['training_iterations'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'training_iterations', ptype="int"))
    crop_size = TextField(label="Crop Size", value=CLIPstyler_prefs['crop_size'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'crop_size', ptype="int"))
    num_crops = TextField(label="Number of Crops", value=CLIPstyler_prefs['num_crops'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e:changed(e,'num_crops', ptype="int"))
    param_rows = Column([Row([batch_folder_name, source]), Row([crop_size, num_crops])])
    training_iterations = Slider(min=50, max=500, divisions=90, label="{value}", value=CLIPstyler_prefs['training_iterations'], on_change=change_iterations, expand=True)
    iterations_value = Text(f" {CLIPstyler_prefs['training_iterations']}", weight=FontWeight.BOLD)
    iterations = Row([Text("Training Iterations: "), iterations_value, training_iterations])
    width = Slider(min=128, max=1024, divisions=14, label="{value}px", value=CLIPstyler_prefs['width'], on_change=change_width, expand=True)
    width_value = Text(f" {int(CLIPstyler_prefs['width'])}px", weight=FontWeight.BOLD)
    width_slider = Row([Text(f"Width: "), width_value, width])
    height = Slider(min=128, max=1024, divisions=14, label="{value}px", value=CLIPstyler_prefs['height'], on_change=change_height, expand=True)
    height_value = Text(f" {int(CLIPstyler_prefs['height'])}px", weight=FontWeight.BOLD)
    height_slider = Row([Text(f"Height: "), height_value, height])

    original_image = TextField(label="Original Image", value=CLIPstyler_prefs['original_image'], on_change=lambda e:changed(e,'original_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_original, col={"*":1, "md":3}))
    #mask_image = TextField(label="Mask Image", value=CLIPstyler_prefs['mask_image'], on_change=lambda e:changed(e,'mask_image'), expand=True, suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD_OUTLINED, on_click=pick_mask, col={"*":1, "md":3}))
    #invert_mask = Checkbox(label="Invert", tooltip="Swaps the Black & White of your Mask Image", value=CLIPstyler_prefs['invert_mask'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'invert_mask'))
    image_picker = Container(content=Row([original_image]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    #prompt_strength = Slider(min=0.1, max=0.9, divisions=16, label="{value}%", value=CLIPstyler_prefs['prompt_strength'], on_change=change_strength, expand=True)
    #strength_value = Text(f" {int(CLIPstyler_prefs['prompt_strength'] * 100)}%", weight=FontWeight.BOLD)
    #strength_slider = Row([Text("Prompt Strength: "), strength_value, prompt_strength])
    #img_block = Container(Column([image_pickers, strength_slider, Divider(height=9, thickness=2)]), padding=padding.only(top=5), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    apply_ESRGAN_upscale = Switch(label="Apply ESRGAN Upscale", value=CLIPstyler_prefs['apply_ESRGAN_upscale'], active_color=colors.PRIMARY_CONTAINER, active_track_color=colors.PRIMARY, on_change=toggle_ESRGAN)
    enlarge_scale_value = Text(f" {float(CLIPstyler_prefs['enlarge_scale'])}x", weight=FontWeight.BOLD)
    enlarge_scale = Slider(min=1, max=4, divisions=6, label="{value}x", value=CLIPstyler_prefs['enlarge_scale'], on_change=change_enlarge_scale, expand=True)
    enlarge_scale_slider = Row([Text("Enlarge Scale: "), enlarge_scale_value, enlarge_scale])
    #face_enhance = Checkbox(label="Use Face Enhance GPFGAN", value=CLIPstyler_prefs['face_enhance'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'face_enhance'))
    display_upscaled_image = Checkbox(label="Display Upscaled Image", value=CLIPstyler_prefs['display_upscaled_image'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'display_upscaled_image'))
    ESRGAN_settings = Container(Column([enlarge_scale_slider, display_upscaled_image], spacing=0), padding=padding.only(left=32), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_styler = Container(Column([apply_ESRGAN_upscale, ESRGAN_settings]), animate_size=animation.Animation(1000, AnimationCurve.BOUNCE_OUT), clip_behavior=ClipBehavior.HARD_EDGE)
    page.ESRGAN_block_styler.height = None if status['installed_ESRGAN'] else 0
    if not CLIPstyler_prefs['apply_ESRGAN_upscale']:
        ESRGAN_settings.height = 0
    parameters_button = ElevatedButton(content=Text(value="📎   Run CLIP-Styler", size=20), on_click=lambda _: run_CLIPstyler(page))

    parameters_row = Row([parameters_button], alignment=MainAxisAlignment.SPACE_BETWEEN)
    page.CLIPstyler_output = Column([])
    c = Column([Container(
        padding=padding.only(18, 14, 20, 10), content=Column([
            Text ("😎   CLIP-Styler", style=TextThemeStyle.TITLE_LARGE),
            Text ("Transfers a Text Guided Style onto your Image From Prompt Description..."),
            Divider(thickness=1, height=4),
            image_picker, prompt_text,
            param_rows, iterations, width_slider, height_slider, #Divider(height=9, thickness=2), 
            page.ESRGAN_block_styler,
            #(img_block if status['installed_img2img'] or status['installed_stability'] else Container(content=None)), (clip_block if prefs['install_CLIP_guided'] else Container(content=None)), (ESRGAN_block if prefs['install_ESRGAN'] else Container(content=None)), 
            parameters_row,
            page.CLIPstyler_output
        ],
    ))], scroll=ScrollMode.AUTO)#batch_folder_name, batch_size, n_iterations, steps, crop_size, num_crops, 
    return c

def buildDreamMask(page):
    #prog_bars: Dict[str, ProgressRing] = {}
    files = Ref[Column]()
    #upload_button = Ref[ElevatedButton]()

    def file_picker_result(e: FilePickerResultEvent):
        files.current.controls.clear()
        if e.files != None:
          upload_files(e)
    def on_upload_progress(e: FilePickerUploadEvent):
      if e.progress == 1:
        files.current.controls.append(Row([Text(f"Done uploading {root_dir}{e.file_name}")]))
        page.update()
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)

    c = Column([
        ElevatedButton(
            "Select Init Image to Mask...",
            icon=icons.FOLDER_OPEN,
            on_click=lambda _: file_picker.pick_files(allow_multiple=False, allowed_extensions=["png", "PNG"], dialog_title="Pick Init Image File" ),
        ),
        Column(ref=files),
    ])
    return c

dreambooth_prefs = {
    'instance_prompt': '',
    'prior_preservation': False,
    'prior_preservation_class_prompt': "",
    'num_class_images': 12,
    'sample_batch_size': 2,
    'prior_loss_weight': 0.5,
    'prior_preservation_class_folder': os.path.join(root_dir, "class_images"),
    'learning_rate': 5e-06,
    'max_train_steps': 450,
    'seed': 222476,
    'name_of_your_concept': "",
    'save_concept': True,
    'where_to_save_concept': "Public Library",
    'max_size': 512,
    'image_path': '',
    'readme_description': '',
    'urls': [],
}

def buildDreamBooth(page):
    global prefs, dreambooth_prefs
    from PIL import Image as PILImage
    def changed(e, pref=None, ptype="str"):
        if pref is not None:
          if ptype == "int":
            dreambooth_prefs[pref] = int(e.control.value)
          elif ptype == "float":
            dreambooth_prefs[pref] = float(e.control.value)
          else:
            dreambooth_prefs[pref] = e.control.value
    def add_to_dreambooth_output(o):
        page.dreambooth_output.controls.append(o)
        page.dreambooth_output.update()
    def clear_output(e):
        if prefs['enable_sounds']: page.snd_delete.play()
        page.dreambooth_output.controls = []
        page.dreambooth_output.update()
        clear_button.visible = False
        clear_button.update()
    def db_help(e):
        def close_db_dlg(e):
          nonlocal db_help_dlg
          db_help_dlg.open = False
          page.update()
        db_help_dlg = AlertDialog(title=Text("💁   Help with DreamBooth"), content=Column([
            Text("First thing is to collect all your own images that you want to teach it to dream.  Feed it at least 5 square pictures of the object or style to learn, and it'll save your Custom Model Checkpoint."),
            Text("Fine-tune your perameters, but be aware that the training process takes a long time to run, so careful with the settings if you don't have the patience or processor. Dream at your own risk."),
          ], scroll=ScrollMode.AUTO), actions=[TextButton(emojize(':sleepy_face:') + "  Got it... ", on_click=close_db_dlg)], actions_alignment=MainAxisAlignment.END)
        page.dialog = db_help_dlg
        db_help_dlg.open = True
        page.update()
    def delete_image(e):
        f = e.control.data
        if os.path.isfile(f):
          os.remove(f)
          for i, fl in enumerate(page.db_file_list.controls):
            if fl.title.value == f:
              del page.db_file_list.controls[i]
              page.db_file_list.update()
              continue
    def delete_all_images(e):
        for fl in page.db_file_list.controls:
          f = fl.title.value
          if os.path.isfile(f):
            os.remove(f)
        page.db_file_list.controls.clear()
        page.db_file_list.update()
    def add_file(fpath, update=True):
        page.db_file_list.controls.append(ListTile(title=Text(fpath), dense=True, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[#TODO: View Image
              PopupMenuItem(icon=icons.DELETE, text="Delete Image", on_click=delete_image, data=fpath),
              PopupMenuItem(icon=icons.DELETE_SWEEP, text="Delete All", on_click=delete_all_images, data=fpath),
          ])))
        if update: page.db_file_list.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    save_dir = os.path.join(root_dir, 'my_concept')
    def on_upload_progress(e: FilePickerUploadEvent):
        if e.progress == 1:
          if not os.path.exists(save_dir):
            os.mkdir(save_dir)
          fname = os.path.join(root_dir, e.file_name)
          fpath = os.path.join(save_dir, e.file_name)
          original_img = PILImage.open(fname)
          width, height = original_img.size
          width, height = scale_dimensions(width, height, dreambooth_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          os.remove(fname)
          #shutil.move(fname, fpath)
          add_file(fpath)
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def pick_path(e):
        file_picker.pick_files(allow_multiple=True, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Image File to Enlarge")
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def add_image(e):
        save_dir = os.path.join(root_dir, 'my_concept')
        if not os.path.exists(save_dir):
          os.mkdir(save_dir)
        if image_path.value.startswith('http'):
          import requests
          from io import BytesIO
          response = requests.get(image_path.value)
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          concept_image = PILImage.open(BytesIO(response.content)).convert("RGB")
          width, height = concept_image.size
          width, height = scale_dimensions(width, height, dreambooth_prefs['max_size'])
          concept_image = concept_image.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          concept_image.save(fpath)
          add_file(fpath)
        elif os.path.isfile(image_path.value):
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          original_img = PILImage.open(image_path.value)
          width, height = original_img.size
          width, height = scale_dimensions(width, height, dreambooth_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          #shutil.copy(image_path.value, fpath)
          add_file(fpath)
        elif os.path.isdir(image_path.value):
          for f in os.listdir(image_path.value):
            file_path = os.path.join(image_path.value, f)
            if os.path.isdir(file_path): continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
              fpath = os.path.join(save_dir, f)
              original_img = PILImage.open(file_path)
              width, height = original_img.size
              width, height = scale_dimensions(width, height, dreambooth_prefs['max_size'])
              original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
              original_img.save(fpath)
              #shutil.copy(file_path, fpath)
              add_file(fpath)
        else:
          if bool(image_path.value):
            alert_msg(page, "Couldn't find a valid File, Path or URL...")
          else:
            pick_path(e)
          return
        image_path.value = ""
        image_path.update()
    def load_images():
        if os.path.exists(save_dir):
          for f in os.listdir(save_dir):
            existing = os.path.join(save_dir, f)
            if os.path.isdir(existing): continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
              add_file(existing, update=False)
    instance_prompt = TextField(label="Instance Prompt Token Text", value=dreambooth_prefs['instance_prompt'], on_change=lambda e:changed(e,'instance_prompt'))
    prior_preservation_class_prompt = TextField(label="Prior Preservation Class Prompt", value=dreambooth_prefs['prior_preservation_class_prompt'], on_change=lambda e:changed(e,'prior_preservation_class_prompt'))
    prior_preservation = Checkbox(label="Prior Preservation", tooltip="If you'd like class of the concept (e.g.: toy, dog, painting) is guaranteed to be preserved. This increases the quality and helps with generalization at the cost of training time", value=dreambooth_prefs['prior_preservation'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'prior_preservation'))
    num_class_images = TextField(label="Number of Class Images", value=dreambooth_prefs['num_class_images'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'num_class_images', ptype='int'), width = 160)
    sample_batch_size = TextField(label="Sample Batch Size", value=dreambooth_prefs['sample_batch_size'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'sample_batch_size', ptype='int'), width = 160)
    prior_loss_weight = TextField(label="Prior Loss Weight", value=dreambooth_prefs['prior_loss_weight'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'prior_loss_weight', ptype='float'), width = 160)
    max_train_steps = TextField(label="Max Training Steps", value=dreambooth_prefs['max_train_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'max_train_steps', ptype='int'), width = 160)
    learning_rate = TextField(label="Learning Rate", value=dreambooth_prefs['learning_rate'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'learning_rate', ptype='float'), width = 160)
    seed = TextField(label="Seed", value=dreambooth_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', ptype='int'), width = 160)
    save_concept = Checkbox(label="Save Concept    ", tooltip="", value=dreambooth_prefs['save_concept'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'save_concept'))
    where_to_save_concept = Dropdown(label="Where to Save Concept", width=250, options=[dropdown.Option("Public Library"), dropdown.Option("Privately to my Profile")], value=dreambooth_prefs['where_to_save_concept'], on_change=lambda e: changed(e, 'where_to_save_concept'))
    prior_preservation_class_folder = TextField(label="Prior Preservation Class Folder", value=dreambooth_prefs['prior_preservation_class_folder'], on_change=lambda e:changed(e,'prior_preservation_class_folder'))
    name_of_your_concept = TextField(label="Name of your Concept", value=dreambooth_prefs['name_of_your_concept'], on_change=lambda e:changed(e,'name_of_your_concept'))
    readme_description = TextField(label="Extra README Description", value=dreambooth_prefs['readme_description'], on_change=lambda e:changed(e,'readme_description'))
    max_size = Slider(min=256, max=1024, divisions=12, label="{value}px", value=float(dreambooth_prefs['max_size']), expand=True, on_change=lambda e:changed(e,'max_size', ptype='int'))
    max_row = Row([Text("Max Resolution Size: "), max_size])
    image_path = TextField(label="Image File or Folder Path or URL to Train", value=dreambooth_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_path), expand=1)
    add_image_button = ElevatedButton(content=Text("Add File or Folder"), on_click=add_image)
    page.db_file_list = Column([], tight=True, spacing=0)
    load_images()
    #seed = TextField(label="Seed", value=dreambooth_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', ptype='int'), width = 160)
    #lambda_entropy = TextField(label="Lambda Entropy", value=dreamfusdreambooth_prefsion_prefs['lambda_entropy'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'lambda_entropy', ptype='float'), width = 160)
    #max_steps = TextField(label="Max Steps", value=dreambooth_prefs['max_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'max_steps', ptype='int'), width = 160)
    page.dreambooth_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.dreambooth_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("😶‍🌫️  Create Custom DreamBooth Concept Model", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with DreamBooth Settings", on_click=db_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Provide a collection of images to conceptualize. Warning: May take over an hour to run the training..."),
        Divider(thickness=1, height=4),
        Row([instance_prompt, name_of_your_concept]),
        Row([num_class_images, sample_batch_size, prior_loss_weight]),
        Row([max_train_steps, learning_rate, seed]),
        Row([save_concept, where_to_save_concept]),
        readme_description,
        #Row([prior_preservation_class_folder]),
        max_row,
        Row([image_path, add_image_button]),
        page.db_file_list,
        ElevatedButton(content=Text("👨‍🎨️  Run DreamBooth", size=20), on_click=lambda _: run_dreambooth(page)),
        page.dreambooth_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

textualinversion_prefs = {
    'what_to_teach': 'object',
    'placeholder_token': '',
    'initializer_token': '',
    'scale_lr': True,
    'max_train_steps': 3000,
    'train_batch_size': 1,
    'gradient_accumulation_steps': 4,
    'seed': 22276,
    'repeats': 100,
    'output_dir': os.path.join(root_dir, "sd-concept-output"),
    'learning_rate': 5e-04,
    'name_of_your_concept': "",
    'save_concept': True,
    'where_to_save_concept': "Public Library",
    'max_size': 512,
    'image_path': '',
    'readme_description': '',
    'urls': [],
}
def buildTextualInversion(page):
    global prefs, textualinversion_prefs
    from PIL import Image as PILImage
    def changed(e, pref=None, ptype="str"):
        if pref is not None:
          if ptype == "int":
            textualinversion_prefs[pref] = int(e.control.value)
          elif ptype == "float":
            textualinversion_prefs[pref] = float(e.control.value)
          else:
            textualinversion_prefs[pref] = e.control.value
    def add_to_textualinversion_output(o):
        page.textualinversion_output.controls.append(o)
        page.textualinversion_output.update()
    def clear_output(e):
        if prefs['enable_sounds']: page.snd_delete.play()
        page.textualinversion_output.controls = []
        page.textualinversion_output.update()
        clear_button.visible = False
        clear_button.update()
    def ti_help(e):
        def close_ti_dlg(e):
          nonlocal ti_help_dlg
          ti_help_dlg.open = False
          page.update()
        ti_help_dlg = AlertDialog(title=Text("💁   Help with Textual-Inversion"), content=Column([
            Text(""),
          ], scroll=ScrollMode.AUTO), actions=[TextButton("😪  I'll figure it out... ", on_click=close_ti_dlg)], actions_alignment=MainAxisAlignment.END)
        page.dialog = ti_help_dlg
        ti_help_dlg.open = True
        page.update()
    def delete_image(e):
        f = e.control.data
        if os.path.isfile(f):
          os.remove(f)
          for i, fl in enumerate(page.ti_file_list.controls):
            if fl.title.value == f:
              del page.ti_file_list.controls[i]
              page.ti_file_list.update()
              continue
    def delete_all_images(e):
        for fl in page.ti_file_list.controls:
          f = fl.title.value
          if os.path.isfile(f):
            os.remove(f)
        page.ti_file_list.controls.clear()
        page.ti_file_list.update()
    def add_file(fpath, update=True):
        page.ti_file_list.controls.append(ListTile(title=Text(fpath), dense=True, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[#TODO: View Image
              PopupMenuItem(icon=icons.DELETE, text="Delete Image", on_click=delete_image, data=fpath),
              PopupMenuItem(icon=icons.DELETE_SWEEP, text="Delete All", on_click=delete_all_images, data=fpath),
          ])))
        if update: page.ti_file_list.update()
    def file_picker_result(e: FilePickerResultEvent):
        if e.files != None:
          upload_files(e)
    save_dir = os.path.join(root_dir, 'my_concept')
    def on_upload_progress(e: FilePickerUploadEvent):
        if e.progress == 1:
          if not os.path.exists(save_dir):
            os.mkdir(save_dir)
          fname = os.path.join(root_dir, e.file_name)
          fpath = os.path.join(save_dir, e.file_name)
          original_img = PILImage.open(fname)
          width, height = original_img.size
          width, height = scale_dimensions(width, height, textualinversion_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          os.remove(fname)
          #shutil.move(fname, fpath)
          add_file(fpath)
    file_picker = FilePicker(on_result=file_picker_result, on_upload=on_upload_progress)
    def pick_path(e):
        file_picker.pick_files(allow_multiple=True, allowed_extensions=["png", "PNG", "jpg", "jpeg"], dialog_title="Pick Image File to Enlarge")
    def upload_files(e):
        uf = []
        if file_picker.result != None and file_picker.result.files != None:
            for f in file_picker.result.files:
                uf.append(FilePickerUploadFile(f.name, upload_url=page.get_upload_url(f.name, 600)))
            file_picker.upload(uf)
    page.overlay.append(file_picker)
    def add_image(e):
        save_dir = os.path.join(root_dir, 'my_concept')
        if not os.path.exists(save_dir):
          os.mkdir(save_dir)
        if image_path.value.startswith('http'):
          import requests
          from io import BytesIO
          response = requests.get(image_path.value)
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          concept_image = PILImage.open(BytesIO(response.content)).convert("RGB")
          width, height = concept_image.size
          width, height = scale_dimensions(width, height, textualinversion_prefs['max_size'])
          concept_image = concept_image.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          concept_image.save(fpath)
          add_file(fpath)
        elif os.path.isfile(image_path.value):
          fpath = os.path.join(save_dir, image_path.value.rpartition(slash)[2])
          original_img = PILImage.open(image_path.value)
          width, height = original_img.size
          width, height = scale_dimensions(width, height, textualinversion_prefs['max_size'])
          original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
          original_img.save(fpath)
          #shutil.copy(image_path.value, fpath)
          add_file(fpath)
        elif os.path.isdir(image_path.value):
          for f in os.listdir(image_path.value):
            file_path = os.path.join(image_path.value, f)
            if os.path.isdir(file_path): continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
              fpath = os.path.join(save_dir, f)
              original_img = PILImage.open(file_path)
              width, height = original_img.size
              width, height = scale_dimensions(width, height, textualinversion_prefs['max_size'])
              original_img = original_img.resize((width, height), resample=PILImage.LANCZOS).convert("RGB")
              original_img.save(fpath)
              #shutil.copy(file_path, fpath)
              add_file(fpath)
        else:
          if bool(image_path.value):
            alert_msg(page, "Couldn't find a valid File, Path or URL...")
          else:
            pick_path(e)
          return
        image_path.value = ""
        image_path.update()
    def load_images():
        if os.path.exists(save_dir):
          for f in os.listdir(save_dir):
            existing = os.path.join(save_dir, f)
            if os.path.isdir(existing): continue
            if f.lower().endswith(('.png', '.jpg', '.jpeg')):
              add_file(existing, update=False)
    what_to_teach = Dropdown(label="What to Teach", width=250, options=[dropdown.Option("object"), dropdown.Option("style")], value=textualinversion_prefs['what_to_teach'], on_change=lambda e: changed(e, 'what_to_teach'))
    placeholder_token = TextField(label="Placeholder <Token> Keyword", value=textualinversion_prefs['placeholder_token'], on_change=lambda e:changed(e,'placeholder_token'))
    initializer_token = TextField(label="Initializer Token Category Summary", value=textualinversion_prefs['initializer_token'], on_change=lambda e:changed(e,'initializer_token'))
    scale_lr = Checkbox(label="Scale Learning Rate", tooltip="", value=textualinversion_prefs['scale_lr'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'scale_lr'))
    gradient_accumulation_steps = TextField(label="Gradient Accumulation Steps", value=textualinversion_prefs['gradient_accumulation_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'gradient_accumulation_steps', ptype='int'), width = 160)
    repeats = TextField(label="Repeats", value=textualinversion_prefs['repeats'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'repeats', ptype='int'), width = 160)
    train_batch_size = TextField(label="Train Batch Size", value=textualinversion_prefs['train_batch_size'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'train_batch_size', ptype='float'), width = 160)
    max_train_steps = TextField(label="Max Training Steps", value=textualinversion_prefs['max_train_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'max_train_steps', ptype='int'), width = 160)
    learning_rate = TextField(label="Learning Rate", value=textualinversion_prefs['learning_rate'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'learning_rate', ptype='float'), width = 160)
    seed = TextField(label="Seed", value=textualinversion_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', ptype='int'), width = 160)
    save_concept = Checkbox(label="Save Concept    ", tooltip="", value=textualinversion_prefs['save_concept'], fill_color=colors.PRIMARY_CONTAINER, check_color=colors.ON_PRIMARY_CONTAINER, on_change=lambda e:changed(e,'save_concept'))
    where_to_save_concept = Dropdown(label="Where to Save Concept", width=250, options=[dropdown.Option("Public Library"), dropdown.Option("Privately to my Profile")], value=textualinversion_prefs['where_to_save_concept'], on_change=lambda e: changed(e, 'where_to_save_concept'))
    output_dir = TextField(label="Prior Preservation Class Folder", value=textualinversion_prefs['output_dir'], on_change=lambda e:changed(e,'output_dir'))
    name_of_your_concept = TextField(label="Name of your Concept", value=textualinversion_prefs['name_of_your_concept'], on_change=lambda e:changed(e,'name_of_your_concept'))
    readme_description = TextField(label="Extra README Description", value=textualinversion_prefs['readme_description'], on_change=lambda e:changed(e,'readme_description'))
    max_size = Slider(min=256, max=1024, divisions=12, label="{value}px", value=float(textualinversion_prefs['max_size']), expand=True, on_change=lambda e:changed(e,'max_size', ptype='int'))
    max_row = Row([Text("Max Resolution Size: "), max_size])
    image_path = TextField(label="Image File or Folder Path or URL to Train", value=textualinversion_prefs['image_path'], on_change=lambda e:changed(e,'image_path'), suffix=IconButton(icon=icons.DRIVE_FOLDER_UPLOAD, on_click=pick_path), expand=1)
    add_image_button = ElevatedButton(content=Text("Add File or Folder"), on_click=add_image)
    page.ti_file_list = Column([], tight=True, spacing=0)
    load_images()
    #seed = TextField(label="Seed", value=textualinversion_prefs['seed'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'seed', ptype='int'), width = 160)
    #lambda_entropy = TextField(label="Lambda Entropy", value=dreamfustextualinversion_prefsion_prefs['lambda_entropy'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'lambda_entropy', ptype='float'), width = 160)
    #max_steps = TextField(label="Max Steps", value=textualinversion_prefs['max_steps'], keyboard_type=KeyboardType.NUMBER, on_change=lambda e: changed(e, 'max_steps', ptype='int'), width = 160)
    page.textualinversion_output = Column([])
    clear_button = Row([ElevatedButton(content=Text("❌   Clear Output"), on_click=clear_output)], alignment=MainAxisAlignment.END)
    clear_button.visible = len(page.textualinversion_output.controls) > 0
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Row([Text("😶‍🌫️  Create Cusom Textual-Inversion Concept Model", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.HELP, tooltip="Help with Textual-Inversion Settings", on_click=ti_help)], alignment=MainAxisAlignment.SPACE_BETWEEN),
        Text("Provide a collection of images to conceptualize. Warning: May take over an hour to run the training..."),
        Divider(thickness=1, height=4),
        Row([what_to_teach, initializer_token]),
        Row([placeholder_token, name_of_your_concept]),
        scale_lr,
        Row([gradient_accumulation_steps, repeats, train_batch_size]),
        Row([max_train_steps, learning_rate, seed]),
        Row([save_concept, where_to_save_concept]),
        readme_description,
        #Row([output_dir]),
        max_row,
        Row([image_path, add_image_button]),
        page.ti_file_list,
        ElevatedButton(content=Text("👨‍🎨️  Run Textual-Inversion", size=20), on_click=lambda _: run_textualinversion(page)),
        page.textualinversion_output,
        clear_button,
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

def get_directory_size(directory):
    total = 0
    for entry in os.scandir(directory):
        if entry.is_file():
            total += entry.stat().st_size
        elif entry.is_dir():
            try:
                total += get_directory_size(entry.path)
            except FileNotFoundError:
                pass
    return total
def convert_bytes(num):
    step_unit = 1000.0 #1024 bad the size
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step_unit:
            return "%3.1f %s" % (num, x)
        num /= step_unit

def buildCachedModelManager(page):
    global prefs
    def scan_cache(e):
      if not bool(prefs['cache_dir']):
        alert_msg(page, "You haven't set a Cache Directory in your Settings...")
        return
      elif not os.path.isdir(prefs['cache_dir']):
        alert_msg(page, "The Cache Directory in your Settings can't be found...")
        return
      if len(page.cached_folders.controls) > 1:
        page.cached_folders.controls.clear()
        page.cached_folders.update()
      page.cached_folders.controls.append(Row([ProgressRing(), Text(f"Scanning {prefs['cache_dir']}")]))
      dirs = [f.path for f in os.scandir(prefs['cache_dir']) if f.is_dir()]
      del page.cached_folders.controls[-1]
      page.cached_folders.update()
      for dir in dirs:
        page.cached_folders.controls.append(ListTile(title=Row([Text(f".{slash}{dir.rpartition(slash)[2]}", weight=FontWeight.BOLD), Text("")], alignment=MainAxisAlignment.SPACE_BETWEEN), data=dir, dense=True, trailing=PopupMenuButton(icon=icons.MORE_VERT,
          items=[PopupMenuItem(icon=icons.DELETE, text="Delete Model Directory", on_click=del_dir, data=dir)])))
        page.cached_folders.update()
      for l in page.cached_folders.controls:
        size = convert_bytes(get_directory_size(l.data))
        l.title.controls[1].value = size
        l.title.controls[1].update()
        page.cached_folders.update()
    def del_dir(e):
      dir = e.control.data
      shutil.rmtree(dir, ignore_errors=True)
      for i, l in enumerate(page.cached_folders.controls):
        if l.data == dir:
          del page.cached_folders.controls[i]
          page.cached_folders.update()
          break
      if prefs['enable_sounds']: e.page.snd_delete.play()
    page.cached_folders = Column([])
    c = Column([Container(
      padding=padding.only(18, 14, 20, 10),
      content=Column([
        Text("🗂️   Manage your Cache Directory Saved Models", style=TextThemeStyle.TITLE_LARGE),
        Text("If you're cacheing your model files, it can fill up your drive space quickly, so you can trim the fat as needed... Redownloads when used."),
        Divider(thickness=1, height=4),
        
        page.cached_folders,
        ElevatedButton(content=Text("🔍  Scan Cache Dirctory", size=20), on_click=scan_cache),
      ]
    ))], scroll=ScrollMode.AUTO)
    return c

use_custom_scheduler = False
retry_attempts_if_NSFW = 3
unet = None
pipe = None
pipe_img2img = None
pipe_interpolation = None
pipe_clip_guided = None
pipe_conceptualizer = None
pipe_repaint = None
pipe_imagic = None
pipe_composable = None
pipe_safe = None
pipe_versatile = None
pipe_versatile_text2img = None
pipe_versatile_variation = None
pipe_versatile_dualguided = None
pipe_upscale = None
pipe_depth = None
pipe_image_variation = None
pipe_unCLIP = None
pipe_unCLIP_image_variation = None
pipe_magic_mix = None
pipe_paint_by_example = None
pipe_kandinsky = None
stability_api = None
model_path = "CompVis/stable-diffusion-v1-4"
inpaint_model = "stabilityai/stable-diffusion-2-inpainting"
#"runwayml/stable-diffusion-inpainting"
scheduler = None
scheduler_clip = None
if is_Colab:
  from google.colab import output
  output.enable_custom_widget_manager()

finetuned_models = [
    #{"name": "Stable Diffusion v1.5", "path": "runwayml/stable-diffusion-v1-5", "prefix": "", "revision": "fp16"},
    #{"name": "Stable Diffusion v1.4", "path": "CompVis/stable-diffusion-v1-4", "prefix": "", "revision": "fp16"},
    {"name": "Midjourney v4 style", "path": "prompthero/midjourney-v4-diffusion", "prefix": "mdjrny-v4 style "},
    {"name": "Openjourney", "path": "prompthero/openjourney", "prefix": "mdjrny-v4 style "},
    {"name": "Future Diffusion", "path": "nitrosocke/Future-Diffusion", "prefix": "future style "},
    {"name": "Anything v3.0", "path": "Linaqruf/anything-v3.0", "prefix": ""},
    {"name": "Analog Diffusion", "path": "wavymulder/Analog-Diffusion", "prefix": "analog style "},
    {"name": "Architecture Diffusers", "path": "rrustom/stable-architecture-diffusers", "prefix": ""},
    {"name": "Arcane", "path":"nitrosocke/Arcane-Diffusion", "prefix":"arcane style "},
    {"name": "Archer Diffusion", "path":"nitrosocke/archer-diffusion", "prefix":"archer style "},
    {"name": "Nitro Diffusion", "path":"nitrosocke/nitro-diffusion", "prefix":"archer style, arcane style, modern disney style "},
    {"name": "Beeple Diffusion", "path": "riccardogiorato/beeple-diffusion", "prefix": "beeple style "},
    {"name": "Elden Ring", "path": "nitrosocke/elden-ring-diffusion", "prefix":"elden ring style "},
    {"name": "Modern Disney", "path": "nitrosocke/mo-di-diffusion", "prefix": "modern disney style "},
    {"name": "Classic Disney", "path": "nitrosocke/classic-anim-diffusion", "prefix": "classic disney style "},
    {"name": "Loving Vincent (Van Gogh)", "path": "dallinmackay/Van-Gogh-diffusion", "prefix": "lvngvncnt "},
    {"name": "Redshift renderer (Cinema4D)", "path": "nitrosocke/redshift-diffusion", "prefix": "redshift style "},
    {"name": "Waifu", "path": "hakurei/waifu-diffusion", "prefix": "", "revision": "fp16"},
    {"name": "TrinArt Waifu 50-50", "path": "doohickey/trinart-waifu-diffusion-50-50", "prefix": ""},
    {"name": "WikiArt v2", "path": "valhalla/sd-wikiart-v2", "prefix": ""},
    {"name": "Jak's Woolitize", "path": "plasmo/woolitize", "prefix": "woolitize "},
    {"name": "Inkpunk Diffusion", "path": "Envvi/Inkpunk-Diffusion", "prefix": "nvinkpunk "},
    {"name": "Simpsons Model", "path": "Norod78/sd-simpsons-model", "prefix":""},
    {"name": "Spider-Verse", "path": "nitrosocke/spider-verse-diffusion", "prefix":"spiderverse style "},
    {"name": "Pokémon", "path": "lambdalabs/sd-pokemon-diffusers", "prefix": ""},
    {"name": "Pony Diffusion", "path": "AstraliteHeart/pony-diffusion", "prefix": ""},
    {"name": "Robo Diffusion", "path": "nousr/robo-diffusion", "prefix": ""},
    {"name": "Dungeons & Diffusion", "path": "0xJustin/Dungeons-and-Diffusion", "prefix": ""},
    {"name": "Cyberpunk Anime", "path": "DGSpitzer/Cyberpunk-Anime-Diffusion", "prefix": "dgs illustration style "},
    {"name": "Tron Legacy", "path": "dallinmackay/Tron-Legacy-diffusion", "prefix": "trnlgcy "},
    {"name": "Guohua Diffusion", "path": "Langboat/Guohua-Diffusion", "prefix": "guohua style "},
    {"name": "Trin-sama TrinArt", "path": "naclbit/trinart_stable_diffusion_v2", "prefix": "", "revision": "diffusers-115k"},
    {"name": "Naruto Diffusers", "path": "lambdalabs/sd-naruto-diffusers", "prefix": ""},
    {"name": "Zelda: Breath of The Wild", "path": "s3nh/zelda-botw-stable-diffusion", "prefix": "botw style "},
    {"name": "JWST Deep Space Diffusion", "path": "dallinmackay/JWST-Deep-Space-diffusion", "prefix": "JWST "},
    #{"name": "LinkedIn-diffusion", "path": "prompthero/linkedin-diffusion", "prefix": "lnkdn photography "},
    {"name": "Bloodborne Diffusion", "path": "Guizmus/BloodborneDiffusion", "prefix": "Bloodborne Style "},
    {"name": "Cats the Musical", "path": "dallinmackay/Cats-Musical-diffusion", "prefix": "ctsmscl "},
    {"name": "Anon v1", "path": "TheMindExpansionNetwork/anonv1", "prefix": "AnonV1 "},
    {"name": "Avatar", "path": "Jersonm89/Avatar", "prefix": "avatar style "},
    {"name": "Dreamlike Diffusion v1", "path": "dreamlike-art/dreamlike-diffusion-1.0", "prefix": "dreamlikeart "},
    {"name": "Glitch", "path": "BakkerHenk/glitch", "prefix": "a photo in sks glitched style "},
    {"name": "Knollingcase", "path": "Aybeeceedee/knollingcase", "prefix": "knollingcase "},
    {"name": "Wavy Diffusion", "path": "wavymulder/wavyfusion", "prefix": "wa-vy style "},
    {"name": "TARDISfusion Classic Tardis", "path": "Guizmus/Tardisfusion", "prefix": "Classic Tardis style "},
    {"name": "TARDISfusion Modern Tardis", "path": "Guizmus/Tardisfusion", "prefix": "Modern Tardis style "},
    {"name": "TARDISfusion Tardis Box", "path": "Guizmus/Tardisfusion", "prefix": "Tardis Box style "},
    {"name": "Rick-Roll Style", "path": "TheLastBen/rick-roll-style", "prefix": "rckrll "},
    #{"name": "Studio Ghibli", "path": "flax/StudioGhibli", "prefix": "", "vae": True},
    #{"name": "Picture of the Week", "path": "Guizmus/SD_PoW_Collection", "prefix": "PoW Style ", "vae": True},
    #{"name": "PoW Bendstract ", "path": "Guizmus/SD_PoW_Collection", "prefix": "Bendstract Style ", "vae": True},
    #{"name": "PoW BendingReality", "path": "Guizmus/SD_PoW_Collection", "prefix": "BendingReality Style ", "vae": True},
    #{"name": "3d Illustration", "path": "aidystark/3Dillustration-stable-diffusion", "prefix": "3d illustration style ", "vae": True},
    #{"name": "megaPals Vintage", "path": "elRivx/megaPals", "prefix": "megaPals style "},
    #{"name": "Epic Space Machine", "path": "rabidgremlin/sd-db-epic-space-machine", "prefix": "EpicSpaceMachine "},
    #{"name": "Ouroboros", "path": "Eppinette/Ouroboros", "prefix": "m_ouroboros style "},
    #{"name": "Neko Girls", "path": "Nerfgun3/NekoModel", "prefix": "neko "},
    #{"name": "New Horror Fantasy", "path": "elRivx/sd-newhorrorfantasy_style", "prefix": "newhorrorfantasy_style "},
    #{"name": "DCAU Batman", "path": "IShallRiseAgain/DCAU", "prefix": "Batman_the_animated_series "},
    #{"name": "Smoke Diffusion", "path": "guumaster/smoke-diffusion", "prefix": "ssmoky "},
    #{"name": "reasonableDrink Dreams", "path": "elRivx/reasonableDrink", "prefix": "reasonableDrink "},
]
dreambooth_models = [{'name': 'disco-diffusion-style', 'token': 'a photo of ddfusion style'}, {'name': 'cat-toy', 'token': 'a photo of sks toy'}, {'name': 'herge-style', 'token': 'a photo of sks herge_style'}, {'name': 'alberto-pablo', 'token': 'a photo of sks Alberto'}, {'name': 'noggles-sd15-800-4e6', 'token': 'someone wearing sks glasses'}, {'name': 'spacecat', 'token': 'a photo of sks spacecat'}, {'name': 'pikachu', 'token': 'pikachu'}, {'name': 'kaltsit', 'token': 'kaltsit'}, {'name': 'robeez-baby-girl-water-shoes', 'token': 'a photo of sks  shoes'}, {'name': 'mertgunhan', 'token': 'mertgunhan'}, {'name': 'soydavidtapia', 'token': 'a photo of david tapia'}, {'name': 'spacecat0001', 'token': 'a photo of sks spacecat'}, {'name': 'noggles-glasses-600', 'token': 'a photo of a person wearing sks glasses'}, {'name': 'mario-action-figure', 'token': 'a photo of sks action figure'}, {'name': 'tattoo-design', 'token': 'line art sks tattoo design'}, {'name': 'danielveneco2', 'token': 'danielveneco'}, {'name': 'scarlet-witch-two', 'token': 'a photo of scarletwi person'}, {'name': 'angus-mcbride-style', 'token': 'angus mcbride style'}, {'name': 'mirtha-legrand', 'token': 'a photo of sks mirtha legrand'}, {'name': 'kiril', 'token': 'kiril'}, {'name': 'mr-potato-head', 'token': 'a photo of sks mr potato head'}, {'name': 'homelander', 'token': 'a photo of homelander guy'}, {'name': 'king-dog-sculpture', 'token': 'a photo of sks king dog sculpture'}, {'name': 'pedrocastillodonkey', 'token': 'a photo of PedroCastilloDonkey'}, {'name': 'xogren', 'token': 'a photo of xogren'}, {'name': 'emily-carroll-style', 'token': 'a detailed digital matte illustration by sks'}, {'name': 'sneaker', 'token': 'a photo of sks sneaker'}, {'name': 'rajj', 'token': 'a photo of sks man face'}, {'name': 'puuung', 'token': 'Puuung'}, {'name': 'partis', 'token': 'a photo of sks partis'}, {'name': 'alien-coral', 'token': 'a photo of sks alien coral'}, {'name': 'hensley-art-style', 'token': 'a painting in style of sks'}, {'name': 'tails-from-sonic', 'token': 'tails'}, {'name': 'ba-shiroko', 'token': 'a photo of sks shiroko'}, {'name': 'marina', 'token': 'marina'}, {'name': 'noggles-glasses-1200', 'token': 'a photo of a person wearing sks glasses'}, {'name': 'a-hat-in-time-girl', 'token': 'a render of sks'}, {'name': 'axolotee', 'token': 'a photo of sks Axolote'}, {'name': 'transparent-90s-console', 'token': 'a photo of sks handheld gaming console'}, {'name': 'andynsane', 'token': 'a photo of sks andynsane'}, {'name': 'tanidareal-v1', 'token': 'tanidareal'}, {'name': 'adventure-time-style', 'token': 'advtime style'}, {'name': 'sks-rv', 'token': 'a photo of sks rv'}, {'name': 'neff-voice-amp-2', 'token': 'a photo of sks neff voice amp #1'}, {'name': '27-from-mayonnaise-salesmen', 'token': 'a drawing of 27 from Mayonnaise SalesMen'}, {'name': 'baracus', 'token': 'b.a. baracus mr t'}, {'name': 'tahdig-rice', 'token': 'tahmricdig'}, {'name': 'angus-mcbride-style-v4', 'token': 'mcbride_style'}, {'name': 'the-witcher-game-ciri', 'token': 'a photo of a sks woman with white hair'}, {'name': 'paolo-bonolis', 'token': 'a photo of sks paolo bonolis'}, {'name': 'the-child', 'token': 'a photo of a mini australian shepherd with a slight underbite sks'}, {'name': 'gomber', 'token': 'a photo of sks toy'}, {'name': 'backpack', 'token': 'a photo of sks backpack'}, {'name': 'ricky-fort', 'token': 'a photo of sks ricky fort'}, {'name': 'mate', 'token': 'a photo of sks mate'}, {'name': 'zombie-head', 'token': 'a photo of sks zombie'}, {'name': 'leone-from-akame-ga-kill-v2', 'token': 'an anime woman character of sks'}, {'name': 'face2contra', 'token': 'a photo of sks face2contra'}, {'name': 'yakuza-0-kiryu-kazuma', 'token': 'photo of sks kiryu'}, {'name': 'gemba-cat', 'token': 'a photo of sks cat'}, {'name': 'angus-mcbride-v-3', 'token': 'angus mcbride style'}, {'name': 'california-gurls-music-video', 'token': 'caligurls'}, {'name': 'solo-levelling-art-style', 'token': 'sololeveling'}, {'name': 'blue-lightsaber-toy', 'token': 'a photo of sks toy'}, {'name': 'dmt-entity', 'token': 'a photo of sks DMT Entity'}, {'name': 'yingdream', 'token': 'a photo of an anime girl'}, {'name': 'kamenridergeats', 'token': 'a photo of kamenridergeats'}, {'name': 'quino', 'token': 'a photo of sks quino'}, {'name': 'digimon-adventure-anime-background-style', 'token': 'a landscape in sks style'}, {'name': 'evangelion-mech-unit-01', 'token': 'rendering of sks evangelion mech'}, {'name': 'elvis', 'token': 'elvis'}, {'name': 'musical-isotope', 'token': 'mi'}, {'name': 'tempa', 'token': 'a photo of sks Tempa'}, {'name': 'tempa2', 'token': 'a photo of sks Tempa'}, {'name': 'froggewut', 'token': 'a painting in the style of sks'}, {'name': 'smiling-friends-cartoon-style', 'token': 'a photo in style of sks'}, {'name': 'smario-world-map', 'token': 'a map in style of sks'}, {'name': 'edd', 'token': 'sks boy smiles'}, {'name': 'fang-yuan-002', 'token': 'an anime art of sks Fang_Yuan'}, {'name': 'langel', 'token': 'Langel'}, {'name': 'arthur-leywin', 'token': 'a photo of sks guy'}, {'name': 'kid-chameleon-character', 'token': 'kid-chameleon-character'}, {'name': 'road-to-ruin', 'token': 'starry night. sks themed level design. tiki ruins, stone statues, night sky and black silhouettes'}, {'name': 'vaporfades', 'token': 'an image in the style of sks'}, {'name': 'beard-oil-big-sur', 'token': 'a photo of sks beard oil'}, {'name': 'monero', 'token': 'a logo of sks'}, {'name': 'yagami-taichi-from-digimon-adventure-1999', 'token': 'an anime boy character of sks'}, {'name': 'duregar', 'token': 'a painting of sks character'}, {'name': 'pathfinder-iconics', 'token': 'drawing in the style of sks'}, {'name': 'tyxxxszv', 'token': 'tyxxxszv'}, {'name': 'Origtron', 'token': 'Entry not found'}, {'name': 'oleg-kog', 'token': 'oleg'}, {'name': 'mau-cat', 'token': 'a photo of sks cat'}, {'name': 'justinkrane-artwork', 'token': 'art by sks JustinKrane'}, {'name': 'little-mario-jumping', 'token': 'a screenshot of tiny sks character'}, {'name': 'blue-moo-moo', 'token': 'an image of sks creature'}, {'name': 'noggles-render-1k', 'token': 'a render of sks'}, {'name': 'metahuman-rkr', 'token': 'a photo of sks rkr'}, {'name': 'taras', 'token': 'photo of sks taras'}, {'name': 'rollerbeetle', 'token': 'a photo of rollerbeetle mount'}, {'name': 'joseph-russel-ammen', 'token': 'Joseph Russel Ammen'}, {'name': 'manybearsx', 'token': 'a photo of sks drawing'}, {'name': 'mexican-concha', 'token': 'a photo of sks Mexican Concha'}, {'name': 'angus-mcbride-style-v2', 'token': 'angus mcbride style'}, {'name': 'magikarp-pokemon', 'token': 'a photo of sks pokemon'}, {'name': 'seraphm', 'token': 'serphm'}, {'name': 'estelle-sims-style', 'token': '3D render from a videogame in sks style'}, {'name': 'iman-maleki-morteza-koutzian', 'token': 'imamk'}, {'name': 'abstract-patterns-in-nature', 'token': 'abnapa'}, {'name': 'retro3d', 'token': 'trsldamrl'}, {'name': 'glitched', 'token': 'trsldamrl'}, {'name': 'dulls', 'token': '<dulls-avatar> face'}, {'name': 'nasa-space-v2-768', 'token': 'Nasa style'}, {'name': 'avocado-toy', 'token': '<avocado-toy> toy'}, {'name': 'crisimsestelle', 'token': '3d render in <cri-sims> style'}, {'name': 'sally-whitemanev', 'token': 'whitemanedb'}, {'name': 'taylorswift', 'token': 'indexaa.png'}, {'name': 'house-emblem', 'token': 'a photo of sks house-emblem'}, {'name': 'skshikakinotonoderugomi', 'token': 'sksHikakinotonoderugomi'}, {'name': 'sksbinjousoudayo', 'token': 'sksBinjouSoudayo'}, {'name': 'sksseisupusyamuzero', 'token': 'ダウンロード'}, {'name': 'sksuminaoshishimabu', 'token': 'ダウンロード'}, {'name': 'hog-rider', 'token': 'a photo of sks character'}, {'name': 'harvard-beating-yale-ii', 'token': 'a photo of sks Harvard beating Yale'}, {'name': 'hockey-player', 'token': 'a photo of sks hockey'}, {'name': 'christiano-ronaldo', 'token': 'a photo of sks'}, {'name': 'colorful-ball', 'token': 'a photo of sks ball'}, {'name': 'american-flag-cowboy-hat', 'token': 'a photo of sks hat'}, {'name': 'pranav', 'token': 'a photo of sks person'}, {'name': 'top-gun-jacket-stable-diffusion', 'token': 'a photo of sks jacket'}, {'name': 'english-bulldog-1', 'token': 'a photo of sks an english bulldog'}, {'name': 'danreynolds', 'token': 'a photo of sks dan reynolds'}, {'name': 'persona-5-shigenori-style', 'token': 'descarga'}, {'name': 'original-character-cyclps', 'token': 'cyclps'}, {'name': 'zlnsky', 'token': 'zlnsky'}, {'name': 'true-guweiz-style', 'token': 'descarga'}, {'name': 'noggles-widescreen-4e6-800', 'token': 'noggles'}, {'name': 'conf', 'token': 'AWCDJG'}, {'name': 'dtv-pkmn-monster-style', 'token': 'image'}, {'name': 'xmasvibes', 'token': 'xmasvibes'}, {'name': 'blue-lightsaber-toy', 'token': 'a photo of sks toy'}, {'name': 'adventure-time-style', 'token': 'advtime style'}, {'name': 'brime', 'token': 'prplbrime'}, {'name': 'angus-mcbride-style-v4', 'token': 'mcbride_style'}, {'name': 'oleg-kog', 'token': 'oleg'}, {'name': 'tanidareal-v1', 'token': 'tanidareal'}, {'name': 'mertgunhan', 'token': 'mertgunhan'}, {'name': 'solo-levelling-art-style', 'token': 'sololeveling'}, {'name': 'tyxxxszv', 'token': 'tyxxxszv'}, {'name': 'california-gurls-music-video', 'token': 'caligurls'}, {'name': 'mario-action-figure', 'token': 'a photo of sks action figure'}, {'name': 'tahdig-rice', 'token': 'tahmricdig'}, {'name': 'pathfinder-iconics', 'token': 'drawing in the style of sks'}, {'name': 'angus-mcbride-v-3', 'token': 'angus mcbride style'}, {'name': 'angus-mcbride-style-v2', 'token': 'angus mcbride style'}, {'name': 'angus-mcbride-style', 'token': 'angus mcbride style'}, {'name': 'danielveneco2', 'token': 'danielveneco'}, {'name': 'emily-carroll-style', 'token': 'a detailed digital matte illustration by sks'}, {'name': 'noggles-sd15-800-4e6', 'token': 'someone wearing sks glasses'}, {'name': 'alberto-pablo', 'token': 'a photo of sks Alberto'}, {'name': 'marina', 'token': 'marina'}, {'name': 'kiril', 'token': 'kiril'}, {'name': 'spacecat0001', 'token': 'a photo of sks spacecat'}, {'name': 'baracus', 'token': 'b.a. baracus mr t'}, {'name': 'gemba-cat', 'token': 'a photo of sks cat'}, {'name': 'xogren', 'token': 'a photo of xogren'}, {'name': 'musical-isotope', 'token': 'mi'}, {'name': 'spacecat', 'token': 'a photo of sks spacecat'}, {'name': 'soydavidtapia', 'token': 'a photo of david tapia'}, {'name': 'yakuza-0-kiryu-kazuma', 'token': 'photo of sks kiryu'}, {'name': 'pedrocastillodonkey', 'token': 'a photo of PedroCastilloDonkey'}, {'name': 'rajj', 'token': 'a photo of sks man face'}, {'name': 'tails-from-sonic', 'token': 'tails'}, {'name': 'pikachu', 'token': 'pikachu'}, {'name': '27-from-mayonnaise-salesmen', 'token': 'a drawing of 27 from Mayonnaise SalesMen'}, {'name': 'vaporfades', 'token': 'an image in the style of sks'}, {'name': 'sally-whitemanev', 'token': 'whitemanedb'} ]

def get_model(name):
  #dropdown.Option("Stable Diffusion v1.5"), dropdown.Option("Stable Diffusion v1.4", dropdown.Option("Community Finetuned Model", dropdown.Option("DreamBooth Library Model"), dropdown.Option("Custom Model Path")
  if name == "Stable Diffusion v2.1 x768":
    return {'name':'Stable Diffusion v2.1 x768', 'path':'stabilityai/stable-diffusion-2-1', 'prefix':'', 'revision': 'fp16'}
  elif name == "Stable Diffusion v2.1 x512":
    return {'name':'Stable Diffusion v2.1 x512', 'path':'stabilityai/stable-diffusion-2-1-base', 'prefix':''}
  elif name == "Stable Diffusion v2.0":
    return {'name':'Stable Diffusion v2.0', 'path':'stabilityai/stable-diffusion-2', 'prefix':'', 'revision': 'fp16'}
  elif name == "Stable Diffusion v2.0 x768":
    return {'name':'Stable Diffusion v2.0 x768', 'path':'stabilityai/stable-diffusion-2', 'prefix':'', 'revision': 'fp16'}
  elif name == "Stable Diffusion v2.0 x512":
    return {'name':'Stable Diffusion v2.0 x512', 'path':'stabilityai/stable-diffusion-2-base', 'prefix':'', 'revision': 'fp16'}
  elif name == "Stable Diffusion v1.5":
    return {'name':'Stable Diffusion v1.5', 'path':'runwayml/stable-diffusion-v1-5', 'prefix':'', 'revision': 'fp16'}
  elif name == "Stable Diffusion v1.4":
    return {'name':'Stable Diffusion v1.4', 'path':'CompVis/stable-diffusion-v1-4', 'prefix':'', 'revision': 'fp16'}
  elif name == "Community Finetuned Model":
    return get_finetuned_model(prefs['finetuned_model'])
  elif name == "DreamBooth Library Model":
    return get_dreambooth_model(prefs['dreambooth_model'])
  elif name == "Custom Model Path":
    return {'name':'Custom Model', 'path':prefs['custom_model'], 'prefix':''}
  else:
    return {'name':'', 'path':'', 'prefix':''}
def get_finetuned_model(name):
  for mod in finetuned_models:
      if mod['name'] == name:
        return mod
  return {'name':'', 'path':'', 'prefix':''}
def get_dreambooth_model(name):
  for mod in dreambooth_models:
      if mod['name'] == name:
        return {'name':mod['name'], 'path':f'sd-dreambooth-library/{mod["name"]}', 'prefix':mod['token']}
  return {'name':'', 'path':'', 'prefix':''}

def get_diffusers(page):
    global scheduler, use_custom_scheduler, model_path, prefs, status
    try:
      import transformers
      #print(f"transformers=={transformers.__version__}")
      if transformers.__version__ == "4.21.3": #Workaround because CLIP-Interrogator required other version
        run_process("pip uninstall -y git+https://github.com/pharmapsychotic/BLIP.git@lib#egg=blip", realtime=False)
        run_process("pip uninstall -y clip-interrogator", realtime=False)
        run_process("pip uninstall -y transformers", realtime=False)
        #run_process("pip uninstall -q transformers==4.21.3", page=page, realtime=False)
      if transformers.__version__ == "4.23.1": # Kandinsky conflict
        run_process("pip uninstall -y transformers", realtime=False)
    except Exception:
      pass
    try:
      from huggingface_hub import notebook_login, HfApi, HfFolder, login
      from diffusers import StableDiffusionPipeline, logging
      import transformers
    except Exception:#ModuleNotFoundError as e:
      run_process("pip install -q --upgrade git+https://github.com/huggingface/accelerate.git", page=page)
      run_process("pip install -q --upgrade git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]", page=page)
      run_process("pip install -q --upgrade git+https://github.com/huggingface/transformers")
      #run_process("pip install -q transformers==4.23.1", page=page)
      run_process("pip install -q --upgrade scipy ftfy", page=page)
      run_process('pip install -qq "ipywidgets>=7,<8"', page=page)
      run_process("git config --global credential.helper store", page=page)
      
      from huggingface_hub import notebook_login, HfApi, HfFolder, login
      from diffusers import StableDiffusionPipeline, logging
      pass
    logging.set_verbosity_error()
    if not os.path.exists(HfFolder.path_token):
        #from huggingface_hub.commands.user import _login
        #_login(HfApi(), token=prefs['HuggingFace_api_key'])
        login(token=prefs['HuggingFace_api_key'], add_to_git_credential=True)
    #if prefs['model_ckpt'] == "Stable Diffusion v1.5": model_path =  "runwayml/stable-diffusion-v1-5"
    #elif prefs['model_ckpt'] == "Stable Diffusion v1.4": model_path =  "CompVis/stable-diffusion-v1-4"
    model = get_model(prefs['model_ckpt'])
    model_path = model['path']
    scheduler = model_scheduler(model_path)
    status['finetuned_model'] = False if model['name'].startswith("Stable") else True
    if prefs['memory_optimization'] == 'Xformers Mem Efficient Attention':
        # Still not the best way.  TODO: Fix importing, try ninja or other wheels?
        page.console_msg("Installing FaceBook's Xformers Memory Efficient Package...")
        run_process("pip install pyre-extensions==0.0.23", page=page)
        run_process("pip install -i https://test.pypi.org/simple/ formers==0.0.15.dev376", page=page)
        #run_process("pip install -q https://github.com/TheLastBen/fast-stable-diffusion/raw/main/precompiled/T4/xformers-0.0.13.dev0-py3-none-any.whl", page=page)
        #run_process("pip install https://github.com/metrolobo/xformers_wheels/releases/download/1d31a3ac/xformers-0.0.14.dev0-cp37-cp37m-linux_x86_64.whl", page=page)
        
def model_scheduler(model, big3=False):
    scheduler_mode = prefs['scheduler_mode']
    if scheduler_mode == "K-LMS":
      from diffusers import LMSDiscreteScheduler
      s = LMSDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "PNDM":
      from diffusers import PNDMScheduler
      s = PNDMScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "DDIM":
      from diffusers import DDIMScheduler
      s = DDIMScheduler.from_pretrained(model, subfolder="scheduler")
    elif big3:
      from diffusers import DDIMScheduler
      s = DDIMScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "DPM Solver":
      from diffusers import DPMSolverMultistepScheduler #"hf-internal-testing/tiny-stable-diffusion-torch"
      s = DPMSolverMultistepScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "DPM Solver Singlestep":
      from diffusers import DPMSolverSinglestepScheduler
      s = DPMSolverSinglestepScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "K-Euler Discrete":
      from diffusers import EulerDiscreteScheduler
      s = EulerDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "K-Euler Ancestrial":
      from diffusers import EulerAncestralDiscreteScheduler
      s = EulerAncestralDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "DPM Solver++":
      from diffusers import DPMSolverMultistepScheduler
      s = DPMSolverMultistepScheduler.from_pretrained(model, subfolder="scheduler",
        beta_start=0.00085,
        beta_end=0.012,
        beta_schedule="scaled_linear",
        num_train_timesteps=1000,
        trained_betas=None,
        #predict_epsilon=True,
        prediction_type="v_prediction" if model.startswith('stabilityai') else "epsilon",
        thresholding=False,
        algorithm_type="dpmsolver++",
        solver_type="midpoint",
        solver_order=2,
        #denoise_final=True,
        lower_order_final=True,
      )
    elif scheduler_mode == "Heun Discrete":
      from diffusers import HeunDiscreteScheduler
      s = HeunDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "K-DPM2 Ancestral":
      from diffusers import KDPM2AncestralDiscreteScheduler
      s = KDPM2AncestralDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "K-DPM2 Discrete":
      from diffusers import KDPM2DiscreteScheduler
      s = KDPM2DiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "IPNDM":
      from diffusers import IPNDMScheduler
      s = IPNDMScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "Score-SDE-Vp":
      from diffusers import ScoreSdeVpScheduler
      s = ScoreSdeVpScheduler() #(num_train_timesteps=2000, beta_min=0.1, beta_max=20, sampling_eps=1e-3, tensor_format="np")
      use_custom_scheduler = True
    elif scheduler_mode == "Score-SDE-Ve":
      from diffusers import ScoreSdeVeScheduler
      s = ScoreSdeVeScheduler() #(num_train_timesteps=2000, snr=0.15, sigma_min=0.01, sigma_max=1348, sampling_eps=1e-5, correct_steps=1, tensor_format="pt"
      use_custom_scheduler = True
    elif scheduler_mode == "DDPM":
      from diffusers import DDPMScheduler
      s = DDPMScheduler(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, variance_type="fixed_small", clip_sample=True, tensor_format="pt")
      use_custom_scheduler = True
    elif scheduler_mode == "Karras-Ve":
      from diffusers import KarrasVeScheduler
      s = KarrasVeScheduler() #(sigma_min=0.02, sigma_max=100, s_noise=1.007, s_churn=80, s_min=0.05, s_max=50, tensor_format="pt")
      use_custom_scheduler = True
    elif scheduler_mode == "LMS": #no more
      from diffusers import LMSScheduler
      s = LMSScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
      #(num_train_timesteps=1000, beta_start=0.0001, beta_end=0.02, beta_schedule="linear", trained_betas=None, timestep_values=None, tensor_format="pt")
      use_custom_scheduler = True
    #print(f"Loaded Schedueler {scheduler_mode} {type(scheduler)}")
    else:
      print(f"Unknown scheduler request {scheduler_mode} - Using K-LMS")
      from diffusers import LMSDiscreteScheduler
      s = LMSDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    return s


torch_device = "cuda"
try:
    import torch
except Exception:
    print("Installing PyTorch with CUDA 1.17")
    run_sp("pip install -U --force-reinstall torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117", realtime=False)
    import torch
    pass
finally:
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if torch_device == "cpu": print("WARNING: CUDA is only available with CPU, so GPU tasks are limited. Can use Stability-API & OpenAI, but not Diffusers...")
import gc
#from torch.amp.autocast_mode import autocast
from random import random
import time

pb = ProgressBar(width=420, bar_height=8)
total_steps = args['steps']
def callback_fn(step: int, timestep: int, latents: torch.FloatTensor) -> None:
    callback_fn.has_been_called = True
    global total_steps, pb
    if total_steps is None: total_steps = timestep
    if total_steps == 0: total_steps = len(latents)
    percent = (step +1)/ total_steps
    pb.value = percent
    pb.tooltip = f"[{step +1} / {total_steps}] (timestep: {timestep})"
    #print(f"step: {step}, total: {total_steps}, latent: {len(latents)}")
    #if step == 0:
        #latents = latents.detach().cpu().numpy()
        #assert latents.shape == (1, 4, 64, 64)
        #latents_slice = latents[0, -3:, -3:, -1]
        #expected_slice = np.array([1.8285, 1.2857, -0.1024, 1.2406, -2.3068, 1.0747, -0.0818, -0.6520, -2.9506])
        #assert np.abs(latents_slice.flatten() - expected_slice).max() < 1e-3
    pb.update()

def optimize_pipe(p, vae=True):
    if prefs['sequential_cpu_offload']:
      p.enable_sequential_cpu_offload()
    if prefs['memory_optimization'] == 'Attention Slicing':
      #if not model['name'].startswith('Stable Diffusion v2'): #TEMP hack until it updates my git with fix
      if prefs['sequential_cpu_offload']:
        p.enable_attention_slicing(1)
      else:
        p.enable_attention_slicing()
    elif prefs['memory_optimization'] == 'Xformers Mem Efficient Attention':
      p.enable_xformers_memory_efficient_attention()
    if prefs['vae_slicing'] and vae:
      p.enable_vae_slicing()
    return p

def get_text2image(page):
    os.chdir(root_dir)
    global pipe, unet, scheduler, prefs
    def open_url(e):
      page.launch_url(e.data)
    '''if pipe is not None:
        #print("Clearing the ol' pipe first...")
        del pipe
        gc.collect()
        torch.cuda.empty_cache()
        pipe = None'''
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
          unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", use_auth_token=True, device_map="auto")
        else:
          unet = UNet2DConditionModel.from_pretrained(model_path, revision="fp16", torch_dtype=torch.float16, subfolder="unet", use_auth_token=True, device_map="auto")
        vae = vae.to(torch_device)
        text_encoder = text_encoder.to(torch_device)
        #if enable_attention_slicing:
        #  unet.enable_attention_slicing() #slice_size
        unet = unet.to(torch_device)
      else:
        #if status['finetuned_model']: pipe = get_txt2img_pipe()
        #else:
        pipe = get_lpw_pipe()
    except EnvironmentError as e:
      model = get_model(prefs['model_ckpt'])
      model_url = f"https://huggingface.co/{model['path']}"
      alert_msg(page, f'ERROR: Looks like you need to accept the HuggingFace {model["name"]} Model Cards to use Checkpoint',
                content=Markdown(f'[{model_url}]({model_url})<br>{e}', on_tap_link=open_url))

# I thought it's what I wanted, but current implementation does same as mine but doesn't clear memory between
def get_mega_pipe():
  global pipe, scheduler, model_path, prefs
  from diffusers import DiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  
  if prefs['higher_vram_mode']:
    pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="stable_diffusion_mega", scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  else:
    pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="stable_diffusion_mega", scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  pipe = pipe.to(torch_device)
  pipe = optimize_pipe(pipe)
  pipe.set_progress_bar_config(disable=True)
  return pipe

def get_lpw_pipe():
  global pipe, scheduler, model_path, prefs
  from diffusers import DiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  from diffusers import AutoencoderKL, UNet2DConditionModel
  model = get_model(prefs['model_ckpt'])
  os.chdir(root_dir)
  #if not os.path.isfile(os.path.join(root_dir, 'lpw_stable_diffusion.py')):
  #  run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/Skquark/diffusers/main/examples/community/lpw_stable_diffusion.py")
  #from lpw_stable_diffusion import StableDiffusionLongPromptWeightingPipeline
  if prefs['higher_vram_mode']:# or model['name'] == "Stable Diffusion v2.1 x768": #, revision="fp32"
    pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/lpw_stable_diffusion_mod", scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, torch_dtype=torch.float32, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker").to(torch_device), feature_extractor=None, requires_safety_checker=not prefs['disable_nsfw_filter'])
  else:
    if 'revision' in model:
      pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/lpw_stable_diffusion_mod", scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, revision=model['revision'], torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker").to(torch_device), device_map="auto", feature_extractor=None, requires_safety_checker=not prefs['disable_nsfw_filter'])
    else:
      if 'vae' in model:
        from diffusers import AutoencoderKL, UNet2DConditionModel
        vae = AutoencoderKL.from_pretrained(model_path, subfolder="vae", torch_dtype=torch.float16)
        unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", torch_dtype=torch.float16)
        pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/lpw_stable_diffusion_mod", vae=vae, unet=unet, scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker").to(torch_device), device_map="auto", feature_extractor=None, requires_safety_checker=not prefs['disable_nsfw_filter'])
      else:
        pipe = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/lpw_stable_diffusion_mod", scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker").to(torch_device), device_map="auto", feature_extractor=None, requires_safety_checker=not prefs['disable_nsfw_filter'])
    #pipe = DiffusionPipeline.from_pretrained(model_path, community="lpw_stable_diffusion", scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
  #if prefs['enable_attention_slicing']: pipe.enable_attention_slicing()
  pipe = pipe.to(torch_device)
  pipe = optimize_pipe(pipe)
  pipe.set_progress_bar_config(disable=True)
  return pipe

def get_txt2img_pipe():
  global pipe, scheduler, model_path, prefs, status
  from diffusers import StableDiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  #from diffusers import AutoencoderKL, UNet2DConditionModel
  #if status['finetuned_model']:
  #  vae = AutoencoderKL.from_pretrained(model_path, subfolder="vae", torch_dtype=torch.float16)
  #  unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", torch_dtype=torch.float16)
  pipe = optimize_pipe(pipe)
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
    unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet", feature_extractor=None, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), device_map="auto")
  else:
    unet = UNet2DConditionModel.from_pretrained(model_path, revision="fp16", feature_extractor=None, torch_dtype=torch.float16, subfolder="unet", safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), device_map="auto")
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
    run_process("pip install watchdog -q", page=page, realtime=False)
    status['loaded_interpolation'] = True

def get_interpolation_pipe():
    global pipe_interpolation, scheduler, model_path, prefs
    from diffusers import StableDiffusionPipeline
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
    os.chdir(root_dir)
    if not os.path.isfile(os.path.join(root_dir, 'clip_guided_stable_diffusion.py')):
      run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/Skquark/diffusers/main/examples/community/interpolate_stable_diffusion.py")
    from interpolate_stable_diffusion import StableDiffusionWalkPipeline
    model = get_model(prefs['model_ckpt'])
    if prefs['higher_vram_mode']:
      pipe_interpolation = StableDiffusionWalkPipeline.from_pretrained(model_path, scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
      #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    else:
      if 'revision' in model:
        pipe_interpolation = StableDiffusionWalkPipeline.from_pretrained(model_path, scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, revision=model['revision'], torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
      else:
        pipe_interpolation = StableDiffusionWalkPipeline.from_pretrained(model_path, scheduler=scheduler, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
      #pipe = StableDiffusionPipeline.from_pretrained(model_path, scheduler=scheduler, revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"))
    pipe_interpolation = pipe_interpolation.to(torch_device)
    pipe_interpolation = optimize_pipe(pipe_interpolation, vae=False)
    pipe_interpolation.set_progress_bar_config(disable=True)
    return pipe_interpolation

def get_image2image(page):
    from diffusers import StableDiffusionInpaintPipeline, DDIMScheduler, PNDMScheduler, LMSDiscreteScheduler
    import torch, gc
    global pipe_img2img
    def open_url(e):
      page.launch_url(e.data)
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if pipe_img2img is not None:
      #print("Clearing the ol' pipe first...")
      del pipe_img2img
      gc.collect()
      torch.cuda.empty_cache()
      pipe_img2img = None
    try:
      pipe_img2img = get_img2img_pipe()
    except EnvironmentError:
      model_url = f"https://huggingface.co/{inpaint_model}"
      alert_msg(page, f'ERROR: Looks like you need to accept the HuggingFace Inpainting Model Card to use Checkpoint',
                content=Markdown(f'[{model_url}]({model_url})', on_tap_link=open_url))
    loaded_img2img = True

def get_img2img_pipe():
  global pipe_img2img, scheduler, model_path, inpaint_model, prefs, callback_fn
  from diffusers import DiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  
  if prefs['higher_vram_mode']:
    pipe_img2img = DiffusionPipeline.from_pretrained(
        inpaint_model,
        custom_pipeline="img2img_inpainting",
        scheduler=model_scheduler(inpaint_model),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  else:
      pipe_img2img = DiffusionPipeline.from_pretrained(
      inpaint_model,
      custom_pipeline="img2img_inpainting",
      scheduler=model_scheduler(inpaint_model),
      cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
      revision="fp16", 
      torch_dtype=torch.float16,
      safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
  pipe_img2img.to(torch_device)
  #if prefs['enable_attention_slicing']: pipe_img2img.enable_attention_slicing() #slice_size
  if prefs['sequential_cpu_offload']:
    pipe_img2img.enable_sequential_cpu_offload()
  pipe_img2img = optimize_pipe(pipe_img2img)
  pipe_img2img.set_progress_bar_config(disable=True)
  #def dummy(images, **kwargs): return images, False
  #pipe_img2img.safety_checker = dummy
  return pipe_img2img

def get_imagic(page):
    global pipe_imagic
    if pipe_imagic is not None:
        del pipe_imagic
        gc.collect()
        torch.cuda.empty_cache()
    pipe_imagic = get_imagic_pipe()

def get_imagic_pipe():
  global pipe_imagic, scheduler, model_path, prefs
  from diffusers import DiffusionPipeline#, DDIMScheduler
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  #ddim = DDIMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", clip_sample=False, set_alpha_to_one=False)
  #if prefs['higher_vram_mode']:
  if True:
    pipe_imagic = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/imagic_stable_diffusion_mod", scheduler=model_scheduler(model_path, big3=True), use_auth_token=True, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
  else:
    pipe_imagic = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/imagic_stable_diffusion_mod", scheduler=model_scheduler(model_path, big3=True), revision="fp16", torch_dtype=torch.float16, safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None)
  pipe_imagic = pipe_imagic.to(torch_device)
  def dummy(images, **kwargs):
    return images, False
  if prefs['disable_nsfw_filter']:
    pipe_imagic.safety_checker = dummy
  pipe_imagic = optimize_pipe(pipe_imagic, vae=False)
  #pipe_imagic.set_progress_bar_config(disable=True)
  return pipe_imagic

def get_composable(page):
    global pipe_composable
    if pipe_composable is not None:
        del pipe_composable
        gc.collect()
        torch.cuda.empty_cache()
    pipe_composable = get_composable_pipe()

def get_composable_pipe():
  global pipe_composable, scheduler, model_path, prefs
  from diffusers import DiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  
  #if prefs['higher_vram_mode']:
  if True:
    pipe_composable = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/composable_stable_diffusion_mod", scheduler=model_scheduler(model_path, big3=True), use_auth_token=True, feature_extractor=None, safety_checker=None)
  else:
    pipe_composable = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/composable_stable_diffusion_mod", scheduler=model_scheduler(model_path, big3=True), revision="fp16", torch_dtype=torch.float16, feature_extractor=None, safety_checker=None)
  pipe_composable = pipe_composable.to(torch_device)
  def dummy(images, **kwargs):
    return images, False
  if prefs['disable_nsfw_filter']:
    pipe_composable.safety_checker = dummy
  pipe_composable = optimize_pipe(pipe_composable, vae=False)
  #pipe_composable.set_progress_bar_config(disable=True)
  return pipe_composable

def get_versatile(page):
    import torch, gc
    global pipe_versatile_text2img
    def open_url(e):
      page.launch_url(e.data)
    try:
      pipe_versatile_text2img = get_versatile_text2img_pipe()
    except Exception as er:
      model_url = f"https://huggingface.co/shi-labs/versatile-diffusion"
      alert_msg(page, f'ERROR: Looks like you need to accept the HuggingFace Versatile Diffusion Model Card to use Checkpoint',
                content=Markdown(f'[{model_url}]({model_url})<br>{er}', on_tap_link=open_url))

def get_versatile_pipe(): # Mega was taking up too much vram and crashing the system
  global pipe_versatile, scheduler, model_path, prefs
  from diffusers import VersatileDiffusionPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "shi-labs/versatile-diffusion"
  if prefs['higher_vram_mode']:
    pipe_versatile = VersatileDiffusionPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  else:
    pipe_versatile = VersatileDiffusionPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        #revision="fp16", 
        torch_dtype=torch.float16,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  pipe_versatile.to(torch_device)
  pipeversatile = optimize_pipe(pipeversatile, vae=False)
  pipe_versatile.set_progress_bar_config(disable=True)
  return pipe_versatile

def get_versatile_text2img_pipe():
  global pipe_versatile_text2img, scheduler, model_path, prefs
  from diffusers import VersatileDiffusionTextToImagePipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "shi-labs/versatile-diffusion"
  if prefs['higher_vram_mode']:
    pipe_versatile_text2img = VersatileDiffusionTextToImagePipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  else:
    pipe_versatile_text2img = VersatileDiffusionTextToImagePipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        #revision="fp16", 
        torch_dtype=torch.float16,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  pipe_versatile_text2img.to(torch_device)
  pipe_versatile_text2img = optimize_pipe(pipe_versatile_text2img, vae=False)
  pipe_versatile_text2img.set_progress_bar_config(disable=True)
  return pipe_versatile_text2img

def get_versatile_variation_pipe():
  global pipe_versatile_variation, scheduler, model_path, prefs
  from diffusers import VersatileDiffusionImageVariationPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "shi-labs/versatile-diffusion"
  if prefs['higher_vram_mode']:
    pipe_versatile_variation = VersatileDiffusionImageVariationPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  else:
    pipe_versatile_variation = VersatileDiffusionImageVariationPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        #revision="fp16", 
        torch_dtype=torch.float16,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  pipe_versatile_variation.to(torch_device)
  pipe_versatile_variation = optimize_pipe(pipe_versatile_variation, vae=False)
  pipe_versatile_variation.set_progress_bar_config(disable=True)
  return pipe_versatile_variation

def get_versatile_dualguided_pipe():
  global pipe_versatile_dualguided, scheduler, model_path, prefs
  from diffusers import VersatileDiffusionDualGuidedPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "shi-labs/versatile-diffusion"
  if prefs['higher_vram_mode']:
    pipe_versatile_dualguided = VersatileDiffusionDualGuidedPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  else:
    pipe_versatile_dualguided = VersatileDiffusionDualGuidedPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        #revision="fp16", 
        torch_dtype=torch.float16,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"), feature_extractor=None
    )
  pipe_versatile_dualguided.to(torch_device)
  pipe_versatile_dualguided = optimize_pipe(pipe_versatile_dualguided, vae=False)
  pipe_versatile_dualguided.set_progress_bar_config(disable=True)
  return pipe_versatile_dualguided

def get_safe(page):
    import torch, gc
    global pipe_safe
    def open_url(e):
      page.launch_url(e.data)
    if pipe_safe is not None:
      #print("Clearing the ol' pipe first...")
      del pipe_safe
      gc.collect()
      torch.cuda.empty_cache()
      pipe_safe = None
    try:
      pipe_safe = get_safe_pipe()
    except Exception as er:
      model_url = f"https://huggingface.co/AIML-TUDA/stable-diffusion-safe"
      alert_msg(page, f'ERROR: Looks like you need to accept the HuggingFace Safe Model Card to use Checkpoint. Reinstall after accepting TOS.',
                content=Markdown(f'[{model_url}]({model_url})<br>{er}', on_tap_link=open_url))

def get_safe_pipe():
  global pipe_safe, scheduler, model_path, prefs, callback_fn
  from diffusers import StableDiffusionPipelineSafe
  from diffusers.pipelines.stable_diffusion_safe import StableDiffusionPipelineSafe
  #from diffusers.pipelines.safety_checker import SafeStableDiffusionPipelineSafe
  #from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "AIML-TUDA/stable-diffusion-safe"
  #if prefs['higher_vram_mode']:
  if True:
    pipe_safe = StableDiffusionPipelineSafe.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None# if prefs['disable_nsfw_filter'] else SafeStableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
    )
  else:
      pipe_safe = StableDiffusionPipelineSafe.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        revision="fp16", 
        torch_dtype=torch.float16,
        safety_checker=None# if prefs['disable_nsfw_filter'] else SafeStableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker")
      )
  pipe_safe.to(torch_device)
  pipe_safe = optimize_pipe(pipe_safe, vae=False)
  pipe_safe.set_progress_bar_config(disable=True)
  return pipe_safe

def get_upscale(page):
    import torch, gc
    global pipe_upscale
    def open_url(e):
      page.launch_url(e.data)
    if pipe_upscale is None:
      try:
        pipe_upscale = get_upscale_pipe()
      except Exception as er:
        model_url = f"https://huggingface.co/{model_path}"
        alert_msg(page, f'ERROR: Looks like you need to accept the HuggingFace Upscale Model Card to use Checkpoint',
                  content=Markdown(f'[{model_url}]({model_url})<br>{er}', on_tap_link=open_url))

def get_upscale_pipe():
  global pipe_upscale, scheduler, prefs
  from diffusers import StableDiffusionUpscalePipeline
  model_id = "stabilityai/stable-diffusion-x4-upscaler"
  if prefs['higher_vram_mode']:
    pipe_upscale = StableDiffusionUpscalePipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id, big3=True),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        #safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
    )
  else:
    pipe_upscale = StableDiffusionUpscalePipeline.from_pretrained(
      model_id,
      scheduler=model_scheduler(model_id, big3=True),
      cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
      revision="fp16", 
      torch_dtype=torch.float16,
      #safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker")
    )
  pipe_upscale.to(torch_device)
  pipe_upscale = optimize_pipe(pipe_upscale, vae=False)
  pipe_upscale.set_progress_bar_config(disable=True)
  return pipe_upscale

def get_clip(page):
    global pipe_clip_guided, model_path
    #os.chdir(root_dir)
    #if not os.path.isfile(os.path.join(root_dir, 'clip_guided_stable_diffusion.py')):
    #  run_sp("wget -q --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/Skquark/diffusers/c16761e9d94a3374710110ba5e3087cb9f8ba906/examples/community/clip_guided_stable_diffusion.py")
    #from clip_guided_stable_diffusion import *

    if pipe_clip_guided is not None:
        #print("Clearing out old CLIP Guided pipeline before reloading.")
        del pipe_clip_guided
        gc.collect()
        torch.cuda.empty_cache()
    pipe_clip_guided = get_clip_guided_pipe()

def get_clip_guided_pipe():
    global pipe_clip_guided, scheduler_clip, prefs
    from diffusers import DiffusionPipeline
    from diffusers import LMSDiscreteScheduler, PNDMScheduler, StableDiffusionPipeline
    from transformers import CLIPModel, CLIPFeatureExtractor #, CLIPGuidedStableDiffusion
    '''pipeline = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        revision="fp16",
    )'''
    if isinstance(scheduler, LMSDiscreteScheduler) or isinstance(scheduler, PNDMScheduler):
      scheduler_clip = scheduler
    else:
      scheduler_clip = LMSDiscreteScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear")
    model = get_model(prefs['model_ckpt'])

    clip_model = CLIPModel.from_pretrained(prefs['clip_model_id'], torch_dtype=torch.float16)
    feature_extractor = CLIPFeatureExtractor.from_pretrained(prefs['clip_model_id'])

    if 'revision' in model:
      pipe_clip_guided = DiffusionPipeline.from_pretrained(
              model_path,
              custom_pipeline="AlanB/clip_guided_stable_diffusion_mod",
              clip_model=clip_model,
              feature_extractor=feature_extractor,
              scheduler=model_scheduler(model_path, big3=True),
              cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
              safety_checker=None,
              torch_dtype=torch.float16,
              revision=model['revision'],
              #device_map="auto",
          )
    else:
      pipe_clip_guided = DiffusionPipeline.from_pretrained(model_path, custom_pipeline="AlanB/clip_guided_stable_diffusion_mod", clip_model=clip_model, feature_extractor=feature_extractor, scheduler=model_scheduler(model_path, big3=True), safety_checker=None, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None, torch_dtype=torch.float16)
    pipe_clip_guided = pipe_clip_guided.to(torch_device)
    '''
    pipe_clip_guided = CLIPGuidedStableDiffusion(
        unet=pipeline.unet,
        vae=pipeline.vae,
        tokenizer=pipeline.tokenizer,
        text_encoder=pipeline.text_encoder,
        scheduler=scheduler_clip,
        clip_model=clip_model,
        feature_extractor=feature_extractor,
    )'''
    pipe_clip_guided = optimize_pipe(pipe_clip_guided, vae=False)
    return pipe_clip_guided

def get_repaint(page):
    global pipe_repaint
    if pipe_repaint is not None:
        #print("Clearing out old CLIP Guided pipeline before reloading.")
        del pipe_repaint
        gc.collect()
        torch.cuda.empty_cache()
    pipe_repaint = get_repaint_pipe()

def get_repaint_pipe():
    global pipe_repaint
    from diffusers import UNet2DModel, RePaintScheduler, RePaintPipeline
    #model = get_model(prefs['model_ckpt'])
    #model_path = model['path']
    model_id = "google/ddpm-ema-celebahq-256"
    unet = UNet2DModel.from_pretrained(model_id)
    repaint_scheduler = RePaintScheduler.from_pretrained(model_id)
    pipe_repaint = RePaintPipeline(unet=unet, scheduler=repaint_scheduler).to(torch_device)
    return pipe_repaint

def get_depth2img(page):
  global pipe_depth
  pipe_depth = get_depth_pipe()

def get_depth_pipe():
  global pipe_depth, prefs
  from diffusers import StableDiffusionDepth2ImgPipeline
  from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
  model_id = "stabilityai/stable-diffusion-2-depth"
  if prefs['higher_vram_mode']:
    pipe_depth = StableDiffusionDepth2ImgPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
    )
  else:
    pipe_depth = StableDiffusionDepth2ImgPipeline.from_pretrained(
        model_id,
        scheduler=model_scheduler(model_id),
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        revision="fp16", 
        torch_dtype=torch.float16,
    )
  pipe_depth.to(torch_device)
  pipe_depth = optimize_pipe(pipe_depth, vae=False)
  pipe_depth.set_progress_bar_config(disable=True)
  return pipe_depth

SD_sampler = None
def get_stability(page):
    global prefs, SD_sampler#, stability_api
    '''try:
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
        engine=prefs['model_checkpoint']# if prefs['model_checkpoint'] == "stable-diffusion-v1-5" else "stable-diffusion-v1",
    )
    SD_sampler = client.get_sampler_from_str(prefs['generation_sampler'].lower())'''
    # New way, other is obsolete
    import requests
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    stability_url = f"{api_host}/v1alpha/engines/list" #user/account"
    response = requests.get(stability_url, headers={"Authorization": prefs['Stability_api_key']})
    if response.status_code != 200:
      alert_msg(page, "ERROR with Stability-ai: " + str(response.text))
      return
    payload = response.json()
    #print(str(payload))
    status['installed_stability'] = True

'''
def update_stability():
    global SD_sampler, stability_api
    from stability_sdk import client
    stability_api = client.StabilityInference(
        key=prefs['Stability_api_key'], 
        verbose=True,
        engine=prefs['model_checkpoint']
    )
    SD_sampler = client.get_sampler_from_str(prefs['generation_sampler'].lower())
'''
def get_ESRGAN(page):
    os.chdir(dist_dir)
    run_process(f"git clone https://github.com/xinntao/Real-ESRGAN.git -q", page=page, cwd=dist_dir)
    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process("pip install basicsr --quiet", page=page, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process("pip install facexlib --quiet", page=page, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process("pip install gfpgan --quiet", page=page, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process(f"pip install -r requirements.txt --quiet", page=page, realtime=False, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process(f"python setup.py develop --quiet", page=page, realtime=False, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    run_process(f"wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -P experiments/pretrained_models --quiet", page=page, cwd=os.path.join(dist_dir, 'Real-ESRGAN'))
    os.chdir(root_dir)


concepts = [{'name': 'cat-toy', 'token': 'cat-toy'}, {'name': 'madhubani-art', 'token': 'madhubani-art'}, {'name': 'birb-style', 'token': 'birb-style'}, {'name': 'indian-watercolor-portraits', 'token': 'watercolor-portrait'}, {'name': 'xyz', 'token': 'xyz'}, {'name': 'poolrooms', 'token': 'poolrooms'}, {'name': 'cheburashka', 'token': 'cheburashka'}, {'name': 'hours-style', 'token': 'hours'}, {'name': 'turtlepics', 'token': 'henry-leonardi'}, {'name': 'karl-s-lzx-1', 'token': 'lzx'}, {'name': 'canary-cap', 'token': 'canary-cap'}, {'name': 'ti-junglepunk-v0', 'token': 'jungle-punk'}, {'name': 'mafalda-character', 'token': 'mafalda-quino'}, {'name': 'magic-pengel', 'token': 'magic-pengel'}, {'name': 'schloss-mosigkau', 'token': 'ralph'}, {'name': 'cubex', 'token': 'cube'}, {'name': 'covid-19-rapid-test', 'token': 'covid-test'}, {'name': 'character-pingu', 'token': 'character-pingu'}, {'name': '2814-roth', 'token': '2814Roth'}, {'name': 'vkuoo1', 'token': 'style-vkuoo1'}, {'name': 'ina-art', 'token': ''}, {'name': 'monte-novo', 'token': 'monte novo cutting board'}, {'name': 'interchanges', 'token': 'xchg'}, {'name': 'walter-wick-photography', 'token': 'walter-wick'}, {'name': 'arcane-style-jv', 'token': 'arcane-style-jv'}, {'name': 'w3u', 'token': 'w3u'}, {'name': 'smiling-friend-style', 'token': 'smilingfriends-cartoon'}, {'name': 'dr-livesey', 'token': 'dr-livesey'}, {'name': 'monster-girl', 'token': 'monster-girl'}, {'name': 'abstract-concepts', 'token': 'art-style'}, {'name': 'reeducation-camp', 'token': 'reeducation-camp'}, {'name': 'miko-3-robot', 'token': 'miko-3'}, {'name': 'party-girl', 'token': 'party-girl'}, {'name': 'dicoo', 'token': 'Dicoo'}, {'name': 'kuvshinov', 'token': 'kuvshinov'}, {'name': 'mass', 'token': 'mass'}, {'name': 'ldr', 'token': 'ldr'}, {'name': 'hub-city', 'token': 'HubCity'}, {'name': 'masyunya', 'token': 'masyunya'}, {'name': 'david-moreno-architecture', 'token': 'dm-arch'}, {'name': 'lolo', 'token': 'lolo'}, {'name': 'apulian-rooster-v0-1', 'token': 'apulian-rooster-v0.1'}, {'name': 'fractal', 'token': 'fractal'}, {'name': 'nebula', 'token': 'nebula'}, {'name': 'ldrs', 'token': 'ldrs'}, {'name': 'art-brut', 'token': 'art-brut'}, {'name': 'malika-favre-art-style', 'token': 'malika-favre'}, {'name': 'line-art', 'token': 'line-art'}, {'name': 'shrunken-head', 'token': 'shrunken-head'}, {'name': 'bonzi-monkey', 'token': 'bonzi'}, {'name': 'herge-style', 'token': 'herge'}, {'name': 'johnny-silverhand', 'token': 'johnny-silverhand'}, {'name': 'linnopoke', 'token': 'linnopoke'}, {'name': 'koko-dog', 'token': 'koko-dog'}, {'name': 'stuffed-penguin-toy', 'token': 'pengu-toy'}, {'name': 'monster-toy', 'token': 'monster-toy'}, {'name': 'dong-ho', 'token': 'dong-ho'}, {'name': 'orangejacket', 'token': 'orangejacket'}, {'name': 'fergal-cat', 'token': 'fergal-cat'}, {'name': 'summie-style', 'token': 'summie-style'}, {'name': 'chonkfrog', 'token': 'chonkfrog'}, {'name': 'alberto-mielgo', 'token': 'street'}, {'name': 'lucky-luke', 'token': 'lucky-luke'}, {'name': 'zdenek-art', 'token': 'zdenek-artwork'}, {'name': 'star-tours-posters', 'token': 'star-tours'}, {'name': 'huang-guang-jian', 'token': 'huang-guang-jian'}, {'name': 'painting', 'token': 'will'}, {'name': 'line-style', 'token': 'line-style'}, {'name': 'venice', 'token': 'venice'}, {'name': 'russian', 'token': 'Russian'}, {'name': 'tony-diterlizzi-s-planescape-art', 'token': 'tony-diterlizzi-planescape'}, {'name': 'moeb-style', 'token': 'moe-bius'}, {'name': 'amine', 'token': 'ayna'}, {'name': 'kojima-ayami', 'token': 'KOJIMA'}, {'name': 'dong-ho2', 'token': 'dong-ho-2'}, {'name': 'ruan-jia', 'token': 'ruan-jia'}, {'name': 'purplefishli', 'token': 'purplefishli'}, {'name': 'cry-baby-style', 'token': 'cry-baby'}, {'name': 'between2-mt-fade', 'token': 'b2MTfade'}, {'name': 'mtl-longsky', 'token': 'mtl-longsky'}, {'name': 'scrap-style', 'token': 'style-chewie'}, {'name': 'tela-lenca', 'token': 'tela-lenca'}, {'name': 'zillertal-can', 'token': 'zillertal-ipa'}, {'name': 'shu-doll', 'token': 'shu-doll'}, {'name': 'eastward', 'token': 'eastward'}, {'name': 'chuck-walton', 'token': 'Chuck_Walton'}, {'name': 'chucky', 'token': 'merc'}, {'name': 'smw-map', 'token': 'smw-map'}, {'name': 'erwin-olaf-style', 'token': 'erwin-olaf'}, {'name': 'maurice-quentin-de-la-tour-style', 'token': 'maurice'}, {'name': 'dan-seagrave-art-style', 'token': 'dan-seagrave'}, {'name': 'drive-scorpion-jacket', 'token': 'drive-scorpion-jacket'}, {'name': 'dark-penguin-pinguinanimations', 'token': 'darkpenguin-robot'}, {'name': 'rd-paintings', 'token': 'rd-painting'}, {'name': 'borderlands', 'token': 'borderlands'}, {'name': 'depthmap', 'token': 'depthmap'}, {'name': 'lego-astronaut', 'token': 'lego-astronaut'}, {'name': 'transmutation-circles', 'token': 'tcircle'}, {'name': 'mycat', 'token': 'mycat'}, {'name': 'ilya-shkipin', 'token': 'ilya-shkipin-style'}, {'name': 'moxxi', 'token': 'moxxi'}, {'name': 'riker-doll', 'token': 'rikerdoll'}, {'name': 'apex-wingman', 'token': 'wingman-apex'}, {'name': 'naf', 'token': 'nal'}, {'name': 'handstand', 'token': 'handstand'}, {'name': 'vb-mox', 'token': 'vb-mox'}, {'name': 'pixel-toy', 'token': 'pixel-toy'}, {'name': 'olli-olli', 'token': 'olli-olli'}, {'name': 'floral', 'token': 'ntry not foun'}, {'name': 'minecraft-concept-art', 'token': 'concept'}, {'name': 'yb-anime', 'token': 'anime-character'}, {'name': 'ditko', 'token': 'cat-toy'}, {'name': 'disquieting-muses', 'token': 'muses'}, {'name': 'ned-flanders', 'token': 'flanders'}, {'name': 'fluid-acrylic-jellyfish-creatures-style-of-carl-ingram-art', 'token': 'jelly-core'}, {'name': 'ic0n', 'token': 'ic0n'}, {'name': 'pyramidheadcosplay', 'token': 'Cos-Pyramid'}, {'name': 'phc', 'token': 'Cos-Pyramid'}, {'name': 'og-mox-style', 'token': 'og-mox-style'}, {'name': 'klance', 'token': 'klance'}, {'name': 'john-blanche', 'token': 'john-blanche'}, {'name': 'cowboy', 'token': 'cowboyStyle'}, {'name': 'darkpenguinanimatronic', 'token': 'penguin-robot'}, {'name': 'doener-red-line-art', 'token': 'dnr'}, {'name': 'style-of-marc-allante', 'token': 'Marc_Allante'}, {'name': 'crybaby-style-2-0', 'token': 'crybaby2'}, {'name': 'werebloops', 'token': 'werebloops'}, {'name': 'xbh', 'token': 'xbh'}, {'name': 'unfinished-building', 'token': 'unfinished-building'}, {'name': 'teelip-ir-landscape', 'token': 'teelip-ir-landscape'}, {'name': 'road-to-ruin', 'token': 'RtoR'}, {'name': 'piotr-jablonski', 'token': 'piotr-jablonski'}, {'name': 'jamiels', 'token': 'jamiels'}, {'name': 'tomcat', 'token': 'tom-cat'}, {'name': 'meyoco', 'token': 'meyoco'}, {'name': 'nixeu', 'token': 'nixeu'}, {'name': 'tnj', 'token': 'tnj'}, {'name': 'cute-bear', 'token': 'cute-bear'}, {'name': 'leica', 'token': 'leica'}, {'name': 'anime-boy', 'token': 'myAItestShota'}, {'name': 'garfield-pizza-plush', 'token': 'garfield-plushy'}, {'name': 'design', 'token': 'design'}, {'name': 'mikako-method', 'token': 'm-m'}, {'name': 'cornell-box', 'token': 'cornell-box'}, {'name': 'sculptural-style', 'token': 'diaosu'}, {'name': 'aavegotchi', 'token': 'aave-gotchi'}, {'name': 'swamp-choe-2', 'token': 'cat-toy'}, {'name': 'super-nintendo-cartridge', 'token': 'snesfita-object'}, {'name': 'garfield-pizza-plush-v2', 'token': 'garfield-plushy'}, {'name': 'rickyart', 'token': 'RickyArt'}, {'name': 'eye-of-agamotto', 'token': 'eye-aga'}, {'name': 'freddy-fazbear', 'token': 'freddy-fazbear'}, {'name': 'glass-pipe', 'token': 'glass-sherlock'}, {'name': 'black-waifu', 'token': 'black-waifu'}, {'name': 'roy-lichtenstein', 'token': 'roy-lichtenstein'}, {'name': 'ugly-sonic', 'token': 'ugly-sonic'}, {'name': 'glow-forest', 'token': 'dark-forest'}, {'name': 'painted-student', 'token': 'painted_student'}, {'name': 'salmonid', 'token': 'salmonid'}, {'name': 'huayecai820-greyscale', 'token': 'huayecaigreyscale-style'}, {'name': 'arthur1', 'token': 'arthur1'}, {'name': 'huckleberry', 'token': 'huckleberry'}, {'name': 'collage3', 'token': 'Collage3'}, {'name': 'spritual-monsters', 'token': 'spritual-monsters'}, {'name': 'baldi', 'token': 'baldi'}, {'name': 'tcirle', 'token': 'tcircle'}, {'name': 'pantone-milk', 'token': 'pantone-milk'}, {'name': 'retropixelart-pinguin', 'token': 'retropixelart-style'}, {'name': 'doose-s-realistic-art-style', 'token': 'doose-realistic'}, {'name': 'grit-toy', 'token': 'grit-toy'}, {'name': 'pink-beast-pastelae-style', 'token': 'pinkbeast'}, {'name': 'mikako-methodi2i', 'token': 'm-mi2i'}, {'name': 'aj-fosik', 'token': 'AJ-Fosik'}, {'name': 'collage-cutouts', 'token': 'collage-cutouts'}, {'name': 'cute-cat', 'token': 'cute-bear'}, {'name': 'kaleido', 'token': 'kaleido'}, {'name': 'xatu', 'token': 'xatu-pokemon'}, {'name': 'a-female-hero-from-the-legend-of-mir', 'token': ' <female-hero> from The Legend of Mi'}, {'name': 'cologne', 'token': 'cologne-dom'}, {'name': 'wlop-style', 'token': 'wlop-style'}, {'name': 'larrette', 'token': 'larrette'}, {'name': 'bert-muppet', 'token': 'bert-muppet'}, {'name': 'my-hero-academia-style', 'token': 'MHA style'}, {'name': 'vcr-classique', 'token': 'vcr_c'}, {'name': 'xatu2', 'token': 'xatu-test'}, {'name': 'tela-lenca2', 'token': 'tela-lenca'}, {'name': 'dragonborn', 'token': 'dragonborn'}, {'name': 'mate', 'token': 'mate'}, {'name': 'alien-avatar', 'token': 'alien-avatar'}, {'name': 'pastelartstyle', 'token': 'Arzy'}, {'name': 'kings-quest-agd', 'token': 'ings-quest-ag'}, {'name': 'doge-pound', 'token': 'doge-pound'}, {'name': 'type', 'token': 'typeface'}, {'name': 'fileteado-porteno', 'token': 'fileteado-porteno'}, {'name': 'bullvbear', 'token': 'bullVBear'}, {'name': 'freefonix-style', 'token': 'Freefonix'}, {'name': 'garcon-the-cat', 'token': 'garcon-the-cat'}, {'name': 'better-collage3', 'token': 'C3'}, {'name': 'metagabe', 'token': 'metagabe'}, {'name': 'ggplot2', 'token': 'ggplot2'}, {'name': 'yoshi', 'token': 'yoshi'}, {'name': 'illustration-style', 'token': 'illustration-style'}, {'name': 'centaur', 'token': 'centaur'}, {'name': 'zoroark', 'token': 'zoroark'}, {'name': 'bad_Hub_Hugh', 'token': 'HubHugh'}, {'name': 'irasutoya', 'token': 'irasutoya'}, {'name': 'liquid-light', 'token': 'lls'}, {'name': 'zaneypixelz', 'token': 'zaneypixelz'}, {'name': 'tubby', 'token': 'tubby'}, {'name': 'atm-ant', 'token': 'atm-ant'}, {'name': 'fang-yuan-001', 'token': 'fang-yuan'}, {'name': 'dullboy-caricature', 'token': 'dullboy-cari'}, {'name': 'bada-club', 'token': 'bada-club'}, {'name': 'zaney', 'token': 'zaney'}, {'name': 'a-tale-of-two-empires', 'token': 'two-empires'}, {'name': 'dabotap', 'token': 'dabotap'}, {'name': 'harley-quinn', 'token': 'harley-quinn'}, {'name': 'vespertine', 'token': 'Vesp'}, {'name': 'ricar', 'token': 'ricard'}, {'name': 'conner-fawcett-style', 'token': 'badbucket'}, {'name': 'ingmar-bergman', 'token': 'ingmar-bergman'}, {'name': 'poutine-dish', 'token': 'poutine-qc'}, {'name': 'shev-linocut', 'token': 'shev-linocut'}, {'name': 'grifter', 'token': 'grifter'}, {'name': 'dog', 'token': 'Winston'}, {'name': 'tangles', 'token': 'cora-tangle'}, {'name': 'lost-rapper', 'token': 'lost-rapper'}, {'name': 'eddie', 'token': 'ddi'}, {'name': 'thunderdome-covers', 'token': 'thunderdome'}, {'name': 'she-mask', 'token': 'she-mask'}, {'name': 'chillpill', 'token': 'Chillpill'}, {'name': 'robertnava', 'token': 'robert-nava'}, {'name': 'looney-anime', 'token': 'looney-anime'}, {'name': 'axe-tattoo', 'token': 'axe-tattoo'}, {'name': 'fireworks-over-water', 'token': 'firework'}, {'name': 'collage14', 'token': 'C14'}, {'name': 'green-tent', 'token': 'green-tent'}, {'name': 'dtv-pkmn', 'token': 'dtv-pkm2'}, {'name': 'crinos-form-garou', 'token': 'crinos'}, {'name': '8bit', 'token': '8bit'}, {'name': 'tubby-cats', 'token': 'tubby'}, {'name': 'travis-bedel', 'token': 'bedelgeuse2'}, {'name': 'uma', 'token': 'uma'}, {'name': 'ie-gravestone', 'token': 'internet-explorer-gravestone'}, {'name': 'colossus', 'token': 'colossus'}, {'name': 'uma-style-classic', 'token': 'uma'}, {'name': 'collage3-hubcity', 'token': 'C3Hub'}, {'name': 'goku', 'token': 'goku'}, {'name': 'galaxy-explorer', 'token': 'galaxy-explorer'}, {'name': 'rl-pkmn-test', 'token': 'rl-pkmn'}, {'name': 'naval-portrait', 'token': 'naval-portrait'}, {'name': 'daycare-attendant-sun-fnaf', 'token': 'biblic-sun-fnaf'}, {'name': 'reksio-dog', 'token': 'reksio-dog'}, {'name': 'breakcore', 'token': 'reakcor'}, {'name': 'junji-ito-artstyle', 'token': 'junji-ito-style'}, {'name': 'gram-tops', 'token': 'gram-tops'}, {'name': 'henjo-techno-show', 'token': 'HENJOTECHNOSHOW'}, {'name': 'trash-polka-artstyle', 'token': 'trash-polka-style'}, {'name': 'faraon-love-shady', 'token': ''}, {'name': 'trigger-studio', 'token': 'Trigger Studio'}, {'name': 'tb303', 'token': '"tb303'}, {'name': 'neon-pastel', 'token': 'neon-pastel'}, {'name': 'fursona', 'token': 'fursona-2'}, {'name': 'sterling-archer', 'token': 'archer-style'}, {'name': 'captain-haddock', 'token': 'captain-haddock'}, {'name': 'my-mug', 'token': 'my-mug'}, {'name': 'joe-whiteford-art-style', 'token': 'joe-whiteford-artstyle'}, {'name': 'on-kawara', 'token': 'on-kawara'}, {'name': 'hours-sentry-fade', 'token': 'Hours_Sentry'}, {'name': 'rektguy', 'token': 'rektguy'}, {'name': 'dyoudim-style', 'token': 'DyoudiM-style'}, {'name': 'kaneoya-sachiko', 'token': 'Kaneoya'}, {'name': 'retro-girl', 'token': 'retro-girl'}, {'name': 'buddha-statue', 'token': 'buddha-statue'}, {'name': 'hitokomoru-style-nao', 'token': 'hitokomoru-style'}, {'name': 'plant-style', 'token': 'plant'}, {'name': 'cham', 'token': 'cham'}, {'name': 'mayor-richard-irvin', 'token': 'Richard_Irvin'}, {'name': 'sd-concepts-library-uma-meme', 'token': 'uma-object-full'}, {'name': 'uma-meme', 'token': 'uma-object-full'}, {'name': 'thunderdome-cover', 'token': 'thunderdome-cover'}, {'name': 'sem-mac2n', 'token': 'SEM_Mac2N'}, {'name': 'hoi4', 'token': 'hoi4'}, {'name': 'hd-emoji', 'token': 'HDemoji-object'}, {'name': 'lumio', 'token': 'lumio'}, {'name': 't-skrang', 'token': 'tskrang'}, {'name': 'agm-style-nao', 'token': 'agm-style'}, {'name': 'uma-meme-style', 'token': 'uma-meme-style'}, {'name': 'retro-mecha-rangers', 'token': 'aesthetic'}, {'name': 'babushork', 'token': 'babushork'}, {'name': 'qpt-atrium', 'token': 'QPT_ATRIUM'}, {'name': 'sushi-pixel', 'token': 'sushi-pixel'}, {'name': 'osrsmini2', 'token': ''}, {'name': 'ttte', 'token': 'ttte-2'}, {'name': 'atm-ant-2', 'token': 'atm-ant'}, {'name': 'dan-mumford', 'token': 'dan-mumford'}, {'name': 'renalla', 'token': 'enall'}, {'name': 'cow-uwu', 'token': 'cow-uwu'}, {'name': 'one-line-drawing', 'token': 'lineart'}, {'name': 'inuyama-muneto-style-nao', 'token': 'inuyama-muneto-style'}, {'name': 'altvent', 'token': 'AltVent'}, {'name': 'accurate-angel', 'token': 'accurate-angel'}, {'name': 'mtg-card', 'token': 'mtg-card'}, {'name': 'ddattender', 'token': 'ddattender'}, {'name': 'thalasin', 'token': 'thalasin-plus'}, {'name': 'moebius', 'token': 'moebius'}, {'name': 'liqwid-aquafarmer', 'token': 'aquafarmer'}, {'name': 'onepunchman', 'token': 'OnePunch'}, {'name': 'kawaii-colors', 'token': 'kawaii-colors-style'}, {'name': 'naruto', 'token': 'Naruto'}, {'name': 'backrooms', 'token': 'Backrooms'}, {'name': 'a-hat-kid', 'token': 'hatintime-kid'}, {'name': 'furrpopasthetic', 'token': 'furpop'}, {'name': 'RINGAO', 'token': ''}, {'name': 'csgo-awp-texture-map', 'token': 'csgo_awp_texture'}, {'name': 'luinv2', 'token': 'luin-waifu'}, {'name': 'hydrasuit', 'token': 'hydrasuit'}, {'name': 'milady', 'token': 'milady'}, {'name': 'ganyu-genshin-impact', 'token': 'ganyu'}, {'name': 'wayne-reynolds-character', 'token': 'warcharport'}, {'name': 'david-firth-artstyle', 'token': 'david-firth-artstyle'}, {'name': 'seraphimmoonshadow-art', 'token': 'seraphimmoonshadow-art'}, {'name': 'osrstiny', 'token': 'osrstiny'}, {'name': 'lugal-ki-en', 'token': 'lugal-ki-en'}, {'name': 'seamless-ground', 'token': 'seamless-ground'}, {'name': 'sewerslvt', 'token': 'ewerslv'}, {'name': 'diaosu-toy', 'token': 'diaosu-toy'}, {'name': 'sakimi-style', 'token': 'sakimi'}, {'name': 'rj-palmer', 'token': 'rj-palmer'}, {'name': 'harmless-ai-house-style-1', 'token': 'bee-style'}, {'name': 'harmless-ai-1', 'token': 'bee-style'}, {'name': 'yerba-mate', 'token': 'yerba-mate'}, {'name': 'bella-goth', 'token': 'bella-goth'}, {'name': 'bobs-burgers', 'token': 'bobs-burgers'}, {'name': 'jamie-hewlett-style', 'token': 'hewlett'}, {'name': 'belen', 'token': 'belen'}, {'name': 'shvoren-style', 'token': 'shvoren-style'}, {'name': 'gymnastics-leotard-v2', 'token': 'gymnastics-leotard2'}, {'name': 'rd-chaos', 'token': 'rd-chaos'}, {'name': 'armor-concept', 'token': 'armor-concept'}, {'name': 'ouroboros', 'token': 'ouroboros'}, {'name': 'm-geo', 'token': 'm-geo'}, {'name': 'Akitsuki', 'token': ''}, {'name': 'uzumaki', 'token': 'NARUTO'}, {'name': 'sorami-style', 'token': 'sorami-style'}, {'name': 'lxj-o4', 'token': 'csp'}, {'name': 'she-hulk-law-art', 'token': 'shehulk-style'}, {'name': 'led-toy', 'token': 'led-toy'}, {'name': 'durer-style', 'token': 'drr-style'}, {'name': 'hiten-style-nao', 'token': 'hiten-style-nao'}, {'name': 'mechasoulall', 'token': 'mechasoulall'}, {'name': 'wish-artist-stile', 'token': 'wish-style'}, {'name': 'max-foley', 'token': 'max-foley'}, {'name': 'loab-style', 'token': 'loab-style'}, {'name': '3d-female-cyborgs', 'token': 'A female cyborg'}, {'name': 'r-crumb-style', 'token': 'rcrumb'}, {'name': 'paul-noir', 'token': 'paul-noir'}, {'name': 'cgdonny1', 'token': 'donny1'}, {'name': 'valorantstyle', 'token': 'valorant'}, {'name': 'loab-character', 'token': 'loab-character'}, {'name': 'Atako', 'token': ''}, {'name': 'threestooges', 'token': 'threestooges'}, {'name': 'dsmuses', 'token': 'DSmuses'}, {'name': 'fish', 'token': 'fish'}, {'name': 'glass-prism-cube', 'token': 'glass-prism-cube'}, {'name': 'elegant-flower', 'token': 'elegant-flower'}, {'name': 'hanfu-anime-style', 'token': 'hanfu-anime-style'}, {'name': 'green-blue-shanshui', 'token': 'green-blue shanshui'}, {'name': 'lizardman', 'token': 'laceholderTokenLizardma'}, {'name': 'rail-scene', 'token': 'rail-pov'}, {'name': 'lula-13', 'token': 'lula-13'}, {'name': 'laala-character', 'token': 'laala'}, {'name': 'margo', 'token': 'dog-margo'}, {'name': 'carrascharacter', 'token': 'Carras'}, {'name': 'vietstoneking', 'token': 'vietstoneking'}, {'name': 'rhizomuse-machine-bionic-sculpture', 'token': ''}, {'name': 'rcrumb-portraits-style', 'token': 'rcrumb-portraits'}, {'name': 'mu-sadr', 'token': '783463b'}, {'name': 'bozo-22', 'token': 'bozo-22'}, {'name': 'skyfalls', 'token': 'SkyFalls'}, {'name': 'zk', 'token': ''}, {'name': 'tudisco', 'token': 'cat-toy'}, {'name': 'kogecha', 'token': 'kogecha'}, {'name': 'ori-toor', 'token': 'ori-toor'}, {'name': 'isabell-schulte-pviii-style', 'token': 'isabell-schulte-p8-style'}, {'name': 'rilakkuma', 'token': 'rilakkuma'}, {'name': 'indiana', 'token': 'indiana'}, {'name': 'black-and-white-design', 'token': 'PM_style'}, {'name': 'isabell-schulte-pviii-1024px-1500-steps-style', 'token': 'isabell-schulte-p8-style-1024p-1500s'}, {'name': 'fold-structure', 'token': 'fold-geo'}, {'name': 'brunnya', 'token': 'Brunnya'}, {'name': 'jos-de-kat', 'token': 'kat-jos'}, {'name': 'singsing-doll', 'token': 'singsing'}, {'name': 'singsing', 'token': 'singsing'}, {'name': 'isabell-schulte-pviii-12tiles-3000steps-style', 'token': 'isabell-schulte-p8-style-12tiles-3000s'}, {'name': 'f-22', 'token': 'f-22'}, {'name': 'jin-kisaragi', 'token': 'jin-kisaragi'}, {'name': 'depthmap-style', 'token': 'depthmap'}, {'name': 'crested-gecko', 'token': 'crested-gecko'}, {'name': 'grisstyle', 'token': 'gris'}, {'name': 'ikea-fabler', 'token': 'ikea-fabler'}, {'name': 'joe-mad', 'token': 'joe-mad'}, {'name': 'boissonnard', 'token': 'boissonnard'}, {'name': 'overprettified', 'token': 'overprettified'}, {'name': 'all-rings-albuns', 'token': 'rings-all-albuns'}, {'name': 'shiny-polyman', 'token': 'shiny-polyman'}, {'name': 'scarlet-witch', 'token': 'sw-mom'}, {'name': 'wojaks-now', 'token': 'red-wojak'}, {'name': 'carasibana', 'token': 'carasibana'}, {'name': 'towerplace', 'token': 'TowerPlace'}, {'name': 'cumbia-peruana', 'token': 'cumbia-peru'}, {'name': 'bloo', 'token': 'owl-guy'}, {'name': 'dog-django', 'token': 'dog-django'}, {'name': 'facadeplace', 'token': 'FacadePlace'}, {'name': 'blue-zombie', 'token': 'blue-zombie'}, {'name': 'blue-zombiee', 'token': 'blue-zombie'}, {'name': 'jinjoon-lee-they', 'token': 'jinjoon_lee_they'}, {'name': 'ralph-mcquarrie', 'token': 'ralph-mcquarrie'}, {'name': 'hiyuki-chan', 'token': 'hiyuki-chan'}, {'name': 'isabell-schulte-pviii-4tiles-6000steps', 'token': 'isabell-schulte-p8-style-4tiles-6000s'}, {'name': 'liliana', 'token': 'liliana'}, {'name': 'morino-hon-style', 'token': 'morino-hon'}, {'name': 'artist-yukiko-kanagai', 'token': 'Yukiko Kanagai '}, {'name': 'wheatland', 'token': ''}, {'name': 'm-geoo', 'token': 'm-geo'}, {'name': 'wheatland-arknight', 'token': 'golden-wheats-fields'}, {'name': 'mokoko', 'token': 'mokoko'}, {'name': '001glitch-core', 'token': '01glitch_cor'}, {'name': 'stardew-valley-pixel-art', 'token': 'pixelart-stardew'}, {'name': 'isabell-schulte-pviii-4tiles-500steps', 'token': 'isabell-schulte-p8-style-4tiles-500s'}, {'name': 'anime-girl', 'token': 'anime-girl'}, {'name': 'heather', 'token': 'eather'}, {'name': 'rail-scene-style', 'token': 'rail-pov'}, {'name': 'quiesel', 'token': 'quiesel'}, {'name': 'matthew-stone', 'token': 'atthew-ston'}, {'name': 'dreamcore', 'token': 'dreamcore'}, {'name': 'pokemon-conquest-sprites', 'token': 'poke-conquest'}, {'name': 'tili-concept', 'token': 'tili'}, {'name': 'nouns-glasses', 'token': 'nouns glasses'}, {'name': 'shigure-ui-style', 'token': 'shigure-ui'}, {'name': 'pen-ink-portraits-bennorthen', 'token': 'ink-portrait-by-BenNorthern'}, {'name': 'nikodim', 'token': 'nikodim'}, {'name': 'ori', 'token': 'Ori'}, {'name': 'anya-forger', 'token': 'anya-forger'}, {'name': 'lavko', 'token': 'lavko'}, {'name': 'fasina', 'token': 'Fasina'}, {'name': 'uma-clean-object', 'token': 'uma-clean-object'}, {'name': 'wojaks-now-now-now', 'token': 'red-wojak'}, {'name': 'memnarch-mtg', 'token': 'mtg-memnarch'}, {'name': 'tonal1', 'token': 'Tonal'}, {'name': 'tesla-bot', 'token': 'tesla-bot'}, {'name': 'red-glasses', 'token': 'red-glasses'}, {'name': 'csgo-awp-object', 'token': 'csgo_awp'}, {'name': 'stretch-re1-robot', 'token': 'stretch'}, {'name': 'isabell-schulte-pv-pvii-3000steps', 'token': 'isabell-schulte-p5-p7-style-3000s'}, {'name': 'insidewhale', 'token': 'InsideWhale'}, {'name': 'noggles', 'token': 'noggles'}, {'name': 'isometric-tile-test', 'token': 'iso-tile'}, {'name': 'bamse-og-kylling', 'token': 'bamse-kylling'}, {'name': 'marbling-art', 'token': 'marbling-art'}, {'name': 'joemad', 'token': 'joemad'}, {'name': 'bamse', 'token': 'bamse'}, {'name': 'dq10-anrushia', 'token': 'anrushia'}, {'name': 'test', 'token': 'AIO'}, {'name': 'naoki-saito', 'token': 'naoki_saito'}, {'name': 'raichu', 'token': 'raichu'}, {'name': 'child-zombie', 'token': 'child-zombie'}, {'name': 'yf21', 'token': 'YF21'}, {'name': 'titan-robot', 'token': 'titan'}, {'name': 'cyberpunk-lucy', 'token': 'cyberpunk-lucy'}, {'name': 'giygas', 'token': 'giygas'}, {'name': 'david-martinez-cyberpunk', 'token': 'david-martinez-cyberpunk'}, {'name': 'phan-s-collage', 'token': 'pcollage'}, {'name': 'jojo-bizzare-adventure-manga-lineart', 'token': 'JoJo_lineart'}, {'name': 'homestuck-sprite', 'token': 'homestuck-sprite'}, {'name': 'kogatan-shiny', 'token': 'ogata'}, {'name': 'moo-moo', 'token': 'moomoo'}, {'name': 'detectivedinosaur1', 'token': 'dd1'}, {'name': 'arcane-face', 'token': 'arcane-face'}, {'name': 'sherhook-painting', 'token': 'sherhook'}, {'name': 'isabell-schulte-pviii-1-image-style', 'token': 'isabell-schulte-p8-1-style'}, {'name': 'dicoo2', 'token': 'dicoo'}, {'name': 'hrgiger-drmacabre', 'token': 'barba'}, {'name': 'babau', 'token': 'babau'}, {'name': 'darkplane', 'token': 'DarkPlane'}, {'name': 'wildkat', 'token': 'wildkat'}, {'name': 'half-life-2-dog', 'token': 'hl-dog'}, {'name': 'outfit-items', 'token': 'outfit-items'}, {'name': 'midjourney-style', 'token': 'midjourney-style'}, {'name': 'puerquis-toy', 'token': 'puerquis'}, {'name': 'maus', 'token': 'Maus'}, {'name': 'jetsetdreamcastcovers', 'token': 'jet'}, {'name': 'karan-gloomy', 'token': 'karan'}, {'name': 'yoji-shinkawa-style', 'token': 'yoji-shinkawa'}, {'name': 'million-live-akane-15k', 'token': 'akane'}, {'name': 'million-live-akane-3k', 'token': 'akane'}, {'name': 'sherhook-painting-v2', 'token': 'sherhook'}, {'name': 'gba-pokemon-sprites', 'token': 'GBA-Poke-Sprites'}, {'name': 'gim', 'token': 'grimes-album-style'}, {'name': 'char-con', 'token': 'char-con'}, {'name': 'bluebey', 'token': 'bluebey'}, {'name': 'homestuck-troll', 'token': 'homestuck-troll'}, {'name': 'million-live-akane-shifuku-3k', 'token': 'akane'}, {'name': 'thegeneral', 'token': 'bobknight'}, {'name': 'million-live-spade-q-object-3k', 'token': 'spade_q'}, {'name': 'million-live-spade-q-style-3k', 'token': 'spade_q'}, {'name': 'ibere-thenorio', 'token': 'ibere-thenorio'}, {'name': 'yinit', 'token': 'init-dropca'}, {'name': 'bee', 'token': 'b-e-e'}, {'name': 'pixel-mania', 'token': 'pixel-mania'}, {'name': 'sunfish', 'token': 'SunFish'}, {'name': 'test2', 'token': 'AIOCARD'}, {'name': 'pool-test', 'token': 'pool_test'}, {'name': 'mokoko-seed', 'token': 'mokoko-seed'}, {'name': 'isabell-schulte-pviii-4-tiles-1-lr-3000-steps-style', 'token': 'isabell-schulte-p8-4tiles-1lr-300s-style'}, {'name': 'ghostproject-men', 'token': 'ghostsproject-style'}, {'name': 'phan', 'token': 'phan'}, {'name': 'chen-1', 'token': 'chen-1'}, {'name': 'bluebey-2', 'token': 'bluebey'}, {'name': 'waterfallshadow', 'token': 'WaterfallShadow'}, {'name': 'chop', 'token': 'Le Petit Prince'}, {'name': 'sintez-ico', 'token': 'sintez-ico'}, {'name': 'carlitos-el-mago', 'token': 'carloscarbonell'}, {'name': 'david-martinez-edgerunners', 'token': 'david-martinez-edgerunners'}, {'name': 'isabell-schulte-pviii-4-tiles-3-lr-5000-steps-style', 'token': 'isabell-schulte-p8-4tiles-3lr-5000s-style'}, {'name': 'guttestreker', 'token': 'guttestreker'}, {'name': 'ransom', 'token': 'ransom'}, {'name': 'museum-by-coop-himmelblau', 'token': 'coop himmelblau museum'}, {'name': 'coop-himmelblau', 'token': 'coop himmelblau'}, {'name': 'yesdelete', 'token': 'yesdelete'}, {'name': 'conway-pirate', 'token': 'conway'}, {'name': 'ilo-kunst', 'token': 'ilo-kunst'}, {'name': 'yilanov2', 'token': 'yilanov'}, {'name': 'dr-strange', 'token': 'dr-strange'}, {'name': 'hubris-oshri', 'token': 'Hubris'}, {'name': 'osaka-jyo', 'token': 'osaka-jyo'}, {'name': 'paolo-bonolis', 'token': 'paolo-bonolis'}, {'name': 'repeat', 'token': 'repeat'}, {'name': 'geggin', 'token': 'geggin'}, {'name': 'lex', 'token': 'lex'}, {'name': 'osaka-jyo2', 'token': 'osaka-jyo2'}, {'name': 'owl-house', 'token': 'owl-house'}, {'name': 'nazuna', 'token': 'nazuna'}, {'name': 'thorneworks', 'token': 'Thorneworks'}, {'name': 'kysa-v-style', 'token': 'kysa-v-style'}, {'name': 'senneca', 'token': 'Senneca'}, {'name': 'zero-suit-samus', 'token': 'zero-suit-samus'}, {'name': 'kanv1', 'token': 'KAN'}, {'name': 'dlooak', 'token': 'dlooak'}, {'name': 'wire-angels', 'token': 'wire-angels'}, {'name': 'mizkif', 'token': 'mizkif'}, {'name': 'brittney-williams-art', 'token': 'Brittney_Williams'}, {'name': 'wheelchair', 'token': 'wheelchair'}, {'name': 'yuji-himukai-style', 'token': 'Yuji Himukai-Style'}, {'name': 'cindlop', 'token': 'cindlop'}, {'name': 'sas-style', 'token': 'smooth-aesthetic-style'}, {'name': 'remert', 'token': 'Remert'}, {'name': 'alex-portugal', 'token': 'alejandro-portugal'}, {'name': 'explosions-cat', 'token': 'explosions-cat'}, {'name': 'onzpo', 'token': 'onzpo'}, {'name': 'eru-chitanda-casual', 'token': 'c-eru-chitanda'}, {'name': 'poring-ragnarok-online', 'token': 'poring-ro'}, {'name': 'cg-bearded-man', 'token': 'LH-Keeper'}, {'name': 'ba-shiroko', 'token': 'shiroko'}, {'name': 'at-wolf-boy-object', 'token': 'AT-Wolf-Boy-Object'}, {'name': 'fairytale', 'token': 'fAIrytale'}, {'name': 'kira-sensei', 'token': 'kira-sensei'}, {'name': 'kawaii-girl-plus-style', 'token': 'kawaii_girl'}, {'name': 'kawaii-girl-plus-object', 'token': 'kawaii_girl'}, {'name': 'boris-anderson', 'token': 'boris-anderson'}, {'name': 'medazzaland', 'token': 'edazzalan'}, {'name': 'duranduran', 'token': 'uranDura'}, {'name': 'crbart', 'token': 'crbart'}, {'name': 'happy-person12345', 'token': 'Happy-Person12345'}, {'name': 'fzk', 'token': 'fzk'}, {'name': 'rishusei-style', 'token': 'crishusei-style'}, {'name': 'felps', 'token': 'Felps'}, {'name': 'plen-ki-mun', 'token': 'plen-ki-mun'}, {'name': 'babs-bunny', 'token': 'babs_bunny'}, {'name': 'james-web-space-telescope', 'token': 'James-Web-Telescope'}, {'name': 'blue-haired-boy', 'token': 'Blue-Haired-Boy'}, {'name': '80s-anime-ai', 'token': '80s-anime-AI'}, {'name': 'spider-gwen', 'token': 'spider-gwen'}, {'name': 'takuji-kawano', 'token': 'takuji-kawano'}, {'name': 'fractal-temple-style', 'token': 'fractal-temple'}, {'name': 'sanguo-guanyu', 'token': 'sanguo-guanyu'}, {'name': 's1m-naoto-ohshima', 'token': 's1m-naoto-ohshima'}, {'name': 'kawaii-girl-plus-style-v1-1', 'token': 'kawaii'}, {'name': 'nathan-wyatt', 'token': 'Nathan-Wyatt'}, {'name': 'kasumin', 'token': 'kasumin'}, {'name': 'happy-person12345-assets', 'token': 'Happy-Person12345-assets'}, {'name': 'oleg-kuvaev', 'token': 'oleg-kuvaev'}, {'name': 'kanovt', 'token': 'anov'}, {'name': 'lphr-style', 'token': 'lphr-style'}, {'name': 'concept-art', 'token': 'concept-art'}, {'name': 'trust-support', 'token': 'trust'}, {'name': 'altyn-helmet', 'token': 'Altyn'}, {'name': '80s-anime-ai-being', 'token': 'anime-AI-being'}, {'name': 'baluchitherian', 'token': 'baluchiter'}, {'name': 'pineda-david', 'token': 'pineda-david'}, {'name': 'ohisashiburi-style', 'token': 'ohishashiburi-style'}, {'name': 'crb-portraits', 'token': 'crbportrait'}, {'name': 'i-love-chaos', 'token': 'chaos'}, {'name': 'alex-thumbnail-object-2000-steps', 'token': 'alex'}, {'name': '852style-girl', 'token': '852style-girl'}, {'name': 'nomad', 'token': 'nomad'}, {'name': 'new-priests', 'token': 'new-priest'}, {'name': 'liminalspaces', 'token': 'liminal image'}, {'name': 'aadhav-face', 'token': 'aadhav-face'}, {'name': 'jang-sung-rak-style', 'token': 'Jang-Sung-Rak-style'}, {'name': 'mattvidpro', 'token': 'mattvidpro'}, {'name': 'chungus-poodl-pet', 'token': 'poodl-chungus-big'}, {'name': 'liminal-spaces-2-0', 'token': 'iminal imag'}, {'name': 'crb-surrealz', 'token': 'crbsurreal'}, {'name': 'final-fantasy-logo', 'token': 'final-fantasy-logo'}, {'name': 'canadian-goose', 'token': 'canadian-goose'}, {'name': 'scratch-project', 'token': 'scratch-project'}, {'name': 'lazytown-stephanie', 'token': 'azytown-stephani'}, {'name': 'female-kpop-singer', 'token': 'female-kpop-star'}, {'name': 'aleyna-tilki', 'token': 'aleyna-tilki'}, {'name': 'other-mother', 'token': 'ther-mothe'}, {'name': 'beldam', 'token': 'elda'}, {'name': 'button-eyes', 'token': 'utton-eye'}, {'name': 'alisa', 'token': 'alisa-selezneva'}, {'name': 'im-poppy', 'token': 'm-popp'}, {'name': 'fractal-flame', 'token': 'fractal-flame'}, {'name': 'Exodus-Styling', 'token': 'Exouds-Style'}, {'name': '8sconception', 'token': '80s-car'}, {'name': 'christo-person', 'token': 'christo'}, {'name': 'slm', 'token': 'c-w388'}, {'name': 'meze-audio-elite-headphones', 'token': 'meze-elite'}, {'name': 'fox-purple', 'token': 'foxi-purple'}, {'name': 'roblox-avatar', 'token': 'roblox-avatar'}, {'name': 'toy-bonnie-plush', 'token': 'toy-bonnie-plush'}, {'name': 'alf', 'token': 'alf'}, {'name': 'wojak', 'token': 'oja'}, {'name': 'animalve3-1500seq', 'token': 'diodio'}, {'name': 'muxoyara', 'token': 'muxoyara'}, {'name': 'selezneva-alisa', 'token': 'selezneva-alisa'}, {'name': 'ayush-spider-spr', 'token': 'spr-mn'}, {'name': 'natasha-johnston', 'token': 'natasha-johnston'}, {'name': 'nard-style', 'token': 'nard'}, {'name': 'kirby', 'token': 'kirby'}, {'name': 'el-salvador-style-style', 'token': 'el-salvador-style'}, {'name': 'rahkshi-bionicle', 'token': 'rahkshi-bionicle'}, {'name': 'masyanya', 'token': 'masyanya'}, {'name': 'command-and-conquer-remastered-cameos', 'token': 'command_and_conquer_remastered_cameos'}, {'name': 'lucario', 'token': 'lucario'}, {'name': 'bruma', 'token': 'Bruma-the-cat'}, {'name': 'nissa-revane', 'token': 'nissa-revane'}, {'name': 'tamiyo', 'token': 'tamiyo'}, {'name': 'pascalsibertin', 'token': 'pascalsibertin'}, {'name': 'chandra-nalaar', 'token': 'chandra-nalaar'}, {'name': 'sam-yang', 'token': 'sam-yang'}, {'name': 'kiora', 'token': 'kiora'}, {'name': 'wedding', 'token': 'wedding1'}, {'name': 'arwijn', 'token': 'rwij'}, {'name': 'gba-fe-class-cards', 'token': 'lasscar'}, {'name': 'painted-by-silver-of-999', 'token': 'cat-toy'}, {'name': 'painted-by-silver-of-999-2', 'token': 'girl-painted-by-silver-of-999'}, {'name': 'toyota-sera', 'token': 'toyota-sera'}, {'name': 'vraska', 'token': 'vraska'}, {'name': 'mystical-nature', 'token': ''}, {'name': 'cartoona-animals', 'token': 'cartoona-animals'}, {'name': 'amogus', 'token': 'amogus'}, {'name': 'kinda-sus', 'token': 'amogus'}, {'name': 'xuna', 'token': 'Xuna'}, {'name': 'pion-by-august-semionov', 'token': 'pion'}, {'name': 'rikiart', 'token': 'rick-art'}, {'name': 'jacqueline-the-unicorn', 'token': 'jacqueline'}, {'name': 'flaticon-lineal-color', 'token': 'flaticon-lineal-color'}, {'name': 'test-epson', 'token': 'epson-branch'}, {'name': 'orientalist-art', 'token': 'orientalist-art'}, {'name': 'ki', 'token': 'ki-mars'}, {'name': 'fnf-boyfriend', 'token': 'fnf-boyfriend'}, {'name': 'phoenix-01', 'token': 'phoenix-style'}, {'name': 'society-finch', 'token': 'society-finch'}, {'name': 'rikiboy-art', 'token': 'Rikiboy-Art'}, {'name': 'flatic', 'token': 'flat-ct'}, {'name': 'logo-with-face-on-shield', 'token': 'logo-huizhang'}, {'name': 'elspeth-tirel', 'token': 'elspeth-tirel'}, {'name': 'zero', 'token': 'zero'}, {'name': 'willy-hd', 'token': 'willy_character'}, {'name': 'kaya-ghost-assasin', 'token': 'kaya-ghost-assasin'}, {'name': 'starhavenmachinegods', 'token': 'StarhavenMachineGods'}, {'name': 'namine-ritsu', 'token': 'namine-ritsu'}, {'name': 'mildemelwe-style', 'token': 'mildemelwe'}, {'name': 'nahiri', 'token': 'nahiri'}, {'name': 'ghost-style', 'token': 'ghost'}, {'name': 'arq-render', 'token': 'arq-style'}, {'name': 'saheeli-rai', 'token': 'saheeli-rai'}, {'name': 'youpi2', 'token': 'youpi'}, {'name': 'youtooz-candy', 'token': 'youtooz-candy'}, {'name': 'beholder', 'token': 'beholder'}, {'name': 'progress-chip', 'token': 'progress-chip'}, {'name': 'lofa', 'token': 'lofa'}, {'name': 'huatli', 'token': 'huatli'}, {'name': 'vivien-reid', 'token': 'vivien-reid'}, {'name': 'wedding-HandPainted', 'token': ''}, {'name': 'sims-2-portrait', 'token': 'sims2-portrait'}, {'name': 'flag-ussr', 'token': 'flag-ussr'}, {'name': 'cortana', 'token': 'cortana'}, {'name': 'azura-from-vibrant-venture', 'token': 'azura'}, {'name': 'liliana-vess', 'token': 'liliana-vess'}, {'name': 'dreamy-painting', 'token': 'dreamy-painting'}, {'name': 'munch-leaks-style', 'token': 'munch-leaks-style'}, {'name': 'gta5-artwork', 'token': 'gta5-artwork'}, {'name': 'xioboma', 'token': 'xi-obama'}, {'name': 'ashiok', 'token': 'ashiok'}, {'name': 'Aflac-duck', 'token': 'aflac duck'}, {'name': 'toho-pixel', 'token': 'toho-pixel'}, {'name': 'alicebeta', 'token': 'Alice-style'}, {'name': 'cute-game-style', 'token': 'cute-game-style'}, {'name': 'a-yakimova', 'token': 'a-yakimova'}, {'name': 'anime-background-style', 'token': 'anime-background-style'}, {'name': 'uliana-kudinova', 'token': 'liana-kudinov'}, {'name': 'msg', 'token': 'MSG69'}, {'name': 'gio', 'token': 'gio-single'}, {'name': 'smooth-pencils', 'token': ''}, {'name': 'pintu', 'token': 'pintu-dog'}, {'name': 'marty6', 'token': 'marty6'}, {'name': 'marty', 'token': 'marty'}, {'name': 'xi', 'token': 'JinpingXi'}, {'name': 'captainkirb', 'token': 'captainkirb'}, {'name': 'urivoldemort', 'token': 'uriboldemort'}, {'name': 'anime-background-style-v2', 'token': 'anime-background-style-v2'}, {'name': 'hk-peach', 'token': 'hk-peach'}, {'name': 'hk-goldbuddha', 'token': 'hk-goldbuddha'}, {'name': 'edgerunners-style', 'token': 'edgerunners-style-av'}, {'name': 'warhammer-40k-drawing-style', 'token': 'warhammer40k-drawing-style'}, {'name': 'hk-opencamera', 'token': 'hk-opencamera'}, {'name': 'hk-breakfast', 'token': 'hk-breakfast'}, {'name': 'iridescent-illustration-style', 'token': 'iridescent-illustration-style'}, {'name': 'edgerunners-style-v2', 'token': 'edgerunners-style-av-v2'}, {'name': 'leif-jones', 'token': 'leif-jones'}, {'name': 'hk-buses', 'token': 'hk-buses'}, {'name': 'hk-goldenlantern', 'token': 'hk-goldenlantern'}, {'name': 'hk-hkisland', 'token': 'hk-hkisland'}, {'name': 'hk-leaves', 'token': ''}, {'name': 'hk-oldcamera', 'token': 'hk-oldcamera'}, {'name': 'frank-frazetta', 'token': 'rank franzett'}, {'name': 'obama-based-on-xi', 'token': 'obama> <JinpingXi'}, {'name': 'hk-vintage', 'token': ''}, {'name': 'degods', 'token': 'degods'}, {'name': 'dishonored-portrait-styles', 'token': 'portrait-style-dishonored'}, {'name': 'manga-style', 'token': 'manga'}, {'name': 'degodsheavy', 'token': 'degods-heavy'}, {'name': 'teferi', 'token': 'teferi'}, {'name': 'car-toy-rk', 'token': 'car-toy'}, {'name': 'anders-zorn', 'token': 'anders-zorn'}, {'name': 'rayne-weynolds', 'token': 'rayne-weynolds'}, {'name': 'hk-bamboo', 'token': 'hk-bamboo'}, {'name': 'hk-betweenislands', 'token': 'hk-betweenislands'}, {'name': 'hk-bicycle', 'token': 'hk-bicycle'}, {'name': 'hk-blackandwhite', 'token': 'hk-blackandwhite'}, {'name': 'pjablonski-style', 'token': 'pjablonski-style'}, {'name': 'hk-market', 'token': 'hk-market'}, {'name': 'hk-phonevax', 'token': 'hk-phonevax'}, {'name': 'hk-clouds', 'token': 'hk-cloud'}, {'name': 'hk-streetpeople', 'token': 'hk-streetpeople'}, {'name': 'iridescent-photo-style', 'token': 'iridescent-photo-style'}, {'name': 'color-page', 'token': 'coloring-page'}, {'name': 'hoi4-leaders', 'token': 'HOI4-Leader'}, {'name': 'franz-unterberger', 'token': 'franz-unterberger'}, {'name': 'angus-mcbride-style', 'token': 'angus-mcbride-style'}, {'name': 'happy-chaos', 'token': 'happychaos'}, {'name': 'gt-color-paint-2', 'token': 'my-color-paint-GT'}, {'name': 'smurf-style', 'token': 'smurfy'}, {'name': 'coraline', 'token': 'coraline'}, {'name': 'terraria-style', 'token': 'terr-sty'}, {'name': 'ettblackteapot', 'token': 'my-teapot'}, {'name': 'gibasachan-v0.1', 'token': 'gibasachan'}, {'name': 'kodakvision500t', 'token': 'kodakvision_500T'}, {'name': 'obama-based-on-xi', 'token': 'obama'}, {'name': 'obama-self-2', 'token': 'Obama'}, {'name': 'bob-dobbs', 'token': 'bob'}, {'name': 'ahx-model-1', 'token': 'ivan-stripes'}, {'name': 'ahx-model-2', 'token': 'artist'}, {'name': 'beetlejuice-cartoon-style', 'token': 'beetlejuice-cartoon'}, {'name': 'pokemon-modern-artwork', 'token': 'pkmn-modern'}, {'name': 'pokemon-classic-artwork', 'token': 'pkmn-classic'}, {'name': 'pokemon-gens-1-to-8', 'token': 'pkmn-galar'}, {'name': 'pokemon-rgby-sprite', 'token': 'pkmn-rgby'}, {'name': 'max-twain', 'token': 'max-twain'}, {'name': 'ihylc', 'token': 'ihylc'}, {'name': 'test-man', 'token': 'Test-man'}, {'name': 'tron-style', 'token': 'tron-style>'}, {'name': 'dulls', 'token': 'dulls-avatar'}, {'name': 'vie-proceres', 'token': 'vie-proceres'}, {'name': 'dovin-baan', 'token': 'dovin-baan'}, {'name': 'polki-jewellery', 'token': 'ccess to model sd-concepts-library/polki-jewellery is restricted and you are not in the authorized list. Visit https://huggingface.co/sd-concepts-library/polki-jewellery to ask for access'}, {'name': 'dog2', 'token': 'ccess to model sd-concepts-library/dog2 is restricted and you are not in the authorized list. Visit https://huggingface.co/sd-concepts-library/dog2 to ask for access'}, {'name': 'caitlin-fairchild-character-gen13-comics-by-j-scott-campbell', 'token': 'Caitlin-Fairchild'}, {'name': 'ugly-sonic', 'token': 'ugly-sonic'}, {'name': 'utopia-beer-mat', 'token': 'utopia-beer-mat'}, {'name': 'old-brno', 'token': 'old-brno'}, {'name': 'moka-pot', 'token': 'moka-pot'}, {'name': 'brno-trenck', 'token': 'brno-trenck'}, {'name': 'brno-tram', 'token': 'brno-tram'}, {'name': 'brno-obasa', 'token': 'brno-obasa'}, {'name': 'brno-night', 'token': 'brno-night'}, {'name': 'brno-dorm', 'token': 'brno-dorm'}, {'name': 'brno-busstop', 'token': 'brno-busstop'}, {'name': 'twitch-league-of-legends', 'token': 'twitch-lol'}, {'name': 'fp-shop2', 'token': 'fp-shop2'}, {'name': 'fp-shop1', 'token': 'fp-shop1'}, {'name': 'fp-content-b', 'token': 'fp-content-b'}, {'name': 'fp-content-a', 'token': 'fp-content-a'}, {'name': 'fp-city', 'token': 'fp-city'}, {'name': 'brno-city-results', 'token': 'brno-city-results'}, {'name': 'brno-city', 'token': 'brno-city'}, {'name': 'brno-chair-results', 'token': 'brno-chair-results'}, {'name': 'brno-chair', 'token': 'brno-chair'}, {'name': 'manga-char-nov-23', 'token': 'char-nov23'}, {'name': 'manga-nov-23', 'token': 'manga-characters-nov23'}, {'name': 'yellow-cockatiel-parrot', 'token': 'rosa-popugai'}, {'name': 'dreams', 'token': 'meeg'}, {'name': 'alberto-montt', 'token': 'AlbertoMontt'}, {'name': 'tooth-wu', 'token': 'tooth-wu'}, {'name': 'filename-2', 'token': 'filename2'}, {'name': 'iridescent-photo-style', 'token': 'iridescent-photo-style'}, {'name': 'bored-ape-textual-inversion', 'token': 'bored_ape'}, {'name': 'ghibli-face', 'token': 'ghibli-face'}, {'name': 'yoshimurachi', 'token': 'yoshi-san'}, {'name': 'jm-bergling-monogram', 'token': 'JM-Bergling-monogram'}, {'name': '4tnght', 'token': '4tNGHT'}, {'name': 'dancing-cactus', 'token': 'dancing-cactus'}, {'name': 'yolandi-visser', 'token': 'olandi-visse'}, {'name': 'zizigooloo', 'token': 'zizigooloo'}, {'name': 'princess-knight-art', 'token': 'princess-knight'}, {'name': 'belle-delphine', 'token': 'elle-delphin'}, {'name': 'cancer_style', 'token': 'cancer_style'}, {'name': 'trypophobia', 'token': 'rypophobi'}, {'name': 'incendegris-grey', 'token': 'incendegris-grey'}, {'name': 'fairy-tale-painting-style', 'token': 'fairy-tale-painting-style'}, {'name': 'arcimboldo-style', 'token': 'arcimboldo-style'}, {'name': 'xidiversity', 'token': 'JinpingXi'}, {'name': 'obama-based-on-xi', 'token': 'obama'}, {'name': 'zero-bottle', 'token': 'zero-bottle'}, {'name': 'victor-narm', 'token': 'victor-narm'}, {'name': 'supitcha-mask', 'token': 'supitcha-mask'}, {'name': 'smarties', 'token': 'smarties'}, {'name': 'rico-face', 'token': 'rico-face'}, {'name': 'rex-deno', 'token': 'rex-deno'}, {'name': 'abby-face', 'token': 'abby-face'}, {'name': 'nic-papercuts', 'token': 'nic-papercuts'}]


def get_concept(name):
  for con in concepts:
      if con['name'] == name:
        return con
  return {'name':'', 'token':''}

def get_conceptualizer(page):
    from huggingface_hub import hf_hub_download
    from diffusers import StableDiffusionPipeline
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
    from transformers import CLIPFeatureExtractor, CLIPTextModel, CLIPTokenizer
    global pipe_conceptualizer
    repo_id_embeds = f"sd-concepts-library/{prefs['concepts_model']}"
    embeds_url = "" #Add the URL or path to a learned_embeds.bin file in case you have one
    placeholder_token_string = "" #Add what is the token string in case you are uploading your own embed

    downloaded_embedding_folder = os.path.join(root_dir, "downloaded_embedding")
    if not os.path.exists(downloaded_embedding_folder):
      os.mkdir(downloaded_embedding_folder)
    try:
      if(not embeds_url):
        embeds_path = hf_hub_download(repo_id=repo_id_embeds, filename="learned_embeds.bin")
        token_path = hf_hub_download(repo_id=repo_id_embeds, filename="token_identifier.txt")
        shutil.copy(embeds_path, downloaded_embedding_folder)
        shutil.copy(token_path, downloaded_embedding_folder)
        with open(f'{downloaded_embedding_folder}/token_identifier.txt', 'r') as file:
          placeholder_token_string = file.read()
      else:
        run_sp(f"wget -q -O {downloaded_embedding_folder}/learned_embeds.bin {embeds_url}")
        #!wget -q -O $downloaded_embedding_folder/learned_embeds.bin $embeds_url
    except Exception as e:
      alert_msg(page, f"Error getting concept. May need to accept model at https://huggingface.co/sd-concepts-library/{prefs['concepts_model']}", content=Text(e))
      return
    learned_embeds_path = f"{downloaded_embedding_folder}/learned_embeds.bin"
    tokenizer = CLIPTokenizer.from_pretrained(model_path, subfolder="tokenizer")
    text_encoder = CLIPTextModel.from_pretrained(model_path, subfolder="text_encoder", torch_dtype=torch.float16)
    def load_learned_embed_in_clip(learned_embeds_path, text_encoder, tokenizer, token=None):
      loaded_learned_embeds = torch.load(learned_embeds_path, map_location="cpu")
      trained_token = list(loaded_learned_embeds.keys())[0]
      embeds = loaded_learned_embeds[trained_token]
      dtype = text_encoder.get_input_embeddings().weight.dtype
      embeds.to(dtype)
      token = token if token is not None else trained_token
      num_added_tokens = tokenizer.add_tokens(token)
      if num_added_tokens == 0:
        alert_msg(page, f"The tokenizer already contains the token {token}. Please pass a different `token` that is not already in the tokenizer.")
        return
      text_encoder.resize_token_embeddings(len(tokenizer))
      token_id = tokenizer.convert_tokens_to_ids(token)
      text_encoder.get_input_embeddings().weight.data[token_id] = embeds
    try:
      load_learned_embed_in_clip(learned_embeds_path, text_encoder, tokenizer)
    except Exception as e:
      alert_msg(page, f"Error Loading Concept", content=Text(e))
      return
    pipe_conceptualizer = StableDiffusionPipeline.from_pretrained(
        model_path,
        revision="fp16",
        torch_dtype=torch.float16,
        text_encoder=text_encoder,
        tokenizer=tokenizer,
        cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None,
        safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
    )
    pipe_conceptualizer = optimize_pipe(pipe_conceptualizer, vae=False)
    pipe_conceptualizer.set_progress_bar_config(disable=True)
    pipe_conceptualizer = pipe_conceptualizer.to(torch_device)
    return pipe_conceptualizer

def get_dreamfusion(page):
    os.chdir(root_dir)
    run_process("git clone https://github.com/ashawkey/stable-dreamfusion.git -q", page=page)
    os.chdir(os.path.join(root_dir, "stable-dreamfusion"))
    run_process("pip install -r requirements.txt -q", page=page)
    run_process("pip install git+https://github.com/NVlabs/nvdiffrast/ -q", page=page)
    os.chdir(root_dir)
    
def run_dreamfusion(page):
    global dreamfusion_prefs, status
    def add_to_dreamfusion_output(o):
      page.dreamfusion_output.controls.append(o)
      page.dreamfusion_output.update()
    def clear_last():
      #page.dreamfusion_output.controls = []
      del page.dreamfusion_output.controls[-1]
      page.dreamfusion_output.update()
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install HuggingFace Diffusers Pipeline before running...")
      return
    if not bool(dreamfusion_prefs["prompt_text"].strip()):
      alert_msg(page, "You must enter a simple prompt to generate 3D model from...")
      return
    page.dreamfusion_output.controls = []
    page.dreamfusion_output.update()
    if not status['installed_dreamfusion']:
      add_to_dreamfusion_output(Row([ProgressRing(), Text("Installing Stable DreamFusion 3D Pipeline...", weight=FontWeight.BOLD)]))
      get_dreamfusion(page)
      status['installed_dreamfusion'] = True
      clear_last()
    def convert(seconds):
      seconds = seconds % (24 * 3600)
      hour = seconds // 3600
      seconds %= 3600
      minutes = seconds // 60
      seconds %= 60
      return "%d:%02d" % (hour, minutes)
    estimate = convert(int(dreamfusion_prefs["training_iters"] * 0.7))
    add_to_dreamfusion_output(Text("Generating your 3D model, this'll take a while...  Estimating " + estimate))
    add_to_dreamfusion_output(ProgressBar())
    df_path = os.path.join(root_dir, "stable-dreamfusion")
    os.chdir(df_path)
    run_str = f'python main.py -O --text "{dreamfusion_prefs["prompt_text"]}" --workspace {dreamfusion_prefs["workspace"]} --iters {dreamfusion_prefs["training_iters"]} --lr {dreamfusion_prefs["learning_rate"]} --w {dreamfusion_prefs["training_nerf_resolution"]} --h {dreamfusion_prefs["training_nerf_resolution"]} --seed {dreamfusion_prefs["seed"]} --lambda_entropy {dreamfusion_prefs["lambda_entropy"]} --ckpt {dreamfusion_prefs["checkpoint"]} --save_mesh --max_steps {dreamfusion_prefs["max_steps"]}'
    print(run_str)
    torch.cuda.empty_cache()
    try:
      run_process(run_str, page=page)
    except:
      clear_last()
      alert_msg(page, "Error running DreamFusion, probably Out of Memory. Adjust settings & try again.")
      return
    clear_last()
    add_to_dreamfusion_output(Text("Finished generating obj model, texture and video... Hope it's good."))
    df_out = os.path.join(df_path, dreamfusion_prefs["workspace"])
    if storage_type == "Colab Google Drive":
      dreamfusion_out = os.path.join(prefs['image_output'].rpartition(slash)[0], 'dreamfusion_out', dreamfusion_prefs["workspace"])
      #os.makedirs(dreamfusion_out, exist_ok=True)
      if os.path.exists(dreamfusion_out):
        dreamfusion_out = available_folder(os.path.join(prefs['image_output'].rpartition(slash)[0], 'dreamfusion_out'), dreamfusion_prefs["workspace"], 1)
      shutil.copytree(df_out, dreamfusion_out)
      add_to_dreamfusion_output(Text(f"Saved to {dreamfusion_out}"))
    else:
      add_to_dreamfusion_output(Text(f"Saved to {df_out}"))
    # TODO: PyDrive2
    if prefs['enable_sounds']: page.snd_alert.play()
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
def clear_conceptualizer_pipe():
  global pipe_conceptualizer
  if pipe_conceptualizer is not None:
    #print("Clearing out CLIP Guided pipeline for more VRAM")
    del pipe_conceptualizer
    gc.collect()
    torch.cuda.empty_cache()
    pipe_conceptualizer = None
def clear_repaint_pipe():
  global pipe_repaint
  if pipe_repaint is not None:
    del pipe_repaint
    gc.collect()
    torch.cuda.empty_cache()
    pipe_repaint = None
def clear_imagic_pipe():
  global pipe_imagic
  if pipe_imagic is not None:
    del pipe_imagic
    gc.collect()
    torch.cuda.empty_cache()
    pipe_imagic = None
def clear_composable_pipe():
  global pipe_composable
  if pipe_composable is not None:
    del pipe_composable
    gc.collect()
    torch.cuda.empty_cache()
    pipe_composable = None
def clear_versatile_pipe():
  global pipe_versatile
  if pipe_versatile is not None:
    del pipe_versatile
    gc.collect()
    torch.cuda.empty_cache()
    pipe_versatile = None
def clear_versatile_text2img_pipe():
  global pipe_versatile_text2img
  if pipe_versatile_text2img is not None:
    del pipe_versatile_text2img
    gc.collect()
    torch.cuda.empty_cache()
    pipe_versatile_text2img = None
def clear_versatile_variation_pipe():
  global pipe_versatile_variation
  if pipe_versatile_variation is not None:
    del pipe_versatile_variation
    gc.collect()
    torch.cuda.empty_cache()
    pipe_versatile_variation = None
def clear_versatile_dualguided_pipe():
  global pipe_versatile_dualguided
  if pipe_versatile_dualguided is not None:
    del pipe_versatile_dualguided
    gc.collect()
    torch.cuda.empty_cache()
    pipe_versatile_dualguided = None
def clear_depth_pipe():
  global pipe_depth
  if pipe_depth is not None:
    del pipe_depth
    gc.collect()
    torch.cuda.empty_cache()
    pipe_depth = None
def clear_safe_pipe():
  global pipe_safe
  if pipe_safe is not None:
    del pipe_safe
    gc.collect()
    torch.cuda.empty_cache()
    pipe_safe = None
def clear_upscale_pipe():
  global pipe_upscale
  if pipe_upscale is not None:
    del pipe_upscale
    gc.collect()
    torch.cuda.empty_cache()
    pipe_upscale = None
def clear_image_variation_pipe():
  global pipe_image_variation
  if pipe_image_variation is not None:
    del pipe_image_variation
    gc.collect()
    torch.cuda.empty_cache()
    pipe_image_variation = None
def clear_unCLIP_pipe():
  global pipe_unCLIP
  if pipe_unCLIP is not None:
    del pipe_unCLIP
    gc.collect()
    torch.cuda.empty_cache()
    pipe_unCLIP = None
def clear_unCLIP_image_variation_pipe():
  global pipe_unCLIP_image_variation
  if pipe_unCLIP_image_variation is not None:
    del pipe_unCLIP_image_variation
    gc.collect()
    torch.cuda.empty_cache()
    pipe_unCLIP_image_variation = None
def clear_magic_mix_pipe():
  global pipe_magic_mix
  if pipe_magic_mix is not None:
    del pipe_magic_mix
    gc.collect()
    torch.cuda.empty_cache()
    pipe_magic_mix = None
def clear_paint_by_example_pipe():
  global pipe_paint_by_example
  if pipe_paint_by_example is not None:
    del pipe_paint_by_example
    gc.collect()
    torch.cuda.empty_cache()
    pipe_paint_by_example = None

def clear_pipes(allbut=None):
    but = [] if allbut == None else [allbut] if type(allbut) is str else allbut
    if not 'txt2img' in but: clear_txt2img_pipe()
    if not 'img2img' in but: clear_img2img_pipe()
    if not 'unet' in but: clear_unet_pipe()
    if not 'clip_guided' in but: clear_clip_guided_pipe()
    if not 'conceptualizer' in but: clear_conceptualizer_pipe()
    if not 'repaint' in but: clear_repaint_pipe()
    if not 'imagic' in but: clear_imagic_pipe()
    if not 'composable': clear_composable_pipe()
    if not 'versatile_text2img' in but: clear_versatile_text2img_pipe()
    if not 'versatile_variation' in but: clear_versatile_variation_pipe()
    if not 'versatile_dualguided' in but: clear_versatile_dualguided_pipe()
    if not 'depth' in but: clear_depth_pipe()
    if not 'safe' in but: clear_safe_pipe()
    if not 'upscale' in but: clear_upscale_pipe()
    if not 'unCLIP' in but: clear_unCLIP_pipe()
    if not 'unCLIP_image_variation' in but: clear_unCLIP_image_variation_pipe()
    if not 'image_variation' in but: clear_image_variation_pipe()
    if not 'magic_mix' in but: clear_magic_mix_pipe()
    if not 'paint_by_example' in but: clear_paint_by_example_pipe()

import base64
def get_base64(image_path):
    with open(image_path, "rb") as img_file:
        my_string = base64.b64encode(img_file.read()).decode('utf-8')
        return my_string

def available_file(folder, name, idx, ext='png'):
  available = False
  while not available:
    # Todo, check if using PyDrive2
    if os.path.isfile(os.path.join(folder, f'{name}-{idx}.{ext}')):
      idx += 1
    else: available = True
  return os.path.join(folder, f'{name}-{idx}.{ext}')

def available_folder(folder, name, idx):
  available = False
  while not available:
    if os.path.isdir(os.path.join(folder, f'{name}-{idx}')):
      idx += 1
    else: available = True
  return os.path.join(folder, f'{name}-{idx}')

#import asyncio
#async 
def start_diffusion(page):
  global pipe, unet, pipe_img2img, pipe_clip_guided, pipe_interpolation, pipe_conceptualizer, pipe_imagic, pipe_depth, pipe_composable, pipe_versatile_text2img, pipe_versatile_variation, pipe_versatile_dualguided, pipe_safe, pipe_upscale
  global SD_sampler, stability_api, total_steps, pb, prefs, args, total_steps
  def prt(line, update=True):
    if type(line) == str:
      line = Text(line)
    try:
      page.imageColumn.controls.append(line)
      if update:
        page.imageColumn.update()
    except Exception:
      clear_image_output()
      pass
    if update:
      page.Images.update()
  def clear_last(update=True):
    del page.imageColumn.controls[-1]
    if update:
      page.imageColumn.update()
      page.Images.update()
  abort_run = False
  def abort_diffusion(e):
    nonlocal abort_run
    abort_run = True
    page.snd_error.play()
    page.snd_delete.play()
  def callback_cancel(cancel) -> None:
    callback_cancel.has_been_called = True
    if abort_run:
      return True
  def download_image(e):
    if is_Colab:
      print(f"{type(e.control.data)} {e.control.data}")
      from google.colab import files
      if os.path.isfile(e.control.data):
        files.download(e.control.data)
      else:
        time.sleep(5)
        files.download(e.control.data)
  def clear_image_output():
    for co in reversed(page.imageColumn.controls):
      del co
    page.imageColumn.controls.clear()
    try:
      page.imageColumn.update()
    except Exception as e:
      try:
        page.imageColumn = Column([], auto_scroll=True, scroll=ScrollMode.AUTO)
      except Exception as er:
        alert_msg(page, f"ERROR: Problem Clearing Image Output List. May need to stop script and restart app to recover, sorry...", content=Text(f'{e}\n{er}'))
        page.Images = buildImages(page)
        pass
      page.update()
      pass
# Why getting Exception: control with ID '_3607' not found when re-running after error
  #page.Images.content.controls = []
  clear_image_output()
  pb.width=page.width - 50
  prt(Row([Text("▶️   Running Stable Diffusion on Batch Prompts List", style=TextThemeStyle.TITLE_LARGE), IconButton(icon=icons.CANCEL, tooltip="Abort Current Diffusion Run", on_click=abort_diffusion)], alignment=MainAxisAlignment.SPACE_BETWEEN))
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
  clear_repaint_pipe()
  output_files = []
  pipe_used = ""
  retry_attempts_if_NSFW = prefs['retry_attempts']
  #if (prefs['use_Stability_api'] and status['installed_stability']) or bool(not status['installed_diffusers'] and status['installed_stability']):
  #  update_stability()
  last_seed = args['seed']
  if args['seed'] < 1 or args['seed'] is None:
    rand_seed = random.randint(0,2147483647)
    if not (prefs['use_Stability_api'] or (not status['installed_diffusers'] and status['installed_stability'])):
      if use_custom_scheduler:
        generator = torch.manual_seed(rand_seed)
      else:
        generator = torch.Generator("cuda").manual_seed(rand_seed)
    last_seed = rand_seed
  else:
    if not (prefs['use_Stability_api'] or (not status['installed_diffusers'] and status['installed_stability'])):
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
  model = get_model(prefs['model_ckpt'])
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
            new_arg['seed'] = random.randint(0,2147483647)
            new_arg['n_iterations'] = 1
            new_dream.arg = new_arg
            #new_dream.arg['seed'] = random.randint(0,4294967295)
          else:
            new_dream = Dream(p, seed=random.randint(0,2147483647), n_iterations=1)
          new_dream.arg['n_iterations'] = 1
          #prompts.insert(p_idx+1, new_dream)
          updated_prompts.append(new_dream)

    if bool(model['prefix']):
      if model['prefix'][-1] != ' ':
        model['prefix'] = model['prefix'] + ' '
    for p in updated_prompts:
      pr = ""
      images = None
      usable_image = True
      arg = {}
      if type(p) == list or type(p) == str:
        pr = model['prefix'] + p
        arg = args.copy()
      elif isinstance(p, Dream):
        pr = model['prefix'] + p.prompt
        arg = merge_dict(args, p.arg)
      else: prt(f"Unknown object {type(p)} in the prompt list")
      if arg['batch_size'] > 1:
        pr = [pr] * arg['batch_size']
        if bool(arg['negative_prompt']):
          arg['negative_prompt'] = [arg['negative_prompt']] * arg['batch_size']
      if last_seed != arg['seed']:
        if arg['seed'] < 1 or arg['seed'] is None:
          rand_seed = random.randint(0,2147483647)
          if not (prefs['use_Stability_api'] or (not status['installed_diffusers'] and status['installed_stability'])):
            if use_custom_scheduler:
              generator = torch.manual_seed(rand_seed)
            else:
              generator = torch.Generator("cuda").manual_seed(rand_seed)
          arg['seed'] = rand_seed
        else:
          if not(prefs['use_Stability_api'] or (not status['installed_diffusers'] and status['installed_stability'])):
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
      prt(Divider(height=6, thickness=2), update=False)
      prt(Row([Text(p_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight=FontWeight.BOLD), Text(f'seed: {arg["seed"]}   ')]))
      time.sleep(0.1)
      page.auto_scrolling(False)
      #prt(p_count + ('─' * 90))
      #prt(f'{pr[0] if type(pr) == list else pr} - seed:{arg["seed"]}')
      total_steps = arg['steps']
      
      if prefs['use_Stability_api'] or bool(arg['use_Stability'] or (not status['installed_diffusers'] and status['installed_stability'])):
        if not status['installed_stability']:
          alert_msg(page, f"ERROR: To use Stability-API, you must run the install it first and have proper API key")
          return
        else:
          prt('Stablity API Diffusion ')# + ('─' * 100))
          #print(f'"{SD_prompt}", height={SD_height}, width={SD_width}, steps={SD_steps}, cfg_scale={SD_guidance_scale}, seed={SD_seed}, sampler={generation_sampler}')
          #strikes = 0
          images = []
          arg['width'] = multiple_of_64(arg['width'])
          arg['height'] = multiple_of_64(arg['height'])
          prt(pb)
          import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
          answers = response = None
          
          import requests
          from io import BytesIO
          import base64
          api_host = os.getenv('API_HOST', 'https://api.stability.ai')
          engine_id = prefs['model_checkpoint']# if prefs['model_checkpoint'] == "stable-diffusion-v1-5" else "stable-diffusion-v1"
          url = f"{api_host}/v1alpha/generation/{engine_id}/"#image-to-image"
          headers = {
              'Content-Type': 'application/json',
              'Accept': 'application/json',#'image/png',
              'Authorization': prefs['Stability_api_key'],
          }
          payload = {
              "cfg_scale": arg['guidance_scale'],
              "clip_guidance_preset": prefs['clip_guidance_preset'],
              "height": arg['height'],
              "width": arg['width'],
              "sampler": prefs['generation_sampler'],
              "samples": arg['batch_size'],
              "seed": arg['seed'],
              "steps": arg['steps'],
              "text_prompts": [
                  {
                      "text": pr,
                      "weight": 1
                  }
              ],
          }
          if bool(arg['negative_prompt']):
            payload['text_prompts'].append({"text": arg['negative_prompt'], "weight": -1})

          if bool(arg['mask_image']) or (bool(arg['init_image']) and arg['alpha_mask']):
            if not bool(arg['init_image']):
              clear_last()
              prt(f"ERROR: You have not selected an init_image to go with your image mask..")
              continue
            if arg['init_image'].startswith('http'):
              response = requests.get(arg['init_image'])
              init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
            else:
              if os.path.isfile(arg['init_image']):
                init_img = PILImage.open(arg['init_image'])
              else: 
                clear_last()
                prt(f"ERROR: Couldn't find your init_image {arg['init_image']}")
            init_img = init_img.resize((arg['width'], arg['height']))
            buff = BytesIO()
            init_img.save(buff, format="PNG")
            buff.seek(0)
            img_str = io.BufferedReader(buff).read()
            #init_image = preprocess(init_img)
            if not arg['alpha_mask']:
              if arg['mask_image'].startswith('http'):
                response = requests.get(arg['mask_image'])
                mask_img = PILImage.open(BytesIO(response.content)).convert("RGB")
              else:
                if os.path.isfile(arg['mask_image']):
                  mask_img = PILImage.open(arg['mask_image'])
                else:
                  clear_last()
                  prt(f"ERROR: Couldn't find your mask_image {arg['mask_image']}")
              mask = mask_img.resize((arg['width'], arg['height']))

              buff = BytesIO()
              mask.save(buff, format="PNG")
              buff.seek(0)
              mask_str = io.BufferedReader(buff).read()
            #payload["step_schedule_end"] = 0.01
            payload["step_schedule_start"] = 1# - arg['init_image_strength']
            files = {
                'init_image': img_str,#base64.b64encode(init_img.tobytes()).decode(),#open(init_img, 'rb'),
                #'mask_image': mask_str,
                'mask_source': "INIT_IMAGE_ALPHA" if arg['alpha_mask'] else "MASK_IMAGE_BLACK" if arg['invert_mask'] else "MASK_IMAGE_WHITE",
                'options': (None, json.dumps(payload)),
            }
            if not arg['alpha_mask']:
              files['mask_image'] = mask_str
            pipe_used = "Stability-API Inpainting"
            #engine_id = prefs['model_checkpoint'] if prefs['model_checkpoint'] == "stable-diffusion-v1-5" else "stable-diffusion-v1"
            response = requests.post(url+"image-to-image/masking", headers=headers, files=files)
            #answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], mask_image=mask, init_image=init_img, start_schedule= 1 - arg['init_image_strength'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], samples=arg['batch_size'], safety=not prefs["disable_nsfw_filter"], seed=arg['seed'], sampler=SD_sampler)
          elif bool(arg['init_image']):
            if arg['init_image'].startswith('http'):
              response = requests.get(arg['init_image'])
              init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
            else:
              if os.path.isfile(arg['init_image']):
                init_img = PILImage.open(arg['init_image']).convert("RGB")
              else:
                clear_last()
                prt(f"ERROR: Couldn't find your init_image {arg['init_image']}")
            init_img = init_img.resize((arg['width'], arg['height']))
            
            buff = BytesIO()
            init_img.save(buff, format="PNG")
            buff.seek(0)
            img_str = io.BufferedReader(buff).read()
            #img_str = open(buff.read(), 'rb') #base64.b64encode(buff.getvalue())  init_img.tobytes("raw")
            payload["step_schedule_end"] = 0.01
            payload["step_schedule_start"] = 1 - arg['init_image_strength']
            files = {
                'init_image': img_str,#base64.b64encode(init_img.tobytes()).decode(),#open(init_img, 'rb'),
                'options': (None, json.dumps(payload)),
            }
            pipe_used = "Stability-API Image-to-Image"
            response = requests.post(url+"image-to-image", headers=headers, files=files)
            #answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], init_image=init_img, start_schedule= 1 - arg['init_image_strength'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], samples=arg['batch_size'], safety=not prefs["disable_nsfw_filter"], seed=arg['seed'], sampler=SD_sampler)
          else:
            pipe_used = "Stability-API Text-to-Image"
            response = requests.post(url+"text-to-image", headers=headers, json=payload)
            #answers = stability_api.generate(prompt=pr, height=arg['height'], width=arg['width'], steps=arg['steps'], cfg_scale=arg['guidance_scale'], seed=arg['seed'], samples=arg['batch_size'], safety=False, sampler=SD_sampler)
          clear_last(update=False)
          clear_last()
          if response != None:
            if response.status_code != 200:
              if response.status_code == 402:
                alert_msg(page, "Stability-API ERROR: Insufficient Credit Balance. Reload at DreamStudio.com...", content=Text(str(response.text)))
                return
              else:
                prt(f"Stability-API ERROR {response.status_code}: " + str(response.text))
                continue
            #with open(output_file, "wb") as f:
            #  f.write(response.content)
            artifacts = json.loads(response.content)
            for resp in artifacts['artifacts']:
              #print(f'{type(resp)} - {resp["seed"]}')
              if resp == None: continue
              images.append(PILImage.open(io.BytesIO(base64.b64decode(resp['base64']))))
            #print(f'{type(response.content)} {response.content}')
          if answers != None:
            for resp in answers:
              for artifact in resp.artifacts:
                #print("Artifact reason: " + str(artifact.finish_reason))
                if artifact.finish_reason == generation.FILTER:         
                  usable_image = False
                if artifact.finish_reason == generation.ARTIFACT_TEXT:         
                  usable_image = False
                  prt(f"Couldn't process NSFW text in prompt.  Can't retry so change your request.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                  images.append(PILImage.open(io.BytesIO(artifact.binary)))

      else:
        #from torch.amp.autocast_mode import autocast
        #precision_scope = autocast if prefs['precision']=="autocast" else nullcontext
        try:
          if use_custom_scheduler and not bool(arg['init_image']) and not bool(arg['mask_image']) and not bool(arg['prompt2']):
            # Not implemented correctly anymore, old code but might reuse custom
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
            clear_pipes("unet")
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
            if bool(arg['use_clip_guided_model']) and status['installed_clip']:
              if bool(arg['init_image']) or bool(arg['mask_image']):
                #raise ValueError("Cannot use CLIP Guided Model with init or mask image yet.")
                alert_msg(page, "Cannot use CLIP Guided Model with init or mask image yet.")
                return
              clear_pipes("clip_guided")
              if pipe_clip_guided is None:
                prt(Row([ProgressRing(), Text("Initializing CLIP-Guided Pipeline...", weight=FontWeight.BOLD)]))
                pipe_clip_guided = get_clip_guided_pipe()
                clear_last()
              clip_prompt = arg["clip_prompt"] if arg["clip_prompt"].strip() != "" else None
              if bool(arg["unfreeze_unet"]):
                pipe_clip_guided.unfreeze_unet()
              else:
                pipe_clip_guided.freeze_unet()
              if bool(arg["unfreeze_vae"]):
                pipe_clip_guided.unfreeze_vae()
              else:
                pipe_clip_guided.freeze_vae()
              # TODO: Figure out why it's broken with use_cutouts=False and doesn't generate, hacking it True for now
              arg["use_cutouts"] = True 
              page.auto_scrolling(False)
              prt(pb)
              pipe_used = "CLIP Guided"
              images = pipe_clip_guided(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], clip_prompt=clip_prompt, clip_guidance_scale=arg["clip_guidance_scale"], num_cutouts=int(arg["num_cutouts"]) if arg["use_cutouts"] else None, use_cutouts=arg["use_cutouts"], generator=generator).images
              clear_last()
              page.auto_scrolling(True)
            elif bool(prefs['use_conceptualizer']) and status['installed_conceptualizer']:
              clear_pipes("conceptualizer")
              if pipe_conceptualizer is None:
                prt(Row([ProgressRing(), Text("Initializing Conceptualizer Pipeline...", weight=FontWeight.BOLD)]))
                pipe_conceptualizer = get_conceptualizer(page)
                clear_last()
              total_steps = arg['steps']
              page.auto_scrolling(False)
              prt(pb)
              pipe_used = f"Conceptualizer {prefs['concepts_model']}"
              images = pipe_conceptualizer(prompt=pr, negative_prompt=arg['negative_prompt'], height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              clear_last()
              page.auto_scrolling(True)
            elif bool(arg['mask_image']) or (not bool(arg['mask_image']) and bool(arg['init_image']) and bool(arg['alpha_mask'])):
              if not bool(arg['init_image']):
                alert_msg(page, f"ERROR: You have not selected an init_image to go with your image mask..")
                return
              #if pipe_inpainting is None:
              #  pipe_inpainting = get_inpainting_pipe()
              if prefs['use_inpaint_model'] and status['installed_img2img']:
                clear_pipes("img2img")
                if pipe_img2img is None:
                  prt(Row([ProgressRing(), Text("Initializing Inpaint Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_img2img = get_img2img_pipe()
                  clear_last()
              else:
                clear_pipes("txt2img")
                if pipe is None:
                  prt(Row([ProgressRing(), Text("Initializing Long Prompt Weighting Inpaint Pipeline...", weight=FontWeight.BOLD)]))
                  pipe = get_txt2img_pipe()
                  clear_last()
              '''if pipe_img2img is None:
                try:
                  pipe_img2img = get_img2img_pipe()
                except NameError:
                  prt(f"{Color.RED}You must install the image2image Pipeline above.{Color.END}")
                finally:
                  raise NameError("You must install the image2image Pipeline above")'''
              import requests
              from io import BytesIO
              if arg['init_image'].startswith('http'):
                response = requests.get(arg['init_image'])
                init_img = PILImage.open(BytesIO(response.content))
              else:
                if os.path.isfile(arg['init_image']):
                  init_img = PILImage.open(arg['init_image'])
                else: prt(f"ERROR: Couldn't find your init_image {arg['init_image']}")
              if bool(arg['alpha_mask']):
                init_img = init_img.convert("RGBA")
              else:
                init_img = init_img.convert("RGB")
              init_img = init_img.resize((arg['width'], arg['height']))
              #init_image = preprocess(init_img)
              mask_img = None
              if not bool(arg['mask_image']) and bool(arg['alpha_mask']):
                mask_img = init_img.convert('RGBA')
                red, green, blue, alpha = PILImage.Image.split(init_img)
                mask_img = alpha.convert('L')
              else:
                if arg['mask_image'].startswith('http'):
                  response = requests.get(arg['mask_image'])
                  mask_img = PILImage.open(BytesIO(response.content))
                else:
                  if os.path.isfile(arg['mask_image']):
                    mask_img = PILImage.open(arg['mask_image'])
                  else: prt(f"ERROR: Couldn't find your mask_image {arg['mask_image']}")
              if arg['invert_mask'] and not arg['alpha_mask']:
                from PIL import ImageOps
                mask_img = ImageOps.invert(mask_img.convert('RGB'))
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
              if prefs['use_inpaint_model'] and status['installed_img2img']:
                pipe_used = "Diffusers Inpaint"
                images = pipe_img2img(prompt=pr, negative_prompt=arg['negative_prompt'], mask_image=mask_img, image=init_img, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              else:
                pipe_used = "Long Prompt Weight Inpaint"
                images = pipe.inpaint(prompt=pr, negative_prompt=arg['negative_prompt'], mask_image=mask_img, image=init_img, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              clear_last()
              page.auto_scrolling(True)
            elif bool(arg['init_image']):
              if not status['installed_txt2img'] and not (prefs['use_imagic'] and status['installed_imagic']) and not (prefs['use_depth2img'] and status['installed_depth2img']):
                alert_msg(page, f"CRITICAL ERROR: You have not installed the image2image pipeline yet.  Run in the Installer..")
                continue
              if prefs['use_versatile'] and status['installed_versatile']:
                if len(pr.strip()) > 2: # Find another way to know the difference
                  clear_pipes("versatile_dualguided")
                  if pipe_versatile_dualguided is None:
                    prt(Row([ProgressRing(), Text("Initializing Versatile Dual-Guided Pipeline...", weight=FontWeight.BOLD)]))
                    pipe_versatile_dualguided = get_versatile_dualguided_pipe()
                    clear_last()
                else:
                  clear_pipes("versatile_variation")
                  if pipe_versatile_variation is None:
                    prt(Row([ProgressRing(), Text("Initializing Versatile Image Variation Pipeline...", weight=FontWeight.BOLD)]))
                    pipe_versatile_variation = get_versatile_variation_pipe()
                    clear_last()
              elif prefs['use_depth2img'] and status['installed_depth2img']:
                clear_pipes("depth")
                if pipe_depth is None:
                  prt(Row([ProgressRing(), Text("Initializing SD2 Depth2Image Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_depth = get_depth_pipe()
                  clear_last()
              elif prefs['use_inpaint_model'] and status['installed_img2img']:
                clear_pipes("img2img")
                if pipe_img2img is None:
                  prt(Row([ProgressRing(), Text("Initializing Inpaint Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_img2img = get_img2img_pipe()
                  clear_last()
              elif prefs['use_imagic'] and status['installed_imagic']:
                clear_pipes("imagic")
                if pipe_imagic is None:
                  prt(Row([ProgressRing(), Text("Initializing iMagic Image2Image Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_imagic = get_imagic_pipe()
                  clear_last()
              else:
                clear_pipes("txt2img")
                if pipe is None:
                  prt(Row([ProgressRing(), Text("Initializing Long Prompt Weighting Image2Image Pipeline...", weight=FontWeight.BOLD)]))
                  pipe = get_txt2img_pipe()
                  clear_last()
              '''if pipe_img2img is None:
                try:
                  pipe_img2img = get_img2img_pipe()
                except NameError:
                  prt(f"{Color.RED}You must install the image2image Pipeline above.{Color.END}")
                  raise NameError("You must install the image2image Pipeline above")'''
                #finally:
              import requests
              from io import BytesIO
              if arg['init_image'].startswith('http'):
                response = requests.get(arg['init_image'])
                init_img = PILImage.open(BytesIO(response.content)).convert("RGB")
              else:
                if os.path.isfile(arg['init_image']):
                  init_img = PILImage.open(arg['init_image']).convert("RGB")
                else: alert_msg(page, f"ERROR: Couldn't find your init_image {arg['init_image']}")
              init_img = init_img.resize((arg['width'], arg['height']))
              #init_image = preprocess(init_img)
              #white_mask = PILImage.new("RGB", (arg['width'], arg['height']), (255, 255, 255))
              page.auto_scrolling(False)
              prt(pb)
              #with autocast("cuda"):
              #images = pipe_img2img(prompt=pr, negative_prompt=arg['negative_prompt'], init_image=init_img, mask_image=white_mask, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              if prefs['use_versatile'] and status['installed_versatile']:
                if len(pr.strip()) > 2:
                  pipe_used = "Versatile Dual-Guided"
                  images = pipe_versatile_dualguided(prompt=pr, negative_prompt=arg['negative_prompt'], image=init_img, text_to_image_strength= arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
                else:
                  pipe_used = "Versatile Variation"
                  images = pipe_versatile_variation(negative_prompt=arg['negative_prompt'], image=init_img, num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              elif prefs['use_depth2img'] and status['installed_depth2img']:
                pipe_used = "Depth-to-Image"
                images = pipe_depth(prompt=pr, negative_prompt=arg['negative_prompt'], image=init_img, strength=arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              elif prefs['use_inpaint_model'] and status['installed_img2img']:
                pipe_used = "Diffusers Inpaint Image-to-Image"
                white_mask = PILImage.new("RGB", (arg['width'], arg['height']), (255, 255, 255))
                images = pipe_img2img(prompt=pr, negative_prompt=arg['negative_prompt'], image=init_img, mask_image=white_mask, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              elif prefs['use_imagic'] and status['installed_imagic']:
                pipe_used = "iMagic Image-to-Image"
                #only one element tensors can be converted to Python scalars
                total_steps = None
                res = pipe_imagic.train(pr, init_img, num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
                images = []
                # TODO: alpha= arguments to customize which to make
                total_steps = 0
                res = pipe_imagic(alpha=1, callback=callback_fn, callback_steps=1)
                images.append(res.images[0])
                res = pipe_imagic(alpha=1.5, callback=callback_fn, callback_steps=1)
                images.append(res.images[0])
                res = pipe_imagic(alpha=2, callback=callback_fn, callback_steps=1)
                images.append(res.images[0])
              else:
                pipe_used = "Long Prompt Weight Image-to-Image"
                images = pipe.img2img(prompt=pr, negative_prompt=arg['negative_prompt'], image=init_img, strength= 1 - arg['init_image_strength'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              clear_last()
              page.auto_scrolling(True)
            elif bool(arg['prompt2']):
              if pipe is None:
                pipe = get_txt2img_pipe()
              #with precision_scope("cuda"):
              #    with torch.no_grad():
              pipe_used = "LPW Tween Lerp"
              images_tween = pipe.lerp_between_prompts(pr, arg["prompt2"], length = arg['tweens'], save=False, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator)
              #print(str(images_tween))
              images = images_tween['images']
              #images = pipe(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator)["sample"]
            else:
              if prefs['use_composable'] and status['installed_composable']:
                clear_pipes("composable")
                if pipe_composable is None:
                  prt(Row([ProgressRing(), Text("Initializing Composable Text2Image Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_composable = get_composable_pipe()
                  clear_last()
              elif prefs['use_versatile'] and status['installed_versatile']:
                clear_pipes("versatile_text2img")
                if pipe_versatile_text2img is None:
                  prt(Row([ProgressRing(), Text("Initializing Versatile Text2Image Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_versatile_text2img = get_versatile_text2img_pipe()
                  clear_last()
              elif prefs['use_safe'] and status['installed_safe']:
                clear_pipes("safe")
                if pipe_safe is None:
                  prt(Row([ProgressRing(), Text("Initializing Safe Stable Diffusion Pipeline...", weight=FontWeight.BOLD)]))
                  pipe_safe = get_safe_pipe()
                  clear_last()
              elif pipe is None:
                clear_pipes("txt2img")
                prt(Row([ProgressRing(), Text("Initializing Long Prompt Weighting Text2Image Pipeline...", weight=FontWeight.BOLD)]))
                pipe = get_txt2img_pipe()
                clear_last()
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
              if prefs['use_composable'] and status['installed_composable']:
                weights = arg['negative_prompt'] #" 1 | 1"  # Equal weight to each prompt. Can be negative
                if not bool(weights):
                  segments = len(pr.split('|'))
                  weights = '|'.join(['1' * segments])
                pipe_used = "Composable Text-to-Image"
                images = pipe_composable(pr, height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], weights=weights, generator=generator, callback=callback_fn, callback_steps=1).images
              elif prefs['use_versatile'] and status['installed_versatile']:
                pipe_used = "Versatile Text-to-Image"
                images = pipe_versatile_text2img(prompt=pr, negative_prompt=arg['negative_prompt'], height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
              elif prefs['use_safe'] and status['installed_safe']:
                from diffusers.pipelines.stable_diffusion_safe import SafetyConfig
                s = prefs['safety_config']
                safety = SafetyConfig.WEAK if s == 'Weak' else SafetyConfig.MEDIUM if s == 'Medium' else SafetyConfig.STRONG if s == 'Strong' else SafetyConfig.MAX if s == 'Max' else SafetyConfig.STRONG 
                pipe_used = f"Safe Diffusion {safety}"
                images = pipe_safe(prompt=pr, negative_prompt=arg['negative_prompt'], height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1, **safety).images
              else:
                pipe_used = "Long Prompt Weight Text-to-Image"
                images = pipe(prompt=pr, negative_prompt=arg['negative_prompt'], height=arg['height'], width=arg['width'], num_inference_steps=arg['steps'], guidance_scale=arg['guidance_scale'], eta=arg['eta'], generator=generator, callback=callback_fn, callback_steps=1).images
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
          clear_last()
          if 'out of memory' in str(e):
            alert_msg(page, f"CRITICAL ERROR: GPU ran out of memory! Flushing memory to save session... Try reducing image size.", content=Text(str(e)))
            pass
          else:
            alert_msg(page, f"RUNTIME ERROR: Unknown error processing image. Check parameters and try again. Restart app if persists.", content=Text(str(e)))
            pass
        except Exception as e:
          alert_msg(page, f"EXCEPTION ERROR: Unknown error processing image. Check parameters and try again. Restart app if persists.", content=Text(str(e)))
          pass
        finally:
          gc.collect()
          torch.cuda.empty_cache()

      txt2img_output = stable_dir #f'{stable_dir}/stable-diffusion/outputs/txt2img-samples'
      batch_output = prefs['image_output']
      if bool(prefs['batch_folder_name']):
        txt2img_output = os.path.join(stable_dir, prefs['batch_folder_name'])
        batch_output = os.path.join(prefs['image_output'], prefs['batch_folder_name'])
      if not os.path.exists(txt2img_output):
        os.makedirs(txt2img_output)
      if save_to_GDrive or storage_type == "Colab Google Drive":
        if not os.path.exists(batch_output):
          os.makedirs(batch_output)
      elif storage_type == "PyDrive Google Drive": # TODO: I'm not getting the parent folder id right, their docs got confusing
        newFolder = gdrive.CreateFile({'title': prefs['batch_folder_name'], "parents": [{"kind": "drive#fileLink", "id": prefs['image_output']}],"mimeType": "application/vnd.google-apps.folder"})
        newFolder.Upload()
        batch_output = newFolder
      else:
        if not os.path.exists(batch_output):
          os.makedirs(batch_output)

      filename = format_filename(pr[0] if type(pr) == list else pr)
      if images is None:
        prt(f"ERROR: Problem generating images, check your settings and run above blocks again, or report the error to Skquark if it really seems broken.")
        images = []

      idx = num = 0
      for image in images:
        cur_seed = arg['seed']
        if idx > 0:
          cur_seed += idx
          i_count = f'  ({idx + 1} of {len(images)})  '
          prt(Row([Text(i_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight=FontWeight.BOLD), Text(f'seed: {cur_seed}   ')]))
          #prt(f'{pr[0] if type(pr) == list else pr} - seed:{cur_seed}')
        seed_suffix = "" if not prefs['file_suffix_seed'] else f"-{cur_seed}"
        if prefs['use_imagic'] and status['installed_imagic'] and bool(arg['init_image'] and not bool(arg['mask_image'])):
          if idx == 0: seed_suffix += '-alpha_1'
          if idx == 1: seed_suffix += '-alpha_1_5'
          if idx == 2: seed_suffix += '-alpha_2'
        fname = f'{prefs["file_prefix"]}{filename}{seed_suffix}'
        image_path = available_file(txt2img_output, fname, idx)
        num = int(image_path.rpartition('-')[2].partition('.')[0])
        #image_path = os.path.join(txt2img_output, f'{fname}-{idx}.png')
        image.save(image_path)
        #print(f'size:{os.path.getsize(f"{fname}-{idx}.png")}')
        if os.path.getsize(image_path) < 2000 or not usable_image: #False: #not sum(image.convert("L").getextrema()) in (0, 2): #image.getbbox():#
          os.remove(os.path.join(txt2img_output, f'{fname}-{num}.png'))
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
          #prt(Row([Img(src=image_path, width=arg['width'], height=arg['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
          #display(image)
        #if bool(batch_folder_name):
        #  fpath = os.path.join(txt2img_output, batch_folder_name, f'{fname}-{idx}.png')
        #fpath = os.path.join(txt2img_output, f'{fname}-{idx}.png')
        #fpath = available_file(txt2img_output, fname, idx)
        fpath = image_path
        if txt2img_output != batch_output:
          new_file = available_file(batch_output, fname, num)
        else:
          new_file = image_path
        #print(f'fpath: {fpath} - idx: {idx}')
        if prefs['centipede_prompts_as_init_images']:
          shutil.copy(fpath, os.path.join(root_dir, 'init_images'))
          last_image = os.path.join(root_dir, 'init_images', f'{fname}-{num}.png')
        if not prefs['display_upscaled_image'] or not prefs['apply_ESRGAN_upscale']:
          #print(f"Image path:{image_path}")
          upscaled_path = new_file #os.path.join(batch_output if save_to_GDrive else txt2img_output, new_file)
          time.sleep(0.2)
          #prt(Row([GestureDetector(content=Img(src_base64=get_base64(fpath), width=arg['width'], height=arg['height'], fit=ImageFit.FILL, gapless_playback=True), data=new_file, on_long_press_end=download_image, on_secondary_tap=download_image)], alignment=MainAxisAlignment.CENTER))
          prt(Row([GestureDetector(content=Img(src=fpath, width=arg['width'], height=arg['height'], fit=ImageFit.FILL, gapless_playback=True), data=new_file, on_long_press_end=download_image, on_secondary_tap=download_image)], alignment=MainAxisAlignment.CENTER))
          time.sleep(0.3)
          #display(image)
        if prefs['use_upscale'] and status['installed_upscale']:
          clear_pipes(['upscale'])
          if pipe_upscale == None:
            prt(Row([ProgressRing(), Text("Initializing Stable Diffusion 2 Upscale Pipeline...", weight=FontWeight.BOLD)]))
            pipe_upscale = get_upscale_pipe()
            clear_last()
          prt(Row([Text("Upscaling 4X"), pb]))
          try:
            output = pipe_upscale(prompt=pr, image=image, guidance_scale=arg['guidance_scale'], generator=generator, noise_level=prefs['upscale_noise_level'], callback=callback_fn, callback_steps=1)
            output.images[0].save(fpath)
            clear_upscale()
          except Exception as e:
            alert_msg(page, "Error Upscaling Image.  Most likely out of Memory... Reduce image size to less than 512px.", content=Text(e))
            pass
          clear_last()
          #clear_upscale_pipe()
        if prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
          w = int(arg['width'] * prefs["enlarge_scale"])
          h = int(arg['height'] * prefs["enlarge_scale"])
          prt(Row([Text(f'Enlarging {prefs["enlarge_scale"]}X to {w}x{h}')], alignment=MainAxisAlignment.CENTER))
          os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
          upload_folder = 'upload'
          result_folder = 'results'     
          if os.path.isdir(upload_folder):
              shutil.rmtree(upload_folder)
          if os.path.isdir(result_folder):
              shutil.rmtree(result_folder)
          os.mkdir(upload_folder)
          os.mkdir(result_folder)
          short_name = f'{fname[:80]}-{num}.png'
          dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
          #print(f'Moving {fpath} to {dst_path}')
          #shutil.move(fpath, dst_path)
          shutil.copy(fpath, dst_path)
          faceenhance = ' --face_enhance' if prefs["face_enhance"] else ''
          #python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {enlarge_scale}{faceenhance}
          run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
          out_file = short_name.rpartition('.')[0] + '_out.png'
          #print(f'move {root_dir}Real-ESRGAN/{result_folder}/{out_file} to {fpath}')
          #shutil.move(f'{root_dir}Real-ESRGAN/{result_folder}/{out_file}', fpath)
          shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), fpath)
          # !python inference_realesrgan.py --model_path experiments/pretrained_models/RealESRGAN_x4plus.pth --input upload --netscale 4 --outscale 3.5 --half --face_enhance
          os.chdir(stable_dir)
          clear_last(update=False)
        
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
          del config_json['alpha_mask']
        if not bool(config_json['mask_image']):
          del config_json['mask_image']
          del config_json['invert_mask']
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
        sampler_str = prefs['generation_sampler'] if prefs['use_Stability_api'] else prefs['scheduler_mode']
        config_json['pipeline'] = pipe_used
        config_json['scheduler_mode'] = sampler_str
        config_json['model_path'] = model_path
        if prefs['save_image_metadata']:
          img = PILImage.open(fpath)
          metadata = PngInfo()
          metadata.add_text("artist", prefs['meta_ArtistName'])
          metadata.add_text("copyright", prefs['meta_Copyright'])
          metadata.add_text("software", "Stable Diffusion Deluxe" + f", upscaled {prefs['enlarge_scale']}x with ESRGAN" if prefs['apply_ESRGAN_upscale'] else "")
          metadata.add_text("title", pr[0] if type(pr) == list else pr)
          if prefs['save_config_in_metadata']:
            config = f"prompt: {pr[0] if type(pr) == list else pr}, seed: {cur_seed}, steps: {arg['steps']}, CGS: {arg['guidance_scale']}, iterations: {arg['n_iterations']}" + f", eta: {arg['eta']}" if not prefs['use_Stability_api'] else ""
            config += f", sampler: {sampler_str}"
            if bool(arg['init_image']): config += f", init_image: {arg['init_image']}, init_image_strength: {arg['init_image_strength']}"
            metadata.add_text("config", config)
            #metadata.add_text("prompt", p)
            metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
          img.save(fpath, pnginfo=metadata)

        #new_file = available_file(batch_output if save_to_GDrive else txt2img_output, fname, idx)
        #new_file = fname #.rpartition('.')[0] #f'{file_prefix}{filename}'
        #if os.path.isfile(os.path.join(batch_output if save_to_GDrive else txt2img_output, f'{new_file}-{idx}.png')):
        #  new_file += '-' + random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        #new_file += f'-{idx}.png'
        if save_to_GDrive:
          shutil.copy(fpath, new_file)#os.path.join(batch_output, new_file))
          #shutil.move(fpath, os.path.join(batch_output, new_file))
        elif storage_type == "PyDrive Google Drive":
          #batch_output
          out_file = gdrive.CreateFile({'title': new_file})
          out_file.SetContentFile(fpath)
          out_file.Upload()
        elif bool(prefs['image_output']):
          shutil.copy(fpath, new_file)#os.path.join(batch_output, new_file))
        if prefs['save_config_json']:
          json_file = new_file.rpartition('.')[0] + '.json'
          with open(os.path.join(stable_dir, json_file), "w") as f:
            json.dump(config_json, f, ensure_ascii=False, indent=4)
          if save_to_GDrive:
            shutil.copy(os.path.join(stable_dir, json_file), os.path.join(batch_output, json_file))
          elif storage_type == "PyDrive Google Drive":
            #batch_output
            out_file = gdrive.CreateFile({'title': json_file})
            out_file.SetContentFile(os.path.join(stable_dir, json_file))
            out_file.Upload()
        output_files.append(os.path.join(batch_output if save_to_GDrive else txt2img_output, new_file))
        if prefs['display_upscaled_image'] and prefs['apply_ESRGAN_upscale']:
          upscaled_path = os.path.join(batch_output if save_to_GDrive else txt2img_output, new_file)
          time.sleep(0.4)
          #prt(Row([GestureDetector(content=Img(src_base64=get_base64(upscaled_path), width=arg['width'] * float(prefs["enlarge_scale"]), height=arg['height'] * float(prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True), data=upscaled_path, on_long_press_end=download_image, on_secondary_tap=download_image)], alignment=MainAxisAlignment.CENTER))
          prt(Row([GestureDetector(content=Img(src=upscaled_path, width=arg['width'] * float(prefs["enlarge_scale"]), height=arg['height'] * float(prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True), data=upscaled_path, on_long_press_end=download_image, on_secondary_tap=download_image)], alignment=MainAxisAlignment.CENTER))
          #prt(Row([Img(src=upscaled_path, width=arg['width'] * float(prefs["enlarge_scale"]), height=arg['height'] * float(prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
          #prt(Img(src=upscaled_path))
          #upscaled = PILImage.open(os.path.join(batch_output, new_file))
          #display(upscaled)
        #else:
          #time.sleep(0.4)
          #prt(Row([Img(src=new_file, width=arg['width'], height=arg['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        prt(Row([Text(fpath.rpartition(slash)[2])], alignment=MainAxisAlignment.CENTER))
        idx += 1
        if abort_run:
          prt(Text("🛑   Aborting Current Diffusion Run..."))
          abort_run = False
          return
      p_idx += 1
      if abort_run:
        prt(Text("🛑   Aborting Current Diffusion Run..."))
        abort_run = False
        return
    if prefs['enable_sounds']: page.snd_alert.play()
  else:
    clear_pipes("interpolation")
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
    from watchdog.events import LoggingEventHandler, FileSystemEventHandler
    class Handler(FileSystemEventHandler):
      def __init__(self):
        super().__init__()
      def on_created(self,event):
        nonlocal img_idx
        if event.is_directory:
          return None
        elif event.event_type == 'created':
          page.auto_scrolling(True)
          clear_last()
          #p_count = f'[{img_idx + 1} of {(len(walk_prompts) -1) * int(prefs['num_interpolation_steps'])}]  '
          #prt(Divider(height=6, thickness=2))
          #prt(Row([Text(p_count), Text(walk_prompts[img_idx], expand=True, weight=FontWeight.BOLD), Text(f'seed: {walk_seeds[img_idx]}')]))
          prt(Row([Img(src=event.src_path, width=arg['width'], height=arg['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
          prt(Row([Text(f'{event.src_path}')], alignment=MainAxisAlignment.CENTER))
          page.update()
          time.sleep(0.2)
          page.auto_scrolling(False)
          prt(pb)
          img_idx += 1
    image_handler = Handler()
    observer = Observer()
    observer.schedule(image_handler, txt2img_output, recursive = True)
    observer.start()
    prt(f"Interpolating latent space between {len(walk_prompts)} prompts with {int(prefs['num_interpolation_steps'])} steps between each.")
    prt(Divider(height=6, thickness=2))
    prt(pb)
    page.auto_scrolling(False)
    #prt(Row([Text(p_count), Text(pr[0] if type(pr) == list else pr, expand=True, weight=FontWeight.BOLD), Text(f'seed: {arg["seed"]}')]))
    images = pipe_interpolation.walk(prompts=walk_prompts, seeds=walk_seeds, num_interpolation_steps=int(prefs['num_interpolation_steps']), batch_size=int(prefs['batch_size']), output_dir=txt2img_output, width=arg['width'], height=arg['height'], guidance_scale=arg['guidance_scale'], num_inference_steps=int(arg['steps']), eta=arg['eta'], callback=callback_fn, callback_steps=1)
    observer.stop()
    clear_last()
    fpath = images[0].rpartition(slash)[0]
    bfolder = fpath.rpartition(slash)[2]
    if prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
      prt('Applying Real-ESRGAN Upscaling to images...')
      os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
      upload_folder = 'upload'
      result_folder = 'results'     
      if os.path.isdir(upload_folder):
          shutil.rmtree(upload_folder)
      if os.path.isdir(result_folder):
          shutil.rmtree(result_folder)
      os.mkdir(upload_folder)
      os.mkdir(result_folder)
      for i in images:
        fname = i.rpartition(slash)[2]
        dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, fname)
        shutil.move(i, dst_path)
      faceenhance = ' --face_enhance' if prefs["face_enhance"] else ''
      run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
      filenames = os.listdir(os.path.join(dist_dir, 'Real-ESRGAN', 'results'))
      for oname in filenames:
        fparts = oname.rpartition('_out')
        fname_clean = fparts[0] + fparts[2]
        opath = os.path.join(fpath, fname_clean)
        shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, oname), opath)
      os.chdir(stable_dir)
    os.makedirs(os.path.join(batch_output, bfolder), exist_ok=True)
    imgs = os.listdir(fpath)
    for i in imgs:
      #prt(f'Created {i}')
      #fname = i.rpartition(slash)[2]
      if save_to_GDrive:
        shutil.copy(os.path.join(fpath, i), os.path.join(batch_output, bfolder, i))
      elif storage_type == "PyDrive Google Drive":
        #batch_output
        out_file = gdrive.CreateFile({'title': i})
        out_file.SetContentFile(fpath)
        out_file.Upload()
      elif bool(prefs['image_output']):
        shutil.copy(os.path.join(fpath, i), os.path.join(batch_output, bfolder, i))
    if prefs['enable_sounds']: page.snd_alert.play()



def wget(url, output):
    import subprocess
    res = subprocess.run(['wget', '-q', url, '-O', output], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(res)

nspterminology = None

def nsp_parse(prompt):
    import random, os, json
    global nspterminology
    new_prompt = ''
    new_prompts = []
    new_dict = {}
    ptype = type(prompt)
    #if not os.path.exists('./nsp_pantry.json'):
    #    wget('https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.json', f'.{slash}nsp_pantry.json')
    if nspterminology is None:
        response = requests.get("https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.json")
        nspterminology = json.loads(response.content)
    if ptype == dict:
        for pstep, pvalue in prompt.items():
            if type(pvalue) == list:
                for prompt in pvalue:
                    new_prompt = prompt
                    for term in nspterminology:
                        tkey = f'_{term}_'
                        tcount = prompt.count(tkey)
                        for i in range(tcount):
                            new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
                    new_prompts.append(new_prompt)
                new_dict[pstep] = new_prompts
                new_prompts = []
        return new_dict
    elif ptype == list:
        for pstr in prompt:
            new_prompt = pstr
            for term in nspterminology:
                tkey = f'_{term}_'
                tcount = new_prompt.count(tkey)
                for i in range(tcount):
                    new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
            new_prompts.append(new_prompt)
            new_prompt = None
        return new_prompts
    elif ptype == str:
        new_prompt = prompt
        for term in nspterminology:
            tkey = f'_{term}_'
            tcount = new_prompt.count(tkey)
            for i in range(tcount):
                new_prompt = new_prompt.replace(tkey, random.choice(nspterminology[term]), 1)
        return new_prompt
    else:
        return


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
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2400, temperature=prefs['prompt_generator']['AI_temperature'], presence_penalty=1)
    #print(response)
    result = response["choices"][0]["text"].strip()
    #if result[-1] == '.': result = result[:-1]
    #print(str(result))
    for p in result.split('\n'):
      pr = p.strip()
      if not bool(pr): continue
      if pr[-1] == '.': pr = pr[:-1]
      if pr[0] == '*': pr = pr[1:].strip()
      elif '.' in pr: # Sometimes got 1. 2.
        pr = pr.partition('.')[2].strip()
      if '"' in pr: pr = pr.replace('"', '')
      prompt_results.append(pr)
  #print(f"Request mode influence: {request_modes[prefs['prompt_generator']['request_mode']]}\n")
  page.prompt_generator_list.controls.append(Row([ProgressRing(), Text("Requesting Prompts from the AI...", weight=FontWeight.BOLD)]))
  page.prompt_generator_list.update()
  prompt_gen()
  del page.prompt_generator_list.controls[-1]
  page.prompt_generator_list.update()
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
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2400, temperature=prefs["prompt_remixer"]['AI_temperature'], presence_penalty=1)
    #print(response)
    result = response["choices"][0]["text"].strip()
    #if result[-1] == '.': result = result[:-1]
    #print(str(result))
    for p in result.split('\n'):
      pr = p.strip()
      if not bool(pr): continue
      if pr[-1] == '.': pr = pr[:-1]
      if pr[0] == '*': pr = pr[1:].strip()
      elif '.' in pr: # Sometimes got 1. 2.
        pr = pr.partition('.')[2].strip()
      prompt_results.append(pr)
  page.prompt_remixer_list.controls.append(Text(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else "") + f"\nRequest mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n"))
  page.prompt_remixer_list.update()
  #page.add_to_prompt_remixer(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else "") + f"\nRequest mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n")
  #print(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else ""))
  #print(f"Request mode influence: {remixer_request_modes[int(prefs['prompt_remixer']['request_mode'])]}\n")
  page.prompt_remixer_list.controls.append(Row([ProgressRing(), Text("Requesting Prompt Remixes...", weight=FontWeight.BOLD)]))
  page.prompt_remixer_list.update()
  prompt_remix()
  del page.prompt_remixer_list.controls[-1]
  page.prompt_remixer_list.update()

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
    if prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Bloom 176B" or prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Flan-T5 XXL":
      try:
        if not bool(prefs['HuggingFace_api_key']): good_key = False
      except NameError: good_key = False
      if not good_key:
        print(f"\33[91mMissing HuggingFace_api_key...\33[0m Define your key up above.")
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
    
    request = f'{brainstorm_request_modes[prefs["prompt_brainstormer"]["request_mode"]]}"{prefs["prompt_brainstormer"]["about_prompt"]}":' if prefs['prompt_brainstormer']['request_mode'] != "Raw Request" else prefs['prompt_brainstormer']['about_prompt']

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
    
    def flan_query(payload):
        #print(payload)
        response = requests.request("POST", "https://api-inference.huggingface.co/models/google/flan-t5-xxl", json=payload, headers={"Authorization": f"Bearer {prefs['HuggingFace_api_key']}"})
        #print(response.text)
        return json.loads(response.content.decode("utf-8"))

    def flan_request(input_sentence):
        parameters = {
            "max_new_tokens": max_tokens_length,
            "do_sample": False,
            "seed": seed,
            "early_stopping": False,
            "length_penalty": 0.0,
            "eos_token_id": None,}
        payload = {"inputs": input_sentence, "parameters": parameters,"options" : {"use_cache": False} }
        data = flan_query(payload)
        if "error" in data:
            return f"\33[31mERROR: {data['error']}\33[0m"

        generation = data[0]["generated_text"].split(input_sentence, 1)[1]
        #return data[0]["generated_text"]
        return generation

    def prompt_brainstormer():
      #(prompt=prompt, temperature=AI_temperature, presence_penalty=1, stop= "\n")
      page.prompt_brainstormer_list.controls.append(Row([ProgressRing(), Text("Storming the AI's Brain...", weight=FontWeight.BOLD)]))
      page.prompt_brainstormer_list.update()

      if prefs['prompt_brainstormer']['AI_engine'] == "TextSynth GPT-J":
        response = textsynth.text_complete(prompt=request, max_tokens=200, temperature=prefs['prompt_brainstormer']['AI_temperature'], presence_penalty=1)
        #print(str(response))
        result = response.text.strip()
      elif prefs['prompt_brainstormer']['AI_engine'] == "OpenAI GPT-3":
        response = openai.Completion.create(engine="text-davinci-003", prompt=request, max_tokens=2400, temperature=prefs['prompt_brainstormer']['AI_temperature'], presence_penalty=1)
        result = response["choices"][0]["text"].strip()
      elif prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Bloom 176B":
        result = bloom_request(request)
      elif prefs['prompt_brainstormer']['AI_engine'] == "HuggingFace Flan-T5":
        result = flan_request(request) 
      del page.prompt_brainstormer_list.controls[-1]
      page.prompt_brainstormer_list.update()
      page.add_to_prompt_brainstormer(str(result) + '\n')
    #print(f"Remixing {seed_prompt}" + (f", about {optional_about_influencer}" if bool(optional_about_influencer) else ""))
    if good_key:
      #print(request)
      prompt_brainstormer()

def run_prompt_writer(page):
    '''try:
        import nsp_pantry
        from nsp_pantry import nsp_parse
    except ModuleNotFoundError:
        run_sp("wget -qq --show-progress --no-cache --backups=1 https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py")
        #print(subprocess.run(['wget', '-q', '--show-progress', '--no-cache', '--backups=1', 'https://raw.githubusercontent.com/WASasquatch/noodle-soup-prompts/main/nsp_pantry.py'], stdout=subprocess.PIPE).stdout.decode('utf-8'))
    finally:
        import nsp_pantry
        from nsp_pantry import nsp_parse'''
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
    
    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
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
          uploaded = {image_path: image_path.rpartition(slash)[2]}
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
    page.clear_ESRGAN_output(uploaded)
    page.add_to_ESRGAN_output(Text(f"Upscaling {len(uploaded)} images.."))
    for filename in uploaded.keys():
      if not os.path.isfile(filename):
        #print("Skipping " + filename)
        continue
      fname = filename.rpartition(slash)[2] if slash in filename else filename
      dst_path = os.path.join(upload_folder, fname)
      #print(f'Copy {filename} to {dst_path}')
      shutil.copy(filename, dst_path)
      if split_image_grid:
        img = PILImage.open(dst_path)
        split(img, rows, cols, dst_path, True)
    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
    faceenhance = ' --face_enhance' if face_enhance else ''
    run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i {upload_folder} --outscale {enlarge_scale}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
    os.chdir(root_dir)
    if is_Colab:
      from google.colab import files
    if not bool(dst_image_path.strip()):
      if os.path.isdir(image_path):
          dst_image_path = image_path
      else:
          dst_image_path = prefs['image_output'] #image_path.rpartition(slash)[0]
    filenames = os.listdir(os.path.join(dist_dir, 'Real-ESRGAN', 'results'))
    for fname in filenames:
      fparts = fname.rpartition('_out')
      fname_clean = fparts[0] + filename_suffix + fparts[2]
      #print(f'Copying {fname_clean}')
      if save_to_GDrive:
        if not os.path.isdir(dst_image_path):
          os.makedirs(dst_image_path)
        shutil.copy(os.path.join(dist_dir, 'Real-ESRGAN', 'results', fname), os.path.join(dst_image_path, fname_clean))
      else: # TODO PyDrive
        shutil.copy(os.path.join(dist_dir, 'Real-ESRGAN', 'results', fname), os.path.join(dst_image_path, fname_clean))
      if download_locally:
        files.download(os.path.join(dist_dir, 'Real-ESRGAN', 'results', fname))
      if display_image:
        page.add_to_ESRGAN_output(Image(src=os.path.join(dist_dir, 'Real-ESRGAN', 'results', fname)))
      page.add_to_ESRGAN_output(Row([Text(os.path.join(dst_image_path, fname_clean))], alignment=MainAxisAlignment.CENTER))

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
          uploaded = {image_path: image_path.rpartition(slash)[2]}
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

def multiple_of_64(x):
    return int(round(x/64)*64)
def multiple_of_8(x):
    return int(round(x/8)*8)
def multiple_of(x, num):
    return int(round(x/num)*num)
def scale_dimensions(width, height, max=1024, multiple=16):
  max = int(max)
  r_width = width
  r_height = height
  if width < max and height < max:
    if width >= height:
      ratio = max / width
      r_width = max
      r_height = int(height * ratio)
    else:
      ratio = max / height
      r_height = max
      r_width = int(width * ratio)
    width = r_width
    height = r_height
  if width >= height:
    if width > max:
      r_width = max
      r_height = int(height * (max/width))
    else:
      r_width = width
      r_height = height
  else:
    if height > max:
      r_height = max
      r_width = int(width * (max/height))
    else:
      r_width = width
      r_height = height
  return multiple_of(r_width, multiple), multiple_of(r_height, multiple)

def run_repainter(page):
    global repaint_prefs, prefs, status, pipe_repaint
    if not status['installed_diffusers']:
      alert_msg(page, "You need to Install HuggingFace Diffusers before using...")
      return
    if not bool(repaint_prefs['original_image']) or not bool(repaint_prefs['mask_image']):
      alert_msg(page, "You must provide the Original Image and the Mask Image to process...")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.repaint_output.controls.append(line)
      page.repaint_output.update()
    def clear_last():
      del page.repaint_output.controls[-1]
      page.repaint_output.update()
    progress = ProgressBar(bar_height=8)
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress
      total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
      #print(f'{type(latents)} {len(latents)}- {str(latents)}')
    prt(Row([ProgressRing(), Text("Installing RePaint Pipeline...", weight=FontWeight.BOLD)]))
    import requests, random
    from io import BytesIO
    from PIL import Image as PILImage
    from PIL import ImageOps
    if repaint_prefs['original_image'].startswith('http'):
      #response = requests.get(repaint_prefs['original_image'])
      #original_img = PILImage.open(BytesIO(response.content)).convert("RGB")
      original_img = PILImage.open(requests.get(repaint_prefs['original_image'], stream=True).raw)
    else:
      if os.path.isfile(repaint_prefs['original_image']):
        original_img = PILImage.open(repaint_prefs['original_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your original_image {repaint_prefs['original_image']}")
        return
    width, height = original_img.size
    width, height = scale_dimensions(width, height, repaint_prefs['max_size'])
    original_img = original_img.resize((width, height), resample=PILImage.LANCZOS)
    original_img = ImageOps.exif_transpose(original_img).convert("RGB")
    mask_img = None
    if repaint_prefs['mask_image'].startswith('http'):
      #response = requests.get(repaint_prefs['mask_image'])
      #mask_img = PILImage.open(BytesIO(response.content)).convert("RGB")
      mask_img = PILImage.open(requests.get(repaint_prefs['mask_image'], stream=True).raw)
    else:
      if os.path.isfile(repaint_prefs['mask_image']):
        mask_img = PILImage.open(repaint_prefs['mask_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your mask_image {repaint_prefs['mask_image']}")
        return
    #mask_img = mask_img.convert("L")
    #mask_img = mask_img.convert("1")
    if repaint_prefs['invert_mask']:
       mask_img = ImageOps.invert(mask_img.convert('RGB'))
    mask_img = mask_img.resize((width, height), resample=PILImage.NEAREST)
    mask_img = ImageOps.exif_transpose(mask_img).convert("RGB")
    #print(f'Resize to {width}x{height}')
    clear_pipes('repaint')
    if not status['installed_repaint']:
      get_repaint(page)
      status['installed_repaint'] = True
    if pipe_repaint is None:
      pipe_repaint = get_repaint_pipe()
    clear_last()
    prt("Generating Repaint of your Image...")
    prt(progress)
    random_seed = int(repaint_prefs['seed']) if int(repaint_prefs['seed']) > 0 else random.randint(0,4294967295)
    generator = torch.Generator(device=torch_device).manual_seed(random_seed)
#Sizes of tensors must match except in dimension 1. Expected size 58 but got size 59 for tensor number 1 in the list.
    try:
      #from IPython.utils.capture import capture_output
      #with capture_output() as captured:
      image = pipe_repaint(image=original_img, mask_image=mask_img, num_inference_steps=repaint_prefs['num_inference_steps'], eta=repaint_prefs['eta'], jump_length=repaint_prefs['jump_length'], jump_n_sample=repaint_prefs['jump_length'], generator=generator, callback=callback_fnc, callback_steps=1).images[0]
      #print(str(captured.stdout))
    except Exception as e:
      clear_last()
      alert_msg(page, f"ERROR: Couldn't Repaint your image for some reason.  Possibly out of memory or something wrong with my code...", content=Text(str(e)))
      return
    fname = repaint_prefs['original_image'].rpartition('.')[0]
    fname = fname.rpartition(slash)[2]
    if prefs['file_suffix_seed']: fname += f"-{random_seed}"
    image_path = available_file(stable_dir, fname, 1)
    image.save(image_path)
    out_path = image_path
    clear_last()
    clear_last()
    prt(Row([Img(src=image_path, width=width, height=height, fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
    #TODO: ESRGAN, Metadata & PyDrive
    if storage_type == "Colab Google Drive":
      new_file = available_file(prefs['image_output'], fname, 1)
      out_path = new_file
      shutil.copy(image_path, new_file)
    elif bool(prefs['image_output']):
      new_file = available_file(prefs['image_output'], fname, 1)
      out_path = new_file
      shutil.copy(image_path, new_file)
    prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_image_variation(page):
    global image_variation_prefs, pipe_image_variation
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.image_variation_output.controls.append(line)
      page.image_variation_output.update()
    def clear_last():
      del page.image_variation_output.controls[-1]
      page.image_variation_output.update()
    progress = ProgressBar(bar_height=8)
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress
      total_steps = image_variation_prefs['num_inference_steps']#len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
    page.image_variation_output.controls.clear()
    from io import BytesIO
    from PIL import Image as PILImage
    from PIL import ImageOps
    if image_variation_prefs['init_image'].startswith('http'):
      init_img = PILImage.open(requests.get(image_variation_prefs['init_image'], stream=True).raw)
    else:
      if os.path.isfile(image_variation_prefs['init_image']):
        init_img = PILImage.open(image_variation_prefs['init_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your init_image {image_variation_prefs['init_image']}")
        return
    width, height = init_img.size
    width, height = scale_dimensions(width, height, image_variation_prefs['max_size'])
    tform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(
            (width, height),
            interpolation=transforms.InterpolationMode.BICUBIC,
            antialias=False,
            ),
        transforms.Normalize(
          [0.48145466, 0.4578275, 0.40821073],
          [0.26862954, 0.26130258, 0.27577711]),
    ])
    init_img = tform(init_img).to(torch_device)
    #init_img = init_img.resize((width, height), resample=PILImage.LANCZOS)
    #init_img = ImageOps.exif_transpose(init_img).convert("RGB")
    clear_pipes('image_variation')
    if pipe_image_variation == None:
        from diffusers import StableDiffusionImageVariationPipeline
        prt(Row([ProgressRing(), Text(" Downloading Image Variation Pipeline", weight=FontWeight.BOLD)]))
        model_id = "fusing/sd-image-variations-diffusers"
        pipe_image_variation = StableDiffusionImageVariationPipeline.from_pretrained(model_id, scheduler=model_scheduler(model_id), safety_checker=None, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None)
        pipe_image_variation.to(torch_device)
        pipe_image_variation = optimize_pipe(pipe_image_variation)
        #pipe_image_variation.set_progress_bar_config(disable=True)
        clear_last()
    s = "s" if image_variation_prefs['num_images'] > 1 else ""
    prt(f"Generating Variation{s} of your Image...")
    prt(progress)
    random_seed = int(image_variation_prefs['seed']) if int(image_variation_prefs['seed']) > 0 else rnd.randint(0,4294967295)
    generator = torch.Generator(device=torch_device).manual_seed(random_seed)

    try:
        images = pipe_image_variation(image=init_img, height=height, width=width, num_inference_steps=image_variation_prefs['num_inference_steps'], guidance_scale=image_variation_prefs['guidance_scale'], eta=image_variation_prefs['eta'], num_images_per_prompt=image_variation_prefs['num_images'], generator=generator, callback=callback_fnc, callback_steps=1).images
    except Exception as e:
        clear_last()
        clear_last()
        alert_msg(page, "Error running pipeline", content=Text(str(e)))
        return
    clear_last()
    clear_last()
    fname = image_variation_prefs['init_image'].rpartition('.')[0]
    fname = fname.rpartition(slash)[2]
    if prefs['file_suffix_seed']: fname += f"-{random_seed}"
    for image in images:
        image_path = available_file(stable_dir, fname, 1)
        image.save(image_path)
        out_path = image_path
        prt(Row([Img(src=image_path, width=width, height=height, fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        #TODO: ESRGAN, Metadata & PyDrive
        if storage_type == "Colab Google Drive":
            new_file = available_file(prefs['image_output'], fname, 1)
            out_path = new_file
            shutil.copy(image_path, new_file)
        elif bool(prefs['image_output']):
            new_file = available_file(prefs['image_output'], fname, 1)
            out_path = new_file
            shutil.copy(image_path, new_file)
        prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_CLIPstyler(page):
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.image2text_output.controls.append(line)
      page.image2text_output.update()
    def clear_last():
      del page.image2text_output.controls[-1]
      page.image2text_output.update()
    clipstyler_dir = os.path.join(root_dir, "CLIPstyler")
    if not os.path.exists(clipstyler_dir):
          os.mkdir(clipstyler_dir)
    if CLIPstyler_prefs['original_image'].startswith('http'):
        import requests
        from io import BytesIO
        response = requests.get(CLIPstyler_prefs['original_image'])
        fpath = os.path.join(clipstyler_dir, CLIPstyler_prefs['original_image'].rpartition(slash)[2])
        original_img = PILImage.open(BytesIO(response.content)).convert("RGB")
        #width, height = original_img.size
        #width, height = scale_dimensions(width, height)
        original_img = original_img.resize((CLIPstyler_prefs['width'], CLIPstyler_prefs['height']), resample=PILImage.LANCZOS).convert("RGB")
        original_img.save(fpath)
        CLIPstyler_prefs['image_dir'] = fpath
    elif os.path.isfile(CLIPstyler_prefs['original_image']):
        fpath = os.path.join(clipstyler_dir, CLIPstyler_prefs['original_image'].rpartition(slash)[2])
        original_img = PILImage.open(CLIPstyler_prefs['original_image'])
        #width, height = original_img.size
        #width, height = scale_dimensions(width, height)
        original_img = original_img.resize((CLIPstyler_prefs['width'], CLIPstyler_prefs['height']), resample=PILImage.LANCZOS).convert("RGB")
        original_img.save(fpath)
        CLIPstyler_prefs['image_dir'] = fpath
    else:
        alert_msg(page, "Couldn't find a valid File, Path or URL...")
        return
    progress = ProgressBar(bar_height=8)
    prt(Row([ProgressRing(), Text(" Downloading CLIP-Styler Packages...", weight=FontWeight.BOLD)]))
    run_process("pip install ftfy regex tqdm", realtime=False, page=page)
    run_sp("pip install git+https://github.com/openai/CLIP.git", realtime=False)
    #os.chdir(clipstyler_dir)
    os.chdir(root_dir)
    run_sp("pip install git+https://github.com/cyclomon/CLIPstyler.git", realtime=True)
    #!git clone https://github.com/cyclomon/CLIPstyler/
    run_sp(f"git clone https://github.com/cyclomon/CLIPstyler/ {clipstyler_dir}", realtime=True)
    os.chdir(root_dir)
    #run_process(f"git clone https://github.com/paper11667/CLIPstyler/ {clipstyler_dir}", realtime=False, page=page)
    sys.path.append(clipstyler_dir)

    import numpy as np
    import torch
    import torch.nn
    import torch.optim as optim
    from torchvision import transforms, models
    import StyleNet
    import utils
    import clip
    import torch.nn.functional as F
    from template import imagenet_templates
    from torchvision import utils as vutils
    import argparse
    from torchvision.transforms.functional import adjust_contrast
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    VGG = models.vgg19(pretrained=True).features
    VGG.to(device)
    save_dir = stable_dir
    if bool(CLIPstyler_prefs['batch_folder_name']):
        save_dir = os.path.join(stable_dir, CLIPstyler_prefs['batch_folder_name'])
    new_file = format_filename(CLIPstyler_prefs["prompt_text"])
    images = []
    for parameter in VGG.parameters():
        parameter.requires_grad_(False)
        
    def img_denormalize(image):
        mean=torch.tensor([0.485, 0.456, 0.406]).to(device)
        std=torch.tensor([0.229, 0.224, 0.225]).to(device)
        mean = mean.view(1,-1,1,1)
        std = std.view(1,-1,1,1)
        image = image*std +mean
        return image

    def img_normalize(image):
        mean=torch.tensor([0.485, 0.456, 0.406]).to(device)
        std=torch.tensor([0.229, 0.224, 0.225]).to(device)
        mean = mean.view(1,-1,1,1)
        std = std.view(1,-1,1,1)
        image = (image-mean)/std
        return image

    def clip_normalize(image,device):
        image = F.interpolate(image,size=224,mode='bicubic')
        mean=torch.tensor([0.48145466, 0.4578275, 0.40821073]).to(device)
        std=torch.tensor([0.26862954, 0.26130258, 0.27577711]).to(device)
        mean = mean.view(1,-1,1,1)
        std = std.view(1,-1,1,1)
        image = (image-mean)/std
        return image
        
    def get_image_prior_losses(inputs_jit):
        diff1 = inputs_jit[:, :, :, :-1] - inputs_jit[:, :, :, 1:]
        diff2 = inputs_jit[:, :, :-1, :] - inputs_jit[:, :, 1:, :]
        diff3 = inputs_jit[:, :, 1:, :-1] - inputs_jit[:, :, :-1, 1:]
        diff4 = inputs_jit[:, :, :-1, :-1] - inputs_jit[:, :, 1:, 1:]
        loss_var_l2 = torch.norm(diff1) + torch.norm(diff2) + torch.norm(diff3) + torch.norm(diff4)
        return loss_var_l2

    from argparse import Namespace
    source = CLIPstyler_prefs['source']

    training_args = {
        "lambda_tv": 2e-3,
        "lambda_patch": 9000,
        "lambda_dir": 500,
        "lambda_c": 150,
        "crop_size": CLIPstyler_prefs['crop_size'],
        "num_crops":CLIPstyler_prefs['num_crops'],
        "img_height":CLIPstyler_prefs['height'],
        "img_width":CLIPstyler_prefs['width'],
        "max_step":CLIPstyler_prefs['training_iterations'],
        "lr":5e-4,
        "thresh":0.7,
        "content_path":CLIPstyler_prefs['image_dir'],
        "text":CLIPstyler_prefs['prompt_text']
    }

    style_args = Namespace(**training_args)

    def compose_text_with_templates(text: str, templates=imagenet_templates) -> list:
        return [template.format(text) for template in templates]

    content_path = style_args.content_path
    content_image = utils.load_image2(content_path, img_height=style_args.img_height,img_width =style_args.img_width)
    content_image = content_image.to(device)
    content_features = utils.get_features(img_normalize(content_image), VGG)
    target = content_image.clone().requires_grad_(True).to(device)
    style_net = StyleNet.UNet()
    style_net.to(device)

    style_weights = {'conv1_1': 0.1,
                    'conv2_1': 0.2,
                    'conv3_1': 0.4,
                    'conv4_1': 0.8,
                    'conv5_1': 1.6}
    clear_last()
    prt("Generating Stylized Image from your source... Check console output for progress.")
    prt(progress)

    content_weight = style_args.lambda_c
    show_every = 20
    optimizer = optim.Adam(style_net.parameters(), lr=style_args.lr)
    s_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=100, gamma=0.5)
    steps = style_args.max_step
    content_loss_epoch = []
    style_loss_epoch = []
    total_loss_epoch = []
    output_image = content_image
    m_cont = torch.mean(content_image,dim=(2,3),keepdim=False).squeeze(0)
    m_cont = [m_cont[0].item(),m_cont[1].item(),m_cont[2].item()]
    cropper = transforms.Compose([transforms.RandomCrop(style_args.crop_size)])
    augment = transforms.Compose([
        transforms.RandomPerspective(fill=0, p=1,distortion_scale=0.5),
        transforms.Resize(224)
    ])

    clip_model, preprocess = clip.load('ViT-B/32', device, jit=False)
    prompt = style_args.text

    with torch.no_grad():
        template_text = compose_text_with_templates(prompt, imagenet_templates)
        tokens = clip.tokenize(template_text).to(device)
        text_features = clip_model.encode_text(tokens).dcrop_sizech()
        text_features = text_features.mean(axis=0, keepdim=True)
        text_features /= text_features.norm(dim=-1, keepdim=True)
        template_source = compose_text_with_templates(source, imagenet_templates)
        tokens_source = clip.tokenize(template_source).to(device)
        text_source = clip_model.encode_text(tokens_source).dcrop_sizech()
        text_source = text_source.mean(axis=0, keepdim=True)
        text_source /= text_source.norm(dim=-1, keepdim=True)
        source_features = clip_model.encode_image(clip_normalize(content_image,device))
        source_features /= (source_features.clone().norm(dim=-1, keepdim=True))

        
    num_crops = style_args.num_crops
    for epoch in range(0, steps+1):
        s_scheduler.step()
        target = style_net(content_image,use_sigmoid=True).to(device)
        target.requires_grad_(True)
        target_features = utils.get_features(img_normalize(target), VGG)
        content_loss = 0
        content_loss += torch.mean((target_features['conv4_2'] - content_features['conv4_2']) ** 2)
        content_loss += torch.mean((target_features['conv5_2'] - content_features['conv5_2']) ** 2)
        loss_patch=0 
        img_proc =[]
        for n in range(num_crops):
            target_crop = cropper(target)
            target_crop = augment(target_crop)
            img_proc.append(target_crop)
        img_proc = torch.cat(img_proc,dim=0)
        img_aug = img_proc
        image_features = clip_model.encode_image(clip_normalize(img_aug,device))
        image_features /= (image_features.clone().norm(dim=-1, keepdim=True))
        img_direction = (image_features-source_features)
        img_direction /= img_direction.clone().norm(dim=-1, keepdim=True)
        text_direction = (text_features-text_source).repeat(image_features.size(0),1)
        text_direction /= text_direction.norm(dim=-1, keepdim=True)
        loss_temp = (1- torch.cosine_similarity(img_direction, text_direction, dim=1))
        loss_temp[loss_temp<style_args.thresh] =0
        loss_patch+=loss_temp.mean()
        glob_features = clip_model.encode_image(clip_normalize(target,device))
        glob_features /= (glob_features.clone().norm(dim=-1, keepdim=True))
        glob_direction = (glob_features-source_features)
        glob_direction /= glob_direction.clone().norm(dim=-1, keepdim=True)
        loss_glob = (1- torch.cosine_similarity(glob_direction, text_direction, dim=1)).mean()
        reg_tv = style_args.lambda_tv*get_image_prior_losses(target)
        total_loss = style_args.lambda_patch*loss_patch + content_weight * content_loss+ reg_tv+ style_args.lambda_dir*loss_glob
        total_loss_epoch.append(total_loss)
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()

        if epoch % show_every == 0:
            prt("After %d iters:" % epoch)
            prt('  Total loss: ', total_loss.item())
            prt('  Content loss: ', content_loss.item())
            prt('  patch loss: ', loss_patch.item())
            prt('  dir loss: ', loss_glob.item())
            prt('  TV loss: ', reg_tv.item())
        
        if epoch % show_every == 0:
            output_image = target.clone()
            output_image = torch.clamp(output_image,0,1)
            output_image = adjust_contrast(output_image,1.5)
            img = utils.im_convert2(output_image)
            save_file = available_file(save_dir, new_file, 1)
            img.save(save_file)
            prt(Row([Img(src=save_file, width=CLIPstyler_prefs['width'], height=CLIPstyler_prefs['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
            prt(Row([Text(save_file)], alignment=MainAxisAlignment.CENTER))
            images.append(save_file)
            #plt.imshow(utils.im_convert2(output_image))
            #plt.show()
        progress.value = (epoch) / steps
        progress.tooltip = f'[{(epoch)} / {steps}]'
        progress.update()
    #clear_last()
    # TODO: ESRGAN and copy to GDrive and Metadata
    if prefs['enable_sounds']: page.snd_alert.play()

def run_image2text(page):
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.image2text_output.controls.append(line)
      page.image2text_output.update()
    def clear_last():
      del page.image2text_output.controls[-1]
      page.image2text_output.update()
    progress = ProgressBar(bar_height=8)
    #if not status['installed_diffusers']:
    #  alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
    #  return
    prt(Row([ProgressRing(), Text(" Downloading Image2Text CLIP-Interrogator Blips...", weight=FontWeight.BOLD)]))
    #try:
    #    import clip
    #except ModuleNotFoundError:
    try:
        if transformers.__version__ != "4.21.3": # Diffusers conflict
          run_process("pip uninstall -y transformers", realtime=False)
    except Exception:
        pass
    run_process("pip install ftfy regex tqdm timm fairscale requests", realtime=False)
    #run_sp("pip install --upgrade transformers==4.21.2", realtime=False)
    run_process("pip install -q transformers==4.21.3 --upgrade --force-reinstall", realtime=False)
    run_process("pip install -e git+https://github.com/openai/CLIP.git@main#egg=clip", realtime=False)
    run_process("pip install -e git+https://github.com/pharmapsychotic/BLIP.git@lib#egg=blip", realtime=False)
    run_process("pip clone https://github.com/pharmapsychotic/clip-interrogator.git", realtime=False)
        #['pip', 'install', 'ftfy', 'gradio', 'regex', 'tqdm', 'transformers==4.21.2', 'timm', 'fairscale', 'requests'],
    #    pass
    # Have to force downgrade of transformers because error with cache_dir, but should upgrade after run
    run_process("pip install clip-interrogator", realtime=False)
    
    '''def setup():
        install_cmds = [
            ['pip', 'install', 'ftfy', 'gradio', 'regex', 'tqdm', 'transformers==4.21.2', 'timm', 'fairscale', 'requests'],
            ['pip', 'install', 'git+https://github.com/openai/CLIP.git@main#egg=clip'],
            ['pip', 'install', 'git+https://github.com/pharmapsychotic/BLIP.git@lib#egg=blip'],
            ['git', 'clone', 'https://github.com/pharmapsychotic/clip-interrogator.git'],
            ['pip', 'install', 'clip-interrogator'],
        ]
        for cmd in install_cmds:
            print(subprocess.run(cmd, stdout=subprocess.PIPE).stdout.decode('utf-8'))
    setup()'''
    #run_sp("pip install git+https://github.com/openai/CLIP.git", realtime=False)
    import argparse, sys, time
    sys.path.append('src/blip')
    sys.path.append('src/clip')
    sys.path.append('clip-interrogator')
    import clip
    import torch
    from clip_interrogator import Interrogator, Config
    clear_last()
    prt("Interrogating Images to Describe Prompt... Check console output for progress.")
    prt(progress)
    ci = Interrogator(Config())
    '''try:
    except Exception as e:
        clear_last()
        alert_msg(page, "ERROR: Problem running Interrogator, check settings and try again...", content=Text(str(e)))
        pass'''
    def inference(image, mode):
        nonlocal ci
        image = image.convert('RGB')
        if mode == 'best':
            return ci.interrogate(image)
        elif mode == 'classic':
            return ci.interrogate_classic(image)
        else:
            return ci.interrogate_fast(image)
    folder_path = image2text_prefs['folder_path']
    mode = image2text_prefs['mode'] #'best' #param ["best","classic", "fast"]
    files = [f for f in os.listdir(folder_path) if f.endswith('.jpg') or  f.endswith('.png')] if os.path.exists(folder_path) else []
    clear_last()
    i2t_prompts = []
    for file in files:
        image = PILImage.open(os.path.join(folder_path, file)).convert('RGB')
        prompt = inference(image, mode)
        i2t_prompts.append(prompt)
        page.add_to_image2text(prompt)
        #thumb = image.copy()
        #thumb.thumbnail([256, 256])
        #display(thumb)
        #print(prompt)
    if image2text_prefs['save_csv']:
        if len(i2t_prompts):
            import csv
            csv_path = os.path.join(folder_path, 'img2txt_prompts.csv')
            with open(csv_path, 'w', encoding='utf-8', newline='') as f:
                w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
                w.writerow(['image', 'prompt'])
                for file, prompt in zip(files, i2t_prompts):
                    w.writerow([file, prompt])

            prt(f"\n\n\nGenerated {len(i2t_prompts)} and saved to {csv_path}, enjoy!")
        else:
            prt(f"Sorry, we couldn't find any images in {folder_path}")
    run_process("pip uninstall -y git+https://github.com/pharmapsychotic/BLIP.git@lib#egg=blip", realtime=False)
    run_process("pip uninstall -y clip-interrogator", realtime=False)
    run_process("pip uninstall -y transformers", realtime=False)
    run_process("pip install --upgrade transformers", realtime=False)
    clear_last()
    if prefs['enable_sounds']: page.snd_alert.play()

def run_dance_diffusion(page):
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    global dance_pipe, dance_prefs
    if dance_prefs['dance_model'] == 'Community':
      alert_msg(page, "Custom Community Checkpoints are not functional yet, working on it so check back later... ")
      return
    from diffusers import DanceDiffusionPipeline
    import scipy.io.wavfile, random
    try:
      import gdown
    except ImportError:
      run_sp("pip install gdown")
    finally:
      import gdown
    #import sys
    #sys.path.append('drive/gdrive/MyDrive/NotebookDatasets/CMVRLG')
    #print(dir(os))
    #print(dir(os.path))
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.dance_output.controls.append(line)
      page.dance_output.update()
    def clear_last():
      del page.dance_output.controls[-1]
      page.dance_output.update()
    def play_audio(e):
      e.control.data.play()
    prt(Row([ProgressRing(), Text(" Downloading Dance Diffusion Models", weight=FontWeight.BOLD)]))
    dance_model_file = f"harmonai/{dance_prefs['dance_model']}"
    if dance_prefs['dance_model'] == 'Community':
      models_path = os.path.join(root_dir, 'models')
      os.makedirs(models_path, exist_ok=True)
      for c in community_models:
        if c['name'] == dance_prefs['community_model']:
          community = c
      if bool(community['download']):
        dance_model_file = os.path.join(models_path, community['ckpt'])
        gdown.download(community['download'], dance_model_file, quiet=True)
        #run_sp(f'gdown {community['download']} {dance_model_file}')
        #run_sp(f"wget {community['download']} -O {models_path}")
    dance_pipe = DanceDiffusionPipeline.from_pretrained(dance_model_file, torch_dtype=torch.float16, device_map="auto")
    dance_pipe = dance_pipe.to(torch_device)
    dance_pipe.set_progress_bar_config(disable=True)
    random_seed = int(dance_prefs['seed']) if int(dance_prefs['seed']) > 0 else random.randint(0,4294967295)
    dance_generator = torch.Generator(device=torch_device).manual_seed(random_seed)
    clear_last()
    pb.width=page.width - 50
    prt(pb)
    if prefs['higher_vram_mode']:
      output = dance_pipe(generator=dance_generator, batch_size=int(dance_prefs['batch_size']), num_inference_steps=int(dance_prefs['inference_steps']), audio_length_in_s=float(dance_prefs['audio_length_in_s']))
    else:
      output = dance_pipe(generator=dance_generator, batch_size=int(dance_prefs['batch_size']), num_inference_steps=int(dance_prefs['inference_steps']), audio_length_in_s=float(dance_prefs['audio_length_in_s']), torch_dtype=torch.float16)
    #, callback=callback_fn, callback_steps=1)
    audio = output.audios
    audio_slice = audio[0, -3:, -3:]
    clear_last()
    #prt(f'audio: {type(audio[0])}, audio_slice: {type(audio_slice)}, len:{len(audio)}')
    #audio_slice.tofile("/content/dance-test.wav")
    audio_name = f"dance-{dance_prefs['dance_model']}" + (f"-{random_seed}" if prefs['file_suffix_seed'] else '')
    audio_local = os.path.join(root_dir, "audio_out")
    audio_out = audio_local
    os.makedirs(audio_local, exist_ok=True)
    if storage_type == "Colab Google Drive":
      audio_out = prefs['image_output'].rpartition(slash)[0] + slash + 'audio_out'
      os.makedirs(audio_out, exist_ok=True)
    i = 0
    for a in audio:
      fname = available_file(audio_local, audio_name, i, ext="wav")
      scipy.io.wavfile.write(fname, dance_pipe.unet.sample_rate, a.transpose())
      os.path.abspath(fname)
      a_out = Audio(src=fname, autoplay=False)
      page.overlay.append(a_out)
      page.update()
      display_name = fname
      #a.tofile(f"/content/dance-{i}.wav")
      if storage_type == "Colab Google Drive":
        audio_save = available_file(audio_out, audio_name, i, ext='wav')
        shutil.copy(fname, audio_save)
        display_name = audio_save
      prt(Row([IconButton(icon=icons.PLAY_CIRCLE_FILLED, icon_size=48, on_click=play_audio, data=a_out), Text(display_name)]))
      i += 1
    if prefs['enable_sounds']: page.snd_alert.play()


# https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb
def run_dreambooth(page):
    global dreambooth_prefs, prefs
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.dreambooth_output.controls.append(line)
      page.dreambooth_output.update()
    def clear_last():
      del page.dreambooth_output.controls[-1]
      page.dreambooth_output.update()
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    save_path = os.path.join(root_dir, "my_concept")
    error = False
    if not os.path.exists(save_path):
      error = True
    elif len(os.listdir(save_path)) == 0:
      error = True
    if len(page.file_list.controls) == 0:
      error = True
    if error:
      alert_msg(page, "Couldn't find a list of images to train concept. Add image files to the list...")
      return
    prt(Row([ProgressRing(), Text(" Downloading DreamBooth Conceptualizers", weight=FontWeight.BOLD)]))
    run_process("pip install -qq bitsandbytes")
    import argparse
    import itertools
    import math
    from contextlib import nullcontext
    import random
    import numpy as np
    import torch
    import torch.nn.functional as F
    import torch.utils.checkpoint
    from torch.utils.data import Dataset
    from accelerate import Accelerator
    from accelerate.logging import get_logger
    from accelerate.utils import set_seed
    from diffusers import AutoencoderKL, DDPMScheduler, PNDMScheduler, StableDiffusionPipeline, UNet2DConditionModel
    from diffusers.hub_utils import init_git_repo, push_to_hub
    from diffusers.optimization import get_scheduler
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
    
    from torchvision import transforms
    from tqdm.auto import tqdm
    from transformers import CLIPFeatureExtractor, CLIPTextModel, CLIPTokenizer
    import bitsandbytes as bnb
    import gc
    import glob
    from io import BytesIO
    from PIL import Image as PILImage

    def download_image(url):
      try:
        response = requests.get(url)
      except:
        return None
      return PILImage.open(BytesIO(response.content)).convert("RGB")
    #images = list(filter(None,[download_image(url) for url in dreambooth_prefs['urls']]))
    #save_path = "./my_concept"
    #if not os.path.exists(save_path):
    #  os.mkdir(save_path)
    #[image.save(f"{save_path}/{i}.jpeg") for i, image in enumerate(images)]
    #image_grid(images, 1, len(images))

    prior_preservation_class_folder = dreambooth_prefs['prior_preservation_class_folder']
    class_data_root=prior_preservation_class_folder
    class_prompt=dreambooth_prefs['prior_preservation_class_prompt']
    class_data_root=prior_preservation_class_folder
    dreambooth_prefs['instance_prompt'] = dreambooth_prefs['instance_prompt'].strip()
    clear_txt2img_pipe()
    clear_img2img_pipe()
    clear_unet_pipe()
    clear_clip_guided_pipe()
    num_new_images = None
    if(dreambooth_prefs['prior_preservation']):
        class_images_dir = Path(class_data_root)
        if not class_images_dir.exists():
            class_images_dir.mkdir(parents=True)
        cur_class_images = len(list(class_images_dir.iterdir()))

        if cur_class_images < dreambooth_prefs['num_class_images']:
            if prefs['higher_vram_mode']:
              pipeline = StableDiffusionPipeline.from_pretrained(model_path).to("cuda")
            else:
              pipeline = StableDiffusionPipeline.from_pretrained(model_path, revision="fp16", torch_dtype=torch.float16).to("cuda")
            if prefs['enable_attention_slicing']:
              pipeline.enable_attention_slicing()
            pipeline.set_progress_bar_config(disable=True)

            num_new_images = dreambooth_prefs['num_class_images'] - cur_class_images
            print(f"Number of class images to sample: {num_new_images}.")

            sample_dataset = PromptDataset(class_prompt, num_new_images)
            sample_dataloader = torch.utils.data.DataLoader(sample_dataset, batch_size=dreambooth_prefs['sample_batch_size'])

            for example in tqdm(sample_dataloader, desc="Generating class images"):
                images = pipeline(example["prompt"]).images

                for i, image in enumerate(images):
                    image.save(class_images_dir / f"{example['index'][i] + cur_class_images}.jpg")
            pipeline = None
            gc.collect()
            del pipeline
            with torch.no_grad():
              torch.cuda.empty_cache()
    text_encoder = CLIPTextModel.from_pretrained(model_path, subfolder="text_encoder")
    vae = AutoencoderKL.from_pretrained(model_path, subfolder="vae")
    unet = UNet2DConditionModel.from_pretrained(model_path, subfolder="unet")
    tokenizer = CLIPTokenizer.from_pretrained(model_path,subfolder="tokenizer")
    
    from argparse import Namespace
    dreambooth_args = Namespace(
        pretrained_model_name_or_path=model_path,
        resolution=dreambooth_prefs['max_size'],
        center_crop=True,
        instance_data_dir=save_path,
        instance_prompt=dreambooth_prefs['instance_prompt'],
        learning_rate=dreambooth_prefs['learning_rate'],#5e-06,
        max_train_steps=dreambooth_prefs['max_train_steps'],#450,
        train_batch_size=1,
        gradient_accumulation_steps=2,
        max_grad_norm=1.0,
        mixed_precision="no", # set to "fp16" for mixed-precision training.
        gradient_checkpointing=True, # set this to True to lower the memory usage.
        use_8bit_adam=not prefs['higher_vram_mode'], # use 8bit optimizer from bitsandbytes
        seed=dreambooth_prefs['seed'],#3434554,
        with_prior_preservation=dreambooth_prefs['prior_preservation'], 
        prior_loss_weight=dreambooth_prefs['prior_loss_weight'],
        sample_batch_size=dreambooth_prefs['sample_batch_size'],
        class_data_dir=dreambooth_prefs['prior_preservation_class_folder'], 
        class_prompt=class_prompt, 
        num_class_images=dreambooth_prefs['num_class_images'], 
        output_dir="dreambooth-concept",
    )

    from accelerate.utils import set_seed
    def training_function(text_encoder, vae, unet):
        logger = get_logger(__name__)

        accelerator = Accelerator(
            gradient_accumulation_steps=dreambooth_args.gradient_accumulation_steps,
            mixed_precision=dreambooth_args.mixed_precision,
        )

        set_seed(dreambooth_args.seed)

        if dreambooth_args.gradient_checkpointing:
            unet.enable_gradient_checkpointing()

        # Use 8-bit Adam for lower memory usage or to fine-tune the model in 16GB GPUs
        if dreambooth_args.use_8bit_adam:
            optimizer_class = bnb.optim.AdamW8bit
        else:
            optimizer_class = torch.optim.AdamW

        optimizer = optimizer_class(unet.parameters(),lr=dreambooth_args.learning_rate)

        noise_scheduler = DDPMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000)
        
        train_dataset = DreamBoothDataset(
            instance_data_root=dreambooth_args.instance_data_dir,
            instance_prompt=dreambooth_args.instance_prompt,
            class_data_root=dreambooth_args.class_data_dir if dreambooth_args.with_prior_preservation else None,
            class_prompt=dreambooth_args.class_prompt,
            tokenizer=tokenizer,
            size=dreambooth_args.resolution,
            center_crop=dreambooth_args.center_crop,
        )

        def collate_fn(examples):
            input_ids = [example["instance_prompt_ids"] for example in examples]
            pixel_values = [example["instance_images"] for example in examples]

            # concat class and instance examples for prior preservation
            if dreambooth_args.with_prior_preservation:
                input_ids += [example["class_prompt_ids"] for example in examples]
                pixel_values += [example["class_images"] for example in examples]

            pixel_values = torch.stack(pixel_values)
            pixel_values = pixel_values.to(memory_format=torch.contiguous_format).float()

            input_ids = tokenizer.pad({"input_ids": input_ids}, padding=True, return_tensors="pt").input_ids

            batch = {
                "input_ids": input_ids,
                "pixel_values": pixel_values,
            }
            return batch
        
        train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=dreambooth_args.train_batch_size, shuffle=True, collate_fn=collate_fn)
        unet, optimizer, train_dataloader = accelerator.prepare(unet, optimizer, train_dataloader)

        # Move text_encode and vae to gpu
        text_encoder.to(accelerator.device)
        vae.to(accelerator.device)

        # We need to recalculate our total training steps as the size of the training dataloader may have changed.
        num_update_steps_per_epoch = math.ceil(len(train_dataloader) / dreambooth_args.gradient_accumulation_steps)
        num_train_epochs = math.ceil(dreambooth_args.max_train_steps / num_update_steps_per_epoch)
        clear_last()
        total_batch_size = dreambooth_args.train_batch_size * accelerator.num_processes * dreambooth_args.gradient_accumulation_steps

        prt("***** Running training *****")
        prt(f"  Number of examples = {len(train_dataset)}")
        if num_new_images != None: prt(f"  Number of class images to sample: {num_new_images}.")
        prt(f"  Instantaneous batch size per device = {dreambooth_args.train_batch_size}")
        prt(f"  Total train batch size (w. parallel, distributed & accumulation) = {total_batch_size}")
        prt(f"  Gradient Accumulation steps = {dreambooth_args.gradient_accumulation_steps}")
        prt(f"  Total optimization steps = {dreambooth_args.max_train_steps}")
        progress = ProgressBar(bar_height=8)
        prt(progress)
        progress_bar = tqdm(range(dreambooth_args.max_train_steps), disable=not accelerator.is_local_main_process)
        progress_bar.set_description("Steps")
        global_step = 0

        for epoch in range(num_train_epochs):
            unet.train()
            for step, batch in enumerate(train_dataloader):
                with accelerator.accumulate(unet):
                    # Convert images to latent space
                    with torch.no_grad():
                        latents = vae.encode(batch["pixel_values"]).latent_dist.sample()
                        latents = latents * 0.18215

                    # Sample noise that we'll add to the latents
                    noise = torch.randn(latents.shape).to(latents.device)
                    bsz = latents.shape[0]
                    # Sample a random timestep for each image
                    timesteps = torch.randint(0, noise_scheduler.config.num_train_timesteps, (bsz,), device=latents.device).long()

                    # Add noise to the latents according to the noise magnitude at each timestep
                    # (this is the forward diffusion process)
                    noisy_latents = noise_scheduler.add_noise(latents, noise, timesteps)

                    # Get the text embedding for conditioning
                    with torch.no_grad():
                        encoder_hidden_states = text_encoder(batch["input_ids"])[0]

                    # Predict the noise residual
                    noise_pred = unet(noisy_latents, timesteps, encoder_hidden_states).sample

                    if dreambooth_args.with_prior_preservation:
                        # Chunk the noise and noise_pred into two parts and compute the loss on each part separately.
                        noise_pred, noise_pred_prior = torch.chunk(noise_pred, 2, dim=0)
                        noise, noise_prior = torch.chunk(noise, 2, dim=0)

                        # Compute instance loss
                        loss = F.mse_loss(noise_pred, noise, reduction="none").mean([1, 2, 3]).mean()

                        # Compute prior loss
                        prior_loss = F.mse_loss(noise_pred_prior, noise_prior, reduction="none").mean([1, 2, 3]).mean()

                        # Add the prior loss to the instance loss.
                        loss = loss + dreambooth_args.prior_loss_weight * prior_loss
                    else:
                        loss = F.mse_loss(noise_pred, noise, reduction="none").mean([1, 2, 3]).mean()

                    accelerator.backward(loss)
                    if accelerator.sync_gradients:
                        accelerator.clip_grad_norm_(unet.parameters(), dreambooth_args.max_grad_norm)
                    optimizer.step()
                    optimizer.zero_grad()

                # Checks if the accelerator has performed an optimization step behind the scenes
                if accelerator.sync_gradients:
                    progress_bar.update(1)
                    global_step += 1

                logs = {"loss": loss.detach().item()}
                progress_bar.set_postfix(**logs)
                progress.value = (global_step + 1) / dreambooth_args.max_train_steps
                progress.tooltip = f'[{(global_step + 1)} / {dreambooth_args.max_train_steps}]'
                progress.update()

                if global_step >= dreambooth_args.max_train_steps:
                    break

            accelerator.wait_for_everyone()
        
        # Create the pipeline using the trained modules and save it.
        if accelerator.is_main_process:
            pipeline = StableDiffusionPipeline(
                text_encoder=text_encoder,
                vae=vae,
                unet=accelerator.unwrap_model(unet),
                tokenizer=tokenizer,
                scheduler=PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", skip_prk_steps=True),
                safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
                feature_extractor=CLIPFeatureExtractor.from_pretrained("openai/clip-vit-base-patch32"),
            )
            pipeline.save_pretrained(dreambooth_args.output_dir)
    
    import accelerate
    try:
      accelerate.notebook_launcher(training_function, args=(text_encoder, vae, unet))
    except Exception as e:
      clear_last()
      alert_msg(page, "ERROR: CUDA Ran Out of Memory. Try reducing parameters and try again...", content=Text(str(e)))
      with torch.no_grad():
        torch.cuda.empty_cache()
      return
    clear_last()
    with torch.no_grad():
        torch.cuda.empty_cache()
    name_of_your_concept = dreambooth_prefs['name_of_your_concept']
    if(dreambooth_prefs['save_concept']):
      from slugify import slugify
      from huggingface_hub import HfApi, HfFolder, CommitOperationAdd
      from huggingface_hub import create_repo
      from IPython.display import display_markdown
      api = HfApi()
      your_username = api.whoami()["name"]
      dreambooth_pipe = StableDiffusionPipeline.from_pretrained(
        dreambooth_args.output_dir,
        torch_dtype=torch.float16,
      ).to("cuda")
      os.makedirs("fp16_model",exist_ok=True)
      dreambooth_pipe.save_pretrained("fp16_model")

      if(dreambooth_prefs['where_to_save_concept'] == "Public Library"):
        repo_id = f"sd-dreambooth-library/{slugify(name_of_your_concept)}"
        #Join the Concepts Library organization if you aren't part of it already
        run_sp(f"curl -X POST -H 'Authorization: Bearer '{hf_token} -H 'Content-Type: application/json' https://huggingface.co/organizations/sd-dreambooth-library/share/SSeOwppVCscfTEzFGQaqpfcjukVeNrKNHX", realtime=False)
        #!curl -X POST -H 'Authorization: Bearer '$hf_token -H 'Content-Type: application/json' https://huggingface.co/organizations/sd-dreambooth-library/share/SSeOwppVCscfTEzFGQaqpfcjukVeNrKNHX
      else:
        repo_id = f"{your_username}/{slugify(name_of_your_concept)}"
      output_dir = dreambooth_args.output_dir
      if(not prefs['HuggingFace_api_key']):
        with open(HfFolder.path_token, 'r') as fin: hf_token = fin.read();
      else:
        hf_token = prefs['HuggingFace_api_key'] 
      
      images_upload = os.listdir(save_path)
      image_string = ""
      #repo_id = f"sd-dreambooth-library/{slugify(name_of_your_concept)}"
      for i, image in enumerate(images_upload):
          image_string = f'''{image_string}![image {i}](https://huggingface.co/{repo_id}/resolve/main/concept_images/{image})
    '''
      description = dreambooth_prefs['readme_description']
      if bool(description.strip()):
        description = dreambooth_prefs['readme_description'] + '\n\n'
      readme_text = f'''---
    license: mit
    ---
    ### {name_of_your_concept} on Stable Diffusion via Dreambooth using [Stable Diffusion Deluxe](https://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb)
    #### model by {api.whoami()["name"]}
    This your the Stable Diffusion model fine-tuned the {name_of_your_concept} concept taught to Stable Diffusion with Dreambooth.
    It can be used by modifying the `instance_prompt`: **{dreambooth_prefs['instance_prompt']}**

    {description}You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
    And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb), [Spaces with the Public Concepts loaded](https://huggingface.co/spaces/sd-dreambooth-library/stable-diffusion-dreambooth-concepts)

    Here are the images used for training this concept:
    {image_string}
    '''
      #Save the readme to a file
      readme_file = open("README.md", "w")
      readme_file.write(readme_text)
      readme_file.close()
      #Save the token identifier to a file
      text_file = open("token_identifier.txt", "w")
      text_file.write(dreambooth_prefs['instance_prompt'])
      text_file.close()
      operations = [
        CommitOperationAdd(path_in_repo="token_identifier.txt", path_or_fileobj="token_identifier.txt"),
        CommitOperationAdd(path_in_repo="README.md", path_or_fileobj="README.md"),
      ]
      create_repo(repo_id,private=True, token=hf_token)
      
      api.create_commit(repo_id=repo_id, operations=operations, commit_message=f"Upload the concept {name_of_your_concept} embeds and token",token=hf_token)
      api.upload_folder(folder_path="fp16_model", path_in_repo="", repo_id=repo_id,token=hf_token)
      api.upload_folder(folder_path=save_path, path_in_repo="concept_images", repo_id=repo_id, token=hf_token)
      prefs['custom_model'] = repo_id
      prt(Markdown(f"## Your concept was saved successfully to _{repo_id}_.<br>[Click here to access it](https://huggingface.co/{repo_id} and go to _Installers->Model Checkpoint->Custom Model Path_ to use. Include Token in prompts."))
    if prefs['enable_sounds']: page.snd_alert.play()

try:
    from torchvision import transforms
except Exception:
    run_sp("pip install torchvision", realtime=False)
    from torchvision import transforms
    pass
from torch.utils.data import Dataset

class DreamBoothDataset(Dataset):
    def __init__(
        self,
        instance_data_root,
        instance_prompt,
        tokenizer,
        class_data_root=None,
        class_prompt=None,
        size=dreambooth_prefs['max_size'],
        center_crop=False,
    ):
        self.size = size
        self.center_crop = center_crop
        self.tokenizer = tokenizer

        self.instance_data_root = Path(instance_data_root)
        if not self.instance_data_root.exists():
            raise ValueError("Instance images root doesn't exists.")

        self.instance_images_path = list(Path(instance_data_root).iterdir())
        self.num_instance_images = len(self.instance_images_path)
        self.instance_prompt = instance_prompt
        self._length = self.num_instance_images

        if class_data_root is not None:
            self.class_data_root = Path(class_data_root)
            self.class_data_root.mkdir(parents=True, exist_ok=True)
            self.class_images_path = list(Path(class_data_root).iterdir())
            self.num_class_images = len(self.class_images_path)
            self._length = max(self.num_class_images, self.num_instance_images)
            self.class_prompt = class_prompt
        else:
            self.class_data_root = None

        self.image_transforms = transforms.Compose(
            [
                transforms.Resize(size, interpolation=transforms.InterpolationMode.BILINEAR),
                transforms.CenterCrop(size) if center_crop else transforms.RandomCrop(size),
                transforms.ToTensor(),
                transforms.Normalize([0.5], [0.5]),
            ]
        )

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        from PIL import Image as PILImage
        example = {}
        instance_image = PILImage.open(self.instance_images_path[index % self.num_instance_images])
        if not instance_image.mode == "RGB":
            instance_image = instance_image.convert("RGB")
        example["instance_images"] = self.image_transforms(instance_image)
        example["instance_prompt_ids"] = self.tokenizer(
            self.instance_prompt,
            padding="do_not_pad",
            truncation=True,
            max_length=self.tokenizer.model_max_length,
        ).input_ids

        if self.class_data_root:
            class_image = PILImage.open(self.class_images_path[index % self.num_class_images])
            if not class_image.mode == "RGB":
                class_image = class_image.convert("RGB")
            example["class_images"] = self.image_transforms(class_image)
            example["class_prompt_ids"] = self.tokenizer(
                self.class_prompt,
                padding="do_not_pad",
                truncation=True,
                max_length=self.tokenizer.model_max_length,
            ).input_ids
        
        return example

class PromptDataset(Dataset):
    def __init__(self, prompt, num_samples):
        self.prompt = prompt
        self.num_samples = num_samples

    def __len__(self):
        return self.num_samples

    def __getitem__(self, index):
        example = {}
        example["prompt"] = self.prompt
        example["index"] = index
        return example


def run_textualinversion(page):
    global textualinversion_prefs, prefs
    def prt(line):
      if type(line) == str:
        line = Text(line)
      page.textualinversion_output.controls.append(line)
      page.textualinversion_output.update()
    def clear_last():
      del page.textualinversion_output.controls[-1]
      page.textualinversion_output.update()
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    save_path = os.path.join(root_dir, "my_concept")
    error = False
    if not os.path.exists(save_path):
      error = True
    elif len(os.listdir(save_path)) == 0:
      error = True
    if len(page.file_list.controls) == 0:
      error = True
    if error:
      alert_msg(page, "Couldn't find a list of images to train concept. Add image files to the list...")
      return
    prt(Row([ProgressRing(), Text(" Downloading Textual-Inversion Training Models", weight=FontWeight.BOLD)]))
    #run_process("pip install -qq bitsandbytes")
    import argparse
    import itertools
    import math
    import random

    import numpy as np
    import torch
    import torch.nn.functional as F
    import torch.utils.checkpoint
    from torch.utils.data import Dataset
    from accelerate import Accelerator
    from accelerate.logging import get_logger
    from accelerate.utils import set_seed
    from diffusers import AutoencoderKL, DDPMScheduler, PNDMScheduler, StableDiffusionPipeline, UNet2DConditionModel
    from diffusers.hub_utils import init_git_repo, push_to_hub
    from diffusers.optimization import get_scheduler
    from diffusers.pipelines.stable_diffusion import StableDiffusionSafetyChecker
    from torchvision import transforms
    from tqdm.auto import tqdm
    from transformers import CLIPFeatureExtractor, CLIPTextModel, CLIPTokenizer

    imagenet_templates_small = [
        "a photo of a {}",
        "a rendering of a {}",
        "a cropped photo of the {}",
        "the photo of a {}",
        "a photo of a clean {}",
        "a photo of a dirty {}",
        "a dark photo of the {}",
        "a photo of my {}",
        "a photo of the cool {}",
        "a close-up photo of a {}",
        "a bright photo of the {}",
        "a cropped photo of a {}",
        "a photo of the {}",
        "a good photo of the {}",
        "a photo of one {}",
        "a close-up photo of the {}",
        "a rendition of the {}",
        "a photo of the clean {}",
        "a rendition of a {}",
        "a photo of a nice {}",
        "a good photo of a {}",
        "a photo of the nice {}",
        "a photo of the small {}",
        "a photo of the weird {}",
        "a photo of the large {}",
        "a photo of a cool {}",
        "a photo of a small {}",
    ]

    imagenet_style_templates_small = [
        "a painting in the style of {}",
        "a rendering in the style of {}",
        "a cropped painting in the style of {}",
        "the painting in the style of {}",
        "a clean painting in the style of {}",
        "a dirty painting in the style of {}",
        "a dark painting in the style of {}",
        "a picture in the style of {}",
        "a cool painting in the style of {}",
        "a close-up painting in the style of {}",
        "a bright painting in the style of {}",
        "a cropped painting in the style of {}",
        "a good painting in the style of {}",
        "a close-up painting in the style of {}",
        "a rendition in the style of {}",
        "a nice painting in the style of {}",
        "a small painting in the style of {}",
        "a weird painting in the style of {}",
        "a large painting in the style of {}",
    ]
    tokenizer = CLIPTokenizer.from_pretrained(
        model_path,
        subfolder="tokenizer",
    )
    placeholder_token = textualinversion_prefs['placeholder_token'].strip()
    if not placeholder_token.startswith('<'): placeholder_token = '<' + placeholder_token
    if not placeholder_token.endswith('>'): placeholder_token = placeholder_token + '>'
    # Add the placeholder token in tokenizer
    num_added_tokens = tokenizer.add_tokens(placeholder_token)
    if num_added_tokens == 0:
        raise ValueError(
            f"The tokenizer already contains the token {placeholder_token}. Please pass a different"
            " `placeholder_token` that is not already in the tokenizer."
        )

    token_ids = tokenizer.encode(textualinversion_prefs['initializer_token'], add_special_tokens=False)
    # Check if initializer_token is a single token or a sequence of tokens
    if len(token_ids) > 1:
        raise ValueError("The initializer token must be a single token.")

    initializer_token_id = token_ids[0]
    placeholder_token_id = tokenizer.convert_tokens_to_ids(placeholder_token)

    # Load the Stable Diffusion model
    # Load models and create wrapper for stable diffusion
    text_encoder = CLIPTextModel.from_pretrained(
        model_path, subfolder="text_encoder"
    )
    vae = AutoencoderKL.from_pretrained(
        model_path, subfolder="vae"
    )
    unet = UNet2DConditionModel.from_pretrained(
        model_path, subfolder="unet"
    )

    text_encoder.resize_token_embeddings(len(tokenizer))
    token_embeds = text_encoder.get_input_embeddings().weight.data
    token_embeds[placeholder_token_id] = token_embeds[initializer_token_id]

    def freeze_params(params):
        for param in params:
            param.requires_grad = False

    # Freeze vae and unet
    freeze_params(vae.parameters())
    freeze_params(unet.parameters())
    # Freeze all parameters except for the token embeddings in text encoder
    params_to_freeze = itertools.chain(
        text_encoder.text_model.encoder.parameters(),
        text_encoder.text_model.final_layer_norm.parameters(),
        text_encoder.text_model.embeddings.position_embedding.parameters(),
    )
    freeze_params(params_to_freeze)
    train_dataset = TextualInversionDataset(
        data_root=save_path,
        tokenizer=tokenizer,
        size=512,
        placeholder_token=placeholder_token,
        repeats=100,
        learnable_property=textualinversion_prefs['what_to_teach'], #Option selected above between object and style
        center_crop=False,
        set="train",
    )
    def create_dataloader(train_batch_size=1):
        return torch.utils.data.DataLoader(train_dataset, batch_size=train_batch_size, shuffle=True)

    noise_scheduler = DDPMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", num_train_timesteps=1000, tensor_format="pt")
    def training_function(text_encoder, vae, unet):
        logger = get_logger(__name__)

        train_batch_size = textualinversion_prefs["train_batch_size"]
        gradient_accumulation_steps = textualinversion_prefs["gradient_accumulation_steps"]
        learning_rate = textualinversion_prefs["learning_rate"]
        max_train_steps = textualinversion_prefs["max_train_steps"]
        output_dir = textualinversion_prefs["output_dir"]
        accelerator = Accelerator(gradient_accumulation_steps=gradient_accumulation_steps)
        train_dataloader = create_dataloader(train_batch_size)
        if textualinversion_prefs["scale_lr"]:
            learning_rate = (learning_rate * gradient_accumulation_steps * train_batch_size * accelerator.num_processes)
        # Initialize the optimizer
        optimizer = torch.optim.AdamW(
            text_encoder.get_input_embeddings().parameters(),  # only optimize the embeddings
            lr=learning_rate,
        )
        text_encoder, optimizer, train_dataloader = accelerator.prepare(text_encoder, optimizer, train_dataloader)
        vae.to(accelerator.device)
        unet.to(accelerator.device)
        vae.eval()
        unet.eval()
        # We need to recalculate our total training steps as the size of the training dataloader may have changed.
        num_update_steps_per_epoch = math.ceil(len(train_dataloader) / gradient_accumulation_steps)
        num_train_epochs = math.ceil(max_train_steps / num_update_steps_per_epoch)
        clear_last()
        # Train!
        total_batch_size = train_batch_size * accelerator.num_processes * gradient_accumulation_steps

        prt("***** Running training *****")
        prt(f"  Num examples = {len(train_dataset)}")
        prt(f"  Instantaneous batch size per device = {train_batch_size}")
        prt(f"  Total train batch size (w. parallel, distributed & accumulation) = {total_batch_size}")
        prt(f"  Gradient Accumulation steps = {gradient_accumulation_steps}")
        prt(f"  Total optimization steps = {max_train_steps}")
        progress = ProgressBar(bar_height=8)
        prt(progress)
        progress_bar = tqdm(range(max_train_steps), disable=not accelerator.is_local_main_process)
        progress_bar.set_description("Steps")
        global_step = 0

        for epoch in range(num_train_epochs):
            text_encoder.train()
            for step, batch in enumerate(train_dataloader):
                with accelerator.accumulate(text_encoder):
                    # Convert images to latent space
                    latents = vae.encode(batch["pixel_values"]).latent_dist.sample().detach()
                    latents = latents * 0.18215

                    # Sample noise that we'll add to the latents
                    noise = torch.randn(latents.shape).to(latents.device)
                    bsz = latents.shape[0]
                    # Sample a random timestep for each image
                    timesteps = torch.randint(0, noise_scheduler.num_train_timesteps, (bsz,), device=latents.device).long()

                    # Add noise to the latents according to the noise magnitude at each timestep
                    # (this is the forward diffusion process)
                    noisy_latents = noise_scheduler.add_noise(latents, noise, timesteps)

                    # Get the text embedding for conditioning
                    encoder_hidden_states = text_encoder(batch["input_ids"])[0]

                    # Predict the noise residual
                    noise_pred = unet(noisy_latents, timesteps, encoder_hidden_states).sample

                    loss = F.mse_loss(noise_pred, noise, reduction="none").mean([1, 2, 3]).mean()
                    accelerator.backward(loss)

                    # Zero out the gradients for all token embeddings except the newly added
                    # embeddings for the concept, as we only want to optimize the concept embeddings
                    if accelerator.num_processes > 1:
                        grads = text_encoder.module.get_input_embeddings().weight.grad
                    else:
                        grads = text_encoder.get_input_embeddings().weight.grad
                    # Get the index for tokens that we want to zero the grads for
                    index_grads_to_zero = torch.arange(len(tokenizer)) != placeholder_token_id
                    grads.data[index_grads_to_zero, :] = grads.data[index_grads_to_zero, :].fill_(0)

                    optimizer.step()
                    optimizer.zero_grad()

                # Checks if the accelerator has performed an optimization step behind the scenes
                if accelerator.sync_gradients:
                    progress_bar.update(1)
                    global_step += 1
                    progress.value = (global_step + 1) / max_train_steps
                    progress.tooltip = f'[{(global_step + 1)} / {max_train_steps}]'
                    progress.update()

                logs = {"loss": loss.detach().item()}
                progress_bar.set_postfix(**logs)

                if global_step >= max_train_steps:
                    break

            accelerator.wait_for_everyone()


        # Create the pipeline using using the trained modules and save it.
        if accelerator.is_main_process:
            pipeline = StableDiffusionPipeline(
                text_encoder=accelerator.unwrap_model(text_encoder),
                vae=vae,
                unet=unet,
                tokenizer=tokenizer,
                scheduler=PNDMScheduler(beta_start=0.00085, beta_end=0.012, beta_schedule="scaled_linear", skip_prk_steps=True),
                safety_checker=None if prefs['disable_nsfw_filter'] else StableDiffusionSafetyChecker.from_pretrained("CompVis/stable-diffusion-safety-checker"),
                feature_extractor=CLIPFeatureExtractor.from_pretrained("openai/clip-vit-base-patch32"),
            )
            pipeline.save_pretrained(output_dir)
            # Also save the newly trained embeddings
            learned_embeds = accelerator.unwrap_model(text_encoder).get_input_embeddings().weight[placeholder_token_id]
            learned_embeds_dict = {placeholder_token: learned_embeds.detach().cpu()}
            torch.save(learned_embeds_dict, os.path.join(output_dir, "learned_embeds.bin"))
    
    import accelerate
    try:
        accelerate.notebook_launcher(training_function, args=(text_encoder, vae, unet))
    except Exception as e:
      clear_last()
      alert_msg(page, "ERROR: CUDA Ran Out of Memory. Try reducing parameters and try again...", content=Text(str(e)))
      with torch.no_grad():
        torch.cuda.empty_cache()
      return
    clear_last()
    #title Save your newly created concept to the [library of concepts](https://huggingface.co/sd-concepts-library)?
    save_concept_to_public_library = textualinversion_prefs['save_concept']
    name_of_your_concept = textualinversion_prefs['name_of_your_concept']
    # `hf_token_write`: leave blank if you logged in with a token with `write access` in the [Initial Setup](#scrollTo=KbzZ9xe6dWwf). If not, [go to your tokens settings and create a write access token](https://huggingface.co/settings/tokens)
    hf_token_write = prefs['HuggingFace_api_key']

    if(save_concept_to_public_library):
        from slugify import slugify
        from huggingface_hub import HfApi, HfFolder, CommitOperationAdd
        from huggingface_hub import create_repo
        api = HfApi()
        your_username = api.whoami()["name"]
        repo_id = f"sd-concepts-library/{slugify(name_of_your_concept)}"
        output_dir = textualinversion_prefs["output_dir"]
        if(not hf_token_write):
            with open(HfFolder.path_token, 'r') as fin: hf_token = fin.read();
        else:
            hf_token = hf_token_write
        if(textualinversion_prefs['where_to_save_concept'] == "Public Library"):
            #Join the Concepts Library organization if you aren't part of it already
            run_sp(f"curl -X POST -H 'Authorization: Bearer '{hf_token} -H 'Content-Type: application/json' https://huggingface.co/organizations/sd-concepts-library/share/VcLXJtzwwxnHYCkNMLpSJCdnNFZHQwWywv", realtime=False)
            # curl -X POST -H 'Authorization: Bearer '$hf_token -H 'Content-Type: application/json' https://huggingface.co/organizations/sd-concepts-library/share/VcLXJtzwwxnHYCkNMLpSJCdnNFZHQwWywv
        else:
            repo_id = f"{your_username}/{slugify(name_of_your_concept)}"
        images_upload = os.listdir("my_concept")
        image_string = ""
        repo_id = f"sd-concepts-library/{slugify(name_of_your_concept)}"
        for i, image in enumerate(images_upload):
            image_string = f'''{image_string}![{placeholder_token} {i}](https://huggingface.co/{repo_id}/resolve/main/concept_images/{image})
        '''
        if(textualinversion_prefs['what_to_teach'] == "style"):
            what_to_teach_article = f"a `{textualinversion_prefs['what_to_teach']}`"
        else:
            what_to_teach_article = f"an `{textualinversion_prefs['what_to_teach']}`"
        description = textualinversion_prefs['readme_description']
        if bool(description.strip()):
            description = textualinversion_prefs['readme_description'] + '\n\n'
        readme_text = f'''---
        license: mit
        ---
        ### {name_of_your_concept} by {your_username} using [Stable Diffusion Deluxe](https://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb)
        This is the `{placeholder_token}` concept taught to Stable Diffusion via Textual Inversion. You can load this concept into the [Stable Diffusion Deluxe](https://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb) notebook. You can also train your own concepts and load them into the concept libraries there too, or using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_textual_inversion_training.ipynb).
    
        {description}Here is the new concept you will be able to use as {what_to_teach_article}:
        {image_string}
        '''
        #Save the readme to a file
        readme_file = open("README.md", "w")
        readme_file.write(readme_text)
        readme_file.close()
        #Save the token identifier to a file
        text_file = open("token_identifier.txt", "w")
        text_file.write(placeholder_token)
        text_file.close()
        #Save the type of teached thing to a file
        type_file = open("type_of_concept.txt","w")
        type_file.write(textualinversion_prefs['what_to_teach'])
        type_file.close()
        operations = [
            CommitOperationAdd(path_in_repo="learned_embeds.bin", path_or_fileobj=f"{output_dir}/learned_embeds.bin"),
            CommitOperationAdd(path_in_repo="token_identifier.txt", path_or_fileobj="token_identifier.txt"),
            CommitOperationAdd(path_in_repo="type_of_concept.txt", path_or_fileobj="type_of_concept.txt"),
            CommitOperationAdd(path_in_repo="README.md", path_or_fileobj="README.md"),
        ]
        create_repo(repo_id,private=True, token=hf_token)
        api = HfApi()
        api.create_commit(
            repo_id=repo_id,
            operations=operations,
            commit_message=f"Upload the concept {name_of_your_concept} embeds and token",
            token=hf_token
        )
        api.upload_folder(
            folder_path=save_path,
            path_in_repo="concept_images",
            repo_id=repo_id,
            token=hf_token
        )
        prefs['custom_model'] = repo_id
        prt(Markdown(f"## Your concept was saved successfully to _{repo_id}_.<br>[Click here to access it](https://huggingface.co/{repo_id} and go to _Installers->Model Checkpoint->Custom Model Path_ to use. Include Token to your Prompt text."))
    if prefs['enable_sounds']: page.snd_alert.play()

class TextualInversionDataset(Dataset):
    import random as rnd
    def __init__(
        self,
        data_root,
        tokenizer,
        learnable_property="object",  # [object, style]
        size=textualinversion_prefs['max_size'],
        repeats=100,
        interpolation="bicubic",
        flip_p=0.5,
        set="train",
        placeholder_token="*",
        center_crop=False,
    ):
        self.data_root = data_root
        self.tokenizer = tokenizer
        self.learnable_property = learnable_property
        self.size = size
        self.placeholder_token = placeholder_token
        self.center_crop = center_crop
        self.flip_p = flip_p
        self.image_paths = [os.path.join(self.data_root, file_path) for file_path in os.listdir(self.data_root)]
        self.num_images = len(self.image_paths)
        self._length = self.num_images
        if set == "train":
            self._length = self.num_images * repeats
        self.interpolation = {
            "linear": PIL.Image.LINEAR,
            "bilinear": PIL.Image.BILINEAR,
            "bicubic": PIL.Image.BICUBIC,
            "lanczos": PIL.Image.LANCZOS,
        }[interpolation]
        self.templates = imagenet_style_templates_small if learnable_property == "style" else imagenet_templates_small
        self.flip_transform = transforms.RandomHorizontalFlip(p=self.flip_p)

    def __len__(self):
        return self._length

    def __getitem__(self, i):
        import random as rnd
        example = {}
        image = PILImage.open(self.image_paths[i % self.num_images])
        if not image.mode == "RGB":
            image = image.convert("RGB")
        placeholder_string = self.placeholder_token
        text = rnd.choice(self.templates).format(placeholder_string)
        example["input_ids"] = self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.tokenizer.model_max_length,
            return_tensors="pt",
        ).input_ids[0]
        # default to score-sde preprocessing
        img = np.array(image).astype(np.uint8)
        if self.center_crop:
            crop = min(img.shape[0], img.shape[1])
            h, w, = (
                img.shape[0],
                img.shape[1],
            )
            img = img[(h - crop) // 2 : (h + crop) // 2, (w - crop) // 2 : (w + crop) // 2]
        image = PILImage.fromarray(img)
        image = image.resize((self.size, self.size), resample=self.interpolation)
        image = self.flip_transform(image)
        image = np.array(image).astype(np.uint8)
        image = (image / 127.5 - 1.0).astype(np.float32)
        example["pixel_values"] = torch.from_numpy(image).permute(2, 0, 1)
        return example

def run_unCLIP(page, from_list=False):
    global unCLIP_prefs, pipe_unCLIP
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    def prt(line, update=True):
      if type(line) == str:
        line = Text(line)
      page.unCLIP_output.controls.append(line)
      if update:
        page.unCLIP_output.update()
    def clear_last():
      del page.unCLIP_output.controls[-1]
      page.unCLIP_output.update()
    def autoscroll(scroll=True):
      page.unCLIP_output.auto_scroll = scroll
      page.unCLIP_output.update()
    progress = ProgressBar(bar_height=8)
    total_steps = unCLIP_prefs['prior_num_inference_steps'] + unCLIP_prefs['decoder_num_inference_steps'] + unCLIP_prefs['super_res_num_inference_steps']
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress, total_steps
      #total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
    unCLIP_prompts = []
    if from_list:
      if len(prompts) < 1:
        alert_msg(page, "You need to add Prompts to your List first... ")
        return
      for p in prompts:
        unCLIP_prompts.append(p.prompt)
    else:
      if not bool(unCLIP_prefs['prompt']):
        alert_msg(page, "You need to add a Text Prompt first... ")
        return
      unCLIP_prompts.append(unCLIP_prefs['prompt'])
    page.unCLIP_output.controls.clear()
    from PIL import Image as PILImage
    from PIL.PngImagePlugin import PngInfo
    clear_pipes('unCLIP')
    torch.cuda.empty_cache()
    torch.cuda.reset_max_memory_allocated()
    torch.cuda.reset_peak_memory_stats()
    if pipe_unCLIP == None:
        from diffusers import UnCLIPPipeline
        prt(Row([ProgressRing(), Text("  Downloading unCLIP Kakaobrain Karlo Pipeline... It's a big one, see console for progress.", weight=FontWeight.BOLD)]))
        try:
            pipe_unCLIP = UnCLIPPipeline.from_pretrained("kakaobrain/karlo-v1-alpha", torch_dtype=torch.float16 if not prefs['higher_vram_mode'] else torch.float32, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None)
            pipe_unCLIP.to(torch_device)
        except Exception as e:
            clear_last()
            alert_msg(page, "Error Downloading unCLIP Pipeline", content=Text(str(e)))
            return
        pipe_unCLIP.set_progress_bar_config(disable=True)
        clear_last()
    s = "s" if unCLIP_prefs['num_images'] > 1 else ""
    prt(f"Generating unCLIP{s} of your Image...")
    batch_output = os.path.join(stable_dir, unCLIP_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    batch_output = os.path.join(prefs['image_output'], unCLIP_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    for pr in unCLIP_prompts:
        for num in range(unCLIP_prefs['num_images']):
            autoscroll(False)
            prt(progress)
            autoscroll(True)
            random_seed = (int(unCLIP_prefs['seed']) + num) if int(unCLIP_prefs['seed']) > 0 else rnd.randint(0,4294967295)
            generator = torch.Generator(device=torch_device).manual_seed(random_seed)
            try:
                images = pipe_unCLIP([pr], prior_num_inference_steps=unCLIP_prefs['prior_num_inference_steps'], decoder_num_inference_steps=unCLIP_prefs['decoder_num_inference_steps'], super_res_num_inference_steps=unCLIP_prefs['super_res_num_inference_steps'], prior_guidance_scale=unCLIP_prefs['prior_guidance_scale'], decoder_guidance_scale=unCLIP_prefs['decoder_guidance_scale'], num_images_per_prompt=1, generator=generator, callback=callback_fnc, callback_steps=1).images
            except Exception as e:
                clear_last()
                alert_msg(page, "Error running unCLIP Pipeline", content=Text(str(e)))
                return
            clear_last()
            fname = format_filename(pr)

            if prefs['file_suffix_seed']: fname += f"-{random_seed}"
            for image in images:
                image_path = available_file(os.path.join(stable_dir, unCLIP_prefs['batch_folder_name']), fname, num)
                unscaled_path = image_path
                output_file = image_path.rpartition(slash)[2]
                image.save(image_path)
                out_path = image_path.rpartition(slash)[0]
                if not unCLIP_prefs['display_upscaled_image'] or not unCLIP_prefs['apply_ESRGAN_upscale']:
                    prt(Row([Img(src=unscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if unCLIP_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
                    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
                    upload_folder = 'upload'
                    result_folder = 'results'     
                    if os.path.isdir(upload_folder):
                        shutil.rmtree(upload_folder)
                    if os.path.isdir(result_folder):
                        shutil.rmtree(result_folder)
                    os.mkdir(upload_folder)
                    os.mkdir(result_folder)
                    short_name = f'{fname[:80]}-{num}.png'
                    dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
                    #print(f'Moving {fpath} to {dst_path}')
                    #shutil.move(fpath, dst_path)
                    shutil.copy(image_path, dst_path)
                    #faceenhance = ' --face_enhance' if unCLIP_prefs["face_enhance"] else ''
                    faceenhance = ''
                    run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {unCLIP_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
                    out_file = short_name.rpartition('.')[0] + '_out.png'
                    upscaled_path = os.path.join(out_path, output_file)
                    shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
                    image_path = upscaled_path
                    os.chdir(stable_dir)
                    if unCLIP_prefs['display_upscaled_image']:
                        time.sleep(0.6)
                        prt(Row([Img(src=upscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if prefs['save_image_metadata']:
                    img = PILImage.open(image_path)
                    metadata = PngInfo()
                    metadata.add_text("artist", prefs['meta_ArtistName'])
                    metadata.add_text("copyright", prefs['meta_Copyright'])
                    metadata.add_text("software", "Stable Diffusion Deluxe" + f", upscaled {unCLIP_prefs['enlarge_scale']}x with ESRGAN" if unCLIP_prefs['apply_ESRGAN_upscale'] else "")
                    metadata.add_text("pipeline", "unCLIP")
                    if prefs['save_config_in_metadata']:
                      metadata.add_text("title", pr)
                      config_json = unCLIP_prefs.copy()
                      config_json['model_path'] = "kakaobrain/karlo-v1-alpha"
                      config_json['seed'] = random_seed
                      del config_json['num_images']
                      del config_json['display_upscaled_image']
                      del config_json['batch_folder_name']
                      if not config_json['apply_ESRGAN_upscale']:
                        del config_json['enlarge_scale']
                        del config_json['apply_ESRGAN_upscale']
                      metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
                    img.save(image_path, pnginfo=metadata)
                #TODO: PyDrive
                if storage_type == "Colab Google Drive":
                    new_file = available_file(os.path.join(prefs['image_output'], unCLIP_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                elif bool(prefs['image_output']):
                    new_file = available_file(os.path.join(prefs['image_output'], unCLIP_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                time.sleep(0.2)
                prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_unCLIP_image_variation(page, from_list=False):
    global unCLIP_image_variation_prefs, pipe_unCLIP_image_variation
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    def prt(line, update=True):
      if type(line) == str:
        line = Text(line)
      page.unCLIP_image_variation_output.controls.append(line)
      if update:
        page.unCLIP_image_variation_output.update()
    def clear_last():
      del page.unCLIP_image_variation_output.controls[-1]
      page.unCLIP_image_variation_output.update()
    def autoscroll(scroll=True):
      page.unCLIP_image_variation_output.auto_scroll = scroll
      page.unCLIP_image_variation_output.update()
    progress = ProgressBar(bar_height=8)
    total_steps = unCLIP_image_variation_prefs['decoder_num_inference_steps'] + unCLIP_image_variation_prefs['super_res_num_inference_steps']
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress, total_steps
      #total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
    unCLIP_image_variation_inits = []
    if from_list:
      if len(prompts) < 1:
        alert_msg(page, "You need to add Prompts to your List first... ")
        return
      for p in prompts:
        if bool(p['init_image']):
          unCLIP_image_variation_inits.append(p.prompt)
    else:
      if not bool(unCLIP_image_variation_prefs['init_image']):
        alert_msg(page, "You need to add a Initial Image first... ")
        return
      unCLIP_image_variation_inits.append(unCLIP_image_variation_prefs['prompt'])
    page.unCLIP_image_variation_output.controls.clear()
    from io import BytesIO
    from PIL import Image as PILImage
    from PIL.PngImagePlugin import PngInfo
    from PIL import ImageOps
    
    clear_pipes('unCLIP_image_variation')
    torch.cuda.empty_cache()
    torch.cuda.reset_max_memory_allocated()
    torch.cuda.reset_peak_memory_stats()
    if pipe_unCLIP_image_variation == None:
        from diffusers import UnCLIPImageVariationPipeline
        prt(Row([ProgressRing(), Text("  Downloading unCLIP Image Variation Kakaobrain Karlo Pipeline... It's a big one, see console for progress.", weight=FontWeight.BOLD)]))
        try:
            pipe_unCLIP_image_variation = UnCLIPImageVariationPipeline.from_pretrained("fusing/karlo-image-variations-diffusers", torch_dtype=torch.float16 if not prefs['higher_vram_mode'] else torch.float32, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None)
            pipe_unCLIP_image_variation.to(torch_device)
        except Exception as e:
            clear_last()
            alert_msg(page, "Error Downloading unCLIP Image Variation Pipeline", content=Text(str(e)))
            return
        pipe_unCLIP_image_variation.set_progress_bar_config(disable=True)
        clear_last()
    s = "s" if unCLIP_image_variation_prefs['num_images'] > 1 else ""
    prt(f"Generating unCLIP Image Variation{s} of your Image...")
    batch_output = os.path.join(stable_dir, unCLIP_image_variation_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    batch_output = os.path.join(prefs['image_output'], unCLIP_image_variation_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    for init in unCLIP_image_variation_inits:
        if init.startswith('http'):
          init_img = PILImage.open(requests.get(init, stream=True).raw)
        else:
          if os.path.isfile(init):
            init_img = PILImage.open(init)
          else:
            alert_msg(page, f"ERROR: Couldn't find your init_image {init}")
            return
        width, height = init_img.size
        width, height = scale_dimensions(width, height, unCLIP_image_variation_prefs['max_size'])
        init_img = init_img.resize((width, height), resample=PILImage.BICUBIC)
        init_img = ImageOps.exif_transpose(init_img).convert("RGB")
        for num in range(unCLIP_image_variation_prefs['num_images']):
            autoscroll(False)
            prt(progress)
            autoscroll(True)
            random_seed = (int(unCLIP_image_variation_prefs['seed']) + num) if int(unCLIP_image_variation_prefs['seed']) > 0 else rnd.randint(0,4294967295)
            generator = torch.Generator(device=torch_device).manual_seed(random_seed)
            try:
                images = pipe_unCLIP_image_variation(image=init, decoder_num_inference_steps=unCLIP_image_variation_prefs['decoder_num_inference_steps'], super_res_num_inference_steps=unCLIP_image_variation_prefs['super_res_num_inference_steps'], decoder_guidance_scale=unCLIP_image_variation_prefs['decoder_guidance_scale'], num_images_per_prompt=1, generator=generator, callback=callback_fnc, callback_steps=1).images
            except Exception as e:
                clear_last()
                alert_msg(page, "Error running unCLIP Image Variation Pipeline", content=Text(str(e)))
                return
            clear_last()
            #fname = format_filename(unCLIP_image_variation_prefs['file_name'])
            fname = init.rpartition(slash)[2].rpartition('.')[0]
            if prefs['file_suffix_seed']: fname += f"-{random_seed}"
            for image in images:
                image_path = available_file(os.path.join(stable_dir, unCLIP_image_variation_prefs['batch_folder_name']), fname, num)
                unscaled_path = image_path
                output_file = image_path.rpartition(slash)[2]
                image.save(image_path)
                out_path = image_path.rpartition(slash)[0]
                if not unCLIP_image_variation_prefs['display_upscaled_image'] or not unCLIP_image_variation_prefs['apply_ESRGAN_upscale']:
                    prt(Row([Img(src=unscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if unCLIP_image_variation_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
                    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
                    upload_folder = 'upload'
                    result_folder = 'results'     
                    if os.path.isdir(upload_folder):
                        shutil.rmtree(upload_folder)
                    if os.path.isdir(result_folder):
                        shutil.rmtree(result_folder)
                    os.mkdir(upload_folder)
                    os.mkdir(result_folder)
                    short_name = f'{fname[:80]}-{num}.png'
                    dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
                    #print(f'Moving {fpath} to {dst_path}')
                    #shutil.move(fpath, dst_path)
                    shutil.copy(image_path, dst_path)
                    #faceenhance = ' --face_enhance' if unCLIP_image_variation_prefs["face_enhance"] else ''
                    faceenhance = ''
                    run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {unCLIP_image_variation_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
                    out_file = short_name.rpartition('.')[0] + '_out.png'
                    upscaled_path = os.path.join(out_path, output_file)
                    shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
                    image_path = upscaled_path
                    os.chdir(stable_dir)
                    if unCLIP_image_variation_prefs['display_upscaled_image']:
                        time.sleep(0.6)
                        prt(Row([Img(src=upscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if prefs['save_image_metadata']:
                    img = PILImage.open(image_path)
                    metadata = PngInfo()
                    metadata.add_text("artist", prefs['meta_ArtistName'])
                    metadata.add_text("copyright", prefs['meta_Copyright'])
                    metadata.add_text("software", "Stable Diffusion Deluxe" + f", upscaled {unCLIP_image_variation_prefs['enlarge_scale']}x with ESRGAN" if unCLIP_image_variation_prefs['apply_ESRGAN_upscale'] else "")
                    metadata.add_text("pipeline", "unCLIP_image_variation")
                    if prefs['save_config_in_metadata']:
                      #metadata.add_text("title", unCLIP_image_variation_prefs['file_name'])
                      config_json = unCLIP_image_variation_prefs.copy()
                      config_json['model_path'] = "fusing/karlo-image-variations-diffusers"
                      config_json['seed'] = random_seed
                      del config_json['num_images']
                      del config_json['display_upscaled_image']
                      del config_json['batch_folder_name']
                      del config_json['file_name']
                      if not config_json['apply_ESRGAN_upscale']:
                        del config_json['enlarge_scale']
                        del config_json['apply_ESRGAN_upscale']
                      metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
                    img.save(image_path, pnginfo=metadata)
                #TODO: PyDrive
                if storage_type == "Colab Google Drive":
                    new_file = available_file(os.path.join(prefs['image_output'], unCLIP_image_variation_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                elif bool(prefs['image_output']):
                    new_file = available_file(os.path.join(prefs['image_output'], unCLIP_image_variation_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                time.sleep(0.2)
                prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_magic_mix(page, from_list=False):
    global magic_mix_prefs, pipe_magic_mix
    if not status['installed_diffusers']:
      alert_msg(page, "You must Install the HuggingFace Diffusers Library first... ")
      return
    def prt(line, update=True):
      if type(line) == str:
        line = Text(line)
      page.magic_mix_output.controls.append(line)
      if update:
        page.magic_mix_output.update()
    def clear_last():
      del page.magic_mix_output.controls[-1]
      page.magic_mix_output.update()
    def autoscroll(scroll=True):
      page.magic_mix_output.auto_scroll = scroll
      page.magic_mix_output.update()
    progress = ProgressBar(bar_height=8)
    total_steps = magic_mix_prefs['num_inference_steps']
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress, total_steps
      total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
    magic_mix_prompts = []
    if from_list:
      if len(prompts) < 1:
        alert_msg(page, "You need to add Prompts to your List first... ")
        return
      for p in prompts:
        magic_mix_prompts.append(p.prompt)
    else:
      if not bool(magic_mix_prefs['prompt']):
        alert_msg(page, "You need to add a Text Prompt first... ")
        return
      magic_mix_prompts.append(magic_mix_prefs['prompt'])
    page.magic_mix_output.controls.clear()
    from io import BytesIO
    from PIL import Image as PILImage
    from PIL.PngImagePlugin import PngInfo
    from PIL import ImageOps
    if magic_mix_prefs['init_image'].startswith('http'):
      init_img = PILImage.open(requests.get(magic_mix_prefs['init_image'], stream=True).raw)
    else:
      if os.path.isfile(magic_mix_prefs['init_image']):
        init_img = PILImage.open(magic_mix_prefs['init_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your init_image {magic_mix_prefs['init_image']}")
        return
    width, height = init_img.size
    width, height = scale_dimensions(width, height, magic_mix_prefs['max_size'])
    init_img = init_img.resize((width, height), resample=PILImage.BICUBIC)
    init_img = ImageOps.exif_transpose(init_img).convert("RGB")
    '''tform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize(
            (width, height),
            interpolation=transforms.InterpolationMode.BICUBIC,
            antialias=False,
            ),
        transforms.Normalize(
          [0.48145466, 0.4578275, 0.40821073],
          [0.26862954, 0.26130258, 0.27577711]),
    ])
    init_img = tform(init_img).to(torch_device)'''
    clear_pipes('magic_mix')
    #torch.cuda.empty_cache()
    #torch.cuda.reset_max_memory_allocated()
    #torch.cuda.reset_peak_memory_stats()
    model = get_model(prefs['model_ckpt'])
    scheduler_mode = magic_mix_prefs['scheduler_mode']
    if scheduler_mode == "K-LMS":
      from diffusers import LMSDiscreteScheduler
      schedule = LMSDiscreteScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "PNDM":
      from diffusers import PNDMScheduler
      schedule = PNDMScheduler.from_pretrained(model, subfolder="scheduler")
    elif scheduler_mode == "DDIM":
      from diffusers import DDIMScheduler
      schedule = DDIMScheduler.from_pretrained(model, subfolder="scheduler")
    if pipe_magic_mix == None or magic_mix_prefs['scheduler_mode'] != magic_mix_prefs['scheduler_last']:
        from diffusers import DiffusionPipeline
        prt(Row([ProgressRing(), Text("  Downloading MagicMix Pipeline... ", weight=FontWeight.BOLD)]))
        try:
            pipe_magic_mix = DiffusionPipeline.from_pretrained(model, custom_pipeline="AlanB/magic_mix_mod", scheduler=schedule, safety_checker=None, cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None)
            pipe_magic_mix.to(torch_device)
            pipe_magic_mix = optimize_pipe(pipe_magic_mix, vae=False)
            magic_mix_prefs['scheduler_last'] = magic_mix_prefs['scheduler_mode']
        except Exception as e:
            clear_last()
            alert_msg(page, "Error Downloading MagicMix Pipeline", content=Text(str(e)))
            return
        #pipe_magic_mix.set_progress_bar_config(disable=True)
        clear_last()
    s = "es" if magic_mix_prefs['num_images'] > 1 else ""
    prt(f"Generating MagicMix{s} of your Image...")
    batch_output = os.path.join(stable_dir, magic_mix_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    batch_output = os.path.join(prefs['image_output'], magic_mix_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    for pr in magic_mix_prompts:
        for num in range(magic_mix_prefs['num_images']):
            autoscroll(False)
            prt(progress)
            autoscroll(True)
            random_seed = (int(magic_mix_prefs['seed']) + num) if int(magic_mix_prefs['seed']) > 0 else rnd.randint(0,4294967295)
            #generator = torch.Generator(device=torch_device).manual_seed(random_seed)
            try:
                images = pipe_magic_mix(image=init_img, prompt=pr, steps=magic_mix_prefs['num_inference_steps'], kmin=magic_mix_prefs['kmin'], kmax=magic_mix_prefs['kmax'], mix_factor=magic_mix_prefs['mix_factor'], guidance_scale=magic_mix_prefs['guidance_scale'], seed=random_seed).images #, callback=callback_fnc, callback_steps=1
            except Exception as e:
                clear_last()
                alert_msg(page, "Error running MagicMix Pipeline", content=Text(str(e)))
                return
            clear_last()
            fname = format_filename(pr)

            if prefs['file_suffix_seed']: fname += f"-{random_seed}"
            for image in images:
                image_path = available_file(os.path.join(stable_dir, magic_mix_prefs['batch_folder_name']), fname, num)
                unscaled_path = image_path
                output_file = image_path.rpartition(slash)[2]
                image.save(image_path)
                out_path = image_path.rpartition(slash)[0]
                if not magic_mix_prefs['display_upscaled_image'] or not magic_mix_prefs['apply_ESRGAN_upscale']:
                    prt(Row([Img(src=unscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if magic_mix_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
                    os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
                    upload_folder = 'upload'
                    result_folder = 'results'     
                    if os.path.isdir(upload_folder):
                        shutil.rmtree(upload_folder)
                    if os.path.isdir(result_folder):
                        shutil.rmtree(result_folder)
                    os.mkdir(upload_folder)
                    os.mkdir(result_folder)
                    short_name = f'{fname[:80]}-{num}.png'
                    dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
                    #print(f'Moving {fpath} to {dst_path}')
                    #shutil.move(fpath, dst_path)
                    shutil.copy(image_path, dst_path)
                    #faceenhance = ' --face_enhance' if magic_mix_prefs["face_enhance"] else ''
                    faceenhance = ''
                    run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {magic_mix_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
                    out_file = short_name.rpartition('.')[0] + '_out.png'
                    upscaled_path = os.path.join(out_path, output_file)
                    shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
                    image_path = upscaled_path
                    os.chdir(stable_dir)
                    if magic_mix_prefs['display_upscaled_image']:
                        time.sleep(0.6)
                        prt(Row([Img(src=upscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
                if prefs['save_image_metadata']:
                    img = PILImage.open(image_path)
                    metadata = PngInfo()
                    metadata.add_text("artist", prefs['meta_ArtistName'])
                    metadata.add_text("copyright", prefs['meta_Copyright'])
                    metadata.add_text("software", "Stable Diffusion Deluxe" + f", upscaled {magic_mix_prefs['enlarge_scale']}x with ESRGAN" if magic_mix_prefs['apply_ESRGAN_upscale'] else "")
                    metadata.add_text("pipeline", "magic_mix")
                    if prefs['save_config_in_metadata']:
                      metadata.add_text("title", pr)
                      config_json = magic_mix_prefs.copy()
                      config_json['model_path'] = model
                      config_json['seed'] = random_seed
                      del config_json['num_images']
                      del config_json['display_upscaled_image']
                      del config_json['batch_folder_name']
                      del config_json['file_name']
                      del config_json["scheduler_last"]
                      del config_json['max_size']
                      if not config_json['apply_ESRGAN_upscale']:
                        del config_json['enlarge_scale']
                        del config_json['apply_ESRGAN_upscale']
                      metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
                    img.save(image_path, pnginfo=metadata)
                #TODO: PyDrive
                if storage_type == "Colab Google Drive":
                    new_file = available_file(os.path.join(prefs['image_output'], magic_mix_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                elif bool(prefs['image_output']):
                    new_file = available_file(os.path.join(prefs['image_output'], magic_mix_prefs['batch_folder_name']), fname, num)
                    out_path = new_file
                    shutil.copy(image_path, new_file)
                time.sleep(0.2)
                prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_paint_by_example(page):
    global paint_by_example_prefs, prefs, status, pipe_paint_by_example
    if not status['installed_diffusers']:
      alert_msg(page, "You need to Install HuggingFace Diffusers before using...")
      return
    if not bool(paint_by_example_prefs['original_image']) or (not bool(paint_by_example_prefs['alpha_image']) and not bool(paint_by_example_prefs['mask_image'])):
      alert_msg(page, "You must provide the Original Image and the Mask Image to process...")
      return
    if not bool(paint_by_example_prefs['example_image']):
      alert_msg(page, "You must provide an Example Image to Transfer Subject from...")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.paint_by_example_output.controls.append(line)
      page.paint_by_example_output.update()
    def clear_last():
      del page.paint_by_example_output.controls[-1]
      page.paint_by_example_output.update()
    progress = ProgressBar(bar_height=8)
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress
      total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
      #print(f'{type(latents)} {len(latents)}- {str(latents)}')
    prt(Row([ProgressRing(), Text("Installing Paint-by-Example Pipeline...", weight=FontWeight.BOLD)]))
    import requests, random
    from io import BytesIO
    from PIL import Image as PILImage
    from PIL import ImageOps
    from PIL.PngImagePlugin import PngInfo
    if paint_by_example_prefs['original_image'].startswith('http'):
      #response = requests.get(paint_by_example_prefs['original_image'])
      #original_img = PILImage.open(BytesIO(response.content)).convert("RGB")
      original_img = PILImage.open(requests.get(paint_by_example_prefs['original_image'], stream=True).raw)
    else:
      if os.path.isfile(paint_by_example_prefs['original_image']):
        original_img = PILImage.open(paint_by_example_prefs['original_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your original_image {paint_by_example_prefs['original_image']}")
        return
    width, height = original_img.size
    width, height = scale_dimensions(width, height, paint_by_example_prefs['max_size'])
    if bool(paint_by_example_prefs['alpha_mask']):
      original_img = ImageOps.exif_transpose(original_img).convert("RGBA")
    else:
      original_img = ImageOps.exif_transpose(original_img).convert("RGB")
    original_img = original_img.resize((width, height), resample=PILImage.LANCZOS)
    mask_img = None
    if not bool(paint_by_example_prefs['mask_image']) and bool(paint_by_example_prefs['alpha_mask']):
      red, green, blue, alpha = PILImage.Image.split(original_img)
      mask_img = alpha.convert('L')
    else:
      if paint_by_example_prefs['mask_image'].startswith('http'):
        mask_img = PILImage.open(requests.get(paint_by_example_prefs['mask_image'], stream=True).raw)
      else:
        if os.path.isfile(paint_by_example_prefs['mask_image']):
          mask_img = PILImage.open(paint_by_example_prefs['mask_image'])
        else:
          alert_msg(page, f"ERROR: Couldn't find your mask_image {paint_by_example_prefs['mask_image']}")
          return
      if paint_by_example_prefs['invert_mask']:
        mask_img = ImageOps.invert(mask_img.convert('RGB'))
    #mask_img = mask_img.convert("L")
    #mask_img = mask_img.convert("1")
    mask_img = mask_img.resize((width, height), resample=PILImage.NEAREST)
    mask_img = ImageOps.exif_transpose(mask_img).convert("RGB")
    #print(f'Resize to {width}x{height}')
    if paint_by_example_prefs['example_image'].startswith('http'):
      example_img = PILImage.open(requests.get(paint_by_example_prefs['example_image'], stream=True).raw)
    else:
      if os.path.isfile(paint_by_example_prefs['example_image']):
        example_img = PILImage.open(paint_by_example_prefs['example_image'])
      else:
        alert_msg(page, f"ERROR: Couldn't find your Example Image {paint_by_example_prefs['example_image']}")
        return
    
    clear_pipes('paint_by_example')
    model_id = "Fantasy-Studio/Paint-by-Example"
    if pipe_paint_by_example is None:
      from diffusers import PaintByExamplePipeline
      pipe_paint_by_example = PaintByExamplePipeline.from_pretrained(model_id, scheduler=model_scheduler(model_id, big3=True), cache_dir=prefs['cache_dir'] if bool(prefs['cache_dir']) else None)
    clear_last()
    prt("Generating Paint-by-Example of your Image...")
    prt(progress)
    batch_output = os.path.join(stable_dir, paint_by_example_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    batch_output = os.path.join(prefs['image_output'], paint_by_example_prefs['batch_folder_name'])
    if not os.path.isdir(batch_output):
      os.makedirs(batch_output)
    random_seed = int(paint_by_example_prefs['seed']) if int(paint_by_example_prefs['seed']) > 0 else random.randint(0,4294967295)
    generator = torch.Generator(device=torch_device).manual_seed(random_seed)
    try:
      images = pipe_paint_by_example(image=original_img, mask_image=mask_img, example_image=example_img, num_inference_steps=paint_by_example_prefs['num_inference_steps'], eta=paint_by_example_prefs['eta'], guidance_scale=paint_by_example_prefs['guidance_scale'], num_images_per_prompt=paint_by_example_prefs['num_images'], generator=generator, callback=callback_fnc, callback_steps=1).images
    except Exception as e:
      clear_last()
      alert_msg(page, f"ERROR: Couldn't Paint-by-Example your image for some reason.  Possibly out of memory or something wrong with my code...", content=Text(str(e)))
      return
    filename = paint_by_example_prefs['original_image'].rpartition(slash)[2].rpartition('.')[0]
    #if prefs['file_suffix_seed']: fname += f"-{random_seed}"
    num = 0
    for image in images:
        random_seed += num
        fname = filename + (f"-{random_seed}" if prefs['file_suffix_seed'] else "")
        image_path = available_file(os.path.join(stable_dir, paint_by_example_prefs['batch_folder_name']), fname, num)
        unscaled_path = image_path
        output_file = image_path.rpartition(slash)[2]
        image.save(image_path)
        out_path = image_path.rpartition(slash)[0]
        if not paint_by_example_prefs['display_upscaled_image'] or not paint_by_example_prefs['apply_ESRGAN_upscale']:
            prt(Row([Img(src=unscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        if paint_by_example_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
            os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
            upload_folder = 'upload'
            result_folder = 'results'     
            if os.path.isdir(upload_folder):
                shutil.rmtree(upload_folder)
            if os.path.isdir(result_folder):
                shutil.rmtree(result_folder)
            os.mkdir(upload_folder)
            os.mkdir(result_folder)
            short_name = f'{fname[:80]}-{num}.png'
            dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
            #print(f'Moving {fpath} to {dst_path}')
            #shutil.move(fpath, dst_path)
            shutil.copy(image_path, dst_path)
            #faceenhance = ' --face_enhance' if paint_by_example_prefs["face_enhance"] else ''
            faceenhance = ''
            run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {paint_by_example_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
            out_file = short_name.rpartition('.')[0] + '_out.png'
            upscaled_path = os.path.join(out_path, output_file)
            shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
            image_path = upscaled_path
            os.chdir(stable_dir)
            if paint_by_example_prefs['display_upscaled_image']:
                time.sleep(0.6)
                prt(Row([Img(src=upscaled_path, fit=ImageFit.FIT_WIDTH, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        if prefs['save_image_metadata']:
            img = PILImage.open(image_path)
            metadata = PngInfo()
            metadata.add_text("artist", prefs['meta_ArtistName'])
            metadata.add_text("copyright", prefs['meta_Copyright'])
            metadata.add_text("software", "Stable Diffusion Deluxe" + f", upscaled {paint_by_example_prefs['enlarge_scale']}x with ESRGAN" if paint_by_example_prefs['apply_ESRGAN_upscale'] else "")
            metadata.add_text("pipeline", "Paint-by-Example")
            if prefs['save_config_in_metadata']:
              config_json = paint_by_example_prefs.copy()
              config_json['model_path'] = model_id
              config_json['seed'] = random_seed
              del config_json['num_images']
              del config_json['max_size']
              del config_json['display_upscaled_image']
              del config_json['batch_folder_name']
              del config_json['invert_mask']
              del config_json['alpha_mask']
              if not config_json['apply_ESRGAN_upscale']:
                del config_json['enlarge_scale']
                del config_json['apply_ESRGAN_upscale']
              metadata.add_text("config_json", json.dumps(config_json, ensure_ascii=True, indent=4))
            img.save(image_path, pnginfo=metadata)
        #TODO: PyDrive
        if storage_type == "Colab Google Drive":
            new_file = available_file(os.path.join(prefs['image_output'], paint_by_example_prefs['batch_folder_name']), fname, num)
            out_path = new_file
            shutil.copy(image_path, new_file)
        elif bool(prefs['image_output']):
            new_file = available_file(os.path.join(prefs['image_output'], paint_by_example_prefs['batch_folder_name']), fname, num)
            out_path = new_file
            shutil.copy(image_path, new_file)
        time.sleep(0.2)
        prt(Row([Text(out_path)], alignment=MainAxisAlignment.CENTER))
        num += 1
    if prefs['enable_sounds']: page.snd_alert.play()

def run_materialdiffusion(page):
    global materialdiffusion_prefs, prefs
    if not bool(materialdiffusion_prefs['material_prompt']):
      alert_msg(page, "You must provide a text prompt to process your material...")
      return
    if not bool(prefs['Replicate_api_key']):
      alert_msg(page, "You must provide your Replicate API Token in Settings to process your material...")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.materialdiffusion_output.controls.append(line)
      page.materialdiffusion_output.update()
    def clear_last():
      del page.materialdiffusion_output.controls[-1]
      page.materialdiffusion_output.update()
    progress = ProgressBar(bar_height=8)
    def callback_fnc(step: int, timestep: int, latents: torch.FloatTensor) -> None:
      callback_fnc.has_been_called = True
      nonlocal progress
      total_steps = len(latents)
      percent = (step +1)/ total_steps
      progress.value = percent
      progress.tooltip = f"{step +1} / {total_steps} timestep: {timestep}"
      progress.update()
      #print(f'{type(latents)} {len(latents)}- {str(latents)}')
    try:
      run_sp("pip install git+https://github.com/TomMoore515/material_stable_diffusion.git@main#egg=predict", realtime=True)
    except Exception as e:
        print(f"Error: {e}")
        #alert_msg(page, f"Error installing Material Diffusion from TomMoore515...", content=Text(str(e)))
        pass
    prt(Row([ProgressRing(), Text("Installing Replicate Material Diffusion Pipeline...", weight=FontWeight.BOLD)]))
    try:
        import replicate
    except ImportError as e:
        run_process("pip install replicate -qq", realtime=True)
        import replicate
        pass
    os.environ["REPLICATE_API_TOKEN"] = prefs['Replicate_api_key']
    #export REPLICATE_API_TOKEN=
    try:
        model = replicate.models.get("tommoore515/material_stable_diffusion")
        version = model.versions.get("3b5c0242f8925a4ab6c79b4c51e9b4ce6374e9b07b5e8461d89e692fd0faa449")
    except Exception as e:
        alert_msg(page, f"Seems like your Replicate API Token is Invalid. Check it again...", content=Text(str(e)))
        return
    import requests
    from io import BytesIO
    from PIL import ImageOps
    init_img = None
    if bool(materialdiffusion_prefs['init_image']):
        if materialdiffusion_prefs['init_image'].startswith('http'):
            init_img = PILImage.open(requests.get(materialdiffusion_prefs['init_image'], stream=True).raw)
        else:
            if os.path.isfile(materialdiffusion_prefs['init_image']):
                init_img = PILImage.open(materialdiffusion_prefs['init_image'])
            else:
                alert_msg(page, f"ERROR: Couldn't find your init_image {materialdiffusion_prefs['init_image']}")
                return
        #width, height = init_img.size
        #width, height = scale_dimensions(materialdiffusion_prefs['width'], materialdiffusion_prefs['height'])
        init_img = init_img.resize((materialdiffusion_prefs['width'], materialdiffusion_prefs['height']), resample=PILImage.LANCZOS)
        init_img = ImageOps.exif_transpose(init_img).convert("RGB")
    mask_img = None
    if bool(materialdiffusion_prefs['mask_image']):
        if materialdiffusion_prefs['mask_image'].startswith('http'):
            mask_img = PILImage.open(requests.get(materialdiffusion_prefs['mask_image'], stream=True).raw)
        else:
            if os.path.isfile(materialdiffusion_prefs['mask_image']):
                mask_img = PILImage.open(materialdiffusion_prefs['mask_image'])
            else:
                alert_msg(page, f"ERROR: Couldn't find your mask_image {materialdiffusion_prefs['mask_image']}")
                return
            if materialdiffusion_prefs['invert_mask']:
                mask_img = ImageOps.invert(mask_img.convert('RGB'))
                mask_img = mask_img.resize((materialdiffusion_prefs['width'], materialdiffusion_prefs['height']), resample=PILImage.NEAREST)
                mask_img = ImageOps.exif_transpose(mask_img).convert("RGB")
    #print(f'Resize to {width}x{height}')
    clear_pipes()
    clear_last()
    prt("Generating your Material Diffusion Image...")
    prt(progress)
    random_seed = int(materialdiffusion_prefs['seed']) if int(materialdiffusion_prefs['seed']) > 0 else rnd.randint(0,4294967295)
    try:
        images = version.predict(prompt=materialdiffusion_prefs['material_prompt'], width=materialdiffusion_prefs['width'], height=materialdiffusion_prefs['height'], init_image=init_img, mask=mask_img, prompt_strength=materialdiffusion_prefs['prompt_strength'], num_outputs=materialdiffusion_prefs['num_outputs'], num_inference_steps=materialdiffusion_prefs['steps'], guidance_scale=materialdiffusion_prefs['guidance_scale'], seed=random_seed)
    except Exception as e:
        clear_last()
        clear_last()
        alert_msg(page, f"ERROR: Couldn't create your image for some reason.  Possibly out of memory or something wrong with my code...", content=Text(str(e)))
        return
    clear_last()
    clear_last()
    txt2img_output = stable_dir
    batch_output = prefs['image_output']
    print(str(images))
    if images is None:
        prt(f"ERROR: Problem generating images, check your settings and run above blocks again, or report the error to Skquark if it really seems broken.")
        return
    idx = 0
    for image in images:
        random_seed += idx
        fname = format_filename(materialdiffusion_prefs['material_prompt'])
        seed_suffix = f"-{random_seed}" if bool(prefs['file_suffix_seed']) else ''
        fname = f'{materialdiffusion_prefs["file_prefix"]}{fname}{seed_suffix}'
        txt2img_output = stable_dir
        if bool(materialdiffusion_prefs['batch_folder_name']):
            txt2img_output = os.path.join(stable_dir, materialdiffusion_prefs['batch_folder_name'])
        if not os.path.exists(txt2img_output):
            os.makedirs(txt2img_output)
        image_path = available_file(txt2img_output, fname, 1)
        #image.save(image_path)
        response = requests.get(image, stream=True)
        with open(image_path, "wb") as f:
          f.write(response.content)
        new_file = image_path.rpartition(slash)[2]
        if not materialdiffusion_prefs['display_upscaled_image'] or not materialdiffusion_prefs['apply_ESRGAN_upscale']:
            prt(Row([Img(src=image_path, width=materialdiffusion_prefs['width'], height=materialdiffusion_prefs['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))

        if save_to_GDrive:
            batch_output = os.path.join(prefs['image_output'], materialdiffusion_prefs['batch_folder_name'])
            if not os.path.exists(batch_output):
                os.makedirs(batch_output)
        elif storage_type == "PyDrive Google Drive":
            newFolder = gdrive.CreateFile({'title': materialdiffusion_prefs['batch_folder_name'], "parents": [{"kind": "drive#fileLink", "id": prefs['image_output']}],"mimeType": "application/vnd.google-apps.folder"})
            newFolder.Upload()
            batch_output = newFolder
        out_path = batch_output if save_to_GDrive else txt2img_output
        
        if materialdiffusion_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
            os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
            upload_folder = 'upload'
            result_folder = 'results'     
            if os.path.isdir(upload_folder):
                shutil.rmtree(upload_folder)
            if os.path.isdir(result_folder):
                shutil.rmtree(result_folder)
            os.mkdir(upload_folder)
            os.mkdir(result_folder)
            short_name = f'{fname[:80]}-{idx}.png'
            dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
            #print(f'Moving {fpath} to {dst_path}')
            #shutil.move(fpath, dst_path)
            shutil.copy(image_path, dst_path)
            #faceenhance = ' --face_enhance' if materialdiffusion_prefs["face_enhance"] else ''
            faceenhance = ''
            #python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {enlarge_scale}{faceenhance}
            run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {materialdiffusion_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
            out_file = short_name.rpartition('.')[0] + '_out.png'
            #print(f'move {root_dir}Real-ESRGAN/{result_folder}/{out_file} to {fpath}')
            #shutil.move(f'{root_dir}Real-ESRGAN/{result_folder}/{out_file}', fpath)
            upscaled_path = os.path.join(out_path, new_file)
            shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
            # !python inference_realesrgan.py --model_path experiments/pretrained_models/RealESRGAN_x4plus.pth --input upload --netscale 4 --outscale 3.5 --half --face_enhance
            os.chdir(stable_dir)
            if materialdiffusion_prefs['display_upscaled_image']:
                time.sleep(0.6)
                prt(Row([Img(src=upscaled_path, width=materialdiffusion_prefs['width'] * float(materialdiffusion_prefs["enlarge_scale"]), height=materialdiffusion_prefs['height'] * float(materialdiffusion_prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        else:
            shutil.copy(image_path, os.path.join(out_path, new_file))
        # TODO: Add Metadata
        prt(Row([Text(new_file)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()


def run_dall_e(page, from_list=False):
    global dall_e_prefs, prefs, prompts
    if (not bool(dall_e_prefs['prompt']) and not from_list) or (from_list and (len(prompts) == 0)):
      alert_msg(page, "You must provide a text prompt to process your image generation...")
      return
    if not bool(prefs['OpenAI_api_key']):
      alert_msg(page, "You must provide your OpenAI API Key in Settings to process your Dall-e 2 Creation...")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.dall_e_output.controls.append(line)
      page.dall_e_output.update()
    def clear_last():
      del page.dall_e_output.controls[-1]
      page.dall_e_output.update()
    progress = ProgressBar(bar_height=8)
    try:
        import openai
    except:
        prt(Row([ProgressRing(), Text("Installing OpenAi Dall-E 2 API...", weight=FontWeight.BOLD)]))
        run_process("pip install -q openai", realtime=False)
        clear_last()
        import openai
        pass
    try:
        openai.api_key = prefs['OpenAI_api_key']
    except Exception as e:
        alert_msg(page, f"Seems like your OpenAI API Key is Invalid. Check it again...", content=Text(str(e)))
        return
    import requests
    from io import BytesIO
    from PIL import ImageOps
    
    save_dir = os.path.join(root_dir, 'dalle_inputs')
    init_img = None
    dall_e_list = []
    if from_list:
        if len(prompts) > 0:
            for p in prompts:
                dall_e_list.append({'prompt': p.prompt, 'init_image': p.arg['init_image'], 'mask_image': p.arg['mask_image']})
        else:
            alert_msg(page, f"Your Prompts List is empty. Add to your batch list to use feature.")
            return
    else:
        dall_e_list.append({'prompt': dall_e_prefs['prompt'], 'init_image': dall_e_prefs['init_image'], 'mask_image': dall_e_prefs['mask_image']})
    
    for p in dall_e_list:
        init_image = p['init_image']
        mask_image = p['mask_image']
        if bool(init_image):
            fname = init_image.rpartition(slash)[2]
            init_file = os.path.join(save_dir, fname)
            if init_image.startswith('http'):
                init_img = PILImage.open(requests.get(init_image, stream=True).raw)
            else:
                if os.path.isfile(init_image):
                    init_img = PILImage.open(init_image)
                else:
                    alert_msg(page, f"ERROR: Couldn't find your init_image {init_image}")
                    return
            init_img = init_img.resize((dall_e_prefs['size'], dall_e_prefs['size']), resample=PILImage.LANCZOS)
            init_img = ImageOps.exif_transpose(init_img).convert("RGB")
            init_img.save(init_file)
        mask_img = None
        if bool(mask_image):
            fname = init_image.rpartition(slash)[2]
            mask_file = os.path.join(save_dir, fname)
            if mask_image.startswith('http'):
                mask_img = PILImage.open(requests.get(mask_image, stream=True).raw)
            else:
                if os.path.isfile(mask_image):
                    mask_img = PILImage.open(mask_image)
                else:
                    alert_msg(page, f"ERROR: Couldn't find your mask_image {mask_image}")
                    return
                if dall_e_prefs['invert_mask']:
                    mask_img = ImageOps.invert(mask_img.convert('RGB'))
            mask_img = mask_img.resize((dall_e_prefs['size'], dall_e_prefs['size']), resample=PILImage.NEAREST)
            mask_img = ImageOps.exif_transpose(init_img).convert("RGB")
            mask_img.save(mask_file)
        #print(f'Resize to {width}x{height}')
        #clear_pipes()
        prt("Generating your Dall-E 2 Image...")
        prt(progress)

        try:
            if bool(init_image) and bool(dall_e_prefs['variation']):
                response = openai.Image.create_variation(image=open(init_file, 'rb'), size=dall_e_prefs['size'], n=dall_e_prefs['num_images'])
            elif bool(init_image) and not bool(mask_image):
                response = openai.Image.create_edit(prompt=p['prompt'], size=dall_e_prefs['size'], n=dall_e_prefs['num_images'], image=open(init_file, 'rb'))
            elif bool(init_image) and bool(mask_image):
                response = openai.Image.create_edit(prompt=p['prompt'], size=dall_e_prefs['size'], n=dall_e_prefs['num_images'], image=open(init_file, 'rb'), mask=open(mask_file, 'rb'))
            else:
                response = openai.Image.create(prompt=p['prompt'], size=dall_e_prefs['size'], n=dall_e_prefs['num_images'])
        except Exception as e:
            clear_last()
            clear_last()
            alert_msg(page, f"ERROR: Something went wrong generating image form API...", content=Text(str(e)))
            return
        clear_last()
        clear_last()
        txt2img_output = stable_dir
        batch_output = prefs['image_output']
        #print(str(images))
        if response is None:
            prt(f"ERROR: Problem generating images, check your settings and run above blocks again, or report the error to Skquark if it really seems broken.")
            return
        #print(str(response))
        idx = 0
        for i in response['data']:
            image = i['url']
            #random_seed += idx
            fname = format_filename(p['prompt'])
            #seed_suffix = f"-{random_seed}" if bool(prefs['file_suffix_seed']) else ''
            fname = f'{dall_e_prefs["file_prefix"]}{fname}'
            txt2img_output = stable_dir
            if bool(dall_e_prefs['batch_folder_name']):
                txt2img_output = os.path.join(stable_dir, dall_e_prefs['batch_folder_name'])
            if not os.path.exists(txt2img_output):
                os.makedirs(txt2img_output)
            image_path = available_file(txt2img_output, fname, 1)
            #image.save(image_path)
            response = requests.get(image, stream=True)
            with open(image_path, "wb") as f:
                f.write(response.content)
            #img = i['url']
            new_file = image_path.rpartition(slash)[2].rpartition('-')[0]
            size = int(dall_e_prefs['size'].rpartition('x')[0])
            if not dall_e_prefs['display_upscaled_image'] or not dall_e_prefs['apply_ESRGAN_upscale']:
                prt(Row([Img(src=image_path, width=size, height=size, fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))

            if save_to_GDrive:
                batch_output = os.path.join(prefs['image_output'], dall_e_prefs['batch_folder_name'])
                if not os.path.exists(batch_output):
                    os.makedirs(batch_output)
            elif storage_type == "PyDrive Google Drive":
                newFolder = gdrive.CreateFile({'title': dall_e_prefs['batch_folder_name'], "parents": [{"kind": "drive#fileLink", "id": prefs['image_output']}],"mimeType": "application/vnd.google-apps.folder"})
                newFolder.Upload()
                batch_output = newFolder
            out_path = batch_output if save_to_GDrive else txt2img_output
            new_path = available_file(out_path, new_file, idx)
            if dall_e_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
                os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
                upload_folder = 'upload'
                result_folder = 'results'     
                if os.path.isdir(upload_folder):
                    shutil.rmtree(upload_folder)
                if os.path.isdir(result_folder):
                    shutil.rmtree(result_folder)
                os.mkdir(upload_folder)
                os.mkdir(result_folder)
                short_name = f'{fname[:80]}-{idx}.png'
                dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
                #print(f'Moving {fpath} to {dst_path}')
                #shutil.move(fpath, dst_path)
                shutil.copy(image_path, dst_path)
                faceenhance = ' --face_enhance' if dall_e_prefs["face_enhance"] else ''
                run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {dall_e_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
                out_file = short_name.rpartition('.')[0] + '_out.png'
                upscaled_path = new_path #os.path.join(out_path, new_file)
                shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
                # python inference_realesrgan.py --model_path experiments/pretrained_models/RealESRGAN_x4plus.pth --input upload --netscale 4 --outscale 3.5 --half --face_enhance
                os.chdir(stable_dir)
                if dall_e_prefs['display_upscaled_image']:
                    time.sleep(0.6)
                    prt(Row([Img(src=upscaled_path, width=size * float(dall_e_prefs["enlarge_scale"]), height=size * float(dall_e_prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
            else:
                shutil.copy(image_path, new_path)#os.path.join(out_path, new_file))
            # TODO: Add Metadata
            prt(Row([Text(new_path)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()

def run_kandinsky(page):
    global kandinsky_prefs, pipe_kandinsky, prefs
    if status['insalled_diffusers']:
      alert_msg(page, "Sorry, currently incompatible with Diffusers installed...", content=Text("To run Kandinsky, restart runtime fresh and DO NOT install HuggingFace Diffusers library first, but you can install ESRGAN to use. Kandinsky is currently using an older version of Transformers and we haven't figured out how to easily downgrade version yet to run models together.. Sorry, trying to fix."))
      return
    if not bool(kandinsky_prefs['prompt']):
      alert_msg(page, "You must provide a text prompt to process your image generation...")
      return
    def prt(line):
      if type(line) == str:
        line = Text(line, size=17)
      page.kandinsky_output.controls.append(line)
      page.kandinsky_output.update()
    def clear_last():
      del page.kandinsky_output.controls[-1]
      page.kandinsky_output.update()
    progress = ProgressBar(bar_height=8)
    prt(Row([ProgressRing(), Text("Installing Kandinsky 2.0 Engine & Models... See console log for progress.", weight=FontWeight.BOLD)]))
    '''try:
        if transformers.__version__ != "4.23.1": # Kandinsky conflict
          run_sp("pip uninstall -y transformers", realtime=True)
          run_process("pip uninstall -y git+https://github.com/huggingface/transformers", realtime=False)
    except Exception:
        pass
    finally:
        run_sp("pip install --target lib --upgrade transformers==4.23.1 -q", realtime=True)
        #print(f"Installed transformers v{transformers.__version__}")
    run_process("pip install -q sentencepiece", realtime=False)'''
    try:
        from kandinsky2 import get_kandinsky2
    except Exception:
        #run_process("pip install transformers==4.23.1 --upgrade --force-reinstall -q", realtime=False)
        #run_process("pip install -q git+https://github.com/ai-forever/Kandinsky-2.0.git", realtime=False)
        #run_sp('pip install -q "git+https://github.com/ai-forever/Kandinsky-2.0.git"', realtime=True)
        run_sp('pip install -q "git+https://github.com/Skquark/Kandinsky-2.0.git"', realtime=True)
        from kandinsky2 import get_kandinsky2
        pass
    import requests
    from io import BytesIO
    from PIL import ImageOps
    #save_dir = os.path.join(root_dir, 'kandinsky_inputs')
    init_img = None
    if bool(kandinsky_prefs['init_image']):
        fname = kandinsky_prefs['init_image'].rpartition(slash)[2]
        #init_file = os.path.join(save_dir, fname)
        if kandinsky_prefs['init_image'].startswith('http'):
            init_img = PILImage.open(requests.get(kandinsky_prefs['init_image'], stream=True).raw)
        else:
            if os.path.isfile(kandinsky_prefs['init_image']):
                init_img = PILImage.open(kandinsky_prefs['init_image'])
            else:
                alert_msg(page, f"ERROR: Couldn't find your init_image {kandinsky_prefs['init_image']}")
                return
        init_img = init_img.resize((kandinsky_prefs['width'], kandinsky_prefs['height']), resample=PILImage.LANCZOS)
        init_img = ImageOps.exif_transpose(init_img).convert("RGB")
        #init_img.save(init_file)
    mask_img = None
    if bool(kandinsky_prefs['mask_image']):
        fname = kandinsky_prefs['init_image'].rpartition(slash)[2]
        #mask_file = os.path.join(save_dir, fname)
        if kandinsky_prefs['mask_image'].startswith('http'):
            mask_img = PILImage.open(requests.get(kandinsky_prefs['mask_image'], stream=True).raw)
        else:
            if os.path.isfile(kandinsky_prefs['mask_image']):
                mask_img = PILImage.open(kandinsky_prefs['mask_image'])
            else:
                alert_msg(page, f"ERROR: Couldn't find your mask_image {kandinsky_prefs['mask_image']}")
                return
            if kandinsky_prefs['invert_mask']:
                mask_img = ImageOps.invert(mask_img.convert('RGB'))
        mask_img = mask_img.resize((kandinsky_prefs['width'], kandinsky_prefs['height']), resample=PILImage.NEAREST)
        mask_img = ImageOps.exif_transpose(mask_img).convert("RGB")
        mask_img = numpy.asarray(mask_img)
        #mask_img.save(mask_file)
    #print(f'Resize to {width}x{height}')
    clear_pipes()
    try:
        if bool(kandinsky_prefs['init_image']) and not bool(kandinsky_prefs['mask_image']):
            pipe_kandinsky = get_kandinsky2('cuda', task_type='img2img')
        elif bool(kandinsky_prefs['init_image']) and bool(kandinsky_prefs['mask_image']):
            pipe_kandinsky = get_kandinsky2('cuda', task_type='inpainting')
        else:
            pipe_kandinsky = get_kandinsky2('cuda', task_type='text2img')
    except Exception as e:
        import traceback
        clear_last()
        alert_msg(page, f"ERROR Initializing Kandinsky, try running without installing Diffusers first...", content=Column([Text(str(e)), Text(str(traceback.format_exc()))]))
        return
    clear_last()
    prt("Generating your Kandinsky 2.0 Image...")
    prt(progress)

    try:
        if bool(kandinsky_prefs['init_image']) and not bool(kandinsky_prefs['mask_image']):
            images = pipe_kandinsky.generate_img2img(kandinsky_prefs['prompt'], init_img, strength=kandinsky_prefs['strength'], batch_size=kandinsky_prefs['num_images'], w=kandinsky_prefs['width'], h=kandinsky_prefs['height'], num_steps=kandinsky_prefs['steps'], denoised_type=kandinsky_prefs['denoised_type'], dynamic_threshold_v=kandinsky_prefs['dynamic_threshold_v'], sampler=kandinsky_prefs['sampler'], ddim_eta=kandinsky_prefs['ddim_eta'], guidance_scale=kandinsky_prefs['guidance_scale'])
        elif bool(kandinsky_prefs['init_image']) and bool(kandinsky_prefs['mask_image']):
            images = pipe_kandinsky.generate_inpainting(kandinsky_prefs['prompt'], init_img, mask_img, batch_size=kandinsky_prefs['num_images'], w=kandinsky_prefs['width'], h=kandinsky_prefs['height'], num_steps=kandinsky_prefs['steps'], denoised_type=kandinsky_prefs['denoised_type'], dynamic_threshold_v=kandinsky_prefs['dynamic_threshold_v'], sampler=kandinsky_prefs['sampler'], ddim_eta=kandinsky_prefs['ddim_eta'], guidance_scale=kandinsky_prefs['guidance_scale'])
        else:
            images = pipe_kandinsky.generate_text2img(kandinsky_prefs['prompt'], batch_size=kandinsky_prefs['num_images'], w=kandinsky_prefs['width'], h=kandinsky_prefs['height'], num_steps=kandinsky_prefs['steps'], denoised_type=kandinsky_prefs['denoised_type'], dynamic_threshold_v=kandinsky_prefs['dynamic_threshold_v'], sampler=kandinsky_prefs['sampler'], ddim_eta=kandinsky_prefs['ddim_eta'], guidance_scale=kandinsky_prefs['guidance_scale'])
    except Exception as e:
        clear_last()
        clear_last()
        alert_msg(page, f"ERROR: Something went wrong generating images...", content=Text(str(e)))
        return
    clear_last()
    clear_last()
    txt2img_output = stable_dir
    batch_output = prefs['image_output']
    #print(str(images))
    if images is None:
        prt(f"ERROR: Problem generating images, check your settings and run again, or report the error to Skquark if it really seems broken.")
        return
    idx = 0
    for image in images:
        fname = format_filename(kandinsky_prefs['prompt'])
        #seed_suffix = f"-{random_seed}" if bool(prefs['file_suffix_seed']) else ''
        fname = f'{kandinsky_prefs["file_prefix"]}{fname}'
        txt2img_output = stable_dir
        if bool(kandinsky_prefs['batch_folder_name']):
            txt2img_output = os.path.join(stable_dir, kandinsky_prefs['batch_folder_name'])
        if not os.path.exists(txt2img_output):
            os.makedirs(txt2img_output)
        image_path = available_file(txt2img_output, fname, 1)
        image.save(image_path)
        new_file = image_path.rpartition(slash)[2]
        if not kandinsky_prefs['display_upscaled_image'] or not kandinsky_prefs['apply_ESRGAN_upscale']:
            prt(Row([Img(src=image_path, width=kandinsky_prefs['width'], height=kandinsky_prefs['height'], fit=ImageFit.FILL, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))

        if save_to_GDrive:
            batch_output = os.path.join(prefs['image_output'], kandinsky_prefs['batch_folder_name'])
            if not os.path.exists(batch_output):
                os.makedirs(batch_output)
        elif storage_type == "PyDrive Google Drive":
            newFolder = gdrive.CreateFile({'title': kandinsky_prefs['batch_folder_name'], "parents": [{"kind": "drive#fileLink", "id": prefs['image_output']}],"mimeType": "application/vnd.google-apps.folder"})
            newFolder.Upload()
            batch_output = newFolder
        out_path = batch_output if save_to_GDrive else txt2img_output
        
        if kandinsky_prefs['apply_ESRGAN_upscale'] and status['installed_ESRGAN']:
            os.chdir(os.path.join(dist_dir, 'Real-ESRGAN'))
            upload_folder = 'upload'
            result_folder = 'results'     
            if os.path.isdir(upload_folder):
                shutil.rmtree(upload_folder)
            if os.path.isdir(result_folder):
                shutil.rmtree(result_folder)
            os.mkdir(upload_folder)
            os.mkdir(result_folder)
            short_name = f'{fname[:80]}-{idx}.png'
            dst_path = os.path.join(dist_dir, 'Real-ESRGAN', upload_folder, short_name)
            #print(f'Moving {fpath} to {dst_path}')
            #shutil.move(fpath, dst_path)
            shutil.copy(image_path, dst_path)
            faceenhance = ' --face_enhance' if kandinsky_prefs["face_enhance"] else ''
            run_sp(f'python inference_realesrgan.py -n RealESRGAN_x4plus -i upload --outscale {kandinsky_prefs["enlarge_scale"]}{faceenhance}', cwd=os.path.join(dist_dir, 'Real-ESRGAN'), realtime=False)
            out_file = short_name.rpartition('.')[0] + '_out.png'
            upscaled_path = os.path.join(out_path, new_file)
            shutil.move(os.path.join(dist_dir, 'Real-ESRGAN', result_folder, out_file), upscaled_path)
            # python inference_realesrgan.py --model_path experiments/pretrained_models/RealESRGAN_x4plus.pth --input upload --netscale 4 --outscale 3.5 --half --face_enhance
            os.chdir(stable_dir)
            if kandinsky_prefs['display_upscaled_image']:
                time.sleep(0.6)
                prt(Row([Img(src=upscaled_path, width=kandinsky_prefs['width'] * float(kandinsky_prefs["enlarge_scale"]), height=kandinsky_prefs['height'] * float(kandinsky_prefs["enlarge_scale"]), fit=ImageFit.CONTAIN, gapless_playback=True)], alignment=MainAxisAlignment.CENTER))
        else:
            shutil.copy(image_path, os.path.join(out_path, new_file))
        # TODO: Add Metadata
        prt(Row([Text(new_file)], alignment=MainAxisAlignment.CENTER))
    if prefs['enable_sounds']: page.snd_alert.play()


def main(page: Page):
    page.title = "Stable Diffusion Deluxe - FletUI"
    #page.scroll=ScrollMode.AUTO
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
        title=Text("💁   Help/Information - Stable Diffusion Deluxe " + version), content=Column([Text("If you don't know what Stable Diffusion is, you're in for a pleasant surprise.. If you're already familiar, you're gonna love how easy it is to be an artist with the help of our AI friends with our pretty interface."),
              Text("Simply go through the self-explanitory tabs step-by-step and set your preferences to get started. The default values are good for most, but you can have some fun experimenting. All values are automatically saved as you make changes and change tabs."),
              Text("Each time you open the app, you should start in the Installers section, turn on all the components you plan on using in you session, then Run the Installers and let them download. You can multitask and work in other tabs while it's installing."),
              Text("In the Prompts List, add as many text prompts as you can think of, and edit any prompt to override any default Image Parameter.  Once you're ready, run diffusion on your prompts list and watch it fill your Google Drive.."),
              Text("Try out any and all of our Prompt Helpers to use practical text AIs to make unique descriptive prompts fast, with our Prompt Generator, Remixer, Brainstormer and Advanced Writer.  You'll never run out of inspiration again..."),
        ], scroll=ScrollMode.AUTO),
        actions=[TextButton("👍  Thanks! ", on_click=close_help_dlg)], actions_alignment=MainAxisAlignment.END,
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
        ], scroll=ScrollMode.AUTO),
        actions=[TextButton("👊   Good Stuff... ", on_click=close_credits_dlg)], actions_alignment=MainAxisAlignment.END,
    )
    page.theme_mode = prefs['theme_mode'].lower()
    if prefs['theme_mode'] == 'Dark':
      page.dark_theme = theme.Theme(color_scheme_seed=prefs['theme_color'].lower())#, use_material3=True)
    else:
      page.theme = theme.Theme(color_scheme_seed=prefs['theme_color'].lower())
    app_icon_color = colors.AMBER_800
    
    appbar=AppBar(title=Text("👨‍🎨️  Stable Diffusion - Deluxe Edition  🖌️" if page.width >= 768 else "Stable Diffusion Deluxe  🖌️", weight=FontWeight.BOLD),elevation=20,
      center_title=True,
          bgcolor=colors.SURFACE_VARIANT,
          leading=IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Save Settings File", on_click=lambda _: app_icon_save()),
          #leading_width=40,
          actions=[
              PopupMenuButton(
                  items=[
                      PopupMenuItem(text="🤔  Help/Info", on_click=open_help_dlg),
                      PopupMenuItem(text="👏  Credits", on_click=open_credits_dlg),
                      PopupMenuItem(text="🤧  Issues/Suggestions", on_click=lambda _:page.launch_url("https://github.com/Skquark/AI-Friends/issues")),
                      PopupMenuItem(text="📨  Email Skquark", on_click=lambda _:page.launch_url("mailto:Alan@Skquark.com")),
                      PopupMenuItem(text="🤑  Offer Donation", on_click=lambda _:page.launch_url("https://paypal.me/StarmaTech")),
                      #PopupMenuItem(text="❎  Exit/Disconnect Runtime", on_click=exit_disconnect) if is_Colab else PopupMenuItem(),
                  ]
              ),
          ])
    if is_Colab:
      appbar.actions[0].items.append(PopupMenuItem())
      appbar.actions[0].items.append(PopupMenuItem(text="❎  Exit/Disconnect Runtime", on_click=exit_disconnect))
    page.appbar = appbar
    def app_icon_save():
      app_icon_color = colors.GREEN_800
      appbar.leading = IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Saving Settings File")
      appbar.update()
      time.sleep(0.6)
      app_icon_color = colors.AMBER_800
      appbar.leading = IconButton(icon=icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, icon_color=app_icon_color, icon_size=32, tooltip="Save Settings File", on_click=lambda _: app_icon_save())
      appbar.update()
    page.app_icon_save = app_icon_save
    page.vertical_alignment = MainAxisAlignment.START
    page.horizontal_alignment = CrossAxisAlignment.START
    t = buildTabs(page)
    t.on_change = tab_on_change
    #(t,page)
    def close_banner(e):
        page.banner.open = False
        page.update()
    #leading=Icon(icons.DOWNLOADING, color=colors.AMBER, size=40), 
    page.banner = Banner(bgcolor=colors.SECONDARY_CONTAINER, content=Column([]), actions=[TextButton("Close", on_click=close_banner)])
    def show_banner_click(e):
        page.banner.open = True
        page.update()

    page.add(t)
    if not status['initialized']:
        initState(page)
        status['initialized'] = True
    #page.add(ElevatedButton("Show Banner", on_click=show_banner_click))
    #page.add (Text ("Enhanced Stable Diffusion Deluxe by Skquark, Inc."))

class NumberPicker(UserControl):
    def __init__(self, label="", value=1, min=0, max=20, step=1, on_change=None):
        super().__init__()
        self.value = value
        self.min = min
        self.max = max
        self.step = step
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
              self.value -= self.step
              self.txt_number.value = self.value
              self.txt_number.update()
              e.control = self
              if self.on_change is not None:
                self.on_change(e)
        def plus_click(e):
            v = int(self.value)
            if v < self.max:
              self.value += self.step
              self.txt_number.value = self.value
              self.txt_number.update()
              e.control = self
              if self.on_change is not None:
                self.on_change(e)
        self.txt_number = TextField(value=str(self.value), text_align=TextAlign.CENTER, width=55, height=42, content_padding=padding.only(top=4), keyboard_type=KeyboardType.NUMBER, on_change=changed)
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
        return Column(controls=[])
class Main:
    def __init__(self):
        self.page = None
    def __call__(self, page: Page):
        self.page = page
        page.title = "Alternative Boot experiment"
        self.add_stuff()
    def add_stuff(self):
        self.page.add(Text("Some text", size=20))
        self.page.update()
main = Main()'''

port = 8510
if tunnel_type == "ngrok":
  if bool(url):
    public_url = url
  else:
    from pyngrok import ngrok
    public_url = ngrok.connect(port = str(port)).public_url
elif tunnel_type == "localtunnel":
  if False:
  #if bool(url):
    public_url = url
  else:
    import re
    localtunnel = subprocess.Popen(['lt', '--port', '80', 'http'], stdout=subprocess.PIPE)
    url = str(localtunnel.stdout.readline())
    public_url = (re.search("(?P<url>https?:\/\/[^\s]+loca.lt)", url).group("url"))
else: public_url=""
from IPython.display import Javascript
if bool(public_url):
    if auto_launch_website:
        display(Javascript('window.open("{url}");'.format(url=public_url)))
        time.sleep(0.7)
        clear_output()
    print("\nOpen URL in browser to launch app in tab: " + str(public_url))

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
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host=socket_host)
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host=host_address)
#flet.app(target=main, view=flet.WEB_BROWSER, port=80, host=public_url.public_url)
#flet.app(target=main, view=flet.WEB_BROWSER, port=port, host="0.0.0.0")
if tunnel_type == "desktop":
  flet.app(target=main, assets_dir=root_dir, upload_dir=root_dir)
else:
  flet.app(target=main, view=flet.WEB_BROWSER, port=80, assets_dir=root_dir, upload_dir=root_dir, web_renderer="html")
