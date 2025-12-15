# Variabel global untuk menyimpan data Buku
buku = []

# fungsi untuk menampilkan semua data
def show_data():
    """Menampilkan semua judul buku beserta ID-nya."""
    print('--- DAFTAR BUKU ---')
    if len(buku) == 0:
        print('BELUM ADA DATA')
    else:
        # Menggunakan enumerate untuk mendapatkan indeks dan nilai secara bersamaan
        for indeks, judul in enumerate(buku):
            # ID dimulai dari 0
            print(f'[{indeks}] {judul}')
    print('-------------------')

# fungsi untuk menambah data
def insert_data():
    """Menambahkan buku baru ke dalam daftar."""
    # Menggunakan input() untuk Python 3
    buku_baru = input('Judul Buku: ')
    buku.append(buku_baru)
    print(f'Buku "{buku_baru}" telah ditambahkan.')

# fungsi untuk edit data
def edit_data():
    """Mengubah judul buku berdasarkan ID."""
    show_data()
    if len(buku) == 0:
        return # Keluar jika tidak ada data

    try:
        # Menggunakan input() dan konversi ke integer
        indeks = int(input('Inputkan ID buku yang akan diubah: '))
    except ValueError:
        print('Input ID harus berupa angka.')
        return

    # Pengecekan ID harus lebih kecil dari panjang daftar dan tidak negatif
    if 0 <= indeks < len(buku):
        judul_lama = buku[indeks]
        judul_baru = input(f'Masukkan judul baru untuk "{judul_lama}": ')
        buku[indeks] = judul_baru
        print(f'Judul buku ID {indeks} berhasil diubah menjadi "{judul_baru}".')
    else:
        print('ID salah atau tidak ditemukan.')

# fungsi untuk menghapus data
def delete_data():
    """Menghapus buku berdasarkan ID."""
    show_data()
    if len(buku) == 0:
        return # Keluar jika tidak ada data

    try:
        # Menggunakan input() dan konversi ke integer
        indeks = int(input('Inputkan ID buku yang akan dihapus: '))
    except ValueError:
        print('Input ID harus berupa angka.')
        return

    # Pengecekan ID
    if 0 <= indeks < len(buku):
        # Menggunakan pop() untuk menghapus berdasarkan indeks dan mendapatkan nilai yang dihapus
        judul_terhapus = buku.pop(indeks)
        print(f'Buku ID {indeks}: "{judul_terhapus}" telah dihapus.')
    else:
        print('ID salah atau tidak ditemukan.')

# fungsi untuk menampilkan menu
def show_menu():
    """Menampilkan menu dan memproses pilihan pengguna."""
    print('\n')
    print('----------- MENU MANAJEMEN BUKU ----------')
    print('[1] Tampilkan Data')
    print('[2] Tambah Data')
    print('[3] Edit Data')
    print('[4] Hapus Data')
    print('[5] Keluar')
    print('------------------------------------------')

    # Menggunakan try-except untuk menangani input yang bukan angka
    try:
        menu = int(input('PILIH MENU> '))
        print('\n')

        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            # Menggunakan return False untuk menghentikan loop utama
            print('Program selesai. Sampai jumpa!')
            return False
        else:
            print('Pilihan menu tidak valid!')
    except ValueError:
        print('Input menu harus berupa angka (1-5).')

    return True # Mengembalikan True untuk melanjutkan loop

# Bagian utama program
if __name__ == '__main__':
    # Loop akan berjalan selama show_menu mengembalikan True
    while show_menu():
        pass