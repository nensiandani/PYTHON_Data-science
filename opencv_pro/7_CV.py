#WAP of nose detection
import cv2

# Load the Haar cascade for nose detection
nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Start webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect noses
    noses = nose_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around detected noses
    for (x, y, w, h) in noses:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle

    cv2.imshow("Nose Detection", frame)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
