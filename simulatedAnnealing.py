from main import *
from helperFunctions import *

class simulateAnnealingData():
    def __init__(self,temperature,epoch,alpha):
        self.temperature = temperature
        self.epoch = epoch
        self.alpha = alpha

def simulateAnnealing(df,optimalCost, initialCost):
    """
    This function runs the simulated annealing procedure for the given
    dataset, along with the inital temperature and the cooling factor
    and the number of iterations for given temperature
    """
    curCost = initialCost
    print("Intial =",initialCost)
    print("-------------")
    newCost = 0

    saData = simulateAnnealingData(temperature=3, epoch = 50, alpha = 0.05)
    while(saData.temperature >= saData.alpha):
        for i in range(1,saData.epoch+1):
            a,b = selectCities(2,len(df)-1)
            newCost = newCostCalc(df, curCost,a,b)
            if(newCost < curCost):
                x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                df.iloc[a-1],df.iloc[b-1] = y,x
                curCost = newCost
                print(saData.temperature,i)
                print(a,b)
                print("newCost = ",newCost)
                print(df)
                print("--------------")
                print("--------------")
            else:
                if(acceptanceProbability(curCost, newCost, saData.temperature) > random.random()):
                    x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                    df.iloc[a-1],df.iloc[b-1] = y,x
                    curCost = newCost
                    print(saData.temperature,i)
                    print(a,b)
                    print("newCost = ",newCost)
                    print(df)
                    print("--------------")
                    print("--------------")
        return
        saData.temperature -= saData.alpha
    print(df)
    print(curCost)
    print("---------------")
    return





def simulateAnnealing1(df,optimalCost, initialCost):
    """
    This function runs the simulated annealing procedure for the given
    dataset, along with the inital temperature and the cooling factor
    and the number of iterations for given temperature
    """
    curCost = initialCost
    print("Intial =",initialCost)
    print("-------------")
    newCost = 0

    saData = simulateAnnealingData(temperature=3, epoch = 50, alpha = 0.05)
    while(saData.temperature >= saData.alpha):
        for i in range(1,saData.epoch+1):
            a,b = selectCities(2,len(df)-1)
            newCost = newCostCalc(df, curCost,a,b)
            if(newCost < curCost):
                x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                df.iloc[a-1],df.iloc[b-1] = y,x
                curCost = newCost
                print(saData.temperature,i)
                print(a,b)
                print("newCost = ",newCost)
                print(df)
                print("--------------")
                print("--------------")
            else:
                if(acceptanceProbability(curCost, newCost, saData.temperature) > random.random()):
                    x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                    df.iloc[a-1],df.iloc[b-1] = y,x
                    curCost = newCost
                    print(saData.temperature,i)
                    print(a,b)
                    print("newCost = ",newCost)
                    print(df)
                    print("--------------")
                    print("--------------")
        return
        saData.temperature -= saData.alpha
    print(df)
    print(curCost)
    print("---------------")
    return
