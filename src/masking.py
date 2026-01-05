import cv2
import os
import numpy as np

try:
    image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")
    

    canvas = np.zeros(image.shape[:2], dtype='uint8')

    cv2.imshow('Output image', image)
    cv2.imshow('Canvas', canvas)

    #mask = cv2.circle(canvas, (image.shape[1] // 2, image.shape[0] // 2), 100, 255, -1)
    mask = cv2.rectangle(canvas.copy(), (600, 20), (100, 100), 255, -1)
    cv2.imshow('Mask', mask)

    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('Masked image', masked)
    
    rectangle = cv2.rectangle(canvas.copy(), (100, 30), (200, 130), 255, 50)
    circle = cv2.circle(canvas.copy(), (100, 80), 50, 255, 50)
    
    weired_mask = cv2.bitwise_and(circle, rectangle)
    weired_masked = cv2.bitwise_and(image, image, mask=weired_mask)
    cv2.imshow('Weired mask', weired_mask)
    cv2.imshow('Weired mask image', weired_masked)

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
except Exception as e:
    print(f'Unexpected error occured, {e}!')
finally:
    cv2.destroyAllWindows()