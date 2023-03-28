package org.example.step1;

import java.util.Scanner;

public class B11382 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Long a, b, c;
        a = scanner.nextLong();
        b = scanner.nextLong();
        c = scanner.nextLong();

        System.out.println(a+b+c);

        scanner.close();
    }
}
