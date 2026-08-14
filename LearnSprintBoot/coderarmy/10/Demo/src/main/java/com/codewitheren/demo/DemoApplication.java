package com.codewitheren.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {

        SpringApplication.run(DemoApplication.class, args);
//        ApplicationContext context = SpringApplication.run(DemoApplication.class, args);
//
//        PaymentGateway paymentGateway = context.getBean(PaymentGateway.class);
//        // These values are getting injected from the application.properties
//        paymentGateway.setType("Paytm");
//        paymentGateway.setRetryCount(5);

//        System.out.println(paymentGateway.getType());
//        System.out.println(paymentGateway.getRetryCount());
//
//        PaymentProperties paymentProperties = context.getBean(PaymentProperties.class);
//
//        System.out.println(paymentProperties.getType());
//        System.out.println(paymentProperties.getRetryCount());

//        BetterPaymentGateway betterPaymentGateway = context.getBean(BetterPaymentGateway.class);
//
//        betterPaymentGateway.print();


    }

}

// application.properties
