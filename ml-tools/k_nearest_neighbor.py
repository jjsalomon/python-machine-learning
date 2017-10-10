import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import pickle
import random

# Read in data into Dataframe
df = pd.read_csv("data/...")

# Reading in random sub sample of a large dataset (no headers)
# Desired random sample_size = 1000
sample_size = 1000
filename = "data/..."
size = sum(for line in open(filename)
skip = sorted(random.sample(xrange(n),n-s))
df = pd.read_csv(filename,skiprows=skip)


# Replace missing values with outliers
df.replace('?', -99999, inplace = True)

# Remove ID Column
df.drop(['id'],1,inplace=True)

# Take a dataframe column and put it into a numpy array
X = np.array(df.drop(['...'],1))

# Take Labels
y = np.array(df.drop(['labels'])

# Cross Validation
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

# Choose K-Nearest Neighbor
classifier = neighbors.KNeighborsClassifier()
classifier.fit(X_train,y_train)
# Save model
with open('k_nearest_model.pickle','wb') as f:
	pickle.dump(classifier,f)
	
# Read in model
pickle_in = open('k_nearest_model.pickle','rb')
classifier = pickle.load(pickle_in)
accuracy = classifier.score(X_test,y_test)
print(accuracy)

# Generating test data
example_measures = np.array([[4,2,1,1,1,2,3,2,1],[4,1,1,2,1,3,3,2,1]])
example_measures = example_measures.reshape(len(example_measures),-1)

prediction = classifier.predict(example_measures)
print(prediction)