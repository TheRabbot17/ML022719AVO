import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import constants as c
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def splitData(trainCoef, testCoef, valCoef, dataset):
    datasetRows = np.shape(dataset)[0]
    
    trainRows = int(np.trunc(datasetRows*trainCoef))
    testRows = int(trainRows + np.trunc(datasetRows*testCoef))
    
    return(trainRows, testRows)

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

def plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred):
    print("Accuracy: ", accuracy_score(dataset_Y_test, dataset_Y_pred))

def predictWin(typeData):
    dataset, target, features = getDatasets(typeData)
    trainRows, testRows = splitData(0.7,0.2,0.1, dataset[1:])
    
    dataset_X_train = dataset[1:trainRows, features]
    dataset_X_test = dataset[trainRows+1:testRows, features]

    dataset_Y_train = target[1:trainRows, 5].astype('int')
    dataset_Y_test = target[trainRows+1:testRows, 5].astype('int')
    
    regr = LogisticRegression()
    regr.fit(dataset_X_train, dataset_Y_train)
    dataset_Y_pred = regr.predict(dataset_X_test)
    
    plotResults(dataset_X_test, dataset_Y_test, dataset_Y_pred)
    
###############################################################################
predictWin(2)