# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:11:02 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

def formStatsTeam(teamData, gameDataset):
    auxStats = np.array(np.sum(teamData[:, 13]))
    for index in range(14, 35):
        auxStats = np.hstack((auxStats, np.nansum(teamData[:, index])))
        
    for index in [15, 18, 21, 24]:
        auxStats[index-13] = np.around(auxStats[index-15]/auxStats[index-14], 2)
        
    return auxStats

def setStatsTeams(teamData, location, gameDataset):
    if location == 'H' and np.shape(gameDataset)[0] > 12:
        np.insert(gameDataset, 4, teamData[0, 4:13])
        np.insert(gameDataset, 13, formStatsTeam(teamData, gameDataset)) 
    else:
        gameDataset = np.hstack((gameDataset, teamData[0, 4:13]))
        gameDataset = np.hstack((gameDataset, formStatsTeam(teamData, gameDataset)))
    
    return gameDataset

def initDataNBA(year):
    file = 'dataInit/games/game-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse('Hoja1'))
    dataNBA = np.delete(dataNBA, c.columnsGameToDelete, 1)
    dataNBA = np.insert(dataNBA, 26, dataNBA[:,20], axis=1)
    dataNBA = np.delete(dataNBA, 20, 1)
    
    return dataNBA

def getGameDataset(dataByGame, dataNBA):
    gameDataset = np.array(dataByGame[0, 0:4])
    for idTeam in np.unique(dataByGame[:, 6]):
        dataByTeam = dataNBA[np.where(dataNBA[:, 6] == idTeam)]
        gameDataset = setStatsTeams(dataByTeam, dataByTeam[0, 10], gameDataset)
        
    return gameDataset
    
    
def getDatasetGamesNBA():
    for year in c.yearsDataFiles:
        dataset = np.array([c.headersGame])
        dataNBA = initDataNBA(year)
        
        for idGame in np.unique(dataNBA[:, 3]):
            dataByGame = dataNBA[np.where(dataNBA[:, 3] == idGame)]
            gameDataset = getGameDataset(dataByGame, dataNBA)
            dataset = np.append(dataset, [gameDataset], axis=0)
        
        
        df = pd.DataFrame (dataset)
        df.to_excel('dataFinal/games/game-' + year + '.xlsx', index=False)


getDatasetGamesNBA()

        

