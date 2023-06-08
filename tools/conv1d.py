import torch.nn as nn
import torch

# 定义一个一维卷积层
conv1d = nn.Conv1d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)

# 定义输入数据，假设输入数据的长度为10，特征数为1
input_data_1 = torch.randn(1, 1, 10)


# 定义输入数据，假设输入数据的长度为100，特征数为20
input_data_20 = torch.randn(20, 1, 100)

# 进行一维卷积操作
output_data_1 = conv1d(input_data_1)
output_data_20 = conv1d(input_data_20)

# 输出卷积后的数据形状
print(output_data_1.shape)  # 输出 (1, 16, 10)
print(output_data_20.shape)
