package com.codewitheren;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
@Scope("prototype")
public class CartService /* implements DisposableBean */ { // 1st method to destroy bean before beam destroy
        /* implements InitializingBean */ // 1st method to add the step after object/ bean creation

    Map<Integer, String> mp;

    public CartService() {
        mp = new HashMap<>();
        System.out.println("CartService Constructor called");
    }

//    @Override
//    public void afterPropertiesSet() throws Exception {
//        mp.put(1, "Eren");
//        mp.put(2, "Levi");
//    }

//    // 2nd method - by init method
//    public void start() {
//        mp.put(1, "Eren");
//        mp.put(2, "Levi");
//    }

    // 3rd method: Using @PostConstruct
    @PostConstruct
    public void start2() {
        mp.put(1, "Eren");
        mp.put(2, "Levi");
    }

    public void addToCart() {
        System.out.println("Added to cart");
    }

    public String getMapValues(Integer id) {
        return mp.get(id);
    }

//    @Override
//    public void destroy() throws Exception {
//        mp.clear();
//        System.out.println("Beam is getting destroyed");
//    }

    // 2nd method to destroy beam
//    public void stop() {
//        mp.clear();
//        System.out.println("Beam is getting destroyed");
//    }

    @PreDestroy
    public void stop2() {
        mp.clear();
        System.out.println("Beam is getting destroyed");
    }
}
