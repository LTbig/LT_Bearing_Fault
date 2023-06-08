import numpy as np
from scipy.signal import hilbert
from scipy.io import loadmat
import matplotlib.pyplot as plt
class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data

# 读取电流信号数据
N09_M07_F10_K001_1 = read_data_one_subject(
    'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_1')

# 提取电流信号
current_1 = N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0]
current_2 = N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0]

# 对电流信号进行希尔伯特变换，得到对应的复数信号
current_hilbert_1 = hilbert(current_1)
current_hilbert_2 = hilbert(current_2)

print("current_hilbert_1 length:", len(current_hilbert_1))
print(current_hilbert_1)
print("current_hilbert_2 length:", len(current_hilbert_2))
print(current_hilbert_2)
# 计算相位角
current_hilbert_1_phase1 = np.angle(current_hilbert_1)
current_hilbert_1_phase2 = np.angle(current_hilbert_1 * np.exp(1j * 2 * np.pi / 3))
current_hilbert_2_phase1 = np.angle(current_hilbert_2)
current_hilbert_2_phase2 = np.angle(current_hilbert_2 * np.exp(1j * 2 * np.pi / 3))

# 将相位信号转化为复数形式
current_hilbert_1_phase1_c1 = np.exp(1j * current_hilbert_1_phase1)
current_hilbert_1_phase2_c2 = np.exp(1j * current_hilbert_1_phase2)
current_hilbert_2_phase1_c1 = np.exp(1j * current_hilbert_2_phase1)
current_hilbert_2_phase2_c2 = np.exp(1j * current_hilbert_2_phase2)

# 进行矢量减法运算
current_1_fault_feature = current_hilbert_1_phase1_c1 - current_hilbert_1_phase2_c2
current_2_fault_feature = current_hilbert_2_phase1_c1 - current_hilbert_2_phase2_c2
print("current_1_fault_feature length:", len(current_1_fault_feature))
print(current_1_fault_feature)
print("current_2_fault_feature length:", len(current_2_fault_feature))
print(current_2_fault_feature)

fault_feature = current_2_fault_feature-current_1_fault_feature
print("fault_feature length:", len(fault_feature))
print(fault_feature)

plt.plot(current_1, label="current_1")
plt.xlim(0, 2560)
plt.show()

plt.plot(current_2, label="current_2")
plt.xlim(0, 2560)
plt.show()

plt.plot(current_1_fault_feature, label="current_1_fault_feature")
plt.xlim(0, 2560)
plt.show()

plt.plot(current_2_fault_feature, label="current_2_fault_feature")
plt.xlim(0, 2560)
plt.show()

plt.plot(fault_feature, label="fault_feature")
plt.xlim(0, 2560)
plt.show()