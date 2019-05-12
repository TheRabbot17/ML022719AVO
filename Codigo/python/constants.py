import numpy as np

####################################################################
####################################################################
#################### HEADERS #######################################
GAMEHEADER = ['yearSeason', 'dateGame', 'idGame', 
           'localIdTeam', 'isLocalB2B', 'isLocalB2BFirst', 'isLocalB2BSecond', 
           'localCountDaysRest', 'localCountDaysNextGameTeam', 
           'awayIdTeam', 'isAwayB2B', 'isAwayB2BFirst', 
           'isAwayB2BSecond', 'awayCountDaysRest', 'awayCountDaysNextGameTeam']

TARGETHEADER = ['yearSeason', 'dateGame', 'idGame', 
                'localPts', 'awayPts', 'winner']

H2HTOTALHEADER = ['yearSeason', 'dateGame', 'idGame', 
                  'idLocal', 'fgmLocal', 'fgaLocal', 'pctFGLocal', 'fg3mLocal',
                  'fg3aLocal', 'pctFG3Local', 'fg2mLocal', 'fg2aLocal', 'pctFG2Local',
                  'ftmLocal', 'ftaLocal', 'pctFTLocal', 'orebLocal', 'drebLocal',
                  'trebLocal', 'astLocal', 'stlLocal', 'blkLocal', 'tovLocal',
                  'pfLocal', 'ptsLocal', 'plsmnsLocal',
                  'idAway', 'fgmAway', 'fgaAway', 'pctFGAway', 'fg3mAway',
                  'fg3aAway', 'pctFG3Away', 'fg2mAway', 'fg2aAway', 'pctFG2Away',
                  'ftmAway', 'ftaAway', 'pctFTAway', 'orebAway', 'drebAway',
                  'trebAway', 'astAway', 'stlAway', 'blkAway', 'tovAway',
                  'pfAway', 'ptsAway', 'plsmnsAway']

H2HSUMMARYHEADER = ['yearSeason', 'dateGame', 'idGame', 
                  'idLocal', 'fgmLocal', 'fgaLocal', 'pctFGLocal', 'fg3mLocal',
                  'fg3aLocal', 'pctFG3Local', 'fg2mLocal', 'fg2aLocal', 'pctFG2Local',
                  'ftmLocal', 'ftaLocal', 'pctFTLocal', 'orebLocal', 'drebLocal',
                  'trebLocal', 'astLocal', 'stlLocal', 'blkLocal', 'tovLocal',
                  'pfLocal', 'ptsLocal', 'plsmnsLocal',
                  'idAway', 'fgmAway', 'fgaAway', 'pctFGAway', 'fg3mAway',
                  'fg3aAway', 'pctFG3Away', 'fg2mAway', 'fg2aAway', 'pctFG2Away',
                  'ftmAway', 'ftaAway', 'pctFTAway', 'orebAway', 'drebAway',
                  'trebAway', 'astAway', 'stlAway', 'blkAway', 'tovAway',
                  'pfAway', 'ptsAway', 'plsmnsAway', 'winsLocal', 'winsAway']

PLAYERSTOTALHEADER = ['yearSeason', 'dateGame', 'idGame',
                      'idLocal', 'activePlayersL', 'idAway', 'activePlayersA']

LINRHEADER = ['id', 'train', 'predict', 'MSE', 'MAD']

LOGRHEADER = ['id', 'train', 'predict', 'accuracy']

####################################################################
####################################################################
################## CONSTANTS VARIABLES #############################
DELETEGAMECOLUMNS = [1, 2, 3, 6, 7, 12, 13, 14, 17, 18, 19, 20]
DELETEGAMECOLUMNS.extend(np.linspace(21, 57, 37))

DELETETEAMCOLUMNS = [1, 2, 11, 12, 14, 19, 20, 21, 64, 65, 157, 158, 159]
DELETETEAMCOLUMNS.extend(np.linspace(108, 151, 43))

TARGETCOLUMNS = [0, 4, 5, 8, 12, 49, 20]

H2HTOTALCOLUMNS = [0,4,5,8,12,27,28,29,30,31,32,33,35,36,37,39,40,41,42,43,
                   44,45,46,47,48,49,50]

PLAYERSTOTALCOLUMNS = [0,4,5,8,12,25,38]

           
####################################################################
####################################################################
################## NORMALIZE VARIABLES #############################
YEARS = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
YEARSH2H = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', 
              '2012', '2013', '2014', '2015', '2016']
WINSTOLOSES = {"W": 1,"L": 0}

####################################################################