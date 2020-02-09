import random

import cv2
import numpy

image = cv2.imread('labka.jpg')

new_image = numpy.zeros(image.shape, numpy.uint8)
prob = 0.2
edge = 1 - prob

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        rand = random.random()
        if rand < prob:
            new_image[i][j] = 0
        elif rand > edge:
            new_image[i][j] = 255	
        else:
            new_image[i][j] = image[i][j]

cv2.imshow('original', image)
cv2.imshow('salt and pepper noise', new_image)

cv2.imwrite('salt_n_pepper_labka.jpg', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()