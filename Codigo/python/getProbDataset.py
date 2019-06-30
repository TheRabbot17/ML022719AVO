# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:02:43 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

def initGameDataset():
    games = 'dataFinal/games/games.xlsx'
    xl = pd.ExcelFile(games)
    games = np.array(xl.parse(xl.sheet_names[0]))
    games = games[:, [0,1,2,3,9]]
    
    print("Hola:" ,games)
    return games

def getNameTeam(games):

    for i in range(1, np.shape(games)[0]):
        games[i, 3] = list(c.TEAMS.keys())[list(c.TEAMS.values()).index(str(games[i, 3]))]
        games[i, 4] = list(c.TEAMS.keys())[list(c.TEAMS.values()).index(str(games[i, 4]))]
    
    return games

games = initGameDataset()
games = getNameTeam(games)

df = pd.DataFrame(games)
df.to_excel('dataFinal/odds/odds.xlsx', index=False)
print('Datos de los partidos actualizados correctamente.')

