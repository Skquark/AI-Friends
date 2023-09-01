@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
cd .\venv
C:\Windows\System32\cmd.exe /k ".\Scripts\activate.bat"