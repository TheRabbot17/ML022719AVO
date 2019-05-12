import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score 
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

def setResults(dataset_Y_test, dataset_Y_pred, experiment):
    errors = abs(dataset_Y_pred - dataset_Y_test)
    mape = 100 * (errors / dataset_Y_test)
    accuracy = 100 - np.mean(mape)

    experiment = np.hstack((experiment, round(accuracy, 2)))
    
    return(experiment)
    
def setColumnsDatasets(combination, isLocal, localAwayColumns):
    auxiliar =1
    if(isLocal):
        auxiliar = 0
        
    column = tuple(map(lambda x:x+5 + 29*auxiliar, combination))
    
    return(column)
    
def predictLocalWin(trainRows, testRows, dataset):
    results = np.array([c.headersLogisticRegression])
    allCombinations = getAllCombinations(dataset[:, 5:33])
    i = 0
    for combi in allCombinations:
        column = setColumnsDatasets(combi, True, 0)
        experiment = np.array([i, dataset[0, column], dataset[0, 64]])
        dataset_X_train = dataset[2:trainRows, column]
        dataset_X_test = dataset[trainRows+2:testRows, column]
        #dataset_X_validate = dataset_X[testRows:, 14:15]
    
        dataset_Y_train = dataset[2:trainRows, 64].astype('int')
        dataset_Y_test = dataset[trainRows+2:testRows, 64].astype('int')
        #dataset_Y_validate = dataset_X[testRows:, 62:63]
        
        rf = RandomForestRegressor(n_estimators = 1000, random_state = 42) 
        rf.fit(dataset_X_train, dataset_Y_train)
        dataset_Y_pred = rf.predict(dataset_X_test)
        
        experiment = setResults(dataset_Y_test, dataset_Y_pred, experiment)
        results = np.vstack((results, experiment))
        i += 1
    
    df = pd.DataFrame(results[1:], columns = c.headersLogisticRegression).sort_values(by=['accuracy'], ascending=False)
    df.to_excel('dataFinal/models/svm/svm-local.xlsx', index=False)
    print("Datos de los partidos como local predecidos correctamente.") 

def predictAwayWin(trainRows, testRows, dataset):
    results = np.array([c.headersLogisticRegression])
    allCombinations = getAllCombinations(dataset[:, 34:62])
    i = 0
    for combi in allCombinations:
        column = setColumnsDatasets(combi, False, 0)
        experiment = np.array([i, dataset[0, column], dataset[0, 65]])
        dataset_X_train = dataset[2:trainRows, column]
        dataset_X_test = dataset[trainRows+2:testRows, column]
        #dataset_X_validate = dataset_X[testRows:, 14:15]
    
        dataset_Y_train = dataset[2:trainRows, 65].astype('int')
        dataset_Y_test = dataset[trainRows+2:testRows, 65].astype('int')
        #dataset_Y_validate = dataset_X[testRows:, 62:63]
        
        rf = RandomForestRegressor(n_estimators = 1000, random_state = 42) 
        rf.fit(dataset_X_train, dataset_Y_train)
        dataset_Y_pred = rf.predict(dataset_X_test)
        
        experiment = setResults(dataset_Y_test, dataset_Y_pred, experiment)
        results = np.vstack((results, experiment))
        i += 1
        
    df = pd.DataFrame(results[1:], columns = c.headersLogisticRegression).sort_values(by=['accuracy'], ascending=False)
    df.to_excel('dataFinal/models/svm/svm-away.xlsx', index=False)
    print("Datos de los partidos como visitante predecidos correctamente.") 

def getAllCombinations(dataset):
    allCombinations = []
    df = pd.DataFrame(dataset)

    #for lenValue in range(1, np.shape(dataset)[1]+1):
    for lenValue in range(1, 3):
        allCombinations.extend(list(combinations(df.columns,lenValue)))
        
    return(allCombinations)

###############################################################################
dataset = np.array(pd.read_excel("dataFinal/games/games.xlsx"))
trainRows, testRows = splitData(0.7,0.2,0.1, dataset[2:])

predictLocalWin(trainRows, testRows, dataset)
predictAwayWin(trainRows, testRows, dataset)