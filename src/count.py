# import cv2
# import numpy as np

# image_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'
# image = cv2.imread(image_path)

# height, width = image.shape[:2]
# blank = np.zeros_like(image)

# for i in range(height + width):  
#     for row in range(height):
#         for col in range(width):
#             if row + col <= i:
#                 blank[row, col] = image[row, col]
#             else:
#                 blank[row, col] = 0
#     char = (i % 26) + 97
#     cv2.putText(blank, f'{chr(char)}', (10, 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 255, 0))
#     cv2.imshow('Diagonal Reveal', blank)
#     cv2.waitKey(10)  

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2 
# import numpy as np

# canvas = np.zeros([400, 400, 3], dtype='uint8')
# n = int(input('Enter number n : '))

# for i in range(n + 1):
#     canvas[:] = 0
#     cv2.putText(canvas, f'{n - i}', (170, 220), cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 3, (0, 255, 0), 2)
#     cv2.imshow('CountDown', canvas)
#     cv2.waitKey(1000)


# import cv2
# import os

# file_path = '/home/aynur/Desktop/opencv_python/pictures/highway.jpeg'
# image = cv2.imread(file_path)

# i = 0

# while True:
#     if i % 2 == 0:
#         image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)
#     else:
#         image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_CUBIC)
#     cv2.imshow('Image', image)

#     i += 1

#     key = cv2.waitKey(100) & 0xFF
#     if key == 27 or key == ord('q'):
#         break

# cv2.destroyAllWindows()

# import cv2 
# import os


# base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'Pictures/Screenshots')
# print(base_dir)

# for file in os.listdir(base_dir):
#     file_path = os.path.join(base_dir, file)
#     image = cv2.imread(file_path)
#     cv2.imshow('Image', image)
#     cv2.waitKey(1000)