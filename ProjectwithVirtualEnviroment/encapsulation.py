
#encapsulation 


class BankAccount:
    def __init__(self, balance):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 1000:
            self._balance += amount

    def get_balance(self):
        return self._balance  # Public method

account = BankAccount(1000)
account.deposit(1200)
print(f"Account balance: {account.get_balance()}")
