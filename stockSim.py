import random, pylab

# Introduction Section
print( '''
This is a program for calculating the price of a number of stocks,
over a number of days. The stock price changes randomly, but can
be influenced by market bias and momentum.''') 
print() 

# Data Section
numStks = int(input("Enter the number of stocks to invest in: "))
numDays = int(input("Enter the number of days to invest: "))
stks1 = []
stks2 = []
bias = 0.0
mo = False

# Class Section
class Stock(object):
	
	def __init__(self, price, distribution):
		self.price = price
		self.distribution = distribution
		self.history = [price]
		self.lastChange = 0

	def setPrice(self, price):
		self.price = price
		self.history.append(price)

	def getPrice(self):
		return self.price

	def makeMove(self, mktBias, mo):
		oldPrice = self.price
		baseMove = self.distribution() + mktBias
		self.price *= (1.0 + baseMove)		
		if mo:
			self.price += random.gauss(-.5, .5)*self.lastChange
		if self.price <0.01:
			self.price = 0.0
		self.history.append(self.price)
		self.lastChange = oldPrice - self.price

	def showHistory(self, figNum):
		pylab.figure(figNum)
		pylab.plot(self.history)
		pylab.title("Stock Closing Price, Test " + str(figNum))
		pylab.xlabel("Days")
		pylab.ylabel("Price")
	

# Main Section
def main():

	def runSim(stks, fig, mo):
		totalClosingPrice = 0.0		
		for s in stks:
			for d in range(numDays):
				s.makeMove(bias, mo)
			s.showHistory(fig)			
			totalClosingPrice += s.getPrice()
		mean = totalClosingPrice / numStks
		pylab.axhline(mean)
		
	for i in range(numStks):
		volatility = random.uniform(0.0, 0.2)
		dist1 = lambda: random.uniform(-volatility, volatility)
		dist2 = lambda: random.gauss(0.0, volatility/2.0)
		stks1.append(Stock(100.0, dist1))
		stks2.append(Stock(100.0, dist2))

	runSim(stks1, 1, mo)
	runSim(stks2, 2, mo)

# Run Section 
main()
pylab.show()

