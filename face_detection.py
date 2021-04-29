import cv2 as cv
import numpy as np
import os

jk_dir = os.path.join(os.getcwd(), "training", "jungkook")
jk_photos = os.listdir(jk_dir)

img = cv.imread(os.path.join(jk_dir, jk_photos[4]))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier(os.path.join(
    os.getcwd(), "haarcascade_frontalface_default.xml"))
faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=3)

for x, y, w, h in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)

cv.imshow("JK Test", img)
cv.waitKey(0)
