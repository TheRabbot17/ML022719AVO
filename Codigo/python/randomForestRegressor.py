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

def getDatasets(typeData, typeOutput, locality):
    switchDatasetLocal = {
            0: ['games', c.GAMEPREDICTUSL, c.GAMEPREDICTFSL,c.GAMEPREDICT],
            1: ['h2h', c.H2HPREDICTUSL, c.H2HPREDICTFSL,c.H2HPREDICT],
            2: ['players', c.PLAYERSPREDICTUS, c.PLAYERSPREDICTFS,c.PLAYERSPREDICT],
            3: ['total', c.TOTALPREDICT, c.TOTALPREDICT,c.TOTALPREDICT]
    }
    
    switchDatasetAway = {
            0: ['games', c.GAMEPREDICTUSA, c.GAMEPREDICTFSA,c.GAMEPREDICT],
            1: ['h2h', c.H2HPREDICTUSA, c.H2HPREDICTFSA,c.H2HPREDICT],
            2: ['players', c.PLAYERSPREDICTUS, c.PLAYERSPREDICTFS,c.PLAYERSPREDICT],
            3: ['total', c.TOTALPREDICT, c.TOTALPREDICT,c.TOTALPREDICT]
    }
    
    if locality == 0:
        nameDataset = switchDatasetLocal.get(typeData, 'Invalid value')
    else:
        nameDataset = switchDatasetAway.get(typeData, 'Invalid value')
    dataset = pd.read_excel("dataFinal/"+nameDataset[0]+"/"+nameDataset[0]+".xlsx")
    dataset = np.array(dataset.fillna(0))
    
    target = np.array(pd.read_excel("dataFinal/target/target.xlsx"))
    
    if typeData == 1:
        dataset = dataset[4921:]
    
    return(dataset, target, nameDataset[1])

def predictLocalPoints(typeData,typeOutput, locality):
    dataset, target, features = getDatasets(typeData, typeOutput, locality)
    trainRows, testRows = splitData(0.7,0.2,0.1, dataset[1:])

    dataset_X_train = dataset[1:trainRows, features]
    dataset_X_test = dataset[trainRows+1:testRows, features]

    dataset_Y_train = dataset[1:trainRows, 3]
    dataset_Y_test = dataset[trainRows+1:testRows, 3]
    
    rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
    rf.fit(dataset_X_train, dataset_Y_train);
    dataset_Y_pred = rf.predict(dataset_X_test)
    
    plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred, 'LOCAL')

def predictAwayPoints(typeData, typeOutput, locality):
    dataset, target, features = getDatasets(typeData, typeOutput, locality)
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
predictLocalPoints(2,0,0)
predictAwayPoints(2,0,1)
    




