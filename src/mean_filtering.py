import cv2
import os
import numpy as np


try:
    image_path = '../pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sobel_image = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sobel_image = np.clip(sobel_image, 0, 255).astype(np.uint8)

    kernel_ = np.ones((2, 2)) / 4
    new_image = cv2.filter2D(image, -1, kernel_)
    mean_filtered = image.copy()

    sharpened_kernel = np.array([
        [-1, -1, -1],
        [ -1,  9,  -1],
        [ -1,  -1, -1]
    ])
    sharpened_image = cv2.filter2D(image, -1, sharpened_kernel)

    for i in range(mean_filtered.shape[0] -  1):
        for j in range(mean_filtered.shape[1] - 1):
            p1 = image[i, j].astype(np.float32)
            p2 = image[i, j + 1].astype(np.float32)
            p3 = image[i + 1, j].astype(np.float32)
            p4 = image[i + 1, j + 1].astype(np.float32)

            kernel = (p1 + p2 + p3 + p4) / 4
            kernel = kernel.astype(np.uint8)

            mean_filtered[i, j] = kernel
            mean_filtered[i, j + 1] = kernel
            mean_filtered[i + 1, j] = kernel
            mean_filtered[i + 1, j + 1] = kernel
    
    cv2.imshow('Original image', image)
    mean_filtered = mean_filtered.astype(np.uint8)
    cv2.imshow('Mean filtered', mean_filtered)
    cv2.imshow('Ready to use method', new_image)
    cv2.imshow('Sharpened image', sharpened_image)
    cv2.imshow('Sobel image', sobel_image)


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
    print(f'Unexpected error occured : {e}.')
finally:
    cv2.destroyAllWindows()

'''
import cv2
import os
import numpy as np


try:
    canvas = np.zeros((6, 6), dtype=np.uint8)
    canvas[0:2, 0:2] = 255
    filtered = canvas.copy()

    for i in range(canvas.shape[0] - 1):
        for j in range(canvas.shape[1] - 1):
            kernel = canvas[i:i + 2, j:j + 2].astype(np.float32)
            mean_value = np.mean(kernel)
            mean_value = np.uint8(mean_value)
            filtered[i, j] = np.uint8(mean_value)
            filtered[i, j + 1] = np.uint8(mean_value)
            filtered[i + 1, j] = np.uint8(mean_value)
            filtered[i + 1, j + 1] = np.uint8(mean_value)

    scale = 60  
    canvas = cv2.resize(canvas, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)
    filtered = cv2.resize(filtered, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_NEAREST)

    cv2.imshow('Mean filtered', filtered)
    cv2.imshow('Canvas', canvas)


    while True:
        key = cv2.waitKey(100) & 0xFF
        if key == ord('q') or key == 27:
            print("Exiting...")
            break

except KeyboardInterrupt:
    print("Exited using Ctrl + C.")
except Exception as e:
    print(f'Unexpected error occured : {e}.')
finally:
    cv2.destroyAllWindows()
'''
