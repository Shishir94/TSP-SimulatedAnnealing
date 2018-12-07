from main import *
from helperFunctions import *

class simulateAnnealingData():
    #Class defining the neccessary parameters for Simulated Annealing
    def __init__(self,temperature,epoch,alpha):
        self.temperature = temperature
        self.epoch = epoch
        self.alpha = alpha

def naiveHillClimbing(df,optimalCost,initialCost):
    print(initialCost)
    curCost = initialCost
    newCost = 0
    #Create a simulateAnnealingData object consisting of the parameter values
    saData = simulateAnnealingData(temperature=100, epoch = 10, alpha = 0.8)
    while(saData.temperature >= (1-saData.alpha)):
        print("Current Temperature = ",saData.temperature)
        print("Current Lowest Cost = ",curCost)
        print("...")

        for i in range(1,saData.epoch+1):
            a = random.randrange(2, len(df)-1, 1)
            b = random.randrange(2, len(df)-1, 1)
            while a == b:
                b = random.randrange(2, len(df)-1, 1)
            newCost = 0
            newCost = newCostCalc(df, curCost,a,b)
            if(newCost < curCost):
                curCost = newCost
                x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                df.iloc[a-1],df.iloc[b-1] = y,x
        saData.temperature *= saData.alpha
    #print(df)
    print(curCost)
    print("---------------")
    return

def simulateAnnealing(df,optimalCost, initialCost):
    """
    This function runs the simulated annealing procedure for the given
    dataset, along with the inital temperature and the cooling factor
    and the number of iterations for given temperature
    """
    print("Optimal Cost = ",optimalCost)
    print("initialCost = ", initialCost)
    curCost = initialCost
    newCost = 0
    #Create a simulateAnnealingData object consisting of the parameter values
    saData = simulateAnnealingData(temperature=100, epoch = 50, alpha = 0.99)
    while(saData.temperature >= (1-saData.alpha)):
        print("Current Temperature = ",saData.temperature)
        print("Current Lowest Cost = ",curCost)
        print("...")

        for i in range(1,saData.epoch+1):
            a = random.randrange(2, len(df)-1, 1)
            b = random.randrange(2, len(df)-1, 1)
            while a == b:
                b = random.randrange(2, len(df)-1, 1)
            newCost = 0
            newCost = newCostCalc(df, curCost,a,b)
            if(acceptanceProbability(newCost,curCost, saData.temperature) > np.random.uniform()):
                curCost = newCost
                x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                df.iloc[a-1],df.iloc[b-1] = y,x
                plt.plot(df[:]['x'], df[:]['y'])
                plt.draw()
                plt.pause(0.0001)
                plt.clf()
        saData.temperature *= saData.alpha
    #print(df)
    print(curCost)
    print("---------------")
    return
