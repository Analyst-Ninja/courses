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
    @PostMapping("/create")
    public ResponseEntity<CreateResponseDto> createStudent(
           @Valid @RequestBody CreateRequestDto createRequestDto
    ) {

        CreateResponseDto createdStudent = studentService.createStudent(createRequestDto);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(createdStudent);
    }

    // Get Student
    @GetMapping("/get")
    public ResponseEntity<CreateResponseDto> getStudent(@RequestParam Long id) {
        CreateResponseDto studentResp = studentService.getStudent(id);

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
    public ResponseEntity<List<CreateResponseDto>> getAllStudents() {
        List<CreateResponseDto> studentList = studentService.getAllStudents();
        if (studentList.isEmpty()) {
            return ResponseEntity.notFound().build();
        }
        return ResponseEntity.ok(studentList);
    }

    // Update Student record
    @PutMapping("/update")
    public ResponseEntity<UpdateResponseDto> updateStudent(
            @RequestParam Long id,
            @RequestBody UpdateRequestDto updateRequestDto
    ) {

        UpdateResponseDto student = studentService.updateStudent(id, updateRequestDto);

        if (student ==  null) {
            return ResponseEntity.notFound().build();
        }

        return ResponseEntity.ok(student);
    }

    @DeleteMapping("/delete")
    public ResponseEntity<String> deleteStudent(@RequestParam Long id) {
        Boolean isDeleted = studentService.deleteStudent(id);

        if (!isDeleted) return ResponseEntity.notFound().build();

        return ResponseEntity.ok("Record deleted");
    }

    @PatchMapping("/deleteSoftly")
    public ResponseEntity<String> deleteStudentSoftly(@RequestParam Long id) {
        Boolean isDeleted = studentService.deleteByIdSoftly(id);

        if (!isDeleted) return ResponseEntity.notFound().build();
        return ResponseEntity.ok("Record deleted with id: " + id);
    }
}
