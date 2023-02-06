@echo off
cd /D "%~dp0"
if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
pip install --upgrade --quiet flet
flet -r Stable-Diffusion-Deluxe.py