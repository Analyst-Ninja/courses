package com.codewitheren;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class OrderService {

    // Dependency Injection through field
//    @Autowired
    private PaymentService paymentService;

    @Autowired
    OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

//    // Dependency Injection through setter method
//    @Autowired
//    public void setPaymentService(PaymentService paymentService) {
//        this.paymentService = paymentService;
//    }



    public void order() {
        paymentService.pay();
        System.out.println("Order Placed");
    }
}
