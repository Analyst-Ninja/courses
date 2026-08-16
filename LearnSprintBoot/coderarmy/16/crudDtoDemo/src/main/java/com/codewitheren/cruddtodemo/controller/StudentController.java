package com.codewitheren.cruddtodemo.controller;

import com.codewitheren.cruddtodemo.entity.Student;
import com.codewitheren.cruddtodemo.service.StudentService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    private StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    // create
    public ResponseEntity<Student> createStudent(@RequestBody Student student) {
        Student studentResponse = studentService.createStudent(student);

        return ResponseEntity.ok(studentResponse);
    }

    // read

    // update

    // delete
}
