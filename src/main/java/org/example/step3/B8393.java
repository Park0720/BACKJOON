package org.example.step3;

import java.util.Scanner;

public class B8393 {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        int total = 0;
        for (int i = 1; i <= num; i++) {
            total += i;
        }
        System.out.println(total);
    }
}
