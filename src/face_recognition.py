import cv2
import numpy as np
import os


haar_cashaar_cascade = cv2.CascadeClassifier('../haar_face.xml')
people = ['messi', 'neymar', 'suarez']

features = np.load('../features.npy', allow_pickle=True)
labels = np.load('../labels.npy', allow_pickle=True)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()  
face_recognizer.read('../face_trained.yml')


for path in os.listdir('../faces/test'):
    test_image_path = os.path.join('../faces/test', path)
    test_image = cv2.imread(test_image_path)
    cv2.imshow('Original image', test_image)

    gray_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray_image)

    faces_rect = haar_cashaar_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4)

    for (x, y, w, h) in faces_rect:
        faces_roi = gray_image[y:y + h, x:x + w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label = {people[label]} with a confidence of {confidence}.')

        cv2.putText(test_image, str(people[label]), (10, 40), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 1)

        cv2.rectangle(test_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Detected face', test_image)
    cv2.waitKey(0)