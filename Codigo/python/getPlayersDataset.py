# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:11:02 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

def initDataNBA(year):
    file = 'dataInit/games/games-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA[:, c.PLAYERSTOTALCOLUMNS]

def createPlayerDatasets(datasetByYear, year, dataset):
    df = pd.DataFrame(datasetByYear)
    df.to_excel('dataFinal/players/players-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.")
    
    return(np.vstack((dataset, datasetByYear[1:])))

def setActivePlayers(activePlayers, gameDataset, dataByTeam):
    if dataByTeam[0,4] == 'H' and np.shape(gameDataset)[0] > 3:
        gameDataset = np.insert(gameDataset, 3, dataByTeam[0, 3])
        gameDataset = np.insert(gameDataset, 4, np.array(activePlayers))
    else:
        gameDataset = np.hstack((gameDataset, dataByTeam[0, 3]))
        gameDataset = np.hstack((gameDataset, np.array(activePlayers)))
    
    return gameDataset

def getPlayerDataset(dataByGame):
    gameDataset = np.array(dataByGame[0, 0:3])
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        activePlayers = dataByTeam[np.where(dataByTeam[:, 6] != 0)][:, 5]
        gameDataset = setActivePlayers(activePlayers, gameDataset, dataByTeam)
        print(gameDataset)
        
    return gameDataset
    
def getDataset():
    dataset = np.array([c.PLAYERSTOTALHEADER])
    for year in c.YEARSH2H:
        datasetByYear = np.array([c.PLAYERSTOTALHEADER])
        dataNBA = initDataNBA(year)
        
        for idGame in np.unique(dataNBA[:, 2]):  
            dataByGame = dataNBA[np.where(dataNBA[:, 2] == idGame)]
            gameDataset = getPlayerDataset(dataByGame)
            
            datasetByYear = np.vstack((dataset, gameDataset))
        
        dataset = createPlayerDatasets(datasetByYear, year, dataset)
    
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/players/players.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

