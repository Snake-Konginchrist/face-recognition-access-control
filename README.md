# 简易人脸识别门禁

这是一个基于 Python 和 OpenCV 的实时人脸识别门禁控制系统。通过利用百度 AI 人脸识别 API，该系统能够对摄像头捕获的视频流进行实时分析，识别其中的人脸，并根据识别结果来控制门禁。

## 特性

- 实时视频流捕获与显示
- 利用百度 AI 进行人脸识别
- 简单的门禁控制逻辑（可根据需要扩展）

## 快速开始

### 环境要求

- Python 3.6+
- OpenCV
- 百度 AI Python SDK

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

### 配置

在 `src/config.py` 文件中配置你的百度 AI 平台的 `APP_ID`、`API_KEY` 和 `SECRET_KEY`：

```python
# config.py
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'
```

请确保在百度 AI 开发者平台获取这些信息并正确配置。

### 使用

运行主程序：

```bash
python src/main.py
```

### 贡献

欢迎任何形式的贡献！请通过 issue 或 pull request 参与项目。

### 许可证

[MIT](LICENSE)

## 联系方式

- GitHub: [Snake-Konginchrist](https://github.com/Snake-Konginchrist)
- Gitee: [Snake-Konginchrist](https://gitee.com/Snake-Konginchrist)
- Email: developer@skstudio.cn (优先)