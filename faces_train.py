import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'Faces/train'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

def create_train():
    features = []
    labels = []

    for person in people:                          #  Loop through people
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):               #  Loop through images
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)

            if img_array is None:                  #  Skip unreadable files
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                face_roi = gray[y:y+h, x:x+w]
                features.append(face_roi)
                labels.append(label)
  
    print('Training done -----------------------')

    face_recognizer = cv.face.LBPHFaceRecognizer_create()
    face_recognizer.train(features, np.array(labels))  #  labels must be numpy array here
    face_recognizer.save('face_trained.yml')

    features = np.array(features, dtype='object')
    labels = np.array(labels)
    np.save('features.npy', features)
    np.save('labels.npy', labels)

create_train() 