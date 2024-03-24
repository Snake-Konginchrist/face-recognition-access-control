import cv2


class FaceDetector:
    def __init__(self):
        # 使用OpenCV自带的人脸识别模型
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    def detect_and_draw(self, frame):
        # 将图像转换为灰度图，这是大多数cv2操作的要求
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 检测图像中的人脸
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                                   flags=cv2.CASCADE_SCALE_IMAGE)

        # 在检测到的每个人脸周围画矩形框
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return frame
