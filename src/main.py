import camera
import json
import os
import wave
import pyaudio
from google import genai
from google.genai import types


class Sear:
    def __init__(self, settings_file=""):
        if settings_file == "":
            settings_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
        print(f"Loading settings from {settings_file}")
        self.load_settings(settings_file)
        self.cam = camera.Camera(self.settings['camera_id'])

        print(f"Creating AI client with API KEY: {self.settings['API_KEY']}")
        self.ai = genai.Client(api_key=self.settings["API_KEY"])

        print("Initialising PyAudio")
        self.audio = pyaudio.PyAudio() 

    def __del__(self):
        print("Releasing PyAudio    ")
        self.audio.terminate()



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
    
    def wave_file(self, filename, pcm, channels=1, rate=24000, sample_width=2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm)

    def get_speech(self, speech, filename="last_speech.wav"):
        print("Saying: " + speech)

        response = self.ai.models.generate_content(
            model="gemini-2.5-flash-preview-tts",
            contents=speech,
            config=types.GenerateContentConfig(
                response_modalities=["AUDIO"],
                speech_config=types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                        voice_name='Leda',
                        )
                    )
                ),
            )
        )
        data = response.candidates[0].content.parts[0].inline_data.data
        file_name='last_speech.wav'
        self.wave_file(file_name, data)

    def play_audio(self, wavfile="last_speech.wav"):
        #define stream chunk   
        chunk = 1024  
        
        #open stream  
        f = wave.open(wavfile,"rb")  
        stream = self.audio.open(format = self.audio.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True)  
        #read data  
        data = f.readframes(chunk)  
        
        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  
        
        #stop stream  
        stream.stop_stream()  
        stream.close()  
    
    def describe(self, prompt=""):
        if prompt == "":
            prompt = "Summarize the contents of this image in one sentence which is suitable for a blind person"
        with open('last_frame.jpg', 'rb') as f:
            image_bytes = f.read()
        response = self.ai.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
            types.Part.from_bytes(
                data=image_bytes,
                mime_type='image/jpeg',
            ),
            prompt
            ]
        )
        return response.text




if __name__ == "__main__":
    s = Sear()
    s.cam.take_picture()
    s.cam.save()
    
    print("Describing image...")
    response = s.describe()
    print(response)
    print("Generating speech audio file...")
    s.get_speech(response)
    print("Playing speech")
    s.play_audio()
    if input("detailed? [y/n]") == "y":
        print("Detailed:")
        response = s.describe("describe this photo in detail as an audio description suitable for a blind person")
        print(response)
        print("Generating speech audio file...")
        s.get_speech(response)
        print("Playing speech")
        s.play_audio()


