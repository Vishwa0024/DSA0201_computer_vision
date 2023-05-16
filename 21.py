#laplacian filter
import cv2
import  numpy as np
kernel = np.array([[0, 1, 0], [1, -8, 1], [0, 1, 0]])
image = cv2.imread("C:/Users/vishwa2003/Downloads/lion-sitting-in-sun.jpg")
image = cv2.resize(image,(255,255))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
laplacian = cv2.Laplacian(gray, cv2.CV_64F, ksize=3)
sharpened = gray - 0.5*laplacian
cv2.imshow('Original', gray)
cv2.imshow('Sharpened', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
   