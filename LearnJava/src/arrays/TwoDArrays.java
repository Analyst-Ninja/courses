package arrays;

import java.util.Scanner;

public class TwoDArrays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Size input - rows and columns
        System.out.println("Enter the size of the array");
        System.out.println("number of rows: ");
        int rows = sc.nextInt();
        System.out.println("number of columns: ");
        int cols = sc.nextInt();

        int[][] arr = new int[rows][cols];

        // input
        // rows
        for (int i = 0; i < rows; i++) {
            // columns
            for (int j = 0; j < cols; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        // output
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }

        // Closing the scanner cursor
        sc.close();
    }
}