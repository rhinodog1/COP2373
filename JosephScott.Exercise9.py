class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate  # annual interest rate (e.g., 0.05 for 5%)

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def deposit(self, amount):
        if amount > 0:
            self.amount += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.amount -= amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        # Simple interest formula: A = P * r * (days/365)
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def __str__(self):
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Interest Rate: {self.interest_rate * 100:.2f}%\n")


# Test function
def test_bank_account():
    print("=== Creating Account ===")
    acct = BankAcct("Joseph Scott", 123456, 1000.00, 0.05)
    print(acct)

    print("=== Deposit $500 ===")
    acct.deposit(500)
    print(acct)

    print("=== Withdraw $200 ===")
    acct.withdraw(200)
    print(acct)

    print("=== Adjust Interest Rate to 3% ===")
    acct.adjust_interest_rate(0.03)
    print(acct)

    print("=== Calculate Interest for 30 days ===")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: ${interest:.2f}")

    print("=== Final Account Info ===")
    print(acct)


# Run test
if __name__ == "__main__":
    test_bank_account()