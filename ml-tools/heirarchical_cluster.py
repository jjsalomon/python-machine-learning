# Heirarchical clustering to allow the machine to figure out how many clusters the data should have
import numpy as np
from sklearn.cluster import MeanShift
# generate sample of data
from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt

centers = [[1,1],[5,5],[3,10]]

# Limit samples to < 10,000
# Y = labels from import generated
X, y = make_blobs(n_samples=500, centers=centers, cluster_std = 1)

plt.scatter(X[:,0],X[:,1])
plt.show()

ms = MeanShift()
ms.fit(X)
# These labels are machine generated
labels = ms.labels_
# estimated centers --similar to centroids
cluster_centers = ms.cluster_centers_
# How many unique values exists
n_clusters = len(np.unique(labels))

print("Number of estimated clusters:", n_clusters)
print(cluster_centers)
# 10 x bigger than it is
colors = 10*['r.','g.','b.','c.','k.','y.','m.']

print(colors)
print(labels)

for i in range(len(X)):
	plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize=10)
	
plt.scatter(cluster_centers[:,0],cluster_centers[:,1], marker="x", s=150,linewidths=5,zorder=10)
plt.show()