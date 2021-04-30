import cv2 as cv
import os
import numpy as np
import time

training_data_path = os.path.join(os.getcwd(), "training")

people = [i for i in os.listdir(training_data_path)]

faces = []
labels = []

haar_cascade = cv.CascadeClassifier(os.path.join(
    os.getcwd(), "haarcascade_frontalface_default.xml"))


def create_train():
    for person in people:
        folder_path = os.path.join(training_data_path, person)
        label = people.index(person)

        for image in os.listdir(folder_path):
            image_path = os.path.join(folder_path, image)

            img = cv.imread(image_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=3)

            for x, y, w, h in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]

            faces.append(faces_roi)
            labels.append(label)


create_train()

face_recogniser = cv.face.LBPHFaceRecognizer_create()

faces = np.array(faces, dtype="object")
labels = np.array(labels)

face_recogniser.train(np.array(faces), np.array(labels))

face_recogniser.save("faces_trained.yml")
