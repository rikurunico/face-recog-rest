# **Face Recognition API**

Aplikasi ini adalah REST API sederhana untuk **registrasi wajah** dan **pengenalan wajah** menggunakan library `face_recognition`. Aplikasi ini memungkinkan pengguna untuk mengunggah gambar wajah, mendaftarkannya, dan kemudian mengenali wajah tersebut dari gambar baru.

---

## **Fitur**
1. **Registrasi Wajah**:
   - Unggah gambar wajah.
   - Deteksi dan crop wajah.
   - Simpan gambar wajah yang di-crop dan encoding wajah.

2. **Pengenalan Wajah**:
   - Unggah gambar baru.
   - Deteksi wajah dan bandingkan dengan wajah yang sudah terdaftar.
   - Tampilkan nama wajah yang dikenali beserta confidence level.

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

---

## **Instalasi**
1. Clone repository ini:
   ```bash
   git clone https://github.com/username/face-recognition-api.git
   cd face-recognition-api
   ```

2. Buat virtual environment (opsional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Jalankan aplikasi:
   ```bash
   python app.py
   ```

   Aplikasi akan berjalan di `http://127.0.0.1:5000`.

---

## **Struktur Proyek**
```
/face-recognition-api
│
├── /cropped_faces          # Folder untuk menyimpan gambar wajah yang di-crop
├── face_encodings.pkl      # File untuk menyimpan encoding wajah
├── app.py                  # File utama aplikasi
├── requirements.txt        # Dependencies
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
1. Siapkan gambar wajah (misal: `training.jpg`).
2. Gunakan Postman atau curl untuk mengunggah gambar:
   ```bash
   curl -X POST -F "file=@training.jpg" http://127.0.0.1:5000/register
   ```
3. Jika berhasil, response akan menampilkan nama file yang disimpan:
   ```json
   {
     "message": "Face registered successfully",
     "filename": "training.jpg"
   }
   ```
4. Gambar wajah yang di-crop akan disimpan di folder `cropped_faces`.

---

### **2. Pengenalan Wajah**
1. Siapkan gambar baru (misal: `testing.jpg`).
2. Gunakan Postman atau curl untuk mengunggah gambar:
   ```bash
   curl -X POST -F "file=@testing.jpg" http://127.0.0.1:5000/recognize
   ```
3. Jika wajah dikenali, response akan menampilkan nama dan confidence level:
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
1. Import Collection Postman dari file `Face Recognition API.postman_collection.json`.
2. Jalankan request **Register Face** untuk mendaftarkan wajah.
3. Jalankan request **Recognize Face** untuk mengenali wajah.

---

## **Contoh Gambar**
- **Gambar untuk Registrasi**: `training.jpg`
- **Gambar untuk Pengenalan**: `testing.jpg`

Pastikan gambar memiliki wajah yang jelas dan menghadap ke depan.

---

## **Catatan**
- Aplikasi ini hanya untuk tujuan pembelajaran dan pengembangan.
- Untuk penggunaan produksi, tambahkan fitur keamanan seperti autentikasi dan validasi input.
- Pastikan library `face_recognition` terinstall dengan benar. Jika mengalami masalah, ikuti panduan instalasi di [dokumentasi resmi](https://github.com/ageitgey/face_recognition).

---

## **Lisensi**
Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---

Dengan README ini, Anda dapat dengan mudah memahami, menginstal, dan menggunakan aplikasi Face Recognition API. Selamat mencoba! 🚀