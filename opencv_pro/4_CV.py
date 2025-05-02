#WAP of Detecting and tracking objects using Haar cascades from images

import cv2

image = cv2.imread(r'F:\subject\kansa\ML\Unit_5\group.jpeg')


face_cascade = cv2.CascadeClassifier(r"C:\haarcascades\haarcascade_frontalface_default.xml")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05,minNeighbors=3)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0,0), 2)

cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
