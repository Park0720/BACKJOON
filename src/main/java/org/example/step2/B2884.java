package org.example.step2;
import java.util.Scanner;
public class B2884 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();
        int c = 0;
        if(b<45){
            c = b - 45;
            b = 60 + c;
            if(a==0) {
                a=24;
            }
            a--;
            System.out.printf("%d %d",a,b);
        }
        else{
            b = b-45;
            System.out.printf("%d %d",a,b);
        }
    }
}
