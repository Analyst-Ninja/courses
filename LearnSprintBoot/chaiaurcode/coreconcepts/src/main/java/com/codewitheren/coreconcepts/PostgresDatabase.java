package com.codewitheren.coreconcepts;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Profile("prod")
@Component
public class PostgresDatabase implements Database {

    @Override
    public void save(String user) {
        System.out.println("Saving user in Postgres: " + user);
    }
}
