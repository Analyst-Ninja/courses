package com.codewitheren.basiccrudspringbootdemo.repository;

import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import org.springframework.stereotype.Component;

@Component
public class StudentRepository {

    public Student saveStudent(Student student) {
        // save to DB
        System.out.println("Inside Student Repository");
        System.out.println("Exiting Student Repository");

        Student s1 = new Student();
        s1.setAge(29);
        s1.setEmail("a.bsjka@gmanasjkcn.com");
        s1.setName("HelloName");
        return s1;
    }

}
