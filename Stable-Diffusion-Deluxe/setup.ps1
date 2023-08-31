powershell Start-Process powershell -Verb runAs
if not EXIST .\venv (python -m venv .\venv)
Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py
cd .\venv\Scripts
.\Activate.ps1
cd ..
python -m pip install --upgrade pip
python -m pip install --upgrade flet
flet .\Stable-Diffusion-Deluxe.py
& .\deactivate.bat
exit /B 1