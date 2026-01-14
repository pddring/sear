# sear
Seeing Ear

Python program to capture an image and provide an audio description for blind or partially sighted users

Use the Raspberry Pi installer to install a Raspberry Pi OS Lite (64 bit) image to a micro SD card for your raspberry pi (tested on a Raspberry Pi 3B v1.2)

You will need a Google Gemini API key for this to work.
You can create one here: https://aistudio.google.com/app/api-keys

## Setup instructions

Clone this repository to get a copy of the source code on the raspberry pi:
`git clone https://github.dev/pddring/sear`

Create a `settings.json` file in the src folder:
```
{
    "API_KEY":"INSERT YOUR API KEY HERE",
    "camera_id": 0
}
```
Install the following system libraries
`sudo apt install libportaudio-ocaml-dev bluez-alsa-utils pulseaudio pulseaudio-module-bluetooth`

Add the user to the bluetooth group:
`sudo adduser pi bluetooth`

Create a virtual environment:
`virtualenv --system-site-packages venv`

Activate that virtual environment:
`source venv/bin/activate`

install additional libraries:
`pip gpiozero install google-genai opencv-python pyaudio azure-cognitiveservices-speech azure-ai-vision-imageanalysis`

This guide was helpful for setting up bluetooth headphones: https://gist.github.com/actuino/9548329d1bba6663a63886067af5e4cb#pair-and-connect
