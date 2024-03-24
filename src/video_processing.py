import cv2
from face_recognition import detect_face
from base64 import b64encode
from face_detector import FaceDetector
from tkinter_display import TkinterDisplay


def process_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    frame_base64 = b64encode(buffer).decode()

    result = detect_face(frame_base64)
    print(result)


def video_capture():
    cap = cv2.VideoCapture(0)
    fd = FaceDetector()
    display = TkinterDisplay(title='简易人脸识别门禁（明德二十八日制）', width=800, height=600)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法获取视频流")
            break

        # process_frame(frame)
        frame = fd.detect_and_draw(frame)
        display.display_frame(frame)
        # cv2.imshow('Face Recognition Access Control', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
