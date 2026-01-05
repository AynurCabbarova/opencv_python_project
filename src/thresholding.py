import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


image_path = '../pictures/baku.jpeg'

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)
    
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError()


    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
    ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('Thres image', thresh)

    adaptive_thresh = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)
    cv2.imshow('Adaptive threshold', adaptive_thresh)

    adaptive_thresh = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    cv2.imshow('Adaptive threshold inverted', adaptive_thresh)

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