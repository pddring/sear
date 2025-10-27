import camera
import json
import os
import audio
import ai


class Sear:
    def __init__(self, settings_file=""):
        if settings_file == "":
            settings_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        print(f"Loading settings from {settings_file}")
        self.load_settings(settings_file)
        self.cam = camera.Camera(self.settings['camera_id'])
        self.settings['API_KEY'] = os.environ['VISION_KEY']

        print(f"Creating AI client with API KEY: {self.settings['API_KEY']}")
        self.ai = ai.AzureAI(self.settings["API_KEY"])

        print("Initialising PyAudio")
        self.audio = audio.Audio() 

    def load_settings(self, settings_file):
        self.settings = {
            "API_KEY":"",
            "camera_id":0
        }
        
        with open(settings_file) as f:
            settings = json.load(f)
            for key in settings:
                self.settings[key] = settings[key]
                print(f"Setting: {key}:{settings[key]}")


if __name__ == "__main__":
    s = Sear()
    #s.audio.select_output_device_by_name("bluealsa")
    s.audio.select_output_device_by_id(5)
    s.cam.take_picture()
    s.cam.save()
    
    print("Describing image...")
    response = s.ai.describe()
    print(response)
    print("Generating speech audio file...")
    s.ai.get_speech(response)
    print("Playing speech")
    s.audio.play_audio()
    if input("detailed? [y/n]") == "y":
        print("Detailed:")
        response = s.describe("describe this photo in detail as an audio description suitable for a blind person")
        print(response)
        print("Generating speech audio file...")
        s.ai.get_speech(response)
        print("Playing speech")
        s.audio.play_audio()


