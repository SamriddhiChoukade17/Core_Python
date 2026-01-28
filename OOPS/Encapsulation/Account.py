class Account:
    count = 0

    def __init__(self):
        self.mobileNumber = input("Enter Mobile Number: ")
        self.name = input("Enter Name: ")
        self.accountType = input("Enter Account Type: ")
        self.balance = input("Enter Balance: ")

    def set_mobileNumber(self, mobileNumber):
        self.mobileNumber = mobileNumber

    def get_mobileNumber(self):
        return self.mobileNumber

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_account(self, accountType):
        self.accountType = accountType

    def get_account(self):
        return self.accountType

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance


a = Account()
print("\n\nHere are your account details",)
print("\nMobile Number: ", a.get_mobileNumber())
print("Name: ", a.get_name())
print("Account Type: ", a.get_account())
print("Balance: ", a.get_balance())

