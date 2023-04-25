@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO NOPYTHON
echo Downloading latest Stable Diffusion Deluxe and running in a Python Virtual Environment
if not EXIST .\venv (python3 -m venv .\venv)
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py"
cd .\venv
call .\Scripts\activate.bat
python3 -m pip install --upgrade --quiet pip
python3 -m pip install --upgrade --quiet flet
cls
flet .\Stable-Diffusion-Deluxe.py
call .\Scripts\deactivate.bat
exit /B 1
:NOPYTHON
echo "Python for Windows is not installed. Get it from https://www.python.org/downloads/ first."