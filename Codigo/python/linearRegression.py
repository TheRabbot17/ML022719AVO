import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, mean_absolute_error
import matplotlib.pyplot as plt
import constants as c
from  itertools import combinations

def splitData(trainCoef, testCoef, valCoef, dataset):
    datasetRows = np.shape(dataset)[0]
    
    trainRows = int(np.trunc(datasetRows*trainCoef))
    testRows = int(trainRows + np.trunc(datasetRows*testCoef))
    
    return(trainRows, testRows)

def plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred):
    plt.scatter(dataset_X_test, dataset_Y_test,  color='black')
    plt.plot(dataset_X_test, dataset_Y_pred, color='blue', linewidth=3)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def setResults(regr, dataset_Y_test, dataset_Y_pred, experiment):
    experiment = np.hstack((experiment, mean_squared_error(dataset_Y_test, dataset_Y_pred)))
    experiment = np.hstack((experiment, r2_score(dataset_Y_test, dataset_Y_pred)))
    experiment = np.hstack((experiment, mean_absolute_error(dataset_Y_test, dataset_Y_pred)))
    
    return(experiment)

def setColumnsDatasets(combination, isLocal):
    auxiliar =1
    if(isLocal):
        auxiliar = 0
        
    column = tuple(map(lambda x:x+5 + 29*auxiliar, combination))
    
    return(column)

def predictLocalPoints(trainRows, testRows, dataset):
    results = np.array([c.headersLinearRegression])
    allCombinations = getAllCombinations(dataset[:, 5:11])
    i = 0
    for combi in allCombinations:
        column = setColumnsDatasets(combi, True)
        experiment = np.array([i, dataset[0, column], dataset[0, 62]])
        dataset_X_train = dataset[2:trainRows, column]
        dataset_X_test = dataset[trainRows+2:testRows, column]
        #dataset_X_validate = dataset_X[testRows:, 14:15]
    
        dataset_Y_train = dataset[2:trainRows, 62]
        dataset_Y_test = dataset[trainRows+2:testRows, 62]
        #dataset_Y_validate = dataset_X[testRows:, 62:63]
        
        regr = linear_model.LinearRegression()
        regr.fit(dataset_X_train, dataset_Y_train)
        dataset_Y_pred = regr.predict(dataset_X_test)
        
        experiment = setResults(regr, dataset_Y_test, dataset_Y_pred, experiment)
        results = np.vstack((results, experiment))
        i += 1
    
    df = pd.DataFrame(results[1:], columns = c.headersLinearRegression).sort_values(by=['MSE'])
    df.to_excel('dataFinal/models/linear-regression/linear-regression-local.xlsx', index=False)
    print("Datos de los partidos como local predecidos correctamente.")
    print(dataset_Y_test[0], dataset_Y_pred[0])
    print(dataset_Y_test[1], dataset_Y_pred[1])
    print(dataset_Y_test[2], dataset_Y_pred[2])

def predictAwayPoints(trainRows, testRows, dataset):
    results = np.array([c.headersLinearRegression])
    allCombinations = getAllCombinations(dataset[:, 34:40])
    i = 0
    for combi in allCombinations:
        column = setColumnsDatasets(combi, False)
        experiment = np.array([i, dataset[0, column], dataset[0, 63]])
        dataset_X_train = dataset[2:trainRows, column]
        dataset_X_test = dataset[trainRows+2:testRows, column]
        #dataset_X_validate = dataset_X[testRows:, 14:15]
    
        dataset_Y_train = dataset[2:trainRows, 63]
        dataset_Y_test = dataset[trainRows+2:testRows, 63]
        #dataset_Y_validate = dataset_X[testRows:, 62:63]
        
        regr = linear_model.LinearRegression()
        regr.fit(dataset_X_train, dataset_Y_train)
        dataset_Y_pred = regr.predict(dataset_X_test)
        
        experiment = setResults(regr, dataset_Y_test, dataset_Y_pred, experiment)
        results = np.vstack((results, experiment))
        i += 1
    
    df = pd.DataFrame(results[1:], columns = c.headersLinearRegression).sort_values(by=['MSE'])
    df.to_excel('dataFinal/models/linear-regression/linear-regression-away.xlsx', index=False)
    print("Datos de los partidos como visitante predecidos correctamente.") 

def getAllCombinations(dataset):
    allCombinations = []
    df = pd.DataFrame(dataset)

    for lenValue in range(1, np.shape(dataset)[1]+1):
        allCombinations.extend(list(combinations(df.columns,lenValue)))
        
    return(allCombinations)

###############################################################################
dataset = np.array(pd.read_excel("dataFinal/games/games.xlsx"))
trainRows, testRows = splitData(0.7,0.2,0.1, dataset[2:])

predictLocalPoints(trainRows, testRows, dataset)
predictAwayPoints(trainRows, testRows, dataset)
    







