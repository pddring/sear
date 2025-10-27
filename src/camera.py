import cv2
class Camera:
    def __init__(self, cam_id = 0):
        self.cam_id = cam_id
        self.last_frame = False
        self.cam = cv2.VideoCapture(cam_id)
        print(f"Initialising camera {cam_id}")

        self.take_picture(150)

    def take_picture(self, max_attempts = 10):
        result = False
        attempts = 0
        while attempts < max_attempts and result == False:
            attempts += 1
            result, self.last_frame = self.cam.read()
            print(f"Attempt {attempts}: {result}")
        return result
    
    def view_and_shoot(self):
        while True:
            if self.take_picture():
                cv2.imshow("SEar", self.last_frame)
                key = cv2.waitKey(1)
                if key > -1:
                    print(key)
                    break

    def save(self, filename="last_frame.jpg"):
        cv2.imwrite(filename, self.last_frame)
    
    def release(self):
        print(f"Releasing camera {self.cam_id}")
        self.cam.release()

    def __del__(self):
        self.release()


if __name__ == "__main__":
    c = Camera()
    print(c.take_picture())
    c.save()

        
