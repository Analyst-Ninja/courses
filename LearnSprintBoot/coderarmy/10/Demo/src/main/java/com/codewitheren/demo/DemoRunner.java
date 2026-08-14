package com.codewitheren.demo;

import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class DemoRunner implements CommandLineRunner /* ApplicationRunner */ {

    private BetterPaymentGateway betterPaymentGateway;

    public DemoRunner(BetterPaymentGateway betterPaymentGateway) {
        this.betterPaymentGateway = betterPaymentGateway;
    }

//    @Override
//    public void run(ApplicationArguments args) throws Exception {
//        betterPaymentGateway.print();
//    }

    @Override
    public void run(String... args) throws Exception {
        betterPaymentGateway.print();
    }
}
