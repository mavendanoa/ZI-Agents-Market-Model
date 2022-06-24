from agent import Agent

import random

import matplotlib.pyplot as plt
import numpy as np

class Market:
	def __init__(self, numBuyers, numSellers):
		self.numBuyers = numBuyers
		self.numSellers = numSellers
		self.listBuyers = []
		self.listSellers = []
		self.setupBuyers()
		self.setupSellers()
		self.demandData = []
		self.supplyData = []
		self.avgPrice = []

		self.buyersWithTrade = []
		self.sellersWithTrade = []

		self.setupDemandCurve()
		self.setupSupplyCurve()

		self.demandData.sort(reverse=True)
		self.supplyData.sort()

		self.experimentDemand = []
		self.experimentSupply = []

		self.experimentSupplyExcedent = []
		self.experimentDemandExcedent = []



	# function to get experiment demand
	def getExperimentDemand(self):
		self.experimentDemand.sort(reverse=True)
		return self.experimentDemand


	# function to get experiment supply
	def getExperimentSupply(self):
		self.experimentSupply.sort()
		return self.experimentSupply

	# function to get the list of buyers
	def getBuyers(self):
		return self.listBuyers

	# function to get the list of sellers
	def getSellers(self):
		return self.listSellers

	# function to get the list of sellers
	def getTotalNumberOfPlayers(self):
		return self.totalNumberOfPlayers

	# function to get the list made of prices to get the avg price of the market
	def getAvgPriceList(self):
		return self.avgPrice


	# Identification of object (was useful in testing)
	def __str__(self):
		lines = []
		lines.append("*********************")
		lines.append("Number of buyers for this market: " + str(self.numBuyers))
		lines.append("Number of sellers for this market: " + str(self.numSellers))
		lines.append("Average price in this market: " + str(self.avgPrice))
		lines.append("Demand data in this market: " + str(self.demandData))
		lines.append("Supply data in this market: " + str(self.supplyData))


		lines.append("*********************")
		return '\n'.join(lines)

	# function to initialize the buyers
	def setupBuyers(self):
		for i in range(self.numBuyers):
			buyersObjects = Agent(i, "Buyer")
			self.listBuyers.append(buyersObjects)

	# function to initialize the sellers
	def setupSellers(self):
		for i in range(self.numSellers):
			sellersObjects = Agent(self.numBuyers + i, "Seller")
			self.listSellers.append(sellersObjects)

	# function to append the WTPs to the demand
	def setupDemandCurve(self):
		for i in range(self.numBuyers):
			self.demandData.append(self.listBuyers[i].WTP)

	# function to append the WTAs to the supply
	def setupSupplyCurve(self):
		for i in range(self.numSellers):
			self.supplyData.append(self.listSellers[i].WTA)

	# function to check if value already exists on a given list
	def duplicateCheck(self, listToBeChecked, number):
		exist_count = listToBeChecked.count(number)
		if exist_count > 0:
			return True
		else:
			return False

	# function to get the sellers ids that already have trade
	def getSellersWithTrade(self):
		return self.sellersWithTrade

	# function to get the buyers ids already have trade
	def getBuyersWithTrade(self):
		return self.buyersWithTrade

	# function to choose a random element from a list
	def randomPicker(self, listToRandom):
		playerToBeCheck = random.choice(listToRandom)
		return playerToBeCheck

	# function to get the demand curve 
	def getDemandCurve (self):
		return self.demandData

	# function to get the supply curve 
	def getSupplyCurve (self):
		return self.supplyData

	

	# function for the market analysis
	def tradeCenter3(self):
		possibleBuyers = list(filter(lambda a: a.trade == False, self.listBuyers)) # creates two list to loop through 
		possibleSellers = list(filter(lambda a: a.trade == False, self.listSellers))
		lenOfAnalysis = (len(possibleBuyers)*len(possibleSellers)) #max quantity of possible trades to be evaluated 
		i = 0
		while i < lenOfAnalysis:
		#while i < 6:
			if len(possibleBuyers) and len(possibleSellers) != 0:
				sellerToBeChecked = self.randomPicker(possibleSellers) #picks random agents
				buyerToBeChecked = self.randomPicker(possibleBuyers)
				# print("*************************************", "\n")
				# print("This list has been checked for time #: " + str(i))

				# print("The buyer to be checked is: ", buyerToBeChecked.__repr__())
				# print("The seller to be checked is: ", sellerToBeChecked.__repr__(), "\n")

				result = self.duplicateCheck(sellerToBeChecked.getTradeHistory(), buyerToBeChecked.getId())# checks if the choosen agents have no history  
				if result != True:
					print("This is trade #: " + str(i+1) + " in this experiment.")
					checkedSeller = sellerToBeChecked
					checkedBuyer = buyerToBeChecked

					#print(result, "\n")

					price = checkedSeller.evaluateTrade(checkedBuyer) #evaluates trades

					if price != 0:
						self.avgPrice.append(price)
						checkedBuyer.setTrade(True) #updates status of agents
						checkedSeller.setTrade(True)

						# adds willingness for experiment demand and supply
						self.experimentDemand.append(checkedBuyer.getWTP())
						self.experimentSupply.append(checkedSeller.getWTA())

						#thisTradeExcedentForSupply = checkedBuyer.getWTA() - price
						#print("This was the excedent for the trade: ", thisTradeExcedentForSupply)


						print("This was the supply excedent: ",  price - checkedSeller.getWTA())
						print("This was the demand excedent: ", checkedBuyer.getWTP() - price)

						self.experimentSupplyExcedent.append(price - checkedSeller.getWTA())
						self.experimentDemandExcedent.append(checkedBuyer.getWTP() - price)

						self.sellersWithTrade.append(checkedSeller.getId()) #updates list of agents with trade
						self.buyersWithTrade.append(checkedBuyer.getId())

						# update lists
						possibleBuyers = list(filter(lambda a: a.trade == False, self.listBuyers))
						possibleSellers = list(filter(lambda a: a.trade == False, self.listSellers))

						# print("This are the remaining possible buyers: ", possibleBuyers)
						# print("This are the remaining possible sellers: ", possibleSellers, "\n")
						# print("This was the buyer  taken out: ", checkedBuyer.__repr__)
						# print("This was the seller  taken out: ", checkedSeller.__repr__)
						# print("*************************************", "\n")
					# else:
					# print("This are the remaining possible buyers: ", len(possibleBuyers))
					# print("This are the remaining possible sellers: ", len(possibleSellers), "\n")


			else:
				print("No more values to look for, market is empty.")

			i = i + 1




	# function to get experiment supply excedent
	def getExperimentSupplyExcedent(self):
		return self.experimentSupplyExcedent


	# function to get experiment supply excedent
	def getExperimentDemandExcedent(self):
		return self.experimentDemandExcedent




	# function that returns the avg value of the market as a rounded number
	def avgPriceFunction(self):
		if len(self.avgPrice) != 0:
			avgPriceForTheMarket = round(sum(self.avgPrice) / len(self.avgPrice), 2)
			#print(avgPriceForTheMarket)
			return avgPriceForTheMarket
		else:
			return 0

"""
a = Market(4, 4)

a.tradeCenter3()

print("This are the buyers id's with trade: ", a.getBuyersWithTrade())
print("This are the sellers id's with trade: ", a.getSellersWithTrade())
print("This was the avg price for the market: ", a.avgPriceFunction())
print("This was the demand excedent in the experiment: ", sum(a.getExperimentDemandExcedent()))
print("This was the supply excedent in the experiment: ", sum(a.getExperimentSupplyExcedent()))


demandExperimento = a.getExperimentDemand()
supplyExperimento = a.getExperimentSupply()


demanda = a.getDemandCurve()
oferta = a.getSupplyCurve()


quantity = np.linspace(0, 4, 4)

quantityExperiment = np.linspace(0, len(demandExperimento), len(demandExperimento))

#plotting 

fig, ax = plt.subplots()

fig, ax2 = plt.subplots()

ax.step(quantity, demanda, 'dodgerblue', quantity, oferta, 'red')
ax2.step( quantityExperiment, demandExperimento, 'blue', quantityExperiment, supplyExperimento, 'y')
#ax.xlabel('Quantity (Q)')
#ax._label('Price (P)')

plt.show()
"""