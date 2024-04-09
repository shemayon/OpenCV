import cv2 as cv
import numpy as np


def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


img = cv.imread(r"Photos\lady.jpg")
if img is None:
    print("image not found")
else:
    while True:
        r_frame = rescale(img, scale = 0.5)
        cv.imshow("image", r_frame)
        if cv.waitKey(0) & 0xFF == ord("d"):
            break


#translation
def translate(r_frame, x,y):
    transMat = np.float32([
        [1,0,x],[0,1,y]
    ])
    dimension = (r_frame.shape[1], r_frame.shape[0])

    return cv.warpAffine(r_frame, transMat, dimension)

trans = translate(r_frame, -100, 100)
cv.imshow("translated", trans)

#rotation
def rotation(r_frame, angle, rotPoint = None):
    (height, width) = r_frame.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(r_frame, rotMat, dimensions)

rot = rotation(r_frame, 180)
cv.imshow("rotated Image", rot)



cv.waitKey(0)