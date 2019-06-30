# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:53:27 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

file = 'dataFinal/games/games.xlsx'
xl = pd.ExcelFile(file)
games = np.array(xl.parse(xl.sheet_names[0]))[1:]

file = 'dataFinal/odds/odds.xlsx'
xl = pd.ExcelFile(file)
odds = np.array(xl.parse(xl.sheet_names[0]))[1:]

print("SIZES: ", np.shape(games), np.shape(odds))