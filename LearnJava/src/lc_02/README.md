#### Data Types

- Primitive 
  - byte
  - short
  - char
  - boolean
  - int
  - long
  - float
  - double
- Non Primitive
  - String
  - Array
  - Class
  - Object
  - Interface

This is how we take input of different types in variables
```java
import java.util.*;

class Input{
    public static void main(String[] args){
        // Input
        Scanner sc = new Scanner(System.in);
        // String name = sc.next(); // For only one word
        String name = sc.nextLine(); // For only one word
        // Different types of input
        // nextInt()
        // nextFloat()
        // nextDouble()

        System.out.println(name);
    }
}
```

Notes link - [Lecture 2](https://docs.google.com/document/d/1upllrlSyv1pe86hBbNPUFT1nrmWsr6QPM4joL6Br1gU/edit?tab=t.0)
