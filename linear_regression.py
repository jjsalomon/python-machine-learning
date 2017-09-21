import quandl
import numpy as np
import math
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
# cross validation --shuffles data into training and testing set
from sklearn.linear_model import LinearRegression

# Extracting data
df = quandl.get('WIKI/GOOGL')
# Extracting column headers
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# Extracting valuable features
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
# Rather than getting rid of data we replace it with -9999
df.fillna(-99999, inplace=True)

# math.ceil rounds up a number to the nearest whole
# We predict 10% of the DataFrame -- 10days ago
forecast_out = int(math.ceil(0.01*len(df)))

# Shifting columns negatively, column gets shifted up
df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

# Features
X = np.array(df.drop(['label'],1))
# Labels
Y = np.array(df['label'])

# Scaling it before classifying
# include all other values in your data
X = preprocessing.scale(X)
df.dropna(inplace = True)
Y = np.array(df['label'])

# cross validation-shuffles data and splits them
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,Y,test_size=0.2)

# Create our classifier
classifier = LinearRegression(n_jobs=-1)
classifier.fit(X_train,y_train)
# SVM Classifier
#classifier = svm.SVR()
#classifier.fit(X_train,y_train)
accuracy = classifier.score(X_test,y_test)

# Confidence level / Accuracy Percentage
print(accuracy)

