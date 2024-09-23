import requests
import numpy as np
import cv2
from flask import Blueprint, request
from face_compare.compare_faces import compare_faces

periphery_blueprint = Blueprint("periphery", __name__)

camera_server_url = "http://192.168.1.154/capture"

def setup_camera():
    requests.get(camera_server_url + 'control?var=framesize&val=12')

def request_camera_image():
    resp = requests.get(camera_server_url + '/capture', stream=True).raw
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image 

@periphery_blueprint.route('/rfid', methods=['POST'])
def handle_rfid_message():
    # todo Получение rfid, сравнение лиц
    # todo Получение эталона из БД
    current_face = request_camera_image()
    
    # print(compare_faces('./tests/me.jpg', './output_image.jpg'))
    return "Handled"
