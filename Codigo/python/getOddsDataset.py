import pandas as pd
import numpy as np
import constants as c

def initOddsDataset():
    file = 'dataInit/odds/odds.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA

def initGameDataset():
    games = 'dataFinal/games/games.xlsx'
    xl = pd.ExcelFile(games)
    games = np.array(xl.parse(xl.sheet_names[0]))
    
    target = 'dataFinal/target/target.xlsx'
    xl = pd.ExcelFile(target)
    target = np.array(xl.parse(xl.sheet_names[0]))
    
    dataNBA = np.hstack((games, target[:, 3:]))
    dataNBA[1:, 15] = list(map(str, dataNBA[1:, 15]))
    dataNBA[1:, 16] = list(map(str, dataNBA[1:, 16]))
    
    return dataNBA[1:]

def getGameDataset(dataByGame):
    gameDataset = np.array(dataByGame[0, 0:3])
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        gameDataset = np.hstack((gameDataset, dataByTeam[0, 3:9]))
    
    return gameDataset

def getDataForMatch(gameDatasetT, oddsDataset, i):
#    print("ODDSDATASET[87]: ", oddsDataset[i])
    condTeams = (((gameDatasetT[:, 3] == oddsDataset[i, 2]) & (gameDatasetT[:, 9] == oddsDataset[i, 3]) & (gameDatasetT[:, 0] == oddsDataset[i, 0])))
    gamesArray = np.where(condTeams)
    ableTeams, indexTeams = isLocalMatchAble(gamesArray, i, 1)

    if ableTeams == 1:
        condPoints = ((gameDatasetT[indexTeams, 15] ==  oddsDataset[i, 4]) & (gameDatasetT[indexTeams, 16] ==  oddsDataset[i, 5]))
        finalSolution = np.where(condPoints)
        ablePoints, indexPoints = isLocalMatchAble(finalSolution, i, 2)
        
        if ablePoints == 1:         
            return ableTeams, ablePoints, indexTeams[indexPoints[0]]
#    print("---------------------------------")
    return -1, -1, []

def isLocalMatchAble(tupleValue, i, step):
    able = -1
    index = -1
#    print("INDEX AND STEP: ", i, step)
#    print("TUPLE: ", tupleValue)
#    if i > 84 and i < 101:
    if tupleValue[0].size == 1:
#        print("UNIQUE OPTIONS: ", i, tupleValue[0], tupleValue[0].size)
        able = 1
        index = tupleValue[0]
    elif tupleValue[0].size > 1:
#        print("MULTIPLE OPTIONS: ", i, tupleValue[0], tupleValue[0].size)
        if step == 1:
            able = 1
            index = tupleValue[0]

    return able, index
    

def getDataset():
    oddsDataset = initOddsDataset()
    gameDatasetT = initGameDataset()
    datasetGlobal = [c.ODDSFINALHEADER]
    testingErrors = []
    testingOKGame = []
    testingOKOdd = []
    
    for i in range(np.shape(oddsDataset)[0]):
#    for i in range(101, 102):
        ableTeams, ablePoints, indexGameT = getDataForMatch(gameDatasetT, oddsDataset, i)
        
        if ableTeams+ablePoints == 2:
            gameSelected = gameDatasetT[indexGameT]
            testingOKGame.append(indexGameT)
            testingOKOdd.append(i)
            
            if(gameSelected[3] == oddsDataset[i, 2]):
                newGameValues = np.hstack((gameSelected[:4],  oddsDataset[i, 6], oddsDataset[i, 3],  oddsDataset[i, 7]))
            else:
                newGameValues = np.hstack((gameSelected[:4],  oddsDataset[i, 7], oddsDataset[i, 3],  oddsDataset[i, 6]))
            
            datasetGlobal = np.vstack((datasetGlobal, newGameValues))
        else:
            testingErrors.append(i)
    
    testingOKGame.sort()
    testingOKOdd.sort()
    df = pd.DataFrame(datasetGlobal)
    df.to_excel('dataFinal/odds/odds.xlsx', index=False)
    print("Datos de las cuotas/probabilidades actualizadas correctamente.") 
    listTotal = np.array(range(0, np.shape(gameDatasetT)[0]))
    result = list(set(listTotal) - set(testingOKGame))
    result.sort()
    print("TESTINGOKGAME: ", testingOKGame)
    print("TESTINGOKODD: ", testingOKOdd)
    print("RESULT: ", len(result), "TESTINGOK: ", len(testingOKGame), "TESTINGOKUNIQUE: ", len(list(set(testingOKGame))))
    
getDataset()

        
    