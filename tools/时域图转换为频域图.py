import numpy as np
import matplotlib.pyplot as plt
# 数据归一化 数据归一化到[-1, 1]
def Min_Max_Scaling_2(data):
    data_min = np.min(data)
    data_max = np.max(data)
    data_norm = 2 * (data - data_min) / (data_max - data_min) - 1
    return data_norm
# 生成时域图
t = np.linspace(0, 1, 1000)
x = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t)
x_noraml = Min_Max_Scaling_2(x)
# 进行DFT并将时域图转换为频域图
y = np.fft.fft(x)
y_normal = Min_Max_Scaling_2(y)
# 计算频率轴
freq = np.fft.fftfreq(len(x), t[1] - t[0])
print(t[1] - t[0])
print(999*(t[1] - t[0]))
# 绘制时域图和频域图
plt.subplot(2, 1, 1)
plt.plot(t, x_noraml)
plt.title('Time Domain')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(y_normal))
# plt.plot(freq, y_normal)
plt.title('Frequency Domain')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.show()