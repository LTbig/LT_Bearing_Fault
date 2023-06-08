import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns
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
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3)
        self.conv3 = nn.Conv2d(16, 24, kernel_size=3)
        self.conv4 = nn.Conv2d(24, 32, kernel_size=3)
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
        self.bn1 = nn.BatchNorm2d(8)
        self.bn2 = nn.BatchNorm2d(16)
        self.bn3 = nn.BatchNorm2d(24)
        self.bn4 = nn.BatchNorm2d(32)
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

        x = self.conv2(x)
        x = self.bn2(x)
        x = self.active2(x)

        x = self.ca1(x)
        x = self.spatial_attention1(x)
        x = self.pool(x)
        x = self.res1(x)

        # 自主特征提取模块2
        x = self.conv3(x)
        x = self.bn3(x)
        x = self.active2(x)

        x = self.conv4(x)
        x = self.bn4(x)
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


if __name__ == '__main__':
    # Create a network instance
    net = Net()
    input = torch.ones(32, 1, 40, 64)  # batchSize channels  weight * height
    output = net(input)
    print(output.shape)

