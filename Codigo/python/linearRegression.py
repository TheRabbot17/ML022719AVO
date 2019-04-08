import numpy as np
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score
import matplotlib.pyplot as plt


def splitData(trainCoef, testCoef, valCoef, dataset):
    datasetRows = np.shape(dataset)[0]
    
    trainRows = int(np.trunc(datasetRows*trainCoef))
    testRows = int(trainRows + np.trunc(datasetRows*testCoef))
    valRows = int(testRows + np.trunc(datasetRows*valCoef))
    
    return(trainRows, testRows, valRows)
    
# Load the games dataset
dataset = np.array(pd.read_excel("dataFinal/games/games.xlsx"))

# Use only one feature
dataset_X = dataset[2:]

trainRows, testRows, valRows = splitData(0.7, 0.2, 0.1, dataset_X)
# Split the data into training/testing sets
#dataset_X_train = dataset_X[:trainRows, :np.shape(dataset)[1]-4]
#dataset_X_test = dataset_X[trainRows:testRows, :np.shape(dataset)[1]-4]
#dataset_X_validate = dataset_X[testRows:, :np.shape(dataset)[1]-4]
dataset_X_train = dataset_X[:trainRows, 14:15]
dataset_X_test = dataset_X[trainRows:testRows, 14:15]
dataset_X_validate = dataset_X[testRows:, 14:15]

# Split the targets into training/testing sets
dataset_Y_train = dataset_X[:trainRows, 62:63]
dataset_Y_test = dataset_X[trainRows:testRows, 62:63]
dataset_Y_validate = dataset_X[testRows:, 62:63]

# Create linear regression object
regr = linear_model.LinearRegression()

print(np.shape(dataset_X_train),np.shape( dataset_Y_train))
# Train the model using the training sets
regr.fit(dataset_X_train, dataset_Y_train)

# Make predictions using the testing set
dataset_Y_pred = regr.predict(dataset_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(dataset_Y_test, dataset_Y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(dataset_Y_test, dataset_Y_pred))
print('Accuracy: %.2f' % accuracy_score(dataset_Y_test, dataset_Y_pred))

# Plot outputs
plt.scatter(dataset_X_test, dataset_Y_test,  color='black')
plt.plot(dataset_X_test, dataset_Y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()