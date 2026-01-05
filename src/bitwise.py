import cv2
import numpy as np


try:
    canvas = np.zeros([400, 400], dtype='uint8')

    rectangle = cv2.rectangle(canvas.copy(), (30, 30), (370, 370), 255, -1)
    circle = cv2.circle(canvas.copy(), (200, 200), 200, 255, -1)
    
    cv2.imshow('Rectangle', rectangle)
    cv2.imshow('Circle', circle)
    
    bitwise_not = cv2.bitwise_not(circle)
    cv2.imshow('Bitwise not', bitwise_not)
    
    bitwise_and = cv2.bitwise_and(rectangle, circle)
    cv2.imshow('Bitwise and', bitwise_and)
    
    bitwise_or = cv2.bitwise_or(rectangle, circle)
    cv2.imshow('Bitwise or', bitwise_or)
    
    bitwise_xor = cv2.bitwise_xor(rectangle, circle)
    cv2.imshow('Bitwise xor', bitwise_xor)

    bitwise_res = bitwise_xor + bitwise_and 
    cv2.imshow('Result', bitwise_res)
    
    while True:
        key = cv2.waitKey(100) & 0xFF
        if key in [ord('q'), 27]:
            print('Exiting...')
            break
    
except KeyboardInterrupt:
    print('Keyboard interrupted, exiting by clicking Ctrl + C!')
except Exception as e:
    print(f'Unexpected error occured, {e}!')
finally:
    cv2.destroyAllWindows()