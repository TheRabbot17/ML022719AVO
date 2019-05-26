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

def initRostersNBA(year):
    file = 'dataInit/rosters/rosters-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA[:, c.ROSTERSTOTALCOLUMNS]
    

def createPlayerDatasets(datasetByYear, year, dataset):
    df = pd.DataFrame(datasetByYear)
    df.to_excel('dataFinal/players/players-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.")
    
    return(np.vstack((dataset, datasetByYear[1:])))

def setPlayers(activePlayers, inactivePlayers, gameDataset, dataByTeam):
    if dataByTeam[0,4] == 'H' and np.shape(gameDataset)[0] > 3:
        gameDataset = np.insert(gameDataset, 3, dataByTeam[0, 3])
        gameDataset = np.insert(gameDataset, 4, activePlayers)
        gameDataset = np.insert(gameDataset, 16, inactivePlayers)
    else:
        gameDataset = np.hstack((gameDataset, dataByTeam[0, 3]))
        gameDataset = np.hstack((gameDataset, activePlayers))
        gameDataset = np.hstack((gameDataset, inactivePlayers))
    
    return gameDataset

def setActiveInactive(activePlayers, inactivePlayers):
    if np.shape(activePlayers)[0] < 12:
        activePlayers = np.hstack((activePlayers, np.zeros((12 - np.shape(activePlayers)[0]))))
    if np.shape(inactivePlayers)[0] < 12:
        inactivePlayers = np.hstack((inactivePlayers, np.zeros((12 - np.shape(inactivePlayers)[0]))))

    return(activePlayers[:12], inactivePlayers[:12])

def getPlayerDataset(dataByGame, rostersNBA):
    gameDataset = dataByGame[0, 0:3]
    for idTeam in np.unique(dataByGame[:, 3]):
        dataByTeam = dataByGame[np.where(dataByGame[:, 3] == idTeam)]
        inactivePlayers = rostersNBA[np.where(rostersNBA[:, 1] == idTeam)][:, 0]
        activePlayers = dataByTeam[np.where(dataByTeam[:, 6] != 0)][:, 5]
        
        inactivePlayers = list(set(inactivePlayers) - set(activePlayers))
        activePlayers.sort()  
        inactivePlayers.sort()
        
        activePlayers, inactivePlayers = setActiveInactive(activePlayers, inactivePlayers)
        gameDataset = setPlayers(activePlayers, inactivePlayers, gameDataset, dataByTeam)
        
    return gameDataset
    
def getDataset():
    dataset = np.array([c.PLAYERSTOTALHEADER])
    for year in c.YEARS:
        datasetByYear = np.array([c.PLAYERSTOTALHEADER])
        dataNBA = initDataNBA(year)
        rostersNBA = initRostersNBA(year)
        
        for idGame in np.unique(dataNBA[:, 2]):  
            dataByGame = dataNBA[np.where(dataNBA[:, 2] == idGame)]
            gameDataset = getPlayerDataset(dataByGame, rostersNBA)
            
            datasetByYear = np.vstack((datasetByYear, gameDataset))
        
        dataset = createPlayerDatasets(datasetByYear, year, dataset)
    
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/players/players.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDataset()

        

