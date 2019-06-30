import numpy as np
import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def plotResults(model, dataset_X_train, dataset):
    #plot graph of feature importances for better visualization
    feat_importances = pd.Series(model.feature_importances_, index=dataset[0])
    feat_importances.nlargest(10).plot(kind='barh')
    plt.show()
    
def getDatasets(typeData, typeTarget):
    switchDataset = {
            0: ['games', [1,2]],
            1: ['h2h', [1,2,25,48]],
            2: ['players', [1,2]],
            3: ['total', [1,2,30,82]]
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
    
    if typeData == 1:
        dataset = np.vstack((dataset[0], dataset[4921:]))
    
    return(dataset, target[:, colsTarget])

def featureImportance(typeData, typeTarget):
    dataset, target = getDatasets(typeData, typeTarget)

    dataset_X_train = dataset[2:]
    dataset_Y_train = target[2:].astype('int')
    
    model = ExtraTreesClassifier()
    model.fit(dataset_X_train, dataset_Y_train)

    plotResults(model, dataset_X_train, dataset)
    
###############################################################################
featureImportance(3,2)

# 0 = Winner; 1 = LocalPts; 2 = AwayPts



