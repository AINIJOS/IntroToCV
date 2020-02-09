import cv2
import numpy 

image = cv2.imread('labka.jpg')

gauss = numpy.zeros(image.shape, numpy.uint8)
mean = (0, 0, 0)
sigma = (50, 50, 50)
cv2.randn(gauss, mean, sigma)

new_image = cv2.add(image, gauss)


cv2.imshow('original', image)
cv2.imshow('gaussian noise', new_image)

cv2.imwrite('gaussian_noise_labka.jpg', new_image)

key = cv2.waitKey(0) & 0xFF

cv2.waitKey(0)
cv2.destroyAllWindows()