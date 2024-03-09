import cv2 as cv

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("park", img)

# TODO: Average blur
average = cv.blur(img, (3, 3))
cv.imshow("average blur", average)

# TODO: Gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gauss)

# TODO: Median blur
median = cv.medianBlur(img, 7)
cv.imshow("median blur", median)

# TODO: Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("bilateral", bilateral)

# ------------------------------------------------------
cv.waitKey(0)