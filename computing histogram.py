import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescale(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


img = cv.imread("Photos/group 1.jpg")

if img is None:
    print("Image not found")
else:
    while True:
        r_frame = rescale(img, scale = 0.5)
        cv.imshow("Cat", r_frame)

        gray = cv.cvtColor(r_frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Gray", gray)

        gray_hist = cv.calcHist([gray], [0],None, [256],[0,256])

        plt.figure()
        plt.title("Group histogram")
        plt.xlabel("bins")
        plt.ylabel("No.of hist")
        plt.plot(gray_hist)
        plt.xlim([0,256])
        plt.show()

        if cv.waitKey(0) & 0xFF==ord('d'):
            break
cv.destroyAllWindows()

