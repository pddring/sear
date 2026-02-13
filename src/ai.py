from google import genai
from google.genai import types
import wave

# Azure cloud
import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import azure.cognitiveservices.speech as speechsdk

class AI:
    def __init__(self, api_key):
        self.api_key = api_key
        print("Setting up AI provider")

    def wave_file(self, filename, pcm, channels=1, rate=24000, sample_width=2):
        with wave.open(filename, "wb") as wf:
            wf.setnchannels(channels)
            wf.setsampwidth(sample_width)
            wf.setframerate(rate)
            wf.writeframes(pcm)

class GoogleAI(AI):
    def __init__(self, api_key):
        self.ai = genai.Client(api_key=api_key)
        print("Setting up Google AI provider")

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
        self.wave_file(filename, data)


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
    
    

class AzureAI(AI):
    def __init__(self, api_key="", endpoint="https://northeurope.api.cognitive.microsoft.com/"):
        print("Setting up Azure AI provider")
        self.api_key = api_key
        self.endpoint = endpoint
        self.client = ImageAnalysisClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )

    def describe(self):
        with open('last_frame.jpg', 'rb') as f:
            image_bytes = f.read()
        print(f"Read {len(image_bytes)} from last_frame.jpg")
        result = self.client._analyze_from_image_data(
            image_data=image_bytes,
            visual_features=[VisualFeatures.CAPTION,VisualFeatures.READ]
        )
        print(result)
        if result:
            return result["captionResult"]["text"]
    
    def get_speech(self, speech, filename="last_speech.wav"):
        print("Saying: " + speech)

        speech_config = speechsdk.SpeechConfig(subscription=self.api_key, endpoint=self.endpoint)
        speech_config.set_speech_synthesis_output_format(format_id=speechsdk.SpeechSynthesisOutputFormat.Riff16Khz16BitMonoPcm)
        audio_config = speechsdk.AudioConfig(filename=filename)
        """en-GB-SoniaNeural (Female)
        en-GB-OliviaNeural (Female)
        en-GB-LibbyNeural (Female)
        en-GB-AdaMultilingualNeural4 (Female)
        en-GB-AbbiNeural (Female)
        en-GB-BellaNeural (Female)
        en-GB-HollieNeural (Female)
        en-GB-EthanNeural (Male)
        en-GB-MaisieNeural (Female, Child)
        en-GB-ElliotNeural (Male)
        en-GB-AlfieNeural (Male)
        en-GB-NoahNeural (Male)
        en-GB-OliverNeural (Male)
        en-GB-OllieMultilingualNeural4 (Male)
        en-GB-RyanNeural (Male)
        en-GB-ThomasNeural """
        # Set the voice name, refer to https://aka.ms/speech/voices/neural for full list.
        speech_config.speech_synthesis_voice_name = "en-GB-MaisieNeural"

        # Creates a speech synthesizer using the default speaker as audio output.
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=audio_config)

        result = speech_synthesizer.speak_text(speech)
        return result

if __name__ == "__main__":
    import settings
    s = settings.Settings()
    s.load_settings()
    #a = AzureAI(s.settings["AZURE_KEY"], s.settings["AZURE_ENDPOINT"])
    a = GoogleAI(s.settings["API_KEY"])
    speech = input("TTS: what to say?")
    filename = input("Filename:")
    result = a.get_speech(speech, filename)
    
