package com.codewitheren;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class PaymentService {

    // Not required now
    // @Autowired
    // OrderService orderService;

//    public PaymentService(OrderService orderService) {
//        this.orderService = orderService;
//    }

    public void pay() {
        System.out.println("Payment Done");

        // Not Payment's Service responsibility
        // orderService.getOrderDetails();
    }
}
