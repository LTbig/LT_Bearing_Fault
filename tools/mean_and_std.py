import numpy as np

# 假设我们有10个准确率值
accuracy = np.array([92.66304348,
95.10869565,
93.20652174,
94.02173913,
92.66304348,
95.65217391,
97.55434783

])

# 计算准确率的平均值和标准差
mean = np.mean(accuracy)
std = np.std(accuracy) # 样本标准差

print("平均准确率：", mean)
print("准确率标准差：", std)

import statistics

data = [99.94959677,
99.84879032,
99.49596774,
99.89919355,
99.84879032,
99.7983871,
99.7983871,
99.89919355,
99.94959677,
99.94959677
]

std_deviation = statistics.stdev(data)  # 总体标准差

print("标准差为:", std_deviation)