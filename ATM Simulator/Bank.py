from Customer import Customer

class Bank:
    def __init__(self):
        self.customers = []
        cust = Customer(111234, 8317)
        self.customers.append(cust)

    #def readCustomers(self, filename):

    def addCustomer(self, c):
        self.customers.append(c)


    def findCustomer(self, aNumber):
        for c in self.customers:
            if c.match(aNumber):
                return c
        return None

    
