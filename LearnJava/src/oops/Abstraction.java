package oops;

abstract class Animal {
    // Constructor can also be created
    Animal() {
        System.out.println("Animal has been created");
    }

    // abstract function
    abstract void walk();

    // non-abstract function
    public void eat() {
        System.out.println("Eating.");
    }
}

class Horse extends Animal {
    Horse() {
        System.out.println("Horse has been created");
    }

    public void walk() {
        System.out.println("Walks in 4 legs");
    }
}

class Chicken extends Animal {
    public void walk() {
        System.out.println("Walks in 2 legs");
    }
}


public class Abstraction {
    public static void main() {
        Horse h = new Horse();
        h.walk();
        h.eat();

        // Checking for creating the object for abstract class
        // Animal a = new Animal();
        // a.walk();
        // It gives the compilation error --> We can't make an object from an abstract class


    }
}
