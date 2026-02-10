class InsufficientBalance(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self, balance):
        return set.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, Total Balance: {self.balance}")

    def withdrawal(self, amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.balance}")
        else:
            raise InsufficientBalance("Insufficient balance. Minimum balance of 2000rs should remain. ")

acc = Account()
acc.set_balance(5000)

try:
    acc.deposit(2000)
    acc.withdrawal(3000)
    acc.withdrawal(2000)
except InsufficientBalance as e:
    print("exception", e)
