import cv2
import numpy

image_gray = cv2.imread('grayscale_labka.jpg')

z = image_gray.reshape((-1, 3))

z = numpy.float32(z)
crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 6
ret, label, center = cv2.kmeans(z, k, None, crit, 10, cv2.KMEANS_RANDOM_CENTERS)

center = numpy.uint8(center)
res = center[label.flatten()]
res2 = res.reshape(image_gray.shape)

cv2.imshow('res2', res2)
cv2.imwrite('grayscale_quantise_labka.jpg', res2)
key = cv2.waitKey(0) & 0xFF

cv2.waitKey(0)
cv2.destroyAllWindows()
