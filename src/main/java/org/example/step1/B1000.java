package org.example.step1;

import java.util.Scanner;

public class B1000 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();
        scanner.close();
        System.out.print(a+b);
    }
}
