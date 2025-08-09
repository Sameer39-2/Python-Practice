class Bank:
    Bank_name = "State Bank of India"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    
    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        print(f"Bank Name: {Bank.Bank_name}")

account = Bank("Lois", 7000)

account.display()