package com.codewitheren.simplepackage;

public class A {
    public B b;

    public A() {
        System.out.println("A created");
        this.b = new B();
    }
}
