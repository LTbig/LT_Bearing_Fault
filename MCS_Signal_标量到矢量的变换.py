from scipy.io import loadmat
import matplotlib.pyplot as plt
import pywt
import numpy as np
import scipy.signal as signal
import math

class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data
# 滤波和去噪处理
def filter(signal_1, signal_2):
    # # fs = 10000  # 采样频率
    # fs = 64000
    # fc = 300  # 截止频率
    # order = 4  # 滤波器阶数
    # b, a = signal.butter(order, fc / (fs / 2), 'lowpass')
    # current1_filtered = signal.filtfilt(b, a, signal_1)
    # current2_filtered = signal.filtfilt(b, a, signal_2)
    current1_filtered = waverec(signal_1)
    current2_filtered = waverec(signal_2)
    # 计算相电流1和相电流2的均值，作为基准值
    # current1_mean = np.mean(current1_filtered)
    # print(current1_mean)
    # current2_mean = np.mean(current2_filtered)
    # print(current2_mean)
    # print("均值的差值:", current2_mean - current1_mean)
    # 计算相电流1和相电流2与基准值之间的差异值，得到相电流差值
    current_diff = current1_filtered - current2_filtered
    current_add = current1_filtered + current2_filtered
    current_multiplication = current1_filtered * current2_filtered
    current_seta = np.arctan(current1_filtered / current2_filtered)
    return Min_Max_Scaling_2(current1_filtered), Min_Max_Scaling_2(current2_filtered), \
           Min_Max_Scaling_2(current_diff), Min_Max_Scaling_2(current_add), \
            Min_Max_Scaling_2(current_multiplication), Min_Max_Scaling_2(current_seta)

