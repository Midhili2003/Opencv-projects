import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Rashmika Mandanna.jpg", 0)
canny = cv.Canny(img, 110, 170)

titles = [' original image' , 'canny image']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
