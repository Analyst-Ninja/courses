package loops.exercises;

import java.util.Scanner;

public class MarksAppreciation {
    public static void main(String[] args) {
        // Use do while to get the menu (because it is the 1st step in any case)

        Scanner sc = new Scanner(System.in);
        int input;

        do {
            System.out.print("Enter your marks: ");
            int marks = sc.nextInt();

            if (marks < 1 || marks > 100) System.out.println("Invalid input");
            else {
                if (marks >= 90) System.out.println("This is Good");
                else if (marks >= 60) System.out.println("This is also Good");
                else System.out.println("This is Good as well");
            }

            System.out.println("Want to continue ? (yes(1) or no(0))");
            input = sc.nextInt();

        } while(input == 1);
    }
}