import camera
import json
import os
import datetime
#import audio
import bluetooth
import ai
import settings
import buttons

class Sear(settings.Settings):
    def __init__(self, settings_file=""):
        
        self.load_settings(settings_file)
        self.cam = camera.Camera(self.settings['camera_id'])
        self.buttons = buttons.ButtonManager()
        self.buttons.add_listener('MIDDLE', 'SHORT_PRESS', self.go_button)

        self.buttons.add_listener('TOP', 'SHORT_PRESS', self.status_button)

        print(f"Creating AI client with API KEY: {self.settings['API_KEY']}")
        #self.ai = ai.AzureAI(self.settings["AZURE_KEY"], self.settings["AZURE_ENDPOINT"])
        self.ai = ai.GoogleAI(self.settings["API_KEY"])

        print("Initialising Bluetooth audio")
        self.audio = bluetooth.Bluetooth()
        self.audio.set_power(True)
        devices = self.audio.get_devices()
        
        # connect to first previously connected device
        for id in devices:
            self.audio.connect(id)
            self.settings["bluetooth_device"] = id
            break

    def go_button(self, name):
        print("Taking picture")
        s.cam.take_picture()
        print("Describing image...")
        s.audio.play_audio("wait_ai.wav", False)
        response = s.ai.describe()
        print(response)
        print("Generating speech audio file...")
        s.audio.play_audio("wait_tts.wav", False)
        s.ai.get_speech(self.settings["voice_prompt"] + "\n" + response)
        print("Playing speech")
        s.audio.play_audio()
        """if input("detailed? [y/n]") == "y":
            print("Detailed:")
            response = s.ai.describe("describe this photo in detail as an audio description suitable for a blind person")
            print(response)
            print("Generating speech audio file...")
            s.ai.get_speech(response)
            print("Playing speech")
            s.audio.play_audio()"""
        
    def status_button(self, name):
        d = datetime.datetime.now()
        status = f"It's {d.strftime('%A %d %B at %I:%M %p')}. "
        id = self.settings["bluetooth_device"]
        b = self.audio.update_status(id)
        if b["connected"]:
            status += f"Connected to {b['name']} with battery at {b['battery']} percent"
        else:
            status += f"Not connected to bluetooth speakers or headphones"
        s.ai.get_speech(self.settings["voice_prompt"] + "\n" + status, "last_status.wav")
        s.audio.play_audio("last_status.wav")
        
    
    def wait_for_buttons(self):
        print("Starting button server")
        self.buttons.start()

if __name__ == "__main__":
    s = Sear()
    s.wait_for_buttons()
