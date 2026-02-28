from threading import Thread
import os
import pexpect
import re

class Bluetooth:
    def __init__(self):
        self.devices = {}

    def set_power(self, on):
        if on:
            print(f"Turning bluetooth on")
            p = pexpect.spawn("bluetoothctl")
            p.sendline("power on")
            p.expect("Changing power on succeeded", timeout=2)
            p.close()
        else:
            print("Turning bluetooth off")
            p = pexpect.spawn("bluetoothctl")
            p.sendline("power off")
            p.expect("Changing power off succeeded", timeout=2)
            p.close()
        
    def update_status(self, id):
        p = pexpect.spawn("bluetoothctl", encoding="utf-8")
        p.sendline(f"info {id}")
        connected = p.expect(["Connected: yes", "Connected: no"]) == 0
        battery = 0
        if connected:
            p.expect("Battery Percentage: .* \\((\\d+)\\)")
            battery = p.match.group(1)
        p.close()

        self.devices[id]["connected"] = connected
        self.devices[id]["battery"] = battery
        return self.devices[id]

    def get_devices(self):
        p = pexpect.spawn("bluetoothctl", encoding="utf-8")
        p.sendline("devices")
        self.devices = {}
        while True:
            try:
                p.expect("Device ([0-9A-F:]+) (.*?)\r\n", timeout=0.1)
                device = p.after
                m = re.match("Device ([0-9A-F:]+) (.*?)\r\n", device)
                self.devices[m.group(1)] = {"name": m.group(2), "connected": False}
                
            except pexpect.TIMEOUT:
                break
        
        for id in self.devices:
            self.update_status(id)
            
            
        p.close()
        return self.devices

    def connect(self, id):
        print(f"Connecting to bluetooth device {id}")
        p = pexpect.spawn("bluetoothctl", encoding="utf-8")
        p.sendline(f"connect {id}")
        p.expect(f"Attempting to connect to {id}")
        success = p.expect(["Connection successful", "not available"])==0
        if id in self.devices:
            self.devices[id]["connected"] = success
        p.close()
        return success


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
    print(b.get_devices())

    input("Wait")
    b.connect("11:75:58:EB:5F:CD")
    input("Wait")

    while True:
        filename = input("wav file:")
        if filename == "":
            break
        b.play_audio(filename, False)
    
    b.set_power(False)

