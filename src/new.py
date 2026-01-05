# import cv2
# import numpy as np

# video_path = '/home/aynur/Desktop/opencv_python/videos/highway.mp4'
# video = cv2.VideoCapture(video_path)

# while True:
#     ret, frame = video.read()

#     if not ret:
#         break

#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     lower_purple = np.array([140, 50, 50])
#     upper_purple = np.array([170, 255, 255])

#     mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)

#     kernel = np.ones((7, 7), np.uint8)
#     mask_purple = cv2.morphologyEx(mask_purple, cv2.MORPH_CLOSE, kernel, iterations=2)

#     contours, _ = cv2.findContours(mask_purple, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#     if contours:
#         for contour in contours:
#             area = cv2.contourArea(contour)

#             if area > 50:
#                 x, y, w, h = cv2.boundingRect(contour)

#                 cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)

#     cv2.imshow('Mask', mask_purple)
#     cv2.imshow('Tracking', frame)
    

#     if cv2.waitKey(10) & 0xFF == 27:
#         break


# video.release()
# cv2.destroyAllWindows()

import cv2
import numpy as np

video_path = '/home/aynur/Desktop/opencv_python/videos/highway.mp4'
video = cv2.VideoCapture(video_path)

next_object_id = 0
objects = {}  # id -> centroid
lost = {}     # id -> frames lost
max_lost = 30

def compute_centroid(x, y, w, h):
    return (int(x + w/2), int(y + h/2))

while True:
    ret, frame = video.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_purple = np.array([140, 50, 50])
    upper_purple = np.array([170, 255, 255])
    mask_purple = cv2.inRange(hsv, lower_purple, upper_purple)
    contours, _ = cv2.findContours(mask_purple, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    detections = []
    boxes = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 50:
            x, y, w, h = cv2.boundingRect(contour)
            centroid = compute_centroid(x, y, w, h)
            detections.append(centroid)
            boxes.append((x, y, w, h))

    updated_objects = {}
    assigned_objects = set()

    for i, centroid in enumerate(detections):
        # Hər detection üçün ən yaxın mövcud obyekt tap
        min_dist = float('inf')
        object_id_match = None
        for object_id, obj_centroid in objects.items():
            if object_id in assigned_objects:
                continue
            dist = np.linalg.norm(np.array(centroid) - np.array(obj_centroid))
            if dist < min_dist:
                min_dist = dist
                object_id_match = object_id
        # Yaxınlıq threshold (obyekti eyni hesab etmək üçün)
        if min_dist < 50 and object_id_match is not None:
            updated_objects[object_id_match] = centroid
            lost[object_id_match] = 0
            assigned_objects.add(object_id_match)
        else:
            updated_objects[next_object_id] = centroid
            lost[next_object_id] = 0
            next_object_id += 1

    # İtirilmiş obyektləri saxla
    for object_id in objects:
        if object_id not in updated_objects:
            lost[object_id] += 1
            if lost[object_id] <= max_lost:
                updated_objects[object_id] = objects[object_id]

    objects = updated_objects.copy()

    # Vizualizasiya: bounding box + ID
    for object_id, centroid in objects.items():
        # Centroid-ə ən yaxın bounding box
        min_dist = float('inf')
        closest_box = None
        for (x, y, w, h) in boxes:
            c = compute_centroid(x, y, w, h)
            dist = np.linalg.norm(np.array(c) - np.array(centroid))
            if dist < min_dist:
                min_dist = dist
                closest_box = (x, y, w, h)
        if closest_box and min_dist < 50:
            x, y, w, h = closest_box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, str(object_id), (centroid[0]-10, centroid[1]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Mask', mask_purple)
    cv2.imshow('Tracking', frame)

    if cv2.waitKey(10) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
