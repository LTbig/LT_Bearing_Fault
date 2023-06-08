import matplotlib.pyplot as plt

from read_data_PU_subject import load_N09_M07_F10_phase_current1_data
from read_data_PU_subject import load_N09_M07_F10_phase_current2_data
import numpy as np
import math
import scipy.signal as signal
import pywt
# 数据归一化 数据归一化到[-1, 1]
def Min_Max_Scaling_2(data):
    data_min = np.min(data)
    data_max = np.max(data)
    data_norm = 2 * (data - data_min) / (data_max - data_min) - 1
    return data_norm


#  数据归一化处理 数据归一化到[0, 1]
def Min_Max_Scaling(data):
    data_norm = (data - np.min(data)) / (np.max(data) - np.min(data))
    return data_norm

def waverec(signal):
    coeffs = pywt.wavedec(signal, 'db8', level=4)
    # 将小波系数中的高频分量置零
    coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]
    # 重构信号
    reconstructed_signal = pywt.waverec(coeffs, 'db8')
    return reconstructed_signal

def cut_data(nu_arr, number):
    result_cut = []
    temp = []
    i = 1
    for value in nu_arr:
        if i % (number + 1) != 0:
            temp.append(value)
        else:
            result_cut.append((np.array(temp)))
            temp = []
        i = i + 1
    return result_cut
'''
这段代码的作用是对输入的信号signal_1和signal_2进行低通滤波，并计算它们之间的差异值current_diff，
最后对current_diff进行最大最小值归一化处理后输出。
首先，该代码使用了scipy库的signal模块中的butter()函数，根据指定的截止频率、采样频率和滤波器阶数，生成了一个低通滤波器的系数b和a。
然后，使用filtfilt()函数对输入信号signal_1和signal_2进行滤波处理，得到了滤波后的信号current1_filtered和current2_filtered。
接着，代码计算了相电流1和相电流2之间的差异值current_diff，即current1_filtered减去current2_filtered。
最后，使用Min_Max_Scaling_2()函数对current_diff进行最大最小值归一化处理，并将结果作为函数的输出。
最大最小值归一化处理可以将数据映射到[0, 1]的区间内，使得不同数据之间的大小比较更加合理，便于进行后续的分析和处理。
例如，在该代码应用场景中，归一化处理可以将不同时间点上的相电流差异值统一到一个相同的尺度上，方便进行故障诊断和预测。
'''
def filter(signal_1):
    # fs = 10000  # 采样频率
    # fc = 50  # 截止频率
    # order = 4  # 滤波器阶数
    # b, a = signal.butter(order, fc / (fs / 2), 'low')
    # current1_filtered = signal.filtfilt(b, a, signal_1)
    # current2_filtered = signal.filtfilt(b, a, signal_2)
    # 计算相电流1和相电流2的均值，作为基准值
    # current1_mean = np.mean(current1_filtered)
    # print(current1_mean)
    # current2_mean = np.mean(current2_filtered)
    # print(current2_mean)
    current1_filtered = waverec(signal_1)
    # current2_filtered = waverec(signal_2)
    # 计算相电流1和相电流2与基准值之间的差异值，得到相电流差值
    # current_diff = current1_filtered - current2_filtered
    # current_add = current1_filtered + current2_filtered
    # current_multiplication = current1_filtered * current2_filtered
    # current_seta = np.arctan(current1_filtered / current2_filtered)
    return Min_Max_Scaling_2(current1_filtered)

