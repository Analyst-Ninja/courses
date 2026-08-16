package com.codewitheren.basiccrudspringbootdemo.dto;

import jakarta.validation.constraints.*;

public class CreateRequestDto {

    @NotBlank(message = "Name cannot be blank/ empty/ null")
    @Size(min = 2, max = 50, message = "Student name must be of length b/w 2 and 50")
    private String name;

    @Min(value = 18, message = "Age should be >= 18")
    private int age;

    @Email(message = "Email should be of proper format")
    private String email;

    @Positive(message = "Roll No should be positive")
    private int rollNo;

    @NotBlank(message = "Subject not be empty/ null/ blank")
    private String subject;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getRollNo() {
        return rollNo;
    }

    public void setRollNo(int rollNo) {
        this.rollNo = rollNo;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
}
