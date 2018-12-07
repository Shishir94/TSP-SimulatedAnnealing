import pandas
import matplotlib.pyplot as plt

def parseData(filename):
    df = pandas.read_csv(filename)
    optimalCost = df['x'][0] #Gets the optimal route distance from the dataset
    df = df[:][1:] #considers all the points apart from the first element
    return optimalCost, df

def readData():
    filename = "custom.csv"
    optimalCost, df = parseData(filename)
    #plot_cities(df)
    return df,optimalCost
