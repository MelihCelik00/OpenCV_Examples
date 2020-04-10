import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,8000)
counter=0
while True:
	ret, frame = cap.read()
	cv2.imshow('frame',frame)
	counter+=1
	if (cv2.waitKey(1) & 0xFF == ord('q')) or (counter==100):
		break
	#print(counter)
cap.release()
cv2.destroyAllWindows()
