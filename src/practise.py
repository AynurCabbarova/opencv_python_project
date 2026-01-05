import cv2
import numpy as np
import math


cap = cv2.VideoCapture('/home/aynur/Desktop/opencv_python/videos/highway.mp4')
cxx, cyy = None, None
cxx_g, cyy_g = None, None
cxx_y, cyy_y = None, None
green_list = []
ret, frame = cap.read()
trail = np.zeros_like(frame)


while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_purple = np.array([140, 50, 50])
    upper_purple = np.array([170, 255, 255])

    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    lower_yellow = np.array([25, 50, 50])
    upper_yellow = np.array([35, 255, 255])

    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)

    contours_p, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_g, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_y, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours_p:
        largest_p = max(contours_p, key=cv2.contourArea)

        M = cv2.moments(largest_p)
        # print(type(M))
        # print(M)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            if cxx is not None:
                speed = math.sqrt((cxx - cx)**2 + (cyy - cy)**2)
                dy = cy - cyy
                dx = cx - cxx
                angle_rad = math.atan2(-dy, dx)
                angle_deg = math.degrees(angle_rad)

                direction = ''
                print(speed)

                if angle_deg < 0:
                    angle_deg += 360
                if 315 <= angle_deg or angle_deg < 45:
                    direction = 'right'
                elif 45 <= angle_deg < 135:
                    direction = 'up'
                elif 135 <= angle_deg < 225:
                    direction = 'left'
                else:
                    direction = 'down'

                cv2.putText(frame, f'Direction purple : {direction}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
                cv2.line(trail, (cx, cy), (cxx, cyy), (255, 0, 255))
            
            cxx, cyy = cx, cy

            cv2.circle(frame, (cx, cy), 6, (255, 0, 255), -1)
            x, y, w, h = cv2.boundingRect(largest_p)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)

    if contours_g:
        largest_g = max(contours_g, key=cv2.contourArea)

        M = cv2.moments(largest_g)
        # print(type(M))
        # print(M)

        if M["m00"] != 0:
            cx_g = int(M["m10"] / M["m00"])
            cy_g = int(M["m01"] / M["m00"])

            if len(green_list) <= 10:
                green_list.append([cx_g, cy_g])

            
            if cxx_g is not None:
                speed = math.sqrt((cxx_g - cx_g)**2 + (cyy_g - cy_g)**2)
                dy = cy_g - cyy_g
                dx = cx_g - cxx_g
                angle_rad = math.atan2(-dy, dx)
                angle_deg = math.degrees(angle_rad)

                direction = ''
                print(speed)

                if angle_deg < 0:
                    angle_deg += 360
                if 315 <= angle_deg or angle_deg < 45:
                    direction = 'right'
                elif 45 <= angle_deg < 135:
                    direction = 'up'
                elif 135 <= angle_deg < 225:
                    direction = 'left'
                else:
                    direction = 'down'

                cv2.putText(frame, f'Direction green : {direction}', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
                
                for i in range(len(green_list) - 1):
                    cv2.line(trail, (green_list[i][0], green_list[i][1]), (green_list[i + 1][0], green_list[i + 1][1]), (0, 255, 0))
            
            cxx_g, cyy_g = cx_g, cy_g

            cv2.circle(frame, (cx_g, cy_g), 6, (0, 255, 0), -1)
            x, y, w, h = cv2.boundingRect(largest_g)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
    if contours_y:
        largest_y = max(contours_y, key=cv2.contourArea)

        M = cv2.moments(largest_y)
        # print(type(M))
        # print(M)

        if M["m00"] != 0:
            cx_y = int(M["m10"] / M["m00"])
            cy_y = int(M["m01"] / M["m00"])

            
            if cxx_y is not None:
                speed = math.sqrt((cxx_y - cx_y)**2 + (cyy_y - cy_y)**2)
                dy = cy_y - cyy_y
                dx = cx_y - cxx_y
                angle_rad = math.atan2(-dy, dx)
                angle_deg = math.degrees(angle_rad)

                direction = ''
                print(speed)

                if angle_deg < 0:
                    angle_deg += 360
                if 315 <= angle_deg or angle_deg < 45:
                    direction = 'right'
                elif 45 <= angle_deg < 135:
                    direction = 'up'
                elif 135 <= angle_deg < 225:
                    direction = 'left'
                else:
                    direction = 'down'

                cv2.putText(frame, f'Direction yellow : {direction}', (10, 110), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
                cv2.line(trail, (cx_y, cy_y), (cxx_y, cyy_y), (0, 255, 255))
            
            cxx_y, cyy_y = cx_y, cy_y

            cv2.circle(frame, (cx_y, cy_y), 6, (0, 255, 255), -1)
            x, y, w, h = cv2.boundingRect(largest_y)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            
            
    result = cv2.add(frame, trail)
    cv2.imshow('Mask', mask_purple)
    cv2.imshow('Center point', frame)
    cv2.imshow('Trail', trail)
    cv2.imshow('Tracking', result)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    
cv2.destroyAllWindows()
cap.release()