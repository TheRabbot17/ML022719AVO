import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import constants as c
from  itertools import combinations
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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
    experiment = np.hstack((experiment, accuracy_score(dataset_Y_test, dataset_Y_pred)))
    
    return(experiment)

def setColumnsDatasets(combination, isLocal):
    auxiliar =1
    if(isLocal):
        auxiliar = 0
        
    column = tuple(map(lambda x:x+5 + 29*auxiliar, combination))
    
    return(column)

def predictWin(trainRows, testRows, dataset):
    results = np.array([c.headersLogisticRegression])
    allCombinations = getAllCombinations(np.hstack((dataset[:, 5:11], dataset[:, 34:40])))
    i = 0
    for combi in allCombinations:
        #column = setColumnsDatasets(combi, False)
        experiment = np.array([i, dataset[0, combi], dataset[0, 64]])
        dataset_X_train = dataset[2:trainRows, combi]
        dataset_X_test = dataset[trainRows+2:testRows, combi]
        #dataset_X_validate = dataset_X[testRows:, 14:15]
    
        dataset_Y_train = dataset[2:trainRows, 64].astype('int')
        dataset_Y_test = dataset[trainRows+2:testRows, 64].astype('int')
        #dataset_Y_validate = dataset_X[testRows:, 62:63]
        
        regr = LogisticRegression()
        regr.fit(dataset_X_train, dataset_Y_train)
        dataset_Y_pred = regr.predict(dataset_X_test)
        
        experiment = setResults(dataset_Y_test, dataset_Y_pred, experiment)
        results = np.vstack((results, experiment))
        i += 1
        
    df = pd.DataFrame(results[1:], columns = c.headersLogisticRegression).sort_values(by=['accuracy'], ascending=False)
    df.to_excel('dataFinal/models/logistic-regression/logistic-regression-outcome.xlsx', index=False)
    print("Datos de los partidos predecidos correctamente.") 

def getAllCombinations(dataset):
    allCombinations = []
    print(dataset)
    df = pd.DataFrame(dataset)

    #for lenValue in range(1, np.shape(dataset)[1]+1):
    for lenValue in range(1, 4):
        allCombinations.extend(list(combinations(df.columns,lenValue)))
        
    return(allCombinations)
    
###############################################################################
dataset = np.array(pd.read_excel("dataFinal/games/games.xlsx"))
trainRows, testRows = splitData(0.7,0.2,0.1, dataset[2:])

predictWin(trainRows, testRows, dataset)