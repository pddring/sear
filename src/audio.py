import pyaudio
import wave

class Audio:
  def __init__(self):
    self.a = pyaudio.PyAudio()
    self.output_device_index = 0

  def __del__(self):
    self.a.terminate()

  def select_output_device(self, index):
    self.output_device_index = index

  def get_output_devices(self):
    devices = []
    for i in range(self.a.get_device_count()):
      devices.append(self.a.get_device_info_by_index(i))
    return devices

  def play_audio(self, wavfile="last_speech.wav"):
        #define stream chunk   
        chunk = 1024  
        
        #open stream  
        f = wave.open(wavfile,"rb")  
        stream = self.a.open(format = self.a.get_format_from_width(f.getsampwidth()),  
                        channels = f.getnchannels(),  
                        rate = f.getframerate(),  
                        output = True,
                        output_device_index = self.output_device_index)  
        #read data  
        data = f.readframes(chunk)  
        
        #play stream  
        while data:  
            stream.write(data)  
            data = f.readframes(chunk)  
        
        #stop stream  
        stream.stop_stream()  
        stream.close()  

if __name__ == "__main__":
  print("Testing audio")
  a = Audio()
  
  print(a.get_output_devices())

  a.play_audio()
  
