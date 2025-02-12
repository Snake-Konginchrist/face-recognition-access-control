from aip import AipFace
import os

_client = None
def get_client():
    global _client
    if not _client:
        _client = AipFace(os.getenv('BAIDU_APP_ID'), 
                         os.getenv('BAIDU_API_KEY'),
                         os.getenv('BAIDU_SECRET_KEY'))
    return _client

def detect_face(image):
    client = get_client()
    imageType = "BASE64"
    options = {
        "face_field": "age,beauty,expression,gender",
        "max_face_num": 2,
        "face_type": "LIVE",
    }
    result = client.detect(image, imageType, options)
    return result
