import cv2
import time
from db import DataManager

from util import download, exists

face_classifier_file = "haarcascade_frontalface_default.xml"
if not exists(face_classifier_file):
    download(face_classifier_file, "https://raw.githubusercontent.com/kipr/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(face_classifier_file)

dbman = DataManager()
a = 1
while True:
    video = cv2.VideoCapture(0)
    ret, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x  + w, y + h), (255, 0, 0), 2)
        # cv2.imwrite("frame%d.jpg" % a, frame)
        # cv2.imshow('Face Detection', frame)
        # time.sleep(2)
    cv2.imwrite("frame%d.jpg" % a, frame)
    video.release()
    a = a+1
    # cv2.imshow('Face Detection', frame)
    # if cv2.waitKey(1) == 27:
    #     break
    print(len(faces))
    dbman.setStatus(len(faces) > 0)
    time.sleep(10)
