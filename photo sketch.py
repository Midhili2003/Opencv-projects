# import library
import cv2 as cv

#Read the image
img = cv.imread("Deepika Padukone.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#invert a image
inverted_gray_img = 255 - gray_img

#blur the image by gaussian function
blurred_img = cv.GaussianBlur(inverted_gray_img, (21,21), 0)

#invert the blurred image
inverted_blurred_img = 255 - blurred_img

#create the pencil sketch img
pencil_sketch_img = cv.divide(gray_img, inverted_blurred_img, scale = 256.0)


#show the image
cv.imshow('original Image', img)
cv.imshow('New Image', pencil_sketch_img)
cv.waitKey(0)
