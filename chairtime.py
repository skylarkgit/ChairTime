import face_recognition
import cv2
import time
from db import DataManager

def detect(frame) -> bool:
    face_locations = face_recognition.face_locations(frame, model="cnn", number_of_times_to_upsample=0)
    return face_locations.__len__() > 0

def monitor_chair_time():
    dbman = DataManager()
    while True:
        video = cv2.VideoCapture(0)
        ret, frame = video.read()
        video.release()
        dbman.setStatus(detect(frame))
        time.sleep(10)
            
if __name__ == '__main__':
    monitor_chair_time()
