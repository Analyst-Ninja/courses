package com.codewitheren.filterdemo.filter;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.util.UUID;


@Component
@Order(2)
public class LoggingFilter implements Filter {


    @Override
    public void doFilter(
            ServletRequest servletRequest,
            ServletResponse servletResponse,
            FilterChain filterChain
    )
            throws IOException, ServletException {

        long startTime = System.currentTimeMillis();

        HttpServletRequest httpServletRequest =
                (HttpServletRequest) servletRequest;

        HttpServletResponse httpServletResponse =
                (HttpServletResponse) servletResponse;

        String requestId = UUID.randomUUID().toString();

        httpServletResponse.setHeader("X-Request-ID", requestId);

        // Request log
        System.out.println("Incoming Request"
                + httpServletRequest.getMethod() + " "
                + httpServletRequest.getRequestURI()
        );

        try {
            filterChain.doFilter(servletRequest, servletResponse);
        }
        finally {

            // Response Time calculation
            long endTime = System.currentTimeMillis();
            long duration = endTime - startTime;

            System.out.println("Response Status: "
                    + httpServletResponse.getStatus()
            );

            System.out.println("API response time: " + duration);
        }


    }
}
