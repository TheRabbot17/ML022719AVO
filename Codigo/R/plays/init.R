install.packages("devtools", repos = "https://cloud.r-project.org/", upgrade = TRUE, dependencies = TRUE)
install.packages("data.table")
install.packages("openxlsx")
devtools::install_github("abresler/nbastatR", upgrade = TRUE, force = TRUE, dependencies = TRUE)

library(devtools)
library(data.table)
library(openxlsx)
library(nbastatR)
