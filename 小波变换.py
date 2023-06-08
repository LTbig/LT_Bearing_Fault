import pywt
import numpy as np
import matplotlib.pyplot as plt
# 构造原始信号，包含噪声
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.sin(2 * np.pi * 20 * t) + 0.2 * np.random.randn(len(t))

# 进行小波变换
coeffs = pywt.wavedec(signal, 'db4', level=4)

# 将小波系数中的高频分量置零
coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]

# 重构信号
reconstructed_signal = pywt.waverec(coeffs, 'db4')

# 绘制原始信号和去噪后的信号
plt.plot(t, signal, label='Original signal')
plt.plot(t, reconstructed_signal, label='Reconstructed signal')
plt.legend()
plt.show()