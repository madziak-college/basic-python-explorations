class BankAccount:
    def __init__(self, balance: float):
        self._balance = balance  # Intended as private by convention

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount

    def get_balance(self) -> float:
        return self._balance

# Example usage:
account = BankAccount(100.0)
account.deposit(50.0)
print(account.get_balance())  # Output: 150.0

# but of course we can still access the "private" attribute directly (not recommended):
print(account._balance)  # Output: 150.0

# and just to see naming:
print(account.__dict__)
"""
"""