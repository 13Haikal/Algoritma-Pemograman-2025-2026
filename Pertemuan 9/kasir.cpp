#include <iostream>


using namespace std;

int main () {
    string nama;
    double harga;
    int jumlah;
    double total, diskon, total_bayar;

    cout << "Masukkan nama barang: ";
    getline(cin, nama);

    cout << "Masukkan harga barang: ";
    cin >> harga;

    cout << "Masukkan jumlah beli: ";
    cin >> jumlah;

    total = harga*jumlah;
    diskon = 0.0;
    
    if (total > 47000) {
        diskon = total*0.07;
    }

    total_bayar = total-diskon;

    cout << "====STRUK PEMBELIAN====\n";
    cout << "Nama Barang : " << nama << endl;
    cout << "Harga Satuan : " << harga << endl;
    cout << "Jumlah Beli : " <<  jumlah << endl;
    cout << "Total Harga : " << total << endl;
    cout << "Diskon : " << diskon << endl;
    cout <<  "Total Bayar : " << total_bayar << endl;
    cout << "=======================\n";

    return 0;
}

