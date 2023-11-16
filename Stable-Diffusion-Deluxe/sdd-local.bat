@echo off
cd /D "%~dp0"
NET SESSION >nul 2>&1
IF NOT %ERRORLEVEL% EQU 0 (
   echo Must launch app with Run as Administrator
   pause
   exit /B 1
)
pip install --upgrade --quiet flet
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\Stable-Diffusion-Deluxe.py"
flet run Stable-Diffusion-Deluxe.py