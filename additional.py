def newCostCalc(dfNew, curCost,a,b):
    """
    Function to calculate the traversal distance after switching two cities at random
    """
    a1,a2,a3 = dfNew.iloc[a-2],dfNew.iloc[a-1],dfNew.iloc[a]
    b1,b2,b3 = dfNew.iloc[b-2],dfNew.iloc[b-1],dfNew.iloc[b]

    print("Points Swap := ")
    print(a1,"\n",a2,"\n",a3)
    print(b1,"\n",b2,"\n",b3)
    """
    #a1 = [dfNew.ix[a-1]['x'],dfNew.ix[a-1]['y']]
    #a2 = [dfNew.ix[a]['x'],dfNew.ix[a]['y']]
    #a3 = [dfNew.ix[a+1]['x'],dfNew.ix[a+1]['y']]
    #b1 = [dfNew.ix[b-1]['x'],dfNew.ix[b-1]['y']]
    b2 = [dfNew.ix[b]['x'],dfNew.ix[b]['y']]
    b3 = [dfNew.ix[b+1]['x'],dfNew.ix[b+1]['y']]
    recalc = curCost
    """

    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print(a,b)
    reCalc = curCost
    print("Cost = ",curCost)
    print("a1a2 =",euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y']))
    reCalc = reCalc - euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y'])
    print("a2a3 =",euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y']))
    reCalc = reCalc - euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y'])
    print("b1b2 =",euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y']))
    reCalc = reCalc - euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y'])
    print("b2b3 =",euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y']))
    reCalc = reCalc - euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y'])
    print("New Cost after reducing = ", reCalc)

    x, y = dfNew.iloc[a-1].copy(), dfNew.iloc[b-1].copy()
    dfNew.iloc[a-1],dfNew.iloc[b-1] = y,x

    a1,a2,a3 = dfNew.iloc[a-2],dfNew.iloc[a-1],dfNew.iloc[a]
    b1,b2,b3 = dfNew.iloc[b-2],dfNew.iloc[b-1],dfNew.iloc[b]
    print("Points Swap := ")
    print(a1,"\n",a2,"\n",a3)
    print(b1,"\n",b2,"\n",b3)

    print("a1a2 =",euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y']))
    reCalc = reCalc + euclideanDistance(a1['x'],a1['y'],a2['x'],a2['y'])
    print("a2a3 =",euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y']))
    reCalc = reCalc + euclideanDistance(a2['x'],a2['y'],a3['x'],a3['y'])
    print("b1b2 =",euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y']))
    reCalc = reCalc + euclideanDistance(b1['x'],b1['y'],b2['x'],b2['y'])
    print("b2b3 =",euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y']))
    reCalc = reCalc + euclideanDistance(b2['x'],b2['y'],b3['x'],b3['y'])

    x, y = dfNew.iloc[a-1].copy(), dfNew.iloc[b-1].copy()
    dfNew.iloc[a-1],dfNew.iloc[b-1] = y,x
    """
    print("a1b2 =",euclideanDistance(a1['x'],a1['y'],b2['x'],b2['y']))
    reCalc = reCalc + euclideanDistance(a1['x'],a1['y'],b2['x'],b2['y'])

    print("b2a3 =",euclideanDistance(b2['x'],b2['y'],a3['x'],a3['y']))
    reCalc = reCalc + euclideanDistance(b2['x'],b2['y'],a3['x'],a3['y'])

    print("b1a2 =",euclideanDistance(b1['x'],b1['y'],a2['x'],a2['y']))
    reCalc = reCalc + euclideanDistance(b1['x'],b1['y'],a2['x'],a2['y'])

    print("a2b3 =",euclideanDistance(a2['x'],a2['y'],b3['x'],b3['y']))
    reCalc = reCalc + euclideanDistance(a2['x'],a2['y'],b3['x'],b3['y'])
    """
    print("New Cost after increasing = ", reCalc)
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    return reCalc


def simulateAnnealing(df,optimalCost, initialCost):
    """
    This function runs the simulated annealing procedure for the given
    dataset, along with the inital temperature and the cooling factor
    and the number of iterations for given temperature
    """
    curCost = initialCost
    newCost = 0
    #Create a simulateAnnealingData object consisting of the parameter values
    saData = simulateAnnealingData(temperature=3, epoch = 50, alpha = 0.05)
    while(saData.temperature >= saData.alpha):
        print("-------------")
        #print(saData.temperature)
        for i in range(1,saData.epoch+1):
            print("index = ",i)
            a,b = selectCities(2,len(df)-1)
            #dfNew = None
            #dfNew = df.copy(deep = True)
            #x, y = dfNew.iloc[a-1].copy(), dfNew.iloc[b-1].copy()
            #dfNew.iloc[a-1],dfNew.iloc[b-1] = y,x
            #newCost = costFunction(dfNew)
            newCost = 0
            newCost = newCostCalc(df, curCost,a,b)
            if(acceptanceProbability(newCost,curCost, saData.temperature) > np.random.uniform()):
                curCost = newCost
                x, y = df.iloc[a-1].copy(), df.iloc[b-1].copy()
                df.iloc[a-1],df.iloc[b-1] = y,x
                print(saData.temperature,i)
                print(a,b)
                print("Cost using DF swapped = ", costFunction(df))
                #z = newCostCalc(df, curCost,a,b)
                print("newCost = ",newCost)
                print(df)
                print("--------------")
                print("--------------")
        saData.temperature -= saData.alpha
    print(df)
    print(curCost)
    print("---------------")
    return
