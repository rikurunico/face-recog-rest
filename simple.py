import face_recognition
import cv2
import numpy as np

# Hardcode gambar untuk registrasi dan testing
register_image = "training.jpg"  # Gambar pendaftaran
checkin_image = "testing3.jpg"  # Gambar check-in

# Load gambar registrasi
register_image = face_recognition.load_image_file(register_image)
register_face_encoding = face_recognition.face_encodings(register_image)[0]

# Load gambar check-in
checkin_image = face_recognition.load_image_file(checkin_image)
checkin_face_locations = face_recognition.face_locations(checkin_image)
checkin_face_encodings = face_recognition.face_encodings(
    checkin_image, checkin_face_locations
)

# Konversi ke format BGR untuk OpenCV
checkin_image_display = cv2.cvtColor(checkin_image, cv2.COLOR_RGB2BGR)

# Bandingkan wajah
for (top, right, bottom, left), checkin_face_encoding in zip(
    checkin_face_locations, checkin_face_encodings
):
    # Hitung jarak (distance) antara wajah yang didaftarkan dan wajah yang dideteksi
    face_distance = face_recognition.face_distance(
        [register_face_encoding], checkin_face_encoding
    )[0]

    # Hitung confidence level (tingkat kepercayaan) dalam persen
    confidence = (1 - face_distance) * 100
    confidence_text = f"{confidence:.2f}%"

    # Tentukan apakah wajah cocok
    matches = face_recognition.compare_faces(
        [register_face_encoding], checkin_face_encoding, tolerance=0.6
    )
    name = "Unknown"

    if matches[0]:
        name = "Registered Person"

    # Gambar kotak dan nama di sekitar wajah
    cv2.rectangle(checkin_image_display, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText(
        checkin_image_display,
        name,
        (left + 6, bottom - 6),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.0,
        (255, 255, 255),
        1,
    )

    # Tampilkan confidence level
    cv2.putText(
        checkin_image_display,
        confidence_text,
        (left + 6, bottom + 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        1,
    )

# Tampilkan hasil
cv2.imshow("Face Recognition Result", checkin_image_display)
cv2.waitKey(0)
cv2.destroyAllWindows()
