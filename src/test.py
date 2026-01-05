import cv2
import os
import numpy as np
import sys
import matplotlib.pyplot as plt


try:
    image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")
    
    
    cv2.imshow('Image', image)

    # channels = (0, 1, 2)
    # for i in range(image.shape[0]):
    #     for j in range(image.shape[1]):
    #         for c in channels:
    #             image[i, j, c] = 255 - image[i, j, c]
        
    # cv2.imshow('Image frame', image)

    result = cv2.convertScaleAbs(image, 1, 1)
    cv2.imshow(' ', result)

    while True:
        key = cv2.waitKey(100) & 0xFF
        if key == 27 or key == ord('q'):
            print('Exiting...')
            break
except FileNotFoundError as fnf:
    print(f"Error: {fnf}")
except ValueError as ve:
    print(f"Image loading error: {ve}")
except KeyboardInterrupt:
    print("Exited using Ctrl + C.")
except Exception as e:
    print(f'Unexpected error occured, {e}!')
finally:
    cv2.destroyAllWindows()