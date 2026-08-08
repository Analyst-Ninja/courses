package conditional_statements.exercises;

import java.util.Scanner;
public class Calculator {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        String operator = sc.next();

        switch (operator) {
            case "+": System.out.println(a + b);
            break;
            case "-": System.out.println(a - b);
            break;
            case "*": System.out.println(a * b);
            break;
            case "/": System.out.println(a / b);
            break;
            case "%": System.out.println(a % b);
            break;
            default: System.out.println("Invalid Operator");
        }
    }
}