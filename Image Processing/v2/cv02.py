import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
outf = cv2.VideoWriter('output.mp4',fourcc, 20.0,(640,480))

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,8000)
counter=0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    counter+=1
    if (cv2.waitKey(1) & 0xFF == ord('q')) or (counter==100):
        break
    print(counter)
    
cap.release()
outf.release()
cv2.destroyAllWindows()