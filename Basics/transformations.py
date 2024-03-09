import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("img", img)


# TODO: Translation - shifting the image on x and y-axis

def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])  # translation matrix
    dimensions = (img.shape[1], img.shape[0])  # (width, height)
    return cv.warpAffine(img, transMat, dimensions)
# -x --> left
# -y --> up
#  x --> right
#  y --> down


translated = translate(img, 100, 100)
cv.imshow("translated", translated)


# TODO: Rotation - specify any rotation point and rotate from that only

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)               # clockwise
# rotated = rotate(img, 45)               # anti-clockwise
cv.imshow("rotated", rotated)

rotated_2nd = rotate(rotated, -45)
cv.imshow("rotated_2nd", rotated_2nd)


# TODO: Resizing

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)      # cubic(slower, higher quality) or linear--> good quality (use in enlarging), area --> decreased quality
cv.imshow("resized", resized)


# TODO: Flipping

flipped = cv.flip(img, 0)           # flip vertical
# flipped = cv.flip(img, 1)         # flip horizontal
# flipped = cv.flip(img, -1)        # flip both vertically & horizontally
cv.imshow("flip", flipped)


# TODO: Cropping

cropped = img[200:300, 300:400]
cv.imshow("croppedd", cropped)

# ---------------------------------------------------------------------------
cv.waitKey(0)
