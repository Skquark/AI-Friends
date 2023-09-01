@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
reg query "hkcu\software\Python"
if ERRORLEVEL 1 GOTO NOPYTHON
echo Running Stable Diffusion Deluxe in a Python Virtual Environment
if not EXIST .\venv GOTO NOVENV
cd .\venv
call .\Scripts\activate.bat
py -3 -m pip install --upgrade --quiet pip
py -3 -m pip install --upgrade --quiet flet
cls
flet .\Stable-Diffusion-Deluxe.py
call .\Scripts\deactivate.bat
exit /B 1
:NOPYTHON
echo "Python for Windows is not installed. Get it from https://www.python.org/downloads/ first."
:NOVENV
echo "Run the regular sdd-venv.bat to initialize before running this."