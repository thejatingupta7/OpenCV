import cv2 as cv

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("park", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# Thresholding: It is the binarization of the image

# TODO: Simple Thresholding
threshold, thresh = cv.threshold(gray, 100,  255, cv.THRESH_BINARY)     # 100 can be changed according to intensity of pixels required
cv.imshow("Simple Threshold", thresh)

threshold1, thresh_inv = cv.threshold(gray, 100,  255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# TODO: Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("adaptive thresh", adaptive_thresh)

cv.waitKey(0)