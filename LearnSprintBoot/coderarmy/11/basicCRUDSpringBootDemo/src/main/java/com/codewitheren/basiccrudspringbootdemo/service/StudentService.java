package com.codewitheren.basiccrudspringbootdemo.service;

import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import com.codewitheren.basiccrudspringbootdemo.repository.StudentRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class StudentService {

    private StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public Student createStudent(Student studentReq) {
        // business logic
        // store to DB ❌
        // delegate the data to Repository

        Student studentResp = studentRepository.save(studentReq);

        return studentResp;
    }

    public Optional<Student> getStudent(Long id) {
        Optional<Student> studentResp = studentRepository.findById(id);

        if (studentResp.isPresent()) {
            return studentResp;
        }
        else {
            return null;
        }
    }

    public List<Student> getAllStudents() {
        List<Student> allStudents = studentRepository.findAll();

        if (allStudents.isEmpty()) return null;

        return allStudents;
    }

    public Student updateStudent(Long id, Student studentReq) {
        Optional<Student> existingStudent = studentRepository.findById(id);

        if (existingStudent.isEmpty()) {
            return null;
        }

        Student studentToUpdate = existingStudent.get();
        studentToUpdate.setName(studentReq.getName());
        studentToUpdate.setEmail(studentReq.getEmail());
        studentToUpdate.setAge(studentReq.getAge());
        studentToUpdate.setRollNo(studentReq.getRollNo());
        studentToUpdate.setSubject(studentReq.getSubject());

        return studentRepository.save(studentToUpdate);
    }

    public Boolean deleteStudent(Long id) {
        // check of id exist

        boolean isStudent = studentRepository.existsById(id);

        if (!isStudent) return false;

        // deleting record
        studentRepository.deleteById(id);

        return true;

    }
}
