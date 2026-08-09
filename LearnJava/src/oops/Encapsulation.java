package oops;
import oops.bank.Bank;

public class Encapsulation {
    public void main() {
        Bank b1 = new Bank();
        b1.bankname = "BoA";

        System.out.println(b1.bankname);
        System.out.println(b1);
    }
}