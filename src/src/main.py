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
        self.buttons.add_listener('MIDDLE', 'SHORT_PRESS', self.go_button)

        print(f"Creating AI client with API KEY: {self.settings['API_KEY']}")
        #self.ai = ai.AzureAI(self.settings["AZURE_KEY"], self.settings["AZURE_ENDPOINT"])
        self.ai = ai.GoogleAI(self.settings["API_KEY"])

        print("Initialising PyAudio")
        self.audio = audio.Audio()
    
    def go_button(self, name):
        print("Taking picture")
        s.cam.take_picture()
        
        print("Describing image...")
        response = s.ai.describe()
        print(response)
        print("Generating speech audio file...")
        speech = s.ai.get_speech(response)
        print(speech)
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
    
    def wait_for_buttons(self):
        print("Starting button server")
        self.buttons.start()

    


if __name__ == "__main__":
    s = Sear()
    s.audio.select_output_device_by_name("bluealsa")
    s.wait_for_buttons()
    
    #s.audio.select_output_device_by_id(5)
    
