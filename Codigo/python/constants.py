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
                      'idLocal', 
                      'actPlayerLocal1' , 'actPlayerLocal2', 'actPlayerLocal3',
                      'actPlayerLocal4' , 'actPlayerLocal5', 'actPlayerLocal6',
                      'actPlayerLocal7' , 'actPlayerLocal8', 'actPlayerLocal9',
                      'actPlayerLocal10' , 'actPlayerLocal11', 'actPlayerLocal12',
                      'inactPlayerLocal1' , 'inactPlayerLocal2', 'inactPlayerLocal3',
                      'inactPlayerLocal4' , 'inactPlayerLocal5', 'inactPlayerLocal6',
                      'inactPlayerLocal7' , 'inactPlayerLocal8', 'inactPlayerLocal9',
                      'inactPlayerLocal10' , 'inactPlayerLocal11', 'inactPlayerLocal12',
                      'idAway',
                      'actPlayerAway1' , 'inactPlayerAway2', 'inactPlayerAway3',
                      'actPlayerAway4' , 'inactPlayerAway5', 'inactPlayerAway6',
                      'actPlayerAway7' , 'inactPlayerAway8', 'inactPlayerAway9',
                      'actPlayerAway10' , 'inactPlayerAway11', 'inactPlayerAway12',
                      'inactPlayerAway1' , 'inactPlayerAway2', 'inactPlayerAway3',
                      'inactPlayerAway4' , 'inactPlayerAway5', 'inactPlayerAway6',
                      'inactPlayerAway7' , 'inactPlayerAway8', 'inactPlayerAway9',
                      'inactPlayerAway10' , 'inactPlayerAway11', 'inactPlayerAway12']

ODDSINITHEADER = ['year', 'hour', 'idLocal', 'idAway', 'ptsLocal' 'ptsAway',
                  'oddWinLocal', 'oddWinAway']

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

ROSTERSTOTALCOLUMNS = [3,5]

URLBASE = 'https://www.oddsportal.com/basketball/usa/nba-{}/results/#/page/{}/'
DRIVERPATH = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'

GAMECOLSTOPREDICTFS = [0, 7, 8, 13, 14]
GAMECOLSTOPREDICTUS = [7, 8, 12, 13, 14]

PLAYERSCOLSTOPREDICTFS = range(3, 53)
           
####################################################################
####################################################################
################## NORMALIZE VARIABLES #############################
YEARS = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
YEARSH2H = ['2005', '2006', '2007', '2008', '2009', '2010', '2011', 
              '2012', '2013', '2014', '2015', '2016']
WINSTOLOSES = {"W": 1,"L": 0}

####################################################################
####################################################################
################## DICTIONARY ######################################
TEAMS = {
        "AtlantaHawks": '1610612737',
        "BostonCeltics": '1610612738',
        "ClevelandCavaliers": '1610612739',
        "NewOrleansPelicans": '1610612740',
        "ChicagoBulls": '1610612741',
        "DallasMavericks": '1610612742',
        "DenverNuggets": '1610612743',
        "GoldenStateWarriors": '1610612744',
        "HoustonRockets": '1610612745',
        "LosAngelesClippers": '1610612746',
        "LosAngelesLakers": '1610612747',
        "MiamiHeat": '1610612748',
        "MilwaukeeBucks": '1610612749',
        "MinnesotaTimberwolves": '1610612750',
        "BrooklynNets": '1610612751',
        "NewYorkKnicks": '1610612752',
        "OrlandoMagic": '1610612753',
        "IndianaPacers": '1610612754',
        "Philadelphia76ers": '1610612755',
        "PhoenixSuns": '1610612756',
        "PortlandTrailBlazers": '1610612757',
        "SacramentoKings": '1610612758',
        "SanAntonioSpurs": '1610612759',
        "OklahomaCityThunder": '1610612760',
        "TorontoRaptors": '1610612761',
        "UtahJazz": '1610612762',
        "MemphisGrizzlies": '1610612763',
        "WashingtonWizards": '1610612764',
        "DetroitPistons": '1610612765',
        "CharlotteHornets": '1610612766',
        }