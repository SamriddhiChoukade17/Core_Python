class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account:
    def __init__(self):
        self.balance = 0
        self.count = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: {amount}, Current Balance: {self.balance}")

    def withdrawal(self, amount):
        if amount > 5000:
            raise InsufficientFundException(" You can't withdraw amount greater than 5k")

        if self.count < 3:
            raise InsufficientFundException("Your withdrawal count is greater than 2. So yoiu can't continue withdrawal.")

        if self.balance - amount >= 2000:
            self.balance -= amount
            self.count += 1
            print(f"Withdrew: {amount}, Remaining Balance: {self.balance}")
        else:
            raise InsufficientFundException("Insufficient balance. Minimum balance of 2000rs should remain. ")




acc = Account()
acc.set_balance(10000)

try:
     acc.withdrawal(6000)
     acc.withdrawal(500)
     acc.withdrawal(1000)
     acc.withdrawal(1000)
     acc.withdrawal(1000)


except InsufficientFundException as e:
    print("exception", e)
