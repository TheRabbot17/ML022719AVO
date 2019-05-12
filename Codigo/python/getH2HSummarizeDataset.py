import pandas as pd
import numpy as np
import constants as c
from  itertools import combinations

def getAllCombinationsTeams(options):
    allCombinations = []
    df = pd.DataFrame(options)

    allCombinations.extend(list(combinations(df.iloc[:,0],2)))
        
    return(allCombinations)

def initDataNBA(year):
    file = 'dataFinal/h2h/total/h2hTotal-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA

def initDataH2H():
    file = 'dataFinal/h2h/total/h2hTotal.xlsx'
    xl = pd.ExcelFile(file)
    h2hTotal = np.array(xl.parse(xl.sheet_names[0]))
    h2hTotal = np.hstack((h2hTotal, np.zeros((np.shape(h2hTotal)[0], 2))))
    
    return(h2hTotal)

def getH2H(dataset):
    H2HFinal = []
    pts = np.hstack((dataset[0][24], dataset[0][47]))
    H2HFinal.append(np.hstack((dataset[0], setWinner(pts))))
    for row in range(1, np.shape(dataset)[0]):
        stats = []
        aux = np.vstack((dataset[row], dataset[row-1]))
        stats.extend(dataset[row][0:4])
        stats.extend(np.mean(aux[:, 4:26], 0))
        stats.extend([dataset[row][26]])
        stats.extend(np.mean(aux[:, 27:49], 0))
        stats.extend(setWinH2H(aux[1], H2HFinal[-1]))

        H2HFinal.append(stats)

    return(H2HFinal)

def setWinH2H(dataset, H2HFinal):
    pts = np.hstack((dataset[24], dataset[47])) 
    outcome = np.add(H2HFinal[-2:], setWinner(pts))
    
    return(outcome)
    
def setWinner(pts):
    winner = []
    if(pts[0] > pts[1]):
        winner = [1,0]
    else:
        winner = [0,1]
        
    return(winner)

def setH2H(H2H, H2HTotal):
    for game in H2H:
        H2HTotal[np.where((H2HTotal[:,2] == game[2]))] = game
    
    return(H2HTotal)
    

def getDataset():
    dataNBA = initDataNBA('2005')
    H2HTotal = initDataH2H()
    combinationsMatch = getAllCombinationsTeams(np.unique(dataNBA[1:,3]))
    
    for combi in combinationsMatch:
        matchConcatenate = []
        for year in c.YEARSH2H[1:]:
            dataNBA = initDataNBA(year)
            matchByYear = dataNBA[np.where((dataNBA[:,3] == combi[0]) * (dataNBA[:,26] == combi[1]))]
            
            for row in range(0, np.shape(matchByYear)[0]):
                matchConcatenate.extend(matchByYear)
        
        H2H = getH2H(matchConcatenate)
        H2HTotal = setH2H(H2H, H2HTotal)
        print(np.shape(combinationsMatch))
        print(list(combinationsMatch).index(combi))
    
    dataset = np.vstack(([c.H2HSUMMARYHEADER], H2HTotal))
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/h2h/summary/h2hSummary.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

