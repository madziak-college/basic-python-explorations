def create_bank_account(initial_balance: float):
    # 'balance' is strictly hidden inside the closure's scope
    balance = initial_balance

    def deposit(amount: float) -> float:
        nonlocal balance
        if amount > 0:
            balance += amount
        return balance

    def get_balance() -> float:
        return balance

    # Return a dict (or custom object) exposing only public methods
    return {
        "deposit": deposit,
        "get_balance": get_balance
    }

account = create_bank_account(100)
account["deposit"](50)

print(account["get_balance"]())  # Output: 150

# NOTE: There is no attribute on 'account' or way to 
# inspect 'balance' directly.
