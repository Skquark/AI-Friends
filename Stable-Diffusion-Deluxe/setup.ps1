cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
if not EXIST .\venv (python -m venv .\venv)
Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Scripts\Stable-Diffusion-Deluxe.py
copy .\Stable-Diffusion-Deluxe.py .\venv\Scripts\
cd .\venv\Scripts
.\Activate.ps1
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade flet
flet .\Stable-Diffusion-Deluxe.py
.\deactivate.bat
exit /B 1