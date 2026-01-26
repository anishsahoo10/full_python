import cv2

# Load Haar Cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

# Check if cascades loaded properly
if face_cascade.empty() or smile_cascade.empty():
    print("❌ Error loading cascade files")
    exit()

# Start webcam
cap = cv2.VideoCapture(0)

print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:
        # Draw face box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

        # Detect smile inside face
        # Detect smile (ONLY lower half of face)
        smiles = smile_cascade.detectMultiScale(
            face_gray[int(h / 2):h, :],
            scaleFactor=1.8,
            minNeighbors=25,
            minSize=(40, 40)
        )

        # Smile confirmation logic
        if len(smiles) > 0:
            cv2.putText(
                frame,
                "REAL SMILE 😁",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

            for (sx, sy, sw, sh) in smiles:
                cv2.rectangle(
                    face_color,
                    (sx, int(h / 2) + sy),
                    (sx + sw, int(h / 2) + sy + sh),
                    (0, 255, 0),
                    2
                )

    cv2.imshow("Smile Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
