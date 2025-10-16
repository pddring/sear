# sear
Seeing Ear

Python program to capture an image and provide an audio description for blind or partially sighted users

Use the Raspberry Pi installer to install a Raspberry Pi OS Lite (64 bit) image to a micro SD card for your raspberry pi (tested on a Raspberry Pi 3B v1.2)

You will need a Google Gemini API key for this to work.
You can create one here: https://aistudio.google.com/app/api-keys

## Setup instructions
Create a `settings.json` file in the src folder:
```
{
    "APIKEY":"INSERT YOUR API KEY HERE",
    "camera_id": 0
}
```
Install the following system libraries
`sudo apt install libportaudio-ocaml-dev`

Create a virtual environment and install additional libraries:
`pip install google-generativeai opencv-python pyaudio`
