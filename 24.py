import cv2
import numpy as np
img = cv2.imread("C:/Users/vishwa2003/Downloads/lion-sitting-in-sun.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.array([[0,-1,0],[-1,5,-1], [0,-1,0]])
kernel_1 = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])


filtered_img = cv2.filter2D(gray_img, -1, kernel)
sharpened_img = cv2.addWeighted(gray_img, 1.5, filtered_img, -0.5, 0)
sharpened_img = cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)

filtered_img_1 = cv2.filter2D(gray_img, -1, kernel_1)
sharpened_img_1 = cv2.addWeighted(gray_img, 1.5, filtered_img_1, -0.5, 0)
sharpened_img_1 = cv2.cvtColor(sharpened_img_1, cv2.COLOR_GRAY2BGR)

cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)

cv2.imshow('Sharpened_Image', sharpened_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
