finetuned_models = [
    #{"name": "Stable Diffusion v1.5", "path": "runwayml/stable-diffusion-v1-5", "prefix": "", "revision": "fp16"},
    #{"name": "Stable Diffusion v1.4", "path": "CompVis/stable-diffusion-v1-4", "prefix": "", "revision": "fp16"},
    {"name": "Midjourney v4 style", "path": "prompthero/midjourney-v4-diffusion", "prefix": "mdjrny-v4 style "},
    {"name": "Midjourney-mini", "path": "openskyml/midjourney-mini", "prefix": ""},
    {"name": "OpenDiffusion v1", "path": "openskyml/open-diffusion-v1", "prefix": ""},
    {"name": "Openjourney", "path": "prompthero/openjourney", "prefix": "mdjrny-v4 style "},
    {"name": "Openjourney v2", "path": "prompthero/openjourney-v2", "prefix": ""},
    {"name": "Future Diffusion", "path": "nitrosocke/Future-Diffusion", "prefix": "future style "},
    #{"name": "Absolute Realism 1.81", "path": "Lykon/absolute-realism-1.81", "prefix": ""},
    {"name": "Am I Real v4.2", "path": "GraydientPlatformAPI/amireal42-proper", "prefix": ""},
    {"name": "Anything v3.0", "path": "ckpt/anything-v3.0", "prefix": ""},
    #{"name": "Anything v4.0", "path": "andite/anything-v4.0", "prefix": ""},
    {"name": "Anything v4.5", "path": "ckpt/anything-v4.5", "prefix": ""},
    {"name": "Anything v5", "path": "stablediffusionapi/anything-v5", "prefix": ""},
    {"name": "Analog Diffusion", "path": "wavymulder/Analog-Diffusion", "prefix": "analog style "},
    {"name": "Architecture Diffusers", "path": "rrustom/stable-architecture-diffusers", "prefix": ""},
    {"name": "Arcane", "path":"nitrosocke/Arcane-Diffusion", "prefix":"arcane style "},
    {"name": "Archer Diffusion", "path":"nitrosocke/archer-diffusion", "prefix":"archer style "},
    {"name": "Nitro Diffusion", "path":"nitrosocke/nitro-diffusion", "prefix":"archer style, arcane style, modern disney style "},
    {"name": "Beeple Diffusion", "path": "riccardogiorato/beeple-diffusion", "prefix": "beeple style "},
    {"name": "Protogen v5.8", "path": "darkstorm2150/Protogen_x5.8_Official_Release", "prefix": ""},
    {"name": "Protogen Eclipse", "path": "darkstorm2150/Protogen_Eclipse_Official_Release", "prefix": ""},
    #{"name": "Protogen Infinity", "path": "darkstorm2150/Protogen_Infinity_Official_Release", "prefix": ""},
    #{"name": "Protogen Nova", "path": "darkstorm2150/Protogen_Nova_Official_Release", "prefix": ""},
    {"name": "Protogen Dragon", "path": "darkstorm2150/Protogen_Dragon_Official_Release", "prefix": ""},
    {"name": "Deliberate", "path": "XpucT/Deliberate", "prefix":""},
    {"name": "Deliberate 2", "path": "SdValar/deliberate2", "prefix":""},
    {"name": "di.FFUSION.ai", "path": "FFusion/di.FFUSION.ai-v2.1-768-BaSE-alpha", "prefix":""},
    {"name": "Elden Ring", "path": "nitrosocke/elden-ring-diffusion", "prefix":"elden ring style "},
    {"name": "Freedom", "path": "artificialguybr/freedom", "prefix":""},
    {"name": "Modern Disney", "path": "nitrosocke/mo-di-diffusion", "prefix": "modern disney style "},
    {"name": "Classic Disney", "path": "nitrosocke/classic-anim-diffusion", "prefix": "classic disney style "},
    {"name": "Loving Vincent (Van Gogh)", "path": "dallinmackay/Van-Gogh-diffusion", "prefix": "lvngvncnt "},
    {"name": "Realistic Vision v1.4", "path": "SG161222/Realistic_Vision_V1.4", "prefix": ""},
    {"name": "Realistic Vision v3", "path": "SG161222/Realistic_Vision_V3.0", "prefix": ""},
    {"name": "Realistic Vision v5.1", "path": "stablediffusionapi/realistic-vision-v51", "prefix": ""},
    {"name": "Realistic Vision v6.0", "path": "stablediffusionapi/realistic_vision_v60", "prefix": ""},
    {"name": "Redshift Renderer (Cinema4D)", "path": "nitrosocke/redshift-diffusion", "prefix": "redshift style "},
    {"name": "Reliberate", "path": "sinkinai/reliberate_v10", "prefix": ""},
    {"name": "ReV Animated Remix", "path": "Yntec/ReVAnimatedRemix", "prefix": ""},
    {"name": "ReV Animated v2 Rebirth", "path": "rubbrband/revAnimated_v2RebirthVAE", "prefix": ""},
    {"name": "Swizz8", "path": "Pr0-SD/Swizz8", "prefix": ""},
    {"name": "Waifu Diffusion", "path": "hakurei/waifu-diffusion", "prefix": "", "revision": "fp16"},
    {"name": "Ultima Waifu Diffusion", "path": "AdamOswald1/Ultima-Waifu-Diffusion", "prefix": ""},
    #{"name": "TrinArt Waifu 50-50", "path": "doohickey/trinart-waifu-diffusion-50-50", "prefix": ""},
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
    {"name": "Dreamlike Photoreal 2", "path": "dreamlike-art/dreamlike-photoreal-2.0", "prefix": ""},
    {"name": "DreamShaper", "path": "Lykon/DreamShaper", "prefix": ""},
    {"name": "DreamShaper 7", "path": "digiplay/DreamShaper_7", "prefix": ""},
    {"name": "DreamShaper 8", "path": "Lykon/dreamShaper-8", "prefix": ""},
    {"name": "Absolute Reality", "path": "Lykon/AbsoluteReality", "prefix": ""},
    {"name": "Glitch", "path": "BakkerHenk/glitch", "prefix": "a photo in sks glitched style "},
    {"name": "Knollingcase", "path": "Aybeeceedee/knollingcase", "prefix": "knollingcase "},
    {"name": "Wavy Diffusion", "path": "wavymulder/wavyfusion", "prefix": "wa-vy style "},
    {"name": "TARDISfusion Classic Tardis", "path": "Guizmus/Tardisfusion", "prefix": "Classic Tardis style "},
    {"name": "TARDISfusion Modern Tardis", "path": "Guizmus/Tardisfusion", "prefix": "Modern Tardis style "},
    {"name": "TARDISfusion Tardis Box", "path": "Guizmus/Tardisfusion", "prefix": "Tardis Box style "},
    {"name": "Rick-Roll Style", "path": "TheLastBen/rick-roll-style", "prefix": "rckrll "},
    {"name": "Filmation MOTU", "path": "zuleo/filmation-motu", "prefix": ""},
    {"name": "F222", "path": "SY573M404/f222-diffusers", "prefix": ""},
    {"name": "Char Helper", "path": "ManglerFTW/CharHelper", "prefix": ""},
    {"name": "Copax Realistic", "path": "KamCastle/copaxRealistic", "prefix": ""},
    {"name": "Maxwell the Cat", "path": "kabachuha/maxwell-the-cat-diffusion", "prefix": ""},
    {"name": "Glitch Embedding", "path": "joachimsallstrom/Glitch-Embedding", "prefix": "glitch "},
    {"name": "Pokemon 3D", "path": "Timmahw/SD2.1_Pokemon3D", "prefix": ""},
    {"name": "Nephos", "path": "RomeroRZ/Nephos", "prefix": ""},
    {"name": "NeverEnding Dream", "path": "Lykon/NeverEnding-Dream", "prefix": ""},
    {"name": "effeffIX Concept", "path": "zuleo/effeffIX-concept-diffusion", "prefix": "effeff9 "},
    {"name": "effeffIX Woman", "path": "zuleo/effeffIX-concept-diffusion", "prefix": "effeff9 woman "},
    {"name": "effeffIX Man", "path": "zuleo/effeffIX-concept-diffusion", "prefix": "effeff9 man "},
    {"name": "effeffIX Creature", "path": "zuleo/effeffIX-concept-diffusion", "prefix": "effeff9 creature "},
    {"name": "effeffIX Architecture", "path": "zuleo/effeffIX-concept-diffusion", "prefix": "effeff9 architecture "},
    {"name": "Double-Exposure-Diffusion", "path": "joachimsallstrom/Double-Exposure-Diffusion", "prefix": "dublex style "},
    #{"name": "Illuminati Diffusion", "path": "IlluminatiAI/Illuminati_Diffusion_v1.0", "prefix": ""},
    {"name": "ChillOutMix", "path": "windwhinny/chilloutmix", "prefix": ""},
    {"name": "Colorful-v1.3", "path": "digiplay/Colorful_v1.3", "prefix": ""},
    {"name": "Colorful-v4.5", "path": "Manseo/Colorful-v4.5", "prefix": ""},
    {"name": "Cool Japan Diffusion", "path": "aipicasso/cool-japan-diffusion-2-1-2-beta", "prefix": ""},
    {"name": "Fantasy Mix", "path": "theintuitiveye/FantasyMix-v1", "prefix": ""},
    {"name": "Level 4 v3", "path": "Yntec/level4", "prefix": ""},
    {"name": "RealCartoon 3D", "path": "digiplay/RealCartoon3D_v6", "prefix": ""},
    {"name": "RealCartoon 3D Full", "path": "digiplay/RealCartoon3D_F16full_v3.1", "prefix": ""},
    {"name": "RealCartoon Pixar", "path": "ironjr/RealCartoon-PixarV5", "prefix": ""},
    {"name": "RealCartoon Realistic v1.4", "path": "rubbrband/realcartoonRealistic_v14", "prefix": ""},
    {"name": "Roughness Painter", "path": "AIARTCHAN/roughnessPainter_v1.0", "prefix": ""},
    {"name": "Isometric Dreams", "path": "Duskfallcrew/isometric-dreams-sd-1-5", "prefix": ""},
    {"name": "Photography & Landscapes", "path": "Duskfallcrew/photography-and-landscapes", "prefix": "phtdzk1 "},
    {"name": "Sygil Diffusion", "path": "Sygil/Sygil-Diffusion", "prefix": ""},
    {"name": "Flat Icons", "path": "viba98/flat-icons", "prefix": ""},
    {"name": "No Branch Repo", "path": "huggingface/the-no-branch-repo", "prefix": ""},
    {"name": "Isometric Floating Icons", "path": "viba98/isometric-floating-icons", "prefix": ""},
    {"name": "Dilbert Diffusion", "path": "CSAle/DilbertDiffusion2", "prefix": "dilbert "},
    {"name": "Sketchstyle", "path": "Cosk/sketchstyle-cutesexyrobutts", "prefix": "sketchstyle "},
    {"name": "Midjourney Shatter", "path": "ShadoWxShinigamI/Midjourney-Shatter", "prefix": "mdjrny-shttr "},
    {"name": "Midjourney PaperCut", "path": "ShadoWxShinigamI/MidJourney-PaperCut", "prefix": "mdjrny-pprct eagle "},
    {"name": "Midjourney Graffiti", "path": "ShadoWxShinigamI/midjourney-graffiti", "prefix": "in the style of mdjrny-grfft "},
    {"name": "MJStyle", "path": "ShadoWxShinigamI/mjstyle", "prefix": "mjstyle "},
    {"name": "Xpero End1ess", "path": "sakistriker/XperoEnd1essModel", "prefix": ""},
    {"name": "Pepe Diffuser", "path": "Dipl0/pepe-diffuser", "prefix": ""},
    {"name": "Pastel Mix", "path": "andite/pastel-mix", "prefix": ""},
    {"name": "Pony Diffusion 4", "path": "AstraliteHeart/pony-diffusion-v4", "prefix": ""},
    {"name": "Counterfeit v2.5", "path": "gsdf/Counterfeit-V2.5", "prefix": ""},
    {"name": "Basil Mix", "path": "nuigurumi/basil_mix", "prefix": ""},
    {"name": "Inkpunk Diffusion", "path": "Envvi/Inkpunk-Diffusion", "prefix": "nvinkpunk "},
    {"name": "Ghibli Diffusion", "path": "nitrosocke/Ghibli-Diffusion", "prefix": "ghibli style "},
    {"name": "7th Layer", "path": "syaimu/7th_Layer", "prefix": ""},
    {"name": "Comic-Diffusion", "path": "ogkalu/Comic-Diffusion", "prefix": ""},
    {"name": "Vintedois Diffusion", "path": "22h/vintedois-diffusion-v0-1", "prefix": ""},
    {"name": "PaperCut", "path": "Fictiverse/Stable_Diffusion_PaperCut_Model", "prefix": "PaperCut "},
    {"name": "Complex Lineart", "path": "Conflictx/Complex-Lineart", "prefix": "ComplexLA style "},
    {"name": "GuoFeng3", "path": "xiaolxl/GuoFeng3", "prefix": ""},
    {"name": "Portrait+", "path": "wavymulder/portraitplus", "prefix": "portrait+ style "},
    {"name": "ACertainThing", "path": "JosephusCheung/ACertainThing", "prefix": ""},
    {"name": "Hassan Blend", "path": "hassanblend/HassanBlend1.5.1.2", "prefix": ""},
    {"name": "Segmind Small-SD", "path": "segmind/small-sd", "prefix": ""},
    {"name": "SD-Turbo", "path": "stabilityai/sd-turbo", "prefix": ""},
    #{"name": "", "path": "", "prefix": ""},
    #{"name": "Latent Labs 360", "path": "AlanB/LatentLabs360", "prefix": ""},
    #{"name": "Rodent Diffusion 1.5", "path": "NerdyRodent/rodent-diffusion-1-5", "prefix": ""},
    #{"name": "Laxpeint", "path": "EldritchAdam/laxpeint", "prefix": ""},
    #{"name": "HeartArt", "path": "spaablauw/HeartArt", "prefix": ""},
    #{"name": "ConceptArt", "path": "SatyamSSJ10/ConceptArt", "prefix": ""},
    #{"name": "Modern Buildings", "path": "smereces/2.1-SD-Modern-Buildings-Style-MD", "prefix": ""},
    #{"name": "Floral Marbles", "path": "N75242/FloralMarbles_Model", "prefix": ""},
    #{"name": "Gemini_Anime", "path": "Cryonicus/Gemini_Anime", "prefix": ""},
    #{"name": "Disco Difland", "path": "DarkBeam/discodifland", "prefix": ""},
    #{"name": "Princess Jai Lee", "path": "zuleo/princess-jai-lee", "prefix": ""},
    #{"name": "Style Goblinmode", "path": "TheAllyPrompts/Style-Goblinmode", "prefix": ""},
    #{"name": "Joe87-Vibe", "path": "Joe87/joe87-vibe", "prefix": "joe87-vibe "},
    #{"name": "Microwaist", "path": "SweetTalk/Microwaist", "prefix": ""},
    #{"name": "Sci-Fi Diffusion", "path": "Corruptlake/Sci-Fi-Diffusion", "prefix": ""},
    #{"name": "ParchArt", "path": "EldritchAdam/ParchArt", "prefix": ""},
    #{"name": "Classipeint", "path": "EldritchAdam/classipeint", "prefix": ""},
    #{"name": "Cyberpunked", "path": "GeneralAwareness/Cyberpunked", "prefix": ""},
    #{"name": "Mangaka Boichi", "path": "Akumetsu971/SD_Boichi_Art_Style", "prefix": ""},
    #{"name": "Samurai Anime", "path": "Akumetsu971/SD_Samurai_Anime_Style", "prefix": ""},
    #{"name": "Cmodel", "path": "jinofcoolnes/CmodelSDV2", "prefix": "cmodel "},
    #{"name": "Cyberware", "path": "Eppinette/Cyberware", "prefix": "-cyberware style "},
    #{"name": "OldJourney", "path": "StarwingDigital/Oldjourney", "prefix": ""},
    #{"name": "Hyper Smoke", "path": "spaablauw/HyperSmoke", "prefix": ""},
    #{"name": "Fantasy Diffusion", "path": "IceChes/fantasydiffusionembedding", "prefix": ""},
    #{"name": "Double-Exposure", "path": "joachimsallstrom/Double-Exposure-Embedding", "prefix": "dblx "},
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
LoRA_models = [
    {'name': 'LCM LoRA', 'path': 'latent-consistency/lcm-lora-sdv1-5', 'prefix':''},
    {'name': 'ByteDance Hyper-SD 8steps', 'path': 'ByteDance/Hyper-SD', 'weights': 'Hyper-SD15-8steps-lora.safetensors'},
    {'name': 'Dog Example', 'path':'patrickvonplaten/lora_dreambooth_dog_example'},
    {'name': 'SayakPaul LoRA-T4', 'path': 'sayakpaul/sd-model-finetuned-lora-t4'},
    {'name': 'Openjourney LoRA', 'path':'prompthero/openjourney-lora', 'prefix': ''},
    {'name': 'Logo.Redmond 1.5V', 'path':'artificialguybr/logo-redmond-1-5v-logo-lora-for-liberteredmond-sd-1-5', 'prefix': 'LogoRedAF, logo', 'weights': 'LogoRedmond15V-LogoRedmAF-Logo.safetensors'},
    {'name': 'Transformers Style', 'path':'AlanB/TransformersStyle', 'prefix': 'TransformersStyle', 'weights': 'TransformersStyle.safetensors'},
    {'name': 'Analog Diffusion', 'path':'https://replicate.delivery/pbxt/IzbeguwVsW3PcC1gbiLy5SeALwk4sGgWroHagcYIn9I960bQA/tmpjlodd7vazekezip.safetensors', 'prefix':'<1> '},
    {'name': 'Analog.Redmond', 'path': 'artificialguybr/analogredmond', 'prefix':'AnalogRedmAF'},
]
SDXL_models = [
    {"name": "SDXL-Base v1", "path": "stabilityai/stable-diffusion-xl-base-1.0", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "SDXL-Turbo", "path": "stabilityai/sdxl-turbo", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "AAM XL AnimeMix", "path": "Lykon/AAM_XL_AnimeMix", "prefix": "", "use_safetensors": True},
    {"name": "AE SDXL v4", "path": "stablediffusionapi/ae-sdxl-v4", "prefix": ""},
    {"name": "AlbedoBase XL 2.0", "path": "stablediffusionapi/albedobase-xl-20", "prefix": ""},
    {"name": "Animagine-XL 3.1", "path": "cagliostrolab/animagine-xl-3.1", "prefix": "", "use_safetensors": True},
    {"name": "Animagine-XL 3.1 FP16", "path": "Asahina2K/Animagine-xl-3.1-diffuser-variant-fp16", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Animagine-XL 3", "path": "cagliostrolab/animagine-xl-3.0", "prefix": "", "use_safetensors": True},
    {"name": "Animagine-XL 3 Lightning", "path": "Bakanayatsu/Animagine-xl-3.0-2step-Lightning", "prefix": ""},
    {"name": "Anime-XL", "path": "stablediffusionapi/animexl-xuebimix", "prefix": ""},
    {"name": "ArtiWaifu Diffusion", "path": "Eugeoter/artiwaifu-diffusion-1.0", "prefix": ""},
    {"name": "AutismMix DPO XL", "path": "femboysLover/autismmix-DPO-XL", "prefix": ""},
    {"name": "BitDiffusion XL", "path": "CortexLM/BitDiffusionXL-v0.1", "prefix": ""},
    {"name": "Cheyenne XL 1.6", "path": "GraydientPlatformAPI/cheyenne16-xl", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Colossus Project XL", "path": "n0madic/colossusProjectXL_v53", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "ColorfulXL", "path": "recoilme/colorfulxl", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "ColorfulXL v7", "path": "John6666/colorful-xl-v7-sdxl", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "ColorfulXL Lightning", "path": "recoilme/ColorfulXL-Lightning", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Copax Timeless 1.22", "path": "rubbrband/copaxTimelessxlSDXL1_v122", "prefix": ""},
    {"name": "Copax Timeless Turbo", "path": "GraydientPlatformAPI/copax-timelessturbo2", "prefix": ""},
    {"name": "Copax NSFW Pony", "path": "GraydientPlatformAPI/copax-nsfwpony-xl", "prefix": ""},
    {"name": "Counterfeit-XL", "path": "gsdf/CounterfeitXL", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "CrystalClear XL", "path": "stablediffusionapi/crystal-clear-xlv1", "prefix": ""},
    {"name": "DPO-Juggernaut 7XL", "path": "dataautogpt3/dpo-sdxl-merged", "prefix": "", "use_safetensors": True},
    {"name": "Dreamshaper-XL", "path": "Lykon/dreamshaper-xl-1-0", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Dreamshaper-XL v2 Turbo", "path": "Lykon/dreamshaper-xl-v2-turbo", "prefix": "", "variant": "fp16"},
    {"name": "Dreamshaper-XL Lightning", "path": "Lykon/dreamshaper-xl-lightning", "prefix": "", "variant": "fp16"},
    {"name": "Dreamviewer", "path": "Andyrasika/dreamviewer-sdxl-1.0", "prefix": ""},
    {"name": "Dusk Slime Mix", "path": "EarthnDusk/DuskSlimeMixUltraInifity-YamerXLfp16", "prefix": ""},
    {"name": "DynaVision-XL", "path": "nyxia/dynavision-xl", "prefix": ""},
    {"name": "E621 Rising 3", "path": "hearmeneigh/e621-rising-v3", "prefix": "rising_masterpiece", "use_safetensors": True},
    {"name": "EpicRealism XL v5 Ultimate", "path": "rubbrband/epicrealismXL_v5Ultimate", "prefix": "", "use_safetensors": True},
    {"name": "EveryJourney", "path": "thehive/everyjourney-sdxl-0.9-finetuned", "prefix": "", "use_safetensors": True},
    {"name": "FFusion FFXL400", "path": "FFusion/FFXL400", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Fluently XL v4", "path": "fluently/Fluently-XL-v4", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Ghost-XL", "path": "GraydientPlatformAPI/ghost-xl", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Hassaku-XL", "path": "femboysLover/Hassaku-fp16-XL", "prefix": "", "variant": "fp16"},
    {"name": "Hotshot SDXL-512", "path": "hotshotco/SDXL-512", "prefix": "", "use_safetensors": True},
    {"name": "JibMix Realistic XL", "path": "misri/jibMixRealisticXL_v60Backgrounds", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Juggernaut XL 5", "path": "stablediffusionapi/juggernaut-xl-v5", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Juggernaut XL 6", "path": "Jeroenvv1985/Juggernaut_v6", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Juggernaut XL 7", "path": "GHArt/Juggernaut_XL_V7vf_xl_fp16", "prefix": "", "use_safetensors": True},
    {"name": "Juggernaut XL 8", "path": "stablediffusionapi/juggernaut-xl-v8", "prefix": ""},
    {"name": "Juggernaut XL 9", "path": "RunDiffusion/Juggernaut-XL-v9", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Juggernaut XL 10", "path": "RunDiffusion/Juggernaut-X-v10", "prefix": ""},
    {"name": "Juggernaut XL Lightning", "path": "RunDiffusion/Juggernaut-XL-Lightning", "prefix": "", "use_safetensors": True},
    {"name": "Juggernaut XI 11", "path": "RunDiffusion/Juggernaut-XI-v11", "prefix": ""},
    {"name": "LEOSAMs-HelloWorld", "path": "imagepipeline/LEOSAMs-HelloWorld-SDXL-Base-Model", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Ludica-Playground", "path": "artificialguybr/Ludica-PlaygroundV2Finetuned", "prefix": "", "variant": "fp16", "use_safetensors": True},
    #{"name": "Midjourney-V4 XL", "path": "openskyml/midjourney-v4-xl", "prefix": "", "use_safetensors": True},
    {"name": "Mann-E Dreams Turbo", "path": "mann-e/Mann-E_Dreams", "prefix": ""},
    {"name": "NewReality XL", "path": "stablediffusionapi/newrealityxl-global-nsfw", "prefix": ""},
    {"name": "NSFW-Gen v2", "path": "UnfilteredAI/NSFW-gen-v2", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "NSFW-Gen Anime", "path": "UnfilteredAI/NSFW-GEN-ANIME", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "OpenDalle v1.1", "path": "dataautogpt3/OpenDalleV1.1", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "PhotoPedia XL", "path": "GHArt/PhotoPedia_XL_V4.5_xl_fp16", "prefix": "", "use_safetensors": True},
    {"name": "Playground v2", "path": "playgroundai/playground-v2-1024px-aesthetic", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "Playground v2.5", "path": "playgroundai/playground-v2.5-1024px-aesthetic", "prefix": "", "variant": "fp16"},
    {"name": "Poltergeist Mix", "path": "EnD-Diffusers/PoltergeistMix-SDXLfp16", "prefix": ""},
    {"name": "Pony Diffusion v6", "path": "kitty7779/ponyDiffusionV6XL", "prefix": ""},
    {"name": "Proteus v0.4", "path": "EasyBits/ProteusV0.4.fp16", "prefix": ""},
    {"name": "Proteus v0.4 Lightning", "path": "dataautogpt3/ProteusV0.4-Lightning", "prefix": ""},
    {"name": "ProtVision-XL 1", "path": "Andyrasika/Sdxl1.0-protvisionXL", "prefix": ""},
    {"name": "ProtVision-XL 3", "path": "stablediffusionapi/protovisionxl-v3", "prefix": ""},
    {"name": "RealCartoon-XL 4", "path": "frankjoshua/realcartoonXL_v4", "prefix": "", "variant": "fp16"},
    {"name": "Realism Engine 3 XL", "path": "GraydientPlatformAPI/realism-engine3-xl", "prefix": "", "use_safetensors": True},
    {"name": "RealVis-XL 2", "path": "SG161222/RealVisXL_V2.0", "prefix": "", "variant": "fp16"},
    {"name": "RealVis-XL 3", "path": "SG161222/RealVisXL_V3.0", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "RealVis-XL 4", "path": "SG161222/RealVisXL_V4.0", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "RealVis-XL 5", "path": "SG161222/RealVisXL_V5.0", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "RealVis-XL 5 Lighting", "path": "SG161222/RealVisXL_V5.0_Lightning", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "RunDiffusion-XL", "path": "RunDiffusion/RunDiffusion-XL-Beta", "prefix": "", "variant": "fp16", "use_safetensors": True},
    {"name": "SD-XL Inpainting 0.1", "path": "diffusers/stable-diffusion-xl-1.0-inpainting-0.1", "prefix": "", "variant": "fp16"},
    {"name": "SeaArt-Furry-XL", "path": "SeaArtLab/SeaArt-Furry-XL-1.0", "prefix": "", "use_safetensors": True},
    {"name": "Segmind SSD-1B", "path": "segmind/SSD-1B", "prefix": "", "variant": "fp16"},
    {"name": "Segmind SSD-1B Anime", "path": "furusu/SSD-1B-anime", "prefix": "", "variant": "fp16"},
    {"name": "Segmind Vega", "path": "segmind/Segmind-Vega", "prefix": "", "variant": "fp16"},
    {"name": "Starry-XL v5.2", "path": "eienmojiki/Starry-XL-v5.2", "prefix": "", "use_safetensors": True},
    {"name": "ThinkDiffusion-XL", "path": "ThinkDiffusion/ThinkDiffusionXL", "prefix": "", "variant": "fp16"},
    {"name": "Unstable-Diffusers", "path": "stablediffusionapi/sdxl-unstable-diffusers-y", "prefix": "", "variant": "fp16"},
    {"name": "Unstable Diffusers YamerMIX", "path": "Yamer-AI/SDXL_Unstable_Diffusers", "prefix": ""},
    {"name": "Unstable Diffusers YamerMIX v9", "path": "GHArt/Unstable_Diffusers_YamerMIX_V9_xl_fp16", "prefix": "", "variant": "fp16"},
    {"name": "YamerMIX v8", "path": "wangqixun/YamerMIX_v8", "prefix": ""},
]
SDXL_LoRA_models = [
    {"name": "3D Redmond", "path": "artificialguybr/3DRedmond-V1", "weights": "3DRedmond-3DRenderStyle-3DRenderAF.safetensors", "prefix": "3D Render Style, 3DRenderAF"}, 
    {"name": "ByteDance Hyper-SDXL 8steps", "path": "ByteDance/Hyper-SD", "weights": "Hyper-SDXL-8steps-lora.safetensors", "prefix": ""}, 
    {"name": "Pixel Art XL", "path": "nerijs/pixel-art-xl", "weights": "pixel-art-xl.safetensors", "prefix": "pixel art"}, 
    {"name": "Crayon Style", "path": "ostris/crayon_style_lora_sdxl", "weights": "crayons_v1_sdxl.safetensors", "prefix": ""}, 
    {"name": "Papercut SDXL", "path": "TheLastBen/Papercut_SDXL", "weights": "papercut.safetensors", "prefix": "papercut"}, 
    {"name": "Aether Ghost", "path": "joachimsallstrom/aether-ghost-lora-for-sdxl", "weights": "Aether_Ghost_v1.1_LoRA.safetensors", "prefix": "transparent ghost"}, 
    {"name": "Aether Bubbles & Foam", "path": "joachimsallstrom/aether-bubbles-foam-lora-for-sdxl", "weights": "Aether_Bubbles_And_Foam_v1_SDXL_LoRA.safetensors", "prefix": "made of bath foam and soap bubbles,"},
    {"name": "Aether Ghost", "path": "joachimsallstrom/aether-ghost-lora-for-sdxl", "weights": "Aether_Ghost_v1.1_LoRA.safetensors", "prefix": "transparent ghost"},
    {"name": "DALL•E 3 XL", "path": "openskyml/dalle-3-xl", "weights": "Dall-e_3_0.3-v2.safetensors", "prefix": ""}, 
    {"name": "Harrlogos text logo", "path": "HarroweD/HarrlogosXL", "weights": "Harrlogos_v2.0.safetensors", "prefix": ""}, 
    {"name": "InkPunk-XL", "path": "openskyml/inkpunk-diffusion-xl", "weights": "IPXL_v8.safetensors", "prefix": ""}, 
    {"name": "Lego Minifig XL", "path": "nerijs/lego-minifig-xl", "weights": "legominifig-v1.0-000003.safetensors", "prefix": "lego minifig"},
    {"name": "Midjourney-V4 XL", "path": "openskyml/midjourney-v4-xl", "weights": "Midjourney.safetensors", "prefix": ""},
    {"name": "Vulcan SDXL", "path": "davizca87/vulcan", "weights": "v5lcnXL-000004.safetensors", "prefix": "v5lcn"}, 
    {"name": "Embroidery Style", "path": "ostris/embroidery_style_lora_sdxl", "weights": "embroidered_style_v1_sdxl.safetensors", "prefix": ""}, 
    {"name": "3D Render Style", "path": "goofyai/3d_render_style_xl", "weights": "3d_render_style_xl.safetensors", "prefix": "3d style"}, 
    {"name": "Watercolor Style", "path": "ostris/watercolor_style_lora_sdxl", "weights": "watercolor_v1_sdxl.safetensors", "prefix": ""}, 
    {"name": "PS1 Graphics SDXL", "path": "veryVANYA/ps1-graphics-sdxl", "weights": "ps1_style_SDXL_v1.safetensors", "prefix": "ps1 style"}, 
    {"name": "William Eggleston Style", "path": "TheLastBen/William_Eggleston_Style_SDXL", "weights": "wegg.safetensors", "prefix": "by william eggleston"},
    {"name": "CAG Coinmaker", "path": "davizca87/c-a-g-coinmaker", "weights": "c01n-000010.safetensors", "prefix": "c01n"},
    {"name": "Cyborg Style", "path": "goofyai/cyborg_style_xl", "weights": "cyborg_style_xl-off.safetensors", "prefix": "cyborg style"},
    {"name": "Toy.Redmond", "path": "artificialguybr/ToyRedmond-ToyLoraForSDXL10", "weights": "ToyRedmond-FnkRedmAF.safetensors", "prefix": "FnkRedmAF"},
    {"name": "Transformers Style XL", "path": "AlanB/TransformersStyleXL", "weights": "TransformersStyleXL.safetensors", "prefix": "TransformersStyle"},
    {"name": "Voxel XL", "path": "Fictiverse/Voxel_XL_Lora", "weights": "VoxelXL_v1.safetensors", "prefix": "voxel style"},
    {"name": "Lego BrickHeadz", "path": "nerijs/lego-brickheadz-xl", "weights": "legobrickheadz-v1.0-000004.safetensors", "prefix": "lego brickheadz"},
    {"name": "Cinematic-2", "path": "jbilcke-hf/sdxl-cinematic-2", "weights": "pytorch_lora_weights.safetensors", "prefix": "cinematic-2"},
    {"name": "ClaymationX", "path": "Norod78/claymationx-sdxl-lora", "weights": "SDXL-ClaymationX-Lora-000002.safetensors", "prefix": "ClaymationX"},
    {"name": "Dripped Out", "path": "nerijs/dripped-out-xl", "weights": "drippedout-v1-000003.safetensors", "prefix": "dripped out"},
    {"name": "JoJo's Bizarre style", "path": "Norod78/SDXL-jojoso_style-Lora", "weights": "SDXL-jojoso_style-Lora-r8.safetensors", "prefix": "jojoso style"},
    {"name": "Pikachu XL", "path": "TheLastBen/Pikachu_SDXL", "weights": "pikachu.safetensors", "prefix": "pikachu"},
    {"name": "SDXL Lightning 8-step", "path": "ByteDance/SDXL-Lightning", "weights": "sdxl_lightning_8step_lora.safetensors", "prefix": ""},
    {"name": "2000s Indie Art", "path": "ntc-ai/SDXL-LoRA-slider.2000s-indie-art-style", "weights": "2000s%20indie%20art%20style.safetensors", "prefix": "2000s indie art style"},
    {"name": "2000s Indie Comic", "path": "ntc-ai/SDXL-LoRA-slider.2000s-indie-comic-art-style", "weights": "2000s%20indie%20comic%20art%20style.safetensors", "prefix": "2000s indie comic art style"},
    {"name": "3D Animated Movie", "path": "ntc-ai/SDXL-LoRA-slider.3d-animated-movie-still", "weights": "3d%20animated%20movie%20still.safetensors", "prefix": "3d animated movie still"},
    {"name": "90S Anime", "path": "ntc-ai/SDXL-LoRA-slider.90s-anime", "weights": "90s%20anime.safetensors", "prefix": "90s anime"},
    {"name": "Action Hero", "path": "ntc-ai/SDXL-LoRA-slider.action-hero", "weights": "action%20hero.safetensors", "prefix": "action hero"},
    {"name": "Action Shot", "path": "ntc-ai/SDXL-LoRA-slider.action-shot", "weights": "action%20shot.safetensors", "prefix": "action shot"},
    {"name": "Admiration", "path": "ntc-ai/SDXL-LoRA-slider.admiration", "weights": "admiration.safetensors", "prefix": "admiration"},
    {"name": "American Indian", "path": "ntc-ai/SDXL-LoRA-slider.american-indian", "weights": "american%20indian.safetensors", "prefix": "american indian"},
    {"name": "Angelic", "path": "ntc-ai/SDXL-LoRA-slider.angelic", "weights": "angelic.safetensors", "prefix": "angelic"},
    {"name": "Anime", "path": "ntc-ai/SDXL-LoRA-slider.anime", "weights": "anime.safetensors", "prefix": "anime"},
    {"name": "Asian", "path": "ntc-ai/SDXL-LoRA-slider.asian", "weights": "asian.safetensors", "prefix": "asian"},
    {"name": "Asleep", "path": "ntc-ai/SDXL-LoRA-slider.asleep", "weights": "asleep.safetensors", "prefix": "asleep"},
    {"name": "Award Winning Film", "path": "ntc-ai/SDXL-LoRA-slider.award-winning-film", "weights": "award%20winning%20film.safetensors", "prefix": "award winning film"},
    {"name": "Blacklight Photography", "path": "ntc-ai/SDXL-LoRA-slider.blacklight-photography", "weights": "blacklight%20photography.safetensors", "prefix": "blacklight photography"},
    {"name": "Captivating Eyes", "path": "ntc-ai/SDXL-LoRA-slider.captivating-eyes", "weights": "captivating%20eyes.safetensors", "prefix": "captivating eyes"},
    {"name": "Cartoon", "path": "ntc-ai/SDXL-LoRA-slider.cartoon", "weights": "cartoon.safetensors", "prefix": "cartoon"},
    {"name": "Casting A Spell", "path": "ntc-ai/SDXL-LoRA-slider.casting-a-spell", "weights": "casting%20a%20spell.safetensors", "prefix": "casting a spell"},
    {"name": "Celestial", "path": "ntc-ai/SDXL-LoRA-slider.celestial", "weights": "celestial.safetensors", "prefix": "celestial"},
    {"name": "Charming", "path": "ntc-ai/SDXL-LoRA-slider.charming", "weights": "charming.safetensors", "prefix": "charming"},
    {"name": "Chiaroscuro", "path": "ntc-ai/SDXL-LoRA-slider.Chiaroscuro", "weights": "Chiaroscuro.safetensors", "prefix": "Chiaroscuro"},
    {"name": "Cinematic Lighting", "path": "ntc-ai/SDXL-LoRA-slider.cinematic-lighting", "weights": "cinematic%20lighting.safetensors", "prefix": "cinematic lighting"},
    {"name": "Claws", "path": "ntc-ai/SDXL-LoRA-slider.claws", "weights": "claws.safetensors", "prefix": "claws"},
    {"name": "Clown", "path": "ntc-ai/SDXL-LoRA-slider.clown", "weights": "clown.safetensors", "prefix": "clown"},
    {"name": "Complex", "path": "ntc-ai/SDXL-LoRA-slider.complex", "weights": "complex.safetensors", "prefix": "complex"},
    {"name": "Cosplay Outfit", "path": "ntc-ai/SDXL-LoRA-slider.cosplay-outfit", "weights": "cosplay%20outfit.safetensors", "prefix": "cosplay outfit"},
    {"name": "Courage", "path": "ntc-ai/SDXL-LoRA-slider.courage", "weights": "courage.safetensors", "prefix": "courage"},
    {"name": "Creativity", "path": "ntc-ai/SDXL-LoRA-slider.creativity", "weights": "creativity.safetensors", "prefix": "creativity"},
    {"name": "Crystal Ball", "path": "ntc-ai/SDXL-LoRA-slider.Crystal-Ball-Photography", "weights": "Crystal%20Ball%20Photography.safetensors", "prefix": "Crystal Ball Photography"},
    {"name": "Curly Hair", "path": "ntc-ai/SDXL-LoRA-slider.curly-hair", "weights": "curly%20hair.safetensors", "prefix": "curly hair"},
    {"name": "Dancing", "path": "ntc-ai/SDXL-LoRA-slider.dancing", "weights": "dancing.safetensors", "prefix": "dancing"},
    {"name": "Dancing with Joy", "path": "ntc-ai/SDXL-LoRA-slider.dancing-with-joy", "weights": "dancing%20with%20joy.safetensors", "prefix": "dancing with joy"},
    {"name": "Dark-Skinned", "path": "ntc-ai/SDXL-LoRA-slider.dark-skinned", "weights": "dark-skinned.safetensors", "prefix": "dark-skinned"},
    {"name": "Deep Sleep", "path": "ntc-ai/SDXL-LoRA-slider.deep-sleep", "weights": "deep%20sleep.safetensors", "prefix": "deep sleep"},
    {"name": "Demon", "path": "ntc-ai/SDXL-LoRA-slider.demon", "weights": "demon.safetensors", "prefix": "demon"},
    {"name": "Dreadlocks", "path": "ntc-ai/SDXL-LoRA-slider.dreadlocks", "weights": "dreadlocks.safetensors", "prefix": "dreadlocks"},
    {"name": "Dreamscape", "path": "ntc-ai/SDXL-LoRA-slider.dreamscape", "weights": "dreamscape.safetensors", "prefix": "dreamscape"},
    {"name": "Drunk", "path": "ntc-ai/SDXL-LoRA-slider.drunk", "weights": "drunk.safetensors", "prefix": "drunk"},
    {"name": "Dynamic Anatomy", "path": "ntc-ai/SDXL-LoRA-slider.dynamic-anatomy", "weights": "dynamic%20anatomy.safetensors", "prefix": "dynamic anatomy"},
    {"name": "Eating Spaghetti", "path": "ntc-ai/SDXL-LoRA-slider.eating-spaghetti", "weights": "eating%20spaghetti.safetensors", "prefix": "eating spaghetti"},
    {"name": "Elf", "path": "ntc-ai/SDXL-LoRA-slider.elf", "weights": "elf.safetensors", "prefix": "elf"},
    {"name": "Emoji", "path": "ntc-ai/SDXL-LoRA-slider.emoji", "weights": "emoji.safetensors", "prefix": "emoji"},
    {"name": "Envy Zoom Slider", "path": "e-n-v-y/envy-zoom-slider-xl-01", "weights": "EnvyZoomSliderXL01.safetensors"},
    {"name": "Epic Oil Painting", "path": "ntc-ai/SDXL-LoRA-slider.epic-oil-painting", "weights": "epic%20oil%20painting.safetensors", "prefix": "epic oil painting"},
    {"name": "Evil Santa", "path": "ntc-ai/SDXL-LoRA-slider.evil-santa", "weights": "evil%20santa.safetensors", "prefix": "evil santa"},
    {"name": "Excited", "path": "ntc-ai/SDXL-LoRA-slider.excited", "weights": "excited.safetensors", "prefix": "excited"},
    {"name": "Expensive", "path": "ntc-ai/SDXL-LoRA-slider.expensive", "weights": "expensive.safetensors", "prefix": "expensive"},
    {"name": "Extreme Sports", "path": "ntc-ai/SDXL-LoRA-slider.extreme-sports", "weights": "extreme%20sports.safetensors", "prefix": "extreme sports"},
    {"name": "Extremely Aesthetic", "path": "ntc-ai/SDXL-LoRA-slider.extremely-extremely-aesthetic", "weights": "extremely%20extremely%20aesthetic.safetensors", "prefix": "extremely extremely aesthetic"},
    {"name": "Extremely Cozy", "path": "ntc-ai/SDXL-LoRA-slider.extremely-cozy", "weights": "extremely%20cozy.safetensors", "prefix": "extremely cozy"},
    {"name": "Extremely Detailed", "path": "ntc-ai/SDXL-LoRA-slider.extremely-detailed", "weights": "extremely%20detailed.safetensors", "prefix": "extremely detailed"},
    {"name": "Eye-Catching", "path": "ntc-ai/SDXL-LoRA-slider.eye-catching", "weights": "eye-catching.safetensors", "prefix": "eye-catching"},
    {"name": "Face Tattoo", "path": "ntc-ai/SDXL-LoRA-slider.face-tattoo", "weights": "face%20tattoo.safetensors", "prefix": "face tattoo"},
    {"name": "Fancy", "path": "ntc-ai/SDXL-LoRA-slider.fancy", "weights": "fancy.safetensors", "prefix": "fancy"},
    {"name": "Ferocious Dragon", "path": "ntc-ai/SDXL-LoRA-slider.ferocious-dragon", "weights": "ferocious%20dragon.safetensors", "prefix": "ferocious dragon"},
    {"name": "Figurine", "path": "ntc-ai/SDXL-LoRA-slider.figurine", "weights": "figurine.safetensors", "prefix": "figurine"},
    {"name": "Fire Elemental", "path": "ntc-ai/SDXL-LoRA-slider.fire-elemental", "weights": "fire%20elemental.safetensors", "prefix": "fire elemental"},
    {"name": "Fit", "path": "ntc-ai/SDXL-LoRA-slider.fit", "weights": "fit.safetensors", "prefix": "fit"},
    {"name": "Friendly Smile", "path": "ntc-ai/SDXL-LoRA-slider.friendly-smile", "weights": "friendly%20smile.safetensors", "prefix": "friendly smile"},
    {"name": "Gingerbread House", "path": "ntc-ai/SDXL-LoRA-slider.gingerbread-house", "weights": "gingerbread%20house.safetensors", "prefix": "gingerbread house"},
    {"name": "Glamour Shot", "path": "ntc-ai/SDXL-LoRA-slider.glamour-shot", "weights": "glamour%20shot.safetensors", "prefix": "glamourshot"},
    {"name": "Gritty Reality", "path": "ntc-ai/SDXL-LoRA-slider.gritty-reality", "weights": "gritty%20reality.safetensors", "prefix": "gritty reality"},
    {"name": "Headshot", "path": "ntc-ai/SDXL-LoRA-slider.headshot", "weights": "headshot.safetensors", "prefix": "headshot"},
    {"name": "Heavy Inking", "path": "ntc-ai/SDXL-LoRA-slider.heavy-inking", "weights": "heavy%20inking.safetensors", "prefix": "heavy inking"},
    {"name": "High Dynamic Range", "path": "ntc-ai/SDXL-LoRA-slider.HDR-high-dynamic-range", "weights": "HDR%2C%20high%20dynamic%20range.safetensors", "prefix": "HDR, high dynamic range"},
    {"name": "Hobbit", "path": "ntc-ai/SDXL-LoRA-slider.hobbit", "weights": "hobbit.safetensors", "prefix": "hobbit"},
    {"name": "Holiday Festivus", "path": "ntc-ai/SDXL-LoRA-slider.holiday-festivus", "weights": "holiday%20festivus.safetensors", "prefix": "holiday festivus"},
    {"name": "Hoodie", "path": "ntc-ai/SDXL-LoRA-slider.hoodie", "weights": "hoodie.safetensors", "prefix": "hoodie"},
    {"name": "Hot", "path": "ntc-ai/SDXL-LoRA-slider.hot", "weights": "hot.safetensors", "prefix": "hot"},
    {"name": "Huge Anime Eyes", "path": "ntc-ai/SDXL-LoRA-slider.huge-anime-eyes", "weights": "huge%20anime%20eyes.safetensors", "prefix": "huge anime eyes"},
    {"name": "Impressed", "path": "ntc-ai/SDXL-LoRA-slider.impressed", "weights": "impressed.safetensors", "prefix": "impressed"},
    {"name": "In Deep Meditation", "path": "ntc-ai/SDXL-LoRA-slider.in-deep-meditation", "weights": "in%20deep%20meditation.safetensors", "prefix": "in deep meditation"},
    {"name": "In Love", "path": "ntc-ai/SDXL-LoRA-slider.in-love", "weights": "in%20love.safetensors", "prefix": "in love"},
    {"name": "In an Airplane", "path": "ntc-ai/SDXL-LoRA-slider.in-an-airplane", "weights": "in%20an%20airplane.safetensors", "prefix": "in an airplane"},
    {"name": "Intense", "path": "ntc-ai/SDXL-LoRA-slider.intense", "weights": "intense.safetensors", "prefix": "intense"},
    {"name": "Intimidating", "path": "ntc-ai/SDXL-LoRA-slider.intimidating", "weights": "intimidating.safetensors", "prefix": "intimidating"},
    {"name": "Intricate", "path": "ntc-ai/SDXL-LoRA-slider.intricate", "weights": "intricate.safetensors", "prefix": "intricate"},
    {"name": "Isometric View", "path": "ntc-ai/SDXL-LoRA-slider.isometric-view", "weights": "isometric%20view.safetensors", "prefix": "isometric view"},
    {"name": "Joy", "path": "ntc-ai/SDXL-LoRA-slider.joy", "weights": "joy.safetensors", "prefix": "joy"},
    {"name": "Laser Background", "path": "ntc-ai/SDXL-LoRA-slider.laser-background", "weights": "laser%20background.safetensors", "prefix": "laser background"},
    {"name": "Latin", "path": "ntc-ai/SDXL-LoRA-slider.latin", "weights": "latin.safetensors", "prefix": "latin"},
    {"name": "Lens Flare", "path": "ntc-ai/SDXL-LoRA-slider.lens-flare", "weights": "lens%20flare.safetensors", "prefix": "lens flare"},
    {"name": "Lizardperson", "path": "ntc-ai/SDXL-LoRA-slider.lizardperson", "weights": "lizardperson.safetensors", "prefix": "lizardperson"},
    {"name": "Long Exposure", "path": "ntc-ai/SDXL-LoRA-slider.long-exposure-photography", "weights": "long%20exposure%20photography.safetensors", "prefix": "long exposure photography"},
    {"name": "Looking Contemplative", "path": "ntc-ai/SDXL-LoRA-slider.looking-contemplative", "weights": "looking%20contemplative.safetensors", "prefix": "looking contemplative"},
    {"name": "Looking at Viewer", "path": "ntc-ai/SDXL-LoRA-slider.looking-at-viewer", "weights": "looking%20at%20viewer.safetensors", "prefix": "looking at viewer"},
    {"name": "Luminescent", "path": "ntc-ai/SDXL-LoRA-slider.luminescent", "weights": "luminescent.safetensors", "prefix": "luminescent"},
    {"name": "Macro Close-up Shot", "path": "ntc-ai/SDXL-LoRA-slider.macro-close-up-shot", "weights": "macro%20close-up%20shot.safetensors", "prefix": "macro close-up shot"},
    {"name": "Mad with Power", "path": "ntc-ai/SDXL-LoRA-slider.mad-with-power", "weights": "mad%20with%20power.safetensors", "prefix": "mad with power"},
    {"name": "Made of Clouds", "path": "ntc-ai/SDXL-LoRA-slider.made-of-clouds", "weights": "made%20of%20clouds.safetensors", "prefix": "made of clouds"},
    {"name": "Magical Enchanted", "path": "ntc-ai/SDXL-LoRA-slider.magicalenchanted", "weights": "magical%2Cenchanted.safetensors", "prefix": "magical,enchanted"},
    {"name": "Magical Energy", "path": "ntc-ai/SDXL-LoRA-slider.magical-energy-swirling-around", "weights": "magical%20energy%20swirling%20around.safetensors", "prefix": "magical energy swirling around"},
    {"name": "Makeup", "path": "ntc-ai/SDXL-LoRA-slider.makeup", "weights": "makeup.safetensors", "prefix": "makeup"},
    {"name": "Masterpiece", "path": "ntc-ai/SDXL-LoRA-slider.masterpiece", "weights": "masterpiece.safetensors", "prefix": "masterpiece"},
    {"name": "Mathematics", "path": "ntc-ai/SDXL-LoRA-slider.mathematics", "weights": "mathematics.safetensors", "prefix": "mathematics"},
    {"name": "Messy Hair", "path": "ntc-ai/SDXL-LoRA-slider.messy-hair", "weights": "messy%20hair.safetensors", "prefix": "messy hair"},
    {"name": "Mid-Dance Move", "path": "ntc-ai/SDXL-LoRA-slider.mid-dance-move", "weights": "mid-dance%20move.safetensors", "prefix": "mid-dance move"},
    {"name": "Mohawk", "path": "ntc-ai/SDXL-LoRA-slider.mohawk", "weights": "mohawk.safetensors", "prefix": "mohawk"},
    {"name": "Motion Blur", "path": "ntc-ai/SDXL-LoRA-slider.motion-blur", "weights": "motion%20blur.safetensors", "prefix": "motion blur"},
    {"name": "Nice Hands", "path": "ntc-ai/SDXL-LoRA-slider.nice-hands", "weights": "nice%20hands.safetensors", "prefix": "nice hands"},
    {"name": "Nightmare Before Xmas", "path": "ntc-ai/SDXL-LoRA-slider.nightmare-before-christmas", "weights": "nightmare%20before%20christmas.safetensors", "prefix": "nightmare before christmas"},
    {"name": "Ninja Turtle", "path": "ntc-ai/SDXL-LoRA-slider.ninja-turtle", "weights": "ninja%20turtle.safetensors", "prefix": "ninja turtle"},
    {"name": "Oil Painting", "path": "ntc-ai/SDXL-LoRA-slider.oil-painting", "weights": "oil%20painting.safetensors", "prefix": "oil painting"},
    {"name": "Old Cigarette Ad", "path": "ntc-ai/SDXL-LoRA-slider.old-cigarette-ad", "weights": "old%20cigarette%20ad.safetensors", "prefix": "old cigarette ad"},
    {"name": "On Stage", "path": "ntc-ai/SDXL-LoRA-slider.on-stage", "weights": "on%20stage.safetensors", "prefix": "on stage"},
    {"name": "On The Bus", "path": "ntc-ai/SDXL-LoRA-slider.on-the-bus", "weights": "on%20the%20bus.safetensors", "prefix": "on the bus"},
    {"name": "Orc", "path": "ntc-ai/SDXL-LoRA-slider.orc", "weights": "orc.safetensors", "prefix": "orc"},
    {"name": "Perfect", "path": "ntc-ai/SDXL-LoRA-slider.perfect", "weights": "perfect.safetensors", "prefix": "perfect"},
    {"name": "Pincushion Distortion", "path": "ntc-ai/SDXL-LoRA-slider.sacred-geometry", "weights": "pincushion%20distortion.safetensors", "prefix": "pincushion distortion"},
    {"name": "Pinhead", "path": "ntc-ai/SDXL-LoRA-slider.pinhead", "weights": "pinhead.safetensors", "prefix": "pinhead"},
    {"name": "Pirate", "path": "ntc-ai/SDXL-LoRA-slider.pirate", "weights": "pirate.safetensors", "prefix": "pirate"},
    {"name": "Pixar-Style", "path": "ntc-ai/SDXL-LoRA-slider.pixar-style", "weights": "pixar-style.safetensors", "prefix": "pixar-style"},
    {"name": "Pixel Art", "path": "ntc-ai/SDXL-LoRA-slider.pixel-art", "weights": "pixel%20art.safetensors", "prefix": "pixel art"},
    {"name": "Plastic", "path": "ntc-ai/SDXL-LoRA-slider.plastic", "weights": "plastic.safetensors", "prefix": "plastic"},
    {"name": "Playing Instrument", "path": "ntc-ai/SDXL-LoRA-slider.playing-a-musical-instrument", "weights": "playing%20a%20musical%20instrument.safetensors", "prefix": "playing a musical instrument"},
    {"name": "Product Photo", "path": "ntc-ai/SDXL-LoRA-slider.Product-Photo", "weights": "Product%20Photo.safetensors", "prefix": "Product Photo"},
    {"name": "Ps1 Graphics", "path": "ntc-ai/SDXL-LoRA-slider.ps1-graphics", "weights": "ps1%20graphics.safetensors", "prefix": "ps1 graphics"},
    {"name": "Psychedelic Trip", "path": "ntc-ai/SDXL-LoRA-slider.psychedelic-trip", "weights": "psychedelic%20trip.safetensors", "prefix": "psychedelic trip"},
    {"name": "Raw", "path": "ntc-ai/SDXL-LoRA-slider.raw", "weights": "raw.safetensors", "prefix": "raw"},
    {"name": "Retro Horror Comic", "path": "ntc-ai/SDXL-LoRA-slider.retro-horror-comic-style-poster", "weights": "retro%20horror%20comic%20style%20poster.safetensors", "prefix": "retro horror comic style poster"},
    {"name": "Rich", "path": "ntc-ai/SDXL-LoRA-slider.rich", "weights": "rich.safetensors", "prefix": "rich"},
    {"name": "RoboDiffusion XL", "path": "Fiacre/robodiffusion-xl-v1", "weights": "robodiffusionxl.safetensors"},
    {"name": "Sacred Geometry", "path": "ntc-ai/SDXL-LoRA-slider.sacred-geometry", "weights": "sacred%20geometry.safetensors", "prefix": "sacred geometry"},
    {"name": "Santa", "path": "ntc-ai/SDXL-LoRA-slider.santa", "weights": "santa.safetensors", "prefix": "santa"},
    {"name": "Scared", "path": "ntc-ai/SDXL-LoRA-slider.scared", "weights": "scared.safetensors", "prefix": "scared"},
    {"name": "Serenity Film", "path": "ntc-ai/SDXL-LoRA-slider.serenity-film-still", "weights": "serenity%20film%20still.safetensors", "prefix": "serenity film still"},
    {"name": "Sexy", "path": "ntc-ai/SDXL-LoRA-slider.sexy", "weights": "sexy.safetensors", "prefix": "sexy"},
    {"name": "Shadows", "path": "ntc-ai/SDXL-LoRA-slider.shadows", "weights": "shadows.safetensors", "prefix": "shadows"},
    {"name": "Shady", "path": "ntc-ai/SDXL-LoRA-slider.shady", "weights": "shady.safetensors", "prefix": "shady"},
    {"name": "Short Curly Red Hair", "path": "ntc-ai/SDXL-LoRA-slider.short-curly-red-hair", "weights": "short%20curly%20red%20hair.safetensors", "prefix": "short curly red hair"},
    {"name": "Silhouette", "path": "ntc-ai/SDXL-LoRA-slider.silhouette", "weights": "silhouette.safetensors", "prefix": "silhouette"},
    {"name": "Sitcom Star", "path": "ntc-ai/SDXL-LoRA-slider.sitcom-star", "weights": "sitcom%20star.safetensors", "prefix": "sitcom star"},
    {"name": "Skeleton", "path": "ntc-ai/SDXL-LoRA-slider.skeleton", "weights": "skeleton.safetensors", "prefix": "skeleton"},
    {"name": "Slice of Life", "path": "ntc-ai/SDXL-LoRA-slider.slice-of-life", "weights": "slice%20of%20life.safetensors", "prefix": "slice of life"},
    {"name": "Smart Intelligent", "path": "ntc-ai/SDXL-LoRA-slider.smartintelligent", "weights": "smart%2Cintelligent.safetensors", "prefix": "smart,intelligent"},
    {"name": "Smoking a Cigarette", "path": "ntc-ai/SDXL-LoRA-slider.smoking-a-cigarette-looking-cool", "weights": "smoking%20a%20cigarette%20looking%20cool.safetensors", "prefix": "smoking a cigarette looking cool"},
    {"name": "Smooth and Shiny", "path": "ntc-ai/SDXL-LoRA-slider.smooth-and-shiny", "weights": "smooth%20and%20shiny.safetensors", "prefix": "smooth and shiny"},
    {"name": "Snow-Covered", "path": "ntc-ai/SDXL-LoRA-slider.snowingsnow-covered", "weights": "snowing%2Csnow-covered.safetensors", "prefix": "snowing,snow-covered"},
    {"name": "Snowman", "path": "ntc-ai/SDXL-LoRA-slider.snowman", "weights": "snowman.safetensors", "prefix": "snowman"},
    {"name": "Soulful", "path": "ntc-ai/SDXL-LoRA-slider.soulful", "weights": "soulful.safetensors", "prefix": "soulful"},
    {"name": "Spooky Ghosts", "path": "ntc-ai/SDXL-LoRA-slider.spooky-ghosts", "weights": "spooky%20ghosts.safetensors", "prefix": "spooky ghosts"},
    {"name": "Studio Ghibli", "path": "ntc-ai/SDXL-LoRA-slider.Studio-Ghibli-style", "weights": "Studio%20Ghibli%20style.safetensors", "prefix": "Studio Ghibli style"},
    {"name": "Studio Lighting", "path": "ntc-ai/SDXL-LoRA-slider.studio-lighting", "weights": "studio%20lighting.safetensors", "prefix": "StdGBRedmAF, Studio Ghibli"},
    {"name": "Superhero", "path": "ntc-ai/SDXL-LoRA-slider.superhero", "weights": "superhero.safetensors", "prefix": "superhero"},
    {"name": "Surprised", "path": "ntc-ai/SDXL-LoRA-slider.surprised", "weights": "surprised.safetensors", "prefix": "surprised"},
    {"name": "Symmetrical", "path": "ntc-ai/SDXL-LoRA-slider.symmetrical", "weights": "symmetrical.safetensors", "prefix": "symmetrical"},
    {"name": "The Starry Night", "path": "ntc-ai/SDXL-LoRA-slider.the-starry-night", "weights": "the%20starry%20night.safetensors", "prefix": "the starry night"},
    {"name": "Toon", "path": "ntc-ai/SDXL-LoRA-slider.toon", "weights": "toon.safetensors", "prefix": "toon"},
    {"name": "Treant", "path": "ntc-ai/SDXL-LoRA-slider.treant", "weights": "treant.safetensors", "prefix": "treant"},
    {"name": "Trending On Artstation", "path": "ntc-ai/SDXL-LoRA-slider.trending-on-artstation", "weights": "trending%20on%20artstation.safetensors", "prefix": "trending on artstation"},
    {"name": "Trollface", "path": "ntc-ai/SDXL-LoRA-slider.trollface", "weights": "trollface.safetensors", "prefix": "trollface"},
    {"name": "Ultra Realistic", "path": "ntc-ai/SDXL-LoRA-slider.ultra-realistic-illustration", "weights": "ultra%20realistic%20illustration.safetensors", "prefix": "ultra realistic illustration"},
    {"name": "Underwater", "path": "ntc-ai/SDXL-LoRA-slider.underwater", "weights": "underwater.safetensors", "prefix": "underwater"},
    {"name": "Unexpected", "path": "ntc-ai/SDXL-LoRA-slider.unexpected", "weights": "unexpected.safetensors", "prefix": "unexpected"},
    {"name": "Unreal-Engine", "path": "ntc-ai/SDXL-LoRA-slider.unreal-engine", "weights": "unreal%20engine.safetensors", "prefix": "unreal engine"},
    {"name": "Upside Down Person", "path": "ntc-ai/SDXL-LoRA-slider.upside-down-person", "weights": "upside%20down%20person.safetensors", "prefix": "upside down person"},
    {"name": "Vampire", "path": "ntc-ai/SDXL-LoRA-slider.vampire", "weights": "vampire.safetensors", "prefix": "vampire"},
    {"name": "Very Aesthetic", "path": "ntc-ai/SDXL-LoRA-slider.very-aesthetic", "weights": "very%20aesthetic.safetensors", "prefix": "very aesthetic"},
    {"name": "Warrior", "path": "ntc-ai/SDXL-LoRA-slider.warrior", "weights": "warrior.safetensors", "prefix": "warrior"},
    {"name": "Water Elemental", "path": "ntc-ai/SDXL-LoRA-slider.water-elemental", "weights": "water%20elemental.safetensors", "prefix": "water elemental"},
    {"name": "Wedding Photo", "path": "ntc-ai/SDXL-LoRA-slider.wedding-photo", "weights": "wedding%20photo.safetensors", "prefix": "wedding photo"},
    {"name": "Whos in Whoville", "path": "ntc-ai/SDXL-LoRA-slider.whos-in-whoville", "weights": "whos%20in%20whoville.safetensors", "prefix": "whos in whoville"},
    {"name": "Wildlife", "path": "ntc-ai/SDXL-LoRA-slider.wildlife", "weights": "wildlife.safetensors", "prefix": "wildlife"},
    {"name": "Winner", "path": "ntc-ai/SDXL-LoRA-slider.winner", "weights": "winner.safetensors", "prefix": "winner"},
    {"name": "Analog.Redmond V2", "path": "artificialguybr/analogredmond-v2", "weights": "AnalogRedmondV2-Analog-AnalogRedmAF.safetensors", "prefix": "AnalogRedmAF"},
    {"name": "Logo.Redmond V2", "path": "artificialguybr/LogoRedmond-LogoLoraForSDXL-V2", "weights": "LogoRedmondV2-Logo-LogoRedmAF.safetensors", "prefix": "LogoRedAF"},
    {"name": "LinearManga.Redmond", "path": "artificialguybr/LineAniRedmond-LinearMangaSDXL", "weights": "LineAniRedmond-LineAniAF.safetensors", "prefix": "LineAniAF"},
    {"name": "Josef Koudelka Style", "path": "TheLastBen/Josef_Koudelka_Style_SDXL", "weights": "koud.safetensors", "prefix": "by josef koudelka"},
    {"name": "Joker", "path": "jbilcke-hf/sdxl-joker", "weights": "pytorch_lora_weights.safetensors", "prefix": "jokerstyle"},
    {"name": "Leonardo Ai Style", "path": "goofyai/Leonardo_Ai_Style_Illustration", "weights": "leonardo_illustration.safetensors", "prefix": "leonardo style"},
    {"name": "SimpStyle", "path": "Norod78/SDXL-simpstyle-Lora", "weights": "SDXL-simpstyle-Lora-r8.safetensors", "prefix": "simpstyle"},
    {"name": "StickerSheet", "path": "Norod78/SDXL-StickerSheet-Lora", "weights": "SDXL-StickerSheet-Lora.safetensors", "prefix": "StickerSheet"},
    {"name": "Stickers.Redmond", "path": "artificialguybr/StickersRedmond", "weights": "StickersRedmond.safetensors", "prefix": "Stickers"},
    {"name": "Storybook.Redmond", "path": "artificialguybr/StoryBookRedmond", "weights": "StoryBookRedmond-KidsRedmAF.safetensors", "prefix": "KidsRedmAF"},
    {"name": "StudioGhibli.Redmond", "path": "artificialguybr/StudioGhibli.Redmond-V2", "weights": "StudioGhibli.Redmond-StdGBRRedmAF-StudioGhibli.safetensors", "prefix": "StdGBRedmAF, Studio Ghibli"},
    {"name": "TshirtDesign.Redmond", "path": "artificialguybr/TshirtDesignRedmond-V2", "weights": "TShirtDesignRedmondV2-Tshirtdesign-TshirtDesignAF.safetensors", "prefix": "TshirtDesignAF"},
    {"name": "Clay Animation.Redmond", "path": "artificialguybr/ClayAnimationRedmond", "weights": "ClayAnimationRedm.safetensors", "prefix": "Clay Animation"},
    {"name": "Blacklight Makeup", "path": "chillpixel/blacklight-makeup-sdxl-lora", "weights": "pytorch_lora_weights.bin", "prefix": "with blacklight makeup"},
    {"name": "Tim Burton Style", "path": "KappaNeuro/director-tim-burton-style", "weights": "Director Tim Burton style.safetensors", "prefix": "Director Tim Burton style"},
    {"name": "Toy Face", "path": "CiroN2022/toy-face", "weights": "toy_face_sdxl.safetensors", "prefix": "toy_face"},
    {"name": "Crayon Style", "path": "ostris/crayon_style_lora_sdxl", "weights": "crayons_v1_sdxl.safetensors", "prefix": ""},
    {"name": "Caricaturized", "path": "Norod78/SDXL-Caricaturized-Lora", "weights": "SDXL-Caricaturized-Lora.safetensors", "prefix": "Caricaturized"},
    {"name": "Watercolor Style", "path": "ostris/watercolor_style_lora_sdxl", "weights": "watercolor_v1_sdxl.safetensors", "prefix": ""},
    {"name": "Photorealistic Slider", "path": "ostris/photorealistic-slider-sdxl-lora", "weights": "sdxl_photorealistic_slider_v1-0.safetensors", "prefix": "more realistic"},
    {"name": "Lofi Girl", "path": "Norod78/SDXL-LofiGirl-Lora", "weights": "SDXL-LofiGirl-Lora.safetensors", "prefix": "LofiGirl"},
    {"name": "Architecture Siheyuan", "path": "frank-chieng/sdxl_lora_architecture_siheyuan", "weights": "sdxl_lora_architecture_siheyuan.safetensors", "prefix": "siheyuan"},
    {"name": "Vintage Magazine", "path": "Norod78/SDXL-VintageMagStyle-Lora", "weights": "SDXL-VintageMagStyle-Lora.safetensors", "prefix": "VintageMagStyle"},
    {"name": "Needlepoint", "path": "KappaNeuro/needlepoint", "weights": "Needlepoint.safetensors", "prefix": "Needlepoint -"},
    {"name": "Dressed animals", "path": "KappaNeuro/dressed-animals", "weights": "Dressed%20animals.safetensors", "prefix": "Dressed animals - "},
    {"name": "Hair Style", "path": "CiroN2022/hair-style", "weights": "hair_style.safetensors", "prefix": "crazy alternate hairstyle"},
    {"name": "Mosaic Style", "path": "CiroN2022/mosaic-style", "weights": "mosaic.safetensors", "prefix": "mosaic"},
    {"name": "Watercolor Style", "path": "ostris/watercolor_style_lora_sdxl", "weights": "watercolor_v1_sdxl.safetensors", "prefix": ""},
    {"name": "Yarn Art Style", "path": "Norod78/SDXL-YarnArtStyle-LoRA", "weights": "SDXL_Yarn_Art_Style.safetensors", "prefix": "Yarn art style"},
    {"name": "Segmind-VegaRT LCM", "path": "segmind/Segmind-VegaRT", "weights": "pytorch_lora_weights.safetensors", "prefix": ""},
    {"name": "LCM LoRA SDXL", "path": "latent-consistency/lcm-lora-sdxl", "weights": "pytorch_lora_weights.safetensors", "prefix": ""},
    #{"name": "", "path": "", "weights": "", "prefix": ""},
]
SD3_models = [
    {"name": "Stable Diffusion 3 Medium", "path": "stabilityai/stable-diffusion-3-medium-diffusers"},
    {"name": "SD3-Reality-Mix", "path": "ptx0/sd3-reality-mix"},
]
SD3_LoRA_models = [
    {"name": "JujutsuKaisen-style", "path": "adbrasi/jujutsuKaisen-style-sd3", "weights": "pytorch_lora_weights.safetensors", "prefix": ""},
    {"name": "Celebrities", "path": "ptx0/sd3-lora-celebrities", "weights": "pytorch_lora_weights.safetensors", "prefix": ""},
    {"name": "Huggy", "path": "linoyts/huggy_sd3_lora_1500", "weights": "pytorch_lora_weights.safetensors", "prefix": "a can of matcha flavored pringles"},
    {"name": "Girl", "path": "adbrasi/girl-trained-sd3", "weights": "pytorch_lora_weights.safetensors", "prefix": "a photo of pmy girl"},
    {"name": "Girl2", "path": "adbrasi/girl2-trained-sd3", "weights": "pytorch_lora_weights.safetensors", "prefix": "a photo of pmy girl"},
    {"name": "Green-BG", "path": "sergon19/green_bg_LoRa10-SDX3-plus", "weights": "pytorch_lora_weights.safetensors", "prefix": "sgc style"},
    {"name": "sd3-lora-test", "path": "ptx0/sd3-lora-test", "weights": "pytorch_lora_weights.safetensors", "prefix": ""},
]
Flux_LoRA_models = [
    {'name': 'ASCII Art', 'path': 'wavymulder/ASCII-flux-LoRA', 'weight_name': 'ASCIIart_fluxlora_wavymulder.safetensors', 'prefix': 'ASCII art'},
    {'name': 'Add Details', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-add-details', 'weight_name': 'FLUX-dev-lora-add_details.safetensors', 'prefix': ''},
    {'name': 'Aesthetic 10k', 'path': 'advokat/aesthetic-flux-lora-10k', 'weight_name': 'aesthetic10k.safetensors', 'prefix': ''},
    {'name': 'Aesthetic Anime', 'path': 'dataautogpt3/FLUX-AestheticAnime', 'weight_name': 'Flux_1_Dev_LoRA_AestheticAnime.safetensors', 'prefix': ''},
    {'name': 'Amateur Photography', 'path': 'ddh0/FLUX-Amateur-Photography-LoRA', 'weight_name': 'FLUX-Amateur-Photography-LoRA-v2.safetensors', 'prefix': 'Amateur Photography of'},
    {'name': 'Animation 2K', 'path': 'nerijs/animation2k-flux', 'weight_name': 'animation2k_v1.safetensors', 'prefix': ''},
    {'name': 'Anime CG', 'path': 'nyanko7/flux-dev-anime-cg', 'weight_name': 'ema_model.safetensors', 'prefix': ''},
    {'name': 'Anti Blur', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-AntiBlur', 'weight_name': 'FLUX-dev-lora-AntiBlur.safetensors', 'prefix': ''},
    {'name': 'Aquarel Watercolor', 'path': 'SebastianBodza/flux_lora_aquarel_watercolor', 'weight_name': 'lora.safetensors', 'prefix': 'AQUACOLTOK'},
    {'name': 'Aquarell Watercolor', 'path': 'SebastianBodza/Flux_Aquarell_Watercolor_v2', 'weight_name': 'lora.safetensors', 'prefix': 'in a watercolor style, AQUACOLTOK. White background.'},
    {'name': 'Black Myth: Wukong', 'path': 'wanghaofan/Black-Myth-Wukong-FLUX-LoRA', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': 'Wukong'},
    {'name': 'Boreal', 'path': 'kudzueye/Boreal', 'weight_name': 'boreal-flux-dev-lora-v04_1000_steps.safetensors', 'prefix': 'phone photo'},
    {'name': 'Breaking Bad', 'path': 'markury/breaking-bad-flux', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': ''},
    {'name': 'Busty', 'path': 'CultriX/Flux-Busty-LoRA', 'weight_name': 'flux-busty-lora.safetensors', 'prefix': ''},
    {'name': 'Caravaggio', 'path': 'ludocomito/flux-lora-caravaggio', 'weight_name': 'lora.safetensors', 'prefix': 'CARAVAGGIO'},
    {'name': 'Cinestill', 'path': 'adirik/flux-cinestill', 'weight_name': 'lora.safetensors', 'prefix': 'CNSTLL'},
    {'name': 'Dark Fantasy', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-Dark-Fantasy', 'weight_name': 'FLUX.1-dev-lora-Dark-Fantasy.safetensors', 'prefix': ''},
    {'name': 'Dark Fantasy Illustration', 'path': 'nerijs/dark-fantasy-illustration-flux', 'weight_name': 'darkfantasy_illustration_v2.safetensors', 'prefix': ''},
    {'name': 'Face Realism', 'path': 'prithivMLmods/Canopus-LoRA-Flux-FaceRealism', 'weight_name': 'Canopus-LoRA-Flux-FaceRealism.safetensors', 'prefix': 'face realism'},
    {'name': 'Fluxlabs Realism', 'path': 'VideoAditor/Flux-Lora-Realism', 'weight_name': 'flux_realism_lora.safetensors', 'prefix': ''},
    {'name': 'Frosting Lane', 'path': 'alvdansen/frosting_lane_flux', 'weight_name': 'flux_dev_frostinglane_araminta_k.safetensors', 'prefix': ''},
    {'name': 'Gegants', 'path': 'xaviviro/Flux-Gegants-Lora', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': ''},
    {'name': 'Ghibli Characters', 'path': 'alvarobartt/ghibli-characters-flux-lora', 'weight_name': 'ghibli-characters-flux-lora.safetensors', 'prefix': 'Ghibli style'},
    {'name': 'Ghibsky Illustration', 'path': 'aleksa-codes/flux-ghibsky-illustration', 'weight_name': 'lora.safetensors', 'prefix': 'GHIBSKY style'},
    {'name': 'Half Illustration', 'path': 'davisbro/half_illustration', 'weight_name': 'flux_train_replicate.safetensors', 'prefix': 'in the style of TOK'},
    {'name': 'Huggieverse', 'path': 'Chunte/flux-lora-Huggieverse', 'weight_name': 'lora.safetensors', 'prefix': 'HGGRE'},
    {'name': 'Hyper-SD-8steps', 'path': 'ByteDance/Hyper-SD', 'weight_name': 'Hyper-FLUX.1-dev-8steps-lora.safetensors', 'prefix': ''},
    {'name': 'Koda', 'path': 'alvdansen/flux-koda', 'weight_name': 'araminta_k_flux_koda.safetensors', 'prefix': 'flmft style'},
    {'name': 'LittleTinies', 'path': 'pzc163/LittleTinies-FLUX-lora', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': ''},
    {'name': 'Logo Design', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-Logo-Design', 'weight_name': 'FLUX-dev-lora-Logo-Design.safetensors', 'prefix': 'wablogo, logo, Minimalist'},
    {'name': 'Micro Landscape', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-Micro-landscape-on-Mobile-Phone', 'weight_name': 'FLUX-dev-lora-micro-landscape', 'prefix': ''},
    {'name': 'Mix Reality', 'path': 'bingbangboom/flux_mixReality', 'weight_name': 'HIHP_flux_lora_v0_2.safetensors', 'prefix': 'HIHP style'},
    {'name': 'Modern Anime', 'path': 'alfredplpl/flux.1-dev-modern-anime-lora', 'weight_name': 'flux.1-dev-modern-anime-lora-2.safetensors', 'prefix': 'modern anime'},
    {'name': 'Monochrome Manga', 'path': 'dataautogpt3/FLUX-MonochromeManga', 'weight_name': 'FLUX-DEV_MonochromeManga.safetensors', 'prefix': 'monochrome manga'},
    {'name': 'NSFW Flux', 'path': 'keepyoursins/nsfw_flux_lora_v1', 'weight_name': 'nsfw_flux_lora_v1.safetensors', 'prefix': ''},
    {'name': 'New Emoji Model M', 'path': 'PTtuts/flux-new-emoji-model-m', 'weight_name': 'lora.safetensors', 'prefix': 'TOK'},
    {'name': 'PS1 style', 'path': 'veryVANYA/ps1-style-flux', 'weight_name': 'flux_dev_softstyle_araminta_k.safetensors', 'prefix': 'ps1 game screenshot'},
    {'name': 'Panorama v2', 'path': 'jbilcke-hf/flux-dev-panorama-lora-2', 'weight_name': 'flux_train_replicate.safetensors', 'prefix': 'HDRI panoramic view of'},
    {'name': 'Paper-Cutout', 'path': 'Norod78/Flux_1_Dev_LoRA_Paper-Cutout-Style', 'weight_name': 'Flux_1_Dev_LoRA_Paper-Cutout-Style.safetensors', 'prefix': 'Paper Cutout Style'},
    {'name': 'Plushy World', 'path': 'alvdansen/plushy-world-flux', 'weight_name': 'plushy_world_flux_araminta_k.safetensors', 'prefix': '3dcndylnd style'},
    {'name': 'Realistic-Illustration', 'path': 'Shakker-Labs/FLUX.1-dev-LoRA-blended-realistic-illustration', 'weight_name': 'FLUX-dev-lora-blended_realistic_illustration.safetensors', 'prefix': 'artistic style blends reality and illustration elements'},
    {'name': 'Retrofuturism', 'path': 'martintomov/retrofuturism-flux', 'weight_name': 'retrofuturism_flux_lora_martintomov_v1.safetensors', 'prefix': ', retrofuturism'},
    {'name': 'SCG-Anatomy-NSFW', 'path': 'john71/SCG-Anatomy-Flux1-d-NSFW-LoRA-for-Flux', 'weight_name': 'scg-anatomy-female-v2.safetensors', 'prefix': ''},
    {'name': 'Sanna-Marin', 'path': 'mikaelh/flux-sanna-marin-lora-v0.1', 'weight_name': 'pytorch_lora_weights.safetensors', 'subfolder': 'checkpoint-1950', 'prefix': 'sanna marin'},
    {'name': 'Scarlett Johansson', 'path': 'AINxtGen/ScarlettJohansson_LoRA_FLUX', 'weight_name': 'Scarlett_Johansson_lora.safetensors', 'prefix': 'Scarlett Johansson'},
    {'name': 'Silver Metallic 3D Font', 'path': 'juaner0211/Font_Design_Silver_Metallic_3D_Bold_Font_FLUX', 'weight_name': 'j_silver_font_flux_rank16_bf16.safetensors', 'prefix': ''},
    {'name': 'SimpleTuner Test', 'path': 'markury/FLUX-dev-LoRA-test', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': 'a photo of man'},
    {'name': 'Simpsons Style', 'path': 'Norod78/Flux_1_Dev_LoRA_Simpsons-Style', 'weight_name': 'Flux_1_Dev_LoRA_Simpsons-Style.safetensors', 'prefix': 'Simpsons Style'},
    {'name': 'SoftServe Anim', 'path': 'alvdansen/softserve_anime', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': ''},
    {'name': 'Synthetic Anime', 'path': 'dataautogpt3/FLUX-SyntheticAnime', 'weight_name': 'Flux_1_Dev_LoRA_syntheticanime.safetensors', 'prefix': 'syntheticanime'},
    {'name': 'SyntheticAnime', 'path': 'dataautogpt3/FLUX-SyntheticAnime', 'weight_name': 'Flux_1_Dev_LoRA_syntheticanime.safetensors', 'prefix': '1980s anime screengrab, VHS quality'},
    {'name': 'Tarot v1', 'path': 'multimodalart/flux-tarot-v1', 'weight_name': 'flux_tarot_v1_lora.safetensors', 'prefix': 'in the style of TOK a trtcrd, tarot style'},
    {'name': 'The Point', 'path': 'alvdansen/the-point-flux', 'weight_name': 'thepoint_flux_araminta_k.safetensors', 'prefix': 'pnt style'},
    {'name': 'The Sims', 'path': 'dvyio/flux-lora-the-sims', 'weight_name': '011ed14848b3408c8d70d3ecfa14f122_lora.safetensors', 'prefix': 'video game screenshot in the style of THSMS'},
    {'name': 'Victorian Satire', 'path': 'dvyio/flux-lora-victorian-satire', 'weight_name': 'lora.safetensors', 'prefix': 'in the style of a Victorian-era TOK cartoon illustration'},
    {'name': 'Wrong', 'path': 'fofr/flux-wrong', 'weight_name': 'lora.safetensors', 'prefix': 'WRNG'},
    {'name': 'XLabs Anime', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'anime_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs Art', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'art_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs Disney', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'disney_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs Furry', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'furry_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs MJ v6', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'mjv6_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs Realism', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'realism_lora.safetensors', 'prefix': ''},
    {'name': 'XLabs Scenery', 'path': 'XLabs-AI/flux-lora-collection', 'weight_name': 'scenery_lora.safetensors', 'prefix': ''},
    {'name': 'Yarn Art', 'path': 'linoyts/yarn_art_Flux_LoRA', 'weight_name': 'pytorch_lora_weights.safetensors', 'prefix': ', yarn art style'},
    {'name': 'unDraw', 'path': 'AlloReview/flux-lora-undraw', 'weight_name': 'lora.safetensors', 'prefix': 'in the style of UndrawPurple'},
]
ip_adapter_models = [
    {'name': 'SD v1.5', 'path': 'h94/IP-Adapter', 'subfolder': 'models', 'weight_name': 'ip-adapter_sd15.bin'},
    {'name': 'Plus SD v1.5', 'path': 'h94/IP-Adapter', 'subfolder': 'models', 'weight_name': 'ip-adapter-plus_sd15.bin'},
    {'name': 'Plus Face SD v1.5', 'path': 'h94/IP-Adapter', 'subfolder': 'models', 'weight_name': 'ip-adapter-plus-face_sd15.bin'},
    {'name': 'Full Face SD v1.5', 'path': 'h94/IP-Adapter', 'subfolder': 'models', 'weight_name': 'ip-adapter-full-face_sd15.bin'},
    {'name': 'Light SD v1.5', 'path': 'h94/IP-Adapter', 'subfolder': 'models', 'weight_name': 'ip-adapter_sd15_light.bin'},
    {'name': 'Composition SD v1.5', 'path': 'ostris/ip-composition-adapter', 'subfolder': '', 'weight_name': 'ip_plus_composition_sd15.safetensors'},
]
ip_adapter_SDXL_models = [
    {'name': 'SDXL', 'path': 'h94/IP-Adapter', 'subfolder': 'sdxl_models', 'weight_name': 'ip-adapter_sdxl.bin'},
    {'name': 'Plus SDXL', 'path': 'h94/IP-Adapter', 'subfolder': 'sdxl_models', 'weight_name': 'ip-adapter-plus_sdxl_vit-h.bin'},
    {'name': 'Plus Face SDXL', 'path': 'h94/IP-Adapter', 'subfolder': 'sdxl_models', 'weight_name': 'ip-adapter-plus-face_sdxl_vit-h.bin'},
    {'name': 'SDXL ViT-H', 'path': 'h94/IP-Adapter', 'subfolder': 'sdxl_models', 'weight_name': 'ip-adapter_sdxl_vit-h.bin'},
    {'name': 'Composition SDXL', 'path': 'ostris/ip-composition-adapter', 'subfolder': '', 'weight_name': 'ip_plus_composition_sdxl.safetensors'},
    #{'name': 'Light SDXL', 'path': 'h94/IP-Adapter', 'subfolder': 'sdxl_models', 'weight_name': 'ip-adapter_sd15_light.bin'},
]

# Search https://openmodeldb.info/?q=real-esrgan
Real_ESRGAN_models = [
    {'name': 'realesr-general-x4v3', 'url': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-general-x4v3.pth', 'info': 'https://openmodeldb.info/models/4x-realesr-general-x4v3'},
    {'name': 'RealESRGAN_x4plus', 'url': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth', 'info': 'https://openmodeldb.info/models/4x-realesrgan-x4plus'},
    {'name': 'RealESRGAN_x4plus_anime', 'url': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.2.4/RealESRGAN_x4plus_anime_6B.pth', 'info': 'https://openmodeldb.info/models/4x-realesrgan-x4plus-anime-6b'},
    {'name': 'RealESRGAN_x2Plus', 'url': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth', 'info': 'https://openmodeldb.info/models/2x-realesrgan-x2plus'},
    {'name': 'BSRGANx2', 'url': 'https://github.com/cszn/KAIR/releases/download/v1.0/BSRGANx2.pth', 'info': 'https://openmodeldb.info/models/2x-BSRGAN'},
    {'name': 'realesr-animevideov3', 'url': 'https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5.0/realesr-animevideov3.pth', 'info': 'https://openmodeldb.info/models/4x-realesr-animevideo-v3'},
    {'name': '4xLSDIRplus', 'url': 'https://github.com/Phhofm/models/raw/main/4xLSDIRplus/4xLSDIRplus.pth', 'info': 'https://openmodeldb.info/models/4x-LSDIRplus'},
    {'name': '2xLexicaRRDBNet_Sharp', 'url': 'https://github.com/Phhofm/models/raw/main/2xLexicaRRDBNet/2xLexicaRRDBNet_Sharp.pth', 'info': 'https://openmodeldb.info/models/2x-LexicaRRDBNet-Sharp'},
    {'name': '2xLexicaRRDBNet', 'url': 'https://github.com/Phhofm/models/raw/main/2xLexicaRRDBNet/2xLexicaRRDBNet.pth', 'info': 'https://openmodeldb.info/models/2x-LexicaRRDBNet'},
    {'name': 'RealisticRescaler', 'url': 'https://drive.google.com/uc?id=1oLpVhJd3bUF8bEq9oMw9EB8WNVMZCBVG', 'info': 'https://openmodeldb.info/models/4x-RealisticRescaler'},
    {'name': 'UltraSharp-4x', 'url': 'https://drive.google.com/uc?id=1eq9KyetUeV-rruE73lKcjcQAFxUwi771', 'info': 'https://openmodeldb.info/models/4x-UltraSharp'},
    {'name': 'UniScaleV2-4x', 'url': 'https://drive.google.com/uc?id=13z0TYXXCEY6dN0iTEa2OTfRwp8-37iEN', 'info': 'https://openmodeldb.info/models/4x-UniScaleV2-Moderate'},
    #{'name': '', 'url': '', 'info': ''}, 'https://drive.google.com/drive/folders/13OC-hQNz_S-kX0EVjVgNO1eoGvcXrTfk?usp=sharing'
]
SwinIR_models = [
    {'name': '2xLexicaSwinIR', 'url': 'https://github.com/Phhofm/models/raw/main/2xLexicaSwinIR/2xLexicaSwinIR.pth', 'info': 'https://openmodeldb.info/models/2x-LexicaSwinIR'},
    {'name': '2xHFA2kSwinIR-S', 'url': 'https://drive.google.com/uc?id=1PeqL1ikJbBJbVzvlqvtb4d7QdSW7BzrQ', 'info': 'https://openmodeldb.info/models/2x-HFA2SwinIR-S'},
    {'name': 'SRFormer_SRx4_DF2K', 'url': 'https://drive.google.com/uc?id=13_fpD4aDE1wbEYX8yGWA3mVLZOCRWkWv', 'info': 'https://openmodeldb.info/models/4x-SRFormer-SRx4-DF2K'},
    {'name': '001_classicalSR_DF2K_s64w8_SwinIR-M_x4', 'url': 'https://github.com/JingyunLiang/SwinIR/releases/download/v0.0/001_classicalSR_DF2K_s64w8_SwinIR-M_x4.pth', 'info': 'https://openmodeldb.info/models/4x-classicalSR-DF2K-s64w8-SwinIR-M'},
    #{'name': '', 'url': '', 'info': ''},
]

#AIHorde_models = ["3DKX", "AAM XL", "Absolute Reality", "Abyss OrangeMix", "AbyssOrangeMix-AfterDark", "ACertainThing", "AIO Pixel Art", "AlbedoBase XL (SDXL)", "AMPonyXP", "Analog Diffusion", "Analog Madness", "Animagine XL", "Anime Pencil Diffusion", "Anime Illust Diffusion XL", "Anygen", "AnyLoRA", "Anything Diffusion", "Anything Diffusion Inpainting", "Anything v3", "Anything v5", "App Icon Diffusion", "Arcane Diffusion", "Archer Diffusion", "Art Of Mtg", "Asim Simpsons", "Aurora", "A to Zovya RPG", "Babes", "Balloon Art", "BB95 Furry Mix", "Blank Canvas XL", "Borderlands", "BPModel", "BRA", "BubblyDubbly", "BweshMix", "CamelliaMix 2.5D", "Cetus-Mix", "Char", "CharHelper", "Cheese Daddys Landscape Mix", "Cheyenne", "ChilloutMix", "ChromaV5", "Classic Animation Diffusion", "Clazy", "Colorful", "Coloring Book", "Comic-Diffusion", "Concept Sheet", "Counterfeit", "Cyberpunk Anime Diffusion", "CyberRealistic", "CyriousMix", "Dan Mumford Style", "Darkest Diffusion", "Dark Sushi Mix", "Dark Victorian Diffusion", "Deliberate", "Deliberate 3.0", "Deliberate Inpainting", "DGSpitzer Art Diffusion", "Disco Elysium", "DnD Item", "Double Exposure Diffusion", "Dreamlike Diffusion", "Dreamlike Photoreal", "DreamLikeSamKuvshinov", "Dreamshaper", "DreamShaper XL", "DucHaiten", "DucHaiten Classic Anime", "Dungeons and Diffusion", "Dungeons n Waifus", "Eimis Anime Diffusion", "Elden Ring Diffusion", "Elldreth's Lucid Mix", "Elldreths Retro Mix", "Epic Diffusion", "Eternos", "Experience", "ExpMix Line", "FaeTastic", "Fantasy Card Diffusion", "FKing SciFi", "Funko Diffusion", "Furry Epoch", "Fustercluck", "Future Diffusion", "Ghibli Diffusion", "GorynichMix", "Grapefruit Hentai", "Graphic-Art", "GTA5 Artwork Diffusion", "GuoFeng", "Guohua Diffusion", "HASDX", "Hassanblend", "Hassaku", "Healy's Anime Blend", "Hentai Diffusion", "HRL", "ICBINP (I Can't Believe It's Not Photography)", "ICBINP XP", "iCoMix", "Illuminati Diffusion", "Inkpunk Diffusion", "Jim Eidomode", "Juggernaut XL", "JWST Deep Space Diffusion", "Kenshi", "Knollingcase", "Korestyle", "kurzgesagt", "Laolei New Berry Protogen Mix", "Lawlas's yiff mix", "Liberty", "majicMIX realistic", "Marvel Diffusion", "Mega Merge Diffusion", "MeinaMix", "Microcasing", "Microchars", "Microcritters", "Microscopic", "Microworlds", "Midjourney Diffusion", "Midjourney PaintArt", "Min Illust Background", "ModernArt Diffusion", "mo-di-diffusion", "Moedel", "MoistMix", "Movie Diffusion", "NeverEnding Dream", "Nitro Diffusion", "Openniji", "OrbAI", "Papercutcraft", "Papercut Diffusion", "Pastel Mix", "Perfect World", "PFG", "pix2pix", "PIXHELL", "Poison", "Pokemon3D", "Pony Diffusion XL", "PortraitPlus", "PPP", "Pretty 2.5D", "PRMJ", "Project Unreal Engine 5", "ProtoGen", "Protogen Anime", "Protogen Infinity", "Pulp Vector Art", "PVC", "Quiet Goodnight XL", "Rachel Walker Watercolors", "Rainbowpatch", "Ranma Diffusion", "RCNZ Dumb Monkey", "RCNZ Gorilla With A Brick", "RealBiter", "Realism Engine", "Realistic Vision", "Redshift Diffusion", "Rev Animated", "Robo-Diffusion", "Rodent Diffusion", "RPG", "Samdoesarts Ultmerge", "Sci-Fi Diffusion", "SD-Silicon", "Seek.art MEGA", "Smoke Diffusion", "Something", "Sonic Diffusion", "Spider-Verse Diffusion", "Squishmallow Diffusion", "SDXL 1.0", "Stable Cascade 1.0", "stable_diffusion", "stable_diffusion_2.1", "stable_diffusion_inpainting", "Supermarionation", "SwamPonyXL", "Sygil-Dev Diffusion", "Synthwave", "SynthwavePunk", "TrexMix", "trinart", "Trinart Characters", "Tron Legacy Diffusion", "T-Shirt Diffusion", "T-Shirt Print Designs", "Uhmami", "Ultraskin", "UMI Olympus", "Unstable Ink Dream", "Unstable Diffusers XL", "URPM", "Valorant Diffusion", "Van Gogh Diffusion", "Vector Art", "vectorartz", "Vintedois Diffusion", "VinteProtogenMix", "Vivid Watercolors", "Voxel Art Diffusion", "waifu_diffusion", "Wavyfusion", "Western Animation Diffusion", "Woop-Woop Photo", "Xynthii-Diffusion", "Yiffy", "Zack3D", "Zeipher Female Model", "Zelda BOTW"]
AIHorde_models = ['3DKX', '526Mix-Animated', 'A-Zovya RPG Inpainting', 'AAM XL', 'ACertainThing', 'AIO Pixel Art', 'AMPonyXL', 'AbsoluteReality', 'Abyss OrangeMix', 'AbyssOrangeMix-AfterDark', 'AlbedoBase XL (SDXL)', 'Analog Diffusion', 'Analog Madness', 'Animagine XL', 'Anime Illust Diffusion XL', 'Anime Pencil Diffusion', 'AnyLoRA', 'Anygen', 'Anything Diffusion', 'Anything Diffusion Inpainting', 'Anything v3', 'Anything v5', 'App Icon Diffusion', 'Art Of Mtg', 'Aurora', 'BB95 Furry Mix', 'BB95 Furry Mix v14', 'BPModel', 'BRA', 'Babes', 'Blank Canvas XL', 'BweshMix', 'CamelliaMix 2.5D', 'Cetus-Mix', 'Char', 'CharHelper', 'Cheese Daddys Landscape Mix', 'Cheyenne', 'ChilloutMix', 'ChromaV5', 'Classic Animation Diffusion', 'Colorful', 'Comic-Diffusion', 'Counterfeit', 'CyberRealistic', 'CyriousMix', 'DGSpitzer Art Diffusion', 'Dan Mumford Style', 'Dark Sushi Mix', 'Dark Victorian Diffusion', 'Deliberate', 'Deliberate 3.0', 'Deliberate Inpainting', 'Disco Elysium', 'Disney Pixar Cartoon Type A', 'DnD Item', 'DnD Map Generator', 'Double Exposure Diffusion', 'DreamLikeSamKuvshinov', 'DreamShaper Inpainting', 'DreamShaper XL', 'Dreamlike Diffusion', 'Dreamlike Photoreal', 'Dreamshaper', 'DucHaiten', 'DucHaiten Classic Anime', 'Dungeons and Diffusion', 'Dungeons n Waifus', 'Edge Of Realism', 'Eimis Anime Diffusion', "Elldreth's Lucid Mix", 'Elysium Anime', 'Epic Diffusion', 'Epic Diffusion Inpainting', 'Ether Real Mix', 'ExpMix Line', 'Experience', 'FaeTastic', 'Fantasy Card Diffusion', 'Fluffusion', 'Flux.1-Schnell fp8 (Compact)', 'Funko Diffusion', 'Furry Epoch', 'Fustercluck', 'GTA5 Artwork Diffusion', 'Galena Redux', 'Ghibli Diffusion', 'GhostMix', 'GorynichMix', 'Grapefruit Hentai', 'Graphic-Art', 'GuFeng', 'GuoFeng', 'HASDX', 'HRL', 'Hassaku', 'Hassanblend', "Healy's Anime Blend", 'Henmix Real', 'Hentai Diffusion', "ICBINP - I Can't Believe It's Not Photography", 'ICBINP XL', 'Illuminati Diffusion', 'Inkpunk Diffusion', 'JWST Deep Space Diffusion', 'Jim Eidomode', 'JoMad Diffusion', 'Juggernaut XL', 'Kenshi', 'Laolei New Berry Protogen Mix', "Lawlas's yiff mix", 'Liberty', 'Lyriel', 'Mega Merge Diffusion', 'MeinaMix', 'Microcritters', 'Microworlds', 'Midjourney PaintArt', 'Mistoon Amethyst', 'ModernArt Diffusion', 'Moedel', 'MoistMix', 'MoonMix Fantasy', 'Movie Diffusion', 'Neurogen', 'NeverEnding Dream', 'Nitro Diffusion', 'OpenJourney Diffusion', 'Openniji', 'PFG', 'PPP', 'Papercut Diffusion', 'Pastel Mix', 'Perfect World', 'Photon', 'Poison', 'Pokemon3D', 'Pony Diffusion XL', 'PortraitPlus', 'Pretty 2.5D', 'Project Unreal Engine 5', 'ProtoGen', 'Protogen Anime', 'Protogen Infinity', 'Pulp Vector Art', 'Quiet Goodnight XL', 'RPG', 'Ranma Diffusion', 'Real Dos Mix', 'RealBiter', 'Realisian', 'Realism Engine', 'Realistic Vision', 'Realistic Vision Inpainting', 'Reliberate', 'Rev Animated', 'Robo-Diffusion', 'SD-Silicon', 'SDXL 1.0', 'Samaritan 3d Cartoon', 'Sci-Fi Diffusion', 'Seek.art MEGA', 'Something', 'Stable Cascade 1.0', 'SwamPonyXL', 'SweetBoys 2D', 'ToonYou', 'Trinart Characters', 'Tron Legacy Diffusion', 'UMI Olympus', 'URPM', 'Uhmami', 'Ultraskin', 'Unstable Diffusers XL', 'Unstable Ink Dream', 'Vector Art', 'VinteProtogenMix', 'Western Animation Diffusion', 'Woop-Woop Photo', 'Yiffy', 'Zack3D', 'Zeipher Female Model', 'iCoMix', 'iCoMix Inpainting', 'majicMIX realistic', 'stable_diffusion', 'stable_diffusion_2.1', 'stable_diffusion_inpainting', 'vectorartz', 'waifu_diffusion']
CivitAI_LoRAs = [
    {"name": "LCM&TurboMix SDXL", "model": 216190, "clip": 1, "SDXL": True},
    {"name": "LCM-LoRA SDXL", "model": 195519, "clip": 1, "SDXL": True},
    {"name": "Lightning 8step SDXL", "model": 324115, "clip": 1, "inject_trigger": "HHQR", "SDXL": True},
    {"name": "Horde Aesthetics Improver", "model": 278377, "clip": 1, "inject_trigger": "HHQR", "SDXL": False},
    {"name": "Blindbox", "model": 25995, "clip": 1, "inject_trigger": "full body, chibi,", "SDXL": False},
    {"name": "Bubbly Tech", "model": 394473, "clip": 1, "inject_trigger": "bubblytech", "SDXL": False},
    {"name": "Anime Lineart", "model": 16014, "clip": 1, "inject_trigger": "lineart, monochrome", "SDXL": False},
    {"name": "GlowingRunesAI", "model": 51686, "clip": 1, "inject_trigger": "GlowingRunes_red", "SDXL": False},
    {"name": "M_Pixel", "model": 44960, "clip": 1, "inject_trigger": "pixel", "SDXL": False},
    {"name": "KIDS ILLUSTRATION", "model": 60724, "clip": 1, "inject_trigger": "pixel", "SDXL": False},
    {"name": "EnvyBetterHands LoCon", "model": 47085, "clip": 1, "inject_trigger": "nice hands, perfect hands", "SDXL": False},
    {"name": "Middle Finger", "model": 7016, "clip": 1, "inject_trigger": "middle finger", "SDXL": False},
    {"name": "SteampunkAI", "model": 20830, "clip": 1, "inject_trigger": "steampunkai", "SDXL": False},
    {"name": "Howls Moving Castle", "model": 14605, "clip": 1, "SDXL": False},
    {"name": "ConstructionyardAI", "model": 53493, "clip": 1, "inject_trigger": "constructionyardai", "SDXL": False},
    {"name": "DragonScaleAI", "model": 55543, "clip": 1, "inject_trigger": "Dr490nSc4leAI", "SDXL": False},
    {"name": "Eye", "model": 5529, "clip": 1, "inject_trigger": "loraeyes", "SDXL": False},
    {"name": "Anime Screencap", "model": 4982, "clip": 1, "inject_trigger": "anime screencap", "SDXL": False},
    {"name": "FairyTaleAI", "model": 42260, "clip": 1, "inject_trigger": "fairytaleai", "SDXL": False},
    {"name": "Stylized 3D", "model": 10679, "clip": 1, "SDXL": False},
    {"name": "BoneyardAI", "model": 48356, "clip": 1, "inject_trigger": "BoneyardAI", "SDXL": False},
    {"name": "IvoryGoldAI", "model": 62700, "clip": 1, "inject_trigger": "IvoryGoldAI", "SDXL": False},
    {"name": "GothicHorrorAI", "model": 39760, "clip": 1, "inject_trigger": "gothichorrorai", "SDXL": False},
    {"name": "TeslapunkAI", "model": 24150, "clip": 1, "inject_trigger": "teslapunkai", "SDXL": False},
    {"name": "ValvepunkAI", "model": 24150, "clip": 1, "inject_trigger": "valvepunkai", "SDXL": False},
    {"name": "OldEgyptAI", "model": 43229, "clip": 1, "inject_trigger": "OldEgyptAI", "SDXL": False},
    {"name": "CyberpunkAI", "model": 77121, "clip": 1, "inject_trigger": "CyberpunkAI", "SDXL": False},
    {"name": "Neon CyberpunkAI", "model": 77121, "clip": 1, "inject_trigger": "neon", "SDXL": False},
    {"name": "DieselpunkAI", "model": 22462, "clip": 1, "inject_trigger": "dieselpunkai", "SDXL": False},
    {"name": "XSarchitectural-19Houseplan", "model": 26580, "clip": 1, "SDXL": False},
    {"name": "CircuitBoardAI", "model": 58410, "clip": 1, "inject_trigger": "CircuitBoardAI", "SDXL": False},
    {"name": "Chinese zodiac", "model": 15246, "clip": 1, "inject_trigger": "animal", "SDXL": False},
    {"name": "Badass Cars", "model": 54798, "clip": 1, "inject_trigger": "zeekars", "SDXL": False},
    {"name": "PiratePunkAI", "model": 45892, "clip": 1, "inject_trigger": "piratepunkai", "SDXL": False},
    {"name": "Vector illustration", "model": 60132, "clip": 1, "inject_trigger": "vector illustration", "SDXL": False},
    {"name": "Steampunk REDONE", "model": 59338, "clip": 1, "inject_trigger": "SteampunkAI", "SDXL": False},
    {"name": "CogPunk REDONE", "model": 59338, "clip": 1, "inject_trigger": "CogPunkAI", "SDXL": False},
    {"name": "BaroqueAI", "model": 38414, "clip": 1, "inject_trigger": "baroqueAI", "SDXL": False},
    {"name": "TotemPunkAI", "model": 31988, "clip": 1, "inject_trigger": "totempunkai", "SDXL": False},
    {"name": "GlassTech - World Morph", "model": 57933, "clip": 1, "inject_trigger": "glasstech scifi", "SDXL": False},
    {"name": "GemstoneAI", "model": 49374, "clip": 1, "inject_trigger": "GemstoneAI", "SDXL": False},
    {"name": "Scifi Environment Concept", "model": 403131, "clip": 1, "SDXL": False},
    {"name": "StreamlinerAI", "model": 23433, "clip": 1, "inject_trigger": "streamlinerai", "SDXL": False},
    {"name": "SXZ WoW Icons", "model": 45713, "clip": 1, "inject_trigger": "wowicon of", "SDXL": False},
    {"name": "SolarpunkAI", "model": 43944, "clip": 1, "inject_trigger": "solarpunkai", "SDXL": False},
    {"name": "Green-PoweredAI", "model": 43944, "clip": 1, "inject_trigger": "green-powered", "SDXL": False},
    {"name": "StainedGlassAI", "model": 46994, "clip": 1, "inject_trigger": "stainedglassai", "SDXL": False},
    {"name": "World of Undead", "model": 149464, "clip": 2, "inject_trigger": "worldofundead", "SDXL": False},
    {"name": "Wrench's Geometric Galore", "model": 381805, "clip": 2, "inject_trigger": "wrenchgeometricgalore", "SDXL": False},
    {"name": "ManyEyedHorrorAI", "model": 47489, "clip": 1, "inject_trigger": "ManyEyedHorrorAI", "SDXL": False},
    {"name": "NightmarishAI", "model": 56336, "clip": 1, "inject_trigger": "NightmarishAI", "SDXL": False},
    {"name": "Not-Midjourney-V3", "model": 369428, "clip": 1, "inject_trigger": "HDR", "SDXL": False},
    {"name": "Thicker Lines Anime", "model": 13910, "clip": 1, "SDXL": False},
    {"name": "3D Rendering", "model": 73756, "clip": 1, "inject_trigger": "3DMM", "SDXL": False},
    {"name": "epi_noiseoffset", "model": 13941, "clip": 1, "inject_trigger": "dark studio", "SDXL": False},
    {"name": "Add More Details Enhancer", "model": 82098, "clip": 1, "SDXL": False},
    {"name": "Anthro/Feral Slider", "model": 341045, "inject_trigger": "anthro", "clip": 1, "SDXL": False},
    {"name": "PDV6XL artist tags", "model": 317578, "clip": 1, "SDXL": False},
    {"name": "Detail Tweaker", "model": 58390, "clip": 1, "SDXL": False},
    #{"name": "", "model": , "clip": 1, "inject_trigger": "", "SDXL": False},
]
dreambooth_models = [{'name': 'disco-diffusion-style', 'token': 'a photo of ddfusion style'}, {'name': 'cat-toy', 'token': 'a photo of sks toy'}, {'name': 'herge-style', 'token': 'a photo of sks herge_style'}, {'name': 'alberto-pablo', 'token': 'a photo of sks Alberto'}, {'name': 'noggles-sd15-800-4e6', 'token': 'someone wearing sks glasses'}, {'name': 'spacecat', 'token': 'a photo of sks spacecat'}, {'name': 'pikachu', 'token': 'pikachu'}, {'name': 'kaltsit', 'token': 'kaltsit'}, {'name': 'robeez-baby-girl-water-shoes', 'token': 'a photo of sks  shoes'}, {'name': 'mertgunhan', 'token': 'mertgunhan'}, {'name': 'soydavidtapia', 'token': 'a photo of david tapia'}, {'name': 'spacecat0001', 'token': 'a photo of sks spacecat'}, {'name': 'noggles-glasses', 'token': 'a photo of a person wearing sks glasses'}, {'name': 'mario-action-figure', 'token': 'a photo of sks action figure'}, {'name': 'tattoo-design', 'token': 'line art sks tattoo design'}, {'name': 'danielveneco2', 'token': 'danielveneco'}, {'name': 'scarlet-witch-two', 'token': 'a photo of scarletwi person'}, {'name': 'angus-mcbride-style', 'token': 'angus mcbride style'}, {'name': 'mirtha-legrand', 'token': 'a photo of sks mirtha legrand'}, {'name': 'kiril', 'token': 'kiril'}, {'name': 'mr-potato-head', 'token': 'a photo of sks mr potato head'}, {'name': 'homelander', 'token': 'a photo of homelander guy'}, {'name': 'king-dog-sculpture', 'token': 'a photo of sks king dog sculpture'}, {'name': 'pedrocastillodonkey', 'token': 'a photo of PedroCastilloDonkey'}, {'name': 'xogren', 'token': 'a photo of xogren'}, {'name': 'emily-carroll-style', 'token': 'a detailed digital matte illustration by sks'}, {'name': 'sneaker', 'token': 'a photo of sks sneaker'}, {'name': 'rajj', 'token': 'a photo of sks man face'}, {'name': 'puuung', 'token': 'Puuung'}, {'name': 'partis', 'token': 'a photo of sks partis'}, {'name': 'alien-coral', 'token': 'a photo of sks alien coral'}, {'name': 'hensley-art-style', 'token': 'a painting in style of sks'}, {'name': 'tails-from-sonic', 'token': 'tails'}, {'name': 'ba-shiroko', 'token': 'a photo of sks shiroko'}, {'name': 'marina', 'token': 'marina'}, {'name': 'noggles-glasses-1200', 'token': 'a photo of a person wearing sks glasses'}, {'name': 'a-hat-in-time-girl', 'token': 'a render of sks'}, {'name': 'axolotee', 'token': 'a photo of sks Axolote'}, {'name': 'transparent-90s-console', 'token': 'a photo of sks handheld gaming console'}, {'name': 'andynsane', 'token': 'a photo of sks andynsane'}, {'name': 'tanidareal-v1', 'token': 'tanidareal'}, {'name': 'adventure-time-style', 'token': 'advtime style'}, {'name': 'sks-rv', 'token': 'a photo of sks rv'}, {'name': 'neff-voice-amp-2', 'token': 'a photo of sks neff voice amp #1'}, {'name': '27-mayonnaise-salesmen', 'token': 'a drawing of 27 from Mayonnaise SalesMen'}, {'name': 'baracus', 'token': 'b.a. baracus mr t'}, {'name': 'tahdig-rice', 'token': 'tahmricdig'}, {'name': 'angus-mcbride-style-v4', 'token': 'mcbride_style'}, {'name': 'the-witcher-game-ciri', 'token': 'a photo of a sks woman with white hair'}, {'name': 'paolo-bonolis', 'token': 'a photo of sks paolo bonolis'}, {'name': 'the-child', 'token': 'a photo of a mini australian shepherd with a slight underbite sks'}, {'name': 'gomber', 'token': 'a photo of sks toy'}, {'name': 'backpack', 'token': 'a photo of sks backpack'}, {'name': 'ricky-fort', 'token': 'a photo of sks ricky fort'}, {'name': 'mate', 'token': 'a photo of sks mate'}, {'name': 'zombie-head', 'token': 'a photo of sks zombie'}, {'name': 'leone-from-akame-ga-kill-v2', 'token': 'an anime woman character of sks'}, {'name': 'face2contra', 'token': 'a photo of sks face2contra'}, {'name': 'yakuza-0-kiryu-kazuma', 'token': 'photo of sks kiryu'}, {'name': 'gemba-cat', 'token': 'a photo of sks cat'}, {'name': 'angus-mcbride-v-3', 'token': 'angus mcbride style'}, {'name': 'california-gurls-music-video', 'token': 'caligurls'}, {'name': 'solo-levelling-art-style', 'token': 'sololeveling'}, {'name': 'blue-lightsaber-toy', 'token': 'a photo of sks toy'}, {'name': 'dmt-entity', 'token': 'a photo of sks DMT Entity'}, {'name': 'yingdream', 'token': 'a photo of an anime girl'}, {'name': 'kamenridergeats', 'token': 'a photo of kamenridergeats'}, {'name': 'quino', 'token': 'a photo of sks quino'}, {'name': 'digimon-adventure-anime', 'token': 'a landscape in sks style'}, {'name': 'evangelion-mech-unit-01', 'token': 'rendering of sks evangelion mech'}, {'name': 'elvis', 'token': 'elvis'}, {'name': 'musical-isotope', 'token': 'mi'}, {'name': 'tempa', 'token': 'a photo of sks Tempa'}, {'name': 'tempa2', 'token': 'a photo of sks Tempa'}, {'name': 'froggewut', 'token': 'a painting in the style of sks'}, {'name': 'smiling-friends-cartoon-style', 'token': 'a photo in style of sks'}, {'name': 'smario-world-map', 'token': 'a map in style of sks'}, {'name': 'edd', 'token': 'sks boy smiles'}, {'name': 'fang-yuan-002', 'token': 'an anime art of sks Fang_Yuan'}, {'name': 'langel', 'token': 'Langel'}, {'name': 'arthur-leywin', 'token': 'a photo of sks guy'}, {'name': 'kid-chameleon-character', 'token': 'kid-chameleon-character'}, {'name': 'road-to-ruin', 'token': 'starry night. sks themed level design. tiki ruins, stone statues, night sky and black silhouettes'}, {'name': 'vaporfades', 'token': 'an image in the style of sks'}, {'name': 'beard-oil-big-sur', 'token': 'a photo of sks beard oil'}, {'name': 'monero', 'token': 'a logo of sks'}, {'name': 'yagami-taichi-digimon', 'token': 'an anime boy character of sks'}, {'name': 'duregar', 'token': 'a painting of sks character'}, {'name': 'pathfinder-iconics', 'token': 'drawing in the style of sks'}, {'name': 'tyxxxszv', 'token': 'tyxxxszv'}, {'name': 'Origtron', 'token': 'Entry not found'}, {'name': 'oleg-kog', 'token': 'oleg'}, {'name': 'mau-cat', 'token': 'a photo of sks cat'}, {'name': 'justinkrane-artwork', 'token': 'art by sks JustinKrane'}, {'name': 'little-mario-jumping', 'token': 'a screenshot of tiny sks character'}, {'name': 'blue-moo-moo', 'token': 'an image of sks creature'}, {'name': 'noggles-render-1k', 'token': 'a render of sks'}, {'name': 'metahuman-rkr', 'token': 'a photo of sks rkr'}, {'name': 'taras', 'token': 'photo of sks taras'}, {'name': 'rollerbeetle', 'token': 'a photo of rollerbeetle mount'}, {'name': 'joseph-russel-ammen', 'token': 'Joseph Russel Ammen'}, {'name': 'manybearsx', 'token': 'a photo of sks drawing'}, {'name': 'mexican-concha', 'token': 'a photo of sks Mexican Concha'}, {'name': 'angus-mcbride-style-v2', 'token': 'angus mcbride style'}, {'name': 'magikarp-pokemon', 'token': 'a photo of sks pokemon'}, {'name': 'seraphm', 'token': 'serphm'}, {'name': 'estelle-sims-style', 'token': '3D render from a videogame in sks style'}, {'name': 'iman-maleki-morteza-koutzian', 'token': 'imamk'}, {'name': 'abstract-patterns-in-nature', 'token': 'abnapa'}, {'name': 'retro3d', 'token': 'trsldamrl'}, {'name': 'glitched', 'token': 'trsldamrl'}, {'name': 'dulls', 'token': '<dulls-avatar> face'}, {'name': 'nasa-space-v2-768', 'token': 'Nasa style'}, {'name': 'avocado-toy', 'token': '<avocado-toy> toy'}, {'name': 'crisimsestelle', 'token': '3d render in <cri-sims> style'}, {'name': 'sally-whitemanev', 'token': 'whitemanedb'}, {'name': 'taylorswift', 'token': 'indexaa.png'}, {'name': 'house-emblem', 'token': 'a photo of sks house-emblem'}, {'name': 'skshikakinotonoderugomi', 'token': 'sksHikakinotonoderugomi'}, {'name': 'sksbinjousoudayo', 'token': 'sksBinjouSoudayo'}, {'name': 'sksseisupusyamuzero', 'token': 'ダウンロード'}, {'name': 'sksuminaoshishimabu', 'token': 'ダウンロード'}, {'name': 'hog-rider', 'token': 'a photo of sks character'}, {'name': 'harvard-beating-yale-ii', 'token': 'a photo of sks Harvard beating Yale'}, {'name': 'hockey-player', 'token': 'a photo of sks hockey'}, {'name': 'christiano-ronaldo', 'token': 'a photo of sks'}, {'name': 'colorful-ball', 'token': 'a photo of sks ball'}, {'name': 'american-flag-cowboy-hat', 'token': 'a photo of sks hat'}, {'name': 'pranav', 'token': 'a photo of sks person'}, {'name': 'top-gun-jacket-stable-diffusion', 'token': 'a photo of sks jacket'}, {'name': 'english-bulldog-1', 'token': 'a photo of sks an english bulldog'}, {'name': 'danreynolds', 'token': 'a photo of sks dan reynolds'}, {'name': 'persona-5-shigenori-style', 'token': 'descarga'}, {'name': 'original-character-cyclps', 'token': 'cyclps'}, {'name': 'zlnsky', 'token': 'zlnsky'}, {'name': 'true-guweiz-style', 'token': 'descarga'}, {'name': 'noggles-widescreen-4e6-800', 'token': 'noggles'}, {'name': 'conf', 'token': 'AWCDJG'}, {'name': 'dtv-pkmn-monster-style', 'token': 'image'}, {'name': 'xmasvibes', 'token': 'xmasvibes'}, {'name': 'blue-lightsaber-toy', 'token': 'a photo of sks toy'}, {'name': 'adventure-time-style', 'token': 'advtime style'}, {'name': 'brime', 'token': 'prplbrime'}, {'name': 'angus-mcbride-style-v4', 'token': 'mcbride_style'}, {'name': 'oleg-kog', 'token': 'oleg'}, {'name': 'tanidareal-v1', 'token': 'tanidareal'}, {'name': 'mertgunhan', 'token': 'mertgunhan'}, {'name': 'solo-levelling-art-style', 'token': 'sololeveling'}, {'name': 'tyxxxszv', 'token': 'tyxxxszv'}, {'name': 'california-gurls-music-video', 'token': 'caligurls'}, {'name': 'mario-action-figure', 'token': 'a photo of sks action figure'}, {'name': 'tahdig-rice', 'token': 'tahmricdig'}, {'name': 'pathfinder-iconics', 'token': 'drawing in the style of sks'}, {'name': 'angus-mcbride-v-3', 'token': 'angus mcbride style'}, {'name': 'angus-mcbride-style-v2', 'token': 'angus mcbride style'}, {'name': 'angus-mcbride-style', 'token': 'angus mcbride style'}, {'name': 'danielveneco2', 'token': 'danielveneco'}, {'name': 'emily-carroll-style', 'token': 'a detailed digital matte illustration by sks'}, {'name': 'noggles-sd15-800-4e6', 'token': 'someone wearing sks glasses'}, {'name': 'alberto-pablo', 'token': 'a photo of sks Alberto'}, {'name': 'marina', 'token': 'marina'}, {'name': 'kiril', 'token': 'kiril'}, {'name': 'spacecat0001', 'token': 'a photo of sks spacecat'}, {'name': 'baracus', 'token': 'b.a. baracus mr t'}, {'name': 'gemba-cat', 'token': 'a photo of sks cat'}, {'name': 'xogren', 'token': 'a photo of xogren'}, {'name': 'musical-isotope', 'token': 'mi'}, {'name': 'spacecat', 'token': 'a photo of sks spacecat'}, {'name': 'soydavidtapia', 'token': 'a photo of david tapia'}, {'name': 'yakuza-0-kiryu-kazuma', 'token': 'photo of sks kiryu'}, {'name': 'pedrocastillodonkey', 'token': 'a photo of PedroCastilloDonkey'}, {'name': 'rajj', 'token': 'a photo of sks man face'}, {'name': 'tails-from-sonic', 'token': 'tails'}, {'name': 'pikachu', 'token': 'pikachu'}, {'name': '27-from-mayonnaise-salesmen', 'token': 'a drawing of 27 from Mayonnaise SalesMen'}, {'name': 'vaporfades', 'token': 'an image in the style of sks'}, {'name': 'sally-whitemanev', 'token': 'whitemanedb'} ]

concepts = [{'name': 'cat-toy', 'token': 'cat-toy'}, {'name': 'madhubani-art', 'token': 'madhubani-art'}, {'name': 'birb-style', 'token': 'birb-style'}, {'name': 'indian-watercolor-portraits', 'token': 'watercolor-portrait'}, {'name': 'xyz', 'token': 'xyz'}, {'name': 'poolrooms', 'token': 'poolrooms'}, {'name': 'cheburashka', 'token': 'cheburashka'}, {'name': 'hours-style', 'token': 'hours'}, {'name': 'turtlepics', 'token': 'henry-leonardi'}, {'name': 'karl-s-lzx-1', 'token': 'lzx'}, {'name': 'canary-cap', 'token': 'canary-cap'}, {'name': 'ti-junglepunk-v0', 'token': 'jungle-punk'}, {'name': 'mafalda-character', 'token': 'mafalda-quino'}, {'name': 'magic-pengel', 'token': 'magic-pengel'}, {'name': 'schloss-mosigkau', 'token': 'ralph'}, {'name': 'cubex', 'token': 'cube'}, {'name': 'covid-19-rapid-test', 'token': 'covid-test'}, {'name': 'character-pingu', 'token': 'character-pingu'}, {'name': '2814-roth', 'token': '2814Roth'}, {'name': 'vkuoo1', 'token': 'style-vkuoo1'}, {'name': 'ina-art', 'token': ''}, {'name': 'monte-novo', 'token': 'monte novo cutting board'}, {'name': 'interchanges', 'token': 'xchg'}, {'name': 'walter-wick-photography', 'token': 'walter-wick'}, {'name': 'arcane-style-jv', 'token': 'arcane-style-jv'}, {'name': 'w3u', 'token': 'w3u'}, {'name': 'smiling-friend-style', 'token': 'smilingfriends-cartoon'}, {'name': 'dr-livesey', 'token': 'dr-livesey'}, {'name': 'monster-girl', 'token': 'monster-girl'}, {'name': 'abstract-concepts', 'token': 'art-style'}, {'name': 'reeducation-camp', 'token': 'reeducation-camp'}, {'name': 'miko-3-robot', 'token': 'miko-3'}, {'name': 'party-girl', 'token': 'party-girl'}, {'name': 'dicoo', 'token': 'Dicoo'}, {'name': 'kuvshinov', 'token': 'kuvshinov'}, {'name': 'mass', 'token': 'mass'}, {'name': 'ldr', 'token': 'ldr'}, {'name': 'hub-city', 'token': 'HubCity'}, {'name': 'masyunya', 'token': 'masyunya'}, {'name': 'david-moreno-architecture', 'token': 'dm-arch'}, {'name': 'lolo', 'token': 'lolo'}, {'name': 'apulian-rooster-v0-1', 'token': 'apulian-rooster-v0.1'}, {'name': 'fractal', 'token': 'fractal'}, {'name': 'nebula', 'token': 'nebula'}, {'name': 'ldrs', 'token': 'ldrs'}, {'name': 'art-brut', 'token': 'art-brut'}, {'name': 'malika-favre-art-style', 'token': 'malika-favre'}, {'name': 'line-art', 'token': 'line-art'}, {'name': 'shrunken-head', 'token': 'shrunken-head'}, {'name': 'bonzi-monkey', 'token': 'bonzi'}, {'name': 'herge-style', 'token': 'herge'}, {'name': 'johnny-silverhand', 'token': 'johnny-silverhand'}, {'name': 'linnopoke', 'token': 'linnopoke'}, {'name': 'koko-dog', 'token': 'koko-dog'}, {'name': 'stuffed-penguin-toy', 'token': 'pengu-toy'}, {'name': 'monster-toy', 'token': 'monster-toy'}, {'name': 'dong-ho', 'token': 'dong-ho'}, {'name': 'orangejacket', 'token': 'orangejacket'}, {'name': 'fergal-cat', 'token': 'fergal-cat'}, {'name': 'summie-style', 'token': 'summie-style'}, {'name': 'chonkfrog', 'token': 'chonkfrog'}, {'name': 'alberto-mielgo', 'token': 'street'}, {'name': 'lucky-luke', 'token': 'lucky-luke'}, {'name': 'zdenek-art', 'token': 'zdenek-artwork'}, {'name': 'star-tours-posters', 'token': 'star-tours'}, {'name': 'huang-guang-jian', 'token': 'huang-guang-jian'}, {'name': 'painting', 'token': 'will'}, {'name': 'line-style', 'token': 'line-style'}, {'name': 'venice', 'token': 'venice'}, {'name': 'russian', 'token': 'Russian'}, {'name': 'tony-diterlizzi-s-planescape-art', 'token': 'tony-diterlizzi-planescape'}, {'name': 'moeb-style', 'token': 'moe-bius'}, {'name': 'amine', 'token': 'ayna'}, {'name': 'kojima-ayami', 'token': 'KOJIMA'}, {'name': 'dong-ho2', 'token': 'dong-ho-2'}, {'name': 'ruan-jia', 'token': 'ruan-jia'}, {'name': 'purplefishli', 'token': 'purplefishli'}, {'name': 'cry-baby-style', 'token': 'cry-baby'}, {'name': 'between2-mt-fade', 'token': 'b2MTfade'}, {'name': 'mtl-longsky', 'token': 'mtl-longsky'}, {'name': 'scrap-style', 'token': 'style-chewie'}, {'name': 'tela-lenca', 'token': 'tela-lenca'}, {'name': 'zillertal-can', 'token': 'zillertal-ipa'}, {'name': 'shu-doll', 'token': 'shu-doll'}, {'name': 'eastward', 'token': 'eastward'}, {'name': 'chuck-walton', 'token': 'Chuck_Walton'}, {'name': 'chucky', 'token': 'merc'}, {'name': 'smw-map', 'token': 'smw-map'}, {'name': 'erwin-olaf-style', 'token': 'erwin-olaf'}, {'name': 'maurice-quentin-de-la-tour-style', 'token': 'maurice'}, {'name': 'dan-seagrave-art-style', 'token': 'dan-seagrave'}, {'name': 'drive-scorpion-jacket', 'token': 'drive-scorpion-jacket'}, {'name': 'dark-penguin-pinguinanimations', 'token': 'darkpenguin-robot'}, {'name': 'rd-paintings', 'token': 'rd-painting'}, {'name': 'borderlands', 'token': 'borderlands'}, {'name': 'depthmap', 'token': 'depthmap'}, {'name': 'lego-astronaut', 'token': 'lego-astronaut'}, {'name': 'transmutation-circles', 'token': 'tcircle'}, {'name': 'mycat', 'token': 'mycat'}, {'name': 'ilya-shkipin', 'token': 'ilya-shkipin-style'}, {'name': 'moxxi', 'token': 'moxxi'}, {'name': 'riker-doll', 'token': 'rikerdoll'}, {'name': 'apex-wingman', 'token': 'wingman-apex'}, {'name': 'naf', 'token': 'nal'}, {'name': 'handstand', 'token': 'handstand'}, {'name': 'vb-mox', 'token': 'vb-mox'}, {'name': 'pixel-toy', 'token': 'pixel-toy'}, {'name': 'olli-olli', 'token': 'olli-olli'}, {'name': 'floral', 'token': 'ntry not foun'}, {'name': 'minecraft-concept-art', 'token': 'concept'}, {'name': 'yb-anime', 'token': 'anime-character'}, {'name': 'ditko', 'token': 'cat-toy'}, {'name': 'disquieting-muses', 'token': 'muses'}, {'name': 'ned-flanders', 'token': 'flanders'}, {'name': 'fluid-acrylic-jellyfish-creatures-style-of-carl-ingram-art', 'token': 'jelly-core'}, {'name': 'ic0n', 'token': 'ic0n'}, {'name': 'pyramidheadcosplay', 'token': 'Cos-Pyramid'}, {'name': 'phc', 'token': 'Cos-Pyramid'}, {'name': 'og-mox-style', 'token': 'og-mox-style'}, {'name': 'klance', 'token': 'klance'}, {'name': 'john-blanche', 'token': 'john-blanche'}, {'name': 'cowboy', 'token': 'cowboyStyle'}, {'name': 'darkpenguinanimatronic', 'token': 'penguin-robot'}, {'name': 'doener-red-line-art', 'token': 'dnr'}, {'name': 'style-of-marc-allante', 'token': 'Marc_Allante'}, {'name': 'crybaby-style-2-0', 'token': 'crybaby2'}, {'name': 'werebloops', 'token': 'werebloops'}, {'name': 'xbh', 'token': 'xbh'}, {'name': 'unfinished-building', 'token': 'unfinished-building'}, {'name': 'teelip-ir-landscape', 'token': 'teelip-ir-landscape'}, {'name': 'road-to-ruin', 'token': 'RtoR'}, {'name': 'piotr-jablonski', 'token': 'piotr-jablonski'}, {'name': 'jamiels', 'token': 'jamiels'}, {'name': 'tomcat', 'token': 'tom-cat'}, {'name': 'meyoco', 'token': 'meyoco'}, {'name': 'nixeu', 'token': 'nixeu'}, {'name': 'tnj', 'token': 'tnj'}, {'name': 'cute-bear', 'token': 'cute-bear'}, {'name': 'leica', 'token': 'leica'}, {'name': 'anime-boy', 'token': 'myAItestShota'}, {'name': 'garfield-pizza-plush', 'token': 'garfield-plushy'}, {'name': 'design', 'token': 'design'}, {'name': 'mikako-method', 'token': 'm-m'}, {'name': 'cornell-box', 'token': 'cornell-box'}, {'name': 'sculptural-style', 'token': 'diaosu'}, {'name': 'aavegotchi', 'token': 'aave-gotchi'}, {'name': 'swamp-choe-2', 'token': 'cat-toy'}, {'name': 'super-nintendo-cartridge', 'token': 'snesfita-object'}, {'name': 'garfield-pizza-plush-v2', 'token': 'garfield-plushy'}, {'name': 'rickyart', 'token': 'RickyArt'}, {'name': 'eye-of-agamotto', 'token': 'eye-aga'}, {'name': 'freddy-fazbear', 'token': 'freddy-fazbear'}, {'name': 'glass-pipe', 'token': 'glass-sherlock'}, {'name': 'black-waifu', 'token': 'black-waifu'}, {'name': 'roy-lichtenstein', 'token': 'roy-lichtenstein'}, {'name': 'ugly-sonic', 'token': 'ugly-sonic'}, {'name': 'glow-forest', 'token': 'dark-forest'}, {'name': 'painted-student', 'token': 'painted_student'}, {'name': 'salmonid', 'token': 'salmonid'}, {'name': 'huayecai820-greyscale', 'token': 'huayecaigreyscale-style'}, {'name': 'arthur1', 'token': 'arthur1'}, {'name': 'huckleberry', 'token': 'huckleberry'}, {'name': 'collage3', 'token': 'Collage3'}, {'name': 'spritual-monsters', 'token': 'spritual-monsters'}, {'name': 'baldi', 'token': 'baldi'}, {'name': 'tcirle', 'token': 'tcircle'}, {'name': 'pantone-milk', 'token': 'pantone-milk'}, {'name': 'retropixelart-pinguin', 'token': 'retropixelart-style'}, {'name': 'doose-s-realistic-art-style', 'token': 'doose-realistic'}, {'name': 'grit-toy', 'token': 'grit-toy'}, {'name': 'pink-beast-pastelae-style', 'token': 'pinkbeast'}, {'name': 'mikako-methodi2i', 'token': 'm-mi2i'}, {'name': 'aj-fosik', 'token': 'AJ-Fosik'}, {'name': 'collage-cutouts', 'token': 'collage-cutouts'}, {'name': 'cute-cat', 'token': 'cute-bear'}, {'name': 'kaleido', 'token': 'kaleido'}, {'name': 'xatu', 'token': 'xatu-pokemon'}, {'name': 'a-female-hero-from-the-legend-of-mir', 'token': ' <female-hero> from The Legend of Mi'}, {'name': 'cologne', 'token': 'cologne-dom'}, {'name': 'wlop-style', 'token': 'wlop-style'}, {'name': 'larrette', 'token': 'larrette'}, {'name': 'bert-muppet', 'token': 'bert-muppet'}, {'name': 'my-hero-academia-style', 'token': 'MHA style'}, {'name': 'vcr-classique', 'token': 'vcr_c'}, {'name': 'xatu2', 'token': 'xatu-test'}, {'name': 'tela-lenca2', 'token': 'tela-lenca'}, {'name': 'dragonborn', 'token': 'dragonborn'}, {'name': 'mate', 'token': 'mate'}, {'name': 'alien-avatar', 'token': 'alien-avatar'}, {'name': 'pastelartstyle', 'token': 'Arzy'}, {'name': 'kings-quest-agd', 'token': 'ings-quest-ag'}, {'name': 'doge-pound', 'token': 'doge-pound'}, {'name': 'type', 'token': 'typeface'}, {'name': 'fileteado-porteno', 'token': 'fileteado-porteno'}, {'name': 'bullvbear', 'token': 'bullVBear'}, {'name': 'freefonix-style', 'token': 'Freefonix'}, {'name': 'garcon-the-cat', 'token': 'garcon-the-cat'}, {'name': 'better-collage3', 'token': 'C3'}, {'name': 'metagabe', 'token': 'metagabe'}, {'name': 'ggplot2', 'token': 'ggplot2'}, {'name': 'yoshi', 'token': 'yoshi'}, {'name': 'illustration-style', 'token': 'illustration-style'}, {'name': 'centaur', 'token': 'centaur'}, {'name': 'zoroark', 'token': 'zoroark'}, {'name': 'bad_Hub_Hugh', 'token': 'HubHugh'}, {'name': 'irasutoya', 'token': 'irasutoya'}, {'name': 'liquid-light', 'token': 'lls'}, {'name': 'zaneypixelz', 'token': 'zaneypixelz'}, {'name': 'tubby', 'token': 'tubby'}, {'name': 'atm-ant', 'token': 'atm-ant'}, {'name': 'fang-yuan-001', 'token': 'fang-yuan'}, {'name': 'dullboy-caricature', 'token': 'dullboy-cari'}, {'name': 'bada-club', 'token': 'bada-club'}, {'name': 'zaney', 'token': 'zaney'}, {'name': 'a-tale-of-two-empires', 'token': 'two-empires'}, {'name': 'dabotap', 'token': 'dabotap'}, {'name': 'harley-quinn', 'token': 'harley-quinn'}, {'name': 'vespertine', 'token': 'Vesp'}, {'name': 'ricar', 'token': 'ricard'}, {'name': 'conner-fawcett-style', 'token': 'badbucket'}, {'name': 'ingmar-bergman', 'token': 'ingmar-bergman'}, {'name': 'poutine-dish', 'token': 'poutine-qc'}, {'name': 'shev-linocut', 'token': 'shev-linocut'}, {'name': 'grifter', 'token': 'grifter'}, {'name': 'dog', 'token': 'Winston'}, {'name': 'tangles', 'token': 'cora-tangle'}, {'name': 'lost-rapper', 'token': 'lost-rapper'}, {'name': 'eddie', 'token': 'ddi'}, {'name': 'thunderdome-covers', 'token': 'thunderdome'}, {'name': 'she-mask', 'token': 'she-mask'}, {'name': 'chillpill', 'token': 'Chillpill'}, {'name': 'robertnava', 'token': 'robert-nava'}, {'name': 'looney-anime', 'token': 'looney-anime'}, {'name': 'axe-tattoo', 'token': 'axe-tattoo'}, {'name': 'fireworks-over-water', 'token': 'firework'}, {'name': 'collage14', 'token': 'C14'}, {'name': 'green-tent', 'token': 'green-tent'}, {'name': 'dtv-pkmn', 'token': 'dtv-pkm2'}, {'name': 'crinos-form-garou', 'token': 'crinos'}, {'name': '8bit', 'token': '8bit'}, {'name': 'tubby-cats', 'token': 'tubby'}, {'name': 'travis-bedel', 'token': 'bedelgeuse2'}, {'name': 'uma', 'token': 'uma'}, {'name': 'ie-gravestone', 'token': 'internet-explorer-gravestone'}, {'name': 'colossus', 'token': 'colossus'}, {'name': 'uma-style-classic', 'token': 'uma'}, {'name': 'collage3-hubcity', 'token': 'C3Hub'}, {'name': 'goku', 'token': 'goku'}, {'name': 'galaxy-explorer', 'token': 'galaxy-explorer'}, {'name': 'rl-pkmn-test', 'token': 'rl-pkmn'}, {'name': 'naval-portrait', 'token': 'naval-portrait'}, {'name': 'daycare-attendant-sun-fnaf', 'token': 'biblic-sun-fnaf'}, {'name': 'reksio-dog', 'token': 'reksio-dog'}, {'name': 'breakcore', 'token': 'reakcor'}, {'name': 'junji-ito-artstyle', 'token': 'junji-ito-style'}, {'name': 'gram-tops', 'token': 'gram-tops'}, {'name': 'henjo-techno-show', 'token': 'HENJOTECHNOSHOW'}, {'name': 'trash-polka-artstyle', 'token': 'trash-polka-style'}, {'name': 'faraon-love-shady', 'token': ''}, {'name': 'trigger-studio', 'token': 'Trigger Studio'}, {'name': 'tb303', 'token': '"tb303'}, {'name': 'neon-pastel', 'token': 'neon-pastel'}, {'name': 'fursona', 'token': 'fursona-2'}, {'name': 'sterling-archer', 'token': 'archer-style'}, {'name': 'captain-haddock', 'token': 'captain-haddock'}, {'name': 'my-mug', 'token': 'my-mug'}, {'name': 'joe-whiteford-art-style', 'token': 'joe-whiteford-artstyle'}, {'name': 'on-kawara', 'token': 'on-kawara'}, {'name': 'hours-sentry-fade', 'token': 'Hours_Sentry'}, {'name': 'rektguy', 'token': 'rektguy'}, {'name': 'dyoudim-style', 'token': 'DyoudiM-style'}, {'name': 'kaneoya-sachiko', 'token': 'Kaneoya'}, {'name': 'retro-girl', 'token': 'retro-girl'}, {'name': 'buddha-statue', 'token': 'buddha-statue'}, {'name': 'hitokomoru-style-nao', 'token': 'hitokomoru-style'}, {'name': 'plant-style', 'token': 'plant'}, {'name': 'cham', 'token': 'cham'}, {'name': 'mayor-richard-irvin', 'token': 'Richard_Irvin'}, {'name': 'sd-concepts-library-uma-meme', 'token': 'uma-object-full'}, {'name': 'uma-meme', 'token': 'uma-object-full'}, {'name': 'thunderdome-cover', 'token': 'thunderdome-cover'}, {'name': 'sem-mac2n', 'token': 'SEM_Mac2N'}, {'name': 'hoi4', 'token': 'hoi4'}, {'name': 'hd-emoji', 'token': 'HDemoji-object'}, {'name': 'lumio', 'token': 'lumio'}, {'name': 't-skrang', 'token': 'tskrang'}, {'name': 'agm-style-nao', 'token': 'agm-style'}, {'name': 'uma-meme-style', 'token': 'uma-meme-style'}, {'name': 'retro-mecha-rangers', 'token': 'aesthetic'}, {'name': 'babushork', 'token': 'babushork'}, {'name': 'qpt-atrium', 'token': 'QPT_ATRIUM'}, {'name': 'sushi-pixel', 'token': 'sushi-pixel'}, {'name': 'osrsmini2', 'token': ''}, {'name': 'ttte', 'token': 'ttte-2'}, {'name': 'atm-ant-2', 'token': 'atm-ant'}, {'name': 'dan-mumford', 'token': 'dan-mumford'}, {'name': 'renalla', 'token': 'enall'}, {'name': 'cow-uwu', 'token': 'cow-uwu'}, {'name': 'one-line-drawing', 'token': 'lineart'}, {'name': 'inuyama-muneto-style-nao', 'token': 'inuyama-muneto-style'}, {'name': 'altvent', 'token': 'AltVent'}, {'name': 'accurate-angel', 'token': 'accurate-angel'}, {'name': 'mtg-card', 'token': 'mtg-card'}, {'name': 'ddattender', 'token': 'ddattender'}, {'name': 'thalasin', 'token': 'thalasin-plus'}, {'name': 'moebius', 'token': 'moebius'}, {'name': 'liqwid-aquafarmer', 'token': 'aquafarmer'}, {'name': 'onepunchman', 'token': 'OnePunch'}, {'name': 'kawaii-colors', 'token': 'kawaii-colors-style'}, {'name': 'naruto', 'token': 'Naruto'}, {'name': 'backrooms', 'token': 'Backrooms'}, {'name': 'a-hat-kid', 'token': 'hatintime-kid'}, {'name': 'furrpopasthetic', 'token': 'furpop'}, {'name': 'RINGAO', 'token': ''}, {'name': 'csgo-awp-texture-map', 'token': 'csgo_awp_texture'}, {'name': 'luinv2', 'token': 'luin-waifu'}, {'name': 'hydrasuit', 'token': 'hydrasuit'}, {'name': 'milady', 'token': 'milady'}, {'name': 'ganyu-genshin-impact', 'token': 'ganyu'}, {'name': 'wayne-reynolds-character', 'token': 'warcharport'}, {'name': 'david-firth-artstyle', 'token': 'david-firth-artstyle'}, {'name': 'seraphimmoonshadow-art', 'token': 'seraphimmoonshadow-art'}, {'name': 'osrstiny', 'token': 'osrstiny'}, {'name': 'lugal-ki-en', 'token': 'lugal-ki-en'}, {'name': 'seamless-ground', 'token': 'seamless-ground'}, {'name': 'sewerslvt', 'token': 'ewerslv'}, {'name': 'diaosu-toy', 'token': 'diaosu-toy'}, {'name': 'sakimi-style', 'token': 'sakimi'}, {'name': 'rj-palmer', 'token': 'rj-palmer'}, {'name': 'harmless-ai-house-style-1', 'token': 'bee-style'}, {'name': 'harmless-ai-1', 'token': 'bee-style'}, {'name': 'yerba-mate', 'token': 'yerba-mate'}, {'name': 'bella-goth', 'token': 'bella-goth'}, {'name': 'bobs-burgers', 'token': 'bobs-burgers'}, {'name': 'jamie-hewlett-style', 'token': 'hewlett'}, {'name': 'belen', 'token': 'belen'}, {'name': 'shvoren-style', 'token': 'shvoren-style'}, {'name': 'gymnastics-leotard-v2', 'token': 'gymnastics-leotard2'}, {'name': 'rd-chaos', 'token': 'rd-chaos'}, {'name': 'armor-concept', 'token': 'armor-concept'}, {'name': 'ouroboros', 'token': 'ouroboros'}, {'name': 'm-geo', 'token': 'm-geo'}, {'name': 'Akitsuki', 'token': ''}, {'name': 'uzumaki', 'token': 'NARUTO'}, {'name': 'sorami-style', 'token': 'sorami-style'}, {'name': 'lxj-o4', 'token': 'csp'}, {'name': 'she-hulk-law-art', 'token': 'shehulk-style'}, {'name': 'led-toy', 'token': 'led-toy'}, {'name': 'durer-style', 'token': 'drr-style'}, {'name': 'hiten-style-nao', 'token': 'hiten-style-nao'}, {'name': 'mechasoulall', 'token': 'mechasoulall'}, {'name': 'wish-artist-stile', 'token': 'wish-style'}, {'name': 'max-foley', 'token': 'max-foley'}, {'name': 'loab-style', 'token': 'loab-style'}, {'name': '3d-female-cyborgs', 'token': 'A female cyborg'}, {'name': 'r-crumb-style', 'token': 'rcrumb'}, {'name': 'paul-noir', 'token': 'paul-noir'}, {'name': 'cgdonny1', 'token': 'donny1'}, {'name': 'valorantstyle', 'token': 'valorant'}, {'name': 'loab-character', 'token': 'loab-character'}, {'name': 'Atako', 'token': ''}, {'name': 'threestooges', 'token': 'threestooges'}, {'name': 'dsmuses', 'token': 'DSmuses'}, {'name': 'fish', 'token': 'fish'}, {'name': 'glass-prism-cube', 'token': 'glass-prism-cube'}, {'name': 'elegant-flower', 'token': 'elegant-flower'}, {'name': 'hanfu-anime-style', 'token': 'hanfu-anime-style'}, {'name': 'green-blue-shanshui', 'token': 'green-blue shanshui'}, {'name': 'lizardman', 'token': 'laceholderTokenLizardma'}, {'name': 'rail-scene', 'token': 'rail-pov'}, {'name': 'lula-13', 'token': 'lula-13'}, {'name': 'laala-character', 'token': 'laala'}, {'name': 'margo', 'token': 'dog-margo'}, {'name': 'carrascharacter', 'token': 'Carras'}, {'name': 'vietstoneking', 'token': 'vietstoneking'}, {'name': 'rhizomuse-machine-bionic-sculpture', 'token': ''}, {'name': 'rcrumb-portraits-style', 'token': 'rcrumb-portraits'}, {'name': 'mu-sadr', 'token': '783463b'}, {'name': 'bozo-22', 'token': 'bozo-22'}, {'name': 'skyfalls', 'token': 'SkyFalls'}, {'name': 'zk', 'token': ''}, {'name': 'tudisco', 'token': 'cat-toy'}, {'name': 'kogecha', 'token': 'kogecha'}, {'name': 'ori-toor', 'token': 'ori-toor'}, {'name': 'isabell-schulte-pviii-style', 'token': 'isabell-schulte-p8-style'}, {'name': 'rilakkuma', 'token': 'rilakkuma'}, {'name': 'indiana', 'token': 'indiana'}, {'name': 'black-and-white-design', 'token': 'PM_style'}, {'name': 'isabell-schulte-pviii-1024px-1500-steps-style', 'token': 'isabell-schulte-p8-style-1024p-1500s'}, {'name': 'fold-structure', 'token': 'fold-geo'}, {'name': 'brunnya', 'token': 'Brunnya'}, {'name': 'jos-de-kat', 'token': 'kat-jos'}, {'name': 'singsing-doll', 'token': 'singsing'}, {'name': 'singsing', 'token': 'singsing'}, {'name': 'isabell-schulte-pviii-12tiles-3000steps-style', 'token': 'isabell-schulte-p8-style-12tiles-3000s'}, {'name': 'f-22', 'token': 'f-22'}, {'name': 'jin-kisaragi', 'token': 'jin-kisaragi'}, {'name': 'depthmap-style', 'token': 'depthmap'}, {'name': 'crested-gecko', 'token': 'crested-gecko'}, {'name': 'grisstyle', 'token': 'gris'}, {'name': 'ikea-fabler', 'token': 'ikea-fabler'}, {'name': 'joe-mad', 'token': 'joe-mad'}, {'name': 'boissonnard', 'token': 'boissonnard'}, {'name': 'overprettified', 'token': 'overprettified'}, {'name': 'all-rings-albuns', 'token': 'rings-all-albuns'}, {'name': 'shiny-polyman', 'token': 'shiny-polyman'}, {'name': 'scarlet-witch', 'token': 'sw-mom'}, {'name': 'wojaks-now', 'token': 'red-wojak'}, {'name': 'carasibana', 'token': 'carasibana'}, {'name': 'towerplace', 'token': 'TowerPlace'}, {'name': 'cumbia-peruana', 'token': 'cumbia-peru'}, {'name': 'bloo', 'token': 'owl-guy'}, {'name': 'dog-django', 'token': 'dog-django'}, {'name': 'facadeplace', 'token': 'FacadePlace'}, {'name': 'blue-zombie', 'token': 'blue-zombie'}, {'name': 'blue-zombiee', 'token': 'blue-zombie'}, {'name': 'jinjoon-lee-they', 'token': 'jinjoon_lee_they'}, {'name': 'ralph-mcquarrie', 'token': 'ralph-mcquarrie'}, {'name': 'hiyuki-chan', 'token': 'hiyuki-chan'}, {'name': 'isabell-schulte-pviii-4tiles-6000steps', 'token': 'isabell-schulte-p8-style-4tiles-6000s'}, {'name': 'liliana', 'token': 'liliana'}, {'name': 'morino-hon-style', 'token': 'morino-hon'}, {'name': 'artist-yukiko-kanagai', 'token': 'Yukiko Kanagai '}, {'name': 'wheatland', 'token': ''}, {'name': 'm-geoo', 'token': 'm-geo'}, {'name': 'wheatland-arknight', 'token': 'golden-wheats-fields'}, {'name': 'mokoko', 'token': 'mokoko'}, {'name': '001glitch-core', 'token': '01glitch_cor'}, {'name': 'stardew-valley-pixel-art', 'token': 'pixelart-stardew'}, {'name': 'isabell-schulte-pviii-4tiles-500steps', 'token': 'isabell-schulte-p8-style-4tiles-500s'}, {'name': 'anime-girl', 'token': 'anime-girl'}, {'name': 'heather', 'token': 'eather'}, {'name': 'rail-scene-style', 'token': 'rail-pov'}, {'name': 'quiesel', 'token': 'quiesel'}, {'name': 'matthew-stone', 'token': 'atthew-ston'}, {'name': 'dreamcore', 'token': 'dreamcore'}, {'name': 'pokemon-conquest-sprites', 'token': 'poke-conquest'}, {'name': 'tili-concept', 'token': 'tili'}, {'name': 'nouns-glasses', 'token': 'nouns glasses'}, {'name': 'shigure-ui-style', 'token': 'shigure-ui'}, {'name': 'pen-ink-portraits-bennorthen', 'token': 'ink-portrait-by-BenNorthern'}, {'name': 'nikodim', 'token': 'nikodim'}, {'name': 'ori', 'token': 'Ori'}, {'name': 'anya-forger', 'token': 'anya-forger'}, {'name': 'lavko', 'token': 'lavko'}, {'name': 'fasina', 'token': 'Fasina'}, {'name': 'uma-clean-object', 'token': 'uma-clean-object'}, {'name': 'wojaks-now-now-now', 'token': 'red-wojak'}, {'name': 'memnarch-mtg', 'token': 'mtg-memnarch'}, {'name': 'tonal1', 'token': 'Tonal'}, {'name': 'tesla-bot', 'token': 'tesla-bot'}, {'name': 'red-glasses', 'token': 'red-glasses'}, {'name': 'csgo-awp-object', 'token': 'csgo_awp'}, {'name': 'stretch-re1-robot', 'token': 'stretch'}, {'name': 'isabell-schulte-pv-pvii-3000steps', 'token': 'isabell-schulte-p5-p7-style-3000s'}, {'name': 'insidewhale', 'token': 'InsideWhale'}, {'name': 'noggles', 'token': 'noggles'}, {'name': 'isometric-tile-test', 'token': 'iso-tile'}, {'name': 'bamse-og-kylling', 'token': 'bamse-kylling'}, {'name': 'marbling-art', 'token': 'marbling-art'}, {'name': 'joemad', 'token': 'joemad'}, {'name': 'bamse', 'token': 'bamse'}, {'name': 'dq10-anrushia', 'token': 'anrushia'}, {'name': 'test', 'token': 'AIO'}, {'name': 'naoki-saito', 'token': 'naoki_saito'}, {'name': 'raichu', 'token': 'raichu'}, {'name': 'child-zombie', 'token': 'child-zombie'}, {'name': 'yf21', 'token': 'YF21'}, {'name': 'titan-robot', 'token': 'titan'}, {'name': 'cyberpunk-lucy', 'token': 'cyberpunk-lucy'}, {'name': 'giygas', 'token': 'giygas'}, {'name': 'david-martinez-cyberpunk', 'token': 'david-martinez-cyberpunk'}, {'name': 'phan-s-collage', 'token': 'pcollage'}, {'name': 'jojo-bizzare-adventure-manga-lineart', 'token': 'JoJo_lineart'}, {'name': 'homestuck-sprite', 'token': 'homestuck-sprite'}, {'name': 'kogatan-shiny', 'token': 'ogata'}, {'name': 'moo-moo', 'token': 'moomoo'}, {'name': 'detectivedinosaur1', 'token': 'dd1'}, {'name': 'arcane-face', 'token': 'arcane-face'}, {'name': 'sherhook-painting', 'token': 'sherhook'}, {'name': 'isabell-schulte-pviii-1-image-style', 'token': 'isabell-schulte-p8-1-style'}, {'name': 'dicoo2', 'token': 'dicoo'}, {'name': 'hrgiger-drmacabre', 'token': 'barba'}, {'name': 'babau', 'token': 'babau'}, {'name': 'darkplane', 'token': 'DarkPlane'}, {'name': 'wildkat', 'token': 'wildkat'}, {'name': 'half-life-2-dog', 'token': 'hl-dog'}, {'name': 'outfit-items', 'token': 'outfit-items'}, {'name': 'midjourney-style', 'token': 'midjourney-style'}, {'name': 'puerquis-toy', 'token': 'puerquis'}, {'name': 'maus', 'token': 'Maus'}, {'name': 'jetsetdreamcastcovers', 'token': 'jet'}, {'name': 'karan-gloomy', 'token': 'karan'}, {'name': 'yoji-shinkawa-style', 'token': 'yoji-shinkawa'}, {'name': 'million-live-akane-15k', 'token': 'akane'}, {'name': 'million-live-akane-3k', 'token': 'akane'}, {'name': 'sherhook-painting-v2', 'token': 'sherhook'}, {'name': 'gba-pokemon-sprites', 'token': 'GBA-Poke-Sprites'}, {'name': 'gim', 'token': 'grimes-album-style'}, {'name': 'char-con', 'token': 'char-con'}, {'name': 'bluebey', 'token': 'bluebey'}, {'name': 'homestuck-troll', 'token': 'homestuck-troll'}, {'name': 'million-live-akane-shifuku-3k', 'token': 'akane'}, {'name': 'thegeneral', 'token': 'bobknight'}, {'name': 'million-live-spade-q-object-3k', 'token': 'spade_q'}, {'name': 'million-live-spade-q-style-3k', 'token': 'spade_q'}, {'name': 'ibere-thenorio', 'token': 'ibere-thenorio'}, {'name': 'yinit', 'token': 'init-dropca'}, {'name': 'bee', 'token': 'b-e-e'}, {'name': 'pixel-mania', 'token': 'pixel-mania'}, {'name': 'sunfish', 'token': 'SunFish'}, {'name': 'test2', 'token': 'AIOCARD'}, {'name': 'pool-test', 'token': 'pool_test'}, {'name': 'mokoko-seed', 'token': 'mokoko-seed'}, {'name': 'isabell-schulte-pviii-4-tiles-1-lr-3000-steps-style', 'token': 'isabell-schulte-p8-4tiles-1lr-300s-style'}, {'name': 'ghostproject-men', 'token': 'ghostsproject-style'}, {'name': 'phan', 'token': 'phan'}, {'name': 'chen-1', 'token': 'chen-1'}, {'name': 'bluebey-2', 'token': 'bluebey'}, {'name': 'waterfallshadow', 'token': 'WaterfallShadow'}, {'name': 'chop', 'token': 'Le Petit Prince'}, {'name': 'sintez-ico', 'token': 'sintez-ico'}, {'name': 'carlitos-el-mago', 'token': 'carloscarbonell'}, {'name': 'david-martinez-edgerunners', 'token': 'david-martinez-edgerunners'}, {'name': 'isabell-schulte-pviii-4-tiles-3-lr-5000-steps-style', 'token': 'isabell-schulte-p8-4tiles-3lr-5000s-style'}, {'name': 'guttestreker', 'token': 'guttestreker'}, {'name': 'ransom', 'token': 'ransom'}, {'name': 'museum-by-coop-himmelblau', 'token': 'coop himmelblau museum'}, {'name': 'coop-himmelblau', 'token': 'coop himmelblau'}, {'name': 'yesdelete', 'token': 'yesdelete'}, {'name': 'conway-pirate', 'token': 'conway'}, {'name': 'ilo-kunst', 'token': 'ilo-kunst'}, {'name': 'yilanov2', 'token': 'yilanov'}, {'name': 'dr-strange', 'token': 'dr-strange'}, {'name': 'hubris-oshri', 'token': 'Hubris'}, {'name': 'osaka-jyo', 'token': 'osaka-jyo'}, {'name': 'paolo-bonolis', 'token': 'paolo-bonolis'}, {'name': 'repeat', 'token': 'repeat'}, {'name': 'geggin', 'token': 'geggin'}, {'name': 'lex', 'token': 'lex'}, {'name': 'osaka-jyo2', 'token': 'osaka-jyo2'}, {'name': 'owl-house', 'token': 'owl-house'}, {'name': 'nazuna', 'token': 'nazuna'}, {'name': 'thorneworks', 'token': 'Thorneworks'}, {'name': 'kysa-v-style', 'token': 'kysa-v-style'}, {'name': 'senneca', 'token': 'Senneca'}, {'name': 'zero-suit-samus', 'token': 'zero-suit-samus'}, {'name': 'kanv1', 'token': 'KAN'}, {'name': 'dlooak', 'token': 'dlooak'}, {'name': 'wire-angels', 'token': 'wire-angels'}, {'name': 'mizkif', 'token': 'mizkif'}, {'name': 'brittney-williams-art', 'token': 'Brittney_Williams'}, {'name': 'wheelchair', 'token': 'wheelchair'}, {'name': 'yuji-himukai-style', 'token': 'Yuji Himukai-Style'}, {'name': 'cindlop', 'token': 'cindlop'}, {'name': 'sas-style', 'token': 'smooth-aesthetic-style'}, {'name': 'remert', 'token': 'Remert'}, {'name': 'alex-portugal', 'token': 'alejandro-portugal'}, {'name': 'explosions-cat', 'token': 'explosions-cat'}, {'name': 'onzpo', 'token': 'onzpo'}, {'name': 'eru-chitanda-casual', 'token': 'c-eru-chitanda'}, {'name': 'poring-ragnarok-online', 'token': 'poring-ro'}, {'name': 'cg-bearded-man', 'token': 'LH-Keeper'}, {'name': 'ba-shiroko', 'token': 'shiroko'}, {'name': 'at-wolf-boy-object', 'token': 'AT-Wolf-Boy-Object'}, {'name': 'fairytale', 'token': 'fAIrytale'}, {'name': 'kira-sensei', 'token': 'kira-sensei'}, {'name': 'kawaii-girl-plus-style', 'token': 'kawaii_girl'}, {'name': 'kawaii-girl-plus-object', 'token': 'kawaii_girl'}, {'name': 'boris-anderson', 'token': 'boris-anderson'}, {'name': 'medazzaland', 'token': 'edazzalan'}, {'name': 'duranduran', 'token': 'uranDura'}, {'name': 'crbart', 'token': 'crbart'}, {'name': 'happy-person12345', 'token': 'Happy-Person12345'}, {'name': 'fzk', 'token': 'fzk'}, {'name': 'rishusei-style', 'token': 'crishusei-style'}, {'name': 'felps', 'token': 'Felps'}, {'name': 'plen-ki-mun', 'token': 'plen-ki-mun'}, {'name': 'babs-bunny', 'token': 'babs_bunny'}, {'name': 'james-web-space-telescope', 'token': 'James-Web-Telescope'}, {'name': 'blue-haired-boy', 'token': 'Blue-Haired-Boy'}, {'name': '80s-anime-ai', 'token': '80s-anime-AI'}, {'name': 'spider-gwen', 'token': 'spider-gwen'}, {'name': 'takuji-kawano', 'token': 'takuji-kawano'}, {'name': 'fractal-temple-style', 'token': 'fractal-temple'}, {'name': 'sanguo-guanyu', 'token': 'sanguo-guanyu'}, {'name': 's1m-naoto-ohshima', 'token': 's1m-naoto-ohshima'}, {'name': 'kawaii-girl-plus-style-v1-1', 'token': 'kawaii'}, {'name': 'nathan-wyatt', 'token': 'Nathan-Wyatt'}, {'name': 'kasumin', 'token': 'kasumin'}, {'name': 'happy-person12345-assets', 'token': 'Happy-Person12345-assets'}, {'name': 'oleg-kuvaev', 'token': 'oleg-kuvaev'}, {'name': 'kanovt', 'token': 'anov'}, {'name': 'lphr-style', 'token': 'lphr-style'}, {'name': 'concept-art', 'token': 'concept-art'}, {'name': 'trust-support', 'token': 'trust'}, {'name': 'altyn-helmet', 'token': 'Altyn'}, {'name': '80s-anime-ai-being', 'token': 'anime-AI-being'}, {'name': 'baluchitherian', 'token': 'baluchiter'}, {'name': 'pineda-david', 'token': 'pineda-david'}, {'name': 'ohisashiburi-style', 'token': 'ohishashiburi-style'}, {'name': 'crb-portraits', 'token': 'crbportrait'}, {'name': 'i-love-chaos', 'token': 'chaos'}, {'name': 'alex-thumbnail-object-2000-steps', 'token': 'alex'}, {'name': '852style-girl', 'token': '852style-girl'}, {'name': 'nomad', 'token': 'nomad'}, {'name': 'new-priests', 'token': 'new-priest'}, {'name': 'liminalspaces', 'token': 'liminal image'}, {'name': 'aadhav-face', 'token': 'aadhav-face'}, {'name': 'jang-sung-rak-style', 'token': 'Jang-Sung-Rak-style'}, {'name': 'mattvidpro', 'token': 'mattvidpro'}, {'name': 'chungus-poodl-pet', 'token': 'poodl-chungus-big'}, {'name': 'liminal-spaces-2-0', 'token': 'iminal imag'}, {'name': 'crb-surrealz', 'token': 'crbsurreal'}, {'name': 'final-fantasy-logo', 'token': 'final-fantasy-logo'}, {'name': 'canadian-goose', 'token': 'canadian-goose'}, {'name': 'scratch-project', 'token': 'scratch-project'}, {'name': 'lazytown-stephanie', 'token': 'azytown-stephani'}, {'name': 'female-kpop-singer', 'token': 'female-kpop-star'}, {'name': 'aleyna-tilki', 'token': 'aleyna-tilki'}, {'name': 'other-mother', 'token': 'ther-mothe'}, {'name': 'beldam', 'token': 'elda'}, {'name': 'button-eyes', 'token': 'utton-eye'}, {'name': 'alisa', 'token': 'alisa-selezneva'}, {'name': 'im-poppy', 'token': 'm-popp'}, {'name': 'fractal-flame', 'token': 'fractal-flame'}, {'name': 'Exodus-Styling', 'token': 'Exouds-Style'}, {'name': '8sconception', 'token': '80s-car'}, {'name': 'christo-person', 'token': 'christo'}, {'name': 'slm', 'token': 'c-w388'}, {'name': 'meze-audio-elite-headphones', 'token': 'meze-elite'}, {'name': 'fox-purple', 'token': 'foxi-purple'}, {'name': 'roblox-avatar', 'token': 'roblox-avatar'}, {'name': 'toy-bonnie-plush', 'token': 'toy-bonnie-plush'}, {'name': 'alf', 'token': 'alf'}, {'name': 'wojak', 'token': 'oja'}, {'name': 'animalve3-1500seq', 'token': 'diodio'}, {'name': 'muxoyara', 'token': 'muxoyara'}, {'name': 'selezneva-alisa', 'token': 'selezneva-alisa'}, {'name': 'ayush-spider-spr', 'token': 'spr-mn'}, {'name': 'natasha-johnston', 'token': 'natasha-johnston'}, {'name': 'nard-style', 'token': 'nard'}, {'name': 'kirby', 'token': 'kirby'}, {'name': 'el-salvador-style-style', 'token': 'el-salvador-style'}, {'name': 'rahkshi-bionicle', 'token': 'rahkshi-bionicle'}, {'name': 'masyanya', 'token': 'masyanya'}, {'name': 'command-and-conquer-remastered-cameos', 'token': 'command_and_conquer_remastered_cameos'}, {'name': 'lucario', 'token': 'lucario'}, {'name': 'bruma', 'token': 'Bruma-the-cat'}, {'name': 'nissa-revane', 'token': 'nissa-revane'}, {'name': 'tamiyo', 'token': 'tamiyo'}, {'name': 'pascalsibertin', 'token': 'pascalsibertin'}, {'name': 'chandra-nalaar', 'token': 'chandra-nalaar'}, {'name': 'sam-yang', 'token': 'sam-yang'}, {'name': 'kiora', 'token': 'kiora'}, {'name': 'wedding', 'token': 'wedding1'}, {'name': 'arwijn', 'token': 'rwij'}, {'name': 'gba-fe-class-cards', 'token': 'lasscar'}, {'name': 'painted-by-silver-of-999', 'token': 'cat-toy'}, {'name': 'painted-by-silver-of-999-2', 'token': 'girl-painted-by-silver-of-999'}, {'name': 'toyota-sera', 'token': 'toyota-sera'}, {'name': 'vraska', 'token': 'vraska'}, {'name': 'mystical-nature', 'token': ''}, {'name': 'cartoona-animals', 'token': 'cartoona-animals'}, {'name': 'amogus', 'token': 'amogus'}, {'name': 'kinda-sus', 'token': 'amogus'}, {'name': 'xuna', 'token': 'Xuna'}, {'name': 'pion-by-august-semionov', 'token': 'pion'}, {'name': 'rikiart', 'token': 'rick-art'}, {'name': 'jacqueline-the-unicorn', 'token': 'jacqueline'}, {'name': 'flaticon-lineal-color', 'token': 'flaticon-lineal-color'}, {'name': 'test-epson', 'token': 'epson-branch'}, {'name': 'orientalist-art', 'token': 'orientalist-art'}, {'name': 'ki', 'token': 'ki-mars'}, {'name': 'fnf-boyfriend', 'token': 'fnf-boyfriend'}, {'name': 'phoenix-01', 'token': 'phoenix-style'}, {'name': 'society-finch', 'token': 'society-finch'}, {'name': 'rikiboy-art', 'token': 'Rikiboy-Art'}, {'name': 'flatic', 'token': 'flat-ct'}, {'name': 'logo-with-face-on-shield', 'token': 'logo-huizhang'}, {'name': 'elspeth-tirel', 'token': 'elspeth-tirel'}, {'name': 'zero', 'token': 'zero'}, {'name': 'willy-hd', 'token': 'willy_character'}, {'name': 'kaya-ghost-assasin', 'token': 'kaya-ghost-assasin'}, {'name': 'starhavenmachinegods', 'token': 'StarhavenMachineGods'}, {'name': 'namine-ritsu', 'token': 'namine-ritsu'}, {'name': 'mildemelwe-style', 'token': 'mildemelwe'}, {'name': 'nahiri', 'token': 'nahiri'}, {'name': 'ghost-style', 'token': 'ghost'}, {'name': 'arq-render', 'token': 'arq-style'}, {'name': 'saheeli-rai', 'token': 'saheeli-rai'}, {'name': 'youpi2', 'token': 'youpi'}, {'name': 'youtooz-candy', 'token': 'youtooz-candy'}, {'name': 'beholder', 'token': 'beholder'}, {'name': 'progress-chip', 'token': 'progress-chip'}, {'name': 'lofa', 'token': 'lofa'}, {'name': 'huatli', 'token': 'huatli'}, {'name': 'vivien-reid', 'token': 'vivien-reid'}, {'name': 'wedding-HandPainted', 'token': ''}, {'name': 'sims-2-portrait', 'token': 'sims2-portrait'}, {'name': 'flag-ussr', 'token': 'flag-ussr'}, {'name': 'cortana', 'token': 'cortana'}, {'name': 'azura-from-vibrant-venture', 'token': 'azura'}, {'name': 'liliana-vess', 'token': 'liliana-vess'}, {'name': 'dreamy-painting', 'token': 'dreamy-painting'}, {'name': 'munch-leaks-style', 'token': 'munch-leaks-style'}, {'name': 'gta5-artwork', 'token': 'gta5-artwork'}, {'name': 'xioboma', 'token': 'xi-obama'}, {'name': 'ashiok', 'token': 'ashiok'}, {'name': 'Aflac-duck', 'token': 'aflac duck'}, {'name': 'toho-pixel', 'token': 'toho-pixel'}, {'name': 'alicebeta', 'token': 'Alice-style'}, {'name': 'cute-game-style', 'token': 'cute-game-style'}, {'name': 'a-yakimova', 'token': 'a-yakimova'}, {'name': 'anime-background-style', 'token': 'anime-background-style'}, {'name': 'uliana-kudinova', 'token': 'liana-kudinov'}, {'name': 'msg', 'token': 'MSG69'}, {'name': 'gio', 'token': 'gio-single'}, {'name': 'smooth-pencils', 'token': ''}, {'name': 'pintu', 'token': 'pintu-dog'}, {'name': 'marty6', 'token': 'marty6'}, {'name': 'marty', 'token': 'marty'}, {'name': 'xi', 'token': 'JinpingXi'}, {'name': 'captainkirb', 'token': 'captainkirb'}, {'name': 'urivoldemort', 'token': 'uriboldemort'}, {'name': 'anime-background-style-v2', 'token': 'anime-background-style-v2'}, {'name': 'hk-peach', 'token': 'hk-peach'}, {'name': 'hk-goldbuddha', 'token': 'hk-goldbuddha'}, {'name': 'edgerunners-style', 'token': 'edgerunners-style-av'}, {'name': 'warhammer-40k-drawing-style', 'token': 'warhammer40k-drawing-style'}, {'name': 'hk-opencamera', 'token': 'hk-opencamera'}, {'name': 'hk-breakfast', 'token': 'hk-breakfast'}, {'name': 'iridescent-illustration-style', 'token': 'iridescent-illustration-style'}, {'name': 'edgerunners-style-v2', 'token': 'edgerunners-style-av-v2'}, {'name': 'leif-jones', 'token': 'leif-jones'}, {'name': 'hk-buses', 'token': 'hk-buses'}, {'name': 'hk-goldenlantern', 'token': 'hk-goldenlantern'}, {'name': 'hk-hkisland', 'token': 'hk-hkisland'}, {'name': 'hk-leaves', 'token': ''}, {'name': 'hk-oldcamera', 'token': 'hk-oldcamera'}, {'name': 'frank-frazetta', 'token': 'rank franzett'}, {'name': 'obama-based-on-xi', 'token': 'obama> <JinpingXi'}, {'name': 'hk-vintage', 'token': ''}, {'name': 'degods', 'token': 'degods'}, {'name': 'dishonored-portrait-styles', 'token': 'portrait-style-dishonored'}, {'name': 'manga-style', 'token': 'manga'}, {'name': 'degodsheavy', 'token': 'degods-heavy'}, {'name': 'teferi', 'token': 'teferi'}, {'name': 'car-toy-rk', 'token': 'car-toy'}, {'name': 'anders-zorn', 'token': 'anders-zorn'}, {'name': 'rayne-weynolds', 'token': 'rayne-weynolds'}, {'name': 'hk-bamboo', 'token': 'hk-bamboo'}, {'name': 'hk-betweenislands', 'token': 'hk-betweenislands'}, {'name': 'hk-bicycle', 'token': 'hk-bicycle'}, {'name': 'hk-blackandwhite', 'token': 'hk-blackandwhite'}, {'name': 'pjablonski-style', 'token': 'pjablonski-style'}, {'name': 'hk-market', 'token': 'hk-market'}, {'name': 'hk-phonevax', 'token': 'hk-phonevax'}, {'name': 'hk-clouds', 'token': 'hk-cloud'}, {'name': 'hk-streetpeople', 'token': 'hk-streetpeople'}, {'name': 'iridescent-photo-style', 'token': 'iridescent-photo-style'}, {'name': 'color-page', 'token': 'coloring-page'}, {'name': 'hoi4-leaders', 'token': 'HOI4-Leader'}, {'name': 'franz-unterberger', 'token': 'franz-unterberger'}, {'name': 'angus-mcbride-style', 'token': 'angus-mcbride-style'}, {'name': 'happy-chaos', 'token': 'happychaos'}, {'name': 'gt-color-paint-2', 'token': 'my-color-paint-GT'}, {'name': 'smurf-style', 'token': 'smurfy'}, {'name': 'coraline', 'token': 'coraline'}, {'name': 'terraria-style', 'token': 'terr-sty'}, {'name': 'ettblackteapot', 'token': 'my-teapot'}, {'name': 'gibasachan-v0.1', 'token': 'gibasachan'}, {'name': 'kodakvision500t', 'token': 'kodakvision_500T'}, {'name': 'obama-based-on-xi', 'token': 'obama'}, {'name': 'obama-self-2', 'token': 'Obama'}, {'name': 'bob-dobbs', 'token': 'bob'}, {'name': 'ahx-model-1', 'token': 'ivan-stripes'}, {'name': 'ahx-model-2', 'token': 'artist'}, {'name': 'beetlejuice-cartoon-style', 'token': 'beetlejuice-cartoon'}, {'name': 'pokemon-modern-artwork', 'token': 'pkmn-modern'}, {'name': 'pokemon-classic-artwork', 'token': 'pkmn-classic'}, {'name': 'pokemon-gens-1-to-8', 'token': 'pkmn-galar'}, {'name': 'pokemon-rgby-sprite', 'token': 'pkmn-rgby'}, {'name': 'max-twain', 'token': 'max-twain'}, {'name': 'ihylc', 'token': 'ihylc'}, {'name': 'test-man', 'token': 'Test-man'}, {'name': 'tron-style', 'token': 'tron-style>'}, {'name': 'dulls', 'token': 'dulls-avatar'}, {'name': 'vie-proceres', 'token': 'vie-proceres'}, {'name': 'dovin-baan', 'token': 'dovin-baan'}, {'name': 'polki-jewellery', 'token': 'ccess to model sd-concepts-library/polki-jewellery is restricted and you are not in the authorized list. Visit https://huggingface.co/sd-concepts-library/polki-jewellery to ask for access'}, {'name': 'dog2', 'token': 'ccess to model sd-concepts-library/dog2 is restricted and you are not in the authorized list. Visit https://huggingface.co/sd-concepts-library/dog2 to ask for access'}, {'name': 'caitlin-fairchild-character-gen13-comics', 'token': 'Caitlin-Fairchild'}, {'name': 'ugly-sonic', 'token': 'ugly-sonic'}, {'name': 'utopia-beer-mat', 'token': 'utopia-beer-mat'}, {'name': 'old-brno', 'token': 'old-brno'}, {'name': 'moka-pot', 'token': 'moka-pot'}, {'name': 'brno-trenck', 'token': 'brno-trenck'}, {'name': 'brno-tram', 'token': 'brno-tram'}, {'name': 'brno-obasa', 'token': 'brno-obasa'}, {'name': 'brno-night', 'token': 'brno-night'}, {'name': 'brno-dorm', 'token': 'brno-dorm'}, {'name': 'brno-busstop', 'token': 'brno-busstop'}, {'name': 'twitch-league-of-legends', 'token': 'twitch-lol'}, {'name': 'fp-shop2', 'token': 'fp-shop2'}, {'name': 'fp-shop1', 'token': 'fp-shop1'}, {'name': 'fp-content-b', 'token': 'fp-content-b'}, {'name': 'fp-content-a', 'token': 'fp-content-a'}, {'name': 'fp-city', 'token': 'fp-city'}, {'name': 'brno-city-results', 'token': 'brno-city-results'}, {'name': 'brno-city', 'token': 'brno-city'}, {'name': 'brno-chair-results', 'token': 'brno-chair-results'}, {'name': 'brno-chair', 'token': 'brno-chair'}, {'name': 'manga-char-nov-23', 'token': 'char-nov23'}, {'name': 'manga-nov-23', 'token': 'manga-characters-nov23'}, {'name': 'yellow-cockatiel-parrot', 'token': 'rosa-popugai'}, {'name': 'dreams', 'token': 'meeg'}, {'name': 'alberto-montt', 'token': 'AlbertoMontt'}, {'name': 'tooth-wu', 'token': 'tooth-wu'}, {'name': 'filename-2', 'token': 'filename2'}, {'name': 'iridescent-photo-style', 'token': 'iridescent-photo-style'}, {'name': 'bored-ape-textual-inversion', 'token': 'bored_ape'}, {'name': 'ghibli-face', 'token': 'ghibli-face'}, {'name': 'yoshimurachi', 'token': 'yoshi-san'}, {'name': 'jm-bergling-monogram', 'token': 'JM-Bergling-monogram'}, {'name': '4tnght', 'token': '4tNGHT'}, {'name': 'dancing-cactus', 'token': 'dancing-cactus'}, {'name': 'yolandi-visser', 'token': 'olandi-visse'}, {'name': 'zizigooloo', 'token': 'zizigooloo'}, {'name': 'princess-knight-art', 'token': 'princess-knight'}, {'name': 'belle-delphine', 'token': 'elle-delphin'}, {'name': 'cancer_style', 'token': 'cancer_style'}, {'name': 'trypophobia', 'token': 'rypophobi'}, {'name': 'incendegris-grey', 'token': 'incendegris-grey'}, {'name': 'fairy-tale-painting-style', 'token': 'fairy-tale-painting-style'}, {'name': 'arcimboldo-style', 'token': 'arcimboldo-style'}, {'name': 'xidiversity', 'token': 'JinpingXi'}, {'name': 'obama-based-on-xi', 'token': 'obama'}, {'name': 'zero-bottle', 'token': 'zero-bottle'}, {'name': 'victor-narm', 'token': 'victor-narm'}, {'name': 'supitcha-mask', 'token': 'supitcha-mask'}, {'name': 'smarties', 'token': 'smarties'}, {'name': 'rico-face', 'token': 'rico-face'}, {'name': 'rex-deno', 'token': 'rex-deno'}, {'name': 'abby-face', 'token': 'abby-face'}, {'name': 'nic-papercuts', 'token': 'nic-papercuts'}]
ImageNet_classes = {'ATM': 480, 'Acinonyx jubatus': 293, 'Aepyceros melampus': 352, 'Afghan': 160, 'Afghan hound': 160, 'African chameleon': 47, 'African crocodile': 49, 'African elephant': 386, 'African gray': 87, 'African grey': 87, 'African hunting dog': 275, 'Ailuropoda melanoleuca': 388, 'Ailurus fulgens': 387, 'Airedale': 191, 'Airedale terrier': 191, 'Alaska crab': 121, 'Alaska king crab': 121, 'Alaskan king crab': 121, 'Alaskan malamute': 249, 'Alligator mississipiensis': 50, 'Alopex lagopus': 279, 'Ambystoma maculatum': 28, 'Ambystoma mexicanum': 29, 'American Staffordshire terrier': 180, 'American alligator': 50, 'American black bear': 295, 'American chameleon': 40, 'American coot': 137, 'American eagle': 22, 'American egret': 132, 'American lobster': 122, 'American pit bull terrier': 180, 'American robin': 15, 'Angora': 332, 'Angora rabbit': 332, 'Anolis carolinensis': 40, 'Appenzeller': 240, 'Aptenodytes patagonica': 145, 'Arabian camel': 354, 'Aramus pictus': 135, 'Aranea diademata': 74, 'Araneus cavaticus': 73, 'Arctic fox': 279, 'Arctic wolf': 270, 'Arenaria interpres': 139, 'Argiope aurantia': 72, 'Ascaphus trui': 32, 'Asiatic buffalo': 346, 'Ateles geoffroyi': 381, 'Australian terrier': 193, 'Band Aid': 419, 'Bedlington terrier': 181, 'Bernese mountain dog': 239, 'Biro': 418, 'Blenheim spaniel': 156, 'Bonasa umbellus': 82, 'Border collie': 232, 'Border terrier': 182, 'Boston bull': 195, 'Boston terrier': 195, 'Bouvier des Flandres': 233, 'Bouviers des Flandres': 233, 'Brabancon griffon': 262, 'Bradypus tridactylus': 364, 'Brittany spaniel': 215, 'Bubalus bubalis': 346, 'CD player': 485, 'CRO': 688, 'CRT screen': 782, 'Cacatua galerita': 89, 'Camelus dromedarius': 354, 'Cancer irroratus': 119, 'Cancer magister': 118, 'Canis dingo': 273, 'Canis latrans': 272, 'Canis lupus': 269, 'Canis lupus tundrarum': 270, 'Canis niger': 271, 'Canis rufus': 271, 'Cape hunting dog': 275, 'Capra ibex': 350, 'Carassius auratus': 1, 'Carcharodon carcharias': 2, 'Cardigan': 264, 'Cardigan Welsh corgi': 264, 'Carduelis carduelis': 11, 'Caretta caretta': 33, 'Carphophis amoenus': 52, 'Carpodacus mexicanus': 12, 'Cavia cobaya': 338, 'Cebus capucinus': 378, 'Cerastes cornutus': 66, 'Chamaeleo chamaeleon': 47, 'Chesapeake Bay retriever': 209, 'Chihuahua': 151, 'Chlamydosaurus kingi': 43, 'Christmas stocking': 496, 'Ciconia ciconia': 127, 'Ciconia nigra': 128, 'Constrictor constrictor': 61, 'Crock Pot': 521, 'Crocodylus niloticus': 49, 'Crotalus adamanteus': 67, 'Crotalus cerastes': 68, 'Cuon alpinus': 274, 'Cygnus atratus': 100, 'Cypripedium calceolus': 986, 'Cypripedium parviflorum': 986, 'Danaus plexippus': 323, 'Dandie Dinmont': 194, 'Dandie Dinmont terrier': 194, 'Dermochelys coriacea': 34, 'Doberman': 236, 'Doberman pinscher': 236, 'Dugong dugon': 149, 'Dungeness crab': 118, 'Dutch oven': 544, 'Egretta albus': 132, 'Egretta caerulea': 131, 'Egyptian cat': 285, 'Elephas maximus': 385, 'English cocker spaniel': 219, 'English foxhound': 167, 'English setter': 212, 'English springer': 217, 'English springer spaniel': 217, 'EntleBucher': 241, 'Erolia alpina': 140, 'Erythrocebus patas': 371, 'Eschrichtius gibbosus': 147, 'Eschrichtius robustus': 147, 'Eskimo dog': 248, 'Euarctos americanus': 295, 'European fire salamander': 25, 'European gallinule': 136, 'Felis concolor': 286, 'Felis onca': 290, 'French bulldog': 245, 'French horn': 566, 'French loaf': 930, 'Fringilla montifringilla': 10, 'Fulica americana': 137, 'Galeocerdo cuvieri': 3, 'German police dog': 235, 'German shepherd': 235, 'German shepherd dog': 235, 'German short-haired pointer': 210, 'Gila monster': 45, 'Gordon setter': 214, 'Gorilla gorilla': 366, 'Granny Smith': 948, 'Great Dane': 246, 'Great Pyrenees': 257, 'Greater Swiss Mountain dog': 238, 'Grifola frondosa': 996, 'Haliaeetus leucocephalus': 22, 'Heloderma suspectum': 45, 'Hippopotamus amphibius': 344, 'Holocanthus tricolor': 392, 'Homarus americanus': 122, 'Hungarian pointer': 211, 'Hylobates lar': 368, 'Hylobates syndactylus': 369, 'Hypsiglena torquata': 60, 'Ibizan Podenco': 173, 'Ibizan hound': 173, 'Iguana iguana': 39, 'Indian cobra': 63, 'Indian elephant': 385, 'Indri brevicaudatus': 384, 'Indri indri': 384, 'Irish setter': 213, 'Irish terrier': 184, 'Irish water spaniel': 221, 'Irish wolfhound': 170, 'Italian greyhound': 171, 'Japanese spaniel': 152, 'Kakatoe galerita': 89, 'Kerry blue terrier': 183, 'Komodo dragon': 48, 'Komodo lizard': 48, 'Labrador retriever': 208, 'Lacerta viridis': 46, 'Lakeland terrier': 189, 'Latrodectus mactans': 75, 'Lemur catta': 383, 'Leonberg': 255, 'Lepisosteus osseus': 395, 'Lhasa': 204, 'Lhasa apso': 204, 'Loafer': 630, 'Loxodonta africana': 386, 'Lycaon pictus': 275, 'Madagascar cat': 383, 'Maine lobster': 122, 'Maltese': 153, 'Maltese dog': 153, 'Maltese terrier': 153, 'Melursus ursinus': 297, 'Mergus serrator': 98, 'Mexican hairless': 268, 'Model T': 661, 'Mustela nigripes': 359, 'Mustela putorius': 358, 'Naja naja': 63, 'Nasalis larvatus': 376, 'Newfoundland': 256, 'Newfoundland dog': 256, 'Nile crocodile': 49, 'Norfolk terrier': 185, 'Northern lobster': 122, 'Norwegian elkhound': 174, 'Norwich terrier': 186, 'Old English sheepdog': 229, 'Oncorhynchus kisutch': 391, 'Orcinus orca': 148, 'Ornithorhynchus anatinus': 103, 'Ovis canadensis': 349, 'Pan troglodytes': 367, 'Panthera leo': 291, 'Panthera onca': 290, 'Panthera pardus': 288, 'Panthera tigris': 292, 'Panthera uncia': 289, 'Paralithodes camtschatica': 121, 'Passerina cyanea': 14, 'Peke': 154, 'Pekinese': 154, 'Pekingese': 154, 'Pembroke': 263, 'Pembroke Welsh corgi': 263, 'Persian cat': 283, 'Petri dish': 712, 'Phalangium opilio': 70, 'Phascolarctos cinereus': 105, 'Polaroid Land camera': 732, 'Polaroid camera': 732, 'Polyporus frondosus': 996, 'Pomeranian': 259, 'Pongo pygmaeus': 365, 'Porphyrio porphyrio': 136, 'Psittacus erithacus': 87, 'Python sebae': 62, 'R.V.': 757, 'RV': 757, 'Rana catesbeiana': 30, 'Rhodesian ridgeback': 159, 'Rocky Mountain bighorn': 349, 'Rocky Mountain sheep': 349, 'Rottweiler': 234, 'Russian wolfhound': 169, 'Saimiri sciureus': 382, 'Saint Bernard': 247, 'Salamandra salamandra': 25, 'Saluki': 176, 'Samoyed': 258, 'Samoyede': 258, 'Sciurus niger': 335, 'Scotch terrier': 199, 'Scottie': 199, 'Scottish deerhound': 177, 'Scottish terrier': 199, 'Sealyham': 190, 'Sealyham terrier': 190, 'Shetland': 230, 'Shetland sheep dog': 230, 'Shetland sheepdog': 230, 'Shih-Tzu': 155, 'Siamese': 284, 'Siamese cat': 284, 'Siberian husky': 250, 'St Bernard': 247, 'Staffordshire bull terrier': 179, 'Staffordshire bullterrier': 179, 'Staffordshire terrier': 180, 'Strix nebulosa': 24, 'Struthio camelus': 9, 'Sus scrofa': 342, 'Sussex spaniel': 220, 'Sydney silky': 201, 'Symphalangus syndactylus': 369, 'T-shirt': 610, 'Thalarctos maritimus': 296, 'Tibetan mastiff': 244, 'Tibetan terrier': 200, 'Tinca tinca': 0, 'Tringa totanus': 141, 'Triturus vulgaris': 26, 'Turdus migratorius': 15, 'U-boat': 833, 'Urocyon cinereoargenteus': 280, 'Ursus Maritimus': 296, 'Ursus americanus': 295, 'Ursus arctos': 294, 'Ursus ursinus': 297, 'Varanus komodoensis': 48, 'Virginia fence': 912, 'Vulpes macrotis': 278, 'Vulpes vulpes': 277, 'Walker foxhound': 166, 'Walker hound': 166, 'Weimaraner': 178, 'Welsh springer spaniel': 218, 'West Highland white terrier': 203, 'Windsor tie': 906, 'Yorkshire terrier': 187, 'abacus': 398, 'abaya': 399, 'academic gown': 400, 'academic robe': 400, 'accordion': 401, 'acorn': 988, 'acorn squash': 941, 'acoustic guitar': 402, 'admiral': 321, 'aegis': 461, 'affenpinscher': 252, 'agama': 42, 'agaric': 992, 'ai': 364, 'aircraft carrier': 403, 'airliner': 404, 'airship': 405, 'albatross': 146, 'all-terrain bike': 671, 'alligator lizard': 44, 'alp': 970, 'alsatian': 235, 'altar': 406, 'ambulance': 407, 'amphibian': 408, 'amphibious vehicle': 408, 'analog clock': 409, 'ananas': 953, 'anemone': 108, 'anemone fish': 393, 'anole': 40, 'ant': 310, 'anteater': 102, 'apiary': 410, 'apron': 411, 'armadillo': 363, 'armored combat vehicle': 847, 'armoured combat vehicle': 847, 'army tank': 847, 'artichoke': 944, 'articulated lorry': 867, 'ash bin': 412, 'ash-bin': 412, 'ashbin': 412, 'ashcan': 412, 'assault gun': 413, 'assault rifle': 413, 'attack aircraft carrier': 403, 'automated teller': 480, 'automated teller machine': 480, 'automatic teller': 480, 'automatic teller machine': 480, 'automatic washer': 897, 'axolotl': 29, 'baboon': 372, 'back pack': 414, 'backpack': 414, 'badger': 362, 'bagel': 931, 'bakehouse': 415, 'bakery': 415, 'bakeshop': 415, 'balance beam': 416, 'bald eagle': 22, 'balloon': 417, 'ballpen': 418, 'ballplayer': 981, 'ballpoint': 418, 'ballpoint pen': 418, 'balusters': 421, 'balustrade': 421, 'banana': 954, 'bandeau': 459, 'banded gecko': 38, 'banister': 421, 'banjo': 420, 'bannister': 421, 'barbell': 422, 'barber chair': 423, 'barbershop': 424, 'barn': 425, 'barn spider': 73, 'barometer': 426, 'barracouta': 389, 'barrel': 427, 'barrow': 428, 'bars': 702, 'baseball': 429, 'baseball player': 981, 'basenji': 253, 'basketball': 430, 'basset': 161, 'basset hound': 161, 'bassinet': 431, 'bassoon': 432, 'bath': 435, 'bath towel': 434, 'bathing cap': 433, 'bathing trunks': 842, 'bathing tub': 435, 'bathroom tissue': 999, 'bathtub': 435, 'beach waggon': 436, 'beach wagon': 436, 'beacon': 437, 'beacon light': 437, 'beagle': 162, 'beaker': 438, 'beam': 416, 'bear cat': 387, 'bearskin': 439, 'beaver': 337, 'bee': 309, 'bee eater': 92, 'bee house': 410, 'beer bottle': 440, 'beer glass': 441, 'beigel': 931, 'bell': 494, 'bell cot': 442, 'bell cote': 442, 'bell pepper': 945, 'bell toad': 32, 'bib': 443, 'bicycle-built-for-two': 444, 'bighorn': 349, 'bighorn sheep': 349, 'bikini': 445, 'billfish': 395, 'billfold': 893, 'billiard table': 736, 'binder': 446, 'binoculars': 447, 'birdhouse': 448, 'bison': 347, 'bittern': 133, 'black Maria': 734, 'black and gold garden spider': 72, 'black bear': 295, 'black grouse': 80, 'black stork': 128, 'black swan': 100, 'black widow': 75, 'black-and-tan coonhound': 165, 'black-footed ferret': 359, 'bloodhound': 163, 'blow drier': 589, 'blow dryer': 589, 'blower': 545, 'blowfish': 397, 'blue jack': 391, 'blue jean': 608, 'bluetick': 164, 'boa': 552, 'boa constrictor': 61, 'boar': 342, 'board': 532, 'boat paddle': 693, 'boathouse': 449, 'bob': 450, 'bobsled': 450, 'bobsleigh': 450, 'bobtail': 229, 'bola': 451, 'bola tie': 451, 'bolete': 997, 'bolo': 451, 'bolo tie': 451, 'bonnet': 452, 'book jacket': 921, 'bookcase': 453, 'bookshop': 454, 'bookstall': 454, 'bookstore': 454, 'borzoi': 169, 'bottle screw': 512, 'bottlecap': 455, 'bow': 456, 'bow tie': 457, 'bow-tie': 457, 'bowtie': 457, 'box tortoise': 37, 'box turtle': 37, 'boxer': 242, 'bra': 459, 'brain coral': 109, 'brambling': 10, 'brass': 458, 'brassiere': 459, 'breakwater': 460, 'breastplate': 461, 'briard': 226, 'bridegroom': 982, 'broccoli': 937, 'broom': 462, 'brown bear': 294, 'bruin': 294, 'brush kangaroo': 104, 'brush wolf': 272, 'bubble': 971, 'bucket': 463, 'buckeye': 990, 'buckle': 464, 'buckler': 787, 'bulbul': 16, 'bull mastiff': 243, 'bullet': 466, 'bullet train': 466, 'bulletproof vest': 465, 'bullfrog': 30, 'bulwark': 460, 'burrito': 965, 'busby': 439, 'bustard': 138, 'butcher shop': 467, 'butternut squash': 942, 'cab': 468, 'cabbage butterfly': 324, 'cairn': 192, 'cairn terrier': 192, 'caldron': 469, 'can opener': 473, 'candle': 470, 'candy store': 509, 'cannon': 471, 'canoe': 472, 'capitulum': 998, 'capuchin': 378, 'car mirror': 475, 'car wheel': 479, 'carabid beetle': 302, 'carbonara': 959, 'cardigan': 474, 'cardoon': 946, 'carousel': 476, "carpenter's kit": 477, "carpenter's plane": 726, 'carriage': 705, 'carriage dog': 251, 'carrier': 403, 'carrion fungus': 994, 'carrousel': 476, 'carton': 478, 'cash dispenser': 480, 'cash machine': 480, 'cask': 427, 'cassette': 481, 'cassette player': 482, 'castle': 483, 'cat bear': 387, 'catamaran': 484, 'catamount': 287, 'cathode-ray oscilloscope': 688, 'cauldron': 469, 'cauliflower': 938, 'cell': 487, 'cello': 486, 'cellphone': 487, 'cellular phone': 487, 'cellular telephone': 487, 'centipede': 79, 'cerastes': 66, 'chain': 488, 'chain armor': 490, 'chain armour': 490, 'chain mail': 490, 'chain saw': 491, 'chainlink fence': 489, 'chainsaw': 491, 'chambered nautilus': 117, 'cheeseburger': 933, 'cheetah': 293, 'chest': 492, 'chetah': 293, 'chickadee': 19, 'chiffonier': 493, 'chime': 494, 'chimp': 367, 'chimpanzee': 367, 'china cabinet': 495, 'china closet': 495, 'chiton': 116, 'chocolate sauce': 960, 'chocolate syrup': 960, 'chopper': 499, 'chow': 260, 'chow chow': 260, 'chrysanthemum dog': 200, 'chrysomelid': 304, 'church': 497, 'church building': 497, 'chute': 701, 'cicada': 316, 'cicala': 316, 'cimarron': 349, 'cinema': 498, 'claw': 600, 'cleaver': 499, 'cliff': 972, 'cliff dwelling': 500, 'cloak': 501, 'clog': 502, 'closet': 894, 'clumber': 216, 'clumber spaniel': 216, 'coach': 705, 'coach dog': 251, 'coast': 978, 'coat-of-mail shell': 116, 'cock': 7, 'cocker': 219, 'cocker spaniel': 219, 'cockroach': 314, 'cocktail shaker': 503, 'coffee mug': 504, 'coffeepot': 505, 'coho': 391, 'coho salmon': 391, 'cohoe': 391, 'coil': 506, 'collie': 231, 'colobus': 375, 'colobus monkey': 375, 'combination lock': 507, 'comfort': 750, 'comforter': 750, 'comic book': 917, 'commode': 493, 'common iguana': 39, 'common newt': 26, 'computer keyboard': 508, 'computer mouse': 673, 'conch': 112, 'confectionary': 509, 'confectionery': 509, 'conker': 990, 'consomme': 925, 'container ship': 510, 'container vessel': 510, 'containership': 510, 'convertible': 511, 'coon bear': 388, 'coral fungus': 991, 'coral reef': 973, 'corkscrew': 512, 'corn': 987, 'cornet': 513, 'cot': 520, 'cottontail': 330, 'cottontail rabbit': 330, 'coucal': 91, 'cougar': 286, 'courgette': 939, 'cowboy boot': 514, 'cowboy hat': 515, 'coyote': 272, 'cradle': 516, 'crampfish': 5, 'crane': 517, 'crash helmet': 518, 'crate': 519, 'crawdad': 124, 'crawdaddy': 124, 'crawfish': 124, 'crayfish': 124, 'crib': 520, 'cricket': 312, 'crinoline': 601, 'croquet ball': 522, 'crossword': 918, 'crossword puzzle': 918, 'crutch': 523, 'cucumber': 943, 'cuirass': 524, 'cuke': 943, 'cup': 968, 'curly-coated retriever': 206, 'custard apple': 956, 'daddy longlegs': 70, 'daisy': 985, 'dalmatian': 251, 'dam': 525, 'damselfly': 320, 'dark glasses': 837, 'darning needle': 319, 'day bed': 831, 'deerhound': 177, 'denim': 608, 'desk': 526, 'desktop computer': 527, "devil's darning needle": 319, 'devilfish': 147, 'dhole': 274, 'dial phone': 528, 'dial telephone': 528, 'diamondback': 67, 'diamondback rattlesnake': 67, 'diaper': 529, 'digital clock': 530, 'digital watch': 531, 'dike': 525, 'dingo': 273, 'dining table': 532, 'dipper': 20, 'dirigible': 405, 'disc brake': 535, 'dish washer': 534, 'dishcloth': 533, 'dishrag': 533, 'dishwasher': 534, 'dishwashing machine': 534, 'disk brake': 535, 'dock': 536, 'dockage': 536, 'docking facility': 536, 'dog sled': 537, 'dog sleigh': 537, 'dogsled': 537, 'dome': 538, 'doormat': 539, 'dough': 961, 'dowitcher': 142, 'dragon lizard': 48, 'dragonfly': 319, 'drake': 97, 'drilling platform': 540, 'dromedary': 354, 'drop': 972, 'drop-off': 972, 'drum': 541, 'drumstick': 542, 'duck-billed platypus': 103, 'duckbill': 103, 'duckbilled platypus': 103, 'dugong': 149, 'dumbbell': 543, 'dung beetle': 305, 'dunlin': 140, 'dust cover': 921, 'dust jacket': 921, 'dust wrapper': 921, 'dustbin': 412, 'dustcart': 569, 'dyke': 525, 'ear': 998, 'earthstar': 995, 'eastern fox squirrel': 335, 'eatery': 762, 'eating house': 762, 'eating place': 762, 'echidna': 102, 'eel': 390, 'eft': 27, 'eggnog': 969, 'egis': 461, 'electric fan': 545, 'electric guitar': 546, 'electric locomotive': 547, 'electric ray': 5, 'electric switch': 844, 'electrical switch': 844, 'elkhound': 174, 'emmet': 310, 'entertainment center': 548, 'envelope': 549, 'espresso': 967, 'espresso maker': 550, 'essence': 711, 'estate car': 436, 'ewer': 725, 'face powder': 551, 'feather boa': 552, 'ferret': 359, 'fiddle': 889, 'fiddler crab': 120, 'field glasses': 447, 'fig': 952, 'file': 553, 'file cabinet': 553, 'filing cabinet': 553, 'fire engine': 555, 'fire screen': 556, 'fire truck': 555, 'fireboat': 554, 'fireguard': 556, 'fitch': 358, 'fixed disk': 592, 'flagpole': 557, 'flagstaff': 557, 'flamingo': 130, 'flat-coated retriever': 205, 'flattop': 403, 'flatworm': 110, 'flowerpot': 738, 'flute': 558, 'fly': 308, 'folding chair': 559, 'food market': 582, 'football helmet': 560, 'footstall': 708, 'foreland': 976, 'forklift': 561, 'foulmart': 358, 'foumart': 358, 'fountain': 562, 'fountain pen': 563, 'four-poster': 564, 'fox squirrel': 335, 'freight car': 565, 'frilled lizard': 43, 'frying pan': 567, 'frypan': 567, 'fur coat': 568, 'gar': 395, 'garbage can': 412, 'garbage truck': 569, 'garden cart': 428, 'garden spider': 74, 'garfish': 395, 'garpike': 395, 'garter snake': 57, 'gas helmet': 570, 'gas pump': 571, 'gasmask': 570, 'gasoline pump': 571, 'gazelle': 353, 'gazelle hound': 176, 'geta': 502, 'geyser': 974, 'giant lizard': 48, 'giant panda': 388, 'giant schnauzer': 197, 'gibbon': 368, 'glasshouse': 580, 'globe artichoke': 944, 'globefish': 397, 'go-kart': 573, 'goblet': 572, 'golden retriever': 207, 'goldfinch': 11, 'goldfish': 1, 'golf ball': 574, 'golf cart': 575, 'golfcart': 575, 'gondola': 576, 'gong': 577, 'goose': 99, 'gorilla': 366, 'gown': 578, 'grampus': 148, 'grand': 579, 'grand piano': 579, 'grass snake': 57, 'grasshopper': 311, 'gray fox': 280, 'gray whale': 147, 'gray wolf': 269, 'great gray owl': 24, 'great grey owl': 24, 'great white heron': 132, 'great white shark': 2, 'green lizard': 46, 'green mamba': 64, 'green snake': 55, 'greenhouse': 580, 'grey fox': 280, 'grey whale': 147, 'grey wolf': 269, 'grille': 581, 'grocery': 582, 'grocery store': 582, 'groenendael': 224, 'groin': 460, 'groom': 982, 'ground beetle': 302, 'groyne': 460, 'grunter': 341, 'guacamole': 924, 'guenon': 370, 'guenon monkey': 370, 'guillotine': 583, 'guinea pig': 338, 'gyromitra': 993, 'hack': 468, 'hair drier': 589, 'hair dryer': 589, 'hair slide': 584, 'hair spray': 585, 'half track': 586, 'hammer': 587, 'hammerhead': 4, 'hammerhead shark': 4, 'hamper': 588, 'hamster': 333, 'hand blower': 589, 'hand-held computer': 590, 'hand-held microcomputer': 590, 'handbasin': 896, 'handkerchief': 591, 'handrail': 421, 'hankey': 591, 'hankie': 591, 'hanky': 591, 'hard disc': 592, 'hard disk': 592, 'hare': 331, 'harmonica': 593, 'harp': 594, 'hartebeest': 351, 'harvester': 595, 'harvestman': 70, 'hatchet': 596, 'hautbois': 683, 'hautboy': 683, 'haversack': 414, 'hay': 958, 'head': 976, 'head cabbage': 936, 'headland': 976, 'hedgehog': 334, 'helix': 506, 'hen': 8, 'hen of the woods': 996, 'hen-of-the-woods': 996, 'hermit crab': 125, 'high bar': 602, 'hip': 989, 'hippo': 344, 'hippopotamus': 344, 'hockey puck': 746, 'hodometer': 685, 'hog': 341, 'hognose snake': 54, 'holothurian': 329, 'holster': 597, 'home theater': 598, 'home theatre': 598, 'honeycomb': 599, 'hook': 600, 'hoopskirt': 601, 'hopper': 311, 'horizontal bar': 602, 'horn': 566, 'hornbill': 93, 'horned asp': 66, 'horned rattlesnake': 68, 'horned viper': 66, 'horse cart': 603, 'horse chestnut': 990, 'horse-cart': 603, 'hot dog': 934, 'hot pot': 926, 'hotdog': 934, 'hotpot': 926, 'hourglass': 604, 'house finch': 12, 'howler': 379, 'howler monkey': 379, 'hummingbird': 94, 'hunting spider': 77, 'husky': 248, 'hussar monkey': 371, 'hyaena': 276, 'hyena': 276, 'hyena dog': 275, 'iPod': 605, 'ibex': 350, 'ice bear': 296, 'ice cream': 928, 'ice lolly': 929, 'icebox': 760, 'icecream': 928, 'igniter': 626, 'ignitor': 626, 'iguana': 39, 'impala': 352, 'indigo bird': 14, 'indigo bunting': 14, 'indigo finch': 14, 'indri': 384, 'indris': 384, 'internet site': 916, 'iron': 606, 'island dispenser': 571, 'isopod': 126, 'jacamar': 95, 'jack': 955, "jack-o'-lantern": 607, 'jackfruit': 955, 'jaguar': 290, 'jak': 955, 'jammies': 697, 'jay': 17, 'jean': 608, 'jeep': 609, 'jellyfish': 107, 'jersey': 610, 'jetty': 460, "jeweler's loupe": 633, 'jigsaw puzzle': 611, 'jinrikisha': 612, 'joystick': 613, "judge's robe": 400, 'junco': 13, 'kangaroo bear': 105, 'keeshond': 261, 'kelpie': 227, 'keypad': 508, 'killer': 148, 'killer whale': 148, 'kimono': 614, 'king crab': 121, 'king of beasts': 291, 'king penguin': 145, 'king snake': 56, 'kingsnake': 56, 'kit fox': 278, 'kite': 21, 'knapsack': 414, 'knee pad': 615, 'knot': 616, 'koala': 105, 'koala bear': 105, 'komondor': 228, 'kuvasz': 222, 'lab coat': 617, 'laboratory coat': 617, 'labyrinth': 646, 'lacewing': 318, 'lacewing fly': 318, 'ladle': 618, 'lady beetle': 301, 'ladybeetle': 301, 'ladybird': 301, 'ladybird beetle': 301, 'ladybug': 301, 'lakeshore': 975, 'lakeside': 975, 'lamp shade': 619, 'lampshade': 619, 'landrover': 609, 'langouste': 123, 'langur': 374, 'laptop': 620, 'laptop computer': 620, 'lavabo': 896, 'lawn cart': 428, 'lawn mower': 621, 'leaf beetle': 304, 'leafhopper': 317, 'leatherback': 34, 'leatherback turtle': 34, 'leathery turtle': 34, 'lemon': 951, 'lens cap': 622, 'lens cover': 622, 'leopard': 288, 'lesser panda': 387, 'letter box': 637, 'letter opener': 623, 'library': 624, 'lifeboat': 625, 'light': 626, 'lighter': 626, 'lighthouse': 437, 'limo': 627, 'limousine': 627, 'limpkin': 135, 'liner': 628, 'linnet': 12, 'lion': 291, 'lionfish': 396, 'lip rouge': 629, 'lipstick': 629, 'little blue heron': 131, 'llama': 355, 'loggerhead': 33, 'loggerhead turtle': 33, 'lollipop': 929, 'lolly': 929, 'long-horned beetle': 303, 'longicorn': 303, 'longicorn beetle': 303, 'lorikeet': 90, 'lotion': 631, 'loudspeaker': 632, 'loudspeaker system': 632, 'loupe': 633, 'lumbermill': 634, 'lycaenid': 326, 'lycaenid butterfly': 326, 'lynx': 287, 'macaque': 373, 'macaw': 88, 'magnetic compass': 635, 'magpie': 18, 'mail': 490, 'mailbag': 636, 'mailbox': 637, 'maillot': 639, 'malamute': 249, 'malemute': 249, 'malinois': 225, 'man-eater': 2, 'man-eating shark': 2, 'maned wolf': 271, 'manhole cover': 640, 'mantid': 315, 'mantis': 315, 'manufactured home': 660, 'maraca': 641, 'marimba': 642, 'market': 582, 'marmoset': 377, 'marmot': 336, 'marsh hen': 137, 'mashed potato': 935, 'mask': 643, 'matchstick': 644, 'maypole': 645, 'maze': 646, 'measuring cup': 647, 'meat cleaver': 499, 'meat loaf': 962, 'meat market': 467, 'meatloaf': 962, 'medicine cabinet': 648, 'medicine chest': 648, 'meerkat': 299, 'megalith': 649, 'megalithic structure': 649, 'membranophone': 541, 'memorial tablet': 458, 'menu': 922, 'merry-go-round': 476, 'microphone': 650, 'microwave': 651, 'microwave oven': 651, 'mierkat': 299, 'mike': 650, 'mileometer': 685, 'military plane': 895, 'military uniform': 652, 'milk can': 653, 'milkweed butterfly': 323, 'milometer': 685, 'mini': 655, 'miniature pinscher': 237, 'miniature poodle': 266, 'miniature schnauzer': 196, 'minibus': 654, 'miniskirt': 655, 'minivan': 656, 'mink': 357, 'missile': 744, 'mitten': 658, 'mixing bowl': 659, 'mobile home': 660, 'mobile phone': 487, 'modem': 662, 'mole': 460, 'mollymawk': 146, 'monarch': 323, 'monarch butterfly': 323, 'monastery': 663, 'mongoose': 298, 'monitor': 664, 'monkey dog': 252, 'monkey pinscher': 252, 'monocycle': 880, 'mop': 840, 'moped': 665, 'mortar': 666, 'mortarboard': 667, 'mosque': 668, 'mosquito hawk': 319, 'mosquito net': 669, 'motor scooter': 670, 'mountain bike': 671, 'mountain lion': 286, 'mountain tent': 672, 'mouse': 673, 'mousetrap': 674, 'mouth harp': 593, 'mouth organ': 593, 'movie house': 498, 'movie theater': 498, 'movie theatre': 498, 'moving van': 675, 'mower': 621, 'mud hen': 137, 'mud puppy': 29, 'mud turtle': 35, 'mushroom': 947, 'muzzle': 676, 'nail': 677, 'napkin': 529, 'nappy': 529, 'native bear': 105, 'nautilus': 117, 'neck brace': 678, 'necklace': 679, 'nematode': 111, 'nematode worm': 111, 'night snake': 60, 'nipple': 680, 'notebook': 681, 'notebook computer': 681, 'notecase': 893, 'nudibranch': 115, 'numbfish': 5, 'nursery': 580, 'obelisk': 682, 'oboe': 683, 'ocarina': 684, 'ocean liner': 628, 'odometer': 685, 'off-roader': 671, 'offshore rig': 540, 'oil filter': 686, 'one-armed bandit': 800, 'opera glasses': 447, 'orang': 365, 'orange': 950, 'orangutan': 365, 'orangutang': 365, 'orca': 148, 'organ': 687, 'oscilloscope': 688, 'ostrich': 9, 'otter': 360, 'otter hound': 175, 'otterhound': 175, 'ounce': 289, 'overskirt': 689, 'ox': 345, 'oxcart': 690, 'oxygen mask': 691, 'oyster catcher': 143, 'oystercatcher': 143, 'packet': 692, 'packsack': 414, 'paddle': 693, 'paddle wheel': 694, 'paddlewheel': 694, 'paddy wagon': 734, 'padlock': 695, 'pail': 463, 'paintbrush': 696, 'painter': 286, 'pajama': 697, 'palace': 698, 'paling': 716, 'panda': 388, 'panda bear': 388, 'pandean pipe': 699, 'panpipe': 699, 'panther': 290, 'paper knife': 623, 'paper towel': 700, 'paperknife': 623, 'papillon': 157, 'parachute': 701, 'parallel bars': 702, 'park bench': 703, 'parking meter': 704, 'partridge': 86, 'passenger car': 705, 'patas': 371, 'patio': 706, 'patrol wagon': 734, 'patten': 502, 'pay-phone': 707, 'pay-station': 707, 'peacock': 84, 'pearly nautilus': 117, 'pedestal': 708, 'pelican': 144, 'pencil box': 709, 'pencil case': 709, 'pencil eraser': 767, 'pencil sharpener': 710, 'penny bank': 719, 'perfume': 711, 'petrol pump': 571, 'pharos': 437, 'photocopier': 713, 'piano accordion': 401, 'pick': 714, 'pickelhaube': 715, 'picket fence': 716, 'pickup': 717, 'pickup truck': 717, 'picture palace': 498, 'pier': 718, 'pig': 341, 'pigboat': 833, 'piggy bank': 719, 'pill bottle': 720, 'pillow': 721, 'pineapple': 953, 'ping-pong ball': 722, 'pinwheel': 723, 'pipe organ': 687, 'pirate': 724, 'pirate ship': 724, 'pismire': 310, 'pit bull terrier': 180, 'pitcher': 725, 'pizza': 963, 'pizza pie': 963, "pj's": 697, 'plane': 726, 'planetarium': 727, 'plaque': 458, 'plastic bag': 728, 'plate': 923, 'plate rack': 729, 'platyhelminth': 110, 'platypus': 103, 'plectron': 714, 'plectrum': 714, 'plinth': 708, 'plough': 730, 'plow': 730, "plumber's helper": 731, 'plunger': 731, 'pocketbook': 893, 'poke bonnet': 452, 'polar bear': 296, 'pole': 733, 'polecat': 361, 'police van': 734, 'police wagon': 734, 'polyplacophore': 116, 'pomegranate': 957, 'poncho': 735, 'pool table': 736, 'pop bottle': 737, 'popsicle': 929, 'porcupine': 334, 'postbag': 636, 'pot': 738, 'potpie': 964, "potter's wheel": 739, 'power drill': 740, 'prairie chicken': 83, 'prairie fowl': 83, 'prairie grouse': 83, 'prairie wolf': 272, 'prayer mat': 741, 'prayer rug': 741, 'press': 894, 'pretzel': 932, 'printer': 742, 'prison': 743, 'prison house': 743, 'proboscis monkey': 376, 'projectile': 744, 'projector': 745, 'promontory': 976, 'ptarmigan': 81, 'puck': 746, 'puff': 750, 'puff adder': 54, 'puffer': 397, 'pufferfish': 397, 'pug': 254, 'pug-dog': 254, 'puma': 286, 'punch bag': 747, 'punchball': 747, 'punching bag': 747, 'punching ball': 747, 'purse': 748, 'pyjama': 697, 'quail': 85, 'quill': 749, 'quill pen': 749, 'quilt': 750, 'race car': 751, 'racer': 751, 'racing car': 751, 'racket': 752, 'racquet': 752, 'radiator': 753, 'radiator grille': 581, 'radio': 754, 'radio reflector': 755, 'radio telescope': 755, 'rain barrel': 756, 'ram': 348, 'rapeseed': 984, 'reaper': 595, 'recreational vehicle': 757, 'red fox': 277, 'red hot': 934, 'red panda': 387, 'red setter': 213, 'red wine': 966, 'red wolf': 271, 'red-backed sandpiper': 140, 'red-breasted merganser': 98, 'redbone': 168, 'redshank': 141, 'reel': 758, 'reflex camera': 759, 'refrigerator': 760, 'remote': 761, 'remote control': 761, 'respirator': 570, 'restaurant': 762, 'revolver': 763, 'rhinoceros beetle': 306, 'ribbed toad': 32, 'ricksha': 612, 'rickshaw': 612, 'rifle': 764, 'rig': 867, 'ring armor': 490, 'ring armour': 490, 'ring mail': 490, 'ring snake': 53, 'ring-binder': 446, 'ring-necked snake': 53, 'ring-tailed lemur': 383, 'ringlet': 322, 'ringlet butterfly': 322, 'ringneck snake': 53, 'ringtail': 378, 'river horse': 344, 'roach': 314, 'robin': 15, 'rock beauty': 392, 'rock crab': 119, 'rock lobster': 123, 'rock python': 62, 'rock snake': 62, 'rocker': 765, 'rocking chair': 765, 'rose hip': 989, 'rosehip': 989, 'rotisserie': 766, 'roundabout': 476, 'roundworm': 111, 'rubber': 767, 'rubber eraser': 767, 'rucksack': 414, 'ruddy turnstone': 139, 'ruffed grouse': 82, 'rugby ball': 768, 'rule': 769, 'ruler': 769, 'running shoe': 770, 'sabot': 502, 'safe': 771, 'safety pin': 772, 'salt shaker': 773, 'saltshaker': 773, 'sand bar': 977, 'sand viper': 66, 'sandal': 774, 'sandbar': 977, 'sarong': 775, 'sawmill': 634, 'sax': 776, 'saxophone': 776, 'scabbard': 777, 'scale': 778, 'schipperke': 223, 'school bus': 779, 'schooner': 780, 'scooter': 670, 'scope': 688, 'scoreboard': 781, 'scorpion': 71, 'screen': 782, 'screw': 783, 'screwdriver': 784, 'scuba diver': 983, 'sea anemone': 108, 'sea cradle': 116, 'sea crawfish': 123, 'sea cucumber': 329, 'sea lion': 150, 'sea slug': 115, 'sea snake': 65, 'sea star': 327, 'sea urchin': 328, 'sea wolf': 148, 'sea-coast': 978, 'seacoast': 978, 'seashore': 978, 'seat belt': 785, 'seatbelt': 785, 'seawall': 460, 'semi': 867, 'sewing machine': 786, 'sewing needle': 319, 'shades': 837, 'shako': 439, 'shield': 787, 'shoe shop': 788, 'shoe store': 788, 'shoe-shop': 788, 'shoji': 789, 'shopping basket': 790, 'shopping cart': 791, 'shovel': 792, 'shower cap': 793, 'shower curtain': 794, 'siamang': 369, 'sidewinder': 68, 'silky terrier': 201, 'silver salmon': 391, 'site': 916, 'six-gun': 763, 'six-shooter': 763, 'skeeter hawk': 319, 'ski': 795, 'ski mask': 796, 'skillet': 567, 'skunk': 361, 'sleeping bag': 797, 'sleuthhound': 163, 'slide rule': 798, 'sliding door': 799, 'slipstick': 798, 'slot': 800, 'sloth bear': 297, 'slug': 114, 'smoothing iron': 606, 'snail': 113, 'snake doctor': 319, 'snake feeder': 319, 'snake fence': 912, 'snake-rail fence': 912, 'snoek': 389, 'snooker table': 736, 'snorkel': 801, 'snow leopard': 289, 'snowbird': 13, 'snowmobile': 802, 'snowplough': 803, 'snowplow': 803, 'soap dispenser': 804, 'soccer ball': 805, 'sock': 806, 'soda bottle': 737, 'soft-coated wheaten terrier': 202, 'solar collector': 807, 'solar dish': 807, 'solar furnace': 807, 'sombrero': 808, 'sorrel': 339, 'soup bowl': 809, 'space bar': 810, 'space heater': 811, 'space shuttle': 812, 'spaghetti squash': 940, 'spatula': 813, 'speaker': 632, 'speaker system': 632, 'speaker unit': 632, 'speedboat': 814, 'spider monkey': 381, 'spider web': 815, "spider's web": 815, 'spike': 998, 'spindle': 816, 'spiny anteater': 102, 'spiny lobster': 123, 'spiral': 506, 'spoonbill': 129, 'sport car': 817, 'sports car': 817, 'spot': 818, 'spotlight': 818, 'spotted salamander': 28, 'squealer': 341, 'squeeze box': 401, 'squirrel monkey': 382, 'stage': 819, 'standard poodle': 267, 'standard schnauzer': 198, 'starfish': 327, 'station waggon': 436, 'station wagon': 436, 'steam locomotive': 820, 'steel arch bridge': 821, 'steel drum': 822, 'stethoscope': 823, 'stick insect': 313, 'stingray': 6, 'stinkhorn': 994, 'stole': 824, 'stone wall': 825, 'stop watch': 826, 'stoplight': 920, 'stopwatch': 826, 'stove': 827, 'strainer': 828, 'strawberry': 949, 'street sign': 919, 'streetcar': 829, 'stretcher': 830, 'studio couch': 831, 'stupa': 832, 'sturgeon': 394, 'sub': 833, 'submarine': 833, 'suit': 834, 'suit of clothes': 834, 'sulfur butterfly': 325, 'sulphur butterfly': 325, 'sulphur-crested cockatoo': 89, 'sun blocker': 838, 'sunblock': 838, 'sundial': 835, 'sunglass': 836, 'sunglasses': 837, 'sunscreen': 838, 'suspension bridge': 839, 'swab': 840, 'sweatshirt': 841, 'sweet potato': 684, 'swimming cap': 433, 'swimming trunks': 842, 'swing': 843, 'switch': 844, 'swob': 840, 'syringe': 845, 'syrinx': 699, 'tabby': 281, 'tabby cat': 281, 'table lamp': 846, 'tailed frog': 32, 'tailed toad': 32, 'tam-tam': 577, 'tandem': 444, 'tandem bicycle': 444, 'tank': 847, 'tank suit': 639, 'tape player': 848, 'taper': 470, 'tarantula': 76, 'taxi': 468, 'taxicab': 468, 'teapot': 849, 'teddy': 850, 'teddy bear': 850, 'tee shirt': 610, 'television': 851, 'television system': 851, 'ten-gallon hat': 515, 'tench': 0, 'tennis ball': 852, 'terrace': 706, 'terrapin': 36, 'thatch': 853, 'thatched roof': 853, 'theater curtain': 854, 'theatre curtain': 854, 'thimble': 855, 'thrasher': 856, 'three-toed sloth': 364, 'thresher': 856, 'threshing machine': 856, 'throne': 857, 'thunder snake': 52, 'tick': 78, 'tiger': 292, 'tiger beetle': 300, 'tiger cat': 282, 'tiger shark': 3, 'tile roof': 858, 'timber wolf': 269, 'tin opener': 473, 'titi': 380, 'titi monkey': 380, 'toaster': 859, 'tobacco shop': 860, 'tobacconist': 860, 'tobacconist shop': 860, 'toilet paper': 999, 'toilet seat': 861, 'toilet tissue': 999, 'tool kit': 477, 'tope': 832, 'torch': 862, 'torpedo': 5, 'totem pole': 863, 'toucan': 96, 'tow car': 864, 'tow truck': 864, 'toy poodle': 265, 'toy terrier': 158, 'toyshop': 865, 'trackless trolley': 874, 'tractor': 866, 'tractor trailer': 867, 'traffic light': 920, 'traffic signal': 920, 'trailer truck': 867, 'tram': 829, 'tramcar': 829, 'transverse flute': 558, 'trash barrel': 412, 'trash bin': 412, 'trash can': 412, 'tray': 868, 'tree frog': 31, 'tree-frog': 31, 'trench coat': 869, 'triceratops': 51, 'tricycle': 870, 'trifle': 927, 'trike': 870, 'trilobite': 69, 'trimaran': 871, 'tripod': 872, 'triumphal arch': 873, 'trolley': 829, 'trolley car': 829, 'trolley coach': 874, 'trolleybus': 874, 'trombone': 875, 'trucking rig': 867, 'trump': 513, 'trumpet': 513, 'tub': 876, 'tup': 348, 'turnstile': 877, 'tusker': 101, 'two-piece': 445, 'tympan': 541, 'typewriter keyboard': 878, 'umbrella': 879, 'unicycle': 880, 'upright': 881, 'upright piano': 881, 'vacuum': 882, 'vacuum cleaner': 882, 'vale': 979, 'valley': 979, 'vase': 883, 'vat': 876, 'vault': 884, 'velocipede': 870, 'velvet': 885, 'vending machine': 886, 'vestment': 887, 'viaduct': 888, 'vine snake': 59, 'violin': 889, 'violoncello': 486, 'vizsla': 211, 'volcano': 980, 'volleyball': 890, 'volute': 506, 'vulture': 23, 'waffle iron': 891, 'waggon': 436, 'wagon': 734, 'walking stick': 313, 'walkingstick': 313, 'wall clock': 892, 'wallaby': 104, 'wallet': 893, 'wardrobe': 894, 'warplane': 895, 'warragal': 273, 'warrigal': 273, 'warthog': 343, 'wash-hand basin': 896, 'washbasin': 896, 'washbowl': 896, 'washer': 897, 'washing machine': 897, 'wastebin': 412, 'water bottle': 898, 'water buffalo': 346, 'water hen': 137, 'water jug': 899, 'water ouzel': 20, 'water ox': 346, 'water snake': 58, 'water tower': 900, 'wax light': 470, 'weasel': 356, 'web site': 916, 'website': 916, 'weevil': 307, 'weighing machine': 778, 'welcome mat': 539, 'wheelbarrow': 428, 'whippet': 172, 'whiptail': 41, 'whiptail lizard': 41, 'whirligig': 476, 'whiskey jug': 901, 'whistle': 902, 'white fox': 279, 'white shark': 2, 'white stork': 127, 'white wolf': 270, 'whorl': 506, 'wig': 903, 'wild boar': 342, 'window screen': 904, 'window shade': 905, 'wine bottle': 907, 'wing': 908, 'wire-haired fox terrier': 188, 'wireless': 754, 'wok': 909, 'wolf spider': 77, 'wombat': 106, 'wood pussy': 361, 'wood rabbit': 330, 'wooden spoon': 910, 'woodworking plane': 726, 'wool': 911, 'woolen': 911, 'woollen': 911, 'worm fence': 912, 'worm snake': 52, 'wreck': 913, 'wrecker': 864, 'xylophone': 642, 'yawl': 914, "yellow lady's slipper": 986, 'yellow lady-slipper': 986, 'yurt': 915, 'zebra': 340, 'zucchini': 939}

artists = ( "Ivan Aivazovsky", "Beeple", "Zdzislaw Beksinski", "Albert Bierstadt", "Noah Bradley", "Jim Burns", "John Harris", "John Howe", "Thomas Kinkade", "Gediminas Pranckevicius", "Andreas Rocha", "Marc Simonetti", "Simon Stalenhag", "Yuumei", "Asher Brown Durand", "Tyler Edlin", "Jesper Ejsing", "Peter Mohrbacher", "RHADS", "Greg Rutkowski", "H.P. Lovecraft", "George Lucas", "Benoit B. Mandelbrot", "Edwin Austin Abbey", "Ansel Adams", "Arthur Adams", "Charles Addams", "Alena Aenami", "Pieter Aertsen", "Hilma af Klint", "Affandi", "Leonid Afremov", "Eileen Agar", "Ivan Aivazovsky", "Anni Albers", "Josef Albers", "Ivan Albright", "Yoshitaka Amano", "Cuno Amiet", "Sophie Anderson", "Wes Anderson", "Esao Andrews", "Charles Angrand", "Sofonisba Anguissola", "Hirohiko Araki", "Nobuyoshi Araki", "Shinji Aramaki", "Diane Arbus", "Giuseppe Arcimboldo", "Steve Argyle", "Jean Arp", "Artgerm", "John James Audubon", "Frank Auerbach", "Milton Avery", "Tex Avery", "Harriet Backer", "Francis Bacon", "Peter Bagge", "Tom Bagshaw", "Karol Bak", "Christopher Balaskas", "Hans Baldung", "Ronald Balfour", "Giacomo Balla", "Banksy", "Cicely Mary Barker", "Carl Barks", "Wayne Barlowe", "Jean-Michel Basquiat", "Jules Bastien-Lepage", "David Bates", "John Bauer", "Aubrey Beardsley", "Jasmine Becket-Griffith", "Max Beckmann", "Beeple", "Zdzislaw Beksinski", "Zdzisław Beksiński", "Julie Bell", "Hans Bellmer", "John Berkey", "Émile Bernard", "Elsa Beskow", "Albert Bierstadt", "Enki Bilal", "Ivan Bilibin", "Simon Bisley", "Charles Blackman", "Thomas Blackshear", "Mary Blair", "Quentin Blake", "William Blake", "Antoine Blanchard", "John Blanche", "Pascal Blanché", "Karl Blossfeldt", "Don Bluth", "Umberto Boccioni", "Arnold Böcklin", "Chesley Bonestell", "Franklin Booth", "Guido Borelli da Caluso", "Marius Borgeaud", "Hieronymous Bosch", "Hieronymus Bosch", "Sam Bosma", "Johfra Bosschart", "Sandro Botticelli", "William-Adolphe Bouguereau", "Louise Bourgeois", "Eleanor Vere Boyle", "Noah Bradley", "Victor Brauner", "Austin Briggs", "Raymond Briggs", "Mark Briscoe", "Romero Britto", "Gerald Brom", "Mark Brooks", "Patrick Brown", "Pieter Bruegel the Elder", "Bernard Buffet", "Laurel Burch", "Charles E. Burchfield", "David Burdeny", "Richard Burlet", "David Burliuk", "Edward Burne-Jones", "Jim Burns", "William S. Burroughs", "Gaston Bussière", "Kaethe Butcher", "Jack Butler Yeats", "Bob Byerley", "Alexandre Cabanel", "Ray Caesar", "Claude Cahun", "Zhichao Cai", "Randolph Caldecott", "Alexander Milne Calder", "Clyde Caldwell", "Eddie Campbell", "Pascale Campion", "Canaletto", "Caravaggio", "Annibale Carracci", "Carl Gustav Carus", "Santiago Caruso", "Mary Cassatt", "Paul Cézanne", "Marc Chagall", "Marcel Chagall", "Yanjun Cheng", "Sandra Chevrier", "Judy Chicago", "James C. Christensen", "Frederic Church", "Mikalojus Konstantinas Ciurlionis", "Pieter Claesz", "Amanda Clark", "Harry Clarke", "Thomas Cole", "Mat Collishaw", "John Constable", "Cassius Marcellus Coolidge", "Richard Corben", "Lovis Corinth", "Joseph Cornell", "Camille Corot", "cosmic nebulae", "Gustave Courbet", "Lucas Cranach the Elder", "Walter Crane", "Craola", "Gregory Crewdson", "Henri-Edmond Cross", "Robert Crumb", "Tivadar Csontváry Kosztka", "Krenz Cushart", "Leonardo da Vinci", "Richard Dadd", "Louise Dahl-Wolfe", "Salvador Dalí", "Farel Dalrymple", "Geof Darrow", "Honoré Daumier", "Jack Davis", "Marc Davis", "Stuart Davis", "Craig Davison", "Walter Percy Day", "Pierre Puvis de Chavannes", "Giorgio de Chirico", "Pieter de Hooch", "Elaine de Kooning", "Willem de Kooning", "Evelyn De Morgan", "Henri de Toulouse-Lautrec", "Richard Deacon", "Roger Dean", "Michael Deforge", "Edgar Degas", "Lise Deharme", "Eugene Delacroix", "Beauford Delaney", "Sonia Delaunay", "Nicolas Delort", "Paul Delvaux", "Jean Delville", "Martin Deschambault", "Brian Despain", "Vincent Di Fate", "Steve Dillon", "Walt Disney", "Tony DiTerlizzi", "Steve Ditko", "Anna Dittmann", "Otto Dix", "Óscar Domínguez", "Russell Dongjun Lu", "Stanley Donwood", "Gustave Doré", "Dave Dorman", "Arthur Dove", "Richard Doyle", "Tim Doyle", "Philippe Druillet", "Joseph Ducreux", "Edmund Dulac", "Asher Brown Durand", "Albrecht Dürer", "Thomas Eakins", "Eyvind Earle", "Jeff Easley", "Tyler Edlin", "Jason Edmiston", "Les Edwards", "Bob Eggleton", "Jesper Ejsing", "El Greco", "Olafur Eliasson", "Harold Elliott", "Dean Ellis", "Larry Elmore", "Peter Elson", "Ed Emshwiller", "Kilian Eng", "James Ensor", "Max Ernst", "Elliott Erwitt", "M.C. Escher", "Richard Eurich", "Glen Fabry", "Anton Fadeev", "Shepard Fairey", "John Philip Falter", "Lyonel Feininger", "Joe Fenton", "Agustín Fernández", "Roberto Ferri", "Hugh Ferriss", "David Finch", "Virgil Finlay", "Howard Finster", "Anton Otto Fischer", "Paul Gustav Fischer", "Paul Gustave Fischer", "Art Fitzpatrick", "Dan Flavin", "Kaja Foglio", "Phil Foglio", "Chris Foss", "Hal Foster", "Jean-Honoré Fragonard", "Victoria Francés", "Lisa Frank", "Frank Frazetta", "Kelly Freas", "Lucian Freud", "Caspar David Friedrich", "Brian Froud", "Wendy Froud", "Ernst Fuchs", "Goro Fujita", "Henry Fuseli", "Thomas Gainsborough", "Emile Galle", "Stephen Gammell", "Hope Gangloff", "Antoni Gaudi", "Antoni Gaudí", "Jack Gaughan", "Paul Gauguin", "Giovanni Battista Gaulli", "Nikolai Ge", "Emma Geary", "Anne Geddes", "Jeremy Geddes", "Artemisia Gentileschi", "Justin Gerard", "Jean-Leon Gerome", "Jean-Léon Gérôme", "Atey Ghailan", "Alberto Giacometti", "Donato Giancola", "Dave Gibbons", "H. R. Giger", "James Gilleard", "Jean Giraud", "Milton Glaser", "Warwick Goble", "Andy Goldsworthy", "Hendrick Goltzius", "Natalia Goncharova", "Rob Gonsalves", "Josan Gonzalez", "Edward Gorey", "Arshile Gorky", "Francisco Goya", "J. J. Grandville", "Jane Graverol", "Mab Graves", "Laurie Greasley", "Kate Greenaway", "Alex Grey", "Peter Gric", "Carne Griffiths", "John Atkinson Grimshaw", "Henriette Grindat", "Matt Groening", "William Gropper", "George Grosz", "Matthias Grünewald", "Rebecca Guay", "James Gurney", "Philip Guston", "Sir James Guthrie", "Zaha Hadid", "Ernst Haeckel", "Sydney Prior Hall", "Asaf Hanuka", "Tomer Hanuka", "David A. Hardy", "Keith Haring", "John Harris", "Lawren Harris", "Marsden Hartley", "Ryohei Hase", "Jacob Hashimoto", "Martin Johnson Heade", "Erich Heckel", "Michael Heizer", "Steve Henderson", "Patrick Heron", "Ryan Hewett", "Jamie Hewlett", "Brothers Hildebrandt", "Greg Hildebrandt", "Tim Hildebrandt", "Miho Hirano", "Adolf Hitler", "Hannah Hoch", "David Hockney", "Filip Hodas", "Howard Hodgkin", "Ferdinand Hodler", "William Hogarth", "Katsushika Hokusai", "Carl Holsoe", "Winslow Homer", "Edward Hopper", "Aaron Horkey", "Kati Horna", "Ralph Horsley", "John Howe", "John Hoyland", "Arthur Hughes", "Edward Robert Hughes", "Friedensreich Regentag Dunkelbunt Hundertwasser", "Hundertwasser", "William Henry Hunt", "Louis Icart", "Ismail Inceoglu", "Bjarke Ingels", "George Inness", "Shotaro Ishinomori", "Junji Ito", "Johannes Itten", "Ub Iwerks", "Alexander Jansson", "Jarosław Jaśnikowski", "James Jean", "Ruan Jia", "Martine Johanna", "Richard S. Johnson", "Jeffrey Catherine Jones", "Peter Andrew Jones", "Kim Jung Gi", "Joe Jusko", "Frida Kahlo", "M.W. Kaluta", "Wassily Kandinsky", "Terada Katsuya", "Audrey Kawasaki", "Hasui Kawase", "Zhang Kechun", "Felix Kelly", "John Frederick Kensett", "Rockwell Kent", "Hendrik Kerstens", "Brian Kesinger", "Jeremiah Ketner", "Adonna Khare", "Kitty Lange Kielland", "Thomas Kinkade", "Jack Kirby", "Ernst Ludwig Kirchner", "Tatsuro Kiuchi", "Mati Klarwein", "Jon Klassen", "Paul Klee", "Yves Klein", "Heinrich Kley", "Gustav Klimt", "Daniel Ridgway Knight", "Nick Knight", "Daniel Ridgway Knights", "Ayami Kojima", "Oskar Kokoschka", "Käthe Kollwitz", "Satoshi Kon", "Jeff Koons", "Konstantin Korovin", "Leon Kossoff", "Hugh Kretschmer", "Barbara Kruger", "Alfred Kubin", "Arkhyp Kuindzhi", "Kengo Kuma", "Yasuo Kuniyoshi", "Yayoi Kusama", "Ilya Kuvshinov", "Chris LaBrooy", "Raphael Lacoste", "Wilfredo Lam", "Mikhail Larionov", "Abigail Larson", "Jeffrey T. Larson", "Carl Larsson", "Dorothy Lathrop", "John Lavery", "Edward Lear", "André Leblanc", "Bastien Lecouffe-Deharme", "Alan Lee", "Jim Lee", "Heinrich Lefler", "Paul Lehr", "Edmund Leighton", "Frederick Lord Leighton", "Jeff Lemire", "Isaac Levitan", "J.C. Leyendecker", "Roy Lichtenstein", "Rob Liefeld", "Malcolm Liepke", "Jeremy Lipking", "Filippino Lippi", "Laurie Lipton", "Michal Lisowski", "Scott Listfield", "Cory Loftis", "Travis Louie", "George Luks", "Dora Maar", "August Macke", "Margaret Macdonald Mackintosh", "Clive Madgwick", "Lee Madgwick", "Rene Magritte", "Don Maitz", "Kazimir Malevich", "Édouard Manet", "Jeremy Mann", "Sally Mann", "Franz Marc", "Chris Mars", "Otto Marseus van Schrieck", "John Martin", "Masaaki Masamoto", "André Masson", "Henri Matisse", "Leiji Matsumoto", "Taiyō Matsumoto", "Roberto Matta", "Rodney Matthews", "David B. Mattingly", "Peter Max", "Marco Mazzoni", "Robert McCall", "Todd McFarlane", "Ryan McGinley", "Dave McKean", "Kelly McKernan", "Angus McKie", "Ralph McQuarrie", "Ian McQue", "Syd Mead", "Józef Mehoffer", "Eddie Mendoza", "Adolph Menzel", "Maria Sibylla Merian", "Daniel Merriam", "Jean Metzinger", "Michelangelo", "Mike Mignola", "Frank Miller", "Ian Miller", "Russ Mills", "Victor Adame Minguez", "Joan Miro", "Kentaro Miura", "Paula Modersohn-Becker", "Amedeo Modigliani", "Moebius", "Peter Mohrbacher", "Piet Mondrian", "Claude Monet", "Jean-Baptiste Monge", "Kent Monkman", "Alyssa Monks", "Sailor Moon", "Chris Moore", "Gustave Moreau", "William Morris", "Igor Morski", "John Kenn Mortensen", "Victor Moscoso", "Grandma Moses", "Robert Motherwell", "Alphonse Mucha", "Craig Mullins", "Augustus Edwin Mulready", "Dan Mumford", "Edvard Munch", "Gabriele Münter", "Gerhard Munthe", "Takashi Murakami", "Patrice Murciano", "Go Nagai", "Hiroshi Nagai", "Tibor Nagy", "Ted Nasmith", "Alice Neel", "Odd Nerdrum", "Mikhail Nesterov", "C. R. W. Nevinson", "Helmut Newton", "Victo Ngai",
           "Dustin Nguyen", "Kay Nielsen", "Tsutomu Nihei", "Yasushi Nirasawa", "Sidney Nolan", "Emil Nolde", "Sven Nordqvist", "Earl Norem", "Marianne North", "Georgia O'Keeffe", "Terry Oakes", "Takeshi Obata", "Eiichiro Oda", "Koson Ohara", "Noriyoshi Ohrai", "Marek Okon", "Méret Oppenheim", "Katsuhiro Otomo", "Shohei Otomo", "Siya Oum", "Ida Rentoul Outhwaite", "James Paick", "David Palumbo", "Michael Parkes", "Keith Parkinson", "Maxfield Parrish", "Alfred Parsons", "Max Pechstein", "Agnes Lawrence Pelton", "Bruce Pennington", "John Perceval", "Gaetano Pesce", "Coles Phillips", "Francis Picabia", "Pablo Picasso", "Mauro Picenardi", "Anton Pieck", "Bonnard Pierre", "Yuri Ivanovich Pimenov", "Robert Antoine Pinchon", "Giovanni Battista Piranesi", "Camille Pissarro", "Patricia Polacco", "Jackson Pollock", "Lyubov Popova", "Candido Portinari", "Beatrix Potter", "Beatrix Potter", "Gediminas Pranckevicius", "Dod Procter", "Howard Pyle", "Arthur Rackham", "Alice Rahon", "Paul Ranson", "Raphael", "Robert Rauschenberg", "Man Ray", "Odilon Redon", "Pierre-Auguste Renoir", "Ilya Repin", "RHADS", "Gerhard Richter", "Diego Rivera", "Hubert Robert", "Andrew Robinson", "Charles Robinson", "W. Heath Robinson", "Andreas Rocha", "Norman Rockwell", "Nicholas Roerich", "Conrad Roset", "Bob Ross", "Jessica Rossier", "Ed Roth", "Mark Rothko", "Georges Rouault", "Henri Rousseau", "Luis Royo", "Jakub Rozalski", "Joao Ruas", "Peter Paul Rubens", "Mark Ryden", "Jan Pietersz Saenredam", "Pieter Jansz Saenredam", "Kay Sage", "Apollonia Saintclair", "John Singer Sargent", "Martiros Saryan", "Masaaki Sasamoto", "Thomas W Schaller", "Miriam Schapiro", "Yohann Schepacz", "Egon Schiele", "Karl Schmidt-Rottluff", "Charles Schulz", "Charles Schulz", "Carlos Schwabe", "Sean Scully", "Franz Sedlacek", "Maurice Sendak", "Zinaida Serebriakova", "Georges Seurat", "Ben Shahn", "Barclay Shaw", "E. H. Shepard", "Cindy Sherman", "Makoto Shinkai", "Yoji Shinkawa", "Chiharu Shiota", "Masamune Shirow", "Ivan Shishkin", "Bill Sienkiewicz", "Greg Simkins", "Marc Simonetti", "Kevin Sloan", "Adrian Smith", "Douglas Smith", "Jeffrey Smith", "Pamela Coleman Smith", "Zack Snyder", "Simeon Solomon", "Joaquín Sorolla", "Ettore Sottsass", "Chaïm Soutine", "Austin Osman Spare", "Sparth ", "Art Spiegelman", "Simon Stalenhag", "Ralph Steadman", "William Steig", "Joseph Stella", "Irma Stern", "Anne Stokes", "James Stokoe", "William Stout", "George Stubbs", "Tatiana Suarez", "Ken Sugimori", "Hiroshi Sugimoto", "Brian Sum", "Matti Suuronen", "Raymond Swanland", "Naoko Takeuchi", "Rufino Tamayo", "Shaun Tan", "Yves Tanguay", "Henry Ossawa Tanner", "Dorothea Tanning", "Ben Templesmith", "theCHAMBA", "Tom Thomson", "Storm Thorgerson", "Bridget Bate Tichenor", "Louis Comfort Tiffany", "Tintoretto", "James Tissot", "Titian", "Akira Toriyama", "Ross Tran", "Clovis Trouille", "J.M.W. Turner", "James Turrell", "Daniela Uhlig", "Boris Vallejo", "Gustave Van de Woestijne", "Frits Van den Berghe", "Anthony van Dyck", "Jan van Eyck", "Vincent Van Gogh", "Willem van Haecht", "Rembrandt van Rijn", "Jacob van Ruisdael", "Salomon van Ruysdael", "Theo van Rysselberghe", "Remedios Varo", "Viktor Vasnetsov", "Kuno Veeber", "Diego Velázquez", "Giovanni Battista Venanzi", "Johannes Vermeer", "Alexej von Jawlensky", "Marianne von Werefkin", "Hendrick Cornelisz Vroom", "Mikhail Vrubel", "Louis Wain", "Ron Walotsky", "Andy Warhol", "John William Waterhouse", "Jean-Antoine Watteau", "George Frederic Watts", "Max Weber", "Gerda Wegener", "Edward Weston", "Michael Whelan", "James Abbott McNeill Whistler", "Tim White", "Coby Whitmore", "John Wilhelm", "Robert Williams", "Al Williamson", "Carel Willink", "Mike Winkelmann", "Franz Xaver Winterhalter", "Klaus Wittmann", "Liam Wong", "Paul Wonner", "Ashley Wood", "Grant Wood", "Patrick Woodroffe", "Frank Lloyd Wright", "Bernie Wrightson", "Andrew Wyeth", "Qian Xuan", "Takato Yamamoto", "Liu Ye", "Jacek Yerka", "Akihiko Yoshida", "Hiroshi Yoshida", "Skottie Young", "Konstantin Yuon", "Yuumei", "Amir Zand", "Fenghua Zhong", "Nele Zirnite", "Anders Zorn")
styles = ( "1970s era", "2001: A Space Odyssey", "60s kitsch and psychedelia", "Aaahh!!! Real Monsters", "abstract illusionism", "afrofuturism", "alabaster", "alhambresque", "ambrotype", "american romanticism", "amethyst", "amigurumi", "anaglyph effect", "anaglyph filter", "Ancient Egyptian", "ancient Greek architecture", "anime", "art nouveau", "astrophotography", "at dawn", "at dusk", "at high noon", "at night", "atompunk", "aureolin", "avant-garde", "Avatar The Last Airbender", "Babylonian", "Baker-Miller pink", "Baroque", "Bauhaus", "biopunk", "bismuth", "Blade Runner 2049", "blueprint", "bokeh", "bonsai", "bright", "bronze", "brutalism", "burgundy", "Byzantine", "calotype", "Cambrian", "camcorder effect", "carmine", "cassette futurism", "cassettepunk", "catholicpunk", "cerulean", "chalk art", "chartreuse", "chiaroscuro", "chillwave", "chromatic aberration", "chrome", "Cirque du Soleil", "claymation", "clockpunk", "cloudpunk", "cobalt", "colored pencil art", "Concept Art World", "copper patina", "copper verdigris", "Coraline", "cosmic horror", "cottagecore", "crayon art", "crimson", "CryEngine", "crystalline lattice", "cubic zirconia", "cubism", "cyanotype", "cyber noir", "cyberpunk", "cyclopean masonry", "daguerreotype", "Danny Phantom", "dark academia", "dark pastel", "dark rainbow", "DayGlo", "decopunk", "Dexter's Lab", "diamond", "dieselpunk", "Digimon", "digital art", "doge", "dollpunk", "Doom engine", "Dreamworks", "dutch golden age", "Egyptian", "eldritch", "emerald", "empyrean", "Eraserhead", "ethereal", "expressionism", "Fantastic Planet", "Fendi", "figurativism", "fire", "fisheye lens", "fluorescent", "forestpunk", "fractal manifold", "fractalism", "fresco", "fuchsia", "futuresynth", "Game of Thrones", "german romanticism", "glitch art", "glittering", "golden", "golden hour", "gothic", "gothic art", "graffiti", "graphite", "grim dark", "Harry Potter", "holography", "Howl’s Moving Castle", "hygge", "hyperrealism", "icy", "ikebana", "impressionism", "in Ancient Egypt", "in Egypt", "in Italy", "in Japan", "in the Central African Republic", "in the desert", "in the jungle", "in the swamp", "in the tundra", "incandescent", "indigo", "infrared", "Interstellar", "inverted colors", "iridescent", "iron", "islandpunk", "isotype", "Kai Fine Art", "khaki", "kokedama", "Korean folk art", "lapis lazuli", "Lawrence of Arabia", "leather", "leopard print", "lilac", "liminal space", "long exposure", "Lord of the Rings", "Louis Vuitton", "Lovecraftian", "low poly", "mac and cheese", "macro lens", "magenta", "magic realism", "manga", "mariachi", "marimekko", "maroon", "Medieval", "Mediterranean", "modernism", "Monster Rancher", "moonstone", "Moulin Rouge!", "multiple exposure", "Myst", "nacreous", "narrative realism", "naturalism", "neon", "Nosferatu", "obsidian", "oil and canvas", "opalescent", "optical illusion", "optical art", "organometallics", "ossuary", "outrun", "Paleolithic", "Pan's Labyrinth", "pastel", "patina", "pearlescent", "pewter", "Pixar", "Play-Doh", "pointillism", "Pokemon", "polaroid", "porcelain", "positivism", "postcyberpunk", "Pride & Prejudice", "prismatic", "pyroclastic flow", "Quake engine", "quartz", "rainbow", "reflective", "Renaissance", "retrowave", "Rococo", "rococopunk", "ruby", "rusty", "Salad Fingers", "sapphire", "scarlet", "shimmering", "silk", "sketched", "Slenderman", "smoke", "snakeskin", "Spaceghost Coast to Coast", "stained glass", "Star Wars", "steampunk", "steel", "steelpunk", "still life", "stonepunk", "Stranger Things", "street art", "stuckism", "Studio Ghibli", "Sumerian", "surrealism", "symbolism", "synthwave", "telephoto lens", "thalassophobia", "thangka", "the matrix", "tiger print", "tilt-shift", "tintype", "tonalism", "Toonami", "turquoise", "Ukiyo-e", "ultramarine", "ultraviolet", "umber", "underwater photography", "Unreal Engine", "vantablack", "vaporwave", "verdigris", "Versacci", "viridian", "wabi-sabi", "watercolor painting", "wooden", "x-ray photography", "minimalist", "dadaist", "neo-expressionist", "post-impressionist", "hyper real", "Art brut", "3D rendering", "uncanny valley", "fractal landscape", "fractal flames", "Mandelbulb", "inception dream", "waking life", "occult inscriptions", "barr relief", "marble sculpture", "wood carving", "church stained glass", "Japanese jade", "Zoetrope", "beautiful", "wide-angle", "Digital Painting", "glossy reflections", "cinematic", "spooky", "Digital paint concept art", "dramatic", "global illumination", "immaculate", "woods", )

# https://github.com/twri/sdxl_prompt_styler/blob/main/sdxl_styles.json

prompt_styles = [
    {
        "name": "cinematic-default",
        "prompt": "cinematic still {prompt}. emotional, harmonious, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "sai-3d-model",
        "prompt": "professional 3d model {prompt}. octane render, highly detailed, volumetric, dramatic lighting",
        "negative_prompt": "ugly, deformed, noisy, low poly, blurry, painting"
    },
    {
        "name": "sai-analog film",
        "prompt": "analog film photo {prompt}. faded film, desaturated, 35mm photo, grainy, vignette, vintage, Kodachrome, Lomography, stained, highly detailed, found footage",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "sai-anime",
        "prompt": "anime artwork {prompt}. anime style, key visual, vibrant, studio anime,  highly detailed",
        "negative_prompt": "photo, deformed, black and white, realism, disfigured, low contrast"
    },
    {
        "name": "sai-cinematic",
        "prompt": "cinematic film still {prompt}. shallow depth of field, vignette, highly detailed, high budget, bokeh, cinemascope, moody, epic, gorgeous, film grain, grainy",
        "negative_prompt": "anime, cartoon, graphic, text, painting, crayon, graphite, abstract, glitch, deformed, mutated, ugly, disfigured"
    },
    {
        "name": "sai-comic book",
        "prompt": "comic {prompt}. graphic illustration, comic art, graphic novel art, vibrant, highly detailed",
        "negative_prompt": "photograph, deformed, glitch, noisy, realistic, stock photo"
    },
    {
        "name": "sai-craft clay",
        "prompt": "play-doh style {prompt}. sculpture, clay art, centered composition, Claymation",
        "negative_prompt": "sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-digital art",
        "prompt": "concept art {prompt}. digital artwork, illustrative, painterly, matte painting, highly detailed",
        "negative_prompt": "photo, photorealistic, realism, ugly"
    },
    {
        "name": "sai-enhance",
        "prompt": "breathtaking {prompt}. award-winning, professional, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, distorted, grainy"
    },
    {
        "name": "sai-fantasy art",
        "prompt": "ethereal fantasy concept art of {prompt}. magnificent, celestial, ethereal, painterly, epic, majestic, magical, fantasy art, cover art, dreamy",
        "negative_prompt": "photographic, realistic, realism, 35mm film, dslr, cropped, frame, text, deformed, glitch, noise, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, sloppy, duplicate, mutated, black and white"
    },
    {
        "name": "sai-isometric",
        "prompt": "isometric style {prompt}. vibrant, beautiful, crisp, detailed, ultra detailed, intricate",
        "negative_prompt": "deformed, mutated, ugly, disfigured, blur, blurry, noise, noisy, realistic, photographic"
    },
    {
        "name": "sai-line art",
        "prompt": "line art drawing {prompt}. professional, sleek, modern, minimalist, graphic, line art, vector graphics",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, blurry, noisy, off-center, deformed, cross-eyed, closed eyes, bad anatomy, ugly, disfigured, mutated, realism, realistic, impressionism, expressionism, oil, acrylic"
    },
    {
        "name": "sai-lowpoly",
        "prompt": "low-poly style {prompt}. low-poly game art, polygon mesh, jagged, blocky, wireframe edges, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-neonpunk",
        "prompt": "neonpunk style {prompt}. cyberpunk, vaporwave, neon, vibes, vibrant, stunningly beautiful, crisp, detailed, sleek, ultramodern, magenta highlights, dark purple shadows, high contrast, cinematic, ultra detailed, intricate, professional",
        "negative_prompt": "painting, drawing, illustration, glitch, deformed, mutated, cross-eyed, ugly, disfigured"
    },
    {
        "name": "sai-origami",
        "prompt": "origami style {prompt}. paper art, pleated paper, folded, origami art, pleats, cut and fold, centered composition",
        "negative_prompt": "noisy, sloppy, messy, grainy, highly detailed, ultra textured, photo"
    },
    {
        "name": "sai-photographic",
        "prompt": "cinematic photo {prompt}. 35mm photograph, film, bokeh, professional, 4k, highly detailed",
        "negative_prompt": "drawing, painting, crayon, sketch, graphite, impressionist, noisy, blurry, soft, deformed, ugly"
    },
    {
        "name": "sai-pixel art",
        "prompt": "pixel-art {prompt}. low-res, blocky, pixel art style, 8-bit graphics",
        "negative_prompt": "sloppy, messy, blurry, noisy, highly detailed, ultra textured, photo, realistic"
    },
    {
        "name": "sai-texture",
        "prompt": "texture {prompt} top down close-up",
        "negative_prompt": "ugly, deformed, noisy, blurry"
    },
    {
        "name": "ads-advertising",
        "prompt": "Advertising poster style {prompt}. Professional, modern, product-focused, commercial, eye-catching, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "ads-automotive",
        "prompt": "Automotive advertisement style {prompt}. Sleek, dynamic, professional, commercial, vehicle-focused, high-resolution, highly detailed",
        "negative_prompt": "noisy, blurry, unattractive, sloppy, unprofessional"
    },
    {
        "name": "ads-corporate",
        "prompt": "Corporate branding style {prompt}. Professional, clean, modern, sleek, minimalist, business-oriented, highly detailed",
        "negative_prompt": "noisy, blurry, grungy, sloppy, cluttered, disorganized"
    },
    {
        "name": "ads-fashion editorial",
        "prompt": "Fashion editorial style {prompt}. High fashion, trendy, stylish, editorial, magazine style, professional, highly detailed",
        "negative_prompt": "outdated, blurry, noisy, unattractive, sloppy"
    },
    {
        "name": "ads-food photography",
        "prompt": "Food photography style {prompt}. Appetizing, professional, culinary, high-resolution, commercial, highly detailed",
        "negative_prompt": "unappetizing, sloppy, unprofessional, noisy, blurry"
    },
    {
        "name": "ads-luxury",
        "prompt": "Luxury product style {prompt}. Elegant, sophisticated, high-end, luxurious, professional, highly detailed",
        "negative_prompt": "cheap, noisy, blurry, unattractive, amateurish"
    },
    {
        "name": "ads-real estate",
        "prompt": "Real estate photography style {prompt}. Professional, inviting, well-lit, high-resolution, property-focused, commercial, highly detailed",
        "negative_prompt": "dark, blurry, unappealing, noisy, unprofessional"
    },
    {
        "name": "ads-retail",
        "prompt": "Retail packaging style {prompt}. Vibrant, enticing, commercial, product-focused, eye-catching, professional, highly detailed",
        "negative_prompt": "noisy, blurry, amateurish, sloppy, unattractive"
    },
    {
        "name": "artstyle-abstract",
        "prompt": "abstract style {prompt}. non-representational, colors and shapes, expression of feelings, imaginative, highly detailed",
        "negative_prompt": "realistic, photographic, figurative, concrete"
    },
    {
        "name": "artstyle-abstract expressionism",
        "prompt": "abstract expressionist painting {prompt}. energetic brushwork, bold colors, abstract forms, expressive, emotional",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, monochrome"
    },
    {
        "name": "artstyle-art deco",
        "prompt": "Art Deco style {prompt}. geometric shapes, bold colors, luxurious, elegant, decorative, symmetrical, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "artstyle-art nouveau",
        "prompt": "Art Nouveau style {prompt}. elegant, decorative, curvilinear forms, nature-inspired, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, modernist, minimalist"
    },
    {
        "name": "artstyle-constructivist",
        "prompt": "constructivist style {prompt}. geometric shapes, bold colors, dynamic composition, propaganda art style",
        "negative_prompt": "realistic, photorealistic, low contrast, plain, simple, abstract expressionism"
    },
    {
        "name": "artstyle-cubist",
        "prompt": "cubist artwork {prompt}. geometric shapes, abstract, innovative, revolutionary",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "artstyle-expressionist",
        "prompt": "expressionist {prompt}. raw, emotional, dynamic, distortion for emotional effect, vibrant, use of unusual colors, detailed",
        "negative_prompt": "realism, symmetry, quiet, calm, photo"
    },
    {
        "name": "artstyle-graffiti",
        "prompt": "graffiti style {prompt}. street art, vibrant, urban, detailed, tag, mural",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "artstyle-hyperrealism",
        "prompt": "hyperrealistic art {prompt}. extremely high-resolution details, photographic, realism pushed to extreme, fine texture, incredibly lifelike",
        "negative_prompt": "simplified, abstract, unrealistic, impressionistic, low resolution"
    },
    {
        "name": "artstyle-impressionist",
        "prompt": "impressionist painting {prompt}. loose brushwork, vibrant color, light and shadow play, captures feeling over form",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "artstyle-pointillism",
        "prompt": "pointillism style {prompt}. composed entirely of small, distinct dots of color, vibrant, highly detailed",
        "negative_prompt": "line drawing, smooth shading, large color fields, simplistic"
    },
    {
        "name": "artstyle-pop art",
        "prompt": "Pop Art style {prompt}. bright colors, bold outlines, popular culture themes, ironic or kitsch",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, minimalist"
    },
    {
        "name": "artstyle-psychedelic",
        "prompt": "psychedelic style {prompt}. vibrant colors, swirling patterns, abstract forms, surreal, trippy",
        "negative_prompt": "monochrome, black and white, low contrast, realistic, photorealistic, plain, simple"
    },
    {
        "name": "artstyle-renaissance",
        "prompt": "Renaissance style {prompt}. realistic, perspective, light and shadow, religious or mythological themes, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, modernist, minimalist, abstract"
    },
    {
        "name": "artstyle-steampunk",
        "prompt": "steampunk style {prompt}. antique, mechanical, brass and copper tones, gears, intricate, detailed",
        "negative_prompt": "deformed, glitch, noisy, low contrast, anime, photorealistic"
    },
    {
        "name": "artstyle-surrealist",
        "prompt": "surrealist art {prompt}. dreamlike, mysterious, provocative, symbolic, intricate, detailed",
        "negative_prompt": "anime, photorealistic, realistic, deformed, glitch, noisy, low contrast"
    },
    {
        "name": "artstyle-typography",
        "prompt": "typographic art {prompt}. stylized, intricate, detailed, artistic, text-based",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "artstyle-watercolor",
        "prompt": "watercolor painting {prompt}. vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "futuristic-biomechanical",
        "prompt": "biomechanical style {prompt}. blend of organic and mechanical elements, futuristic, cybernetic, detailed, intricate",
        "negative_prompt": "natural, rustic, primitive, organic, simplistic"
    },
    {
        "name": "futuristic-biomechanical cyberpunk",
        "prompt": "biomechanical cyberpunk {prompt}. cybernetics, human-machine fusion, dystopian, organic meets artificial, dark, intricate, highly detailed",
        "negative_prompt": "natural, colorful, deformed, sketch, low contrast, watercolor"
    },
    {
        "name": "futuristic-cybernetic",
        "prompt": "cybernetic style {prompt}. futuristic, technological, cybernetic enhancements, robotics, artificial intelligence themes",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "futuristic-cybernetic robot",
        "prompt": "cybernetic robot {prompt}. android, AI, machine, metal, wires, tech, futuristic, highly detailed",
        "negative_prompt": "organic, natural, human, sketch, watercolor, low contrast"
    },
    {
        "name": "futuristic-cyberpunk cityscape",
        "prompt": "cyberpunk cityscape {prompt}. neon lights, dark alleys, skyscrapers, futuristic, vibrant colors, high contrast, highly detailed",
        "negative_prompt": "natural, rural, deformed, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "futuristic-futuristic",
        "prompt": "futuristic style {prompt}. sleek, modern, ultramodern, high tech, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vintage, antique"
    },
    {
        "name": "futuristic-retro cyberpunk",
        "prompt": "retro cyberpunk {prompt}. 80's inspired, synthwave, neon, vibrant, detailed, retro futurism",
        "negative_prompt": "modern, desaturated, black and white, realism, low contrast"
    },
    {
        "name": "futuristic-retro futurism",
        "prompt": "retro-futuristic {prompt}. vintage sci-fi, 50s and 60s style, atomic age, vibrant, highly detailed",
        "negative_prompt": "contemporary, realistic, rustic, primitive"
    },
    {
        "name": "futuristic-sci-fi",
        "prompt": "sci-fi style {prompt}. futuristic, technological, alien worlds, space themes, advanced civilizations",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, historical, medieval"
    },
    {
        "name": "futuristic-vaporwave",
        "prompt": "vaporwave style {prompt}. retro aesthetic, cyberpunk, vibrant, neon colors, vintage 80s and 90s style, highly detailed",
        "negative_prompt": "monochrome, muted colors, realism, rustic, minimalist, dark"
    },
    {
        "name": "game-bubble bobble",
        "prompt": "Bubble Bobble style {prompt}. 8-bit, cute, pixelated, fantasy, vibrant, reminiscent of Bubble Bobble game",
        "negative_prompt": "realistic, modern, photorealistic, violent, horror"
    },
    {
        "name": "game-cyberpunk game",
        "prompt": "cyberpunk game style {prompt}. neon, dystopian, futuristic, digital, vibrant, detailed, high contrast, reminiscent of cyberpunk genre video games",
        "negative_prompt": "historical, natural, rustic, low detailed"
    },
    {
        "name": "game-fighting game",
        "prompt": "fighting game style {prompt}. dynamic, vibrant, action-packed, detailed character design, reminiscent of fighting video games",
        "negative_prompt": "peaceful, calm, minimalist, photorealistic"
    },
    {
        "name": "game-gta",
        "prompt": "GTA-style artwork {prompt}. satirical, exaggerated, pop art style, vibrant colors, iconic characters, action-packed",
        "negative_prompt": "realistic, black and white, low contrast, impressionist, cubist, noisy, blurry, deformed"
    },
    {
        "name": "game-mario",
        "prompt": "Super Mario style {prompt}. vibrant, cute, cartoony, fantasy, playful, reminiscent of Super Mario series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "game-minecraft",
        "prompt": "Minecraft style {prompt}. blocky, pixelated, vibrant colors, recognizable characters and objects, game assets",
        "negative_prompt": "smooth, realistic, detailed, photorealistic, noise, blurry, deformed"
    },
    {
        "name": "game-pokemon",
        "prompt": "Pokémon style {prompt}. vibrant, cute, anime, fantasy, reminiscent of Pokémon series",
        "negative_prompt": "realistic, modern, horror, dystopian, violent"
    },
    {
        "name": "game-retro arcade",
        "prompt": "retro arcade style {prompt}. 8-bit, pixelated, vibrant, classic video game, old school gaming, reminiscent of 80s and 90s arcade games",
        "negative_prompt": "modern, ultra-high resolution, photorealistic, 3D"
    },
    {
        "name": "game-retro game",
        "prompt": "retro game art {prompt}. 16-bit, vibrant colors, pixelated, nostalgic, charming, fun",
        "negative_prompt": "realistic, photorealistic, 35mm film, deformed, glitch, low contrast, noisy"
    },
    {
        "name": "game-rpg fantasy game",
        "prompt": "role-playing game (RPG) style fantasy {prompt}. detailed, vibrant, immersive, reminiscent of high fantasy RPG games",
        "negative_prompt": "sci-fi, modern, urban, futuristic, low detailed"
    },
    {
        "name": "game-strategy game",
        "prompt": "strategy game style {prompt}. overhead view, detailed map, units, reminiscent of real-time strategy video games",
        "negative_prompt": "first-person view, modern, photorealistic"
    },
    {
        "name": "game-streetfighter",
        "prompt": "Street Fighter style {prompt}. vibrant, dynamic, arcade, 2D fighting game, highly detailed, reminiscent of Street Fighter series",
        "negative_prompt": "3D, realistic, modern, photorealistic, turn-based strategy"
    },
    {
        "name": "game-zelda",
        "prompt": "Legend of Zelda style {prompt}. vibrant, fantasy, detailed, epic, heroic, reminiscent of The Legend of Zelda series",
        "negative_prompt": "sci-fi, modern, realistic, horror"
    },
    {
        "name": "misc-architectural",
        "prompt": "architectural style {prompt}. clean lines, geometric shapes, minimalist, modern, architectural drawing, highly detailed",
        "negative_prompt": "curved lines, ornate, baroque, abstract, grunge"
    },
    {
        "name": "misc-disco",
        "prompt": "disco-themed {prompt}. vibrant, groovy, retro 70s style, shiny disco balls, neon lights, dance floor, highly detailed",
        "negative_prompt": "minimalist, rustic, monochrome, contemporary, simplistic"
    },
    {
        "name": "misc-dreamscape",
        "prompt": "dreamscape {prompt}. surreal, ethereal, dreamy, mysterious, fantasy, highly detailed",
        "negative_prompt": "realistic, concrete, ordinary, mundane"
    },
    {
        "name": "misc-dystopian",
        "prompt": "dystopian style {prompt}. bleak, post-apocalyptic, somber, dramatic, highly detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, cheerful, optimistic, vibrant, colorful"
    },
    {
        "name": "misc-fairy tale",
        "prompt": "fairy tale {prompt}. magical, fantastical, enchanting, storybook style, highly detailed",
        "negative_prompt": "realistic, modern, ordinary, mundane"
    },
    {
        "name": "misc-gothic",
        "prompt": "gothic style {prompt}. dark, mysterious, haunting, dramatic, ornate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, cheerful, optimistic"
    },
    {
        "name": "misc-grunge",
        "prompt": "grunge style {prompt}. textured, distressed, vintage, edgy, punk rock vibe, dirty, noisy",
        "negative_prompt": "smooth, clean, minimalist, sleek, modern, photorealistic"
    },
    {
        "name": "misc-horror",
        "prompt": "horror-themed {prompt}. eerie, unsettling, dark, spooky, suspenseful, grim, highly detailed",
        "negative_prompt": "cheerful, bright, vibrant, light-hearted, cute"
    },
    {
        "name": "misc-kawaii",
        "prompt": "kawaii style {prompt}. cute, adorable, brightly colored, cheerful, anime influence, highly detailed",
        "negative_prompt": "dark, scary, realistic, monochrome, abstract"
    },
    {
        "name": "misc-lovecraftian",
        "prompt": "lovecraftian horror {prompt}. eldritch, cosmic horror, unknown, mysterious, surreal, highly detailed",
        "negative_prompt": "light-hearted, mundane, familiar, simplistic, realistic"
    },
    {
        "name": "misc-macabre",
        "prompt": "macabre style {prompt}. dark, gothic, grim, haunting, highly detailed",
        "negative_prompt": "bright, cheerful, light-hearted, cartoonish, cute"
    },
    {
        "name": "misc-manga",
        "prompt": "manga style {prompt}. vibrant, high-energy, detailed, iconic, Japanese comic style",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, Western comic style"
    },
    {
        "name": "misc-metropolis",
        "prompt": "metropolis-themed {prompt}. urban, cityscape, skyscrapers, modern, futuristic, highly detailed",
        "negative_prompt": "rural, natural, rustic, historical, simple"
    },
    {
        "name": "misc-minimalist",
        "prompt": "minimalist style {prompt}. simple, clean, uncluttered, modern, elegant",
        "negative_prompt": "ornate, complicated, highly detailed, cluttered, disordered, messy, noisy"
    },
    {
        "name": "misc-monochrome",
        "prompt": "monochrome {prompt}. black and white, contrast, tone, texture, detailed",
        "negative_prompt": "colorful, vibrant, noisy, blurry, deformed"
    },
    {
        "name": "misc-nautical",
        "prompt": "nautical-themed {prompt}. sea, ocean, ships, maritime, beach, marine life, highly detailed",
        "negative_prompt": "landlocked, desert, mountains, urban, rustic"
    },
    {
        "name": "misc-space",
        "prompt": "space-themed {prompt}. cosmic, celestial, stars, galaxies, nebulas, planets, science fiction, highly detailed",
        "negative_prompt": "earthly, mundane, ground-based, realism"
    },
    {
        "name": "misc-stained glass",
        "prompt": "stained glass style {prompt}. vibrant, beautiful, translucent, intricate, detailed",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "misc-techwear fashion",
        "prompt": "techwear fashion {prompt}. futuristic, cyberpunk, urban, tactical, sleek, dark, highly detailed",
        "negative_prompt": "vintage, rural, colorful, low contrast, realism, sketch, watercolor"
    },
    {
        "name": "misc-tribal",
        "prompt": "tribal style {prompt}. indigenous, ethnic, traditional patterns, bold, natural colors, highly detailed",
        "negative_prompt": "modern, futuristic, minimalist, pastel"
    },
    {
        "name": "misc-zentangle",
        "prompt": "zentangle {prompt}. intricate, abstract, monochrome, patterns, meditative, highly detailed",
        "negative_prompt": "colorful, representative, simplistic, large fields of color"
    },
    {
        "name": "papercraft-collage",
        "prompt": "collage style {prompt}. mixed media, layered, textural, detailed, artistic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic"
    },
    {
        "name": "papercraft-flat papercut",
        "prompt": "flat papercut style {prompt}. silhouette, clean cuts, paper, sharp edges, minimalist, color block",
        "negative_prompt": "3D, high detail, noise, grainy, blurry, painting, drawing, photo, disfigured"
    },
    {
        "name": "papercraft-kirigami",
        "prompt": "kirigami representation of {prompt}. 3D, paper folding, paper cutting, Japanese, intricate, symmetrical, precision, clean lines",
        "negative_prompt": "painting, drawing, 2D, noisy, blurry, deformed"
    },
    {
        "name": "papercraft-paper mache",
        "prompt": "paper mache representation of {prompt}. 3D, sculptural, textured, handmade, vibrant, fun",
        "negative_prompt": "2D, flat, photo, sketch, digital art, deformed, noisy, blurry"
    },
    {
        "name": "papercraft-paper quilling",
        "prompt": "paper quilling art of {prompt}. intricate, delicate, curling, rolling, shaping, coiling, loops, 3D, dimensional, ornamental",
        "negative_prompt": "photo, painting, drawing, 2D, flat, deformed, noisy, blurry"
    },
    {
        "name": "papercraft-papercut collage",
        "prompt": "papercut collage of {prompt}. mixed media, textured paper, overlapping, asymmetrical, abstract, vibrant",
        "negative_prompt": "photo, 3D, realistic, drawing, painting, high detail, disfigured"
    },
    {
        "name": "papercraft-papercut shadow box",
        "prompt": "3D papercut shadow box of {prompt}. layered, dimensional, depth, silhouette, shadow, papercut, handmade, high contrast",
        "negative_prompt": "painting, drawing, photo, 2D, flat, high detail, blurry, noisy, disfigured"
    },
    {
        "name": "papercraft-stacked papercut",
        "prompt": "stacked papercut art of {prompt}. 3D, layered, dimensional, depth, precision cut, stacked layers, papercut, high contrast",
        "negative_prompt": "2D, flat, noisy, blurry, painting, drawing, photo, deformed"
    },
    {
        "name": "papercraft-thick layered papercut",
        "prompt": "thick layered papercut art of {prompt}. deep 3D, volumetric, dimensional, depth, thick paper, high stack, heavy texture, tangible layers",
        "negative_prompt": "2D, flat, thin paper, low stack, smooth texture, painting, drawing, photo, deformed"
    },
    {
        "name": "photo-alien",
        "prompt": "alien-themed {prompt}. extraterrestrial, cosmic, otherworldly, mysterious, sci-fi, highly detailed",
        "negative_prompt": "earthly, mundane, common, realistic, simple"
    },
    {
        "name": "photo-film noir",
        "prompt": "film noir style {prompt}. monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, realism, photorealistic, vibrant, colorful"
    },
    {
        "name": "photo-hdr",
        "prompt": "HDR photo of {prompt}. High dynamic range, vivid, rich details, clear shadows and highlights, realistic, intense, enhanced contrast, highly detailed",
        "negative_prompt": "flat, low contrast, oversaturated, underexposed, overexposed, blurred, noisy"
    },
    {
        "name": "photo-long exposure",
        "prompt": "long exposure photo of {prompt}. Blurred motion, streaks of light, surreal, dreamy, ghosting effect, highly detailed",
        "negative_prompt": "static, noisy, deformed, shaky, abrupt, flat, low contrast"
    },
    {
        "name": "photo-neon noir",
        "prompt": "neon noir {prompt}. cyberpunk, dark, rainy streets, neon signs, high contrast, low light, vibrant, highly detailed",
        "negative_prompt": "bright, sunny, daytime, low contrast, black and white, sketch, watercolor"
    },
    {
        "name": "photo-silhouette",
        "prompt": "silhouette style {prompt}. high contrast, minimalistic, black and white, stark, dramatic",
        "negative_prompt": "ugly, deformed, noisy, blurry, low contrast, color, realism, photorealistic"
    },
    {
        "name": "photo-tilt-shift",
        "prompt": "tilt-shift photo of {prompt}. Selective focus, miniature effect, blurred background, highly detailed, vibrant, perspective control",
        "negative_prompt": "blurry, noisy, deformed, flat, low contrast, unrealistic, oversaturated, underexposed"
    },
    
    {
        "name": "Watercolor",
        "prompt": "watercolor painting, {prompt}. vibrant, beautiful, painterly, detailed, textural, artistic",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, anime, photorealistic, 35mm film, deformed, glitch, low contrast, noisy",
    },
    {
        "name": "Film Noir",
        "prompt": "film noir style, ink sketch|vector, {prompt} highly detailed, sharp focus, ultra sharpness, monochrome, high contrast, dramatic shadows, 1940s style, mysterious, cinematic",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Neon",
        "prompt": "masterpiece painting, buildings in the backdrop, kaleidoscope, lilac orange blue cream fuchsia bright vivid gradient colors, the scene is cinematic, {prompt}, emotional realism, double exposure, watercolor ink pencil, graded wash, color layering, magic realism, figurative painting, intricate motifs, organic tracery, polished",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Jungle",
        "prompt": 'waist-up "{prompt} in a Jungle" by Syd Mead, tangerine cold color palette, muted colors, detailed, 8k, photo r3al, dripping paint, 3d toon style, 3d style, Movie Still',
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Mars",
        "prompt": "{prompt}, Post-apocalyptic. Mars Colony, Scavengers roam the wastelands searching for valuable resources, rovers, bright morning sunlight shining, detailed, intricate, 8k, HDR, cinematic lighting, sharp focus",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Vibrant Color",
        "prompt": "vibrant colorful, ink sketch|vector|2d colors, at nightfall, sharp focus, {prompt}, highly detailed, crisp, refreshing, colorful, ultra sharpness",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "Snow",
        "prompt": "cinema 4d render, {prompt}, high contrast, vibrant and saturated, sico style, surrounded by magical glow, floating ice shards, snow crystals, cold, windy background, frozen natural landscape in background  cinematic atmosphere,highly detailed, sharp focus, intricate design, 3d, unreal engine, octane render, CG best quality, highres, photorealistic, dramatic lighting, artstation, concept art, cinematic, epic Steven Spielberg movie still, sharp focus, smoke, sparks, art by pascal blanche and greg rutkowski and repin, trending on artstation, hyperrealism painting, matte painting, 4k resolution",
        "negative_prompt": "lowres, low quality, worst quality, text, watermark, frame, deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, photo, pet collar, gun, weapon, blue, 3d, drones, drone, buildings in background, green",
    },
    {
        "name": "MK Chromolithography",
        "prompt": "Chromolithograph {prompt}. Vibrant colors, intricate details, rich color saturation, meticulous registration, multi-layered printing, decorative elements, historical charm, artistic reproductions, commercial posters, nostalgic, ornate compositions.",
        "negative_prompt": "monochromatic, simple designs, limited color palette, imprecise registration, minimalistic, modern aesthetic, digital appearance."
    },
    {
        "name": "MK Cross Processing Print",
        "prompt": "Cross processing print {prompt}. Experimental color shifts, unconventional tonalities, vibrant and surreal hues, heightened contrasts, unpredictable results, artistic unpredictability, retro and vintage feel, dynamic color interplay, abstract and dreamlike.",
        "negative_prompt": "predictable color tones, traditional processing, realistic color representation, subdued contrasts, standard photographic aesthetics."
    },
    {
        "name": "MK Dufaycolor Photograph",
        "prompt": "Dufaycolor photograph {prompt}. Vintage color palette, distinctive color rendering, soft and dreamy atmosphere, historical charm, unique color process, grainy texture, evocative mood, nostalgic aesthetic, hand-tinted appearance, artistic patina.",
        "negative_prompt": "modern color reproduction, hyperrealistic tones, sharp and clear details, digital precision, contemporary aesthetic."
    },
    {
        "name": "MK Herbarium",
        "prompt": "Herbarium drawing{prompt}. Botanical accuracy, old botanical book illustration, detailed illustrations, pressed plants, delicate and precise linework, scientific documentation, meticulous presentation, educational purpose, organic compositions, timeless aesthetic, naturalistic beauty.",
        "negative_prompt": "abstract representation, vibrant colors, artistic interpretation, chaotic compositions, fantastical elements, digital appearance."
    },
    {
        "name": "MK Punk Collage",
        "prompt": "Punk collage style {prompt}. mixed media, papercut,textured paper, overlapping, ripped posters, safety pins, chaotic layers, graffiti-style elements, anarchy symbols, vintage photos, cut-and-paste aesthetic, bold typography, distorted images, political messages, urban decay, distressed textures, newspaper clippings, spray paint, rebellious icons, DIY spirit, vivid colors, punk band logos, edgy and raw compositions, ",
        "negative_prompt": "conventional, blurry, noisy, low contrast"
    },
    {
        "name": "MK mosaic",
        "prompt": "mosaic style {prompt}. fragmented, assembled, colorful, highly detailed",
        "negative_prompt": "whole, unbroken, monochrome"
    },
    {
        "name": "MK Van Gogh",
        "prompt": "Oil painting by Van Gogh {prompt}. Expressive, impasto, swirling brushwork, vibrant, brush strokes, Brushstroke-heavy, Textured, Impasto, Colorful, Dynamic, Bold, Distinctive, Vibrant, Whirling, Expressive, Dramatic, Swirling, Layered, Intense, Contrastive, Atmospheric, Luminous, Textural, Evocative, SpiraledVan Gogh style",
        "negative_prompt": "realistic, photorealistic, calm, straight lines, signature, frame, text, watermark"
    },
    {
        "name": "MK Coloring Book",
        "prompt": "Centered black and white high contrast line drawing, coloring book style, {prompt}. monochrome, blank white background",
        "negative_prompt": "greyscale, gradients, shadows,shadow, colored, Red, Blue, Yellow, Green, Orange, Purple, Pink, Brown, Gray, Beige, Turquoise, Lavender, Cyan, Magenta, Olive, Indigo, black background"
    },
    {
        "name": "MK Singer Sargent",
        "prompt": "Oil painting by John Singer Sargent, {prompt}. Elegant, refined, masterful technique,realistic portrayal, subtle play of light, captivating expression, rich details, harmonious colors, skillful composition, brush strokes, chiaroscuro.",
        "negative_prompt": "realistic, photorealistic, abstract, overly stylized, excessive contrasts, distorted, bright colors,disorder."
    },
    {
        "name": "MK Pollock",
        "prompt": "Oil painting by Jackson Pollock, {prompt}. Abstract expressionism, drip painting, chaotic composition, energetic, spontaneous, unconventional technique, dynamic, bold, distinctive, vibrant, intense, expressive, energetic, layered, non-representational, gestural.",
        "negative_prompt": "(realistic)1.5, (photorealistic)1.5, representational, calm, ordered composition, precise lines, detailed forms, subdued colors, quiet, static, traditional, figurative."
    },
    {
        "name": "MK Basquiat",
        "prompt": "Artwork by Jean-Michel Basquiat, {prompt}. Neo-expressionism, street art influence, graffiti-inspired, raw, energetic, bold colors, dynamic composition, chaotic, layered, textural, expressive, spontaneous, distinctive, symbolic,energetic brushstrokes.",
        "negative_prompt": "(realistic)1.5, (photorealistic)1.5, calm, precise lines, conventional composition, subdued"    
	},
	{
       "name": "MK Andy Warhol",
       "prompt": "Artwork in the style of Andy Warhol, {prompt}. Pop art, vibrant colors, bold compositions, repetition of iconic imagery, celebrity culture, commercial aesthetics, mass production influence, stylized simplicity, cultural commentary, graphical elements, distinctive portraits.",
       "negative_prompt": "subdued colors, realistic, lack of repetition, minimalistic."
    },
    {
        "name": "MK Halftone print",
        "prompt": "Halftone print {prompt}. Dot matrix pattern, grayscale tones, vintage aesthetic, newspaper print vibe, stylized dots, visual texture, black and white contrasts, retro appearance, artistic pointillism,pop culture, (Roy Lichtenstein style)1.5.",
        "negative_prompt": "smooth gradients, continuous tones, vibrant colors."
    },
    {
        "name": "MK Gond Painting",
        "prompt": "Gond painting {prompt}. Intricate patterns, vibrant colors, detailed motifs, nature-inspired themes, tribal folklore, fine lines, intricate detailing, storytelling compositions, mystical and folkloric, cultural richness.",
        "negative_prompt": "monochromatic, abstract shapes, minimalistic."
    },
    {
        "name": "MK Albumen Print",
        "prompt": "Albumen print {prompt}. Sepia tones, fine details, subtle tonal gradations, delicate highlights, vintage aesthetic, soft and muted atmosphere, historical charm, rich textures, meticulous craftsmanship, classic photographic technique, vignetting.",
        "negative_prompt": "vibrant colors, high contrast, modern, digital appearance, sharp details, contemporary style."
    },
    {
        "name": "MK Aquatint Print",
        "prompt": "Aquatint print {prompt}. Soft tonal gradations, atmospheric effects, velvety textures, rich contrasts, fine details, etching process, delicate lines, nuanced shading, expressive and moody atmosphere, artistic depth.",
        "negative_prompt": "sharp contrasts, bold lines, minimalistic."
    },
    {
        "name": "MK Anthotype Print",
        "prompt": "Anthotype print {prompt}. Monochrome dye, soft and muted colors, organic textures, ephemeral and delicate appearance, low details, watercolor canvas, low contrast, overexposed, silhouette, textured paper.",
        "negative_prompt": "vibrant synthetic dyes, bold and saturated colors."
    },
    {
        "name": "MK Inuit Carving",
        "prompt": "Inuit art {prompt} made of ivory. Sculptures, intricate carvings, natural materials, storytelling motifs, arctic wildlife themes, symbolic representations, cultural traditions, earthy tones, harmonious compositions, spiritual and mythological elements.",
        "negative_prompt": "abstract, vibrant colors."
    },
    {
        "name": "MK Bromoil Print",
        "prompt": "Bromoil print {prompt}. Painterly effects, sepia tones, textured surfaces, rich contrasts, expressive brushwork, tonal variations, vintage aesthetic, atmospheric mood, handmade quality, artistic experimentation, darkroom craftsmanship, vignetting.",
        "negative_prompt": "smooth surfaces, minimal brushwork, contemporary digital appearance."
    },
    {
        "name": "MK Calotype Print",
        "prompt": "Calotype print {prompt}. Soft focus, subtle tonal range, paper negative process, fine details, vintage aesthetic, artistic experimentation, atmospheric mood, early photographic charm, handmade quality, vignetting.",
        "negative_prompt": "sharp focus, bold contrasts, modern aesthetic, digital photography."
    },
    {
        "name": "MK Color Sketchnote",
        "prompt": "Color sketchnote {prompt}. Hand-drawn elements, vibrant colors, visual hierarchy, playful illustrations, varied typography, graphic icons, organic and dynamic layout, personalized touches, creative expression, engaging storytelling.",
        "negative_prompt": "monochromatic, geometric layout."
    },
    {
        "name": "MK Cibulak Porcelain",
        "prompt": "A sculpture made of blue pattern porcelain of {prompt}. Classic design, blue and white color scheme, intricate detailing, floral motifs, onion-shaped elements, historical charm, rococo, white ware, cobalt blue, underglaze pattern, fine craftsmanship, traditional elegance, delicate patterns, vintage aesthetic, Meissen, Blue Onion pattern, Cibulak.",
        "negative_prompt": "tea, teapot, cup, teacup, bright colors, bold and modern design, absence of intricate detailing, lack of floral motifs, non-traditional shapes."
    },
    {
        "name": "MK Alcohol Ink Art",
        "prompt": "Alcohol ink art {prompt}. Fluid and vibrant colors, unpredictable patterns, organic textures, translucent layers, abstract compositions, ethereal and dreamy effects, free-flowing movement, expressive brushstrokes, contemporary aesthetic, wet textured paper.",
        "negative_prompt": "monochromatic, controlled patterns."
    },
    {
        "name": "MK One Line Art",
        "prompt": "One line art {prompt}. Continuous and unbroken black line, minimalistic, simplicity, economical use of space, flowing and dynamic, symbolic representations, contemporary aesthetic, evocative and abstract, white background.",
        "negative_prompt": "disjointed lines, complexity, complex detailing."
    },
    {
        "name": "MK Blacklight Paint",
        "prompt": "Blacklight paint {prompt}. Fluorescent pigments, vibrant and surreal colors, ethereal glow, otherworldly effects, dynamic and psychedelic compositions, neon aesthetics, transformative in ultraviolet light, contemporary and experimental.",
        "negative_prompt": "muted colors, traditional and realistic compositions."
    },
    {
        "name": "MK Carnival Glass",
        "prompt": "Carnival glass {prompt}. Iridescent surfaces, vibrant colors, intricate patterns, opalescent hues, reflective and prismatic effects, Art Nouveau and Art Deco influences, vintage charm, intricate detailing, lustrous and luminous appearance.",
        "negative_prompt": "non-iridescent surfaces, muted colors, absence of intricate patterns, lack of opalescent hues, modern and minimalist aesthetic."
    },
    {
        "name": "MK Cyanotype Print",
        "prompt": "Cyanotype print {prompt}. Prussian blue tones, distinctive coloration, high contrast, blueprint aesthetics, atmospheric mood, sun-exposed paper, silhouette effects, delicate details, historical charm, handmade and experimental quality.",
        "negative_prompt": "vibrant colors, low contrast, modern and polished appearance."
    },
    {
        "name": "MK Cross-Stitching",
        "prompt": "Cross-stitching {prompt}. Intricate patterns, embroidery thread, sewing, fine details, precise stitches, textile artistry, symmetrical designs, varied color palette, traditional and contemporary motifs, handmade and crafted,canvas, nostalgic charm.",
        "negative_prompt": "paper, paint, ink, photography."
    },
    {
        "name": "MK Encaustic Paint",
        "prompt": "Encaustic paint {prompt}. Textured surfaces, translucent layers, luminous quality, wax medium, rich color saturation, fluid and organic shapes, contemporary and historical influences, mixed media elements, atmospheric depth.",
        "negative_prompt": "flat surfaces, opaque layers, lack of wax medium, muted color palette, absence of textured surfaces, non-mixed media."
    },
    {
        "name": "MK Embroidery",
        "prompt": "Embroidery {prompt}. Intricate stitching, embroidery thread, fine details, varied thread textures, textile artistry, embellished surfaces, diverse color palette, traditional and contemporary motifs, handmade and crafted, tactile and ornate.",
        "negative_prompt": "minimalist, monochromatic."
    },
    {
        "name": "MK Gyotaku",
        "prompt": "Gyotaku {prompt}. Fish impressions, realistic details, ink rubbings, textured surfaces, traditional Japanese art form, nature-inspired compositions, artistic representation of marine life, black and white contrasts, cultural significance.",
        "negative_prompt": "photography."
    },
    {
        "name": "MK Luminogram",
        "prompt": "Luminogram {prompt}. Photogram technique, ethereal and abstract effects, light and shadow interplay, luminous quality, experimental process, direct light exposure, unique and unpredictable results, artistic experimentation.",
        "negative_prompt": ""
    },
    {
        "name": "MK Lite Brite Art",
        "prompt": "Lite Brite art {prompt}. Luminous and colorful designs, pixelated compositions, retro aesthetic, glowing effects, creative patterns, interactive and playful, nostalgic charm, vibrant and dynamic arrangements.",
        "negative_prompt": "monochromatic."
    },
    {
        "name": "MK Mokume-gane",
        "prompt": "Mokume-gane {prompt}. Wood-grain patterns, mixed metal layers, intricate and organic designs, traditional Japanese metalwork, harmonious color combinations, artisanal craftsmanship, unique and layered textures, cultural and historical significance.",
        "negative_prompt": "uniform metal surfaces."
    },
    {
        "name": "MK Pebble Art",
        "prompt": "a sculpture made of peebles, {prompt}. Pebble art style, natural materials, textured surfaces, balanced compositions, organic forms, harmonious arrangements, tactile and 3D effects, beach-inspired aesthetic, creative storytelling, artisanal craftsmanship.",
        "negative_prompt": "non-natural materials, lack of textured surfaces, imbalanced compositions, absence of organic forms, non-tactile appearance."
    },
    {
        "name": "MK Palekh",
        "prompt": "Palekh art {prompt}. Miniature paintings, intricate details, vivid colors, folkloric themes, lacquer finish, storytelling compositions, symbolic elements, Russian folklore influence, cultural and historical significance.",
        "negative_prompt": "large-scale paintings."
    },
    {
        "name": "MK Suminagashi",
        "prompt": "Suminagashi {prompt}. Floating ink patterns, marbled effects, delicate and ethereal designs, water-based ink, fluid and unpredictable compositions, meditative process, monochromatic or subtle color palette, Japanese artistic tradition.",
        "negative_prompt": "vibrant and bold color palette."
    },
    {
        "name": "MK Scrimshaw",
        "prompt": "Scrimshaw {prompt}. Intricate engravings on a spermwhale's teeth, marine motifs, detailed scenes, nautical themes, black and white contrasts, historical craftsmanship, artisanal carving, storytelling compositions, maritime heritage.",
        "negative_prompt": "colorful, modern."
    },
    {
        "name": "MK Shibori",
        "prompt": "Shibori {prompt}. Textured fabric, intricate patterns, resist-dyeing technique, indigo or vibrant colors, organic and flowing designs, Japanese textile art, cultural tradition, tactile and visual interest.",
        "negative_prompt": "monochromatic."
    },
    {
        "name": "MK Vitreous Enamel",
        "prompt": "Vitreous enamel {prompt}. Smooth and glossy surfaces, vibrant colors, glass-like finish, durable and resilient, intricate detailing, traditional and contemporary applications, artistic craftsmanship, jewelry and decorative objects.",
        "negative_prompt": "rough surfaces, muted colors."
    },
    {
        "name": "MK Ukiyo-e",
        "prompt": "Ukiyo-e {prompt}. Woodblock prints, vibrant colors, intricate details, depictions of landscapes, kabuki actors, beautiful women, cultural scenes, traditional Japanese art, artistic craftsmanship, historical significance.",
        "negative_prompt": "absence of woodblock prints, muted colors, lack of intricate details, non-traditional Japanese themes, absence of cultural scenes."
    },
    {
        "name": "MK vintage-airline-poster",
        "prompt": "Vintage airline poster {prompt}. classic aviation fonts, pastel colors, elegant aircraft illustrations, scenic destinations, distressed textures, retro travel allure",
        "negative_prompt": "modern fonts, bold colors, hyper-realistic, sleek design"
    },
    {
        "name": "MK vintage-travel-poster",
        "prompt": "Vintage travel poster {prompt}. retro fonts, muted colors, scenic illustrations, iconic landmarks, distressed textures, nostalgic vibes",
        "negative_prompt": "modern fonts, vibrant colors, hyper-realistic, sleek design"
    },
    {
        "name": "MK bauhaus-style",
        "prompt": "Bauhaus-inspired {prompt}. minimalism, geometric precision, primary colors, sans-serif typography, asymmetry, functional design",
        "negative_prompt": "ornate, intricate, excessive detail, complex patterns, serif typography"
    },
    {
        "name": "MK afrofuturism",
        "prompt": "Afrofuturism {prompt}. vibrant colors, futuristic elements, cultural symbolism, cosmic imagery, dynamic patterns, empowering narratives",
        "negative_prompt": "monochromatic"
    },
    {
        "name": "MK atompunk",
        "prompt": "Atompunk {prompt}. retro-futuristic, atomic age aesthetics, sleek lines, metallic textures, futuristic technology, optimism, energy",
        "negative_prompt": "organic, natural textures, rustic, dystopian"
    },
    {
        "name": "MK constructivism",
        "prompt": "Constructivism {prompt}. geometric abstraction, bold colors, industrial aesthetics, dynamic compositions, utilitarian design, revolutionary spirit",
        "negative_prompt": "organic shapes, muted colors, ornate elements, traditional"
    },
    {
        "name": "MK chicano-art",
        "prompt": "Chicano art {prompt}. bold colors, cultural symbolism, muralism, lowrider aesthetics, barrio life, political messages, social activism, Mexico",
        "negative_prompt": "monochromatic, minimalist, mainstream aesthetics"
    },
    {
        "name": "MK de-stijl",
        "prompt": "De Stijl {prompt}. neoplasticism, primary colors, geometric abstraction, horizontal and vertical lines, simplicity, harmony, utopian ideals",
        "negative_prompt": "complex patterns, muted colors, ornate elements, asymmetry"
    },
    {
        "name": "MK dayak-art",
        "prompt": "Dayak art {prompt}. intricate patterns, nature-inspired motifs, vibrant colors, traditional craftsmanship, cultural symbolism, storytelling",
        "negative_prompt": "minimalist, monochromatic, modern"
    },
    {
        "name": "MK fayum-portrait",
        "prompt": "Fayum portrait {prompt}. encaustic painting, realistic facial features, warm earth tones, serene expressions, ancient Egyptian influences",
        "negative_prompt": "abstract, vibrant colors, exaggerated features, modern"
    },
    {
        "name": "MK illuminated-manuscript",
        "prompt": "Illuminated manuscript {prompt}. intricate calligraphy, rich colors, detailed illustrations, gold leaf accents, ornate borders, religious, historical, medieval",
        "negative_prompt": "modern typography, minimalist design, monochromatic, abstract themes"
    },
    {
        "name": "MK kalighat-painting",
        "prompt": "Kalighat painting {prompt}. bold lines, vibrant colors, narrative storytelling, cultural motifs, flat compositions, expressive characters",
        "negative_prompt": "subdued colors, intricate details, realistic portrayal, modern aesthetics"
    },
    {
        "name": "MK madhubani-painting",
        "prompt": "Madhubani painting {prompt}. intricate patterns, vibrant colors, nature-inspired motifs, cultural storytelling, symmetry, folk art aesthetics",
        "negative_prompt": "abstract, muted colors, minimalistic design, modern aesthetics"
    },
    {
        "name": "MK pictorialism",
        "prompt": "Pictorialism illustration {prompt}. soft focus, atmospheric effects, artistic interpretation, tonality, muted colors, evocative storytelling",
        "negative_prompt": "sharp focus, high contrast, realistic depiction, vivid colors"
    },
    {
        "name": "MK pichwai-painting",
        "prompt": "Pichwai painting {prompt}. intricate detailing, vibrant colors, religious themes, nature motifs, devotional storytelling, gold leaf accents",
        "negative_prompt": "minimalist, subdued colors, abstract design"
    },
    {
        "name": "MK patachitra-painting",
        "prompt": "Patachitra painting {prompt}. bold outlines, vibrant colors, intricate detailing, mythological themes, storytelling, traditional craftsmanship",
        "negative_prompt": "subdued colors, minimalistic, abstract, modern aesthetics"
    },
    {
        "name": "MK samoan-art-inspired",
        "prompt": "Samoan art-inspired {prompt}. traditional motifs, natural elements, bold colors, cultural symbolism, storytelling, craftsmanship",
        "negative_prompt": "modern aesthetics, minimalist, abstract"
    },
    {
        "name": "MK tlingit-art",
        "prompt": "Tlingit art {prompt}. formline design, natural elements, animal motifs, bold colors, cultural storytelling, traditional craftsmanship, Alaska traditional art, (totem)1.5",
        "negative_prompt": ""
    },
    {
        "name": "MK adnate-style",
        "prompt": "Painting by Adnate {prompt}. realistic portraits, street art, large-scale murals, subdued color palette, social narratives",
        "negative_prompt": "abstract, vibrant colors, small-scale art"
    },
    {
        "name": "MK ron-english-style",
        "prompt": "Painting by Ron English, {prompt}. pop-surrealism, cultural subversion, iconic mash-ups, vibrant and bold colors, satirical commentary",
        "negative_prompt": "traditional, monochromatic"
    },
    {
        "name": "MK shepard-fairey-style",
        "prompt": "Painting by Shepard Fairey, {prompt}. street art, political activism, iconic stencils, bold typography, high contrast, red, black, and white color palette",
        "negative_prompt": "traditional, muted colors"
    }
]

prompt_styles = {k['name']: (k['prompt'], k['negative_prompt']) for k in prompt_styles}
style_keys = list(prompt_styles.keys())


SD_XL_BASE_RATIOS = {
    "0.25": (512, 2048),
    "0.26": (512, 1984),
    "0.27": (512, 1920),
    "0.28": (512, 1856),
    "0.32": (576, 1792),
    "0.33": (576, 1728),
    "0.35": (576, 1664),
    "0.4": (640, 1600),
    "0.42": (640, 1536),
    "0.48": (704, 1472),
    "0.5": (704, 1408),
    "0.52": (704, 1344),
    "0.57": (768, 1344),
    "0.6": (768, 1280),
    "0.68": (832, 1216),
    "0.72": (832, 1152),
    "0.78": (896, 1152),
    "0.82": (896, 1088),
    "0.88": (960, 1088),
    "0.94": (960, 1024),
    "1.0": (1024, 1024),
    "1.07": (1024, 960),
    "1.13": (1088, 960),
    "1.21": (1088, 896),
    "1.29": (1152, 896),
    "1.38": (1152, 832),
    "1.46": (1216, 832),
    "1.67": (1280, 768),
    "1.75": (1344, 768),
    "1.91": (1344, 704),
    "2.0": (1408, 704),
    "2.09": (1472, 704),
    "2.4": (1536, 640),
    "2.5": (1600, 640),
    "2.89": (1664, 576),
    "3.0": (1728, 576),
    "3.11": (1792, 576),
    "3.62": (1856, 512),
    "3.75": (1920, 512),
    "3.88": (1984, 512),
    "4.0": (2048, 512),
}

aspect_ratios = {str(v[0])+'×'+str(v[1]):v for k, v in SD_XL_BASE_RATIOS.items()}

def apply_style(style, positive, negative):
    p, n = prompt_styles.get(style, default_style)
    return p.replace('{prompt}', positive), n + ', ' + negative
#From https://github.com/TonyLianLong/LLM-groundedDiffusion/blob/main/prompt.py
llm_template = """You are an intelligent bounding box generator. I will provide you with a caption for a photo, image, or painting. Your task is to generate the bounding boxes for the objects mentioned in the caption, along with a background prompt describing the scene. The images are of size {width}x{height}. The top-left corner has coordinate [0, 0]. The bottom-right corner has coordinnate [{width}, {height}]. The bounding boxes should not overlap or go beyond the image boundaries. Each bounding box should be in the format of (object name, [top-left x coordinate, top-left y coordinate, box width, box height]) and should not include more than one object. Do not put objects that are already provided in the bounding boxes into the background prompt. Do not include non-existing or excluded objects in the background prompt. Use "A realistic scene" as the background prompt if no background is given in the prompt. If needed, you can make reasonable guesses. Please refer to the example below for the desired format.

Caption: A realistic image of landscape scene depicting a green car parking on the left of a blue truck, with a red air balloon and a bird in the sky
Objects: [('a green car', [21, 281, 211, 159]), ('a blue truck', [269, 283, 209, 160]), ('a red air balloon', [66, 8, 145, 135]), ('a bird', [296, 42, 143, 100])]
Background prompt: A realistic landscape scene
Negative prompt: 

Caption: A realistic top-down view of a wooden table with two apples on it
Objects: [('a wooden table', [20, 148, 472, 216]), ('an apple', [150, 226, 100, 100]), ('an apple', [280, 226, 100, 100])]
Background prompt: A realistic top-down view
Negative prompt: 

Caption: A realistic scene of three skiers standing in a line on the snow near a palm tree
Objects: [('a skier', [5, 152, 139, 168]), ('a skier', [278, 192, 121, 158]), ('a skier', [148, 173, 124, 155]), ('a palm tree', [404, 105, 103, 251])]
Background prompt: A realistic outdoor scene with snow
Negative prompt: 

Caption: An oil painting of a pink dolphin jumping on the left of a steam boat on the sea
Objects: [('a steam boat', [232, 225, 257, 149]), ('a jumping pink dolphin', [21, 249, 189, 123])]
Background prompt: An oil painting of the sea
Negative prompt: 

Caption: A cute cat and an angry dog without birds
Objects: [('a cute cat', [51, 67, 271, 324]), ('an angry dog', [302, 119, 211, 228])]
Background prompt: A realistic scene
Negative prompt: birds

Caption: Two pandas in a forest without flowers
Objects: [('a panda', [30, 171, 212, 226]), ('a panda', [264, 173, 222, 221])]
Background prompt: A forest
Negative prompt: flowers

Caption: An oil painting of a living room scene without chairs with a painting mounted on the wall, a cabinet below the painting, and two flower vases on the cabinet
Objects: [('a painting', [88, 85, 335, 203]), ('a cabinet', [57, 308, 404, 201]), ('a flower vase', [166, 222, 92, 108]), ('a flower vase', [328, 222, 92, 108])]
Background prompt: An oil painting of a living room scene
Negative prompt: chairs

Caption: {prompt}
Objects: """

# prompt_full = llm_template.format(prompt=prompt.strip().rstrip("."))
DEFAULT_SO_NEGATIVE_PROMPT = "artifacts, blurry, smooth texture, bad quality, distortions, unrealistic, distorted image, bad proportions, duplicate, two, many, group, occlusion, occluded, side, border, collate"
DEFAULT_OVERALL_NEGATIVE_PROMPT = "artifacts, blurry, smooth texture, bad quality, distortions, unrealistic, distorted image, bad proportions, duplicate"
