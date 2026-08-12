package com.codewitheren;

import com.codewitheren.payment.CardPayment;
import com.codewitheren.payment.PaymentService;
import com.codewitheren.payment.UPIPayment;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Configuration
@ComponentScan("com.codewitheren")
//@ComponentScan --> It will also work | it will take the default folder or package to search as the package in which this config is defined
public class AppConfig {

    @Bean
    public User createUser() {
        return new User("Eren", 25);
    }

    @Bean
    @Qualifier("cp")
    public PaymentService cardPaymentService() {
        return new CardPayment();
    }

    @Bean
    @Qualifier("upi")
    public PaymentService UPIPaymentService() {
        return new UPIPayment();
    }

    @Bean
    public OrderService orderService(@Qualifier("upi") PaymentService paymentService) {
        return new OrderService(paymentService);
    }
}
