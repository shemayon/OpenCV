# importing image
import cv2 as cv
import numpy as np

def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread("Photos/lady.jpg")
if img is None:
    print("Image not found")
else:
    while True:
        r_frame = rescale(img, scale = 0.5)
        cv.imshow("Image", r_frame)
        if cv.waitKey(1000):
            break

#grayscale
    gray = cv.cvtColor(r_frame, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)

#blur
    blur = cv.GaussianBlur(r_frame, (5,5), cv.BORDER_DEFAULT)
    cv.imshow("blur", blur)
    cv.waitKey(1000)

#edge cascade
    canny = cv.Canny(r_frame, 125,175)
    cv.imshow("cascade", canny)
    cv.waitKey(1000)

#Dilating the image
    d = cv.dilate(canny, (3,3), iterations = 1)
    cv.imshow("dilate", d)
    cv.waitKey(1000)

#eroding
    e = cv.erode(d, (3,3), iterations = 1)
    cv.imshow("erode", e)
    cv.waitKey(1000)

cv.destroyAllWindows()