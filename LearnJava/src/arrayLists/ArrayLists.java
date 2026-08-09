package arrayLists;

import java.util.ArrayList;
import java.util.Collections;

public class ArrayLists {
    public static void main() {
        // Integer | Float | Boolean | String --> ArrayList does not store primitive data type, it stores only objects
        ArrayList<Integer> list =  new ArrayList<Integer>();
        // ArrayList<Integer> list =  new ArrayList<>(); This is also a correct format
        // ArrayList<String> names = new ArrayList<String>();
        // ArrayList<Boolean> booleans = new ArrayList<Boolean>();

        // Add element
        list.add(1);
        list.add(2);
        list.add(5);

        System.out.println(list);

        // Get element
        int ele = list.get(2);
        System.out.println(ele);

        // To add element in between
        list.add(1, 100);
        System.out.println(list);

        // Set element
        list.set(0, 800);
        System.out.println(list);

        // Delete element
        list.remove(1); // removing element at 1 index --> 100
        System.out.println(list);

        // Get Size
        int size =  list.size();
        System.out.println(size);

        // Iterate on ArrayList
        for (int i=0; i < list.size(); i++) {
            System.out.print(list.get(i)+" ");
        }
        System.out.println();

        // Sorting
        Collections.sort(list);
        System.out.println(list);

    }
}
