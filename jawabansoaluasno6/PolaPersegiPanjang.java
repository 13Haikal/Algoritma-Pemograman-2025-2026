package jawabansoaluasno6;
public class PolaPersegiPanjang {
    public static void main(String[] args) {
        int tinggi = 3; // Jumlah baris
        int lebar = 8;  // Jumlah kolom

        for (int i = 0; i < tinggi; i++) {
            for (int j = 0; j < lebar; j++) {
                System.out.print("* ");
            }
            System.out.println(); // Pindah baris
        }
    }
}
