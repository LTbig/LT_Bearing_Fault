import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 卷积层
        self.conv1 = nn.Conv1d(1, 16, kernel_size=5, stride=1, padding=2)
        self.conv2 = nn.Conv1d(16, 32, kernel_size=5, stride=1, padding=2)
        # 激活层
        self.active1 = nn.ReLU()
        # 暂退层
        self.back1 = nn.Dropout()
        # 全连接层
        self.fc1 = nn.Linear(81920, 2560)
        self.fc2 = nn.Linear(2560, 256)
        self.fc3 = nn.Linear(256, 10)

    def forward(self, x):

        x = self.conv1(x)
        self.active1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        x = self.active1(x)
        x = self.back1(x)
        x = self.fc2(x)
        x = self.back1(x)
        x = self.fc3(x)
        return x


if __name__ == '__main__':
    # Create a network instance
    net = Net()
    input = torch.ones(32, 1, 2560)  # 32 是指批量大小
    output = net(input)
    print(output.shape)

