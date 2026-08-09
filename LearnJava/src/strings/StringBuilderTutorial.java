package strings;
import java.util.*;

public class StringBuilderTutorial {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder("Tony");

        // Print
        System.out.println(sb);

        // Char at Index 0
        System.out.println(sb.charAt(0));

        // Set character at index
        sb.setCharAt(0, 'P');
        System.out.println(sb);

        // insert character at index i
        sb.insert(2,'n');
        System.out.println(sb);

        // Delete character/ substring from sb
        sb.delete(2, 3);
        System.out.println(sb);

        sb.delete(2, 4);
        System.out.println(sb);

        // Append
        sb.append("Stark");
        System.out.println(sb);

        // Length
        System.out.println(sb.length());

        // Reverse a string
        System.out.println(sb.reverse());

        // Capacity
        System.out.println(sb.capacity());

        // Loop to reverse a string
        StringBuilder str = new StringBuilder("hello");

        for (int i = 0; i < str.length()/2; i++) {
            int front = i;
            int back = str.length() - i - 1;

            char frontChar = str.charAt(front);
            char backChar = str.charAt(back);

            str.setCharAt(front, backChar);
            str.setCharAt(back, frontChar);
        }

        System.out.println(str);
    }
}