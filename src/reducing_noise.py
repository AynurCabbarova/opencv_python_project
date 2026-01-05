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
    
    # Background subtractor yaratmaq
    backSub = cv2.createBackgroundSubtractorMOG2()

    # Şəkli grayscale formatına çevirmək
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Background subtraction tətbiq etmək
    fg_mask = backSub.apply(gray)

    # Hərəkətli obyektləri ayırmaq üçün maska ilə şəkli məhdudlaşdırırıq
    fg_objects = cv2.bitwise_and(image, image, mask=fg_mask)

    # Son nəticəni göstərmək
    cv2.imshow('Foreground Objects', fg_objects)

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

