NAMA  : DEFIT BAGUS SAPUTRA
NIM   : H1D023036
SHIFT : G (SEBELUM)/F (SETELAH)


PROGRAM KLASIFIKASI GANGGUAN MENTAL DENGAN DECISION TREE

Program ini digunakan untuk memprediksi kemungkinan gangguan mental yang dialami seseorang berdasarkan tiga faktor utama: 
1. Mood (suasana hati)
2. Kualitas tidur
3. Tingkat konsentrasi
Program menggunakan algoritma Decision Tree Classifier dari scikit-learn untuk melakukan klasifikasi berdasarkan data yang sudah diberikan sebelumnya.

PENJELASAN PROGRAM

1. Struktur Program
Program ini terdiri dari beberapa bagian utama:
A. Import Library
import pandas as pd  # Untuk manipulasi data
from sklearn.tree import DecisionTreeClassifier  # Untuk model klasifikasi

- `pandas` digunakan untuk membuat dan mengolah data dalam bentuk tabel (`DataFrame`).
- `DecisionTreeClassifier` dari `sklearn.tree` digunakan sebagai model pembelajaran mesin untuk klasifikasi.

B. Membuat Dataset
data = {
    'Mood': ['Sedih', 'Sedih', 'Senang', 'Senang', 'Cemas', 'Cemas', 'Marah', 'Marah'],
    'Tidur': ['Tidak Cukup', 'Cukup', 'Cukup', 'Tidak Cukup', 'Tidak Cukup', 'Cukup', 'Cukup', 'Tidak Cukup'],
    'Konsentrasi': ['Rendah', 'Rendah', 'Tinggi', 'Tinggi', 'Rendah', 'Tinggi', 'Rendah', 'Tinggi'],
    'Gangguan_Mental': ['Depresi', 'Depresi', 'Bipolar', 'Bipolar', 'Anxiety', 'Anxiety', 'Bipolar', 'Depresi']
}
Dataset ini berisi informasi tentang mood, tidur, dan konsentrasi, serta label gangguan mental yang mungkin terjadi:

| Mood  | Tidur       | Konsentrasi | Gangguan Mental |
|--------|------------|-------------|----------------|
| Sedih  | Tidak Cukup | Rendah      | Depresi       |
| Sedih  | Cukup      | Rendah      | Depresi       |
| Senang | Cukup      | Tinggi      | Bipolar       |
| Senang | Tidak Cukup | Tinggi      | Bipolar       |
| Cemas  | Tidak Cukup | Rendah      | Anxiety       |
| Cemas  | Cukup      | Tinggi      | Anxiety       |
| Marah  | Cukup      | Rendah      | Bipolar       |
| Marah  | Tidak Cukup | Tinggi      | Depresi       |


C. Konversi Data Kategorikal menjadi Numerik
Karena model *machine learning* hanya dapat bekerja dengan angka, maka data yang berbentuk teks perlu dikonversi ke angka:
df['Mood'] = df['Mood'].map({'Sedih': 0, 'Senang': 1, 'Cemas': 2, 'Marah': 3})
df['Tidur'] = df['Tidur'].map({'Tidak Cukup': 0, 'Cukup': 1})
df['Konsentrasi'] = df['Konsentrasi'].map({'Rendah': 0, 'Tinggi': 1})
df['Gangguan_Mental'] = df['Gangguan_Mental'].map({'Depresi': 0, 'Bipolar': 1, 'Anxiety': 2})

Setelah konversi, tabel menjadi seperti ini:

| Mood | Tidur | Konsentrasi | Gangguan Mental |
|------|-------|------------|----------------|
| 0    | 0     | 0          | 0 (Depresi)   |
| 0    | 1     | 0          | 0 (Depresi)   |
| 1    | 1     | 1          | 1 (Bipolar)   |
| 1    | 0     | 1          | 1 (Bipolar)   |
| 2    | 0     | 0          | 2 (Anxiety)   |
| 2    | 1     | 1          | 2 (Anxiety)   |
| 3    | 1     | 0          | 1 (Bipolar)   |
| 3    | 0     | 1          | 0 (Depresi)   |

