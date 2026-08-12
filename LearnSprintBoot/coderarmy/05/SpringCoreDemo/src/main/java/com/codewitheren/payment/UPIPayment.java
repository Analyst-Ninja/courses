package com.codewitheren.payment;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

// @Component
// @Primary
@Qualifier("UPI") // If we don't wanna use @Primary
public class UPIPayment implements PaymentService {
    @Override
    public void pay() {
        System.out.println("Payment via UPI");
    }
}
