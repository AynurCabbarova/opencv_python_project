'''
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

try:
    image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Grayscale image', grayscale_image)

    canvas = np.zeros((image.shape[:2]), dtype='uint8')
    circle = cv2.circle(canvas.copy(), (image.shape[1] // 2, image.shape[0] // 2), 70, 255, -1)

    mask = cv2.bitwise_and(grayscale_image, grayscale_image, mask = circle)    
    cv2.imshow('Mask', mask)

    gray_hist = cv2.calcHist([grayscale_image], [1], mask, [256], [0, 256])

    plt.figure()
    plt.title('Grayscale Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')
    plt.plot(gray_hist)
    plt.xlim([0, 256])
    plt.show()

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
'''

#displaying  colorful histogram
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

try:
    image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'

    if not os.path.exists(image_path):
        raise FileNotFoundError("Image file does not exist!")

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Failed to load the image. The format may be unsupported or the file may be corrupted.")
    
    canvas = np.zeros((image.shape[:2]), dtype='uint8')
    mask = cv2.circle(canvas, (image.shape[1] // 2, image.shape[0] // 2), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('Masked image', masked)

    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')

    colors = ('b', 'g', 'r')
    for i, col in enumerate(colors):
        hist = cv2.calcHist([image], [i], mask, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    plt.show()
        
    ''' for dominant color
    colors = ('b', 'g', 'r')
    color_intensivity = []

    for i, color in enumerate(colors):
        color_hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        total = np.sum(color_hist)
        color_intensivity.append(total)
        plt.plot(color_hist, color=color)

    plt.legend(['Blue', 'Green', 'Red'])


    dominant_index = np.argmax(color_intensivity)
    dominant_color = ['Blue', 'Green', 'Red'][dominant_index]

    print(f'Dominant color is {dominant_color}.')
    '''

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