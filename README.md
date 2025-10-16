# sear
Seeing Ear

Python program to capture an image and provide an audio description for blind or partially sighted users

## Setup instructions
Create a `settings.json` file in the src folder:
```
{
    "APIKEY":"INSERT YOUR API KEY HERE",
    "camera_id": 0
}
```

Install relevant libraries:
`sudo apt install python3-opencv python3-pyaudio`

Then create a virtual environment and install additional libraries:
`pip install google-generativeai`
