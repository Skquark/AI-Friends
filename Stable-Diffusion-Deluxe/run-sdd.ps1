powershell Start-Process powershell -Verb runAs
if not EXIST .\venv (python -m venv .\venv)
# Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py
if (Test-Connection -ComputerName google.com -Count 1 -Quiet) { Invoke-WebRequest https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -OutFile .\venv\Stable-Diffusion-Deluxe.py } else { if (Test-Path '.\venv\Stable-Diffusion-Deluxe.py') { Write-Host 'No internet connection. Using existing script version.' } else { Write-Host 'No internet connection on first run. Unable to proceed.' ; exit 1 } }
cd .\venv\Scripts
.\Activate.ps1
cd ..
.\Scripts\python.exe -m pip install --upgrade pip
.\Scripts\python.exe -m pip install --upgrade flet
flet .\Stable-Diffusion-Deluxe.py
& .\Scripts\deactivate.bat
exit /B 1