# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:59:07 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

file = 'dataFinal/h2h/summary/h2hSummary.xlsx'
xl = pd.ExcelFile(file)
dataNBA = np.array(xl.parse(xl.sheet_names[0]))[1:]

file = 'dataFinal/h2h/total/h2hTotal.xlsx'
xl = pd.ExcelFile(file)
dataTotalNBA = np.array(xl.parse(xl.sheet_names[0]))[1:]


condition = (((dataNBA[:, 3] == 1610612752) * (dataNBA[:, 26] == 1610612761)) | ((dataNBA[:, 3] == 1610612761) * (dataNBA[:, 26] == 1610612752)))
rows = np.where(condition)

for row in rows[0]:
    print("COMBI: ", dataNBA[row, 3], dataNBA[row, 26], "Pts: ", dataTotalNBA[row, 24], dataTotalNBA[row, 47],"Pts Average: ",  dataNBA[row, 24], dataNBA[row, 47],"Outcome: ", dataNBA[row, 49], dataNBA[row, 50])
    
print("SHAPE: ", np.shape(rows))