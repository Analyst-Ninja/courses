package com.codewitheren;

import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

@Component
@Lazy
public class PaymentService {
    public PaymentService() {
        System.out.println("Payment Service Created");
    }

    public void pay() {
        System.out.println("Payment Done");
    }
}
