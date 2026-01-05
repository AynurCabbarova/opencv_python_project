import cv2
import numpy as np

def nothing(x):
    pass

image_path = '/home/aynur/Desktop/opencv_python/pictures/baku.jpeg'
image = cv2.imread(image_path)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.namedWindow('Trackbars')

cv2.createTrackbar('H_min','Trackbars',0,179,nothing)
cv2.createTrackbar('H_max','Trackbars',179,179,nothing)
cv2.createTrackbar('S_min','Trackbars',0,255,nothing)
cv2.createTrackbar('S_max','Trackbars',255,255,nothing)
cv2.createTrackbar('V_min','Trackbars',0,255,nothing)
cv2.createTrackbar('V_max','Trackbars',255,255,nothing)

while True:
    h_min = cv2.getTrackbarPos('H_min','Trackbars')
    h_max = cv2.getTrackbarPos('H_max','Trackbars')
    s_min = cv2.getTrackbarPos('S_min','Trackbars')
    s_max = cv2.getTrackbarPos('S_max','Trackbars')
    v_min = cv2.getTrackbarPos('V_min','Trackbars')
    v_max = cv2.getTrackbarPos('V_max','Trackbars')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Original', image)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == 27:  
        break

cv2.destroyAllWindows()