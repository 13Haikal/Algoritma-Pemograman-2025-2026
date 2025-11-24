import java.util.Scanner;

public class kasir {
    public static void main(String[]args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan nama barang: ");
        String nama = scanner.nextLine();

        System.out.print("Masukkan harga barang: ");
        double harga = scanner.nextDouble();

        System.out.print("Masukkan jumlah beli: ");
        int jumlah = scanner.nextInt();

        double total = harga * jumlah;

        double diskon = 0;

        if (total > 47000) {
            diskon = total * 0.07;
        }

        double total_bayar = total-diskon;

        System.out.println("\n==========STRUK PEMBELIAN==========");
        System.out.println("Nama Barang : " + nama);
        System.out.printf("Harga satuan : %.2f%n", harga);
        System.out.println("Jumlah Beli : " + jumlah);
        System.out.printf("Total Harga : %.2f%n", total);
        System.out.printf("Diskon : %.2f%n", diskon);
        System.out.printf("Total Bayar : %.2f%n", total_bayar);
        System.out.println("====================");
    }
}
