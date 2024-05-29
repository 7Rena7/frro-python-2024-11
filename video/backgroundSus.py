import cv2
import numpy as np

cap = cv2.VideoCapture("1.mp4")
ret, img = cap.read()
if not ret:
    print("Error: Couldn't read the video file")
    cap.release()
    exit()

averageValue1 = np.float32(img)

while True:
    ret, img = cap.read()
    if not ret:
        break
    
    cv2.accumulateWeighted(img, averageValue1, 0.02)
    resultingFrames1 = cv2.convertScaleAbs(averageValue1)
    
    cv2.imshow('InputWindow', img)
    cv2.imshow('averageValue1', resultingFrames1)
    
    k = cv2.waitKey(30) & 0xff
    if k == 27:  # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()