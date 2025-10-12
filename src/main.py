import camera
import json
import os

class Sear:
    def __init__(self, settings_file=""):
        if settings_file == "":
            settings_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        print(f"Loading settings from {settings_file}")
        self.load_settings(settings_file)
        self.cam = camera.Camera(self.settings['camera_id'])

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

