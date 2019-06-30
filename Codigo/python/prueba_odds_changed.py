import pandas as pd
import numpy as np
import constants as c

def initOddsDataset():
    file = 'dataInit/odds/odds.xlsx'
    xl = pd.ExcelFile(file)
    dataNBA = np.array(xl.parse(xl.sheet_names[0]))
    
    return dataNBA

def initGameDataset():
    games = 'dataFinal/games/games.xlsx'
    xl = pd.ExcelFile(games)
    games = np.array(xl.parse(xl.sheet_names[0]))
    
    target = 'dataFinal/target/target.xlsx'
    xl = pd.ExcelFile(target)
    target = np.array(xl.parse(xl.sheet_names[0]))
    
    dataNBA = np.hstack((games, target[:, 3:]))
    dataNBA[1:, 15] = list(map(str, dataNBA[1:, 15]))
    dataNBA[1:, 16] = list(map(str, dataNBA[1:, 16]))
    
    return dataNBA[1:]

def getOddsDatasetByYear(year, oddsDataset):
    oddsDataset = oddsDataset[np.where(oddsDataset[:, 0] == year)]
    extra = c.EXTRA[year]
    
    return oddsDataset[extra[1]:np.shape(oddsDataset)[0]-extra[0]]

def getOdds(gameDatasetT, oddsDataset, game, matchUsed):
    oddsDataset = getOddsDatasetByYear(gameDatasetT[game, 0], oddsDataset)
    condTeams = (((gameDatasetT[game, 3] == oddsDataset[:, 2]) & (gameDatasetT[game, 9] == oddsDataset[:, 3])))
    optionsTeams = np.where(condTeams)[0]
    validOptions = validOptionsF(game, np.shape(oddsDataset)[0], matchUsed, optionsTeams)
    result = -1

    if len(validOptions) != 0:
        condPoints = ((gameDatasetT[game, 15] ==  oddsDataset[validOptions, 4]) & (gameDatasetT[game, 16] ==  oddsDataset[validOptions, 5]))
        optionsPoints = np.where(condPoints)[0]

        if len(optionsPoints) == 1:
            result = validOptions[optionsPoints[0]]
            print("RESULT: ", result)
        elif len(optionsPoints) > 1:
            print("MULTIPLE OPTIONS: ", game)
            

    return result

def validOptionsF(game, sizeOddDataset, matchUsed, options):
    validOptions = []

    for option in options:
        if option < sizeOddDataset-game+50 and option > sizeOddDataset-game-50:
            print("La opcion ", option, " se encuentra dentro de rango.")

            if option not in matchUsed:
                print("La solución ", option, " es nueva y no ha sido utilizada.")
                validOptions.append(option)

    return validOptions

def getDataset():
    oddsDataset = initOddsDataset()
    gameDatasetT = initGameDataset()
    datasetGlobal = [c.ODDSFINALHEADER]
    matchUsed = []
    matchNotWorking = []

    for game in range(np.shape(gameDatasetT)[0]):
        indexOdd = getOdds(gameDatasetT, oddsDataset, game, matchUsed)
        newGameValues = []

        if indexOdd != -1:
            matchUsed.append(indexOdd)
            newGameValues = np.hstack((gameDatasetT[game, :4], oddsDataset[indexOdd, 6], oddsDataset[indexOdd, 3],  oddsDataset[indexOdd, 7]))

            datasetGlobal = np.vstack((datasetGlobal, newGameValues))
        else:
            matchNotWorking.append(game)

    print("FALLADO: ", np.shape(matchNotWorking))
    df = pd.DataFrame(datasetGlobal)
    df.to_excel('dataFinal/odds/odds.xlsx', index=False)
    print("Datos de las cuotas/probabilidades actualizadas correctamente.") 

getDataset()