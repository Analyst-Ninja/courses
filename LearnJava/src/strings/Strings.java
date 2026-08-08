package strings;

import java.util.Scanner;

public class Strings {
    public static void main(String[] args) {
        // Strings are Immutable

        // String Declaration
        String firstName = "Tony";
        String LastName = "Stark";
        String sentence = "I am IRON MAN!!";

        // String input from user
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter name: ");

        // To get only 1 word as input
        // String nameInput = sc.next();

        // To get a line as input
        String nameInput = sc.nextLine();

        System.out.println("Name: " + nameInput);

        // Concatenation
        System.out.println("Full Name: " + firstName + " " + LastName);

        // Get the length of the length
        System.out.println("Length: " + sentence.length());

        // charAt() - return the character at the index
        String str = "Tony";
        for (int i = 0; i < str.length(); i++) {
            System.out.println(str.charAt(i));
        }

        // String comparison
        String str1 = "Hello";
        String str2 = "Hello";

        // 3 cases in compareTo
        // 1 --> s1 > s2   --> positive value
        // 2 --> s1 == s2  --> 0
        // 3 --> s1 < s2   --> negative value

        // using compareTo
        if (str1.compareTo(str2) == 0) {
            System.out.println("Strings are equal");
        }
        else {
            System.out.println("Strings are not equal");
        }

        // using == --> Very fragile can fail at other scenarios --> Don't use for string comparision
        if (str1 == str2) {
            System.out.println("Strings are equal");
        } else
            System.out.println("Strings are not equal");

        // newly created object comparison --> Object comparison will lead to fail because they are 2 different object
        if (new String("Hello") == new String("Hello")) {
            System.out.println("Strings are equal");
        } else
            System.out.println("Strings are not equal");

        // using equals --> Safe for string comparison
        if (str1.equals(str2)) {
            System.out.println("Strings are equal");
        } else
            System.out.println("Strings are not equal");

        // Substrings - substring(start_index, end_index)

        String longSentence = "My name is Tony Stark and I am IRON MAN!!";
        System.out.println("Substring " + longSentence.substring(5, longSentence.length()));

        // Another way
        System.out.println("Substring " + longSentence.substring(5));

    }
}