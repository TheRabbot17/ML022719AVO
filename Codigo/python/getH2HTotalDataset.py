import pandas as pd
import numpy as np
import constants as c

def formStatsTeam(teamData, gameDataset):
    auxStats = np.array(np.sum(teamData[:, 0]))
    for index in range(1, np.shape(teamData)[1]):
        auxStats = np.hstack((auxStats, np.nansum(teamData[:, index])))
        
    for index in [2, 5, 8, 11]:
        auxStats[index] = np.around(auxStats[index-2]/auxStats[index-1], 2)

    return auxStats

def setStatsTeams(teamData, location, gameDataset):
    if location == 'H' and np.shape(gameDataset)[0] > 3:
        gameDataset = np.insert(gameDataset, 3, teamData[0, 3])
        gameDataset = np.insert(gameDataset, 4, formStatsTeam(teamData[:, 5:], gameDataset)) 
    else:
        gameDataset = np.hstack((gameDataset, teamData[0, 3]))
        gameDataset = np.hstack((gameDataset, formStatsTeam(teamData[:, 5:], gameDataset)))
    
    return gameDataset

def initDataNBA(year):
    file = 'dataInit/games/games-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    dataNBA = dataNBA[:, c.H2HTOTALCOLUMNS]
    dataNBA = np.insert(dataNBA, 17, dataNBA[:,11], 1)
    dataNBA = np.delete(dataNBA, [11], 1)
    
    return dataNBA

def getGameDataset(dataByGame):
    gameDataset = np.array(dataByGame[0, 0:3])
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        gameDataset = setStatsTeams(dataByTeam, dataByTeam[0,4], gameDataset)
    
    return gameDataset

def createGamesDatasets(dataset, year, dataJoined):
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/h2h/total/h2hTotal-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.")

    return(np.vstack((dataJoined, dataset[1:])))
    
def cleanDataset(dataset):
    dataset[1:, 64] = [c.transWinsLoses[letter] for letter in dataset[1:, 64]]
    dataset[1:, 1] = [c.transTypeSeason[letter] for letter in dataset[1:, 1]]
    dataset[1:, 5] = [c.transNameTeam[letter] for letter in dataset[1:, 5]]
    dataset[1:, 34] = [c.transNameTeam[letter] for letter in dataset[1:, 34]]
    
    return(dataset)

def getDataset():
    datasetGlobal = np.array([c.H2HTOTALHEADER])
    for year in c.YEARSH2H:
        datasetByYear = np.array([c.H2HTOTALHEADER])
        dataNBA = initDataNBA(year)
        
        for idGame in np.unique(dataNBA[:, 2]):  
            dataByGame = dataNBA[np.where(dataNBA[:, 2] == idGame)]
            gameDataset = getGameDataset(dataByGame)

            datasetByYear = np.append(datasetByYear, [gameDataset], axis=0)

        datasetGlobal = createGamesDatasets(datasetByYear, year, datasetGlobal)
   
    df = pd.DataFrame(datasetGlobal)
    df.to_excel('dataFinal/h2h/total/h2hTotal.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

