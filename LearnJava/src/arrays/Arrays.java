package arrays;

import java.util.Scanner;

public class Arrays {
    public static void main(String[] args) {

        int marks [] = new int[3];
        marks[0] = 100; // Maths
        marks[1] = 99; // Physics
        marks[2] = 98; // Chemistry

        // Another way to define an array of fixed size
        int [] marks_new = {100, 99, 97};

        // System.out.println(marks[0]);
        // System.out.println(marks[1]);
        // System.out.println(marks[2]);

        System.out.println("Marks from `marks` variable");
        for (int i = 0; i < 3; i++) {
            System.out.println(marks[i]);
        }

        System.out.println("Marks from `marks_new` variable");
        for (int i = 0; i < 3; i++) {
            System.out.println(marks_new[i]);
        }

        // Take number as input in array

        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Size: ");
        int size = sc.nextInt();
        int [] numbers = new int[size];
        // In Java, variables are initialized with their default values
        // int -> 0
        // object -> Null
        // boolean -> false
        // String -> ""
        // float -> 0.0 etc.
        // for (int i = 0; i < size; i++) {
        //    System.out.println(numbers[i]);
        // }

        // Taking numbers as input
        for (int i = 0; i < size; i++) {
            numbers[i] = sc.nextInt();
        }

        // Printing Array
        for (int i = 0; i < numbers.length; i++) {
            System.out.println(numbers[i]);
        }

        // Another way to iterate over array
        for (int number : numbers) {
            System.out.println(number);
        }

    }
}