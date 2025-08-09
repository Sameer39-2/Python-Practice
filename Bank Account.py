class Bank_Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit: {amount}, New Balance: {self.balance}")
        else:
            print("Deopist must be positive.")
    def withdraw(self,amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withrawal: {amount}, New Balance: {self.balance}")
            else:
                print("Withdrawal exceed the current balance.")
        else:
            print("Withdrawal must be positive")
        
    def display(self):
        print(f"Owner: {self.owner} \nBalance = {self.balance}")


amount = Bank_Account("John", 2300)

amount.deposit(700)
amount.withdraw(500)
amount.withdraw(3000)

amount.display()