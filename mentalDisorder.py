# Import library
import pandas as pd  # Untuk manipulasi data
from sklearn.tree import DecisionTreeClassifier  # Untuk model klasifikasi

# Ini contoh data gangguan mental
data = {
    'Mood': ['Sedih', 'Sedih', 'Senang', 'Senang', 'Cemas', 'Cemas', 'Marah', 'Marah'],
    'Tidur': ['Tidak Cukup', 'Cukup', 'Cukup', 'Tidak Cukup', 'Tidak Cukup', 'Cukup', 'Cukup', 'Tidak Cukup'],
    'Konsentrasi': ['Rendah', 'Rendah', 'Tinggi', 'Tinggi', 'Rendah', 'Tinggi', 'Rendah', 'Tinggi'],
    'Gangguan_Mental': ['Depresi', 'Depresi', 'Bipolar', 'Bipolar', 'Anxiety', 'Anxiety', 'Bipolar', 'Depresi']
}

# Mengubah data menjadi DataFrame
df = pd.DataFrame(data)

# Mengubah data kategorikal menjadi numerik
df['Mood'] = df['Mood'].map({'Sedih': 0, 'Senang': 1, 'Cemas': 2, 'Marah': 3})
df['Tidur'] = df['Tidur'].map({'Tidak Cukup': 0, 'Cukup': 1})
df['Konsentrasi'] = df['Konsentrasi'].map({'Rendah': 0, 'Tinggi': 1})
df['Gangguan_Mental'] = df['Gangguan_Mental'].map({'Depresi': 0, 'Bipolar': 1, 'Anxiety': 2})

# Memisahkan fitur dan target
X = df[['Mood', 'Tidur', 'Konsentrasi']]  # Fitur
y = df['Gangguan_Mental']  # Target

# Membuat model Decision Tree
model = DecisionTreeClassifier()

# Melatih model dengan data
model.fit(X, y)

# Fungsi untuk prediksi gangguan mental
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

# Input dari user
print("Selamat datang di Program Klasifikasi Gangguan Mental")
mood = input("Masukkan mood Anda (Sedih/Senang/Cemas/Marah): ")
tidur = input("Masukkan kualitas tidur Anda (Cukup/Tidak Cukup): ")
konsentrasi = input("Masukkan tingkat konsentrasi Anda (Rendah/Tinggi): ")

# Melakukan prediksi
hasil = prediksi_gangguan_mental(mood, tidur, konsentrasi)
print(f"Hasil prediksi: {hasil}")