set python="C:\ProgramData\Anaconda3\python.exe"
cmd /c C:\ProgramData\Anaconda3\condabin\conda.bat run %python% "C:\Users\User Name\Path to your Python File\Python File.py"
%python% -m pip install --upgrade --quiet pip
%python% -m pip install --upgrade --quiet flet
flet .\Stable-Diffusion-Deluxe.py