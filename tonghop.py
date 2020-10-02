import numpy as np
import cv2

#Read jpg(RGB) image
img = cv2.imread("examplejpg.jpg")
cv2.imshow("RGB image",img)

#Convert RGB img to HSV img and show
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV image",hsv_img)

#Split hsv color channel
h,s,v = cv2.split(hsv_img)
height,width = h.shape

#Create fill_data to show h,s,v color channel
fill_data = np.zeros([height,width],dtype="uint8")
imgH = cv2.merge([h,fill_data,fill_data])
imgS = cv2.merge([fill_data,s,fill_data])
imgV = cv2.merge([fill_data,fill_data,v])
# cv2.imshow("H color with fill_data=0",imgH)
# cv2.imshow("S color with fill_data=0",imgS)
# cv2.imshow("V color with fill_data=0",imgV)
hsv_split = np.concatenate((imgH,imgS,imgV),axis=1)
cv2.imshow("Split HSV",hsv_img)

fill_data.fill(255)
imgH = cv2.merge([h,fill_data,fill_data])
imgS = cv2.merge([fill_data,s,fill_data])
imgV = cv2.merge([fill_data,fill_data,v])
# cv2.imshow("H color with fill_data=255",imgH)
# cv2.imshow("S color with fill_data=255",imgS)
# cv2.imshow("V color with fill_data=255",imgV)
hsv_split = np.concatenate((imgH,imgS,imgV),axis=1)
cv2.imshow("Split HSV 255",hsv_split)

#Modify brightness(v channel)
lim = 255 - 100
v[v > lim] = 255
v[v <= lim] += 100
bright_hsv_img = cv2.merge((h,s,v))
cv2.imshow("Brighter HSV image",bright_hsv_img)
bright_rgb_img = cv2.cvtColor(bright_hsv_img,cv2.COLOR_HSV2RGB)
cv2.imshow("Brighter RGB image",bright_rgb_img)

#HSV to BGR
bgr_img = cv2.cvtColor(hsv_img,cv2.COLOR_HSV2BGR)
cv2.imshow("BGR_Image",bgr_img)
#Wait for key press to exit
cv2.waitKey()
