@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
if not EXIST .\venv (python3 -m venv .\venv)
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Scripts\Stable-Diffusion-Deluxe.py"
cd .\venv\Scripts
call .\activate.bat
python3 -m pip install --upgrade --quiet pip
python3 -m pip install --upgrade --quiet flet
flet .\Stable-Diffusion-Deluxe.py
call .\deactivate.bat
exit /B 1