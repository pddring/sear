import pyaudio

if __name__ == "__main__":
  print("Testing audio")
  audio = pyaudio.PyAudio()
  audio.terminate()
