public class SoalUAS4 {
    public static void main(String[] args) {
        int n = 5;
        int i, j;

        // Pola bergeser ke kiri
        for (i = 0; i < n; i++) {
            for (int k = n - i; k > 1; k--) {
                System.out.print(" ");
            }
            for (j = 0; j <= i; j++) {
                System.out.print(j);
            }
            System.out.println();
        }
    }
}