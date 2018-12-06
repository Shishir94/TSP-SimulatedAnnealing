import pandas
import math
import random
import numpy as np
from data import *
from simulatedAnnealing import *
from helperFunctions import *

if __name__ == '__main__':
    df,optimalCost,initialCost = dataInitialization()
    print(df)
    simulateAnnealing(df, optimalCost, initialCost)
