package org.example.step3;

import java.util.Scanner;

public class B11021 {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i = 1; i <= T; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            System.out.println("Case #"+i+": "+ (a+b));
        }
    }
}
