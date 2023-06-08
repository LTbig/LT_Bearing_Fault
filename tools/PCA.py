from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

# 假设X是一个n*m的特征矩阵，n为样本数，m为特征数
pca = PCA(n_components=2)  # 设置降维后的维度为2
X_pca = pca.fit_transform(X)  # 进行PCA降维

# 绘制散点图
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1])
plt.show()