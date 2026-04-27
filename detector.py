import cv2
import random
import time
import os

from database import get_owner, add_violation

# Haar face detector (used for head detection)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

last_violation_time = 0
COOLDOWN = 5  # seconds

os.makedirs("violation_images", exist_ok=True)

def fake_plate():
    plates = ["MH39AJ566", "MH12AB1234", "MH01XY9999"]
    return random.choice(plates)


def is_helmet_present(head_region):
    """
    VERY BASIC helmet detection:
    - checks if region is dark (helmet-like)
    """
    gray = cv2.cvtColor(head_region, cv2.COLOR_BGR2GRAY)
    avg_intensity = gray.mean()

    return avg_intensity < 100  # dark = helmet


def process_frame(frame):
    global last_violation_time

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        plate = fake_plate()
        name = get_owner(plate)

        head = frame[y:y+h, x:x+w]

        helmet = is_helmet_present(head)

        if not helmet:
            current_time = time.time()

            if current_time - last_violation_time > COOLDOWN:
                fine = 500
                reason = "No Helmet"

                add_violation(plate, name, fine, reason)

                filename = f"violation_images/{plate}_{int(time.time())}.jpg"
                cv2.imwrite(filename, frame)

                last_violation_time = current_time

        # Draw UI
        color = (0,255,0) if helmet else (0,0,255)

        cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2)

        status = "Helmet" if helmet else "No Helmet"

        cv2.putText(frame, f"{plate} - {name}",
                    (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        cv2.putText(frame, status,
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return frame