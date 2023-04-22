#! /bin/sh
echo "Downloading latest Stable Diffusion Deluxe and running in a Python Virtual Environment"
if [ ! -d ./venv ] ; then
    python -m venv ./venv
wget https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py  ./venv/Stable-Diffusion-Deluxe.py
cd ./venv
source ./bin/activate
./bin/pip install --upgrade --quiet pip
./bin/pip install --upgrade --quiet flet
flet ./Stable-Diffusion-Deluxe.py
deactivate
exit