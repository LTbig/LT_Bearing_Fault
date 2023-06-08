import numpy as np
from torch.utils.data import DataLoader, Dataset
from sklearn.manifold import TSNE
from read_fault_data_PU_N15_M07_F04_phase_current import ready_data
import torch
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import pandas as pd

data = ready_data()  # 读取数据集

# 将数据升为2维数据
temp = []
for i in range(len(data)):
    # temp = data[i][0].reshape(24, 36)
    # temp = data[i][0].reshape(32, 32)
    temp = data[i][0].reshape(40, 64)
    data[i][0] = temp
temp = []
print("data length:", len(data))


np.random.shuffle(data)




# 轴承数据集读取
class PU_Dataset(Dataset):
    def __init__(self, data):
        self.len = len(data)
        self.x_data = torch.from_numpy(np.array(list(map(lambda x: x[0:-1], data)), dtype=np.float32))
        self.y_data = torch.from_numpy(np.array(list(map(lambda x: x[-1], data)), dtype=np.float32)).squeeze().long()

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


Train_dataset = PU_Dataset(list(data))  # 训练集dataloader构造
dataloader = DataLoader(Train_dataset, shuffle=True, batch_size=5120, drop_last=True)



# 通道注意力
class ChannelAttention(nn.Module):
    def __init__(self, in_channels, reduction_ratio=16):
        super(ChannelAttention, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.max_pool = nn.AdaptiveMaxPool2d(1)
        self.fc1 = nn.Conv2d(in_channels, in_channels // reduction_ratio, 1)
        self.relu = nn.ReLU()
        self.fc2 = nn.Conv2d(in_channels // reduction_ratio, in_channels, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        avg_out = self.fc2(self.relu(self.fc1(self.avg_pool(x))))
        max_out = self.fc2(self.relu(self.fc1(self.max_pool(x))))
        out = avg_out + max_out
        return self.sigmoid(out) * x


# 空间注意力
class SpatialAttention(nn.Module):
    def __init__(self, in_channels):
        super(SpatialAttention, self).__init__()
        self.conv = nn.Conv2d(in_channels, 1, kernel_size=7, padding=3)

    def forward(self, x):
        # 卷积操作
        out = self.conv(x)
        # 对卷积后的输出数据进行softmax操作
        out = F.softmax(out, dim=1)
        # 将得到的权重与原始输入数据相乘，得到加权后的输出数据
        out = x * out
        return out


# 残差块
class ResBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=out_channels, out_channels=out_channels, kernel_size=3, padding=1)

    def forward(self, x):
        # 卷积操作
        out = self.conv1(x)
        # ReLU激活
        out = nn.ReLU()(out)
        # 再次卷积操作
        out = self.conv2(out)
        # 将卷积后的输出与输入数据相加，得到残差块的输出
        out += x
        return out


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 卷积层
        self.conv1 = nn.Conv2d(1, 16, kernel_size=5)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=5)
        # 通道注意力层
        self.ca1 = ChannelAttention(16)
        self.ca2 = ChannelAttention(32)
        # （空间注意力层） 全局平均池化层和全局最大池化层
        self.spatial_attention1 = SpatialAttention(16)
        self.spatial_attention2 = SpatialAttention(32)
        # 残差块
        self.res1 = ResBlock(16, 16)
        self.res2 = ResBlock(32, 32)
        # 批处理层
        self.bn1 = nn.BatchNorm2d(16)
        self.bn2 = nn.BatchNorm2d(32)
        # 池化层
        self.pool = nn.MaxPool2d(kernel_size=2)
        # 激活层
        self.active1 = nn.ReLU()
        self.active2 = nn.PReLU()
        # 暂退层
        # 全连接层
        self.liner1 = nn.Linear(576, 10)
        self.liner2 = nn.Linear(800, 10)
        self.liner3 = nn.Linear(2912, 800)

    def forward(self, x):
        # 自主特征提取模块1
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.active2(x)
        x = self.ca1(x)
        x = self.spatial_attention1(x)
        x = self.pool(x)
        x = self.res1(x)
        # 自主特征提取模块2
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.active2(x)
        x = self.ca2(x)
        x = self.spatial_attention2(x)
        x = self.pool(x)
        x = self.res2(x)
        # 分类器
        x = x.view(x.size(0), -1)
        x = self.liner3(x)
        x = self.liner2(x)

        return x

model = Net()
# print(model)

# 加载已经训练好的模型
# checkpoint = torch.load('models/CAR_99.48381696428571.pth')
# model.load_state_dict(checkpoint['model_state_dict'])
model = torch.load('models/N15_M07_F04/CAR_99.81863839285714.pth',  map_location=torch.device('cpu'))



def Min_Max_Scaling_2(data):
    data_min = np.min(data)
    data_max = np.max(data)
    data_norm = 2 * (data - data_min) / (data_max - data_min) - 1
    return data_norm

def Min_Max_Scaling(data):
    data_norm = (data - np.min(data)) / (np.max(data) - np.min(data))
    return data_norm

# 获取最后一个隐藏层的输出
model.eval()
with torch.no_grad():
    for images, labels in dataloader:
        # print(len(labels))
        # print(labels)
        output = model(images)
        # print(max(output).item())
        # labels = model(labels)
        # last_hidden_layer = model.liner3.weight
# print(output.shape)
# print(output)
# 使用T-SNE将高维特征映射为二维特征向量
tsne = TSNE(n_components=2, random_state=0, perplexity=50)
X_tsne = tsne.fit_transform(output.detach().numpy())
X_tsne = Min_Max_Scaling(X_tsne)
# print(X_tsne.shape)
# print(X_tsne)
# df = pd.DataFrame(X_tsne)
# df.to_csv('N15_M07_F04_Tsne_data.csv', index=False)
# import matplotlib.cm as cm
from matplotlib.colors import ListedColormap
import matplotlib as mpl
# 可视化结果
plt.figure(figsize=(10, 10))
# 设置颜色映射
colors = ['#76D69C', '#27834B', '#1B5632']
cmap = ListedColormap(colors)
# 设置全局字体
mpl.rcParams['font.family'] = 'Times New Roman'
mpl.rcParams['font.size'] = 36
# 绘制散点图
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=labels, cmap=cmap)
# 添加图例
unique_labels = np.unique(labels)
for label in unique_labels:
    plt.scatter([], [], color=cmap(label), label=label) # 绘制一个空的散点图，并指定颜色和标签
plt.legend(markerscale=2)
plt.title('N15_M07_F04')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()