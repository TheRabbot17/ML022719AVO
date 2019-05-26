import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import constants as c

def splitData(trainCoef, testCoef, valCoef, dataset):
    datasetRows = np.shape(dataset)[0]
    
    trainRows = int(np.trunc(datasetRows*trainCoef))
    testRows = int(trainRows + np.trunc(datasetRows*testCoef))
    
    return(trainRows, testRows)

def plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred, location):    
#    errors = abs(dataset_Y_pred - dataset_Y_test)
#    mape = 100 * (errors / dataset_Y_test)
#    accuracy = 100 - np.mean(mape)
    
    print("MEAN ABSOLUTE ERROR ("+location+"): ", mean_absolute_error(dataset_Y_test, dataset_Y_pred))
#    print('Accuracy:', round(accuracy, 2), '%.')

def getDatasets(typeData):
    switchDataset = {
            0: ['games', c.GAMECOLSTOPREDICTFS],
            1: ['h2h'],
            2: ['players', c.PLAYERSCOLSTOPREDICTFS],
            3: ['totalData']
    }
    
    nameDataset = switchDataset.get(typeData, 'Invalid value')
    dataset = pd.read_excel("dataFinal/"+nameDataset[0]+"/"+nameDataset[0]+".xlsx")
    dataset = np.array(dataset.fillna(0))
    
    target = np.array(pd.read_excel("dataFinal/target/target.xlsx"))
    
    return(dataset, target, nameDataset[1])

def predictLocalPoints(typeData):
    dataset, target, features = getDatasets(typeData)
    trainRows, testRows = splitData(0.7,0.2,0.1, dataset[1:])

    dataset_X_train = dataset[1:trainRows, features]
    dataset_X_test = dataset[trainRows+1:testRows, features]

    dataset_Y_train = dataset[1:trainRows, 3]
    dataset_Y_test = dataset[trainRows+1:testRows, 3]
    
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    rf.fit(dataset_X_train, dataset_Y_train);
    dataset_Y_pred = rf.predict(dataset_X_test)
    
    plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred, 'LOCAL')

def predictAwayPoints(typeData):
    dataset, target, features = getDatasets(typeData)
    trainRows, testRows = splitData(0.7,0.2,0.1, dataset[1:])

    dataset_X_train = dataset[1:trainRows, features]
    dataset_X_test = dataset[trainRows+1:testRows, features]

    dataset_Y_train = target[1:trainRows, 4]
    dataset_Y_test = target[trainRows+1:testRows, 4]
    
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    rf.fit(dataset_X_train, dataset_Y_train);
    dataset_Y_pred = rf.predict(dataset_X_test)
    
    plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred, 'AWAY')
    

###############################################################################
predictLocalPoints(2)
predictAwayPoints(2)
    




