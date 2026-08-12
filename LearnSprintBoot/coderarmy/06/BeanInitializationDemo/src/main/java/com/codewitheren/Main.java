package com.codewitheren;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

        OrderService order = context.getBean(OrderService.class);
//        PaymentService payment = context.getBean(PaymentService.class);

        System.out.println("Payment Service is not created yet");

        order.placeOrder();
    }
}