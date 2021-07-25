import cv2

cap = cv2.VideoCapture(0)

n=0

while True :
    ok, frame = cap.read()


    if not ok:
        break

    n = n+1

    cv2.putText(frame,str(n),(30,50),cv2.FONT_ITALIC,1,(0,0,255))

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break