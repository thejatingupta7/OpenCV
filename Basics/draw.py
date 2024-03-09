import cv2 as cv
import numpy as np

# [height, width, colors] = [500, 500, 3] RGB
blank = np.zeros((500, 500, 3), dtype="uint8")          # blank sheet - black colored
img = cv.imread("../Resources/Photos/cat.jpg")          # imported image

# TODO 1. Paint the image a certain color
blank[:] = 0, 255, 0
cv.imshow("painted", blank)

# TODO 2. Make a certain area colored
blank[200:300, 300:400] = 0, 255, 0
cv.imshow("painted", blank)

# TODO 3. Draw a Rectangle
cv.rectangle(blank, (0, 0), (300, 200), (0, 255, 0), thickness=2)
cv.imshow("rectangle", blank)

# TODO 4. Fill the Rectangle
cv.rectangle(blank, (0, 0), (300, 200), (0, 255, 0), thickness=cv.FILLED)
cv.rectangle(blank, (0, 0), (300, 200), (0, 255, 0), thickness=-1)
# above both works the same
cv.imshow("rectangle", blank)

# TODO 5. Draw a Circle
cv.circle(blank, (300, 200), 40, (0, 255, 0), thickness=2)
cv.imshow("circle", blank)
# to fill the circle put thickness = -1 or cv.FILLED

# TODO 6. Draw a line
cv.line(blank, (0, 0), (300, 200), (0, 255, 0), thickness=3)
cv.imshow("line", blank)

# TODO 7. Write Text on an image
cv.putText(blank, "Hello World!", (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 200, 0), 2)
cv.imshow("text", blank)


cv.waitKey(0)
