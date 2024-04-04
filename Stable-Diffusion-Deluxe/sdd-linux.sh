#! /bin/sh
echo "Downloading latest Stable Diffusion Deluxe and running in a Python Virtual Environment"
if [ ! -d "./venv" ] ; then
    python3 -m venv ./venv || { echo "Failed to create the virtual environment"; exit 1; }
fi
wget https://raw.githubusercontent.com/Skquark/AI-Friends/main/Stable-Diffusion-Deluxe/Stable-Diffusion-Deluxe.py -O ./venv/Stable-Diffusion-Deluxe.py || { echo "Failed to download Stable Diffusion Deluxe script"; exit 1; }
cd ./venv
source ./bin/activate || { echo "Failed to activate the virtual environment"; exit 1; }
./bin/pip install --upgrade --quiet pip
./bin/pip install --upgrade --quiet flet
flet ./Stable-Diffusion-Deluxe.py --saved_settings_json ./sdd-settings.json || { echo "Failed to run Stable Diffusion Deluxe script"; exit 1; }
deactivate
exit
