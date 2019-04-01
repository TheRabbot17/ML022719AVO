# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 20:37:42 2019

@author: AlbertVillarOrtiz
"""

headersGame = ['yearSeason', 'typeSeason', 'dateGame', 'idGame', 
           'numberGameLocalSeason', 'localNameTeam', 'localIdTeam', 'isLocalB2B',
           'isLocalB2BFirst', 'isLocalB2BSecond', 'localCountDaysRest', 
           'localCountDaysNextGameTeam', 'isLocalWinner', 'localFgm', 'localFga',
           'localpctFG', 'localFg3m', 'localFg3a', 'localPctFG3', 'localFg2m', 
           'localFg2a', 'localPctFG2', 'localFtm', 'localFta', 'localPctFT',
           'localOReb', 'localDReb', 'localTreb', 'localAst', 
           'localStl', 'localBlk', 'localTov', 'localPf', 'localPts', 
           'localPlusMinus', 'numberGameAwaySeason','awayNameTeam', 'awayIdTeam', 
           'isAwayB2B', 'isAwayB2BFirst', 'isAwayB2BSecond', 'awayCountDaysRest', 
           'awayCountDaysNextGameTeam', 'isAwayWinner', 'awayFgm', 'awayFga',
           'awaypctFG', 'awayFg3m', 'awayFg3a', 'awayPctFG3', 'awayFg2m', 
           'awayFg2a', 'awayPctFG2', 'awayFtm', 'awayFta', 'awayPctFT',
           'awayOReb', 'awayDReb', 'awayTreb', 'awayAst', 
           'awayStl', 'awayBlk', 'awayTov', 'awayPf', 'awayPts', 'awayPlusMinus']

columnsGameToDelete = [1, 2, 12, 13, 14, 17, 18, 19, 21, 22, 23, 24, 25, 26, 34, 38,
                 51, 52, 53, 54, 55, 56, 57]

yearsDataFiles = ['2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009']