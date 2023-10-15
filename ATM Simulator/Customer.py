from BankAccount import BankAccount

class Customer:
    def __init__(self, customerNumber, pin):
        self.customerNumber = customerNumber
        self.pin = pin
        self.checkingAccount = BankAccount(100.0)
        self.savingsAccount = BankAccount(0.0)

    def getCheckingAccount(self):
        return self.checkingAccount

    def getSavingsAccount(self):
        return self.savingsAccount

    def match(self, aNumber):
        return aNumber == self.pin
    
