package com.codewitheren;

import com.codewitheren.notifications.EmailService;
import com.codewitheren.notifications.FakeEmailService;
import com.codewitheren.notifications.NotificationService;
import com.codewitheren.notifications.PopUpNotificationService;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        NotificationService notification = new EmailService();
        // OrderService orderService = new OrderService(notification);
        OrderService orderService = new OrderService();
        orderService.setNotification(notification);
        orderService.placeOrder();
    }
}