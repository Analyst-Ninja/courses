package com.codewitheren;

import com.codewitheren.notifications.EmailService;
import com.codewitheren.notifications.NotificationService;
import com.codewitheren.notifications.PopUpNotificationService;

public class OrderService {

    NotificationService notification;

    public OrderService(NotificationService notification) {
        this.notification = notification;
    }

    // Overloading to check the usage of setter
    public OrderService() {}

    public void placeOrder() {
        System.out.println("Order Placed");
        // Actual Business Logic
        notification.sendNotification();
    }

    public void setNotification(NotificationService notification) {
        this.notification = notification;
    }
}
