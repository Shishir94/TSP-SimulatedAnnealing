import pandas
import math
import random
import numpy as np
from data import *

def costFunction(df, distanceMatrix):
    """
    This accepts the current data frame as it is along with the euclidean
    distances between the points and returns the current cost of traversal
    """
    return

def calculateDistances(df):
    """
    This functions accepts the data set and calculates the distance between
    each city and stores it in a matrix.
    (NOT SURE IF THIS FUNCTION IS REQUIRED...)
    """
    return

def selectCities(x,y):
    a = np.random.randint(x,y)
    b = np.random.randint(x,y)
    #Loop to ensure the two randomly selected cities are different.
    while a == b:
        b = np.random.randint(x,y)
    return a,b

def newCostCalc(df, curCost,a,b):
    """
    Function to calculate the traversal distance after switching two cities at random
    """

    a1 = [df.ix[a-1]['x'],df.ix[a-1]['y']]
    a2 = [df.ix[a]['x'],df.ix[a]['y']]
    a3 = [df.ix[a+1]['x'],df.ix[a+1]['y']]
    b1 = [df.ix[b-1]['x'],df.ix[b-1]['y']]
    b2 = [df.ix[b]['x'],df.ix[b]['y']]
    b3 = [df.ix[b+1]['x'],df.ix[b+1]['y']]
    recalc = curCost
    recalc -= (euclideanDistance(a1[0],a1[1],a2[0],a2[1]) + euclideanDistance(a2[0],a2[1],a3[0],a3[1]))
    recalc -= (euclideanDistance(b1[0],b1[1],b2[0],b2[1]) + euclideanDistance(b2[0],b2[1],b3[0],b3[1]))
    recalc += (euclideanDistance(a1[0],a1[1],b2[0],b2[1]) + euclideanDistance(b2[0],b2[1],a3[0],a3[1]))
    recalc += (euclideanDistance(b1[0],b1[1],a2[0],a2[1]) + euclideanDistance(a2[0],a2[1],b3[0],b3[1]))
    return recalc

def acceptanceProbability(newCost, curCost, temperature):
        return math.exp(((-(curCost - newCost))/temperature))

def euclideanDistance(x1,y1,x2,y2):
    """
    Calculate the euclidean distance whne given two points (x1,y1) & (x2,y2)
    """
    distance = math.sqrt(abs(math.pow((x2-x1),2)) + abs(math.pow((y2-y1),2)))
    return distance

def dataInitialization():
    df,optimalCost = readData()
    initialCost = 0
    for i in range(1,len(df)):
        initialCost += euclideanDistance(df.ix[i]['x'],df.ix[i]['y'],df.ix[i+1]['x'],df.ix[i+1]['y'])
    return df,optimalCost,initialCost
