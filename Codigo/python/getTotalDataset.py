import pandas as pd
import numpy as np
import constants as c

def initGamesDataset():
    file = 'dataFinal/games/games.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    index = np.where(dataNBA[0,:] == 'idAway')[0][0]
    
    return dataNBA, index

def initTeamsDataset():
    file = 'dataFinal/h2h/h2h.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    index = np.where(dataNBA[0,:] == 'idAway')[0][0]
    dataNBA = np.vstack((dataNBA[0], dataNBA[4921:]))
    
    return dataNBA, index

def initPlayersDataset():
    file = 'dataFinal/players/players.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    index = np.where(dataNBA[0,:] == 'idAway')[0][0]
    
    return dataNBA, index

def getDataset():
    games, index0 = initGamesDataset()
    teams, index1 = initTeamsDataset()
    players, index2 = initPlayersDataset()

    local = np.hstack((teams[:, 4:index1], players[:, 4:index2]))
    away = np.hstack((teams[:, index1+1:], players[:, index2+1:]))
    
    for i in range(np.shape(local)[1]):
        games = np.insert(games, index0+i, local[:, i], 1)
    totalDataset = np.hstack((games, away))
    
    df = pd.DataFrame(totalDataset)
    df.to_excel('dataFinal/total/total.xlsx', index=False)
    print("Todos los datos han sido actualizados correctamente.") 

getDataset()