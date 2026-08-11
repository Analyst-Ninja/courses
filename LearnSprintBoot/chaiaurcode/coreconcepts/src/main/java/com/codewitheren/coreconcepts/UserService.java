package com.codewitheren.coreconcepts;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;

@Service
public class UserService {

    Database database;

    public UserService(Database database) {
        this.database = database;
    }

    public void saveUser(String user) {
        System.out.println("UserService saving the user");
        database.save(user);
    }
}
