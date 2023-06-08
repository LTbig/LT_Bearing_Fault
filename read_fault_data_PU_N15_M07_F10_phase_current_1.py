import matplotlib.pyplot as plt
import pywt
from read_data_PU_subject import load_N15_M07_F10_data_phase_current_1
import numpy as np


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
    coeffs = pywt.wavedec(signal, 'db4', level=4)
    # 将小波系数中的高频分量置零
    coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]
    # 重构信号
    reconstructed_signal = pywt.waverec(coeffs, 'db4')
    return reconstructed_signal

def waverec2(signal):
    coeffs = pywt.wavedec(signal, 'db1', level=5)
    # 将小波系数中的高频分量置零
    coeffs[1:] = [np.zeros_like(v) for v in coeffs[1:]]
    # 重构信号
    reconstructed_signal = pywt.waverec(coeffs, 'db1')
    return reconstructed_signal

def cut_data(nu_arr, number):
    result_cut = []
    temp = []
    i = 1
    for value in nu_arr:
        if i % (number + 1) != 0:
            temp.append(value)
        else:
            result_cut.append(Min_Max_Scaling_2(waverec(np.array(temp))))
            temp = []
        i = i + 1
    return result_cut


def ready_data():
    '''
    1.加载德国帕德博恩轴承原始轴承数据
    '''

    PU_N15_M01_F10_data = load_N15_M07_F10_data_phase_current_1()
    print("PU_N15_M01_F10_data_length:", len(PU_N15_M01_F10_data))
    PU_data_n = PU_N15_M01_F10_data[0]
    PU_data_out = PU_N15_M01_F10_data[1]
    PU_data_in = PU_N15_M01_F10_data[2]


    '''
    2.处理原始轴承数据
    '''
    # 切割数据
    # cut_number = 864
    # cut_number = 1024
    cut_number = 2560
    PU_data_n_cut = cut_data(PU_data_n, cut_number)
    PU_data_in_cut = cut_data(PU_data_in, cut_number)
    PU_data_out_cut = cut_data(PU_data_out, cut_number)

    # 准备好数据包
    PU_data_n_cut_packge = []
    PU_data_in_cut_packge = []
    PU_data_out_cut_packge = []
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

    # 构造数据的label
    # ball_inch007_label，其中包含了len(ball_inch007_cut_512)个元素，每个元素都是一个只包含一个元素0的列表。
    PU_data_out_label = [[0] for index in range(len(PU_data_out_cut))]
    PU_data_in_label = [[1] for index in range(len(PU_data_in_cut))]
    PU_data_n_label = [[2] for index in range(len(PU_data_n_cut))]

    # 整合好数据和数据标签
    Fault_data = []
    Fault_data = Fault_data + PU_data_out_cut_packge + PU_data_in_cut_packge + PU_data_n_cut_packge

    Fault_label = []
    Fault_label = Fault_label + PU_data_out_label + PU_data_in_label + PU_data_n_label
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
