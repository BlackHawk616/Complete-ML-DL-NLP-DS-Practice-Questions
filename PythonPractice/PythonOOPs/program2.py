# Create a BankAccount class with methods for deposit, withdrawal, and balance inquiry. Handle invalid transactions.


class BankAccount:
    def __init__(self, account_holder, inital_balance=0):
        self.account_holder = account_holder
        self.balance = inital_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Withdrawal denied.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def balance_inquiry(self):
        print(f"Current balance: {self.balance}")

bank = BankAccount("John Doe", 1000)
bank.deposit(500)
bank.withdraw(200)
bank.balance_inquiry()