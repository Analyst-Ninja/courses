package com.codewitheren;

import com.codewitheren.payment.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

@Component
public class OrderService {

    // Dependency Injection through field
//    @Autowired
    private PaymentService paymentService;

//    OrderService(@Qualifier("cardPayment") PaymentService paymentService) {
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
