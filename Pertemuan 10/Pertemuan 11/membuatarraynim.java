import java.util.Scanner;
import java.util.Arrays;

public class membuatarraynim {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

       
        System.out.print("Masukkan NIM:");
        String nimStr = scanner.nextLine();
        scanner.close();

        
        int[] digit = new int[nimStr.length()];
        for (int i = 0; i < nimStr.length(); i++) {
           
            digit[i] = Character.getNumericValue(nimStr.charAt(i)); 
        }

        System.out.println("Digit Array: " + Arrays.toString(digit));

    
        int total = 0;
        for (int d : digit) {
            total += d;
        }

        
        int maks = digit[0];
        int minim = digit[0];

        for (int d : digit) {
            if (d > maks) {
                maks = d;
            }
            if (d < minim) {
                minim = d;
            }
        }

       
        double rata = (double) total / digit.length;

       
        int[] rev = new int[digit.length];
        for (int i = 0; i < digit.length; i++) {
            rev[i] = digit[digit.length - 1 - i];
        }

        
        System.out.println("Total: " + total);
        System.out.println("Maksimum: " + maks);
        System.out.println("Minimum: " + minim);
        System.out.println("Reverse Array: " + Arrays.toString(rev));
    }
}