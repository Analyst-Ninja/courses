package lc_02;

public class Variables {
    public static void main(String[] args) {
        // Variables

        int age = 25;
        int a = 20;
        int b = 10, c = 60;
        double d = 3.14;
        String name = "Tony Stark";
        int sum = a + b + c;
        int mul = a*b*c;

        System.out.println("age: " + age);
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("c: " + c);
        System.out.println("sum: " + sum);
        System.out.println("mul: " + mul);
        System.out.println("name: " + name);

        // Modifying the values in variables
        a = 40;
        int sum2 = a + b + c;
        name = "Captain America";
        System.out.println("age: " + age);
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("c: " + c);
        System.out.println("sum2: " + sum2);
        System.out.println("name: " + name);
    }
}