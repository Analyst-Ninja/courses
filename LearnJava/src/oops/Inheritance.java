package oops;
import oops.Encapsulation;

// Base class
class Shape {
    String color;

    public void area() {
        System.out.println("Displaying Area!!");
    }
}

// Inheritance -> provide reusability
// Sub class/ Child class
class Triangle extends Shape {
    int a;
    int b;
    int c;

    public void area(int b, int h) {
        System.out.println("Triangle Area: " + (0.5*b*h));
    }
}

class EquilateralTriangle extends Triangle {
    public void area(int a, int b) {
        double area = (Math.sqrt(3) / 4) * (a * a);
        System.out.println("Equilateral Triangle Area: " + area);
    }
}

class Circle extends Shape {
    public void area(int r) {
        System.out.println("Circle Area: " + (3.14)*r*r);
    }
}


public class Inheritance {
    public static void main(String[] args) {

        Triangle t1 = new Triangle();
        t1.color = "yellow";
        System.out.println(t1.color);
        t1.area(4, 2);

        Triangle t2 = new EquilateralTriangle();
        t2.area(8, 8);

        Circle c1 = new Circle();
        c1.area(6);

    }
}