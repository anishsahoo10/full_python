import cv2

# Load cascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")

if face_cascade.empty() or smile_cascade.empty():
    print("❌ Error loading cascade files")
    exit()

cap = cv2.VideoCapture(0)

smile_frames = 0
smile_count = 0
smiling = False  # to avoid double count

print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, 1.2, 5, minSize=(100, 100)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

        # Detect smile only in lower half of face
        smiles = smile_cascade.detectMultiScale(
            face_gray[int(h/2):h, :],
            scaleFactor=1.8,
            minNeighbors=25,
            minSize=(40, 40)
        )

        if len(smiles) > 0:
            smile_frames += 1
        else:
            smile_frames = 0
            smiling = False

        # Count smile only once
        if smile_frames > 5 and not smiling:
            smile_count += 1
            smiling = True

        # Display smile text
        if smiling:
            cv2.putText(
                frame,
                "SMILING 😁",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(
                face_color,
                (sx, int(h/2) + sy),
                (sx + sw, int(h/2) + sy + sh),
                (0, 255, 0),
                2
            )

    # Display smile count
    cv2.putText(
        frame,
        f"Smile Count: {smile_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("Smile Counter", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
