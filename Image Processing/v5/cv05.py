import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage .png')

ret1 = cv2.resize(img1, (1572,790))
ret2 = cv2.resize(img2, (1572,790))

rows, cols, channels = ret2.shape
roi = ret1[0:rows,0:cols]

img2gray = cv2.cvtColor(ret2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)


mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(ret2, ret2, mask=mask)

dst = cv2.add(img1_bg,img2_fg)
ret1[0:rows,0:cols] = dst

cv2.imshow('res',ret1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dst',dst)


#add = ret1 + ret2
#add = cv2.add(ret1,ret2)
#weighted = cv2.addWeighted(ret1, 0.6, ret2, 0.4, 0)
#cv2.imshow('add',add)
#cv2.imshow('weighted',weighted)


#cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows