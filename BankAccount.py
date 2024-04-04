class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостатньо коштів")
        else:
            self.balance -= amount

    def topup(self, amount):
        self.balance += amount

    def __str__(self):
        return f"Баланс вашого рахунку становить: {self.balance}"


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)