def ready_data():
    '''
    1.加载德国帕德博恩轴承原始轴承数据
    '''

    PU_N09_M07_F10_data_1 = load_N09_M07_F10_phase_current1_data()
    print("PU_N09_M07_F10_data_1 length:", len(PU_N09_M07_F10_data_1))
    PU_data_n_1 = PU_N09_M07_F10_data_1[0]
    PU_data_out_1 = PU_N09_M07_F10_data_1[1]
    PU_data_in_1 = PU_N09_M07_F10_data_1[2]
    PU_data_inout_1 = PU_N09_M07_F10_data_1[3]
    PU_data_outin_1 = PU_N09_M07_F10_data_1[4]

    # PU_N09_M07_F10_data_2 = load_N09_M07_F10_phase_current2_data()
    # print("PU_N09_M07_F10_data_2 length:", len(PU_N09_M07_F10_data_2))
    # PU_data_n_2 = PU_N09_M07_F10_data_2[0]
    # PU_data_out_2 = PU_N09_M07_F10_data_2[1]
    # PU_data_in_2 = PU_N09_M07_F10_data_2[2]
    # PU_data_inout_2 = PU_N09_M07_F10_data_2[3]
    # PU_data_outin_2 = PU_N09_M07_F10_data_2[4]


    PU_data_n = filter(PU_data_n_1)
    PU_data_in = filter(PU_data_in_1)
    PU_data_out = filter(PU_data_out_1)
    PU_data_inout = filter(PU_data_inout_1)
    PU_data_outin = filter(PU_data_outin_1)
    '''
    2.处理轴承数据
    '''
    # 切割数据
    # cut_number = 864
    # cut_number = 1024
    cut_number = 2560
    PU_data_n_cut = cut_data(PU_data_n, cut_number)
    PU_data_in_cut = cut_data(PU_data_in, cut_number)
    PU_data_out_cut = cut_data(PU_data_out, cut_number)
    PU_data_inout_cut = cut_data(PU_data_inout, cut_number)
    PU_data_outin_cut = cut_data(PU_data_outin, cut_number)

    # 准备好数据包
    PU_data_n_cut_packge = []
    PU_data_in_cut_packge = []
    PU_data_out_cut_packge = []
    PU_data_inout_cut_packge = []
    PU_data_outin_cut_packge = []
    # 0
    j = []
    for i in PU_data_n_cut:
        j.append(i)
        PU_data_n_cut_packge.append(j)
        j = []
    # 1
    j = []
    for i in PU_data_in_cut:
        j.append(i)
        PU_data_in_cut_packge.append(j)
        j = []
    # 2
    j = []
    for i in PU_data_out_cut:
        j.append(i)
        PU_data_out_cut_packge.append(j)
        j = []
    # 3
    j = []
    for i in PU_data_inout_cut:
        j.append(i)
        PU_data_inout_cut_packge.append(j)
        j = []
    # 4
    j = []
    for i in PU_data_outin_cut:
        j.append(i)
        PU_data_outin_cut_packge.append(j)
        j = []


    # 构造数据的label
    # ball_inch007_label，其中包含了len(ball_inch007_cut_512)个元素，每个元素都是一个只包含一个元素0的列表。
    PU_data_out_label = [[0] for index in range(len(PU_data_out_cut))]
    PU_data_in_label = [[1] for index in range(len(PU_data_in_cut))]
    PU_data_outin_label = [[2] for index in range(len(PU_data_outin_cut))]
    PU_data_inout_label = [[3] for index in range(len(PU_data_inout_cut))]
    PU_data_n_label = [[4] for index in range(len(PU_data_n_cut))]

    # 整合好数据和数据标签
    Fault_data = []
    Fault_data = Fault_data + PU_data_out_cut_packge + PU_data_in_cut_packge + PU_data_outin_cut_packge + \
                 PU_data_inout_cut_packge + PU_data_n_cut_packge

    Fault_label = []
    Fault_label = Fault_label + PU_data_out_label + PU_data_in_label + PU_data_outin_label + \
                  PU_data_inout_label + PU_data_n_label
    Fault = []
    for data, label in zip(list(map(list, Fault_data)), Fault_label):
        Fault.append(data + label)
    return Fault


if __name__ == '__main__':
    data = ready_data()
    print("data length:", len(data))

    plt.Figure(figsize=(16, 9))
    plt.subplots_adjust(hspace=0.3, wspace=0.4)

    plt.subplot(331)
    plt.plot(data[0][0][:1024])

    plt.subplot(332)
    plt.plot(data[1][0])

    plt.subplot(333)
    plt.plot(data[2][0])

    plt.subplot(334)
    plt.plot(data[3][0])

    plt.subplot(335)
    plt.plot(data[4][0])

    plt.subplot(336)
    plt.plot(data[5][0])

    plt.subplot(337)
    plt.plot(data[6][0])

    plt.subplot(338)
    plt.plot(data[7][0])

    plt.subplot(339)
    plt.plot(data[8][0])

    # plt.subplot(3, 3, 10)
    # plt.plot(data[9][0])

    plt.show()
