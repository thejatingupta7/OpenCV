import cv2 as cv
import numpy as np


img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("cats", img)

# A contour is a continuous line or curve of pixels that joins the boundary of an object
# Mathematical POV: contours and edges looks same but aren't

# TODO: Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

# TODO: Getting the boundaries of image objects
canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

# TODO: getting the contours
# contours is the list of all the coordinates of the contours found in the image
# hierarchies  refers to hierarchical representation of contours in the image
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# cv.RETR_LIST --> all contours
# cv.RETR_TREE --> for hierarchical contours
# cv.RETR_EXTERNAL --> external contours
# cv.CHAIN_APPROX_NONE   --> It returns the contours
# cv.CHAIN_APPROX_SIMPLE --> Compresses and returns the contours
print(f"{len(contours)} Contours found in the image!")
# Bluring reduces the number of contours

# TODO: drawing the contours on a blank image / visualizing the contours
blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("contours_on_blank", blank)

# TODO: setting threshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


cv.waitKey(0)