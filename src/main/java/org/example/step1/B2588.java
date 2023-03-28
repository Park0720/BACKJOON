package org.example.step1;
import java.util.Scanner;
public class B2588 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();
        String[] bList = (b+"").split("");
        for(int i = bList.length-1; i>=0 ; i--) {
            System.out.println(a * Integer.parseInt(bList[i]));
        }
        System.out.println(a*b);
        scanner.close();
    }
}
