import numpy as np
from torch.utils.data import DataLoader, Dataset
from sklearn.manifold import TSNE
from read_fault_data_PU_N15_M07_F10_phase_current import ready_data
import torch
from torch import nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import pandas as pd

data = ready_data()  # 读取数据集

# 将数据升为2维数据
temp = []
for i in range(len(data)):
    # temp = data[i][0].reshape(24, 36)
    # temp = data[i][0].reshape(32, 32)
    temp = data[i][0].reshape(40, 64)
    data[i][0] = temp
temp = []
print("data length:", len(data))
print("shape", data[0][0].shape)
x1 = data[0][0]
x2 = data[1][0]
x3 = data[2][0]
x4 = data[3][0]
x5 = data[4][0]
x6 = data[5][0]
x7 = data[6][0]
x8 = data[7][0]



# 绘制热力图
plt.figure(figsize=(16, 9))
plt.subplot(421)
plt.imshow(x1, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(422)
plt.imshow(x2, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(423)
plt.imshow(x3, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(424)
plt.imshow(x4, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(425)
plt.imshow(x5, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(426)
plt.imshow(x6, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(427)
plt.imshow(x7, cmap='hot', aspect='auto')
plt.colorbar()

plt.subplot(428)
plt.imshow(x8, cmap='hot', aspect='auto')
plt.colorbar()

plt.show()


