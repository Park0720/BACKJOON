package org.example;

import java.util.Scanner;

public class B1001 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();

        System.out.print(a-b);

        scanner.close();
    }
}
