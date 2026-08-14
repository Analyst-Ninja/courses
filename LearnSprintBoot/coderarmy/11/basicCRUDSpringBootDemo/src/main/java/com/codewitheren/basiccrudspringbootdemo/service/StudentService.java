package com.codewitheren.basiccrudspringbootdemo.service;

import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import com.codewitheren.basiccrudspringbootdemo.repository.StudentRepository;
import org.springframework.stereotype.Service;

@Service
public class StudentService {

    private StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public Student createStudent(Student student) {
        // business logic
        // store to DB ❌
        // delegate the data to Repository
        System.out.println("Inside Student Service");
        Student studentResp = studentRepository.saveStudent(student);
        System.out.println("Exiting Student Service");
        return studentResp;
    }
}
