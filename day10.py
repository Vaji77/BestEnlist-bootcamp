# 1.Banking concept-inheritance(Multilevel)
class Bank_Account:
    def __init__1(self):
        self.balance = 0
        print("Welcome to the Deposit & Withdrawal Machine")

    def display(self):
        print("Net Available Balance=", self.balance)


class Deposit(Bank_Account):
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print(amount, "Successfully Deposited")


class Withdraw(Deposit):
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient balance  ")


ob = Bank_Account()
ob.display()

ob1 = Withdraw()
ob1.deposit()
ob1.display()
ob1.withdraw()
ob1.display()