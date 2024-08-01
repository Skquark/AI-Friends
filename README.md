# AI-Friends
A collection of handy helpers for AI art generation, AI writing and other experimental tools
---
# 🎨 **Stable Diffusion Deluxe Edition** 👨‍🎨️ - Python to Flutter Framework

*...using `🧨diffusers`* and practical bonus features...



---
### Designed by [**Skquark**, Inc.](https://www.Skquark.com) 😋 - Project at [DiffusionDeluxe.com](https://DiffusionDeluxe.com)
<p align=center>
<a href="https://github.com/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb"><img src="https://badgen.net/badge/icon/github?icon=github&label" alt="Github"></a> <a href="https://github.com/Skquark/AI-Friends"><img src="https://badgen.net/github/release/Skquark/AI-Friends/stable" alt="Release version"></a>
<a href="https://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb"><img src="https://img.shields.io/badge/Open-in%20Colab-brightgreen?logo=google-colab&style=flat-square" alt="Open in Google Colab"/></a>
</p>

*   Runs in a pretty WebUI using [Flet - Flutter for Python](https://flet.dev) with themes, interactivity & sound
*   Saves all settings/parameters in your config file, don't need to Copy to Drive
*   Run a batch list of prompts at once, so queue many and walk away
*   Option to override any parameter per prompt in queue
*   Option to use Stability-API tokens for more samplers, bigger size & CPU runtime
*   Use Stable Diffusion [XL](https://huggingface.co/stabilityai/stable-diffusion-xl-base-0.9), [2.1](https://huggingface.co/stabilityai/stable-diffusion-2-1), [2.0](https://huggingface.co/stabilityai/stable-diffusion-2), [1.5 ](https://huggingface.co/runwayml/stable-diffusion-v1-5), or [1.4](https://huggingface.co/CompVis/stable-diffusion-v1-4) Checkpoint Model File
*   Supports Stable Diffusion image2image to use an init_image
*   Supports Stable Diffusion [Inpaint](https://huggingface.co/runwayml/stable-diffusion-inpainting) mask_image layer
*   Supports Negative Prompts to specify what you don't want
*   Supports Long Prompt Weighting to emphasize (positive) & [negative] word strengths
*   Prompt tweening to combine latent space of 2 prompts in a series
*   Can use Interpolation to walk steps between latent space of prompt list
*   Can use CLIP Guidance with LAION & OpenAI ViT models
*   Can use Textual Inversion Conceptualizer with 760+ Community Concepts
*   Can Centipede prompts as init images feeding down the list
*   Can save all images to your Google Drive (PyDrive support soon)
*   Can Upscale automatically with Real-ESRGAN enlarging
*   Embeds exif metadata directly into png files
*   Disabled NSFW filtering and added custom sampler options
*   Renames image filenames to the prompt text, with options
*   OpenAI Prompt Generator, Remixer, Brainstormer & Noodle Soup Prompt Writer included
*   Standalone ESRGAN Upscaler for batch uploads and image splitting
*   Experimental HarmonAI Dance Diffusion audio generator
*   Experimental DreamFusion 3D model generator with texture & video
*   Additional features added regularly...

#### <a href="https://github.com/Skquark/AI-Friends/raw/main/Stable-Diffusion-Deluxe/SDD-setup.exe">Download Windows</a> | <a href="https://github.com/Skquark/AI-Friends/raw/main/Stable-Diffusion-Deluxe/SDD-setup-noadmin.exe">Download Windows No-Admin</a> | <a href="https://github.com/Skquark/AI-Friends/raw/main/Stable-Diffusion-Deluxe/sdd-linux.sh">Download Linux/Mac Script</a> | <a href="https://DiffusionDeluxe.com">Project Website</a>

Can also use origional Colab implementation of [Enhanced Stable Diffusion](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/Enhanced_Stable_Diffusion_with_diffusers.ipynb) instead..

Try these other useful notebooks [Enhanced DiscoArt](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/DiscoArt_%5B_w_Batch_Prompts_%26_GPT_3_Generator%5D.ipynb) and [Structured Prompt Generator](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/Structured_Prompt_Generator.ipynb)

Feature Short List: Uses Enhanced Diffusers in Material UI Flutter/Flet GUI with Themes & SoundFX, Stable Diffusion XL & lower, advanced Prompts List with overrides, many Finetuned Community Models, Dreambooth Library, Long Prompt Weighting, Walk Interpolation, Prompt Tweening, Centipede Prompts as init-images, CLIP-Guided, Textual-Inversion Conceptualizer, Dual Guided Versatile Diffusion, Image Variation, LoRA Adapters, IP-Adapters, iMagic, Depth2Image, Composable, Self-Attention Guidance, Attend & Excite, Panorama, Safe Pipeline, ControlNet SDXL & XS, DeepFloyd-IF, Stable Cascade, Wuerstchen, PixArt-alpha, LMD+, LCM, unCLIP Generator, unCLIP Image Variations, unCLIP Interpolation & Image Interpolation, LEdits++, Null-Text Inversion, AnyText, aMUSEd, DemoFusion, Text-to-Video, Text2Video-Zero, AnimateDiff Enhanced, SVD, Potat1 Text-to-Video, Infinite Zoom, Rerender-a-Video, TemporalNet XL, ControlNet Video2Video, Video-to-Video, ROOP Face Swapper, Video ReTalking, AnimateDiff to-Video, I2VGen-XL, Stable Animation, Stability-API, PIA Image Animator, TokenFlow, StyleCrafter, RAVE, AIHorde-API, SD2 4X Upscale, Real-ESRGAN Upscaling, Prompt Writer, PaLM Gemini, Antrhopic Claude 3, GPT-3, 4 ChatGPT Prompt Generator, Prompt Remixer, Prompt Brainstormer, Styler, Negatives Builder, GPT-2 Magic Prompt, Distil GPT-2, DreamBooth, LoRA & Texual Inversion Trainer, Model Converter & Merger, SD2 Image Variations, EDICT Editor, DiffEdit, MagicMix, RePainter, Paint-by-Example, Instruct Pix2Pix, ControlNet Multi, ControlNet QRCode, BLIP-Diffusion, Reference-Only, Re-Segment Anything, CLIP-Styler, Semantic Guidance, Material Diffusion, DreamFusion 3D, Point-E 3D, Shap-E 3D, LDM3D, Luma Vid-to-3D, ZoeDepth, MarigoldDepth, Tripo, CRM 3D, InstantNGR, Meshy.ai, Tortoise TTS, HarmonAI Dance Diffusion, Audio Diffusion, Bark, Riffusion, AudioLDM Text2Sound, MusicLDM, MusicGen, ZETA Editing, Mubert Music, Whisper STT, VoiceFixer, Image2Text Interrogator, DALL-E 2 API, DALL-E 3, Kandinsky 3/2.2 & Fuser, Kandinsky ControlNet, DeepDaze, Background Remover, Metadata in png, smart filenames, Batch Upscaler, Prompt Retriever, Cache Manager, Init Images from Folder or Video, and more being added regularly..