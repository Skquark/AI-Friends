@echo off
cd /D "%~dp0"
copy .\venv\*.json .\
del /s /q .\venv
python -m venv .\venv
move *.json .\venv