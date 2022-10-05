#importing required modules
import cv2
import numpy as np

# Loading teh image
image1 = cv2.imread('YOLO_test.jpg')

# Converting the image to grayscale
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# Types of thresholding techniques
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)

# output
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)

# Close output
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
