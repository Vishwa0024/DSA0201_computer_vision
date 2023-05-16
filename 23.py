import cv2
import numpy as np
img = cv2.imread("C:/Users/vishwa2003/Downloads/lion-sitting-in-sun.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
mask = cv2.subtract(gray_img, blurred_img)
sharpened_img = cv2.addWeighted(gray_img, 1.5, mask, -0.5, 0)
sharpened_img = cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image', sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
