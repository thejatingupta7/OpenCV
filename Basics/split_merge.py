import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("park", img)

# TODO: Splitting the image into color channels
b, g, r = cv.split(img)
cv.imshow("Blue", b)
cv.imshow("Green", g)
cv.imshow("Red", r)
# these above images are shown in grayscale
# lighter the region, more the color presence
# darker the region, lesser the color presence


# TODO: Merging the separated color channels
merged = cv.merge([b, g, r])
cv.imshow("merged", merged)

# TODO: Using merge to show splitted images in color
b, g, r = cv.split(img)

blank = np.zeros(img.shape[:2], dtype="uint8")
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("blue", blue)
cv.imshow("red", red)
cv.imshow("green", green)

# ---------------------------------------------------------
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.waitKey(0)