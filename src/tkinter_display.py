import cv2
from tkinter import Tk, Label
from PIL import Image, ImageTk


class TkinterDisplay:
    def __init__(self, title='Video Display', width=800, height=600):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f'{width}x{height}')  # 设置窗口大小

        self.lbl_video = Label(self.root)
        self.lbl_video.pack(expand=True, fill='both')  # 让标签充满窗口并自动调整大小

    def display_frame(self, cv2img):
        cv2img = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)  # 转换颜色从BGR到RGB
        pil_img = Image.fromarray(cv2img)  # 将数组转换为图像
        tk_img = ImageTk.PhotoImage(image=pil_img)  # 将PIL图像转换为Tkinter图像

        self.lbl_video.imgtk = tk_img
        self.lbl_video.configure(image=tk_img)
        self.lbl_video.update()

    def run(self):
        self.root.mainloop()
