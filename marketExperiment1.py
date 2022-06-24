from agent import Agent
from market import Market

import matplotlib.pyplot as plt
import numpy as np

# Market analysis for 2 buyers and 2 sellers
marketAnalysis1 = Market(2, 2)
marketAnalysis1.tradeCenter3()
print("This was the avg price for the market: ", marketAnalysis1.avgPriceFunction())
print("This was the number of trades made in the experiment: ", len(marketAnalysis1.getSellersWithTrade()))
print("This was the demand excedent in the experiment: ", sum(marketAnalysis1.getExperimentDemandExcedent()))
print("This was the supply excedent in the experiment: ", sum(marketAnalysis1.getExperimentSupplyExcedent()))

#Graph for the market
demandMarket1 = marketAnalysis1.getDemandCurve()
supplyMarket1 = marketAnalysis1.getSupplyCurve()

quantityMarket1 = np.linspace(0, 2, 2)

fig, market = plt.subplots()
plt.title('Given market')


market.step(quantityMarket1, demandMarket1, 'dodgerblue', quantityMarket1, supplyMarket1, 'red')
market.set_xlabel('Quantity(Q)')
market.set_xlabel('Price')


# Graph for the experiment
fig, experiment = plt.subplots()
plt.title('Market in the experiment')

demandExperiment = marketAnalysis1.getExperimentDemand()
supplyExperiment = marketAnalysis1.getExperimentSupply()

quantityExperiment = np.linspace(0, len(demandExperiment), len(demandExperiment))
experiment.step( quantityExperiment, demandExperiment, 'blue', quantityExperiment, supplyExperiment, 'y')
experiment.set_xlabel('Quantity(Q)')
experiment.set_xlabel('Price')



	



plt.show()




