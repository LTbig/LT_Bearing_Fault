import numpy as np
import matplotlib.pyplot as plt

# 生成一维信号
N = 40*64
x = np.sin(np.arange(N) * np.pi / 10)

# 将信号升成二维
X = np.zeros((40, 64))
for i in range(40):
    for j in range(64):
        if i >= j:
            X[i, j] = x[i-j]
        else:
            X[i, j] = x[0]

# 绘制热力图
plt.imshow(X, cmap='hot', aspect='auto')
plt.colorbar()
plt.show()