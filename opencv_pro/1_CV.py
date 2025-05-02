#conda install -c conda-forge opencv

# WAP of Loading and Displaying an Image

import cv2

# Load an image
image = cv2.imread('tower.jpg')

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()
