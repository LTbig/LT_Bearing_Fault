import torch
import torchvision.models as models
import torch.nn.functional as F

model = models.resnet50(pretrained=True)

x = torch.ones(32, 1024, 24, 36)
hidden = model.layer4(x)

features = F.adaptive_avg_pool2d(hidden, (1, 1)).squeeze()

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 使用t-SNE算法将特征向量降维为二维
tsne = TSNE(n_components=2, random_state=0)
X_2d = tsne.fit_transform(features.detach().numpy())

# 绘制散点图
plt.scatter(X_2d[:, 0], X_2d[:, 1])
plt.show()
