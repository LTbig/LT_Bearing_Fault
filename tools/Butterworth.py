import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt

# 定义滤波器参数
fc1 = 100 # 低截止频率
fc2 = 1000 # 高截止频率
fs = 8000 # 采样率
order = 6 # 滤波器阶数

# 计算滤波器系数
nyq = 0.5 * fs
low = fc1 / nyq
high = fc2 / nyq
b, a = butter(order, [low, high], btype='band')

# 滤波器应用
np.random.seed(0)
t = np.linspace(0, 1, 10000, False)
input_signal = np.random.randn(len(t))
output_signal = lfilter(b, a, input_signal)

# 绘制滤波前后信号的频谱图
w, h = freqz(b, a)
f = w * fs / (2 * np.pi)
input_spectrum = np.abs(np.fft.fft(input_signal)[:len(input_signal)//2+1])
output_spectrum = np.abs(np.fft.fft(output_signal)[:len(output_signal)//2+1])
fig, ax = plt.subplots(2, 1)
ax[0].plot(f, input_spectrum)
ax[0].set_title('Input Spectrum')
ax[0].set_xlabel('Frequency (Hz)')
ax[0].set_ylabel('Magnitude')
ax[1].plot(f, output_spectrum)
ax[1].set_title('Output Spectrum')
ax[1].set_xlabel('Frequency (Hz)')
ax[1].set_ylabel('Magnitude')
plt.show()