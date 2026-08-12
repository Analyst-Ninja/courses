package com.codewitheren.notifications;

public class EmailService implements NotificationService {

    @Override
    public void sendNotification() {
        // Actual Email notification logic
        System.out.println("Email Notification Sent");
    }
}
