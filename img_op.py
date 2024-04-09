import numpy as np
import cv2 as cv

blank = np.zeros((500, 500,3), dtype = 'uint8')
cv.imshow("blank", blank)


#adding color
blank[:] = 0,0,255
cv.imshow("color", blank)

#certain portion of the image
img = blank
img[200:300, 300:400] = 255,0,0
cv.imshow("certain", img)

#creating rectangle
img1 = np.zeros((200,200,3), dtype = 'uint8')
cv.rectangle(img1, (0,0), (50,100), (0,255,0), thickness = cv.FILLED)
# cv.imshow("rect", img1)

#creating circle
cv.circle(img1, (30,35), 20, (255,0,0), thickness = cv.FILLED)
cv.imshow("SHAPES", img1)


cv.waitKey(0)