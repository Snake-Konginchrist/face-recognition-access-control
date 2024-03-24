from aip import AipFace
import config

client = AipFace(config.APP_ID, config.API_KEY, config.SECRET_KEY)


def detect_face(image):
    imageType = "BASE64"
    options = {
        "face_field": "age,beauty,expression,gender",
        "max_face_num": 2,
        "face_type": "LIVE",
    }
    result = client.detect(image, imageType, options)
    return result
