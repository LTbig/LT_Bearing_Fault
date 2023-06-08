import matplotlib.pyplot as plt
import pandas as pd
from sklearn.manifold import TSNE
X_tsne = pd.read_csv('E:/我的实验记录/Origin作图/N09_M07_F10_Tsne_data.csv')
print(X_tsne.head())
plt.scatter(X_tsne['0'],X_tsne['1'])
plt.show()
# plt.scatter(X_tsne[:, 0], X_tsne[:, 1])
# plt.title('T-SNE Visualization')
# plt.xlabel('Dimension 1')
# plt.ylabel('Dimension 2')
# plt.show()