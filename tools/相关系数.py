import numpy as np

# 生成两个信号
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# 计算两个信号的互相关系数
N = len(x)
x_mean = np.mean(x)
y_mean = np.mean(y)
std_x = np.std(x)
std_y = np.std(y)
rxy = (1/N) * np.sum((x - x_mean) * (y - y_mean)) / (std_x * std_y)

print('信号x：', x)
print('信号y：', y)
print('互相关系数rxy：', rxy)