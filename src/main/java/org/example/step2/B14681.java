package org.example.step2;
import java.util.Scanner;
public class B14681 {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int a, b;
        a = scanner.nextInt();
        b = scanner.nextInt();
        if(a>0 && b>0){
            System.out.println(1);
        }
        else if(a>0 && b<0){
            System.out.println(4);
        }
        else if(a<0 && b>0){
            System.out.println(2);
        }
        else{
            System.out.println(3);
        }
    }
}
