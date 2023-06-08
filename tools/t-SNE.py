import numpy as np
from sklearn.datasets import make_blobs
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

# 构造3个类别的数据
X, y = make_blobs(n_samples=3000, centers=3, random_state=0, cluster_std=0.5)

# 使用T-SNE算法将高维特征映射到二维空间中
tsne = TSNE(n_components=2, random_state=0)
X_tsne = tsne.fit_transform(X)

# 可视化
sns.scatterplot(x=X_tsne[:,0], y=X_tsne[:,1], hue=y, palette="Set2")
plt.show()