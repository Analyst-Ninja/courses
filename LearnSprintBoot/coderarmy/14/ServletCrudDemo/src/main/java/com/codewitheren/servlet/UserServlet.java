package com.codewitheren.servlet;

import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;

import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

@WebServlet("/users")
public class UserServlet extends HttpServlet {

    @Override
    public void doGet(HttpRequest request, HttpResponse response) {
        String name = "a";

    }

    @Override
    public void doPost(HttpRequest request, HttpResponse response) {

    }

    @Override
    public void doPut(HttpRequest request, HttpResponse response) {

    }

    @Override
    public void doGet(HttpRequest request, HttpResponse response) {

    }



}
