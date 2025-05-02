import cv2  

# Load Haar cascade for eye detection  
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')  

# Start webcam  
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  

while True:  
    ret, frame = cap.read()  
    if not ret:  
        break  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  

    # Detect eyes  
    eyes = eye_cascade.detectMultiScale(gray, 1.1, 10)  
    for (x, y, w, h) in eyes:  
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  

    cv2.imshow("Eye Detection", frame)  
    if cv2.waitKey(1) == ord('q'):  # Press 'q' to exit  
        break  

cap.release()  
cv2.destroyAllWindows()
