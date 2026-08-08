package loops.exercises;

import java.util.Scanner;

public class SumOfNumbers {
    public static void main(String[] args) {
        // Question to get the sum of n natural numbers
        System.out.print("Enter a number: ");
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int sum = 0;

        for (int i = 1; i <= n; i++) sum += i;
        System.out.println(sum);
    }
}