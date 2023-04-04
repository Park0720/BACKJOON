package org.example.step3;
import java.util.Scanner;
public class B2739 {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        for(int i=1;i<=9;i++){
            System.out.println(a + " * " + i + " = " + a*i );
        }
    }
}
