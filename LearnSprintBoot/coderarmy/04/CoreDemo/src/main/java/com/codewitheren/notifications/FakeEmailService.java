package com.codewitheren.notifications;

public class FakeEmailService implements NotificationService {

    @Override
    public void sendNotification() {
        System.out.println("Fake Email Notification Sent");
    }
}
