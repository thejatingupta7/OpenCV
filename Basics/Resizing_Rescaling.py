import cv2 as cv


def rescale_frame(frame, scale=1.75):
    # work for Images, Videos and live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def change_resolution(width, height):
    # for Live Videos
    capture.set(3, width)
    capture.set(4, height)


# TODO: Resizing an Image
img = cv.imread("../Resources/Photos/cat.jpg")
img2 = rescale_frame(img)
cv.imshow("cat", img2)
cv.waitKey(0)

# TODO: Resizing videos
capture = cv.VideoCapture("../Resources/Videos/kitten.mp4")
while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_frame(frame)

    cv.imshow("capture", frame)
    cv.imshow("Video Rescaled", frame_resized)
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()
