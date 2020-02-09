import cv2
  
image = cv2.imread('../labka.jpg')
im_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
cv2.imshow('Gray image', im_gray)
cv2.imwrite('grayscale_labka.jpg', im_gray)
  

key = cv2.waitKey(0) & 0xFF

cv2.waitKey(0)
cv2.destroyAllWindows()