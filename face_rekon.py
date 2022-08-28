import face_recognition

def detect(frame) -> bool:
    # image = face_recognition.load_image_file(filename)
    face_locations = face_recognition.face_locations(frame, model="cnn", number_of_times_to_upsample=0)
    return face_locations.__len__() > 0

import cv2
import time
from db import DataManager

dbman = DataManager()
while True:
    video = cv2.VideoCapture(0)
    ret, frame = video.read()
    video.release()
    dbman.setStatus(detect(frame))
    time.sleep(10)
