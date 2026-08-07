package conditional_statements;

import java.util.Scanner;
public class SwitchCase {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int button = input.nextInt();
        switch (button){
            case 1: System.out.println("Hello");
            break;
            case 2: System.out.println("Namste");
            break;
            case 3: System.out.println("Bonjour");
            break;
            default: System.out.println("Invalid number");
        }
    }
}