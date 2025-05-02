import cv2

img = cv2.imread('tower.jpg')
cv2.imshow('Edges', cv2.Canny(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 50, 150))

cv2.waitKey()
cv2.destroyAllWindows()
