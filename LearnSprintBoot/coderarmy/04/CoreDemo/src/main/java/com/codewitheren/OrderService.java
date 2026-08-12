package com.codewitheren;

import com.codewitheren.notifications.EmailService;
import com.codewitheren.notifications.NotificationService;
import com.codewitheren.notifications.PopUpNotificationService;

public class OrderService {

    NotificationService notification;

    public OrderService(NotificationService notification) {
        this.notification = notification;
    }

    public void placeOrder() {
        System.out.println("Order Placed");
        notification.sendNotification();
    }
}
