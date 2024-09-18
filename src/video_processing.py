import cv2  # OpenCV 库，用于视频捕捉和图像处理
from face_recognition import detect_face  # face_recognition 库中的 detect_face 函数，用于人脸检测
from base64 import b64encode  # base64 编码模块，用于将图像转换为 base64 格式
from face_detector import FaceDetector  # 自定义的 FaceDetector 模块，用于检测和绘制人脸
from tkinter_display import TkinterDisplay  # 自定义的 TkinterDisplay 模块，用于显示视频帧


# 定义一个处理帧的函数
def process_frame(frame):
    # 将图像帧编码为 JPG 格式
    _, buffer = cv2.imencode('.jpg', frame)

    # 将编码后的图像转换为 base64 格式
    frame_base64 = b64encode(buffer).decode()

    # 使用 detect_face 函数进行人脸检测，并将 base64 格式的图像传递给函数
    result = detect_face(frame_base64)

    # 打印检测结果
    print(result)


# 定义视频捕捉功能
def video_capture():
    # 打开摄像头捕捉视频流，设备编号为 0（即默认摄像头）
    cap = cv2.VideoCapture(0)

    # 创建人脸检测器对象
    fd = FaceDetector()

    # 创建一个用于显示视频帧的 Tkinter 窗口对象，窗口标题为“简易人脸识别门禁（明德二十八日制）”，窗口大小为 800x600
    display = TkinterDisplay(title='简易人脸识别门禁（明德二十八日制）', width=800, height=600)

    # 开启无限循环来持续读取视频帧
    while True:
        # 从摄像头读取一帧视频图像，ret 为读取状态，frame 为读取的图像帧
        ret, frame = cap.read()

        # 如果未成功读取视频帧，则打印错误信息并退出循环
        if not ret:
            print("无法获取视频流")
            break

        # 调用处理帧的函数对帧进行人脸检测（此行已注释掉）
        process_frame(frame)

        # 使用 FaceDetector 检测人脸并在图像上绘制边框
        frame = fd.detect_and_draw(frame)

        # 将处理后的帧显示在 Tkinter 窗口中
        display.display_frame(frame)

        # 检查键盘输入，如果按下 'q' 键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放摄像头资源
    cap.release()

    # 关闭所有 OpenCV 创建的窗口
    cv2.destroyAllWindows()
