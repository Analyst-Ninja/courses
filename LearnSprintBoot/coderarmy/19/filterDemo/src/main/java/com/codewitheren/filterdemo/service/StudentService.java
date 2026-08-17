package com.codewitheren.filterdemo.service;

import com.codewitheren.filterdemo.dto.StudentDto;
import org.springframework.stereotype.Service;

@Service
public class StudentService {

    public void createStudent(StudentDto studentDto) {
        System.out.println("Student is created");
        System.out.println(studentDto.getName());
        System.out.println(studentDto.getEmail());

        try {
            Thread.sleep(3000);
        } catch (Exception e) { }


    }
}
