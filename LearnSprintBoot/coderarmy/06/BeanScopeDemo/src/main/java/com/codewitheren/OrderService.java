package com.codewitheren;

import org.springframework.context.annotation.Scope;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

@Component
//@Scope("singleton") // Eager Initialization but create only one object
@Scope("prototype") // Lazy initialization but create multiple object when required/ craeted
public class OrderService {

    public OrderService() {
        System.out.println("Order Service created...");
    }

    public void placeOrder() {
        System.out.println("Order placed");
    }
}
