package banking;

/**
 * A savings account that earns interest.
 * Demonstrates: inheritance, constructor chaining via super(), @Override.
 */
public class SavingsAccount extends Account {

    private double interestRate; // annual rate, e.g. 0.04 = 4 %

    // ── Constructor 1 (primary) ─────────────────────────────────────────────
    public SavingsAccount(String accountNumber, String ownerName,
                          double initialBalance, double interestRate) {
        super(accountNumber, ownerName, initialBalance);   // chains to Account's primary ctor
        setInterestRate(interestRate);
    }

    // ── Constructor 2 (convenience – default 3.5 % interest) ───────────────
    public SavingsAccount(String accountNumber, String ownerName, double initialBalance) {
        this(accountNumber, ownerName, initialBalance, 0.035); // constructor chaining via this(...)
    }

    // ── Getter / Setter ─────────────────────────────────────────────────────
    public double getInterestRate() { return interestRate; }

    public void setInterestRate(double interestRate) {
        if (interestRate < 0 || interestRate > 1)
            throw new IllegalArgumentException("Interest rate must be between 0 and 1.");
        this.interestRate = interestRate;
    }

    // ── Business logic ──────────────────────────────────────────────────────

    /**
     * Applies simple annual interest to the current balance.
     */
    public void applyInterest() {
        double interest = getBalance() * interestRate;
        adjustBalance(interest);   // uses protected helper from Account
        System.out.printf("  [Interest] %-12s  +%.2f (%.1f%%)  →  Balance: %.2f%n",
                getAccountNumber(), interest, interestRate * 100, getBalance());
    }

    // ── Display (overridden) ────────────────────────────────────────────────

    @Override
    public void display() {
        super.display();   // reuse base output
        System.out.printf( "│  Type     : %-29s│%n", "Savings Account");
        System.out.printf( "│  Interest : %-28s│%n",
                String.format("%.2f%%", interestRate * 100));
        System.out.printf( "│  Interest : ₹%-28.2f│%n", getBalance() * interestRate);
        System.out.println("└─────────────────────────────────────────┘");
    }
}
