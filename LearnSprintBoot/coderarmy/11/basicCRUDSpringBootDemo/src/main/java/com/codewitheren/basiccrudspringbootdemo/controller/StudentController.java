package com.codewitheren.basiccrudspringbootdemo.controller;

import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import com.codewitheren.basiccrudspringbootdemo.service.StudentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("api/students")
public class StudentController {

    private StudentService studentService;

    public StudentController( StudentService studentService) {
        this.studentService = studentService;
    }

    // Create a student
    @PostMapping("/create")
    public ResponseEntity<Student> createStudent(@RequestBody Student student) {

        Student createdStudent = studentService.createStudent(student);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(createdStudent);
    }

    // Get Student
    @GetMapping("/get/{id}")
    public ResponseEntity<Optional<Student>> getStudent(@PathVariable Long id) {
        Optional<Student> studentResp = studentService.getStudent(id);

        if (studentResp == null) {
            return ResponseEntity
                    // .status(HttpStatus.NOT_FOUND).body(studentResp);
                    // Another way
                    .notFound().build();
        }

        return ResponseEntity.ok(studentResp);
    }

    // Get all students
    @GetMapping("/getAll")
    public ResponseEntity<List<Student>> getAllStudents() {
        List<Student> studentList = studentService.getAllStudents();
        if (studentList.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(studentList);
    }

    // Update Student record
    @PutMapping("/update/{id}")
    public ResponseEntity<Student> updateStudent(
            @PathVariable Long id,
            @RequestBody Student studentReq
    ) {

        Student student = studentService.updateStudent(id, studentReq);

        if (student ==  null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(student);
    }

    @DeleteMapping("delete/{id}")
    public ResponseEntity<String> deleteStudent(@PathVariable Long id) {
        Boolean isDeleted = studentService.deleteStudent(id);

        if (!isDeleted) return ResponseEntity.notFound().build();

        return ResponseEntity.ok("Record deleted");
    }
}
