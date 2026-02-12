import camera
import json
import os
import audio
import ai
import settings
import buttons

class Sear(settings.Settings):
    def __init__(self, settings_file=""):
        
        self.load_settings(settings_file)
        self.cam = camera.Camera(self.settings['camera_id'])
        self.buttons = buttons.ButtonManager()

        print(f"Creating AI client with API KEY: {self.settings['API_KEY']}")
        #self.ai = ai.AzureAI(self.settings["AZURE_KEY"], self.settings["AZURE_ENDPOINT"])
        self.ai = ai.GoogleAI(self.settings["API_KEY"])

        print("Initialising PyAudio")
        self.audio = audio.Audio() 


if __name__ == "__main__":
    s = Sear()
    print("Hello")
    exit()
    #s.audio.select_output_device_by_name("bluealsa")
    s.audio.select_output_device_by_id(5)
    s.cam.take_picture()
    
    print("Describing image...")
    response = s.ai.describe()
    print(response)
    print("Generating speech audio file...")
    speech = s.ai.get_speech(response)
    print(speech)
    print("Playing speech")
    s.audio.play_audio()
    if input("detailed? [y/n]") == "y":
        print("Detailed:")
        response = s.ai.describe("describe this photo in detail as an audio description suitable for a blind person")
        print(response)
        print("Generating speech audio file...")
        s.ai.get_speech(response)
        print("Playing speech")
        s.audio.play_audio()


