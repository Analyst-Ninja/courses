package com.codewitheren.controller;

import com.codewitheren.entity.Student;
import com.codewitheren.service.StudentService;
import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.rmi.StubNotFoundException;
import java.util.List;

@RestController
@RequestMapping("/api/students")
public class StudentController {

    private StudentService studentService;

    public StudentController(StudentService studentService) {
        this.studentService = studentService;
    }

    @GetMapping("/get/{id}")
    public ResponseEntity<Student> createStudent(@PathVariable("id") Long id) {
        Student studentResp = studentService.getStudent(id);
        if (studentResp == null) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(studentResp);
    }

    @GetMapping("/getAll")
    public ResponseEntity<List<Student>> getAllStudents() {
        List<Student> studentList = studentService.getAllStudents();
        if (studentList.isEmpty()) return ResponseEntity.notFound().build();
        return ResponseEntity.ok(studentList);
    }

    @PostMapping("/create")
    public ResponseEntity<Student> createStudent(@RequestBody Student student) {
        Student studentResp = studentService.createStudent(student);
        return ResponseEntity.ok(studentResp);
    }
}
