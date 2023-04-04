package org.example.step3;
import java.util.Scanner;

public class B25314 {
    public static void main(String[] arg) {
        Scanner scanner = new Scanner(System.in);
        int num = scanner.nextInt();
        String answer = "";
        for(int i=0;i<num/4;i++){
            answer+="long ";
        }
        answer+="int";
        System.out.println(answer);
    }
}
