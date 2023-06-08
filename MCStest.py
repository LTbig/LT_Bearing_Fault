import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt
import pywt


class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data

def waverec(signal):
    coeffs = pywt.wavedec(signal, 'db8', level=4)
    # 将小波系数中的高频分量置零
    coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]
    # 重构信号
    reconstructed_signal = pywt.waverec(coeffs, 'db8')
    return reconstructed_signal

#  数据归一化处理 数据归一化到[0, 1]
def Min_Max_Scaling(data):
    data_norm = (data - np.min(data)) / (np.max(data) - np.min(data))
    return data_norm

# 数据归一化 数据归一化到[-1, 1]
def Min_Max_Scaling_2(data):
    data_min = np.min(data)
    data_max = np.max(data)
    data_norm = 2 * (data - data_min) / (data_max - data_min) - 1
    return data_norm

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
    # 数据归一化
    Min_Max_Scaling11 = Min_Max_Scaling_2(data=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0])
    Min_Max_Scaling21 = Min_Max_Scaling_2(data=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0])
    # 进行小波变换
    waverec11 = waverec(signal=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0])
    waverec21 = waverec(signal=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    Min_Max_Scaling12 = Min_Max_Scaling_2(data=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][1][2][0])
    Min_Max_Scaling22 = Min_Max_Scaling_2(data=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][2][2][0])
    waverec12 = waverec(signal=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][1][2][0])
    waverec22 = waverec(signal=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][2][2][0])

    '''
    3.InnerFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    Min_Max_Scaling13 = Min_Max_Scaling_2(data=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][1][2][0])
    Min_Max_Scaling23 = Min_Max_Scaling_2(data=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][2][2][0])
    waverec13 = waverec(signal=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][1][2][0])
    waverec23 = waverec(signal=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][2][2][0])

    # phase_current_1
    plt.title("N09_M07_F10 phase_current_1")
    plt.plot(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0], label="normal phase_current_1")
    plt.plot(N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][1][2][0], label="OuterFault phase_current_1")
    plt.plot(N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][1][2][0], label="InnerFault phase_current_1")
    plt.xlim(0, 4266)
    plt.legend()
    plt.show()

    # nor phase_current_1
    plt.title("N09_M07_F10 compare nor phase_current_1")
    plt.plot(Min_Max_Scaling11, label="normal nor phase_current_1")
    plt.plot(Min_Max_Scaling12, label="OuterFault nor phase_current_1")
    plt.plot(Min_Max_Scaling13, label="InnerFault nor phase_current_1")
    plt.xlim(0, 4266)
    plt.legend()
    plt.show()

    # wave phase_current_1
    plt.title("N09_M07_F10 compare wave phase_current_1")
    plt.plot(waverec11, label="normal wave phase_current_1")
    plt.plot(waverec12, label="OuterFault wave  phase_current_1")
    plt.plot(waverec13, label="InnerFault wave phase_current_1")
    plt.xlim(0, 4266)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N09_M07_F10 compare phase_current_2")
    plt.plot(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0], label="normal phase_current_2")
    plt.plot(N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][2][2][0], label="OuterFault phase_current_2")
    plt.plot(N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][2][2][0], label="InnerFault phase_current_2")
    plt.xlim(0, 4266)
    plt.legend()
    plt.show()

    # nor phase_current_2
    plt.title("N09_M07_F10 compare nor phase_current_1")
    plt.plot(Min_Max_Scaling21, label="normal nor phase_current_2")
    plt.plot(Min_Max_Scaling22, label="OuterFault nor phase_current_2")
    plt.plot(Min_Max_Scaling23, label="InnerFault nor phase_current_2")
    plt.xlim(0, 4266)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N09_M07_F10 compare wave phase_current_2")
    plt.plot(waverec21, label="normal wave phase_current_2")
    plt.plot(waverec22, label="OuterFault wave  phase_current_2")
    plt.plot(waverec23, label="InnerFault wave phase_current_2")
    plt.xlim(0, 4266)
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
    waverec11 = waverec(signal=N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][1][2][0])
    waverec21 = waverec(signal=N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][2][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M01_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_1')
    waverec12 = waverec(signal=N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][1][2][0])
    waverec22 = waverec(signal=N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][2][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M01_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_1')
    waverec13 = waverec(signal=N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][1][2][0])
    waverec23 = waverec(signal=N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][2][2][0])

    # phase_current_1
    plt.title("N15_M01_F10 phase_current_1")
    plt.plot(N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][1][2][0], label="normal phase_current_1")
    plt.plot(N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][1][2][0], label="OuterFault phase_current_1")
    plt.plot(N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][1][2][0], label="InnerFault phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # wave phase_current_1
    plt.title("N15_M01_F10 compare wave phase_current_1")
    plt.plot(waverec11, label="normal wave phase_current_1")
    plt.plot(waverec12, label="OuterFault wave  phase_current_1")
    plt.plot(waverec13, label="InnerFault wave phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M01_F10 compare phase_current_2")
    plt.plot(N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][2][2][0], label="normal phase_current_2")
    plt.plot(N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][2][2][0], label="OuterFault phase_current_2")
    plt.plot(N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][2][2][0], label="InnerFault phase_current_2")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M01_F10 compare wave phase_current_2")
    plt.plot(waverec21, label="normal wave phase_current_2")
    plt.plot(waverec22, label="OuterFault wave  phase_current_2")
    plt.plot(waverec23, label="InnerFault wave phase_current_2")
    plt.xlim(0, 2560)
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
    waverec11 = waverec(signal=N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][1][2][0])
    waverec21 = waverec(signal=N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][2][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M07_F04_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_1')
    waverec12 = waverec(signal=N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][1][2][0])
    waverec22 = waverec(signal=N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][2][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M07_F04_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_1')
    waverec13 = waverec(signal=N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][1][2][0])
    waverec23 = waverec(signal=N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][2][2][0])

    # phase_current_1
    plt.title("N15_M07_F04 phase_current_1")
    plt.plot(N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][1][2][0], label="normal phase_current_1")
    plt.plot(N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][1][2][0], label="OuterFault phase_current_1")
    plt.plot(N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][1][2][0], label="InnerFault phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # wave phase_current_1
    plt.title("N15_M07_F04 compare wave phase_current_1")
    plt.plot(waverec11, label="normal wave phase_current_1")
    plt.plot(waverec12, label="OuterFault wave  phase_current_1")
    plt.plot(waverec13, label="InnerFault wave phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M07_F04 compare phase_current_2")
    plt.plot(N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][2][2][0], label="normal phase_current_2")
    plt.plot(N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][2][2][0], label="OuterFault phase_current_2")
    plt.plot(N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][2][2][0], label="InnerFault phase_current_2")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M07_F04 compare wave phase_current_2")
    plt.plot(waverec21, label="normal wave phase_current_2")
    plt.plot(waverec22, label="OuterFault wave  phase_current_2")
    plt.plot(waverec23, label="InnerFault wave phase_current_2")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    '''
    读取N15_M07_F10数据
    '''
    N15_M07_F10_ALL = []
    '''
    1.NORMAL
    '''
    # K001
    N15_M07_F10_K001_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_1')
    # 进行小波变换
    waverec11 = waverec(signal=N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][1][2][0])
    waverec21 = waverec(signal=N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][2][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N15_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_1')
    waverec12 = waverec(signal=N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][1][2][0])
    waverec22 = waverec(signal=N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][2][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N15_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_1')
    waverec13 = waverec(signal=N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][1][2][0])
    waverec23 = waverec(signal=N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][2][2][0])

    # phase_current_1
    plt.title("N15_M07_F10 phase_current_1")
    plt.plot(N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][1][2][0], label="normal phase_current_1")
    plt.plot(N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][1][2][0], label="OuterFault phase_current_1")
    plt.plot(N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][1][2][0], label="InnerFault phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # wave phase_current_1
    plt.title("N15_M07_F10 compare wave phase_current_1")
    plt.plot(waverec11, label="normal wave phase_current_1")
    plt.plot(waverec12, label="OuterFault wave  phase_current_1")
    plt.plot(waverec13, label="InnerFault wave phase_current_1")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M07_F10 compare phase_current_2")
    plt.plot(N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][2][2][0], label="normal phase_current_2")
    plt.plot(N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][2][2][0], label="OuterFault phase_current_2")
    plt.plot(N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][2][2][0], label="InnerFault phase_current_2")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    # phase_current_2
    plt.title("N15_M07_F10 compare wave phase_current_2")
    plt.plot(waverec21, label="normal wave phase_current_2")
    plt.plot(waverec22, label="OuterFault wave  phase_current_2")
    plt.plot(waverec23, label="InnerFault wave phase_current_2")
    plt.xlim(0, 2560)
    plt.legend()
    plt.show()

    print("done!")
