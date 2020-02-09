import cv2

image1 = cv2.imread('gaussian_noise_labka.jpg')
image2 = cv2.imread('salt_n_pepper_labka.jpg')
blur1 = cv2.blur(image1, (20, 20))
blur2 = cv2.blur(image2, (20, 20))

cv2.imshow('blurred gaussian', blur1)
cv2.imshow('blurred salt and pepper', blur2)

cv2.imwrite('blur_one_labka.jpg', blur1)
cv2.imwrite('blur_two_labka.jpg', blur2)


cv2.waitKey(0)
cv2.destroyAllWindows()