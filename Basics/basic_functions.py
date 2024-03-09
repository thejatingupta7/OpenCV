import cv2 as cv

img = cv.imread("../Resources/Photos/cat.jpg")
cv.imshow("cat", img)

# TODO 1. Converting image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("grayscale", gray)

# TODO 2. Blur an Image
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# TODO 3. Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow("cascade", canny)

# TODO 4. Dilating the image - Dilates the cascade lines
dilated = cv.dilate(canny, (3, 3), iterations=2)
cv.imshow("dilated", dilated)

# TODO 5. Eroding the image - reverse the dilation
erode = cv.erode(dilated, (3, 3), iterations=2)
cv.imshow("eroded", erode)

# TODO 6. Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)      # cubic gives higher quality than linear or area
cv.imshow("resized", resized)

# TODO 7. Cropping
cropped = img[50:200, 200:400]
cv.imshow("cropped", cropped)


cv.waitKey(0)