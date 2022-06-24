from agent import Agent
from market import Market

import matplotlib.pyplot as plt
import numpy as np

# Market analysis for 150 buyers and 150 sellers
marketAnalysis2 = Market(150, 150)
marketAnalysis2.tradeCenter3()
print("This was the avg price for the market: ", marketAnalysis2.avgPriceFunction())
print("This was the number of trades made in the experiment: ", len(marketAnalysis2.getSellersWithTrade()))
print("This was the demand excedent in the experiment: ", sum(marketAnalysis2.getExperimentDemandExcedent()))
print("This was the supply excedent in the experiment: ", sum(marketAnalysis2.getExperimentSupplyExcedent()))

#Graph for the market
demandMarket2 = marketAnalysis2.getDemandCurve()
supplyMarket2 = marketAnalysis2.getSupplyCurve()

quantityMarket2 = np.linspace(0, 150, 150)

fig, market = plt.subplots()
plt.title('Given market')


market.step(quantityMarket2, demandMarket2, 'dodgerblue', quantityMarket2, supplyMarket2, 'red')
market.set_xlabel('Quantity(Q)')
market.set_xlabel('Price')


# Graph for the experiment
fig, experiment = plt.subplots()
plt.title('Market in the experiment')

demandExperiment = marketAnalysis2.getExperimentDemand()
supplyExperiment = marketAnalysis2.getExperimentSupply()

quantityExperiment = np.linspace(0, len(demandExperiment), len(demandExperiment))
experiment.step( quantityExperiment, demandExperiment, 'blue', quantityExperiment, supplyExperiment, 'y')
experiment.set_xlabel('Quantity(Q)')
experiment.set_xlabel('Price')



	



plt.show()




