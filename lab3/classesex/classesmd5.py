class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} accepted. Balance is {self.balance}.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. Current balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


account = BankAccount("Nurik")


account.deposit(5000)
account.withdraw(4700)
account.withdraw(1000)  
account.deposit(-200)  
