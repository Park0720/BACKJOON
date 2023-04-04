package org.example.step2;
import java.util.Scanner;
public class B2525 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b, c;
        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();
        int d = 0;
        d = b + c;
        if(d>=60){
            a += d/60;
            b = d%60;
            if(a>=24) {
                a-=24;
            }
            System.out.printf("%d %d",a,b);
        }
        else{
            System.out.printf("%d %d",a,d);
        }
    }
}
