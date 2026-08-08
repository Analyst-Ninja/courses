package arrays.exercises;

import java.util.Scanner;

public class FindNumIn2DArray {

    public static int[] findIn2DArray(int[][] arr, int num) {
        int[] index = {-1, -1};
        for (int i = 0; i < arr.length; i++){
            for (int j = 0; j < arr[i].length; j++){
                if (arr[i][j] == num){
                    index[0] = i;
                    index[1] = j;
                }
            }
        }
        return index;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        int[][] arr = new int[rows][cols];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                arr[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter the number to be searched: ");
        int numberToSearch = sc.nextInt();

        int[] index = findIn2DArray(arr, numberToSearch);
        System.out.println("Element at index: [" + index[0] + " " + index[1] + "]");
    }
}