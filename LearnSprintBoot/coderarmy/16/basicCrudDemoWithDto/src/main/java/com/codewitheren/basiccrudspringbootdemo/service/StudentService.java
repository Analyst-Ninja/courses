package com.codewitheren.basiccrudspringbootdemo.service;

import com.codewitheren.basiccrudspringbootdemo.dto.CreateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.CreateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import com.codewitheren.basiccrudspringbootdemo.exception.DuplicateResourceException;
import com.codewitheren.basiccrudspringbootdemo.exception.ResourceNotFoundException;
import com.codewitheren.basiccrudspringbootdemo.repository.StudentRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;

@Service
public class StudentService {

    private StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    public CreateResponseDto createStudent(CreateRequestDto createRequestDto) {
        // business logic
        // store to DB ❌
        // delegate the data to Repository
        Student student = mapToEntity(createRequestDto);

        if (emailExists(student)) {
            throw new DuplicateResourceException("Resource with the `" + student.getEmail() +"` email already exists");
        }

        Student studentResp = studentRepository.save(student);

        return mapToDto(studentResp);
    }

    public CreateResponseDto getStudent(Long id) {
//        Student studentResp = studentRepository
//                .findByIdAndDeletedIsFalse(id)
//                .orElse(null);

        Student studentResp = studentRepository
                .findByIdAndDeletedIsFalse(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("No student found with the Id: " + id)
                );

        return mapToDto(studentResp);
    }

    public List<CreateResponseDto> getAllStudents() {
        List<Student> allStudents = studentRepository.findAllByDeletedIsFalse();

        if (allStudents.isEmpty()) return null;

        return allStudents.stream()
                .map(this::mapToDto)
                .toList();
    }

    public UpdateResponseDto updateStudent(Long id, UpdateRequestDto updateRequestDto) {
        Student existingStudent = studentRepository
                .findByIdAndDeletedIsFalse(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("Student not present with id: " + id));

        existingStudent.setName(updateRequestDto.getName());
        existingStudent.setAge(updateRequestDto.getAge());
        existingStudent.setRollNo(updateRequestDto.getRollNo());
        existingStudent.setSubject(updateRequestDto.getSubject());
        existingStudent.setDeleted(false); // Can be deleted now, as we will not get the deleted value from user explicitly
        existingStudent.setUpdatedAt(LocalDateTime.now());

        Student updatedStudent = studentRepository.save(existingStudent);

        return mapToUpdateDto(updatedStudent);
    }

    public void deleteStudent(Long id) {
        // check of id exist

        Student studentToBeDeleted = studentRepository
                .findById(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("Student not present with id: " + id));

        // deleting record
        studentRepository.delete(studentToBeDeleted);
    }

    // soft delete
    public void deleteByIdSoftly(Long id) {

        // delete student (softly)
        Student studentToSoftDeleted = studentRepository
                .findByIdAndDeletedIsFalse(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException("Student not present with id: " + id));

        studentToSoftDeleted.setDeleted(true);
        studentRepository.save(studentToSoftDeleted);
    }

    private Student mapToEntity(CreateRequestDto createRequestDto) {
        Student student = new Student();

        // Very tedious - we can forget some key to set
        student.setName(createRequestDto.getName());
        student.setAge(createRequestDto.getAge());
        student.setSubject(createRequestDto.getSubject());
        student.setRollNo(createRequestDto.getRollNo());
        student.setEmail(createRequestDto.getEmail());
        student.setDeleted(false);
        student.setUpdatedAt(LocalDateTime.now());
        student.setCreatedAt(LocalDateTime.now());

        // builder pattern

        return student;
    }

    private CreateResponseDto mapToDto(Student student) {
        CreateResponseDto createResponseDto = new CreateResponseDto();

        createResponseDto.setName(student.getName());
        createResponseDto.setAge(student.getAge());
        createResponseDto.setSubject(student.getSubject());
        createResponseDto.setRollNo(student.getRollNo());
        createResponseDto.setEmail(student.getEmail());
        createResponseDto.setId(student.getId());
        createResponseDto.setMessage("Student saved successfully");
        createResponseDto.setCreatedAt(student.getCreatedAt());
        createResponseDto.setUpdatedAt(student.getUpdatedAt());

        return createResponseDto;
    }

    private UpdateResponseDto mapToUpdateDto(Student student) {
        UpdateResponseDto updateResponseDto = new UpdateResponseDto();

        updateResponseDto.setName(student.getName());
        updateResponseDto.setAge(student.getAge());
        updateResponseDto.setSubject(student.getSubject());
        updateResponseDto.setRollNo(student.getRollNo());
        updateResponseDto.setEmail(student.getEmail());
        updateResponseDto.setMessage("Student updated successfully");
        updateResponseDto.setCreatedAt(student.getCreatedAt());
        updateResponseDto.setUpdatedAt(student.getUpdatedAt());

        return updateResponseDto;
    }

    public Boolean emailExists(Student student) {
        return studentRepository.existsByEmail(student.getEmail());
    }
}
