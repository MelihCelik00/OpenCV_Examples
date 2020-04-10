import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,800)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,1000)
ctr = 0
while True:
    ret, frame = cap.read()
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)


    cv2.imshow('frame',frame)
    #cv2.imshow('gray',gray)
    ctr += 1

    if ctr == 1000:
        break

cap.release()
cv2.destroyAllWindows()