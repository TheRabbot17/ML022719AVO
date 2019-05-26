import pandas as pd
import numpy as np
import constants as c
from  itertools import combinations

def getAllCombinationsTeams(options):
    allCombinations = []
    df = pd.DataFrame(options)

    allCombinations.extend(list(combinations(df.iloc[:,0],2)))
        
    return(allCombinations)

def initDataH2H():
    file = 'dataFinal/h2h/total/h2hTotal.xlsx'
    xl = pd.ExcelFile(file)
    h2hTotal = np.array(xl.parse(xl.sheet_names[0]))
    zerosArray = np.zeros((np.shape(h2hTotal)[0], 2), dtype = int)
    h2hTotal = np.hstack((h2hTotal, zerosArray))
    
    return(h2hTotal[1:])

def getH2H(dataset):
    dictLocalAway = getLocalAwayByTeam(dataset)
    H2HFinal = [dataset[0]]

    for row in range(1, np.shape(dataset)[0]):
        stats = []
        stats.extend(dataset[row, 0:4])
        stats.extend(setStatsByTeam(dataset[:row+2], dictLocalAway))
        stats.extend(setWinH2H(dataset[row], dataset[row-1], H2HFinal[-1]))
        H2HFinal.append(stats)
        
    return(H2HFinal)

def setStatsByTeam(dataset, dictLocalAway):
    dictStatsByTeam = {}
    keysValues = list(dictLocalAway.keys())

    for key in keysValues:
        aux = []
        
        for row in range(np.shape(dataset)[0]-1):
            index = dictLocalAway[key][row]*23
            aux.append(dataset[row, 4+index:26+index])

        dictStatsByTeam[key] = np.mean(aux, axis=0)
    
    if(dictLocalAway[keysValues[0]][np.shape(dataset)[0]-1] == 0):
        stats = np.hstack((dictStatsByTeam[keysValues[0]], dataset[-1:, 26], dictStatsByTeam[keysValues[1]]))
    else:
        stats = np.hstack((dictStatsByTeam[keysValues[1]], dataset[-1:, 26], dictStatsByTeam[keysValues[0]]))
    
    return(stats)
   
def getLocalAwayByTeam(dataset):
    dictLocaAway = {}
    for team in np.unique(dataset[:, 3]):
        localAwayArray = []
        
        for row in range(0, np.shape(dataset)[0]):
            if dataset[row, 3] == team:
                localAwayArray.append(0)
            else: 
                localAwayArray.append(1)
                
        dictLocaAway[team] = localAwayArray
    
    return(dictLocaAway)
    

def setWinH2H(lastGame, lastLastGameInit, lastLastGameH2H):
    pts = np.hstack((lastLastGameInit[24], lastLastGameInit[47]))
    preOutcome = lastLastGameH2H[-2:]
    result = setWinner(pts)
            
    outcome = np.add(preOutcome, result)
    
    if lastGame[3] != lastLastGameInit[3]:
        return(np.flip(outcome))
    else:
        return(outcome)
    
def setWinner(pts):
    if(pts[0] > pts[1]): 
        winner = [1,0]
    else: 
        winner = [0,1]
        
    return(winner)

def setH2H(games, H2H):
    for game in games:
        H2H[np.where((H2H[:,2] == game[2]))] = game
    
    return(H2H)
    

def getDataset():
    H2H = initDataH2H()
    combinationsMatch = getAllCombinationsTeams(np.unique(H2H[1:,3]))
    
    for combi in combinationsMatch:
        condition = (((H2H[:,3] == combi[0]) * (H2H[:,26] == combi[1])) | ((H2H[:,3] == combi[1])) * (H2H[:,26] == combi[0]))
        matchs = H2H[np.where(condition)]
        
        games = getH2H(matchs)
        H2H = setH2H(games, H2H)
        print("SHAPE & INDEX: ", np.shape(combinationsMatch), list(combinationsMatch).index(combi))
    
    dataset = np.vstack(([c.H2HSUMMARYHEADER], H2H))
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/h2h/summary/h2hSummary.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

