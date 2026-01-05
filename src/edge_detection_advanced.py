import cv2
import os
import numpy as np


image_path = '../test/test_image_2.jpeg'

try:
    if not os.path.exists(image_path):
        raise FileNotFoundError(image_path)
    
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError()
    
    cv2.imshow('Image Frame', image)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)

    lap = cv2.Laplacian(image, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    cv2.imshow('Laplacian image', lap)

    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
    combined_sobel = cv2.bitwise_or(sobelx, sobely)
    cv2.imshow('Sobel x ', sobelx)
    cv2.imshow('Sobek y', sobely)
    cv2.imshow('Combined sobel', combined_sobel)

    canny = cv2.Canny(gray, 150, 175)
    cv2.imshow('Cannied', canny)

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