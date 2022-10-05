import cv2
import numpy as np
def nothing(x):
    pass
cap = cv2.VideoCapture(0)


cv2.namedWindow("Trackbars")
cv2.createTrackbar("LT", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("UT", "Trackbars", 0, 255, nothing)

while True:
  
    ret, frame = cap.read()
    frame=cv2.GaussianBlur(frame,(9,9),cv2.BORDER_DEFAULT)
    
    image = cv2.flip( frame, 1 ) 
    fram1=image
   
    l_h = cv2.getTrackbarPos("LT", "Trackbars")
    l_s = cv2.getTrackbarPos("UT" ,"Trackbars")
   
   
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    edged = cv2.Canny(gray, l_h,l_s) 
    edgedc= cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
    img_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    
    stacked = np.hstack((fram1,edgedc,img_bgr))
    
 
    cv2.imshow('Trackbars',cv2.resize(stacked,None,fx=0.4,fy=0.4))
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    
 

cap.release()
cv2.destroyAllWindows()
