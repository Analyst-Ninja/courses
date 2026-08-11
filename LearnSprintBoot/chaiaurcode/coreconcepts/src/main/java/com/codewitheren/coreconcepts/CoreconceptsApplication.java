package com.codewitheren.coreconcepts;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CoreconceptsApplication implements CommandLineRunner {

    public static void main(String[] args) {
        SpringApplication.run(CoreconceptsApplication.class, args);
    }

    public CoreconceptsApplication(UserService userService) {
        this.userService = userService;
    }

    private final UserService userService;

    @Override
    public void run(String ... args) throws Exception {
        userService.saveUser("Eren");
    }
}
