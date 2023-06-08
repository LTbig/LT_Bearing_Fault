import numpy as np

# 生成一维数据
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 计算数据的平均值和标准差
mean = np.mean(data)
std = np.std(data)

# 进行数据标准化
data_standardized = (data - mean) / std

print(data_standardized)