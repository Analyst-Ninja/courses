package oops;

interface Bird {
    void fly();
    void eat();
}

interface Herbivore {
    void eatVeganFood();
}

class Parrot implements Bird, Herbivore {
    public void fly() {
        System.out.println("Parrot is flying!!");
    }

    public void eatVeganFood() {
        System.out.println("Parrot eating Spinach!!");
    }

    public void eat() {
        System.out.println("Parrot is eating!!");
    }
}

public class Interface {
    public static void main() {
        Parrot p = new Parrot();
        p.eat();
        p.fly();
        p.eatVeganFood();
    }
}
