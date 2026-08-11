package com.codewitheren.coreconcepts;

import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Component;

@ConditionalOnProperty(name = "db.type", havingValue = "postgres")
@Component
public class PostgresDatabase implements Database {

    @Override
    public void save(String user) {
        System.out.println("Saving user in Postgres: " + user);
    }
}
