import numpy as np
import matplotlib.pyplot as plt

# 生成时间序列
t = np.linspace(0, 1, 2560)

# 生成双相电流信号
i1 = np.sin(2 * np.pi * 50 * t)
for i in range(len(i1)):
    print(i1[i])
print("==============================1==============================")
i2 = np.sin(2 * np.pi * 50 * t + np.pi/2)
for i in range(len(i2)):
    print(i2[i])
print("=====================================2===============")

# 绘制波形
plt.title("2 phase current")
plt.plot(t, i1, label='1')
plt.plot(t, i2, label='2')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.xlim(0, 0.04)
plt.show()