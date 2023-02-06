# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata
datas = []
binaries = []
hiddenimports = ['requests', 'torch', 'huggingface-hub', 'transformers', 'tqdm', 'regex', 'https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]']
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('transformers')
datas += copy_metadata('numpy')
datas += copy_metadata('numba')
datas += copy_metadata('tokenizers')
tmp_ret = collect_all('tqdm')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('transformers')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('regex')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
#pyinstaller Stable-Diffusion-Deluxe.spec -y

block_cipher = None


a = Analysis(
    ['Stable-Diffusion-Deluxe.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
splash = Splash('SDD-Icon-Transparent-512.png',
                binaries=a.binaries,
                datas=a.datas,
                text_pos=(10, 50),
                text_size=18,
                text_color='green')

exe = EXE(
    pyz,
    splash,
    splash.binaries,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Stable-Diffusion-Deluxe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['favicon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Stable-Diffusion-Deluxe',
)
