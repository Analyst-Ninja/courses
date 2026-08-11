package com.codewitheren.coreconcepts;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    Database database;
    Configurations configurations;
    public UserService(Database database, Configurations configurations) {
        this.database = database;
        this.configurations = configurations;
    }

    public void saveUser(String user) {
        System.out.println("UserService saving the user" + user + "with property: " + configurations.getType());
        database.save(user);
    }
}
