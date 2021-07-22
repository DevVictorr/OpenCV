import cv2


img = cv2.imread("image.jpg")

cv2.line(img,(0,0),(500,500),(100,0,0),15)
cv2.line(img,(0,50),(500,550),(100,0,0),15)

cv2.imshow('image',img)
cv2.waitKey(0)