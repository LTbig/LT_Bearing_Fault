import numpy as np
import matplotlib.pyplot as plt

# 生成包含高频噪声的信号
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 50 * t) + \
         np.sin(2 * np.pi * 100 * t) + 0.5 * np.random.randn(len(t))
plt.plot(t, signal)
plt.title('Signal with high frequency noise')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()

from scipy.signal import butter, filtfilt

# 设计Butterworth低通滤波器
fs = 1000  # 采样率
fc = 10  # 截止频率
n_order = 4  # 滤波器阶数
nyq = 0.5 * fs  # Nyquist频率
b, a = butter(n_order, fc/nyq, btype='low')

# 应用滤波器
filtered_signal = filtfilt(b, a, signal)

# 绘制滤波后的信号
plt.plot(t, filtered_signal)
plt.title('Signal after low-pass filtering')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()