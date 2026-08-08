package loops;

public class ForLoop {
    public static void main(String[] args) {
        // Example of a for loop that prints Hello world 10 times
        for (int i = 0; i < 10 ; i = i + 1) {
            System.out.println("Hello World");
        }

        System.out.println("\n====================\n");

        // Example for a for loop that prints numbers from 1 to 10 in a single line
        for (int i = 1; i <= 10; i++) { // i++ is short for i = i + 1
            System.out.print(i + " ");
        }
    }
}