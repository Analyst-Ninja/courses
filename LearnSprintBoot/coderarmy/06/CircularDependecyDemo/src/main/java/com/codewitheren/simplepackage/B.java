package com.codewitheren.simplepackage;

public class B {
    public A a;

    public B() {
        System.out.println("B created");
        this.a = new A();
    }
}
