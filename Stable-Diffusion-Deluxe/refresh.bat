@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
copy .\venv\*.json .\
del /s /q .\venv
python3 -m venv .\venv
move *.json .\venv