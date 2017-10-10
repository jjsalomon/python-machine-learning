import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
# We hardcode how many clusters....
X = np.array([[1,2],[2,3],[123,23],[135,87],[34,344],[256,400]])

# We are choosing 3 categories in the dataset
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
# 3 Centres in the dataset
centroids = kmeans.cluster_centers_
# 3 Labels
labels = kmeans.labels_

print(centroids)
print(labels)

# color per cluster
colors = ['g.','r.','c.']

# Display Data
for i in range(len(X)):
	print("Coordinate:", X[i], "Label:", labels[i])
	plt.plot(X[i][0],X[i][1], colors[labels[i]], markersize=10)	
plt.scatter(centroids[:,0],centroids[:,1], marker="x",s=150, linewidths=5,zorder=10)
plt.show()