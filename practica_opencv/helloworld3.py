import cv2
imagen = cv2.imread("imagen.png")
cv2.imshow("imagen", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
