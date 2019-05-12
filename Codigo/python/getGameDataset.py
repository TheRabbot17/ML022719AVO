import pandas as pd
import numpy as np
import constants as c

def initDataNBA(year):
    file = 'dataInit/games/games-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    dataNBA = np.delete(dataNBA, c.DELETEGAMECOLUMNS, 1)
    
    return dataNBA

def getGameDataset(dataByGame):
    gameDataset = np.array(dataByGame[0, 0:3])
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        gameDataset = np.hstack((gameDataset, dataByTeam[0, 3:9]))
    
    return gameDataset

def createGamesDatasets(dataset, year, dataJoined):
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/games/games-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.")

    return(np.vstack((dataJoined, dataset[1:])))
    
def normalizeDataset(df):
    values = {7:0, 13:0}
    df = df.fillna(value = values)
    
    return df

def getDataset():
    datasetGlobal = np.array([c.GAMEHEADER])
    for year in c.YEARS:
        datasetByYear = np.array([c.GAMEHEADER])
        dataNBA = initDataNBA(year)
        
        for idGame in np.unique(dataNBA[:, 2]):  
            dataByGame = dataNBA[np.where(dataNBA[:, 2] == idGame)]
            gameDataset = getGameDataset(dataByGame)
            datasetByYear = np.append(datasetByYear, [gameDataset], axis=0)

        datasetGlobal = createGamesDatasets(datasetByYear, year, datasetGlobal)
      
    df = pd.DataFrame(datasetGlobal)
    df = normalizeDataset(df)
    df.to_excel('dataFinal/games/games.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

