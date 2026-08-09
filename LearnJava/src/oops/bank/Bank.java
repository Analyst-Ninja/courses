package oops.bank;

class Account {
    public String name;
    protected String email;
    private String password = "Default Password";

    // getters and setters
    // getter
    public String getPassword() {
        return this.password;
    }

    // setter
    public void setPassword(String pass) {
        this.password = pass;
        System.out.println("Password set successfully");
    }
}

public class Bank {

    public String bankname;

    public static void main() {
        Account acc1 = new Account();
        acc1.name = "bytehub";
        acc1.email = "bytehub@gmail.com";
        // acc1.password = "password" // not allowed as it is private

        // calling getter
        System.out.println(acc1.getPassword());

        // calling setter
        acc1.setPassword("New Password");

        // calling getter again for new password
        System.out.println(acc1.getPassword());

    }
}
