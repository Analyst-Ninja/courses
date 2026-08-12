package com.codewitheren;

import org.springframework.stereotype.Component;

@Component
public class OrderService {

//    private final PaymentService paymentService;

//    OrderService(PaymentService paymentService) {
//        this.paymentService = paymentService;
//    }

    public void order() {
//        paymentService.pay();
        System.out.println("Order Placed");
    }
}
