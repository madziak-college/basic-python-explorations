class BankAccount:
    def __init__(self, initial_balance: float):
        self._balance = initial_balance

    @property
    def balance(self) -> float:
        """Read-only access to balance."""
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

account = BankAccount(100)
print(account.balance)  # 100

# account.balance = 200  # Raises AttributeError: can't set attribute
