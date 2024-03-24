# 简易人脸识别门禁

这是一个基于Python和OpenCV的实时人脸识别门禁控制系统。通过利用百度AI人脸识别API，该系统能够对摄像头捕获的视频流进行实时分析，识别其中的人脸，并根据识别结果来控制门禁。

## 特性

- 实时视频流捕获与显示
- 利用百度AI进行人脸识别
- 简单的门禁控制逻辑（可根据需要扩展）

## 快速开始

### 环境要求

- Python 3.6+
- OpenCV
- 百度AI Python SDK

### 安装

首先，克隆仓库到本地：

```bash
git clone https://gitee.com/Snake-Konginchrist/face-recognition-access-control.git
```
安装所需的依赖：

```bash
cd FaceRecognitionAccessControl
pip install -r requirements.txt
```
使用
运行主程序：

``` bash
python src/main.py
```

### 配置
在使用之前，你需要在src/face_recognition.py中配置你的百度AI平台APP_ID、API_KEY和SECRET_KEY。

### 贡献
欢迎任何形式的贡献！请通过issue或pull request参与项目。

### 许可证
[MIT](LICENSE)
