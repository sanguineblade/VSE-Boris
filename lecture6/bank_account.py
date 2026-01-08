class BankAccount:
    def __init__(self, accountNumber, owner, balans):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balans = balans
    
    def Deposit(self, amount):
        self.balans = self.balans + amount

    def Withdrawal(self, amount):
        if self.balans < amount:
            print("insufficient funds")
        else:
            self.balans = self.balans - amount

    def display(self):
        print(f"\nAccount Nubmer: {self.accountNumber}" )
        print(f"Account owner = {self.owner}")
        print(f"Account: {self.balans}\n")

newAccount = BankAccount(2178514584, "Mariq" , 2700)
newAccount.Withdrawal(300)
newAccount.Deposit(200)
newAccount.display()