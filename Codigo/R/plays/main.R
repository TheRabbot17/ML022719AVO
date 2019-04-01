library(nbastatR)
library(future)
library(openxlsx)
plan(multiprocess) 

# OBTENER DATOS SOBRE LOS PARTIDOS
for (iter in 2009:2016) {
  games = game_logs(seasons = iter)
  openxlsx::write.xlsx(games, paste0('games-', iter, '.xlsx'))
}

# OBTENER DATOS SOBRE LOS EQUIPOS
for (iter in 2009:2016) {
  teams = bref_teams_stats(seasons = iter)
  openxlsx::write.xlsx(teams$dataTable, paste0('teams-', iter, '.xlsx'))
}

# OBTENER DATOS SOBRE LOS JUGADORES
for (iter in 2009:2016) {
  players = bref_players_stats(seasons = iter, tables = c("advanced", "totals"))
  openxlsx::write.xlsx(players, paste0('players-', iter, '.xlsx'))
}