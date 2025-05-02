#WAP of mouth detection
import cv2

# Load Haar cascade for mouth detection
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')

# Start webcam
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect mouths
    mouths = mouth_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    # Draw rectangles around detected mouths
    for (x, y, w, h) in mouths:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle for mouth

    cv2.imshow("Mouth Detection", frame)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()
