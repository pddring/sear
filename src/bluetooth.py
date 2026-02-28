from threading import Thread
import os
import pexpect

class Bluetooth:
    def __init__(self):
        pass

    def set_power(self, on):
        if on:
            print(f"Turning bluetooth on")
            p = pexpect.spawn("bluetoothctl")
            p.sendline("power on")
            p.expect("Changing power on succeeded", timeout=2)
            print(p.after)
            p.close()
        else:
            print("Turning bluetooth off")
            p = pexpect.spawn("bluetoothctl")
            p.sendline("power off")
            p.expect("Changing power off succeeded", timeout=2)
            print(p.after)
            p.close()

    def get_devices(self):
        p = pexpect.spawn("bluetoothctl")
        p.sendline("devices")
        while True:
            p.expect("Device ([0-9A-F:]+) (.*?)\r", timeout=1)
            print(p.after)
        p.close()



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
    b.set_power(True)
    b.get_devices()
    input("Wait")
    b.set_power(False)

    while True:
        filename = input("wav file:")
        b.play_audio(filename, False)
    #
