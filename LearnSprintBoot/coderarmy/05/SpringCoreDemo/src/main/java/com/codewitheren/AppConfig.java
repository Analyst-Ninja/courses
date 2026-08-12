package com.codewitheren;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;

@Configuration
@ComponentScan("com.codewitheren")
//@ComponentScan --> It will also work | it will take the default folder or package to search
// as the package in which this config is defined
public class AppConfig {
    // Empty
}
