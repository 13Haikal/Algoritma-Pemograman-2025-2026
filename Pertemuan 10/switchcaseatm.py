import sys

def formatRupiah(n):
   
    s = str(n)
    n_len = len(s)
    res = ""
    counter = 0


    for i in range(n_len - 1, -1, -1):
        res = s[i] + res
        counter += 1
        if counter % 3 == 0 and i != 0:
            res = "." + res
    return res

def main():
    saldo = 0
    
    nama = input("Masukkan nama: ")

    valid = input("Apakah nama sudah benar? (TRUE/FALSE): ")
    if valid.upper() != "TRUE":
        print("Nama tidak valid. Silakan ulangi.")
        sys.exit(0) 

    nim_str = input("Masukkan NIM: ")

    saldo = 2510147

    print(f"\nSelamat datang, {nama}")
    print(f"Saldo Anda saat ini: Rp {formatRupiah(saldo)}\n")

    print("======== MENU ATM ========")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Transfer")
    print("5. Keluar")
    
    try:
        pilihan = int(input("Pilih menu (1-5): "))
    except ValueError:
        print("Pilihan tidak valid.")
        return

    nominal = 0

    if pilihan == 1:
        print(f"\nSaldo Anda saat ini adalah: Rp {formatRupiah(saldo)}")
    elif pilihan == 2:
        try:
            nominal = int(input("Masukkan nominal Tarik Tunai: Rp "))
        except ValueError:
            print("Input nominal tidak valid.")
            return

        if nominal > saldo:
            print("Saldo tidak mencukupi.")
        else:
            saldo -= nominal
            print(f"Penarikan berhasil. Saldo sisa: Rp {formatRupiah(saldo)}")
    elif pilihan == 3:
        try:
            nominal = int(input("Masukkan nominal Setor Tunai: Rp "))
        except ValueError:
            print("Input nominal tidak valid.")
            return
            
        saldo += nominal
        print(f"Penyetoran berhasil. Saldo saat ini: Rp {formatRupiah(saldo)}")
    elif pilihan == 4:
        try:
            nominal = int(input("Masukkan nominal Transfer: Rp "))
        except ValueError:
            print("Input nominal tidak valid.")
            return

        if nominal > saldo:
            print("Saldo tidak mencukupi untuk transfer.")
        else:
            saldo -= nominal
            print(f"Transfer Rp {formatRupiah(nominal)} berhasil. Saldo sisa: Rp {formatRupiah(saldo)}")
    elif pilihan == 5:
        print("Terima kasih, silakan ambil kartu Anda.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()