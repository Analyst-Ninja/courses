package com.codewitheren.basiccrudspringbootdemo.repository;

import com.codewitheren.basiccrudspringbootdemo.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;
import java.util.Optional;

//@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {

    Optional<Student> findByIdAndDeletedIsFalse(Long id);

    List<Student> findAllByDeletedIsFalse();

    // findBy + fieldName + condition
}
