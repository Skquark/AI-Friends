set python="C:\ProgramData\Anaconda3\python.exe"
set PROGRAMDATA = "C:\ProgramData"
set venv=sdd
:: cmd /c C:\ProgramData\Anaconda3\condabin\conda.bat run %python% "C:\Users\User Name\Path to your Python File\Python File.py"
call %PROGRAMDATA%\Anaconda3\Scripts\activate %venv%
::call activate %venv%
cd %~dp0
pip install --upgrade pip
pip install --upgrade flet

:: Run script at this location
::call %PROGRAMDATA%/Anaconda3/envs/%venv%/python.exe "%~dp0\main.py"
PAUSE
call flet run .\Stable-Diffusion-Deluxe.py
C:\ProgramData\Anaconda3\Scripts\conda create --name sddconda
C:\ProgramData\Anaconda3\Scripts\conda activate sddconda