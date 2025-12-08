# SOAL - Membuat Array Dari Digit NIM

# 1. Input NIM
nim = input("Masukkan NIM: ")

# 2. Ubah string menjadi array digit (integer)
# Menggunakan List Comprehension untuk efisiensi
digit = [int(c) for c in nim]

# --- Tugas Khusus: Hitung Menggunakan Loop ---

# #Total
total = 0
for d in digit:
    total += d

# #Maks
# Inisialisasi dengan elemen pertama
maks = digit[0]
for d in digit:
    if d > maks:
        maks = d

# #Min
# Inisialisasi dengan elemen pertama
minim = digit[0]
for d in digit:
    if d < minim:
        minim = d

# #Rata
# Pastikan array tidak kosong
if len(digit) > 0:
    rata = total / len(digit)
else:
    rata = 0

# #Reverse array
rev = []
# Loop dari indeks terakhir (len(digit)-1) hingga 0, dengan step -1
for i in range(len(digit)-1, -1, -1):
    # Kesalahan minor pada gambar: di gambar Anda tertulis rev.append(digit[i]), 
    # namun di potongan lain (3fee5bf7-7651-4731-a045-e3e8f6c36e81.jpg) ada typo digit[1]. 
    # Saya perbaiki menjadi yang benar: digit[i]
    rev.append(digit[i]) 
    
# --- Output Hasil ---
print("Digit        :", digit)
print("Total        :", total)
print("Maksimum     :", maks)
print("Minimum      :", minim)
print("Rata-rata    :", rata)
print("Reverse array:", rev)