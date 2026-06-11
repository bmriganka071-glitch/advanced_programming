package banking;

import java.util.ArrayList;
import java.util.List;

/**
 * Driver class – demonstrates:
 *   • Constructor overloading / chaining
 *   • Encapsulation  (all field access via getters/setters)
 *   • Inheritance    (SavingsAccount, CurrentAccount extends Account)
 *   • Polymorphism   (Account reference list → dynamic dispatch on display())
 *   • Validation     (IllegalArgumentException / IllegalStateException)
 */
public class BankingDemo {

    public static void main(String[] args) {

        // ── 1. Create accounts (shows both constructors for each class) ──────
        SavingsAccount savings1 = new SavingsAccount("SAV-1001", "Aarav Sharma", 15000.00, 0.05);
        SavingsAccount savings2 = new SavingsAccount("SAV-1002", "Priya Nair",   8000.00);      // default 3.5 %

        CurrentAccount current1 = new CurrentAccount("CUR-2001", "Rohit Das",  25000.00, 10000.00);
        CurrentAccount current2 = new CurrentAccount("CUR-2002", "Meena Iyer",  5000.00);       // no overdraft

        // ── 2. Operations on SavingsAccount ─────────────────────────────────
        System.out.println("\n══════════  SAVINGS ACCOUNT OPERATIONS  ══════════");
        savings1.deposit(5000);
        savings1.withdraw(2000);
        savings1.applyInterest();

        savings2.deposit(3000);
        savings2.applyInterest();

        // ── 3. Operations on CurrentAccount ─────────────────────────────────
        System.out.println("\n══════════  CURRENT ACCOUNT OPERATIONS  ══════════");
        current1.deposit(1000);
        current1.withdraw(30000);      // uses overdraft (balance goes to -4000)

        current2.deposit(500);

        // ── 4. Polymorphism – store everything in an Account list ────────────
        List<Account> allAccounts = new ArrayList<>();
        allAccounts.add(savings1);
        allAccounts.add(savings2);
        allAccounts.add(current1);
        allAccounts.add(current2);

        System.out.println("\n══════════  ACCOUNT STATEMENTS (polymorphic display)  ══════════");
        for (Account account : allAccounts) {
            account.display();   // dynamic dispatch → correct override called
            System.out.println();
        }

        // ── 5. Validation / error-handling demo ──────────────────────────────
        System.out.println("══════════  VALIDATION DEMO  ══════════");
        testValidation(savings1, current2);
    }

    /** Shows that invalid operations throw meaningful exceptions. */
    private static void testValidation(SavingsAccount savings, CurrentAccount current) {

        // 5a. Negative deposit
        try {
            savings.deposit(-500);
        } catch (IllegalArgumentException e) {
            System.out.println("[OK] Caught negative deposit   → " + e.getMessage());
        }

        // 5b. Withdraw more than balance (no overdraft)
        try {
            current.withdraw(99999);
        } catch (IllegalStateException e) {
            System.out.println("[OK] Caught overdraft breach    → " + e.getMessage());
        }

        // 5c. Invalid interest rate
        try {
            savings.setInterestRate(1.5);   // > 100 % is invalid
        } catch (IllegalArgumentException e) {
            System.out.println("[OK] Caught bad interest rate   → " + e.getMessage());
        }

        // 5d. Blank account owner name
        try {
            savings.setOwnerName("   ");
        } catch (IllegalArgumentException e) {
            System.out.println("[OK] Caught blank owner name    → " + e.getMessage());
        }

        // 5e. assert – enabled with JVM flag -ea
        assert savings.getBalance() > 0 : "Balance should be positive after operations";
        System.out.println("[OK] assert passed – balance is positive.");
    }
}
