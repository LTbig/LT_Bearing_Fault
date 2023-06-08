import torch
import torch.nn as nn
import torch.nn.functional as F

class SpatialAttention(nn.Module):
    def __init__(self):
        super(SpatialAttention, self).__init__()
        self.conv = nn.Conv2d(16, 1, kernel_size=7, padding=3)

    def forward(self, x):
        # 卷积操作
        out = self.conv(x)
        # 对卷积后的输出数据进行softmax操作
        out = F.softmax(out, dim=1)
        # 将得到的权重与原始输入数据相乘，得到加权后的输出数据
        out = x * out
        return out

# 测试代码
if __name__ == '__main__':
    x = torch.randn(1, 16, 20, 32)
    sa = SpatialAttention()
    out = sa(x)
    print(out.shape)  # 输出大小为20*32