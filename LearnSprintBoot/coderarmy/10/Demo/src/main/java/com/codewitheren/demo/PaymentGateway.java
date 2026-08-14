package com.codewitheren.demo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class PaymentGateway {

    @Value("${paymentGateway.type:RazorPay}") // default value
    private String type;

    @Value("${paymentGateway.retry-count:3}")
    private int retryCount;

//    // Value can be set without the Constructor as well
//    public PaymentGateway(
//            @Value("${paymentGateway.type}") String type,
//            @Value("${paymentGateway.retry-count}") int retryCount
//    ) {
//        this.type = type;
//        this.retryCount = retryCount;
//    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public int getRetryCount() {
        return retryCount;
    }

    public void setRetryCount(int retryCount) {
        this.retryCount = retryCount;
    }
}

// @Value
