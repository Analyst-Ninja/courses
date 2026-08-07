package conditional_statements;

import java.util.Scanner;

public class IsEven {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();

        if (num % 2 == 0) {
            System.out.println("Even");
        }
        else {
            System.out.println("Odd");
        }
    }
}