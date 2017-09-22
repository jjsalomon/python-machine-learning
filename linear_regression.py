import quandl
import numpy as np
import math
import datetime
import pandas as pd
from sklearn import preprocessing, cross_validation, svm
# cross validation --shuffles data into training and testing set
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

# Extracting data
df = quandl.get('WIKI/GOOGL')
# Extracting column headers
df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_Change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
# Extracting valuable features -- which isnt valuable after all....
df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
# Rather than getting rid of data we replace it with -9999
df.fillna(-99999, inplace=True)

# math.ceil rounds up a number to the nearest whole
# We predict 10% of the DataFrame -- 10days ago
forecast_out = int(math.ceil(0.1*len(df)))

# Shifting columns negatively, column gets shifted up
df['label'] = df[forecast_col].shift(-forecast_out)

# Features
X = np.array(df.drop(['label'],1))

# Scaling it before classifying
# include all other values in your data
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace = True)
Y = np.array(df['label'])

# cross validation-shuffles data and splits them
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,Y,test_size=0.2)

# Create our classifier
#classifier = LinearRegression(n_jobs=-1)
#classifier.fit(X_train,y_train)
# Save classifier
#with open('linearregression.pickle','wb') as f:
#    pickle.dump(classifier,f)

pickle_in = open('linearregression.pickle','rb')
classifier = pickle.load(pickle_in)
# SVM Classifier
#classifier = svm.SVR()
#classifier.fit(X_train,y_train)
accuracy = classifier.score(X_test,y_test)

# Confidence level / Accuracy Percentage
print(accuracy)

forecast_set = classifier.predict(X_lately)
print(forecast_set,accuracy,forecast_out)

df['Forecast'] = np.nan

# Specify date -- take last date
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()