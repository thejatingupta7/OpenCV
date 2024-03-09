import cv2 as cv
import numpy as np

# Pixel is turned on  if 1
# Pixel is turned off if 0

blank = np.zeros((400, 400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("rectangle", rectangle)
cv.imshow("circle", circle)

# TODO: bitwise AND --> intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("AND", bitwise_and)

# TODO: bitwise OR --> both intersecting & non-intersecting region
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("OR", bitwise_or)

# TODO: bitwise XOR --> non_intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("XOR", bitwise_xor)

# TODO: bitwise NOT -->
bitwise_not = cv.bitwise_not(circle)
cv.imshow("NOT", bitwise_not)

# -------------------------------------------------------------
cv.waitKey(0)