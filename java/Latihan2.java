import java.util.Scanner;
public class Latihan2 {
    public static void main(String[]args) {
        final double PI= 3.14159;
        Scanner sc= new Scanner(System.in);
        System.out.print("Masukan jari-jari: ");
        double r= sc.nextDouble();
        double luas= PI*r*r;
        System.out.println("Luas lingkaran="+ luas);
    }
}

