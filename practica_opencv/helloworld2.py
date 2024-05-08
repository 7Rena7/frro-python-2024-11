import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("videoplayback.mp4")
# cap = cv2.VideoCapture("rtsp://192.168.1.2:8080/out.h264")

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Video ended")
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
