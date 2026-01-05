import cv2
import numpy as np

image_path = '../pictures/baku.jpeg'
image = cv2.imread(image_path)
b, g, r = cv2.split(image)
zeros = np.zeros_like(b)
b = cv2.merge([b, zeros, zeros])
g = cv2.merge([zeros, g, zeros])
r = cv2.merge([zeros, zeros, r])
cv2.imshow('r', r) 
cv2.imshow('b', b) 
cv2.imshow('g', g)
cv2.imshow('Test image', image)
cv2.waitKey(0)