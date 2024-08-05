# Write a program to simulate saving account processing in a bank using constructors. Create Deposit and Withdraw with other member function and Check for Validation while withdrawing the amount. 
# Raise the appropriate exceptions when depositing and withdrawing an incorrect mount. Display appropriate messages

class SavingAccount:
    def __init__(self,acc_no,acc_name,initial = 0):
        self.account_no = acc_no
        self.account_name = acc_name
        self.balance = initial
    def deposit(self,amount):
        if amount <= 0:
            raise Exception("Amount cannot be zero or negative")
        self.balance += amount
        print("Amount dposited")
    def withdraw(self,amount):
        if amount <= 0:
            raise Exception("Amount cannot be zero or negative ")
        if amount > self.balance:
            raise Exception("Insufficient funds ")
        self.balance -= amount
        print("Amount withdrawn")
    def showBalance(self):
        print(f"Available blanace {self.balance}")
    
a1 = SavingAccount(76968,"GH")
a1.deposit(900)

a1.withdraw(8999)
a1.display()



