package loops.exercises;

import java.util.Scanner;

public class IsPrime {
    public static void main(String[] args) {
        // Exercise to find a number is prime or not
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt();
        int count = 0;
        for (int i = 1; i <= n; i++) {
            if (n % i == 0)  count++;

            if (count == 3) break;
        }

        if (n == 1) System.out.println("Neither prime nor composite");
        else {
            if (count == 2) System.out.println("Prime");
            else System.out.println("Not Prime");
        }

    }
}