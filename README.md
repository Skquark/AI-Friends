# AI-Friends
A collection of handy helpers for AI art generation, AI writing and other experimental tools
---
# 🎨 **Stable Diffusion Deluxe Edition** 👨‍🎨️ - Python to Flutter Framework

*...using `🧨diffusers`* and practical bonus features...



---
### Designed by [**Skquark**, Inc.](https://www.Skquark.com) 😋
<p align=center>
<a href="https://github.com/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb"><img src="https://badgen.net/badge/icon/github?icon=github&label" alt="Github"></a> <a href="https://github.com/Skquark/AI-Friends"><img src="https://badgen.net/github/release/Skquark/AI-Friends/stable" alt="Release version"></a>
<a href="https://colab.research.google.com/github/Skquark/AI-Friends/blob/main/Stable_Diffusion_Deluxe.ipynb"><img src="https://img.shields.io/badge/Open-in%20Colab-brightgreen?logo=google-colab&style=flat-square" alt="Open in Google Colab"/></a>
</p>

*   Runs in a pretty WebUI using [Flet - Flutter for Python](https://flet.dev) with themes, interactivity & sound
*   Saves all settings/parameters in your config file, don't need to Copy to Drive
*   Run a batch list of prompts at once, so queue many and walk away
*   Option to override any parameter per prompt in queue
*   Option to use Stability-API tokens for more samplers, bigger size & CPU runtime
*   Use Stable Diffusion [1.5 Checkpoint Model File](https://huggingface.co/runwayml/stable-diffusion-v1-5), or the [1.4 models](https://huggingface.co/CompVis/stable-diffusion-v1-4)
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

Can also use origional Colab implementation of [Enhanced Stable Diffusion](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/Enhanced_Stable_Diffusion_with_diffusers.ipynb) instead..

Try these other useful notebooks [Enhanced DiscoArt](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/DiscoArt_%5B_w_Batch_Prompts_%26_GPT_3_Generator%5D.ipynb) and [Structured Prompt Generator](https://colab.research.google.com/github/Skquark/structured-prompt-generator/blob/main/Structured_Prompt_Generator.ipynb)

Feature Short List: Uses Enhanced Diffusers in Material UI Flutter/Flet GUI with Themes & SoundFX, Stable Diffusion v2.1 & lower, advanced Prompts List with overrides, many Finetuned Community Models, Dreambooth Library, Long Prompt Weighting, Walk Interpolation, Prompt Tweening, Centipede Prompts as init-images, CLIP-Guided, Textual-Inversion Conceptualizer, Dual Guided Versatile Diffusion, Image Variation, iMagic, Depth2Image, Composable, Self-Attention Guidance, Attend & Excite, Panorama, Safe Pipeline, DeepFloyd-IF, unCLIP Generator, unCLIP Image Variations, unCLIP Interpolation & Image Interpolation, Text-to-Video, Text2Video-Zero, Potat1 Text-to-Video, Stable Animation, Stability-API, AIHorde-API, SD2 4X Upscale, Real-ESRGAN Upscaling, Prompt Writer, GPT-3 & ChatGPT Prompt Generator, Prompt Remixer, Prompt Brainstormer, GPT-2 Magic Prompt, Distil GPT-2, DreamBooth, LoRA & Texual Inversion Trainer, Model Converter & Merger, SD2 Image Variations, EDICT Editor, DiffEdit, MagicMix, RePainter, Paint-by-Example, Instruct Pix2Pix, ControlNet Multi, ControlNet QRCode, Reference-Only, Re-Segment Anything, CLIP-Styler, Semantic Guidance, Material Diffusion, DreamFusion 3D, Point-E 3D, Shap-E 3D, InstantNGR, Tortoise TTS, HarmonAI Dance Diffusion, Audio Diffusion, Bark, Riffusion, AudioLDM Text2Sound, MusicGen, Mubert Music, Whisper STT, Image2Text Interrogator, DALL-E 2 API, Kandinsky 2.1 & Fuser, DeepDaze, Metadata in png, smart filenames, Batch Upscaler, Prompt Retriever, Cache Manager, Init Images from Folder or Video, and more being added regularly..