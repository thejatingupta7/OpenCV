import cv2 as cv
#
# # TODO: Reading an Image
# img = cv.imread("../Resources/Photos/cat.jpg")
# cv.imshow("cat", img)
# cv.waitKey(0)   # wait for an infinite amount of time
#
#
# # TODO: Reading videos
# video = cv.VideoCapture("../Resources/Videos/kitten.mp4")
# while True:                                     # while loop for reading capture frame by frame
#     isTrue, frame = video.read()                # capture is getting read by capture.read()
#     cv.imshow("capture", frame)                   # displaying capture frame by frame
#     if cv.waitKey(20) & 0xFF == ord("d"):
#         break
#
# video.release()
# cv.destroyAllWindows()



# reading live camera
capture = cv.VideoCapture(0)                    # integer references to webcams - 0 for default cam
while True:                                     # while loop for reading capture frame by frame
    isTrue, frame = capture.read()              # capture is getting read by capture.read()
    cv.imshow("capture", frame)                 # displaying capture frame by frame
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()