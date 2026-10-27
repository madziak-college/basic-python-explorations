class BankAccount:
    def __init__(self, balance: float):
        self.__balance = balance  # Intended as private by convention

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self) -> float:
        return self.__balance

# Example usage:
account = BankAccount(100.0)
account.deposit(50.0)
print(account.get_balance())  # Output: 150.0

# But we cannot access the "private" attribute directly:
#print(account.__balance)  # This would raise an AttributeError
"""
That is, this would result in:

AttributeError: 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?
"""

# but let's see if we can see what the mangled name is:
print(account.__dict__)
"""
{'_BankAccount__balance': 150.0}
"""