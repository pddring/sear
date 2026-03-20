# sear
<img width="117" height="82" alt="image" src="https://github.com/user-attachments/assets/95c012e9-f7de-4457-8a75-822d1f0c4731" />

Sear is our entry to the PA Consulting Raspberry Pi Competition 2026 from Fulford School KS3.

## About Sear
Our project is called SEAR (Seeing ear) and it focuses mainly on the Healthier Humans part of this year’s theme of the PA Consulting competition.

Many people in society can’t see, and although most can get treatment or help easily, not everyone can get treatment as they might not have access to it or might not be able to afford it. This means that they are left out of education, employment and entertainment.

A little while back, a visually impaired student joined our school. We wanted to help her as she faced a multitude of difficulties ranging from not being able to participate in physical lessons like drama and PE to not understanding what was going on.  Not being able to see what was on the board made it hard for her as she had to work harder to understand what was going on. 

She has a teaching assistant who was her eyes for her as the assistant told her what was going on in the lesson. This was great but this meant that she was dependent on the assistant and we wanted to help become independent.

So, we started working on a device to better her school and overall life.
That is where SEAR comes in. It is a cost effective and efficient AI powered speaking camera which uses a Raspberry Pi to take a picture of what it sees and then describes it to the user.

It is unique in many ways. For example, it is suitable for school as in our school phones are banned: making it is a better alternative to a phone, where you will get in trouble for using it.

Everyone in our team is autistic so we know what it feels like to be excluded and we didn't want anyone else to feel this way, so we started working on a device to help them.

We created SEAR to help visually impaired students thrive in all aspects of life.
It helps them be:
**Safer**: They can know about their surroundings and can keep themselves safe.
**Happier**: They can join in with activities they wouldn't be able to participate in normally.
**Healthier**: They won’t need to be cautious and scared anymore.

# Build instructions: hardware

Use the Raspberry Pi installer to install a Raspberry Pi OS Lite (64 bit) image to a micro SD card for your raspberry pi (tested on a Raspberry Pi 3B v1.2 but we used a Raspberry Pi Zero 2 W)

You will need to connect some push switches to 4 GPIO pins:

- Middle button (white) to BCM pin 2
- Right button (green) to BCM pin 3
- Left button (blue) to BCM pin 4
- Top button (red) to BCM pin 22

We soldered these on a prototyping board with headers so it would plug in on top of the raspberry pi zero:
<img width="1380" height="862" alt="{C74A0183-AE29-4668-9B7F-E0921284E3B7}" src="https://github.com/user-attachments/assets/847e4185-3379-4974-be92-d1d3ca7982ae" />

<img width="494" height="679" alt="{A6F4F192-AF0A-46CB-A0C6-BDD28C138EDD}" src="https://github.com/user-attachments/assets/5f9e48c4-f307-4243-bc38-db5bf114e644" />

We designed the casing in Fusion and printed it on a Creality K1C using PLA in two parts: 

Top: 
<img width="1390" height="865" alt="{46EBAE07-D8B7-4F37-BD93-4DD2711C0A69}" src="https://github.com/user-attachments/assets/85d3e337-8583-4409-a982-2c513bfd01c3" />



Bottom:
<img width="1413" height="886" alt="{4A3DCC7C-A16C-482D-9F5B-EC7D22D911FC}" src="https://github.com/user-attachments/assets/946404d3-fced-4661-afb9-57efdebced24" />

We used a USB recharable battery pack and a camera which fits into the case as shown below:
<img width="1446" height="923" alt="{42C25944-D81C-42B9-BE46-63027A7721F2}" src="https://github.com/user-attachments/assets/bce476f2-7153-442a-a4a5-06e27c778929" />


## Setup instructions
You will need a Google Gemini API key for this to work.
You can create one here: https://aistudio.google.com/app/api-keys



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
`pip install gpiozero google-genai opencv-python pyaudio azure-cognitiveservices-speech azure-ai-vision-imageanalysis`


# Usage instructions
We added a script to make the code run automatically on start up, but if you want to make it run manually, you can do this by enabling the virtual environment (as shown above) then running:
`python main.py`

When the progrma runs you can attempt to connect to the closest bluetooth speaker / headset by placing the sear device next to the speakers and holding down the top button

Pressing the top button rather than holding it should give a status update (speaking the time and speaker battery life)

Pressing the middle button should take a picture and describe what it sees, speaking the description through bluetooth speakers.

# Future plans
We haven't yet made it so that the sear device can measure how much battery charge is left. It can read the battery life of the bluetooth speaker but there's no way to detect when the main battery runs down. We've ordered a sensor which we could directly connect to the battery inside the battery pack but we haven't connected that up yet.

We haven't yet coded it to fast forward / repeat the last speech using the left and right button. We hope to get that working soon

Attempting to connect to the closest bluetooth headset or speaker doesn't always work reliably and sometimes you need to do this in the terminal using `bluetoothctl` then `scan on` to show all devices. This should show the MAC addresses of all detected devices, then you can do `connect 00:00:00:00:00` (replacing the MAC address with the one for the device you want to connect to.

# List of parts
| Part | Link | Price |
| --- | --- | --- |
| Raspberry Pi Zero 2 W | https://shop.pimoroni.com/products/raspberry-pi-zero-2-w?variant=42101934587987 | £14.40 |
| Raspberry Pi Camera | https://shop.pimoroni.com/products/raspberry-pi-camera-module-v2?variant=19833929735 | £14.40 |
| Battery pack | We used a free promotional one a bit like this: https://www.highflyers.de/p/span-1200-mah-powerbank-2513427700-p.html | £3.00 |
| Bluetooth speaker | Any bluetooth headset would work | Not included in price |
| | Totals: | £31.80 |
