import picamera2
class Camera:
    def __init__(self, cam_id = 0):
        self.cam_id = cam_id
        self.last_frame = False

        self.cam = picamera2.Picamera2(cam_id)
        print(self.cam.sensor_modes)
        self.config = self.cam.create_still_configuration(
            buffer_count=1, 
            main={"size": (640, 480)})
        self.cam.start()
        
        print(f"Initialising camera {cam_id}")

    def take_picture(self, filename="last_frame.jpg"):
        request = self.cam.capture_request(flush=True)
        request.save('main', filename)
        request.release()

    def __del__(self):
        self.cam.stop()

if __name__ == "__main__":
    c = Camera()
    i = ""
    while i != "q":
        i = input("Press Enter to take a picture... (or q to quit)")
        c.take_picture()

        
