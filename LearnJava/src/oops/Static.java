package oops;

class CoachingStudent {
    String name;
    static String coachingName; // With Static keywork we can define class variables and functions

    public static void changeCoaching() {
        coachingName = "New Coaching";
    }
}

public class Static {
    public static void main() {
        CoachingStudent.coachingName = "ABC Coaching"; // Since static variable, it can be modified by using class itself
        CoachingStudent cs = new CoachingStudent();
        cs.name = "Tony";
        // cs.coachingName = "New Coaching"; // Modified for all objects from CoachingStudent class

        System.out.println(cs.name);
        System.out.println(cs.coachingName);

        CoachingStudent.changeCoaching();

        CoachingStudent cs2 = new CoachingStudent();
        System.out.println(cs2.coachingName);

    }
}