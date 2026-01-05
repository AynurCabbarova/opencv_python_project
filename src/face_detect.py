import cv2
import os
import numpy as np

image_path = '../pictures/messi.jpeg'

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)
    
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError()
    
    cv2.imshow('Image Frame', image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray image', gray)

    haar_cascade = cv2.CascadeClassifier('../haar_face.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    print(f'Number of face(s) found : {len(faces_rect)}.')

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    cv2.imshow('Detected faces', image)

    while True:
        key = cv2.waitKey(100) & 0xFF
        if key == 27 or key == ord('q'):
            print('Exiting ...')
            break
    

except FileNotFoundError as fnf:
    print(f'Invalid path! {fnf}')
except ValueError as ve:
    print(f'Image is not found! {ve}')
except KeyboardInterrupt:
    print(f'Keyboard interrupted, exiting by clicking Ctrl + C!')
except Exception as e:
    print(f'Unexpected error occured! {e}')
finally:
    cv2.destroyAllWindows()


'''
import cv2
import os
import numpy as np

cap = cv2.VideoCapture(0)

try:
    if not cap.isOpened():
        raise Exception("Could not access the camera")

    while True:
        ret, image = cap.read()

        if not ret:
            break 

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        haar_cascade = cv2.CascadeClassifier('../haar_face.xml')

        if haar_cascade.empty():
            raise FileNotFoundError('Haar Cascade XML file is missing or cannot be loaded.')

        faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

        print(f'Number of face(s) found: {len(faces_rect)}.')

        for (x, y, w, h) in faces_rect:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Detected Faces', image)

        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'):
            print('Exiting ...')
            break

except FileNotFoundError as fnf:
    print(f'Invalid path! {fnf}')
except Exception as e:
    print(f'Unexpected error occurred! {e}')
finally:
    cap.release()
    cv2.destroyAllWindows()

'''