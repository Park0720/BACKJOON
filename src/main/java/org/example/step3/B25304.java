package org.example.step3;

import java.util.Scanner;

public class B25304 {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int total = scanner.nextInt();
        int count = scanner.nextInt();
        int answer = 0;
        for (int i = 0; i < count; i++) {
            int cash = scanner.nextInt();
            int num = scanner.nextInt();
            answer+=cash*num;
        }
        if(answer == total){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
