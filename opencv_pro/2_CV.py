#WAP of Converting an Image to Grayscale

import cv2

image = cv2.imread('tower.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
