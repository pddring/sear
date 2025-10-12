import cv2
class Camera:
    def __init__(self, cam_id = 0):
        self.cam_id = cam_id
        self.cam = cv2.VideoCapture(cam_id)
        print(f"Initialising camera {cam_id}")

    def take_picture(self):
        result, self.last_frame = self.cam.read()
        return result
    
    def release(self):
        print(f"Releasing camera {self.cam_id}")
        self.cam.release()

    def __del__(self):
        self.release()


if __name__ == "__main__":
    c = Camera()
    while True:
        if c.take_picture():
            cv2.imshow("Last image", c.last_frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        