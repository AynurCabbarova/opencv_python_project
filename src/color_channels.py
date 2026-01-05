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
    
    blank = np.zeros(image.shape[:2], dtype='uint8')
    
    cv2.imshow('Original image', image)

    '''
    #same as split
    blue, green, red = image[:, :, 0], image[:, :, 1], image[:, :, 2]
    cv2.imshow('Blue', blue)
    cv2.imshow('Green', green)
    cv2.imshow('Red', red)
    '''

    blue, green, red = cv2.split(image)
    cv2.imshow('Blue', blue)
    cv2.imshow('Green', green)
    cv2.imshow('Red', red)

    blue_ = cv2.merge([blue, blank, blank])
    green_ = cv2.merge([blank, green, blank])
    red_ = cv2.merge([blank, blank, red])

    img_bgr = cv2.hconcat([blue, green, red])
    img_bgr_ = cv2.vconcat([blue, green, red])

    new_image = image.copy()
    new_image[:, :, 0] = 0
    new_image[:, :, 1] = 0
    cv2.imshow('New image', new_image)# same as red_ = cv2.merge([blank, blank, red])

    print(image.shape)
    print(blue.shape)
    print(green.shape)
    print(red.shape)

    cv2.imshow('Merged blue', blue_)
    cv2.imshow('Merged green', green_)
    cv2.imshow('Merged red', red_)

    merged_image = cv2.merge([blue, green, red])
    cv2.imshow('Merged image', merged_image)

    cv2.imshow('Vconcat result', img_bgr_)
    cv2.imshow('Hconcat result', img_bgr)

    print(merged_image.shape)

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