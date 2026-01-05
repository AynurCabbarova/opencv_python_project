import cv2
import os
import numpy as np


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

    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayscale = cv2.GaussianBlur(grayscale, (7, 7), cv2.BORDER_DEFAULT)
    
    gx = np.zeros_like(grayscale)
    gy = np.zeros_like(grayscale)
    edges = np.zeros_like(grayscale)

    for i in range(grayscale.shape[0] - 1):
        for j in range(grayscale.shape[1] - 1):
            gx[i][j] = grayscale[i][j + 1] - grayscale[i][j]
            gy[i][j] = grayscale[i + 1][j] - grayscale[i][j]
            edges[i][j] = np.sqrt(gx[i][j] ** 2 + gy[i][j] ** 2)



    edges = handmade_thresholding(edges, 80, 255, 0)
    cv2.imshow('Edge detection', edges)

    canvas = image.copy()
    contours, hierarchies = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 30:
            cv2.drawContours(canvas, [contour], -1, (255, 0, 0), 1)
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(canvas, (x, y), (x + w, y + h), (0, 255, 0), 1)
    cv2.imshow('Canvas', canvas)


    while True:
        key = cv2.waitKey(100) & 0xFF
        if key == ord('q') or key == 27:
            print("Exiting...")
            break

except FileNotFoundError as fnf:
    print(f"Error: {fnf}")
except ValueError as ve:
    print(f"Image loading error: {ve}")
except KeyboardInterrupt:
    print("Exited using Ctrl + C.")
finally:
    cv2.destroyAllWindows()