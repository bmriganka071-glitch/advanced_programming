package banking;

/**
 * Base class representing a generic bank account.
 * Demonstrates: encapsulation, constructor chaining, basic validation.
 */
public class Account {

    // ── Private fields (encapsulation) ─────────────────────────────────────
    private final String accountNumber;
    private String ownerName;
    private double balance;

    // ── Constructor 1 (primary – all fields) ───────────────────────────────
    public Account(String accountNumber, String ownerName, double initialBalance) {
        if (accountNumber == null || accountNumber.isBlank())
            throw new IllegalArgumentException("Account number must not be blank.");
        if (ownerName == null || ownerName.isBlank())
            throw new IllegalArgumentException("Owner name must not be blank.");
        if (initialBalance < 0)
            throw new IllegalArgumentException("Initial balance cannot be negative.");

        this.accountNumber = accountNumber;
        this.ownerName     = ownerName;
        this.balance       = initialBalance;
    }

    // ── Constructor 2 (convenience – zero balance) – chains to primary ──────
    public Account(String accountNumber, String ownerName) {
        this(accountNumber, ownerName, 0.0);   // constructor chaining via this(...)
    }

    // ── Getters / Setters ───────────────────────────────────────────────────
    public String getAccountNumber() { return accountNumber; }

    public String getOwnerName()     { return ownerName; }
    public void   setOwnerName(String ownerName) {
        if (ownerName == null || ownerName.isBlank())
            throw new IllegalArgumentException("Owner name must not be blank.");
        this.ownerName = ownerName;
    }

    public double getBalance()       { return balance; }

    // balance is only changed via deposit / withdraw (no public setter)

    // ── Core operations ─────────────────────────────────────────────────────

    /**
     * Deposits a positive amount into the account.
     *
     * @param amount the amount to deposit (must be > 0)
     */
    public void deposit(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Deposit amount must be positive.");
        balance += amount;
        System.out.printf("  [Deposit]  %-12s  +%.2f  →  Balance: %.2f%n",
                accountNumber, amount, balance);
    }

    /**
     * Withdraws an amount from the account.
     * Sub-classes may override to relax or tighten this rule.
     *
     * @param amount the amount to withdraw (must be > 0 and ≤ balance)
     */
    public void withdraw(double amount) {
        if (amount <= 0)
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        if (amount > balance)
            throw new IllegalStateException(
                    String.format("Insufficient funds. Available: %.2f, Requested: %.2f",
                                  balance, amount));
        balance -= amount;
        System.out.printf("  [Withdraw] %-12s  -%.2f  →  Balance: %.2f%n",
                accountNumber, amount, balance);
    }

    /**
     * Protected helper so sub-classes can adjust the balance directly
     * (e.g., apply interest) without violating encapsulation at the public API.
     */
    protected void adjustBalance(double delta) {
        this.balance += delta;
    }

    // ── Display ─────────────────────────────────────────────────────────────

    /**
     * Prints a summary of the account.  Sub-classes override this to add
     * type-specific details while reusing the base output via super.display().
     */
    public void display() {
        System.out.println("┌─────────────────────────────────────────┐");
        System.out.printf( "│  Account  : %-29s│%n", accountNumber);
        System.out.printf( "│  Owner    : %-29s│%n", ownerName);
        System.out.printf( "│  Balance  : ₹%-28.2f│%n", balance);
    }
}
