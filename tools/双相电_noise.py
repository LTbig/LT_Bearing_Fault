import numpy as np
import matplotlib.pyplot as plt

# 生成时间序列
t = np.linspace(0, 1, 1000)
# 生成I1和I2正弦波
I0 = 1.0
w = 10 * np.pi
I1 = I0 * np.sin(w * t)
I2 = I0 * np.sin(w * t + np.pi / 2)

# 添加高斯噪声
mean = 0.0
std = 0.1
noise = np.random.normal(mean, std, len(t))
I1_noisy = I1 + noise
for i in range(len(I1_noisy)):
    print(i)
print("========1=================================")
for i in range(len(t)):
    print(I1_noisy[i])
print("========2=================================")
I2_noisy = I2 + noise
for i in range(len(I2_noisy)):
    print(I2_noisy[i])
print("========3================================")

# 绘制带噪音的双相电流波形
plt.plot(t, I1_noisy, label='1')
plt.plot(t, I2_noisy, label='2')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Current')
plt.xlim(0, 0.5)
plt.show()