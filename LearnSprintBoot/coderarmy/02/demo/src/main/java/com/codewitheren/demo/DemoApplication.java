package com.codewitheren.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {

        SpringApplication.run(DemoApplication.class, args);

        System.out.println("Hello World");

        // Or

        // HelloController helloController = new HelloController();
        // System.out.println(helloController.helloWorld());

    }
}
