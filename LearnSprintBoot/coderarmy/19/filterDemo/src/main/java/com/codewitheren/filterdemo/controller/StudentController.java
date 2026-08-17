package com.codewitheren.filterdemo.controller;

import com.codewitheren.filterdemo.dto.StudentDto;
import com.codewitheren.filterdemo.service.StudentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    private final StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    @PostMapping
    public ResponseEntity<String> createStudent(@RequestBody StudentDto studentDto) {

        studentService.createStudent(studentDto);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body("DONE");
    }
}
