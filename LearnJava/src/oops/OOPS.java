package oops;

class Pen {
    String color;
    String type; // ball-point / gel

    public void write() {
        System.out.println("Writing Something!!");
    }

    public void printColor() {
        System.out.println("Color: " + this.color);
    }
}

class Student {
    String name;
    int age;

     // Non parameterized constructor definition
     Student() {
        System.out.println("Constructor called!!");
     }

    // Parameterized constructor definition
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Copy Constructor
    Student(Student other) {
        this.name = other.name;
        this.age = other.age;
    }

    // For copy constructor a non parameterized constructor is required
    // Student() {
    //
    // }

    public void printInfo() {
        System.out.println("Name: " +this.name);
        System.out.println("Age: " +this.age);
    }
}

public class OOPS {
    public static void  main () {
        // Instantiating Pen object from Pen class
        Pen pen1 = new Pen();
        pen1.color = "Blue";
        pen1.type = "Ball-Point";

        Pen pen2 = new Pen();
        pen2.color = "Black";
        pen2.type = "Gel";

        System.out.println(pen1);

        pen1.write();
        pen1.printColor();

        pen2.write();
        pen2.printColor();

        Student s1 = new Student();
        s1.name = "Eren";
        s1.age = 29;

        Student s2 = new Student(s1);

        s1.printInfo();
        s2.printInfo();
    }
}