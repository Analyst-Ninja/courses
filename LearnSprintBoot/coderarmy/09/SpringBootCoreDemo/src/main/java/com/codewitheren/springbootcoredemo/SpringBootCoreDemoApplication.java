package com.codewitheren.springbootcoredemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class SpringBootCoreDemoApplication {

    public static void main(String[] args) {

        ApplicationContext context = SpringApplication.run(SpringBootCoreDemoApplication.class, args);

        OrderService orderService = context.getBean(OrderService.class);
        orderService.placeOrder();

        UserService userService = context.getBean(UserService.class);

        UserService a = getUserServiceBean();
        System.out.printf(a.toString());

    }

    @Bean
    public static UserService getUserServiceBean() {
        return new  UserService();
    }

}
