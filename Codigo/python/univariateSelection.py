import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def plotResults(dfcolumns, dfscores):
    #concat two dataframes for better visualization 
    featureScores = pd.concat([dfcolumns,dfscores],axis=1)
    featureScores.columns = ['Specs','Score']  #naming the dataframe columns
    print(featureScores.nlargest(10,'Score'))  #print 10 best features

def getDatasets(typeData, typeTarget):
    switchDataset = {
            0: ['games', [1,2]],
            1: ['h2h', [1,2]],
            2: ['players', [1,2]],
            3: ['totalData', [1,2]]
    }
    
    switchTarget = {
            0: 5,
            1: 3,
            2: 4
    }
    
    nameDataset = switchDataset.get(typeData, 'Invalid value for dataset')
    colsTarget = switchTarget.get(typeTarget, 'Invalid value for target')
    dataset = pd.read_excel("dataFinal/"+nameDataset[0]+"/"+nameDataset[0]+".xlsx")
    dataset = np.array(dataset.fillna(0))
    
    target = np.array(pd.read_excel("dataFinal/target/target.xlsx"))
    dataset = np.delete(dataset, nameDataset[1], 1)
    
    return(dataset, target[:, colsTarget])

def univariateSelection(typeData, typeTarget):
    dataset, target = getDatasets(typeData, typeTarget)

    dataset_X_train = dataset[1:]
    dataset_Y_train = target[1:].astype('int')
    
    #apply SelectKBest class to extract top 10 best features
    bestfeatures = SelectKBest(score_func=chi2)
    fit = bestfeatures.fit(dataset_X_train, dataset_Y_train)
    dfscores = pd.DataFrame(fit.scores_)
    dfcolumns = pd.DataFrame(dataset[0])

    plotResults(dfcolumns, dfscores)
    
###############################################################################
univariateSelection(2, 0)



