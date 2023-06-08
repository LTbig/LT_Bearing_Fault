import numpy as np
import matplotlib.pyplot as plt

# 生成时间序列
t = np.linspace(0, 1, 1000)

# 生成三相电流信号 相位差120
i1 = np.sin(2 * np.pi * 50 * t)
i2 = np.sin(2 * np.pi * 50 * t + 2 * np.pi / 3)
i3 = np.sin(2 * np.pi * 50 * t + 4 * np.pi / 3)

# 绘制波形
plt.title("3 phase_current")
plt.plot(t, i1, label='I1')
plt.plot(t, i2, label='I2')
plt.plot(t, i3, label='I3')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.legend()
plt.xlim(0, 0.1)
plt.show()