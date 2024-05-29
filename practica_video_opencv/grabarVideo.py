import cv2
import numpy as np
captura = cv2.VideoCapture(0)
salida = cv2.VideoWriter('salida.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

while (captura.isOpened()):
    ret, imagen = captura.read()
    if ret == True:
        cv2.imshow('video', imagen)
        salida.write(imagen)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else: 
        break

cap = cv2.VideoCapture("1.mp4")
_, img = cap.read()
averageValue1 = np.float32(img)
while(1):
    cv2.accumulateWeighted(img, averageValue1, 0.02)
    resultingFrames1 = cv2.convertScaleAbs(averageValue1)
    cv2.imshow('InputWindow', img)
    cv2.imshow('averageValue1', resultingFrames1)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()

salida.release()
cv2.destroyAllWindows()