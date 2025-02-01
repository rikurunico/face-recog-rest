# **Face Recognition API**

API ini adalah REST API sederhana untuk **registrasi wajah** dan **pengenalan wajah** menggunakan library `face_recognition`. Aplikasi ini memungkinkan pengguna untuk mendaftarkan wajah dan mengenali wajah dari gambar baru.

---

## **Fitur**

1. **Registrasi Wajah**:
   - Unggah gambar wajah.
   - Deteksi dan crop wajah dari gambar yang diunggah.
   - Simpan gambar wajah yang di-crop dan encoding wajah.

2. **Pengenalan Wajah**:
   - Unggah gambar baru.
   - Deteksi wajah dan bandingkan dengan wajah yang sudah terdaftar.
   - Tampilkan nama wajah yang dikenali beserta tingkat kepercayaan (confidence level).

3. **Penyimpanan Data**:
   - Gambar wajah yang di-crop disimpan dalam folder `cropped_faces`.
   - Encoding wajah disimpan dalam file `face_encodings.pkl`.

---

## **Persyaratan**

1. **Python 3.7+**
2. Library yang diperlukan:
   - `flask`
   - `face_recognition`
   - `opencv-python`
   - `numpy`
   - `pickle`
3. **Docker & Docker Compose**

---

## **Instalasi dengan Docker Compose**

1. **Clone repositori**
   ```bash
   git clone https://github.com/rikurunico/face-recog-rest.git
   cd face-recognition-api
   ```

2. **Bangun dan Jalankan Kontainer**
   ```bash
   docker-compose up -d --build
   ```
   Aplikasi akan berjalan di `http://localhost:5000`.

3. **Menghentikan Kontainer**
   ```bash
   docker-compose down
   ```

---

## **Struktur Proyek**

```plaintext
/face-recognition-api
├── /cropped_faces          # Folder untuk menyimpan gambar wajah yang di-crop
├── face_encodings.pkl      # File untuk menyimpan encoding wajah
├── simple.py               # File untuk testing dan debugging
├── web.py                  # File utama untuk menjalankan aplikasi
├── requirements.txt        # File daftar dependensi
├── docker-compose.yml      # File konfigurasi Docker Compose
├── Dockerfile              # File konfigurasi Docker
├── /postman                # Koleksi Postman untuk testing API
└── README.md               # Dokumentasi
```

---

## **Endpoint API**

### 1. **Registrasi Wajah**
- **URL**: `POST /register`
- **Body**: Form-data dengan key `file` (file gambar).
- **Response**:
  ```json
  {
    "message": "Face registered successfully",
    "filename": "nama_file.jpg"
  }
  ```

### 2. **Pengenalan Wajah**
- **URL**: `POST /recognize`
- **Body**: Form-data dengan key `file` (file gambar).
- **Response**:
  ```json
  {
    "recognized_faces": [
      {
        "name": "nama_file.jpg",
        "confidence": "95.23%"
      }
    ]
  }
  ```

---

## **Cara Menggunakan**

### **1. Registrasi Wajah**
1. Siapkan gambar wajah, misalnya `training.jpg`.
2. Gunakan Postman atau `curl` untuk mengunggah gambar:
   ```bash
   curl -X POST -F "file=@training.jpg" http://localhost:5000/register
   ```
3. Jika berhasil, respons akan menampilkan nama file yang disimpan:
   ```json
   {
     "message": "Face registered successfully",
     "filename": "training.jpg"
   }
   ```
4. Gambar wajah yang di-crop akan disimpan di folder `cropped_faces`.

### **2. Pengenalan Wajah**
1. Siapkan gambar baru, misalnya `testing.jpg`.
2. Gunakan Postman atau `curl` untuk mengunggah gambar:
   ```bash
   curl -X POST -F "file=@testing.jpg" http://localhost:5000/recognize
   ```
3. Jika wajah dikenali, respons akan menampilkan nama dan tingkat kepercayaan:
   ```json
   {
     "recognized_faces": [
       {
         "name": "training.jpg",
         "confidence": "95.23%"
       }
     ]
   }
   ```

---

## **Testing dengan Postman**

1. Import koleksi Postman dari file `postman\Face Recognition API.postman_collection.json`.
2. Jalankan request **Register Face** untuk mendaftarkan wajah.
3. Jalankan request **Recognize Face** untuk mengenali wajah.

---

## **Catatan**

- Aplikasi ini hanya untuk tujuan pembelajaran dan pengembangan.
- Tambahkan fitur keamanan seperti autentikasi dan validasi input untuk penggunaan di produksi.
- Jika mengalami masalah dengan library `face_recognition`, ikuti panduan instalasi di [dokumentasi resmi](https://github.com/ageitgey/face_recognition).

---

## **Lisensi**

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

