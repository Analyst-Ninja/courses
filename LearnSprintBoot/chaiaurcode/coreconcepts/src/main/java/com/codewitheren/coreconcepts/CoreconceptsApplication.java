package com.codewitheren.coreconcepts;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CoreconceptsApplication implements CommandLineRunner {

    public static void main(String[] args) {
        SpringApplication.run(CoreconceptsApplication.class, args);
    }

    @Override
    public void run(String ... args) throws Exception {
        UserService userService = new UserService();
        userService.saveUser("Eren");
    }
}
