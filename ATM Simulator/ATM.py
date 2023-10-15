from BankAccount import BankAccount
from Bank import Bank
from Customer import Customer

class ATM:
    CHECKING = 1
    SAVINGS = 2
    START = 1
    PIN = 2
    ACCOUNT = 3
    TRANSACT = 4
    
    def __init__(self, aBank):
        self.theBank = aBank
        self.currentAccount = None
        self.customerNumber = None
        self.currentCustomer = Customer(111234, 8317)
        self.state = None
        self.reset()

    def reset(self):
        self.customerNumber = -1
        currentAccount = None
        self.state = ATM.START

    def withdraw(self, value):
        self.currentAccount.withdraw(value)

    def deposit(self, value):
        self.currentAccount.deposit(value)
    
    def setCustomerNumber(self, number):
        self.customerNumber = number
        self.state = ATM.PIN

    def selectCustomer(self):
        #self.currentCustomer = self.theBank.findCustomer(self.customerNumber)
        self.currentCustomer = Customer(1234,8317)
        if self.currentCustomer == None:
            self.state = ATM.START
        else:
            self.state = ATM.ACCOUNT

    def selectAccount(self, account):
        if account == ATM.CHECKING:
            self.currentAccount = self.currentCustomer.getCheckingAccount()
        else:
            self.currentAccount = self.currentCustomer.getSavingsAccount()
        self.state = ATM.TRANSACT
            

    def getBalance(self):
        return self.currentAccount.getBalance()

    def back(self):
        if self.state == ATM.TRANSACT:
            self.state = ATM.ACCOUNT
        elif self.state == ATM.ACCOUNT:
            self.state = ATM.PIN
        elif self.state == ATM.PIN:
            self.state = ATM.START
        
    
    def getState(self):
        return self.state
        
