import numpy as np
import cv2 as cv
img = cv.imread('OpenCV Logo1.png')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

cv.drawContours(img, contours, -1, (255, 212, 59), 3)


cv.imshow('Imagae', img)
cv.imshow('Image_Gray', img_gray)
cv.waitKey(0)
cv.destroyAllWindows()