package com.codewitheren.notifications;

public class SmsService implements NotificationService {

    @Override
    public void sendNotification() {
        System.out.println("SMS notification sent");
    }
}
