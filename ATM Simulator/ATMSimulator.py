from ATM import ATM
from Bank import Bank
from Customer import Customer


def main():
    #theATM = ATM()
    theBank = Bank()
    theATM = ATM(theBank)
    
    while(True):
        
        state = theATM.getState()
        if state == ATM.START:
            number = int(input("Enter Customer Number: "))
            theATM.setCustomerNumber(number)
            
        elif state == ATM.PIN:
            pin = int(input("Enter PIN: "))
            theATM.selectCustomer()            

        elif state == ATM.ACCOUNT:
            command = input("A=Checking, B=Savings, C=Quit: ")
            if command == 'A' or command == 'a':
                theATM.selectAccount(ATM.CHECKING)
            elif command == 'B' or command == 'b':
                theATM.selectAccount(ATM.SAVINGS)
            elif command == 'C' or command == 'c':
                theATM.reset()
            else:
                print("Illegal input!")
                
        elif state == ATM.TRANSACT:
            print("Ballance = " ,theATM.getBalance())
            command = input("A=Deposit, B=Withdraw, C=Cancel: ")
            if command == 'A' or command == 'a':
                amount = int(input("Amount: "))
                theATM.deposit(amount)
            elif command == 'B' or command == 'b':
                amount = int(input("Amount: "))
                theATM.withdraw(amount)
            elif command == 'C' or command == 'c':
                theATM.back()
            else:
                print("Illegal input!")
                
                
main()
