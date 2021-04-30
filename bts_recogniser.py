import cv2 as cv
import imutils
import numpy as np
import os

people = os.listdir(os.path.join(os.getcwd(), "training"))
test_directory = os.path.join(os.getcwd(), "test")

haar_cascade = cv.CascadeClassifier(os.path.join(
    os.getcwd(), "haarcascade_frontalface_default.xml"))
face_recogniser = cv.face.LBPHFaceRecognizer_create()
face_recogniser.read("faces_trained.yml")

img = cv.imread(os.path.join(test_directory, "jin_test_2.jpg"))
img = imutils.resize(img, height=min(img.shape[0], 600))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

img_height = img.shape[0]
img_width = img.shape[1]

for x, y, w, h in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]

    label, confidence = face_recogniser.predict(faces_roi)
    name = people[label]
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
    cv.putText(img, name, (img_width//2 - 100, img_height//2 + 50),
               cv.FONT_HERSHEY_SIMPLEX, 0.8, (255))
    confidence_label = f'Confidence: {round(confidence, 4)}%'
    cv.putText(img, confidence_label, (img_width//2 - 100, img_height //
                                       2 + 100), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255))

cv.imshow("Test Data", img)
cv.waitKey(0)