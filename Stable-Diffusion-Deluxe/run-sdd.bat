@echo off
cd /D "%~dp0"
reg query "HKCU\Console" /v VirtualTerminalLevel >nul
IF NOT %ERRORLEVEL% EQU 0 (
  reg add "HKCU\Console" /v VirtualTerminalLevel /t REG_DWORD /d 0x1
)
reg query "hkcu\software\Python" >nul
if ERRORLEVEL 1 GOTO NOPYTHON
echo Downloading latest Stable Diffusion Deluxe and running in a Python Virtual Environment
if not EXIST .\venv (py -3 -m venv .\venv)
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py"
powershell -Command "if (Test-Connection -ComputerName google.com -Count 1 -Quiet) { Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py } else { if (Test-Path '.\venv\Stable-Diffusion-Deluxe.py') { Write-Host 'No internet connection. Using existing script version.' } else { Write-Host 'No internet connection on first run. Unable to proceed.' ; exit 1 } }"
cd .\venv
call .\Scripts\activate.bat
.\Scripts\python.exe -m pip install --upgrade --quiet pip
.\Scripts\python.exe -m pip install --upgrade --quiet flet
cls
flet .\Stable-Diffusion-Deluxe.py
call .\Scripts\deactivate.bat
exit /B 1
:NOPYTHON
echo "Python for Windows is not installed. Get it from https://www.python.org/downloads/ first."