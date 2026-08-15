package com.codewitheren;

import com.codewitheren.config.WebConfig;
import org.apache.catalina.Context;
import org.apache.catalina.LifecycleException;
import org.apache.catalina.startup.Tomcat;
import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
import org.springframework.web.servlet.DispatcherServlet;

import java.io.File;

public class Main {
    public static void main(String[] args) throws LifecycleException {

        // Boiler Plate code

        Tomcat tomcat = new Tomcat();
        tomcat.setPort(8080);
        tomcat.getConnector();

        String contextPath = "" ;
        String baseDoc = new File("src/main/webapp").getAbsolutePath();

        Context context = tomcat.addContext(contextPath, baseDoc);

        // IOC Container
        AnnotationConfigWebApplicationContext springContext = new AnnotationConfigWebApplicationContext();
        springContext.register(WebConfig.class);

        // Dispatcher Servlet
        DispatcherServlet dispatcherServlet = new DispatcherServlet(springContext);

        // add servlet
        Tomcat.addServlet(context, "dispatcherServlet", dispatcherServlet);

        // add mapping handlings
        context.addServletMappingDecoded("/", "dispatcherServlet");

        tomcat.start();

        System.out.println("Tomcat Started on port 8080");

        // To keep server running
        tomcat.getServer().await();
    }
}