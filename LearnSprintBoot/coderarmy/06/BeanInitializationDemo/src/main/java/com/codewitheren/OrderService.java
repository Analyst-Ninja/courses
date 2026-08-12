package com.codewitheren;

import org.springframework.context.annotation.Lazy;
import org.springframework.stereotype.Component;

@Component
public class OrderService {

    PaymentService paymentService;

    public OrderService(@Lazy PaymentService paymentService) {

        this.paymentService = paymentService;
        System.out.println("Order Service Created");
    }

    public void placeOrder() {
        paymentService.pay();
        System.out.println("Order Placed");
    }
}
