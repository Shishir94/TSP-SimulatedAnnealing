import pandas
import matplotlib.pyplot as plt

def plot_cities(df):
        plt.scatter(df['x'], df['y'])
        plt.show()

def parse_data(filename):
    df = pandas.read_csv(filename)
    optimal_cost = df['x'][0] #Gets the optimal route distance from the dataset
    df = df[:][1:] #considers all the points apart from the first element
    return optimal_cost, df

def read_data():
    filename = "canada.csv"
    optimal_cost, df = parse_data(filename)
    plot_cities(df)

read_data()
