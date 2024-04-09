import cv2 as cv
import numpy as np

def rescale(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread("Photos/cats.jpg")
blank = np.zeros(img.shape[:2], dtype='uint8')

if img is None:
    print("Image not found")
else:
    while True:
        r_frame = rescale(img)
        cv.imshow("Cats", r_frame)

        gray = cv.cvtColor(r_frame, cv.COLOR_BGR2GRAY)
        cv.imshow("Gray", gray)

        blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
        cv.imshow("Blur", blur)

        edge = cv.Canny(blur, 125, 175)
        cv.imshow("Edge", edge)

        contours, _ = cv.findContours(edge, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        contour_img = np.zeros_like(r_frame)
        cv.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
        cv.imshow("Contours drawn", contour_img)

        if cv.waitKey(0) & 0xFF == ord('d'):
            break

cv.destroyAllWindows()