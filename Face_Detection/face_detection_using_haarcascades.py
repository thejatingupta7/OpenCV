# Face Detection --> performed using classifiers
# Classifier is an algo that decides if an image is +ve or -ve, whether a face is present or not

# classifiers take a lot of images to be trained
# but opencv comes with a lot of pre-trained classifiers

# 2 basic types of classifiers are: 1. haarcascades 2. local binary patterns (advanced)

# https://github.com/opencv/opencv/tree/master/data/haarcascades
# we downloaded face/detection/default xml file from the above link that is our pre-built classifier

# ---------------------------------------------------------------------------------------------------

import cv2 as cv

img = cv.imread("../Resources/Photos/group 1.jpg")
cv.imshow("lady", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("haar_face.xml")

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)       # change minNeighbors to get opencv detect clearly
# faces_rect gets a list of coordinates of edges of a face detected
# print(faces_rect)
print(f"Number of faces found: {len(faces_rect)}")

# drawing a rectangle over the coordinates of the detected image
for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected faces", img)



# ---------------------------------------------------------------------------------------------------
cv.waitKey(0)