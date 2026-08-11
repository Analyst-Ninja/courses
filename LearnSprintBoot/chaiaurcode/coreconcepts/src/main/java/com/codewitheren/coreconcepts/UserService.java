package com.codewitheren.coreconcepts;

public class UserService {

    MySQLDatabase mySQLDatabase = new MySQLDatabase();
    public void saveUser(String user) {
        System.out.println("UserService saving the user");
        mySQLDatabase.saveToDB(user);
    }
}
