import pandas
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from data import *
from simulatedAnnealing import *
from helperFunctions import *

def randomTour(df):
    dfNew = df.copy()
    arr = np.random.permutation(len(df))
    print(arr)
    j=0
    for i in range(2,len(df)-1):
        if(arr[j] == 0):
            j = j+1
        if(arr[j] == len(df)-1):
            j = j+1
        df.iloc[i] = dfNew.iloc[arr[j]+1]
        j = j+1
    return df

def plot_cities(df):
    plt.plot(df[:]['x'], df[:]['y'])
    plt.show()

if __name__ == '__main__':
    df,optimalCost = dataInitialization()
    df = randomTour(df)
    print(df)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*")
    initialCost = initialCostCalc(df)
    #plot_cities(df)
    simulateAnnealing(df, optimalCost, initialCost)
    plot_cities(df)
    #naiveHillClimbing(df, optimalCost, initialCost)
