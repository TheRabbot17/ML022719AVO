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

transWinsLoses = {"W": 1,"L": 0}

transTrueFalse = {"VERDADERO": 1, "FALSO":0, "True": 1, "False": 0}

transTypeSeason = {"Pre Season": 0, "Regular Season": 1, "Playoffs": 3, "All Star": 4}

transNameTeam = {
        "Boston Celtics": 0,
        "Philadelphia 76ers": 1,
        "New Jersey Nets": 2,
        "Toronto Raptors": 3,
        "New York Knicks": 4,
        "Cleveland Cavaliers": 5,
        "Chicago Bulls": 6,
        "Detroit Pistons": 7,
        "Indiana Pacers": 8,
        "Milwaukee Bucks": 9,
        "Orlando Magic": 10,
        "Atlanta Hawks": 11,
        "Miami Heat": 12,
        "Charlotte Bobcats": 13,
        "Washington Wizards": 14,
        "Denver Nuggets": 15,
        "Portland Trail Blazers": 16,
        "Utah Jazz": 17,
        "Minnesota Timberwolves": 18,
        "Oklahoma City Thunder": 19,
        "Los Angeles Lakers": 20,
        "Phoenix Suns": 21,
        "Golden State Warriors": 22,
        "Los Angeles Clippers": 23,
        "Sacramento Kings": 24,
        "San Antonio Spurs": 25,
        "Houston Rockets": 26,
        "Dallas Mavericks": 27,
        "New Orleans Hornets": 28,
        "Memphis Grizzlies": 29,
        "Charlotte Hornets": 13,
        "Brooklyn Nets": 2,
        "New Orleans Pelicans": 28,
        "LA Clippers": 23
        }