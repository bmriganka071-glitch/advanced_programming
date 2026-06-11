package banking;

/**
 * A current (checking) account that permits withdrawals up to an overdraft limit.
 * Demonstrates: inheritance, @Override, overriding business-logic in withdraw().
 */
public class CurrentAccount extends Account {

    private double overdraftLimit; // maximum amount by which balance may go negative

    // ── Constructor 1 (primary) ─────────────────────────────────────────────
    public CurrentAccount(String accountNumber, String ownerName,
                          double initialBalance, double overdraftLimit) {
        super(accountNumber, ownerName, initialBalance);   // chains to Account's primary ctor
        setOverdraftLimit(overdraftLimit);
    }

    // ── Constructor 2 (convenience – no overdraft) ──────────────────────────
    public CurrentAccount(String accountNumber, String ownerName, double initialBalance) {
        this(accountNumber, ownerName, initialBalance, 0.0); // constructor chaining via this(...)
    }

    // ── Getter / Setter ─────────────────────────────────────────────────────
    public double getOverdraftLimit() { return overdraftLimit; }

    public void setOverdraftLimit(double overdraftLimit) {
        if (overdraftLimit < 0)
            throw new IllegalArgumentException("Overdraft limit cannot be negative.");
        this.overdraftLimit = overdraftLimit;
    }

    // ── Overridden withdraw – respects overdraft limit ───────────────────────

    /**
     * Allows withdrawal as long as (balance - amount) ≥ -overdraftLimit.
     */
    @Override
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal amount must be positive.");

        double resultingBalance = getBalance() - amount;
        if (resultingBalance < -overdraftLimit)
            throw new IllegalStateException(
                    String.format(
                        "Overdraft limit exceeded. Available (incl. overdraft): %.2f, Requested: %.2f",
                        getBalance() + overdraftLimit, amount));

        adjustBalance(-amount);   // protected helper; avoids direct field access
        System.out.printf("  [Withdraw] %-12s  -%.2f  →  Balance: %.2f%n",
                getAccountNumber(), amount, getBalance());
    }

    // ── Display (overridden) ────────────────────────────────────────────────

    @Override
    public void display() {
        super.display();   // reuse base output
        System.out.printf( "│  Type     : %-29s│%n", "Current Account");
        System.out.printf( "│  Overdraft: ₹%-28.2f│%n", overdraftLimit);
        System.out.println("└─────────────────────────────────────────┘");
    }
}
