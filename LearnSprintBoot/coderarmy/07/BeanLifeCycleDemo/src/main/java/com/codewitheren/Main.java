package com.codewitheren;


import org.springframework.context.ApplicationContext;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
//        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        ConfigurableApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

        OrderService orderService = context.getBean(OrderService.class);
        orderService.placeOrder();

        AppConfig config = context.getBean(AppConfig.class);
//        config.getDemo();

        CartService cartService = context.getBean(CartService.class);
        System.out.printf(cartService.getMapValues(2) + "\n");

        context.close();
    }
}