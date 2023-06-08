import torch
import torch.nn as nn


class ResBlock(nn.Module):
    def __init__(self):
        super(ResBlock, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels=16, out_channels=16, kernel_size=3, padding=1)

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


# 测试代码
if __name__ == '__main__':
    x = torch.randn(1, 16, 10, 16)
    res_block = ResBlock()
    out = res_block(x)
    print(out.shape)  # 输出大小为10*16
