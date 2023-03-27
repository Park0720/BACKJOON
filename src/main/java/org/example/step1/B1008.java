package org.example;

import java.util.Scanner;

public class B1008 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double a, b;
        a = scanner.nextDouble();
        b = scanner.nextDouble();

        System.out.print(a/b);

        scanner.close();
    }
}
