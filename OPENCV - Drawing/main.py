import numpy as np
import cv2

img = np.zeros ((512,512,3), np.uint8)

cv2.rectangle(img,(447,80),(100,0),(0,255,0),10)
cv2.circle (img, (447,63), 63, (0,0,255), -1)

cv2.imshow("Display window", img)
cv2.waitKey(0)