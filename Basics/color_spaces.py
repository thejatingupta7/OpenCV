import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("../Resources/Photos/park.jpg")
cv.imshow("park", img)

# TODO: BGR (default OpenCV format) to GrayScale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# TODO: BGR to HSV (Hue Saturation value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)

# TODO: BGR to LAB (L*a*b)
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# TODO: BGR vs RGB
# BGR is for OpenCV, and RGB is inverse of BGR
plt.imshow(img)             # BGR image is displayed using matplotlib
plt.show()

# TODO: BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
plt.imshow(rgb)
plt.show()

# we can convert all these formats to BGR back,
# but we can't directly convert hsv to lab, etc.

cv.waitKey(0)