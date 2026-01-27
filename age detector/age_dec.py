import cv2
import numpy as np

# Age labels used by the model
AGE_BUCKETS = [
    "(0-2)", "(4-6)", "(8-12)", "(15-20)",
    "(25-32)", "(38-43)", "(48-53)", "(60-100)"
]

# Load FACE detection model (Caffe)
face_net = cv2.dnn.readNetFromCaffe(
    "deploy.prototxt",
    "res10_300x300_ssd_iter_140000.caffemodel"
)

# Load AGE detection model (Caffe)
age_net = cv2.dnn.readNetFromCaffe(
    "age_deploy.prototxt",
    "age_net.caffemodel"
)

# Safety check
if face_net.empty():
    print("❌ Face model not loaded")
    exit()

if age_net.empty():
    print("❌ Age model not loaded")
    exit()

print("✅ Models loaded successfully")
print("Press Q to quit")

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    # Prepare face detection blob
    face_blob = cv2.dnn.blobFromImage(
        frame,
        1.0,
        (300, 300),
        (104.0, 177.0, 123.0)
    )

    face_net.setInput(face_blob)
    detections = face_net.forward()

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]

        if confidence > 0.6:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            x1, y1, x2, y2 = box.astype(int)

            # Clamp values to frame
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)

            face = frame[y1:y2, x1:x2]
            if face.size == 0:
                continue

            # Prepare age detection blob
            age_blob = cv2.dnn.blobFromImage(
                face,
                1.0,
                (227, 227),
                (78.426, 87.768, 114.895),
                swapRB=False
            )

            age_net.setInput(age_blob)
            age_preds = age_net.forward()
            age = AGE_BUCKETS[age_preds[0].argmax()]

            # Draw results
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                f"Age: {age}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 255, 0),
                2
            )

    cv2.imshow("Age Detector", frame)

    # Quit on Q or window close
    if cv2.waitKey(1) & 0xFF == ord('q') or \
       cv2.getWindowProperty("Age Detector", cv2.WND_PROP_VISIBLE) < 1:
        break

cap.release()
cv2.destroyAllWindows()
