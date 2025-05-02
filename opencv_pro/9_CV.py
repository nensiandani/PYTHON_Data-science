#WAP of Pupils
import cv2

# Load Haar cascade for eyes
eye_cascade = cv2.CascadeClassifier(r"C:\haarcascades\haarcascade_eye.xml")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect eyes (pupils are inside the eyes)
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw circles around detected pupils
    for (x, y, w, h) in eyes:
        cx, cy = x + w // 2, y + h // 2  # Center of the detected eye
        radius = min(w, h) // 4
        cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 2)  # Green circle for pupil

    cv2.imshow("Pupil Detection", frame)

    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()