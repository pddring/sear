import pyaudio

if __name__ == "__main__":
  print("Testing audio")
  audio = pyaudio.PyAudio()
  for i in range(audio.get_device_count()):
    print(audio.get_device_info_by_index(i))
  audio.terminate()
