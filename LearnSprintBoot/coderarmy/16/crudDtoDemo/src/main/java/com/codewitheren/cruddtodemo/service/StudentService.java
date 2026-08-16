package com.codewitheren.cruddtodemo.service;

import com.codewitheren.cruddtodemo.entity.Student;
import com.codewitheren.cruddtodemo.repository.StudentRepository;
import org.springframework.stereotype.Service;

@Service
public class StudentService {
    private StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public Student createStudent(Student studentReq) {
        return studentRepository.save(studentReq);
    }
}
