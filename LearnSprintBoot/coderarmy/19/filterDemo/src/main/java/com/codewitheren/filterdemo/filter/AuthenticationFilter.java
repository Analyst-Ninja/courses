package com.codewitheren.filterdemo.filter;

import jakarta.servlet.*;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.core.annotation.Order;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
@Order(1)
public class AuthenticationFilter implements Filter {

    @Override
    public void doFilter(
            ServletRequest servletRequest,
            ServletResponse servletResponse,
            FilterChain filterChain
    )
            throws IOException, ServletException {

        HttpServletRequest httpServletRequest =
                (HttpServletRequest) servletRequest;

        HttpServletResponse httpServletResponse =
                (HttpServletResponse) servletResponse;

        String token = httpServletRequest.getHeader("token");
        String apiKey = httpServletRequest.getHeader("X-api-key");

        if (token == null || !token.equals("1234")) {
            httpServletResponse.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            return;
        }

        if (apiKey == null || !(apiKey.equals("secret123"))) {
            httpServletResponse.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
            httpServletResponse.setContentType("application/json");
            httpServletResponse.getWriter().write(
                         "{\n" +
                            "     \"message\" : \"Invalid or missing API key\"" +
                            "}"
            );
            return;
        }

        filterChain.doFilter(servletRequest, servletResponse);
    }
}
