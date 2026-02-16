from time import sleep
from threading import Thread, Lock


class Account:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()     #ye apn ne lock add kiya

    def set_balance(self, balance):
        sleep(1)
        self.balance = balance

    def get_balance(self):
        sleep(1)
        return self.balance

    def deposit(self, amount):
        with self.lock:              #yaha lock laga diya
            bal = self.get_balance()
            self.set_balance(bal + amount)


class Racing(Thread):
    def __init__(self, account, name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range (5):
            self.account.deposit(100)
            print(self.name, self.account.get_balance())


def main_task():
    acc = Account()

    t1 = Racing(acc, 'abc')
    t2 = Racing(acc, 'xyz')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
main_task()