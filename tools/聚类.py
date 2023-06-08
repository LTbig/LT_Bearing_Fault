import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 生成数据
X = np.random.rand(100, 2)

# 使用K-Means聚类
kmeans = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# 绘制聚类图
colors = ['r', 'g', 'b']
for i in range(len(X)):
    plt.scatter(X[i, 0], X[i, 1], color=colors[labels[i]])
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, linewidths=3, color='k')
plt.show()