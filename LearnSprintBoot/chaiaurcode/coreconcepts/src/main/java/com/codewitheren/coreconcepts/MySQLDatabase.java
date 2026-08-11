package com.codewitheren.coreconcepts;

import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

@ConditionalOnProperty(name = "db.type", havingValue = "mysql")
@Component
public class MySQLDatabase implements Database {

    @Override
    public void save(String user) {
        System.out.println("MySQL is saving the user: " + user);
    }
}
