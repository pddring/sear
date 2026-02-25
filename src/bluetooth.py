from threading import Thread
import os
class Bluetooth:
    def __init__(self):
        pass
    def connect(self):
        print(f"Connecting to bluetooth device {self.device_id} (NOT IMPLEMENTED YET)")

    def play_audio(self, filename="last_speech.wav", blocking=True):       
        if blocking:
            print("Stopping all previous playback")
            os.system("killall aplay")

            print(f"Playing audio {filename}")
            os.system(f"aplay -D bluealsa {filename} -q")
            print("Done")
        
        else:
            t = Thread(target = self.play_audio, args=(filename, True))
            t.start()


if __name__ == "__main__":
    print("Testing bluetooth")
    b = Bluetooth()
    while True:
        filename = input("wav file:")
        b.play_audio(filename, False)
    #
