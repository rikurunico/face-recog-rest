import os
import uuid
import face_recognition
from flask import Flask, request, jsonify
import cv2
import numpy as np
import pickle

app = Flask(__name__)

# Direktori untuk menyimpan gambar wajah yang di-crop
CROPPED_FACES_DIR = "cropped_faces"
os.makedirs(CROPPED_FACES_DIR, exist_ok=True)

# File untuk menyimpan encoding wajah
ENCODINGS_FILE = "face_encodings.pkl"

# Load encoding wajah yang sudah ada (jika file ada)
if os.path.exists(ENCODINGS_FILE):
    with open(ENCODINGS_FILE, "rb") as f:
        known_face_encodings = pickle.load(f)
else:
    known_face_encodings = {}

# Fungsi untuk crop wajah dan simpan
def crop_and_save_face(image, filename):
    # Deteksi wajah
    face_locations = face_recognition.face_locations(image)
    
    if len(face_locations) == 0:
        return None  # Tidak ada wajah yang terdeteksi
    
    # Ambil bounding box wajah pertama
    top, right, bottom, left = face_locations[0]
    
    # Crop wajah
    face_image = image[top:bottom, left:right]
    
    # Simpan gambar wajah yang di-crop
    face_filename = os.path.join(CROPPED_FACES_DIR, filename)
    cv2.imwrite(face_filename, cv2.cvtColor(face_image, cv2.COLOR_RGB2BGR))
    
    # Hitung encoding wajah
    face_encoding = face_recognition.face_encodings(image, [face_locations[0]])[0]
    
    return face_encoding

# Endpoint untuk upload gambar dan registrasi wajah
@app.route("/register", methods=["POST"])
def register_face():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    # Baca gambar
    image = face_recognition.load_image_file(file)
    
    # Crop wajah dan simpan
    filename = file.filename  # Gunakan nama file asli sebagai label
    face_encoding = crop_and_save_face(image, filename)
    
    if face_encoding is None:
        return jsonify({"error": "No face detected"}), 400
    
    # Simpan encoding wajah
    known_face_encodings[filename] = face_encoding
    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(known_face_encodings, f)
    
    return jsonify({"message": "Face registered successfully", "filename": filename}), 200

# Endpoint untuk face recognition
@app.route("/recognize", methods=["POST"])
def recognize_face():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400
    
    # Baca gambar
    image = face_recognition.load_image_file(file)
    
    # Deteksi wajah
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    
    if len(face_encodings) == 0:
        return jsonify({"error": "No face detected"}), 400
    
    # Bandingkan dengan wajah yang sudah terdaftar
    recognized_faces = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(list(known_face_encodings.values()), face_encoding)
        face_distances = face_recognition.face_distance(list(known_face_encodings.values()), face_encoding)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            recognized_name = list(known_face_encodings.keys())[best_match_index]
            confidence = (1 - face_distances[best_match_index]) * 100
            recognized_faces.append({"name": recognized_name, "confidence": f"{confidence:.2f}%"})
        else:
            recognized_faces.append({"name": "Unknown", "confidence": "0%"})
    
    return jsonify({"recognized_faces": recognized_faces}), 200

# Jalankan aplikasi
if __name__ == "__main__":
    app.run(debug=True)