import cv2

# Load the image
image = cv2.imread(r'D:\python_prog\python\p1.jpeg')

# Load the pre-trained face detection model (use the correct XML file)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=10)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
