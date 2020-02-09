import cv2

image = cv2.imread('labka.jpg')

yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
# cmy = cv2.cvtColor(image, cv2.COLOR_BGR2CMY)

cv2.imshow('original', image)
cv2.imshow('YUV', yuv)
cv2.imshow('HLS', hls)
# cv2.imshow('CMY', cmy)

cv2.imwrite('YUV_labka.jpg', yuv)
cv2.imwrite('HLS_labka.jpg', hls)

k = cv2.waitKey(0) & 0xFF

cv2.waitKey(0)
cv2.destroyAllWindows()