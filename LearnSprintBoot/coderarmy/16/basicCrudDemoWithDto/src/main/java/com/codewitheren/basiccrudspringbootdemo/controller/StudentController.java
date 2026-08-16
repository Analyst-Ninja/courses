package com.codewitheren.basiccrudspringbootdemo.controller;

import com.codewitheren.basiccrudspringbootdemo.dto.CreateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.CreateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import com.codewitheren.basiccrudspringbootdemo.service.StudentService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Value;
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
    @PostMapping
    public ResponseEntity<CreateResponseDto> createStudent(
           @Valid @RequestBody CreateRequestDto createRequestDto
    ) {

        CreateResponseDto createdStudent = studentService.createStudent(createRequestDto);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(createdStudent);
    }

    // Get Student
    @GetMapping("/{id}")
    public ResponseEntity<CreateResponseDto> getStudent(@PathVariable Long id) {
        CreateResponseDto studentResp = studentService.getStudent(id);

        return ResponseEntity.ok(studentResp);
    }

    // Get all students
    @GetMapping
    public ResponseEntity<List<CreateResponseDto>> getAllStudents() {
        List<CreateResponseDto> studentList = studentService.getAllStudents();

        return ResponseEntity.ok(studentList);
    }

    // Update Student record
    @PutMapping
    public ResponseEntity<UpdateResponseDto> updateStudent(
            @RequestParam Long id,
            @RequestBody UpdateRequestDto updateRequestDto
    ) {

        UpdateResponseDto student = studentService.updateStudent(id, updateRequestDto);

        return ResponseEntity.ok(student);
    }

    @DeleteMapping
    public ResponseEntity<String> deleteStudent(@RequestParam Long id) {
        studentService.deleteStudent(id);

        return ResponseEntity
                .status(HttpStatus.NO_CONTENT)
                .build();
    }

    @PatchMapping("/deleteSoftly")
    public ResponseEntity<String> deleteStudentSoftly(@RequestParam Long id) {
        studentService.deleteByIdSoftly(id);

        return ResponseEntity
                .status(HttpStatus.NO_CONTENT)
                .build();
    }
}
