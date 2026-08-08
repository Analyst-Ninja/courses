package functions_and_methods;

import java.util.Scanner;

public class Functions {
    public static void printMyName(String name){ // Function Declaration
        System.out.println(name);
    }

    public static int calculateSum(int a, int b){
        return a+b;
    }

    public static int calculateProduct(int a, int b){
        return a*b;
    }

    public static int calculateFactorial(int n){
        int factorial = 1;

        // Checking for invalid number
        if (n<0){
            System.out.println("Invalid number");
            return -1;
        }

        // base case
        if (n == 1 || n == 0) return factorial;

        // Loop for calculating factorail
        for (int i = 1; i <= n; i++) {
            factorial *= i;
        }
        return factorial;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Print Name
        String name = sc.nextLine();
        printMyName(name); // Function call

        // Sum function
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = calculateSum(a, b); // Function call
        System.out.println(sum);

        // calculateProduct function
        int a1 = sc.nextInt();
        int b1 = sc.nextInt();
        int prod = calculateProduct(a1, b1); // Function call
        System.out.println(prod);

        // calculateFactorial function
        int num = sc.nextInt();
        int factorial = calculateFactorial(num); // Function call
        System.out.println(factorial);
    }
}