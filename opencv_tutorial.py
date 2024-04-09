import cv2 as cv

def rescale(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    r_frame = rescale(frame, scale = 0.2)
    if frame is None:
        break
    cv.imshow("dog", r_frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

