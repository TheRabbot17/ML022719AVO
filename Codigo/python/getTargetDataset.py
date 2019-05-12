import pandas as pd
import numpy as np
import constants as c

def setStatsTeams(teamData, location, gameDataset):
    if location == 'H' and np.shape(gameDataset)[0] > 3:
        gameDataset = np.insert(gameDataset, 3, np.nansum(teamData[:, 5]))
    else:
        gameDataset = np.hstack((gameDataset, np.nansum(teamData[:, 5])))
    
    return gameDataset

def initDataNBA(year):
    file = 'dataInit/games/games-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA[:, c.TARGETCOLUMNS]

def getGameDataset(dataByGame):
    gameDataset = np.array(dataByGame[0, 0:3])
    winner = ''
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        gameDataset = setStatsTeams(dataByTeam, dataByTeam[0, 4], gameDataset)
        if dataByTeam[0, 4] == 'H':
            winner = dataByTeam[0, 6]
    gameDataset = np.hstack((gameDataset, [winner]))
    return gameDataset

def createGamesDatasets(dataset, year, dataJoined):
    dataset = cleanDataset(dataset)
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/target/target-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.")

    return(np.vstack((dataJoined, dataset[1:])))
    
def cleanDataset(dataset):
    dataset[1:, 5] = [c.WINSTOLOSES[letter] for letter in dataset[1:, 5]]
    
    return(dataset)

    
def getDataset():
    datasetGlobal = np.array([c.TARGETHEADER])
    for year in c.YEARS:
        datasetByYear = np.array([c.TARGETHEADER])
        dataNBA = initDataNBA(year)
        
        df = pd.DataFrame(dataNBA)
        df.to_excel('prueba.xlsx', index=False)
        print("Datos de los partidos actualizados correctamente.")
               
        for idGame in np.unique(dataNBA[:, 2]):  
            dataByGame = dataNBA[np.where(dataNBA[:, 2] == idGame)]
            gameDataset = getGameDataset(dataByGame)
            datasetByYear = np.append(datasetByYear, [gameDataset], axis=0)
            
        datasetGlobal = createGamesDatasets(datasetByYear, year, datasetGlobal)

    df = pd.DataFrame(datasetGlobal)
    df.to_excel('dataFinal/target/target.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

