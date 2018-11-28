import pandas
import math
from data import *

def cost_function(df, distance_matrix):
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

def simulateAnnealing(df,initial_cost):
    """
    This function runs the simulated annealing procedure for the given
    dataset, along with the inital temperature and the cooling factor
    and the number of iterations for given temperature
    """
    return

def euclideanDistance(x1,y1,x2,y2):
    """
    Calculate the euclidean distance whne given two points (x1,y1) & (x2,y2)
    """
    distance = math.sqrt(abs(math.pow((x2-x1),2)) + abs(math.pow((y2-y1),2)))
    return distance

if __name__ == '__main__':
    df,optimal_cost = read_data()
    initial_cost = 0
    for i in range(1,len(df)):
        initial_cost += euclideanDistance(df.ix[i]['x'],df.ix[i]['y'],df.ix[i+1]['x'],df.ix[i+1]['y'])
