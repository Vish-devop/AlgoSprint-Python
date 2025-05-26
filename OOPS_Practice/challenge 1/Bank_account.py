'''
Problem Statement:
Create a BankAccount class with:

Attributes: account_holder, balance

Methods:
deposit(amount)
withdraw(amount) (if balance >= amount)
check_balance()

Bonus: Prevent negative balances.

'''
class BankAccount: 
    def __init__(self,account_holder, balance): 
        self.account_holder=account_holder
        self.balance = balance 

    def deposit(self, amount): 
        if amount>0: 
            self.balance+=amount
            print(f"Deposited Rs-{amount}. New Balance: Rs-{self.balance}")
        else: 
            print("Enter a valid deposit amount")

    def withdraw(self,amount): 
        if amount>self.balance: 
            print("Insufficient Balance")
        elif amount<=0: 
            print("Enter a valid amount")
        else: 
            self.balance-=amount
            print(f"Withdraw Rs-{amount}. New balance: Rs-{self.balance}")

    def check_balance(self): 
        print(f"Current balance: Rs-{self.balance}")

if __name__=="__main__": 
    bankaccount = BankAccount("Amit", 1000)
    print("-----------------------")
    bankaccount.check_balance()
    bankaccount.deposit(500)
    bankaccount.withdraw(200)
    bankaccount.check_balance()