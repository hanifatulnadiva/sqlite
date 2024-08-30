import tkinter as tk  # Untuk membuat tampilan aplikasi
from tkinter import *
import sqlite3  # Untuk berinteraksi dengan database SQLite

# Membuat jendela utama aplikasi
jendela = tk.Tk()
jendela.configure(bg="#649e8a")
jendela.title("Aplikasi Prodi Pilihan")
jendela.geometry("400x400")

# Fungsi untuk menyiapkan database
def setup_database():
    conn = sqlite3.connect('prodi.db')  # Membuka atau membuat database
    c = conn.cursor()  # Membuat kursor untuk menjalankan perintah SQL
    c.execute('''
    CREATE TABLE IF NOT EXISTS prediksi_prodi (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        nilai_biologi REAL NOT NULL,
        nilai_fisika REAL NOT NULL,
        nilai_inggris REAL NOT NULL,
        hasil TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Fungsi untuk menyimpan data ke dalam database
def simpan_ke_database(nama, biologi, fisika, inggris, hasil):
    """Menyimpan data ke database"""
    with sqlite3.connect('prodi.db') as conn:
        c = conn.cursor()
        c.execute('''
        INSERT INTO prediksi_prodi (nama, nilai_biologi, nilai_fisika, nilai_inggris, hasil)
        VALUES (?, ?, ?, ?, ?)
        ''', (nama, biologi, fisika, inggris, hasil))
        conn.commit()

# Memanggil fungsi untuk menyiapkan database
setup_database()

# Variabel untuk menyimpan input
biologi = tk.DoubleVar()
fisika = tk.DoubleVar()
inggris = tk.DoubleVar()
nama = tk.StringVar()

# Fungsi untuk memprediksi jurusan berdasarkan nilai yang dimasukkan
def prediksi():
    biologi_value = biologi.get()
    fisika_value = fisika.get()
    inggris_value = inggris.get()
    nama_value = nama.get()

    if biologi_value < 75 or fisika_value < 75 or inggris_value < 75:
        hasil = 'Tidak Lulus Seleksi'
    elif biologi_value > fisika_value and biologi_value > inggris_value:
        hasil = 'Kedokteran'
    elif fisika_value > biologi_value and fisika_value > inggris_value:
        hasil = 'Teknik'
    elif inggris_value > fisika_value and inggris_value > biologi_value:
        hasil = 'Bahasa'
    else:
        hasil = 'Tidak dapat diprediksi'
        
    simpan_ke_database(nama_value, int(biologi_value), int(fisika_value), int(inggris_value), hasil)
    tombol_hasil.config(text=f"Hasil: {hasil}")


# Membuat elemen GUI
nama_label = tk.Label(jendela, text="Nama Siswa", font=("Arial", 12), fg="#FFFFFF", bg="#649e8a")
nama_label.place(relx=0.5, rely=0.25, anchor="center")
nama_entry = tk.Entry(jendela, textvariable=nama, font=("Arial", 12), width=30, fg="#000000")
nama_entry.place(relx=0.5, rely=0.30, anchor="center")

biologi_label = tk.Label(jendela, text="Nilai Biologi:", font=("Arial", 12), fg="#FFFFFF", bg="#649e8a")
biologi_label.place(relx=0.5, rely=0.40, anchor="center")
biologi_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFF0CE", textvariable=biologi)
biologi_entry.place(relx=0.5, rely=0.45, anchor="center")

fisika_label = tk.Label(jendela, text="Nilai Fisika:", font=("Arial", 12), fg="#FFFFFF", bg="#649e8a")
fisika_label.place(relx=0.5, rely=0.55, anchor="center")
fisika_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFF0CE", textvariable=fisika)
fisika_entry.place(relx=0.5, rely=0.60, anchor="center")

bahasa_inggris_label = tk.Label(jendela, text="Nilai Bahasa Inggris:", font=("Arial", 12), fg="#FFFFFF", bg="#649e8a")
bahasa_inggris_label.place(relx=0.5, rely=0.70, anchor="center")
bahasa_inggris_entry = tk.Entry(jendela, font=("Arial", 12), width=30, fg="#000000", bg="#FFF0CE", textvariable=inggris)
bahasa_inggris_entry.place(relx=0.5, rely=0.75, anchor="center")

# Tombol untuk memprediksi hasil
prediksi_button = tk.Button(jendela, text="Prediksi", command=prediksi, font=("Arial", 12), bg="#0C356A", fg="#FFFFFF")
prediksi_button.place(relx=0.5, rely=0.83, anchor="center")

# Label untuk menampilkan hasil prediksi
tombol_hasil = tk.Label(jendela, text="", font=("Arial", 12), fg="#FFFFFF", bg="#649e8a")
tombol_hasil.place(relx=0.5, rely=0.90, anchor="center")

# Menjalankan aplikasi
jendela.mainloop()
