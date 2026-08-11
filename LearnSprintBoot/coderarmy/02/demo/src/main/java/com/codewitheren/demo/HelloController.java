package com.codewitheren.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    // --> /hello
    // --> /orders

    @GetMapping("hello")
    public String helloWorld() {
        return "<h1>Hello World</h1>";
    }

    @GetMapping("bye")
    public String bye() {
        return "<h1>See you soon!</h1>";
    }
}
