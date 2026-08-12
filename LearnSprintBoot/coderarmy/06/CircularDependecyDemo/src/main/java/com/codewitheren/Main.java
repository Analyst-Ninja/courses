package com.codewitheren;

import com.codewitheren.simplepackage.A;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.io.ObjectInputFilter;

public class Main {
    public static void main(String[] args) {

        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

        OrderService orderService = (OrderService) context.getBean("orderService");
        orderService.placeOrder();

//        A a = new A();
    }
}