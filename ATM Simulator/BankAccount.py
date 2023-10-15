class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, ammount):
        self.balance += ammount
        
    def getBalance(self):
        return self.balance
    
    def withdraw(self, ammount):
        self.balance -= ammount
