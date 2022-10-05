import cv2

cap = cv2.VideoCapture(0)

while True:
  
    ret, frame = cap.read()
    print(ret)
    image = cv2.flip( frame, 1 ) 
   
 
    cv2.imshow('Image',frame)
 
    key = cv2.waitKey(100)
    if key == 27:
        break
    
    

cap.release()
cv2.destroyAllWindows()
