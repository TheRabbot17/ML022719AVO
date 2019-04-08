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
    file = 'dataInit/games/games-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
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

def setOrderDataset(dataset):
    dataset = np.hstack((dataset, dataset[:,33:34]))
    dataset = np.hstack((dataset, dataset[:,64:65]))
    dataset = np.hstack((dataset, dataset[:,12:13]))
    dataset = np.hstack((dataset, dataset[:,43:44]))
    dataset = np.delete(dataset, [12,33,43,64], 1)
    
    return dataset

def createGamesDatasets(dataset, year, dataJoined):
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/games/games-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.") 
    
    return(np.vstack((dataJoined, dataset[2:])))
    
def cleanDataset(dataset):
    dataset[1:, 64] = [c.transWinsLoses[letter] for letter in dataset[1:, 64]]
    dataset[1:, 65] = [c.transWinsLoses[letter] for letter in dataset[1:, 65]]
    #dataset[1:, 7] = [c.transTrueFalse[letter] for letter in dataset[1:, 7]]
    #dataset[1:, 8] = [c.transTrueFalse[letter] for letter in dataset[1:, 8]]
    #dataset[1:, 9] = [c.transTrueFalse[letter] for letter in dataset[1:, 9]]
    #dataset[1:, 36] = [c.transTrueFalse[letter] for letter in dataset[1:, 36]]
    #dataset[1:, 37] = [c.transTrueFalse[letter] for letter in dataset[1:, 37]]
    #dataset[1:, 38] = [c.transTrueFalse[letter] for letter in dataset[1:, 38]]
    dataset[1:, 1] = [c.transTypeSeason[letter] for letter in dataset[1:, 1]]
    dataset[1:, 5] = [c.transNameTeam[letter] for letter in dataset[1:, 5]]
    dataset[1:, 34] = [c.transNameTeam[letter] for letter in dataset[1:, 34]]
    
    return(dataset)
    
def getDatasetGamesNBA():
    dataJoined = np.array([c.headersGame])
    for year in c.yearsDataFiles:
        dataset = np.array([c.headersGame])
        dataNBA = initDataNBA(year)
        
        for idGame in np.unique(dataNBA[:, 3]):
            dataByGame = dataNBA[np.where(dataNBA[:, 3] == idGame)]
            gameDataset = getGameDataset(dataByGame, dataNBA)
            dataset = np.append(dataset, [gameDataset], axis=0)
        
        dataset = setOrderDataset(dataset)
        dataset = cleanDataset(dataset)
        dataJoined = createGamesDatasets(dataset, year, dataJoined)
        
    df = pd.DataFrame(dataJoined)
    df.to_excel('dataFinal/games/games.xlsx', index=False)
    print("Datos de los partidos actualizados correctamente.") 
    
getDatasetGamesNBA()

        

