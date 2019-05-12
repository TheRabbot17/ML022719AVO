# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:11:02 2019

@author: AlbertVillarOrtiz
"""
import pandas as pd
import numpy as np
import constants as c

def initDataNBA(year):
    file = 'dataInit/teams/teams-' + year + '.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.vstack((xl.parse(xl.sheet_names[0]).columns, xl.parse(xl.sheet_names[0])))
    dataNBA = np.delete(dataNBA, c.columnsTeamToDelete, 1)
    print(np.shape(dataNBA))
    
    return dataNBA

def createTeamDatasets(dataset, year):
    df = pd.DataFrame(dataset)
    df.to_excel('dataFinal/teams/teams-' + year + '.xlsx', index=False)
    print("Datos del año " + year + " actualizados correctamente.") 
    
def getDatasetTeamsNBA():
    for year in c.yearsDataFiles:
        dataNBA = initDataNBA(year)
        createTeamDatasets(dataNBA, year)
    
getDatasetTeamsNBA()

        

