import cv2 

img = cv2.imread("abc.jpg")

blur = cv2.GaussianBlur(img,(11,11),cv2.BORDER_DEFAULT)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Blurred Image', blur)
cv2.imshow('Gray Scale', gray)
cv2.imshow('HSV', hsv)

cv2.waitKey()
cv2.destroyAllWindows()