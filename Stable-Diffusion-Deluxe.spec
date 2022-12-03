# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata
# pyinstaller Stable-Diffusion-Deluxe.py --hidden-import=requests --hidden-import=huggingface-hub --hidden-import=transformers --hidden-import=tqdm --hidden-import=regex  --hidden-import=git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch] --collect-all=tqdm --collect-all=git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]  --collect-all=transformers --collect-all=regex --collect-all=stability_api --copy-metadata=requests --copy-metadata=packaging --copy-metadata=filelock --copy-metadata=transformers --copy-metadata=numpy --copy-metadata=numba --copy-metadata=tokenizers
datas = []
binaries = []
hiddenimports = ['requests', 'huggingface-hub', 'transformers', 'tqdm', 'regex', 'stability_api', 'tensors_pb2', 'torch.jit', 'git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]', 'stability_sdk.interfaces.gooseai.generation.generation_pb2']
datas += copy_metadata('requests')
datas += copy_metadata('packaging')
datas += copy_metadata('filelock')
datas += copy_metadata('transformers')
datas += copy_metadata('numpy')
datas += copy_metadata('numba')
datas += copy_metadata('tokenizers')
tmp_ret = collect_all('tqdm')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('git+https://github.com/Skquark/diffusers.git@main#egg=diffusers[torch]')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('transformers')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('regex')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('stability_api')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


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

exe = EXE(
    pyz,
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
