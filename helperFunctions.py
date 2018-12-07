import pandas
import math
import random
import matplotlib.pyplot as plt
import numpy as np
from data import *

"""def plot_cities(df):
    plt.pause(0.01)
    plt.clf()
    plt.plot(df[:]['x'], df[:]['y'])
    plt.show()
    plt.pause(0.01)
    plt.clf()"""


def costFunction(dfNew):
    """
    This accepts the current data frame as it is along with the euclidean
    distances between the points and returns the current cost of traversal
    """
    reCalc = 0
    for i in range(1,len(dfNew)):
        reCalc += euclideanDistance(dfNew.ix[i]['x'],dfNew.ix[i]['y'],dfNew.ix[i+1]['x'],dfNew.ix[i+1]['y'])
    return reCalc

def calculateDistances(df):
    """
    This functions accepts the data set and calculates the distance between
    each city and stores it in a matrix.
    (NOT SURE IF THIS FUNCTION IS REQUIRED...)
    """
    return

def selectCities(x,y):
    a = random.randrange(x, y, 1)
    b = random.randrange(x, y, 1)
    #a = np.random.randint(x,y)
    #b = np.random.randint(x,y)
    #Loop to ensure the two randomly selected cities are different.
    while a == b:
        b = random.randrange(x, y, 1)
        #b = np.random.randint(x,y)
    return a,b

def newCostCalc(dfNew, curCost,a,b):
    """
    Function to calculate the traversal distance after switching two cities at random
    """
    a1,a2,a3 = dfNew.iloc[a-2],dfNew.iloc[a-1],dfNew.iloc[a]
    b1,b2,b3 = dfNew.iloc[b-2],dfNew.iloc[b-1],dfNew.iloc[b]
    reCalc = curCost
    reCalc = reCalc - euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y'])
    reCalc = reCalc - euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y'])
    reCalc = reCalc - euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y'])
    reCalc = reCalc - euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y'])

    x, y = dfNew.iloc[a-1].copy(), dfNew.iloc[b-1].copy()
    dfNew.iloc[a-1],dfNew.iloc[b-1] = y,x

    a1,a2,a3 = dfNew.iloc[a-2],dfNew.iloc[a-1],dfNew.iloc[a]
    b1,b2,b3 = dfNew.iloc[b-2],dfNew.iloc[b-1],dfNew.iloc[b]

    reCalc = reCalc + euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y'])
    reCalc = reCalc + euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y'])
    reCalc = reCalc + euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y'])
    reCalc = reCalc + euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y'])

    x, y = dfNew.iloc[a-1].copy(), dfNew.iloc[b-1].copy()
    dfNew.iloc[a-1],dfNew.iloc[b-1] = y,x

    return reCalc

def acceptanceProbability(newCost, curCost, temperature):
        if(newCost < curCost):
            return 1.0
        else:
            return math.exp(((-(newCost - curCost))/temperature))

def euclideanDistance(x1,y1,x2,y2):
    """
    Calculate the euclidean distance whne given two points (x1,y1) & (x2,y2)
    """
    distance = math.sqrt(abs(math.pow((x2-x1),2)) + abs(math.pow((y2-y1),2)))
    return distance

def initialCostCalc(df):
    initialCost = 0
    for i in range(1,len(df)):
        initialCost += euclideanDistance(df.ix[i]['x'],df.ix[i]['y'],df.ix[i+1]['x'],df.ix[i+1]['y'])
    return initialCost

def dataInitialization():
    df,optimalCost = readData()
    return df, optimalCost
