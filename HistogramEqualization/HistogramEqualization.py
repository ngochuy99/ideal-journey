import cv2
import numpy as np

img = cv2.imread('anhthieusang.jpg')
HSVimg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(HSVimg)
v = cv2.equalizeHist(v)
HSVimg = cv2.merge((h,s,v))
ModifiedImg = cv2.cvtColor(HSVimg,cv2.COLOR_HSV2BGR)
cv2.imshow("Can bang sang",np.concatenate((img,ModifiedImg),axis=1))
cv2.waitKey()