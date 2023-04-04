package org.example.step2;

import java.util.*;

public class B2480 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a, b, c;
        a = scanner.nextInt();
        b = scanner.nextInt();
        c = scanner.nextInt();
        if(a==b && b==c){
            System.out.println(10000+a*1000);
        }
        else if(a==b){
            System.out.println(1000+a*100);
        }
        else if(b==c){
            System.out.println(1000+b*100);
        }
        else if(a==c){
            System.out.println(1000+a*100);
        }
        else{
            List<Integer> list = new ArrayList<>();
            list.add(a);
            list.add(b);
            list.add(c);
            Collections.sort(list);
            System.out.println(list.get(2)*100);
        }
    }
}