def waverec(signal):
    coeffs = pywt.wavedec(signal, 'db8', level=8)
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
    # 展示数据信息
    print("=======================X======================")
    print(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['X'])
    print("=======================Y======================")
    print(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0])
    # 滤波和去噪
    s11, s12, s13, s14, s15, s16 = filter(signal_1=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0],
               signal_2=N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0])
    '''
    2.OuterFault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    # 滤波和去噪
    s21, s22, s23, s24, s25, s26 = filter(signal_1=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][1][2][0],
               signal_2=N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][2][2][0])
    '''
    3.InnerFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    s31, s32, s33, s34, s35, s36 = filter(signal_1=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][1][2][0],
               signal_2=N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][2][2][0])

    '''
    4.OuterFault+InnerFault
    '''
    # KB27
    N09_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_1')
    s41, s42, s43, s44, s45, s46 = filter(signal_1=N09_M07_F10_KB27_1.data['N09_M07_F10_KB27_1']['Y'][0][0][0][1][2][0],
               signal_2=N09_M07_F10_KB27_1.data['N09_M07_F10_KB27_1']['Y'][0][0][0][2][2][0])
    '''
    5.InnerFault+OuterFault
    '''
    # KB24
    N09_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_1')
    s51, s52, s53, s54, s55, s56 = filter(signal_1=N09_M07_F10_KB24_1.data['N09_M07_F10_KB24_1']['Y'][0][0][0][1][2][0],
               signal_2=N09_M07_F10_KB24_1.data['N09_M07_F10_KB24_1']['Y'][0][0][0][2][2][0])
    # phase_current
    # plt.title("N09_M07_F10  phase_current")
    '''
     1.NORMAL
     '''
    plt.plot(s11, label="NORMAL 1")
    plt.plot(s12, label="NORMAL 2")
    # plt.plot(s13, label="NORMAL 2 subtract 1")
    # plt.plot(s14, label="NORMAL 2 add 1")
    # plt.plot(s15, label="NORMAL 2 Multi 1")
    # plt.plot(s16, label="NORMAL arc (2/1)")
    '''
    2.OuterFault
    '''
    # plt.plot(s21, label="OuterFault 1")
    # plt.plot(s22, label="OuterFault 2")
    # plt.plot(s23, label="OuterFault 2 subtract 1")
    # plt.plot(s24, label="OuterFault 2 add 1")
    # plt.plot(s25, label="OuterFault 2 Multi 1")
    # plt.plot(s26, label="OuterFault arc (2/1)")
    '''
    3.InnerFault
    '''
    # plt.plot(s31, label="InnerFault 1")
    # plt.plot(s32, label="InnerFault 2")
    # plt.plot(s33, label="InnerFault 2 subtract 1")
    # plt.plot(s34, label="InnerFault 2 add 1")
    # plt.plot(s35, label="InnerFault 2 Multi 1")
    # plt.plot(s36, label="InnerFault arc (2/1)")
    '''
    4.OuterFault+InnerFault
    '''
    # plt.plot(s41, label="OuterFault+InnerFault 1")
    # plt.plot(s42, label="OuterFault+InnerFault 2")
    # plt.plot(s43, label="OuterFault+InnerFault 2 subtract 1")
    # plt.plot(s44, label="OuterFault+InnerFault 2 add 1")
    # plt.plot(s45, label="OuterFault+InnerFault 2 Multi 1")
    # plt.plot(s46, label="OuterFault+InnerFault arc (2/1)")
    '''
    5.InnerFault+OuterFault
    '''
    # plt.plot(s51, label="InnerFault+OuterFault 1")
    # plt.plot(s52, label="InnerFault+OuterFault 2")
    # plt.plot(s53, label="InnerFault+OuterFault 2 subtract 1")
    # plt.plot(s54, label="InnerFault+OuterFault 2 add 1")
    # plt.plot(s55, label="InnerFault+OuterFault 2 Multi 1")
    # plt.plot(s56, label="InnerFault+OuterFault arc (2/1)")

    # plt.xlim(0, 2560)
    plt.xlim(0, 2560)
    # plt.legend()
    plt.show()

    # subtract
    plt.figure(figsize=(16, 9))
    plt.suptitle("Subtract")
    plt.subplots_adjust(hspace=0.3)

    plt.subplot(511)
    plt.title("NORMAL")
    plt.plot(s13, label="NORMAL 2 subtract 1")
    # s13_data = s13[0:2560]
    # print(len(s13_data))
    # for i in range(len(s13_data)):
    #     print(i+1)
    # for i in range(len(s13_data)):
    #     print(s13[i])
    # print("===s13====")
    plt.xlim(0, 2560)


    plt.subplot(512)
    plt.title("OR")
    plt.plot(s23, label="OuterFault 2 subtract 1")
    # s23_data = s23[0:2560]
    # for i in range(len(s23_data)):
    #     print(s23[i])
    # print("===s23====")
    plt.xlim(0, 2560)


    plt.subplot(513)
    plt.title("IR")
    plt.plot(s33, label="InnerFault 2 subtract 1")
    # s33_data = s33[0:2560]
    # for i in range(len(s33_data)):
    #     print(s33[i])
    # print("===s33====")
    plt.xlim(0, 2560)


    plt.subplot(514)
    plt.title("OR_IR")
    plt.plot(s43, label="OuterFault+InnerFault 2 subtract 1")
    # s43_data = s43[0:2560]
    # for i in range(len(s43_data)):
    #     print(s43[i])
    # print("===s43====")
    plt.xlim(0, 2560)


    plt.subplot(515)
    plt.title("IR_OR")
    plt.plot(s53, label="InnerFault+OuterFault 2 subtract 1")
    s53_data = s53[0:2560]
    # for i in range(len(s53_data)):
    #     print(s53[i])
    # print("===s53====")
    plt.xlim(0, 2560)

    plt.show()

    # add
    plt.figure(figsize=(16, 9))
    plt.suptitle("Add")
    plt.subplots_adjust(hspace=0.3)

    plt.subplot(511)
    plt.title("NORMAL")
    plt.plot(s14, label="NORMAL 2 add 1")
    # s14_data = s14[0:2560]
    # for i in range(len(s14_data)):
    #     print(s14[i])
    # print("===s14====")
    plt.xlim(0, 2560)

    plt.subplot(512)
    plt.title("OR")
    plt.plot(s24, label="OuterFault 2 add 1")
    # s24_data = s24[0:2560]
    # for i in range(len(s24_data)):
    #     print(s24[i])
    # print("===s24====")
    plt.xlim(0, 2560)

    plt.subplot(513)
    plt.title("IR")
    plt.plot(s34, label="InnerFault 2 add 1")
    # s34_data = s34[0:2560]
    # for i in range(len(s34_data)):
    #     print(s34[i])
    # print("===s34====")
    plt.xlim(0, 2560)

    plt.subplot(514)
    plt.title("OR_IR")
    plt.plot(s44, label="OuterFault+InnerFault 2 add 1")
    # s44_data = s44[0:2560]
    # for i in range(len(s44_data)):
    #     print(s44[i])
    # print("===s44====")
    plt.xlim(0, 2560)

    plt.subplot(515)
    plt.title("IR_OR")
    plt.plot(s54, label="InnerFault+OuterFault 2 add 1")
    # s54_data = s54[0:2560]
    # for i in range(len(s54_data)):
    #     print(s54[i])
    # print("===s54====")
    plt.xlim(0, 2560)

    plt.show()

    # multi
    plt.figure(figsize=(16, 9))
    plt.suptitle("Multi")
    plt.subplots_adjust(hspace=0.3)

    plt.subplot(511)
    plt.title("NORMAL")
    plt.plot(s15, label="NORMAL 2 multi 1")
    # s15_data = s15[0:2560]
    # for i in range(len(s15_data)):
    #     print(s15[i])
    # print("===s15====")
    plt.xlim(0, 2560)

    plt.subplot(512)
    plt.title("OR")
    plt.plot(s25, label="OuterFault 2 multi 1")
    # s25_data = s25[0:2560]
    # for i in range(len(s25_data)):
    #     print(s25[i])
    # print("===s25====")
    plt.xlim(0, 2560)

    plt.subplot(513)
    plt.title("IR")
    plt.plot(s35, label="InnerFault 2 multi 1")
    # s35_data = s35[0:2560]
    # for i in range(len(s35_data)):
    #     print(s35[i])
    # print("===s35====")
    plt.xlim(0, 2560)

    plt.subplot(514)
    plt.title("OR_IR")
    plt.plot(s45, label="OuterFault+InnerFault 2 multi 1")
    # s45_data = s45[0:2560]
    # for i in range(len(s45_data)):
    #     print(s45[i])
    # print("===s45====")
    plt.xlim(0, 2560)

    plt.subplot(515)
    plt.title("IR_OR")
    plt.plot(s55, label="InnerFault+OuterFault 2 multi 1")
    # s55_data = s55[0:2560]
    # for i in range(len(s55_data)):
    #     print(s55[i])
    # print("===s55====")
    plt.xlim(0, 2560)
    plt.show()

    # arctan
    plt.figure(figsize=(16, 9))
    plt.suptitle("Arctan")
    plt.subplots_adjust(hspace=0.3)

    plt.subplot(511)
    plt.title("NORMAL")
    plt.plot(s16, label="NORMAL 2 arctan 1")
    # s16_data = s16[0:2560]
    # for i in range(len(s16_data)):
    #     print(s16[i])
    # print("===s16====")
    plt.xlim(0, 2560)

    plt.subplot(512)
    plt.title("OR")
    plt.plot(s26, label="OuterFault 2 arctan 1")
    # s26_data = s26[0:2560]
    # for i in range(len(s26_data)):
    #     print(s26[i])
    # print("===s26====")
    plt.xlim(0, 2560)

    plt.subplot(513)
    plt.title("IR")
    plt.plot(s36, label="InnerFault 2 arctan 1")
    # s36_data = s36[0:2560]
    # for i in range(len(s36_data)):
    #     print(s36[i])
    # print("===s36====")
    plt.xlim(0, 2560)

    plt.subplot(514)
    plt.title("OR_IR")
    plt.plot(s46, label="OuterFault+InnerFault 2 arctan 1")
    # s46_data = s46[0:2560]
    # for i in range(len(s46_data)):
    #     print(s46[i])
    # print("===s46====")
    plt.xlim(0, 2560)

    plt.subplot(515)
    plt.title("IR_OR")
    plt.plot(s56, label="InnerFault+OuterFault 2 arctan 1")
    # s56_data = s56[0:2560]
    # for i in range(len(s56_data)):
    #     print(s56[i])
    # print("===s56====")
    plt.xlim(0, 2560)

    plt.show()


    print("done!")
