import cv2
import os
import numpy as np
import sys
import matplotlib.pyplot as plt


def handmade_thresholding(image, threshold, max_value, min_value):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i][j] > threshold:
                image[i][j] = max_value
            else:
                image[i][j] = min_value

    return image

try:
    image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
    cv2.imshow('Thresholding', thresh)

    result = handmade_thresholding(gray.copy(), 125, 255, 0)
    cv2.imshow('Handmade thresholding', result)

    final = np.hstack((thresh, result))
    cv2.imshow('Result', final)

    plt.subplot(1, 2, 1)
    plt.imshow(thresh, cmap='gray')
    plt.title('OpenCV Threshold')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap='gray')
    plt.title('Handmade Threshold')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

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