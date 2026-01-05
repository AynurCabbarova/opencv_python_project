import cv2
import os

try:
    image_path = '../pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")
    
    #Averaging
    average = cv2.blur(image, (7, 7))

    #Gaussian blur
    gauss = cv2.GaussianBlur(image, (7, 7), 0)

    #Median blur
    median = cv2.medianBlur(image, 7)

    #Bilateral
    bilateral = cv2.bilateralFilter(image, 5, 15, 15)

    cv2.imshow('Original image', image)
    cv2.imshow('Average blurred', average)
    cv2.imshow('Gaussian blur', gauss)
    cv2.imshow('Median blur', median)
    cv2.imshow('Bilateral blur', bilateral)

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