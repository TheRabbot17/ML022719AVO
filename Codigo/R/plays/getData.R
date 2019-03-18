get_gameTable <- function (year) {
  return(game_logs(seasons = year))
}

get_probabilityTable <- function (gameID) {
  return(win_probability(game_ids = c(gameID), filter_non_plays = T))
}