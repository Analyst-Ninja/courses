package oops;

class Car {
    String name;
    int year;

    // Function Overloading -
        // Compile time polymorphism - It will check the code at the compile time only,
        // if we have implemented the polymorphism correctly
    // There should be some kind of differentiating factor
        // 1. Function Return Type should be different
        // 2. Number of Parameters should be different
        // 3. Parameter type should be different (if same number of arguments)

    // Function Overriding
        // Runtime Polymorphism
        // It will be explained in Inheritance section
    public void printInfo(String name) {
        System.out.println("Name: "+ this.name);
    }

    public void printInfo(int year) {
        System.out.println("Year: "+ this.year);
    }

    public void printInfo(String name, int year) {
        System.out.println(this.name + " | " + this.year);
    }
}


class Polymorphism {
    public static void main() {

        Car c1 = new Car();
        c1.name = "BMW";
        c1.year = 2026;

        c1.printInfo(c1.name);
        c1.printInfo(c1.year);
        c1.printInfo(c1.name, c1.year);
    }
}