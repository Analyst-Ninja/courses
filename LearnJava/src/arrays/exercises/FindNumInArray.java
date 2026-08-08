package arrays.exercises;

import java.util.Scanner;

public class FindNumInArray {
    public static int findIndex(int[] arr, int num) {
        for (int i = 0; i < arr.length; i++) if (arr[i] == num) return i;
        return -1;
    }
    public static void main(String[] args) {
        // Input Array from user
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int size = sc.nextInt();

        int[] arr = new int[size];
        System.out.println("Enter the elements of the array: ");
        for (int i = 0; i < size; i++) arr[i] = sc.nextInt();

        System.out.println("Enter the number to be searched: ");
        int num = sc.nextInt();
        int index = findIndex(arr, num);
        if (index == -1) System.out.println("Element not found");
        else System.out.println("Element found at index: " + index);
    }
}