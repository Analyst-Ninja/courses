package com.codewitheren;


import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);

        OrderService orderService = context.getBean(OrderService.class);
        orderService.order();
    }
}

//------------------------------------------------------------------------------------------------
//    // To understand the concept of Java Reflections and class metadata
//    static class Student {
//        private String name;
//        private int age;
//
//        public Student() {
//
//        }
//
//        public void getAttendance() {
//
//        }
//
//        public void print() {
//
//        }
//    }
//}
//
//public class Main {
//    public static void main(String[] args) {
//        PaymentService paymentService = new PaymentService();
//        OrderService orderService = new OrderService(paymentService);
//        orderService.order();
//
//        // Object Creation
//        Main.Student s1 = new Main.Student();
//
//        // Class
//        Class<Main.Student> c1 = Main.Student.class;
//
//        /*
//        This class variable stores the class metadata
//        - Class name: Student
//        - Fields: name, age
//        - Constructor: Student()
//        - Methods: getAttendance, print
//        - Annotations
//
//        The concept of Class Metadata is used to understand the class structure and metadata,
//        and Spring uses the Java Reflection or Reflection API to inject those functionalities dynamically
//        */
//
//    }
