#single object tracking
'''
import cv2 

video_path = '/home/aynur/Desktop/opencv_python/videos/highway.mp4'
video = cv2.VideoCapture(video_path)

ret, frame = video.read()

if not ret:
    print('Unable to open video!')
    exit()


roi = cv2.selectROI('Select ROI', frame)

tracker = cv2.TrackerKCF_create()
tracker.init(frame, roi)

while True:
    ret, frame = video.read()

    if not ret:
        break

    success, bbox = tracker.update(frame)

    if success:
        x, y, w, h = map(int, bbox)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    else:
        cv2.putText(frame, 'Lost', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)

    cv2.imshow('Tracking', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break


video.release()
cv2.destroyAllWindows()        
'''


#multi object tracking 
'''
import cv2

video_path = '/home/aynur/Desktop/opencv_python/videos/highway.mp4'
video = cv2.VideoCapture(video_path)

ret, frame = video.read()

if not ret:
    print('Unable to open video.')
    exit()

rois = []

while True:
    roi = cv2.selectROI('Select ROI(s)', frame)
    if roi == (0, 0, 0, 0):
        break

    rois.append(roi)

cv2.destroyAllWindows()

trackers = []

next_id = 1

for roi in rois:
    tracker = cv2.TrackerKCF_create()
    tracker.init(frame, roi)
    trackers.append([next_id, tracker, 'Active', 0])
    next_id += 1

while True:
    ret, frame = video.read()

    if not ret:
        break

    for tracker in trackers:
        success, bbox = tracker[1].update(frame)
        if success:
            x, y, w, h = map(int, bbox)
            cv2.putText(frame, f'{tracker[0]}', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        else:
            cv2.putText(frame, f'Object {tracker[0]} state : {tracker[2]}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 255), 2)
            tracker[2] = 'Lost'
            tracker[3] += 1

    cv2.imshow('Multi Tracking', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break


video.release()
cv2.destroyAllWindows()
'''

import cv2
import numpy as np
import math


cap = cv2.VideoCapture('/home/aynur/Desktop/opencv_python/videos/highway.mp4')
cxx, cyy = None, None
xxc, yyc = None, None
ret, frame = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)
trail = np.zeros_like(frame)
trail_tracker = np.zeros_like(frame)
tracker = cv2.TrackerCSRT_create()
tracker_started = False
colors = (255, 255, 255)
average = 0
count = 0
summa = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_contour = frame.copy()
    frame_tracking = frame.copy()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_purple = np.array([140, 50, 50])
    upper_purple = np.array([170, 255, 255])

    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

    contours_p, _ = cv2.findContours(mask_purple, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours_p:
        largest_p = max(contours_p, key=cv2.contourArea)

        M = cv2.moments(largest_p)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            if cxx is not None:
                speed = math.sqrt((cxx - cx)**2 + (cyy - cy)**2)
                pixelspers = fps * speed
                meter_per_pixel = 1 / 50
                mpers = meter_per_pixel * pixelspers
                count += 1
                average = (average * (count - 1) + mpers) / count
                kmperh = mpers * 3.6

                dy = cy - cyy
                dx = cx - cxx
                angle_rad = math.atan2(-dy, dx)
                angle_deg = math.degrees(angle_rad)


                if mpers < 2:
                    colors = (255, 0, 0)

                elif mpers >= 2 and mpers < 8:
                    colors  =(0, 255, 0)
                elif mpers >= 8:
                    colors = (0, 0, 255)

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

                cv2.putText(frame_contour, f'Speed m/s : {mpers}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)
                cv2.line(trail, (cx, cy), (cxx, cyy), (255, 0, 255), 1)
            
            cxx, cyy = cx, cy

            cv2.circle(frame_contour, (cx, cy), 6, (255, 0, 255), -1)
            x, y, w, h = cv2.boundingRect(largest_p)

            if tracker_started is False:
                tracker.init(frame, (x, y, w, h))
                tracker_started = True
            cv2.rectangle(frame_contour, (x, y), (x + w, y + h), colors, 2)
        

    if tracker_started:
        success, bbox = tracker.update(frame)

        if success:
            x, y, w, h = map(int, bbox)
            xc = x + w // 2
            yc = y + h // 2
            if xxc is not None and yyc is not None:
                cv2.line(trail_tracker, (xc, yc), (xxc, yyc), (0, 255, 0), 1)
                if average != 0:
                    cv2.putText(frame_tracking, f'Average speed : {average}', (10, 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 3)

            xxc, yyc = xc, yc
            cv2.rectangle(frame_tracking, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame_tracking, (xc, yc), 6, (0, 255, 0), -1)
        else:
            tracker_started = False
            xxc, yyc = None, None
            if contours_p:
                largest_p = max(contours_p, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(largest_p)
                tracker.init(frame, (x, y, w, h))
                tracker_started = True

            
    result = cv2.add(frame_contour, trail)
    result_ = cv2.add(frame_tracking, trail_tracker)
    cv2.imshow('Mask', mask_purple)
    cv2.imshow('Original video stream', frame)
    output_trail = np.hstack([trail, trail_tracker])
    output_tracking = np.hstack([result, result_])
    output = np.vstack([output_trail, output_tracking])
    cv2.imshow('Result', output)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    
cv2.destroyAllWindows()
cap.release()