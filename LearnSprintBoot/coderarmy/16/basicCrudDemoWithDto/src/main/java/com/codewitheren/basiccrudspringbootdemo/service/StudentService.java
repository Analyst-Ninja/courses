package com.codewitheren.basiccrudspringbootdemo.service;

import com.codewitheren.basiccrudspringbootdemo.dto.CreateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.CreateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateRequestDto;
import com.codewitheren.basiccrudspringbootdemo.dto.UpdateResponseDto;
import com.codewitheren.basiccrudspringbootdemo.entity.Student;
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

        Student studentResp = studentRepository.save(student);

        return mapToDto(studentResp);
    }

    public CreateResponseDto getStudent(Long id) {
        Optional<Student> studentResp = studentRepository.findByIdAndDeletedIsFalse(id);

        if(studentResp.isPresent()) {
            return mapToDto(studentResp.get());
        }
        return null;
    }

    public List<CreateResponseDto> getAllStudents() {
        List<Student> allStudents = studentRepository.findAllByDeletedIsFalse();

        if (allStudents.isEmpty()) return null;

        return allStudents.stream()
                .map(this::mapToDto)
                .toList();
    }

    public UpdateResponseDto updateStudent(Long id, UpdateRequestDto updateRequestDto) {
        Optional<Student> existingStudent = studentRepository.findByIdAndDeletedIsFalse(id);

        if (existingStudent.isEmpty()) {
            return null;
        }

        Student studentToUpdate = existingStudent.get();
        studentToUpdate.setName(updateRequestDto.getName());
        studentToUpdate.setAge(updateRequestDto.getAge());
        studentToUpdate.setRollNo(updateRequestDto.getRollNo());
        studentToUpdate.setSubject(updateRequestDto.getSubject());
        studentToUpdate.setDeleted(false); // Can be deleted now, as we will not get the deleted value from user explicitly
        studentToUpdate.setUpdatedAt(LocalDateTime.now());

        Student updatedStudent = studentRepository.save(studentToUpdate);

        return mapToUpdateDto(updatedStudent);
    }

    public Boolean deleteStudent(Long id) {
        // check of id exist

        boolean isStudent = studentRepository.existsById(id);

        if (!isStudent) return false;

        // deleting record
        studentRepository.deleteById(id);

        return true;

    }

    // soft delete
    public Boolean deleteByIdSoftly(Long id) {

        Optional<Student> existingStudent = studentRepository.findByIdAndDeletedIsFalse(id);

        if (existingStudent.isEmpty()) return false;

        // delete student (softly)
        Student studentToSoftDelete = existingStudent.get();
        studentToSoftDelete.setDeleted(true);

        studentRepository.save(studentToSoftDelete);

        return true;
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
}
