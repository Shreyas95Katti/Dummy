import cv2 
img = cv2.imread('ieee1.jpg')     
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
cv2.imshow('Grayscale', gray_image)
cv2.waitKey() 
cv2.destroyAllWindows() 

