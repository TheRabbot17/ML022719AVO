from rpy2.robjects.packages import importr
utils = importr("utils")
package_name = 'nbastatR'
utils.install_packages(package_name, lib_loc="D:\AlbertVillarOrtiz\Documents\R\win-library\3.5")
nba = importr('nbastatR')

def getGameTable(year):
    print(nba.game_logs(seasons = year, season_types = ["Regular Season","Playoffs"]))
    #return(nba.game_logs(seasons = year))

def getProbTable(gameID):
    print(nba.win_probability(game_ids = gameID, filter_non_plays = True))
    #return(nba.win_probability(game_ids = gameID, filter_non_plays = True))
    
def getTeamsTable(year):
    print(nba.bref_teams_stats(seasons = year))
    #return(nba.bref_teams_stats(seasons = year))
    
def getPlayersTable(year):
    print(nba.bref_players_stats(seasons = year, tables = ["advanced", "totals"]))
    #return(nba.bref_players_stats(seasons = year, tables = c("advanced", "totals")))
    
