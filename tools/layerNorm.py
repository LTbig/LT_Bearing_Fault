import numpy as np
import matplotlib.pyplot as plt

# 生成示意数据
x = np.arange(0, 10, 0.1)
y1 = np.random.normal(0, 1, len(x))
y2 = np.random.normal(5, 1, len(x))

# 计算Layer Normalization后的结果
eps = 1e-8
y1_norm = (y1 - np.mean(y1)) / np.sqrt(np.var(y1) + eps)
y2_norm = (y2 - np.mean(y2)) / np.sqrt(np.var(y2) + eps)

# 绘制图形
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y1_norm, label='y1_norm')
ax.plot(x, y2_norm, label='y2_norm')
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Layer Normalization')
plt.show()