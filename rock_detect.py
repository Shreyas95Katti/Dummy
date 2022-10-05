import cv2

img = cv2.imread("nasa-mars.jpg")
#cv2.imshow("Image", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", img_gray)
contours, hierarchy = cv2.findContours(img_gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)


for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    #if(area > 100):
    x, y, w, h = cv2.boundingRect(contour)
    img_gray = cv2.rectangle(img_gray, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.putText(img_gray, "Rock", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

cv2.imshow("Multiple Color Detection in Real-TIme", img_gray)
cv2.waitKey()
cv2.destroyAllWindows()