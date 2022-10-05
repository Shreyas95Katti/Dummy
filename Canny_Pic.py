import cv2
import numpy as np

img = cv2.imread("abc.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img1 = cv2.inRange(img_hsv, (0,50,20), (5,255,255))
img2 = cv2.inRange(img_hsv, (175,50,20), (180,255,255))
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mask = cv2.bitwise_or(img1, img2 )
croped = cv2.bitwise_and(img, img, mask=mask)
newcroped = cv2.GaussianBlur(croped,(101,101),cv2.BORDER_DEFAULT)
gray_image = cv2.cvtColor(croped, cv2.COLOR_BGR2GRAY)
final = cv2.Canny(img,301,301)

cv2.imshow("mask", mask)
cv2.imshow("croped", croped)
cv2.imshow("final", final)
cv2.waitKey()