# this file is made to design the nature of the agents 




import random 

class Agent:

	def __init__(self, id, role):
		self.id = id 
		self.role = role # where role can be seller(1) or buyer(2) 
		#self.WTA = 0 # willingness to accept
		#self.WTP = 0 # willingness to pay 
		self.WTA = random.randint(1, 10) # willingness to accept
		self.WTP = random.randint(1, 10) # willingness to pay 
		self.trade = False

		self.tradeHistory = []

	# Function to get the id
	def getId(self):
		return self.id

	# Function to set the WTA (was useful in testing)
	def setWTA(self, n):
		self.WTA = n

	# Function to set the WTP (was useful in testing)
	def setWTP(self, n):
		self.WTP = n

	# Function to get WTA
	def getWTA(self):
		return self.WTA

	# Function to get WTP
	def getWTP(self):
		return self.WTP

	# Function to update the flag for trade
	def setTrade(self, flag):
		self.trade = flag

	# Function to get the flag of trade
	def getTrade(self):
		return self.trade

	# Function to get the Trade History 
	def getTradeHistory(self):
		return self.tradeHistory

	# Identification of object (was useful in testing)
	def __str__(self):
		lines = []
		lines.append("*********************")
		lines.append("Id: " + str(self.id) + " Player is a " + str(self.role))
		if self.role == "Seller":
			lines.append("Willingness to accept = " + str(self.WTA))
		if self.role == "Buyer":
			lines.append("Willingness to pay = " + str(self.WTP))

		lines.append("*********************")
		return '\n'.join(lines)


	# Function to evaluate trade
	def evaluateTrade(self, partner):     #trade is evaluated from the seller perspective
		priceAccorded = 0
		if partner.WTP == self.WTA: # in case both have the same amounts
			priceAccorded = self.WTA 
			print("Success in trade! Price accorded between the seller with id S" + str(self.id) +" and buyer with id B" + str(partner.getId()) + " was: " + str(priceAccorded) + " $ with a WTA of: " + str(self.WTA) + " and a WTP of: " + str(partner.WTP))
			self.tradeHistory.append(partner.getId()) #id is added to the trade history 
			partner.tradeHistory.append(self.id)	

		elif partner.WTP > self.WTA: #trade with random value
			priceAccorded = random.randint(self.WTA, partner.WTP)
			print("Success in trade! Price accorded between the seller with id S" + str(self.id) +" and buyer with id B" + str(partner.getId()) + " was: " + str(priceAccorded) + " $ with a WTA of: " + str(self.WTA) + " and a WTP of: " + str(partner.WTP))
			self.tradeHistory.append(partner.getId())
			partner.tradeHistory.append(self.id)	#id is added to the trade history
		elif partner.WTP < self.WTA: #no trade
			print("Unsuccessful trade!")	
			self.tradeHistory.append(partner.getId())
			partner.tradeHistory.append(self.id)	#id is added to the trade history
		return priceAccorded





