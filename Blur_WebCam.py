import cv2

cap = cv2.VideoCapture(0)

while True:
  
    ret, frame = cap.read()
    print(ret)
    image = cv2.flip( frame, 1 ) 
   
 
    res = cv2.GaussianBlur(frame,(41,41),cv2.BORDER_DEFAULT)
    cv2.imshow('result.jpg', res)
 
    key = cv2.waitKey(100)
    if key == 27:
        break
    
    

cap.release()
cv2.destroyAllWindows()
