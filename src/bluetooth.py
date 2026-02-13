from threading import Thread
import os
class Bluetooth:
    def __init__(self, device_id):
        self.device_id = device_id

    def connect(self):
        print(f"Connecting to bluetooth device {self.device_id} (NOT IMPLEMENTED YET)")

    def play_audio(self, filename="last_speech.wav", blocking=True):       
        if blocking:
            print("Stopping all previous playback")
            os.system("killall aplay")

            print(f"Playing audio {filename}")
            os.system(f"aplay -D bluealsa:DEV={self.device_id},PROFILE=a2dp {filename} -q")
            print("Done")
        
        else:
            t = Thread(target = self.play_audio, args=(filename, True))
            t.start()


if __name__ == "__main__":
    print("Testing bluetooth")
    b = Bluetooth("24:29:34:A2:22:ED")
    b.play_audio("last_speech.wav", False)
    input("Wait...")
    b.play_audio("last_speech.wav", False)