D. Memisahkan Data Fitur dan Target
X = df[['Mood', 'Tidur', 'Konsentrasi']]  # Fitur
y = df['Gangguan_Mental']  # Target

- `X` adalah fitur yang digunakan untuk prediksi (Mood, Tidur, Konsentrasi).
- `y` adalah target atau label yang ingin diprediksi (Gangguan Mental).

E. Membuat dan Melatih Mode
model = DecisionTreeClassifier()
model.fit(X, y)
- `DecisionTreeClassifier()` membuat model Decision Tree untuk klasifikasi.
- `model.fit(X, y)` melatih model menggunakan dataset yang diberikan.

F. Fungsi untuk Prediksi
def prediksi_gangguan_mental(mood, tidur, konsentrasi):
    # Mapping input user ke numerik
    mood_map = {'Sedih': 0, 'Senang': 1, 'Cemas': 2, 'Marah': 3}
    tidur_map = {'Tidak Cukup': 0, 'Cukup': 1}
    konsentrasi_map = {'Rendah': 0, 'Tinggi': 1}

    # Konversi input user ke numerik
    mood_num = mood_map.get(mood, -1)  # Default -1 jika input tidak valid
    tidur_num = tidur_map.get(tidur, -1)
    konsentrasi_num = konsentrasi_map.get(konsentrasi, -1)

    # Validasi input
    if mood_num == -1 or tidur_num == -1 or konsentrasi_num == -1:
        return "Input tidak valid!"

    # Prediksi
    prediksi = model.predict([[mood_num, tidur_num, konsentrasi_num]])
    gangguan_map = {0: 'Depresi', 1: 'Bipolar', 2: 'Anxiety'}
    return gangguan_map.get(prediksi[0], "Tidak Diketahui")

- Fungsi ini mengubah input pengguna dari teks menjadi angka.
- Jika input tidak valid, akan menampilkan pesan "Input tidak valid!".
- Menggunakan `model.predict()` untuk membuat prediksi berdasarkan input pengguna.
- Hasil prediksi dikonversi kembali ke nama gangguan mental.

G. Input dari Pengguna

print("Selamat datang di Program Klasifikasi Gangguan Mental")
mood = input("Masukkan mood Anda (Sedih/Senang/Cemas/Marah): ")
tidur = input("Masukkan kualitas tidur Anda (Cukup/Tidak Cukup): ")
konsentrasi = input("Masukkan tingkat konsentrasi Anda (Rendah/Tinggi): ")

- Program meminta pengguna memasukkan mood, kualitas tidur, dan tingkat konsentrasi.

H. Menampilkan Hasil Prediksi
hasil = prediksi_gangguan_mental(mood, tidur, konsentrasi)
print(f"Hasil prediksi: {hasil}")

- Program memanggil fungsi `prediksi_gangguan_mental()` untuk memproses input pengguna.
- Hasil prediksi ditampilkan sebagai nama gangguan mental yang diprediksi.

---

2. Contoh Penggunaan
Input pengguna:
Masukkan mood Anda (Sedih/Senang/Cemas/Marah): Cemas
Masukkan kualitas tidur Anda (Cukup/Tidak Cukup): Cukup
Masukkan tingkat konsentrasi Anda (Rendah/Tinggi): Tinggi

Proses:
- `Cemas` → 2
- `Cukup` → 1
- `Tinggi` → 1
- Model akan memprediksi berdasarkan dataset.

Output:
Hasil prediksi: Anxiety

3. Kesimpulan
- Program ini menggunakan *Decision Tree Classifier* untuk mengklasifikasikan gangguan mental.
- Input pengguna berupa *mood, tidur, dan konsentrasi* dikonversi ke angka sebelum diproses.
- Model dipelajari dari dataset sederhana dan dapat memberikan prediksi yang cukup baik berdasarkan pola yang ditemukan.

