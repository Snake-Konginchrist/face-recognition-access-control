from dotenv import load_dotenv
import os
from video_processing import video_capture
load_dotenv()  # 必须在所有导入前加载环境变量

# 百度AI配置
APP_ID = os.getenv('BAIDU_APP_ID')
API_KEY = os.getenv('BAIDU_API_KEY')
SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')

if __name__ == '__main__':
    video_capture()
