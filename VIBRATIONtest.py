import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import pywt


class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data
'''
这段代码实现了一个基于小波变换的信号重构函数。具体步骤如下：
1. 使用PyWavelets库中的`wavedec`函数对输入信号进行小波分解，分解使用的小波基为'db1'，分解的层数为4，即将信号分解为4层小波系数。
2. 将小波系数中的高频分量置零，即将`coeffs`列表中从索引1开始的所有元素（对应高频小波系数）都赋值为一个与其形状相同但元素全为0的数组。
    这一步的作用是保留信号的低频部分，滤除高频噪声。
3. 使用PyWavelets库中的`waverec`函数对处理后的小波系数进行重构，重构使用的小波基仍为'db1'。重构得到的信号即为经过小波去噪后的信号。
4. 返回重构后的信号。
需要注意的是，由于小波变换是一种多尺度分析方法，因此在进行小波分解时需要指定分解的层数。
在这个例子中，选择了4层分解，因此重构出的信号将只保留原始信号的前4个尺度上的信息。
同时，由于小波变换可以非常有效地去除信号中的噪声，因此这个函数可以用于信号降噪等应用场景。
'''
def waverec(signal):
    coeffs = pywt.wavedec(signal, 'db4', level=4)
    # 将小波系数中的高频分量置零
    coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]
    # 重构信号
    reconstructed_signal = pywt.waverec(coeffs, 'db4')
    return reconstructed_signal

if __name__ == '__main__':
    '''
    读取N09_M07_F10数据
    '''
    N09_M07_F10_ALL = []
    '''
    1.NORMAL
    '''
    # K001
    N09_M07_F10_K001_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_1')
    # 进行小波变换
    waverec11 = waverec(signal=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][-1][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    waverec12 = waverec(signal=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    waverec13 = waverec(signal=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0])

    # Vibration
    plt.title("N09_M07_F10 compare Vibration")
    plt.plot(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][-1][2][0], label="normal Vibration ")
    plt.plot(N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0], label="OuterFault Vibration ")
    plt.plot(N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0], label="InnerFault Vibration ")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # wave Vibration
    plt.title("N09_M07_F10 compare wave Vibration")
    plt.plot(waverec11, label="normal wave Vibration")
    plt.plot(waverec12, label="OuterFault wave  Vibration")
    plt.plot(waverec13, label="InnerFault wave Vibration")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    '''
    读取N15_M07_F10数据
    '''
    N15_M07_F10_K001_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_1')
    # 进行小波变换
    waverec11 = waverec(signal=N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][-1][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_1')
    waverec12 = waverec(signal=N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_1')
    waverec13 = waverec(signal=N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0])

    # Vibration
    plt.title("N15_M07_F10 compare Vibration")
    plt.plot(N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][-1][2][0], label="normal Vibration ")
    plt.plot(N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0], label="OuterFault Vibration ")
    plt.plot(N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0], label="InnerFault Vibration ")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    # wave Vibration
    plt.title("N15_M07_F10 compare wave Vibration")
    plt.plot(waverec11, label="normal wave Vibration")
    plt.plot(waverec12, label="OuterFault wave  Vibration")
    plt.plot(waverec13, label="InnerFault wave Vibration")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    '''
     读取N15_M07_F04数据
     '''
    N15_M07_F04_ALL = []
    '''
    1.NORMAL
    '''
    # K001
    N15_M07_F04_K001_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_1')
    # 进行小波变换
    waverec11 = waverec(signal=N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][-1][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M07_F04_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_1')
    waverec12 = waverec(signal=N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][-1][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M07_F04_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_1')
    waverec13 = waverec(signal=N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][-1][2][0])

    # Vibration
    plt.title("N15_M07_F04 compare Vibration")
    plt.plot(N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][-1][2][0], label="normal Vibration ")
    plt.plot(N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][-1][2][0], label="OuterFault Vibration ")
    plt.plot(N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][-1][2][0], label="InnerFault Vibration ")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    # wave Vibration
    plt.title("N15_M07_F04 compare wave Vibration")
    plt.plot(waverec11, label="normal wave Vibration")
    plt.plot(waverec12, label="OuterFault wave  Vibration")
    plt.plot(waverec13, label="InnerFault wave Vibration")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    '''
    读取N15_M01_F10数据
    '''
    N15_M01_F10_ALL = []
    '''
    1.NORMAL
    '''
    # K001
    N15_M01_F10_K001_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_1')
    # 进行小波变换
    waverec11 = waverec(signal=N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][-1][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M01_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_1')
    waverec12 = waverec(signal=N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][-1][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M01_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_1')
    waverec13 = waverec(signal=N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][-1][2][0])

    # Vibration
    plt.title("N15_M01_F10 compare Vibration")
    plt.plot(N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][-1][2][0], label="normal Vibration ")
    plt.plot(N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][-1][2][0], label="OuterFault Vibration ")
    plt.plot(N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][-1][2][0], label="InnerFault Vibration ")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    # wave Vibration
    plt.title("N15_M01_F10 compare wave Vibration")
    plt.plot(waverec11, label="normal wave Vibration")
    plt.plot(waverec12, label="OuterFault wave  Vibration")
    plt.plot(waverec13, label="InnerFault wave Vibration")
    plt.xlim(2560, 5120)
    plt.legend()
    plt.show()

    print("done!")
