import cv2 as cv
import numpy as np

img = cv.imread("../Resources/Photos/cats.jpg")
cv.imshow("img", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# TODO: Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("laplacian", lap)

# TODO: Sobel
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

cv.imshow("Sobel_x", sobel_x)
cv.imshow("Sobel_y", sobel_y)
cv.imshow("Sobel_combined", combined_sobel)

# TODO: Canny Edge Detector
canny = cv.Canny(gray, 150, 175)
cv.imshow("canny", canny)



# -------------------------------------------------------------------
cv.waitKey(0)