# SVM better than neural network at recognizing hand written digits
# One of the most complex machine learning algorithms
# Binary Classifier -- separates into two groups positive or negative
# Finds decision boundary
# Depicted into two dimensional space

import numpy as np
from sklearn import preprocessing, cross_validation, svm
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
# replace missing values with outlier value
df.replace('?', -99999, inplace=True)

# remove ID column --as its annoying towards the algorithm
df.drop(['id'], 1, inplace=True)

#Features
X = np.array(df.drop(['class'],1))
# Labels
y = np.array(df['class'])
# Cross validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
# Choose Support Vector Machine algorithm
classifier = svm.SVC()
classifier.fit(X_train,y_train)

accuracy = classifier.score(X_test,y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,1,1,2,1,3,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)

prediction = classifier.predict(example_measures)
print(prediction)