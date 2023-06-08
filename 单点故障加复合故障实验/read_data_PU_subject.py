import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt


class read_data_one_subject:
    def __init__(self, path):
        with open(path + '.mat', 'rb') as file:
            data = loadmat(file)
        self.data = data


'''
4种工况,判断故障类型
首先要保证 电机转速一样 扭矩一样 径向力一样

| 工况编号   | 转速 [rpm] | 负载 [Nm] | 径向力 [N] | 数据名前缀  |
| :------: | :--------: | :-------: | :--------: | :---------: |
|    0     |    1500    |    0.7    |    1000    | N15_M07_F10 |
|    1     |    900     |    0.7    |    1000    | N09_M07_F10 |
|    2     |    1500    |    0.1    |    1000    | N15_M01_F10 |
|    3     |    1500    |    0.7    |    400     | N15_M07_F04 |
'''


def load_N09_M07_F10_phase_current1_data():
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
    N09_M07_F10_K001_1 = N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][1][2][0].flatten()
    # N09_M07_F10_K001_MCS_1 = N09_M07_F10_K001_1.data[]

    N09_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_2')
    N09_M07_F10_K001_2 = N09_M07_F10_K001_2.data['N09_M07_F10_K001_2']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_3')
    N09_M07_F10_K001_3 = N09_M07_F10_K001_3.data['N09_M07_F10_K001_3']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_4')
    N09_M07_F10_K001_4 = N09_M07_F10_K001_4.data['N09_M07_F10_K001_4']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_5')
    N09_M07_F10_K001_5 = N09_M07_F10_K001_5.data['N09_M07_F10_K001_5']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_6')
    N09_M07_F10_K001_6 = N09_M07_F10_K001_6.data['N09_M07_F10_K001_6']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_7')
    N09_M07_F10_K001_7 = N09_M07_F10_K001_7.data['N09_M07_F10_K001_7']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_8')
    N09_M07_F10_K001_8 = N09_M07_F10_K001_8.data['N09_M07_F10_K001_8']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_9')
    N09_M07_F10_K001_9 = N09_M07_F10_K001_9.data['N09_M07_F10_K001_9']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_10')
    N09_M07_F10_K001_10 = N09_M07_F10_K001_10.data['N09_M07_F10_K001_10']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_11')
    N09_M07_F10_K001_11 = N09_M07_F10_K001_11.data['N09_M07_F10_K001_11']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_12')
    N09_M07_F10_K001_12 = N09_M07_F10_K001_12.data['N09_M07_F10_K001_12']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_13')
    N09_M07_F10_K001_13 = N09_M07_F10_K001_13.data['N09_M07_F10_K001_13']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_14')
    N09_M07_F10_K001_14 = N09_M07_F10_K001_14.data['N09_M07_F10_K001_14']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_15')
    N09_M07_F10_K001_15 = N09_M07_F10_K001_15.data['N09_M07_F10_K001_15']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_16')
    N09_M07_F10_K001_16 = N09_M07_F10_K001_16.data['N09_M07_F10_K001_16']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_17')
    N09_M07_F10_K001_17 = N09_M07_F10_K001_17.data['N09_M07_F10_K001_17']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_18')
    N09_M07_F10_K001_18 = N09_M07_F10_K001_18.data['N09_M07_F10_K001_18']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_19')
    N09_M07_F10_K001_19 = N09_M07_F10_K001_19.data['N09_M07_F10_K001_19']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_20')
    N09_M07_F10_K001_20 = N09_M07_F10_K001_20.data['N09_M07_F10_K001_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    N09_M07_F10_KA01_1 = N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_2')
    N09_M07_F10_KA01_2 = N09_M07_F10_KA01_2.data['N09_M07_F10_KA01_2']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_3')
    N09_M07_F10_KA01_3 = N09_M07_F10_KA01_3.data['N09_M07_F10_KA01_3']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_4')
    N09_M07_F10_KA01_4 = N09_M07_F10_KA01_4.data['N09_M07_F10_KA01_4']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_5')
    N09_M07_F10_KA01_5 = N09_M07_F10_KA01_5.data['N09_M07_F10_KA01_5']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_6')
    N09_M07_F10_KA01_6 = N09_M07_F10_KA01_6.data['N09_M07_F10_KA01_6']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_7')
    N09_M07_F10_KA01_7 = N09_M07_F10_KA01_7.data['N09_M07_F10_KA01_7']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_8')
    N09_M07_F10_KA01_8 = N09_M07_F10_KA01_8.data['N09_M07_F10_KA01_8']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_9')
    N09_M07_F10_KA01_9 = N09_M07_F10_KA01_9.data['N09_M07_F10_KA01_9']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_10')
    N09_M07_F10_KA01_10 = N09_M07_F10_KA01_10.data['N09_M07_F10_KA01_10']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_11')
    N09_M07_F10_KA01_11 = N09_M07_F10_KA01_11.data['N09_M07_F10_KA01_11']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_12')
    N09_M07_F10_KA01_12 = N09_M07_F10_KA01_12.data['N09_M07_F10_KA01_12']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_13')
    N09_M07_F10_KA01_13 = N09_M07_F10_KA01_13.data['N09_M07_F10_KA01_13']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_14')
    N09_M07_F10_KA01_14 = N09_M07_F10_KA01_14.data['N09_M07_F10_KA01_14']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_15')
    N09_M07_F10_KA01_15 = N09_M07_F10_KA01_15.data['N09_M07_F10_KA01_15']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_16')
    N09_M07_F10_KA01_16 = N09_M07_F10_KA01_16.data['N09_M07_F10_KA01_16']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_17')
    N09_M07_F10_KA01_17 = N09_M07_F10_KA01_17.data['N09_M07_F10_KA01_17']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_18')
    N09_M07_F10_KA01_18 = N09_M07_F10_KA01_18.data['N09_M07_F10_KA01_18']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_19')
    N09_M07_F10_KA01_19 = N09_M07_F10_KA01_19.data['N09_M07_F10_KA01_19']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_20')
    N09_M07_F10_KA01_20 = N09_M07_F10_KA01_20.data['N09_M07_F10_KA01_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    N09_M07_F10_KI01_1 = N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_2')
    N09_M07_F10_KI01_2 = N09_M07_F10_KI01_2.data['N09_M07_F10_KI01_2']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_3')
    N09_M07_F10_KI01_3 = N09_M07_F10_KI01_3.data['N09_M07_F10_KI01_3']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_4')
    N09_M07_F10_KI01_4 = N09_M07_F10_KI01_4.data['N09_M07_F10_KI01_4']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_5')
    N09_M07_F10_KI01_5 = N09_M07_F10_KI01_5.data['N09_M07_F10_KI01_5']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_6')
    N09_M07_F10_KI01_6 = N09_M07_F10_KI01_6.data['N09_M07_F10_KI01_6']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_7')
    N09_M07_F10_KI01_7 = N09_M07_F10_KI01_7.data['N09_M07_F10_KI01_7']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_8')
    N09_M07_F10_KI01_8 = N09_M07_F10_KI01_8.data['N09_M07_F10_KI01_8']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_9')
    N09_M07_F10_KI01_9 = N09_M07_F10_KI01_9.data['N09_M07_F10_KI01_9']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_10')
    N09_M07_F10_KI01_10 = N09_M07_F10_KI01_10.data['N09_M07_F10_KI01_10']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_11')
    N09_M07_F10_KI01_11 = N09_M07_F10_KI01_11.data['N09_M07_F10_KI01_11']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_12')
    N09_M07_F10_KI01_12 = N09_M07_F10_KI01_12.data['N09_M07_F10_KI01_12']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_13')
    N09_M07_F10_KI01_13 = N09_M07_F10_KI01_13.data['N09_M07_F10_KI01_13']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_14')
    N09_M07_F10_KI01_14 = N09_M07_F10_KI01_14.data['N09_M07_F10_KI01_14']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_15')
    N09_M07_F10_KI01_15 = N09_M07_F10_KI01_15.data['N09_M07_F10_KI01_15']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_16')
    N09_M07_F10_KI01_16 = N09_M07_F10_KI01_16.data['N09_M07_F10_KI01_16']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_17')
    N09_M07_F10_KI01_17 = N09_M07_F10_KI01_17.data['N09_M07_F10_KI01_17']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_18')
    N09_M07_F10_KI01_18 = N09_M07_F10_KI01_18.data['N09_M07_F10_KI01_18']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_19')
    N09_M07_F10_KI01_19 = N09_M07_F10_KI01_19.data['N09_M07_F10_KI01_19']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_20')
    N09_M07_F10_KI01_20 = N09_M07_F10_KI01_20.data['N09_M07_F10_KI01_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N09_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_1')
    N09_M07_F10_KB24_1 = N09_M07_F10_KB24_1.data['N09_M07_F10_KB24_1']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_2')
    N09_M07_F10_KB24_2 = N09_M07_F10_KB24_2.data['N09_M07_F10_KB24_2']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_3')
    N09_M07_F10_KB24_3 = N09_M07_F10_KB24_3.data['N09_M07_F10_KB24_3']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_4')
    N09_M07_F10_KB24_4 = N09_M07_F10_KB24_4.data['N09_M07_F10_KB24_4']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_5')
    N09_M07_F10_KB24_5 = N09_M07_F10_KB24_5.data['N09_M07_F10_KB24_5']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_6')
    N09_M07_F10_KB24_6 = N09_M07_F10_KB24_6.data['N09_M07_F10_KB24_6']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_7')
    N09_M07_F10_KB24_7 = N09_M07_F10_KB24_7.data['N09_M07_F10_KB24_7']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_8')
    N09_M07_F10_KB24_8 = N09_M07_F10_KB24_8.data['N09_M07_F10_KB24_8']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_9')
    N09_M07_F10_KB24_9 = N09_M07_F10_KB24_9.data['N09_M07_F10_KB24_9']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_10')
    N09_M07_F10_KB24_10 = N09_M07_F10_KB24_10.data['N09_M07_F10_KB24_10']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_11')
    N09_M07_F10_KB24_11 = N09_M07_F10_KB24_11.data['N09_M07_F10_KB24_11']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_12')
    N09_M07_F10_KB24_12 = N09_M07_F10_KB24_12.data['N09_M07_F10_KB24_12']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_13')
    N09_M07_F10_KB24_13 = N09_M07_F10_KB24_13.data['N09_M07_F10_KB24_13']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_14')
    N09_M07_F10_KB24_14 = N09_M07_F10_KB24_14.data['N09_M07_F10_KB24_14']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_15')
    N09_M07_F10_KB24_15 = N09_M07_F10_KB24_15.data['N09_M07_F10_KB24_15']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_16')
    N09_M07_F10_KB24_16 = N09_M07_F10_KB24_16.data['N09_M07_F10_KB24_16']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_17')
    N09_M07_F10_KB24_17 = N09_M07_F10_KB24_17.data['N09_M07_F10_KB24_17']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_18')
    N09_M07_F10_KB24_18 = N09_M07_F10_KB24_18.data['N09_M07_F10_KB24_18']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_19')
    N09_M07_F10_KB24_19 = N09_M07_F10_KB24_19.data['N09_M07_F10_KB24_19']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_20')
    N09_M07_F10_KB24_20 = N09_M07_F10_KB24_20.data['N09_M07_F10_KB24_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N09_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_1')
    N09_M07_F10_KB27_1 = N09_M07_F10_KB27_1.data['N09_M07_F10_KB27_1']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_2')
    N09_M07_F10_KB27_2 = N09_M07_F10_KB27_2.data['N09_M07_F10_KB27_2']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_3')
    N09_M07_F10_KB27_3 = N09_M07_F10_KB27_3.data['N09_M07_F10_KB27_3']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_4')
    N09_M07_F10_KB27_4 = N09_M07_F10_KB27_4.data['N09_M07_F10_KB27_4']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_5')
    N09_M07_F10_KB27_5 = N09_M07_F10_KB27_5.data['N09_M07_F10_KB27_5']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_6')
    N09_M07_F10_KB27_6 = N09_M07_F10_KB27_6.data['N09_M07_F10_KB27_6']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_7')
    N09_M07_F10_KB27_7 = N09_M07_F10_KB27_7.data['N09_M07_F10_KB27_7']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_8')
    N09_M07_F10_KB27_8 = N09_M07_F10_KB27_8.data['N09_M07_F10_KB27_8']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_9')
    N09_M07_F10_KB27_9 = N09_M07_F10_KB27_9.data['N09_M07_F10_KB27_9']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_10')
    N09_M07_F10_KB27_10 = N09_M07_F10_KB27_10.data['N09_M07_F10_KB27_10']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_11')
    N09_M07_F10_KB27_11 = N09_M07_F10_KB27_11.data['N09_M07_F10_KB27_11']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_12')
    N09_M07_F10_KB27_12 = N09_M07_F10_KB27_12.data['N09_M07_F10_KB27_12']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_13')
    N09_M07_F10_KB27_13 = N09_M07_F10_KB27_13.data['N09_M07_F10_KB27_13']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_14')
    N09_M07_F10_KB27_14 = N09_M07_F10_KB27_14.data['N09_M07_F10_KB27_14']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_15')
    N09_M07_F10_KB27_15 = N09_M07_F10_KB27_15.data['N09_M07_F10_KB27_15']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_16')
    N09_M07_F10_KB27_16 = N09_M07_F10_KB27_16.data['N09_M07_F10_KB27_16']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_17')
    N09_M07_F10_KB27_17 = N09_M07_F10_KB27_17.data['N09_M07_F10_KB27_17']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_18')
    N09_M07_F10_KB27_18 = N09_M07_F10_KB27_18.data['N09_M07_F10_KB27_18']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_19')
    N09_M07_F10_KB27_19 = N09_M07_F10_KB27_19.data['N09_M07_F10_KB27_19']['Y'][0][0][0][1][2][0].flatten()
    N09_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_20')
    N09_M07_F10_KB27_20 = N09_M07_F10_KB27_20.data['N09_M07_F10_KB27_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    合并N09_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N09_M07_F10 = np.append(N09_M07_F10_K001_1, N09_M07_F10_K001_2)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_3)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_4)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_5)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_6)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_7)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_8)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_9)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_10)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_11)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_12)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_13)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_14)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_15)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_16)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_17)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_18)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_19)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_20)
    
    '''
    Outer
    '''
    # KA01
    N09_M07_F10_Outer = np.append(N09_M07_F10_KA01_1, N09_M07_F10_KA01_2)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_3)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_4)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_5)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_6)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_7)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_8)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_9)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_10)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_11)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_12)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_13)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_14)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_15)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_16)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_17)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_18)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_19)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_20)
    
    '''
    Inner
    '''
    # KI01
    N09_M07_F10_Inner = np.append(N09_M07_F10_KI01_1, N09_M07_F10_KI01_2)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_3)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_4)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_5)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_6)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_7)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_8)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_9)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_10)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_11)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_12)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_13)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_14)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_15)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_16)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_17)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_18)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_19)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N09_M07_F10_IROR = np.append(N09_M07_F10_KB24_1, N09_M07_F10_KB24_2)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_3)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_4)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_5)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_6)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_7)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_8)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_9)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_10)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_11)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_12)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_13)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_14)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_15)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_16)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_17)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_18)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_19)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N09_M07_F10_ORIR = np.append(N09_M07_F10_KB27_1, N09_M07_F10_KB27_2)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_3)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_4)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_5)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_6)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_7)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_8)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_9)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_10)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_11)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_12)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_13)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_14)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_15)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_16)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_17)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_18)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_19)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_20)

    N09_M07_F10_ALL.append(N09_M07_F10)
    N09_M07_F10_ALL.append(N09_M07_F10_Outer)
    N09_M07_F10_ALL.append(N09_M07_F10_Inner)
    N09_M07_F10_ALL.append(N09_M07_F10_IROR)
    N09_M07_F10_ALL.append(N09_M07_F10_ORIR)

    return N09_M07_F10_ALL
def load_N09_M07_F10_phase_current2_data():
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
    N09_M07_F10_K001_1 = N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][2][2][0].flatten()
    # N09_M07_F10_K001_MCS_1 = N09_M07_F10_K001_1.data[]

    N09_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_2')
    N09_M07_F10_K001_2 = N09_M07_F10_K001_2.data['N09_M07_F10_K001_2']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_3')
    N09_M07_F10_K001_3 = N09_M07_F10_K001_3.data['N09_M07_F10_K001_3']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_4')
    N09_M07_F10_K001_4 = N09_M07_F10_K001_4.data['N09_M07_F10_K001_4']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_5')
    N09_M07_F10_K001_5 = N09_M07_F10_K001_5.data['N09_M07_F10_K001_5']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_6')
    N09_M07_F10_K001_6 = N09_M07_F10_K001_6.data['N09_M07_F10_K001_6']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_7')
    N09_M07_F10_K001_7 = N09_M07_F10_K001_7.data['N09_M07_F10_K001_7']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_8')
    N09_M07_F10_K001_8 = N09_M07_F10_K001_8.data['N09_M07_F10_K001_8']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_9')
    N09_M07_F10_K001_9 = N09_M07_F10_K001_9.data['N09_M07_F10_K001_9']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_10')
    N09_M07_F10_K001_10 = N09_M07_F10_K001_10.data['N09_M07_F10_K001_10']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_11')
    N09_M07_F10_K001_11 = N09_M07_F10_K001_11.data['N09_M07_F10_K001_11']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_12')
    N09_M07_F10_K001_12 = N09_M07_F10_K001_12.data['N09_M07_F10_K001_12']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_13')
    N09_M07_F10_K001_13 = N09_M07_F10_K001_13.data['N09_M07_F10_K001_13']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_14')
    N09_M07_F10_K001_14 = N09_M07_F10_K001_14.data['N09_M07_F10_K001_14']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_15')
    N09_M07_F10_K001_15 = N09_M07_F10_K001_15.data['N09_M07_F10_K001_15']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_16')
    N09_M07_F10_K001_16 = N09_M07_F10_K001_16.data['N09_M07_F10_K001_16']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_17')
    N09_M07_F10_K001_17 = N09_M07_F10_K001_17.data['N09_M07_F10_K001_17']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_18')
    N09_M07_F10_K001_18 = N09_M07_F10_K001_18.data['N09_M07_F10_K001_18']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_19')
    N09_M07_F10_K001_19 = N09_M07_F10_K001_19.data['N09_M07_F10_K001_19']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_20')
    N09_M07_F10_K001_20 = N09_M07_F10_K001_20.data['N09_M07_F10_K001_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    N09_M07_F10_KA01_1 = N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_2')
    N09_M07_F10_KA01_2 = N09_M07_F10_KA01_2.data['N09_M07_F10_KA01_2']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_3')
    N09_M07_F10_KA01_3 = N09_M07_F10_KA01_3.data['N09_M07_F10_KA01_3']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_4')
    N09_M07_F10_KA01_4 = N09_M07_F10_KA01_4.data['N09_M07_F10_KA01_4']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_5')
    N09_M07_F10_KA01_5 = N09_M07_F10_KA01_5.data['N09_M07_F10_KA01_5']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_6')
    N09_M07_F10_KA01_6 = N09_M07_F10_KA01_6.data['N09_M07_F10_KA01_6']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_7')
    N09_M07_F10_KA01_7 = N09_M07_F10_KA01_7.data['N09_M07_F10_KA01_7']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_8')
    N09_M07_F10_KA01_8 = N09_M07_F10_KA01_8.data['N09_M07_F10_KA01_8']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_9')
    N09_M07_F10_KA01_9 = N09_M07_F10_KA01_9.data['N09_M07_F10_KA01_9']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_10')
    N09_M07_F10_KA01_10 = N09_M07_F10_KA01_10.data['N09_M07_F10_KA01_10']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_11')
    N09_M07_F10_KA01_11 = N09_M07_F10_KA01_11.data['N09_M07_F10_KA01_11']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_12')
    N09_M07_F10_KA01_12 = N09_M07_F10_KA01_12.data['N09_M07_F10_KA01_12']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_13')
    N09_M07_F10_KA01_13 = N09_M07_F10_KA01_13.data['N09_M07_F10_KA01_13']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_14')
    N09_M07_F10_KA01_14 = N09_M07_F10_KA01_14.data['N09_M07_F10_KA01_14']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_15')
    N09_M07_F10_KA01_15 = N09_M07_F10_KA01_15.data['N09_M07_F10_KA01_15']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_16')
    N09_M07_F10_KA01_16 = N09_M07_F10_KA01_16.data['N09_M07_F10_KA01_16']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_17')
    N09_M07_F10_KA01_17 = N09_M07_F10_KA01_17.data['N09_M07_F10_KA01_17']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_18')
    N09_M07_F10_KA01_18 = N09_M07_F10_KA01_18.data['N09_M07_F10_KA01_18']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_19')
    N09_M07_F10_KA01_19 = N09_M07_F10_KA01_19.data['N09_M07_F10_KA01_19']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_20')
    N09_M07_F10_KA01_20 = N09_M07_F10_KA01_20.data['N09_M07_F10_KA01_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    N09_M07_F10_KI01_1 = N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_2')
    N09_M07_F10_KI01_2 = N09_M07_F10_KI01_2.data['N09_M07_F10_KI01_2']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_3')
    N09_M07_F10_KI01_3 = N09_M07_F10_KI01_3.data['N09_M07_F10_KI01_3']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_4')
    N09_M07_F10_KI01_4 = N09_M07_F10_KI01_4.data['N09_M07_F10_KI01_4']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_5')
    N09_M07_F10_KI01_5 = N09_M07_F10_KI01_5.data['N09_M07_F10_KI01_5']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_6')
    N09_M07_F10_KI01_6 = N09_M07_F10_KI01_6.data['N09_M07_F10_KI01_6']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_7')
    N09_M07_F10_KI01_7 = N09_M07_F10_KI01_7.data['N09_M07_F10_KI01_7']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_8')
    N09_M07_F10_KI01_8 = N09_M07_F10_KI01_8.data['N09_M07_F10_KI01_8']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_9')
    N09_M07_F10_KI01_9 = N09_M07_F10_KI01_9.data['N09_M07_F10_KI01_9']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_10')
    N09_M07_F10_KI01_10 = N09_M07_F10_KI01_10.data['N09_M07_F10_KI01_10']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_11')
    N09_M07_F10_KI01_11 = N09_M07_F10_KI01_11.data['N09_M07_F10_KI01_11']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_12')
    N09_M07_F10_KI01_12 = N09_M07_F10_KI01_12.data['N09_M07_F10_KI01_12']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_13')
    N09_M07_F10_KI01_13 = N09_M07_F10_KI01_13.data['N09_M07_F10_KI01_13']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_14')
    N09_M07_F10_KI01_14 = N09_M07_F10_KI01_14.data['N09_M07_F10_KI01_14']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_15')
    N09_M07_F10_KI01_15 = N09_M07_F10_KI01_15.data['N09_M07_F10_KI01_15']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_16')
    N09_M07_F10_KI01_16 = N09_M07_F10_KI01_16.data['N09_M07_F10_KI01_16']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_17')
    N09_M07_F10_KI01_17 = N09_M07_F10_KI01_17.data['N09_M07_F10_KI01_17']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_18')
    N09_M07_F10_KI01_18 = N09_M07_F10_KI01_18.data['N09_M07_F10_KI01_18']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_19')
    N09_M07_F10_KI01_19 = N09_M07_F10_KI01_19.data['N09_M07_F10_KI01_19']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_20')
    N09_M07_F10_KI01_20 = N09_M07_F10_KI01_20.data['N09_M07_F10_KI01_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N09_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_1')
    N09_M07_F10_KB24_1 = N09_M07_F10_KB24_1.data['N09_M07_F10_KB24_1']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_2')
    N09_M07_F10_KB24_2 = N09_M07_F10_KB24_2.data['N09_M07_F10_KB24_2']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_3')
    N09_M07_F10_KB24_3 = N09_M07_F10_KB24_3.data['N09_M07_F10_KB24_3']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_4')
    N09_M07_F10_KB24_4 = N09_M07_F10_KB24_4.data['N09_M07_F10_KB24_4']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_5')
    N09_M07_F10_KB24_5 = N09_M07_F10_KB24_5.data['N09_M07_F10_KB24_5']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_6')
    N09_M07_F10_KB24_6 = N09_M07_F10_KB24_6.data['N09_M07_F10_KB24_6']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_7')
    N09_M07_F10_KB24_7 = N09_M07_F10_KB24_7.data['N09_M07_F10_KB24_7']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_8')
    N09_M07_F10_KB24_8 = N09_M07_F10_KB24_8.data['N09_M07_F10_KB24_8']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_9')
    N09_M07_F10_KB24_9 = N09_M07_F10_KB24_9.data['N09_M07_F10_KB24_9']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_10')
    N09_M07_F10_KB24_10 = N09_M07_F10_KB24_10.data['N09_M07_F10_KB24_10']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_11')
    N09_M07_F10_KB24_11 = N09_M07_F10_KB24_11.data['N09_M07_F10_KB24_11']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_12')
    N09_M07_F10_KB24_12 = N09_M07_F10_KB24_12.data['N09_M07_F10_KB24_12']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_13')
    N09_M07_F10_KB24_13 = N09_M07_F10_KB24_13.data['N09_M07_F10_KB24_13']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_14')
    N09_M07_F10_KB24_14 = N09_M07_F10_KB24_14.data['N09_M07_F10_KB24_14']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_15')
    N09_M07_F10_KB24_15 = N09_M07_F10_KB24_15.data['N09_M07_F10_KB24_15']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_16')
    N09_M07_F10_KB24_16 = N09_M07_F10_KB24_16.data['N09_M07_F10_KB24_16']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_17')
    N09_M07_F10_KB24_17 = N09_M07_F10_KB24_17.data['N09_M07_F10_KB24_17']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_18')
    N09_M07_F10_KB24_18 = N09_M07_F10_KB24_18.data['N09_M07_F10_KB24_18']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_19')
    N09_M07_F10_KB24_19 = N09_M07_F10_KB24_19.data['N09_M07_F10_KB24_19']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_20')
    N09_M07_F10_KB24_20 = N09_M07_F10_KB24_20.data['N09_M07_F10_KB24_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N09_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_1')
    N09_M07_F10_KB27_1 = N09_M07_F10_KB27_1.data['N09_M07_F10_KB27_1']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_2')
    N09_M07_F10_KB27_2 = N09_M07_F10_KB27_2.data['N09_M07_F10_KB27_2']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_3')
    N09_M07_F10_KB27_3 = N09_M07_F10_KB27_3.data['N09_M07_F10_KB27_3']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_4')
    N09_M07_F10_KB27_4 = N09_M07_F10_KB27_4.data['N09_M07_F10_KB27_4']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_5')
    N09_M07_F10_KB27_5 = N09_M07_F10_KB27_5.data['N09_M07_F10_KB27_5']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_6')
    N09_M07_F10_KB27_6 = N09_M07_F10_KB27_6.data['N09_M07_F10_KB27_6']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_7')
    N09_M07_F10_KB27_7 = N09_M07_F10_KB27_7.data['N09_M07_F10_KB27_7']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_8')
    N09_M07_F10_KB27_8 = N09_M07_F10_KB27_8.data['N09_M07_F10_KB27_8']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_9')
    N09_M07_F10_KB27_9 = N09_M07_F10_KB27_9.data['N09_M07_F10_KB27_9']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_10')
    N09_M07_F10_KB27_10 = N09_M07_F10_KB27_10.data['N09_M07_F10_KB27_10']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_11')
    N09_M07_F10_KB27_11 = N09_M07_F10_KB27_11.data['N09_M07_F10_KB27_11']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_12')
    N09_M07_F10_KB27_12 = N09_M07_F10_KB27_12.data['N09_M07_F10_KB27_12']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_13')
    N09_M07_F10_KB27_13 = N09_M07_F10_KB27_13.data['N09_M07_F10_KB27_13']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_14')
    N09_M07_F10_KB27_14 = N09_M07_F10_KB27_14.data['N09_M07_F10_KB27_14']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_15')
    N09_M07_F10_KB27_15 = N09_M07_F10_KB27_15.data['N09_M07_F10_KB27_15']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_16')
    N09_M07_F10_KB27_16 = N09_M07_F10_KB27_16.data['N09_M07_F10_KB27_16']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_17')
    N09_M07_F10_KB27_17 = N09_M07_F10_KB27_17.data['N09_M07_F10_KB27_17']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_18')
    N09_M07_F10_KB27_18 = N09_M07_F10_KB27_18.data['N09_M07_F10_KB27_18']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_19')
    N09_M07_F10_KB27_19 = N09_M07_F10_KB27_19.data['N09_M07_F10_KB27_19']['Y'][0][0][0][2][2][0].flatten()
    N09_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_20')
    N09_M07_F10_KB27_20 = N09_M07_F10_KB27_20.data['N09_M07_F10_KB27_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    合并N09_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N09_M07_F10 = np.append(N09_M07_F10_K001_1, N09_M07_F10_K001_2)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_3)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_4)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_5)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_6)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_7)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_8)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_9)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_10)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_11)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_12)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_13)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_14)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_15)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_16)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_17)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_18)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_19)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N09_M07_F10_Outer = np.append(N09_M07_F10_KA01_1, N09_M07_F10_KA01_2)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_3)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_4)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_5)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_6)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_7)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_8)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_9)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_10)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_11)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_12)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_13)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_14)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_15)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_16)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_17)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_18)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_19)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N09_M07_F10_Inner = np.append(N09_M07_F10_KI01_1, N09_M07_F10_KI01_2)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_3)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_4)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_5)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_6)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_7)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_8)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_9)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_10)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_11)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_12)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_13)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_14)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_15)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_16)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_17)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_18)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_19)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N09_M07_F10_IROR = np.append(N09_M07_F10_KB24_1, N09_M07_F10_KB24_2)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_3)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_4)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_5)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_6)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_7)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_8)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_9)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_10)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_11)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_12)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_13)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_14)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_15)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_16)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_17)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_18)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_19)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N09_M07_F10_ORIR = np.append(N09_M07_F10_KB27_1, N09_M07_F10_KB27_2)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_3)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_4)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_5)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_6)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_7)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_8)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_9)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_10)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_11)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_12)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_13)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_14)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_15)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_16)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_17)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_18)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_19)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_20)

    N09_M07_F10_ALL.append(N09_M07_F10)
    N09_M07_F10_ALL.append(N09_M07_F10_Outer)
    N09_M07_F10_ALL.append(N09_M07_F10_Inner)
    N09_M07_F10_ALL.append(N09_M07_F10_IROR)
    N09_M07_F10_ALL.append(N09_M07_F10_ORIR)

    return N09_M07_F10_ALL
def load_N09_M07_F10_Vibration_data():
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
    N09_M07_F10_K001_1 = N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0][-1][2][0].flatten()
    # N09_M07_F10_K001_MCS_1 = N09_M07_F10_K001_1.data[]

    N09_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_2')
    N09_M07_F10_K001_2 = N09_M07_F10_K001_2.data['N09_M07_F10_K001_2']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_3')
    N09_M07_F10_K001_3 = N09_M07_F10_K001_3.data['N09_M07_F10_K001_3']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_4')
    N09_M07_F10_K001_4 = N09_M07_F10_K001_4.data['N09_M07_F10_K001_4']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_5')
    N09_M07_F10_K001_5 = N09_M07_F10_K001_5.data['N09_M07_F10_K001_5']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_6')
    N09_M07_F10_K001_6 = N09_M07_F10_K001_6.data['N09_M07_F10_K001_6']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_7')
    N09_M07_F10_K001_7 = N09_M07_F10_K001_7.data['N09_M07_F10_K001_7']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_8')
    N09_M07_F10_K001_8 = N09_M07_F10_K001_8.data['N09_M07_F10_K001_8']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_9')
    N09_M07_F10_K001_9 = N09_M07_F10_K001_9.data['N09_M07_F10_K001_9']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_10')
    N09_M07_F10_K001_10 = N09_M07_F10_K001_10.data['N09_M07_F10_K001_10']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_11')
    N09_M07_F10_K001_11 = N09_M07_F10_K001_11.data['N09_M07_F10_K001_11']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_12')
    N09_M07_F10_K001_12 = N09_M07_F10_K001_12.data['N09_M07_F10_K001_12']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_13')
    N09_M07_F10_K001_13 = N09_M07_F10_K001_13.data['N09_M07_F10_K001_13']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_14')
    N09_M07_F10_K001_14 = N09_M07_F10_K001_14.data['N09_M07_F10_K001_14']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_15')
    N09_M07_F10_K001_15 = N09_M07_F10_K001_15.data['N09_M07_F10_K001_15']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_16')
    N09_M07_F10_K001_16 = N09_M07_F10_K001_16.data['N09_M07_F10_K001_16']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_17')
    N09_M07_F10_K001_17 = N09_M07_F10_K001_17.data['N09_M07_F10_K001_17']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_18')
    N09_M07_F10_K001_18 = N09_M07_F10_K001_18.data['N09_M07_F10_K001_18']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_19')
    N09_M07_F10_K001_19 = N09_M07_F10_K001_19.data['N09_M07_F10_K001_19']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N09_M07_F10_K001_20')
    N09_M07_F10_K001_20 = N09_M07_F10_K001_20.data['N09_M07_F10_K001_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N09_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_1')
    N09_M07_F10_KA01_1 = N09_M07_F10_KA01_1.data['N09_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_2')
    N09_M07_F10_KA01_2 = N09_M07_F10_KA01_2.data['N09_M07_F10_KA01_2']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_3')
    N09_M07_F10_KA01_3 = N09_M07_F10_KA01_3.data['N09_M07_F10_KA01_3']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_4')
    N09_M07_F10_KA01_4 = N09_M07_F10_KA01_4.data['N09_M07_F10_KA01_4']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_5')
    N09_M07_F10_KA01_5 = N09_M07_F10_KA01_5.data['N09_M07_F10_KA01_5']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_6')
    N09_M07_F10_KA01_6 = N09_M07_F10_KA01_6.data['N09_M07_F10_KA01_6']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_7')
    N09_M07_F10_KA01_7 = N09_M07_F10_KA01_7.data['N09_M07_F10_KA01_7']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_8')
    N09_M07_F10_KA01_8 = N09_M07_F10_KA01_8.data['N09_M07_F10_KA01_8']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_9')
    N09_M07_F10_KA01_9 = N09_M07_F10_KA01_9.data['N09_M07_F10_KA01_9']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_10')
    N09_M07_F10_KA01_10 = N09_M07_F10_KA01_10.data['N09_M07_F10_KA01_10']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_11')
    N09_M07_F10_KA01_11 = N09_M07_F10_KA01_11.data['N09_M07_F10_KA01_11']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_12')
    N09_M07_F10_KA01_12 = N09_M07_F10_KA01_12.data['N09_M07_F10_KA01_12']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_13')
    N09_M07_F10_KA01_13 = N09_M07_F10_KA01_13.data['N09_M07_F10_KA01_13']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_14')
    N09_M07_F10_KA01_14 = N09_M07_F10_KA01_14.data['N09_M07_F10_KA01_14']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_15')
    N09_M07_F10_KA01_15 = N09_M07_F10_KA01_15.data['N09_M07_F10_KA01_15']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_16')
    N09_M07_F10_KA01_16 = N09_M07_F10_KA01_16.data['N09_M07_F10_KA01_16']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_17')
    N09_M07_F10_KA01_17 = N09_M07_F10_KA01_17.data['N09_M07_F10_KA01_17']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_18')
    N09_M07_F10_KA01_18 = N09_M07_F10_KA01_18.data['N09_M07_F10_KA01_18']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_19')
    N09_M07_F10_KA01_19 = N09_M07_F10_KA01_19.data['N09_M07_F10_KA01_19']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N09_M07_F10_KA01_20')
    N09_M07_F10_KA01_20 = N09_M07_F10_KA01_20.data['N09_M07_F10_KA01_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N09_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_1')
    N09_M07_F10_KI01_1 = N09_M07_F10_KI01_1.data['N09_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_2')
    N09_M07_F10_KI01_2 = N09_M07_F10_KI01_2.data['N09_M07_F10_KI01_2']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_3')
    N09_M07_F10_KI01_3 = N09_M07_F10_KI01_3.data['N09_M07_F10_KI01_3']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_4')
    N09_M07_F10_KI01_4 = N09_M07_F10_KI01_4.data['N09_M07_F10_KI01_4']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_5')
    N09_M07_F10_KI01_5 = N09_M07_F10_KI01_5.data['N09_M07_F10_KI01_5']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_6')
    N09_M07_F10_KI01_6 = N09_M07_F10_KI01_6.data['N09_M07_F10_KI01_6']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_7')
    N09_M07_F10_KI01_7 = N09_M07_F10_KI01_7.data['N09_M07_F10_KI01_7']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_8')
    N09_M07_F10_KI01_8 = N09_M07_F10_KI01_8.data['N09_M07_F10_KI01_8']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_9')
    N09_M07_F10_KI01_9 = N09_M07_F10_KI01_9.data['N09_M07_F10_KI01_9']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_10')
    N09_M07_F10_KI01_10 = N09_M07_F10_KI01_10.data['N09_M07_F10_KI01_10']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_11')
    N09_M07_F10_KI01_11 = N09_M07_F10_KI01_11.data['N09_M07_F10_KI01_11']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_12')
    N09_M07_F10_KI01_12 = N09_M07_F10_KI01_12.data['N09_M07_F10_KI01_12']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_13')
    N09_M07_F10_KI01_13 = N09_M07_F10_KI01_13.data['N09_M07_F10_KI01_13']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_14')
    N09_M07_F10_KI01_14 = N09_M07_F10_KI01_14.data['N09_M07_F10_KI01_14']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_15')
    N09_M07_F10_KI01_15 = N09_M07_F10_KI01_15.data['N09_M07_F10_KI01_15']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_16')
    N09_M07_F10_KI01_16 = N09_M07_F10_KI01_16.data['N09_M07_F10_KI01_16']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_17')
    N09_M07_F10_KI01_17 = N09_M07_F10_KI01_17.data['N09_M07_F10_KI01_17']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_18')
    N09_M07_F10_KI01_18 = N09_M07_F10_KI01_18.data['N09_M07_F10_KI01_18']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_19')
    N09_M07_F10_KI01_19 = N09_M07_F10_KI01_19.data['N09_M07_F10_KI01_19']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N09_M07_F10_KI01_20')
    N09_M07_F10_KI01_20 = N09_M07_F10_KI01_20.data['N09_M07_F10_KI01_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N09_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_1')
    N09_M07_F10_KB24_1 = N09_M07_F10_KB24_1.data['N09_M07_F10_KB24_1']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_2')
    N09_M07_F10_KB24_2 = N09_M07_F10_KB24_2.data['N09_M07_F10_KB24_2']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_3')
    N09_M07_F10_KB24_3 = N09_M07_F10_KB24_3.data['N09_M07_F10_KB24_3']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_4')
    N09_M07_F10_KB24_4 = N09_M07_F10_KB24_4.data['N09_M07_F10_KB24_4']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_5')
    N09_M07_F10_KB24_5 = N09_M07_F10_KB24_5.data['N09_M07_F10_KB24_5']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_6')
    N09_M07_F10_KB24_6 = N09_M07_F10_KB24_6.data['N09_M07_F10_KB24_6']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_7')
    N09_M07_F10_KB24_7 = N09_M07_F10_KB24_7.data['N09_M07_F10_KB24_7']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_8')
    N09_M07_F10_KB24_8 = N09_M07_F10_KB24_8.data['N09_M07_F10_KB24_8']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_9')
    N09_M07_F10_KB24_9 = N09_M07_F10_KB24_9.data['N09_M07_F10_KB24_9']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_10')
    N09_M07_F10_KB24_10 = N09_M07_F10_KB24_10.data['N09_M07_F10_KB24_10']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_11')
    N09_M07_F10_KB24_11 = N09_M07_F10_KB24_11.data['N09_M07_F10_KB24_11']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_12')
    N09_M07_F10_KB24_12 = N09_M07_F10_KB24_12.data['N09_M07_F10_KB24_12']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_13')
    N09_M07_F10_KB24_13 = N09_M07_F10_KB24_13.data['N09_M07_F10_KB24_13']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_14')
    N09_M07_F10_KB24_14 = N09_M07_F10_KB24_14.data['N09_M07_F10_KB24_14']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_15')
    N09_M07_F10_KB24_15 = N09_M07_F10_KB24_15.data['N09_M07_F10_KB24_15']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_16')
    N09_M07_F10_KB24_16 = N09_M07_F10_KB24_16.data['N09_M07_F10_KB24_16']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_17')
    N09_M07_F10_KB24_17 = N09_M07_F10_KB24_17.data['N09_M07_F10_KB24_17']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_18')
    N09_M07_F10_KB24_18 = N09_M07_F10_KB24_18.data['N09_M07_F10_KB24_18']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_19')
    N09_M07_F10_KB24_19 = N09_M07_F10_KB24_19.data['N09_M07_F10_KB24_19']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N09_M07_F10_KB24_20')
    N09_M07_F10_KB24_20 = N09_M07_F10_KB24_20.data['N09_M07_F10_KB24_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N09_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_1')
    N09_M07_F10_KB27_1 = N09_M07_F10_KB27_1.data['N09_M07_F10_KB27_1']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_2')
    N09_M07_F10_KB27_2 = N09_M07_F10_KB27_2.data['N09_M07_F10_KB27_2']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_3')
    N09_M07_F10_KB27_3 = N09_M07_F10_KB27_3.data['N09_M07_F10_KB27_3']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_4')
    N09_M07_F10_KB27_4 = N09_M07_F10_KB27_4.data['N09_M07_F10_KB27_4']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_5')
    N09_M07_F10_KB27_5 = N09_M07_F10_KB27_5.data['N09_M07_F10_KB27_5']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_6')
    N09_M07_F10_KB27_6 = N09_M07_F10_KB27_6.data['N09_M07_F10_KB27_6']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_7')
    N09_M07_F10_KB27_7 = N09_M07_F10_KB27_7.data['N09_M07_F10_KB27_7']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_8')
    N09_M07_F10_KB27_8 = N09_M07_F10_KB27_8.data['N09_M07_F10_KB27_8']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_9')
    N09_M07_F10_KB27_9 = N09_M07_F10_KB27_9.data['N09_M07_F10_KB27_9']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_10')
    N09_M07_F10_KB27_10 = N09_M07_F10_KB27_10.data['N09_M07_F10_KB27_10']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_11')
    N09_M07_F10_KB27_11 = N09_M07_F10_KB27_11.data['N09_M07_F10_KB27_11']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_12')
    N09_M07_F10_KB27_12 = N09_M07_F10_KB27_12.data['N09_M07_F10_KB27_12']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_13')
    N09_M07_F10_KB27_13 = N09_M07_F10_KB27_13.data['N09_M07_F10_KB27_13']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_14')
    N09_M07_F10_KB27_14 = N09_M07_F10_KB27_14.data['N09_M07_F10_KB27_14']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_15')
    N09_M07_F10_KB27_15 = N09_M07_F10_KB27_15.data['N09_M07_F10_KB27_15']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_16')
    N09_M07_F10_KB27_16 = N09_M07_F10_KB27_16.data['N09_M07_F10_KB27_16']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_17')
    N09_M07_F10_KB27_17 = N09_M07_F10_KB27_17.data['N09_M07_F10_KB27_17']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_18')
    N09_M07_F10_KB27_18 = N09_M07_F10_KB27_18.data['N09_M07_F10_KB27_18']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_19')
    N09_M07_F10_KB27_19 = N09_M07_F10_KB27_19.data['N09_M07_F10_KB27_19']['Y'][0][0][0][-1][2][0].flatten()
    N09_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N09_M07_F10_KB27_20')
    N09_M07_F10_KB27_20 = N09_M07_F10_KB27_20.data['N09_M07_F10_KB27_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    合并N09_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N09_M07_F10 = np.append(N09_M07_F10_K001_1, N09_M07_F10_K001_2)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_3)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_4)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_5)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_6)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_7)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_8)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_9)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_10)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_11)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_12)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_13)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_14)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_15)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_16)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_17)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_18)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_19)
    N09_M07_F10 = np.append(N09_M07_F10, N09_M07_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N09_M07_F10_Outer = np.append(N09_M07_F10_KA01_1, N09_M07_F10_KA01_2)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_3)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_4)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_5)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_6)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_7)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_8)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_9)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_10)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_11)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_12)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_13)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_14)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_15)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_16)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_17)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_18)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_19)
    N09_M07_F10_Outer = np.append(N09_M07_F10_Outer, N09_M07_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N09_M07_F10_Inner = np.append(N09_M07_F10_KI01_1, N09_M07_F10_KI01_2)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_3)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_4)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_5)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_6)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_7)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_8)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_9)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_10)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_11)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_12)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_13)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_14)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_15)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_16)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_17)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_18)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_19)
    N09_M07_F10_Inner = np.append(N09_M07_F10_Inner, N09_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N09_M07_F10_IROR = np.append(N09_M07_F10_KB24_1, N09_M07_F10_KB24_2)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_3)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_4)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_5)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_6)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_7)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_8)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_9)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_10)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_11)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_12)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_13)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_14)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_15)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_16)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_17)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_18)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_19)
    N09_M07_F10_IROR = np.append(N09_M07_F10_IROR, N09_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N09_M07_F10_ORIR = np.append(N09_M07_F10_KB27_1, N09_M07_F10_KB27_2)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_3)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_4)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_5)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_6)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_7)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_8)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_9)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_10)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_11)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_12)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_13)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_14)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_15)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_16)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_17)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_18)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_19)
    N09_M07_F10_ORIR = np.append(N09_M07_F10_ORIR, N09_M07_F10_KB27_20)

    N09_M07_F10_ALL.append(N09_M07_F10)
    N09_M07_F10_ALL.append(N09_M07_F10_Outer)
    N09_M07_F10_ALL.append(N09_M07_F10_Inner)
    N09_M07_F10_ALL.append(N09_M07_F10_IROR)
    N09_M07_F10_ALL.append(N09_M07_F10_ORIR)

    return N09_M07_F10_ALL
def load_N15_M07_F10_phase_current1_data():
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
    N15_M07_F10_K001_1 = N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][1][2][0].flatten()
    # N15_M07_F10_K001_MCS_1 = N15_M07_F10_K001_1.data[]

    N15_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_2')
    N15_M07_F10_K001_2 = N15_M07_F10_K001_2.data['N15_M07_F10_K001_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_3')
    N15_M07_F10_K001_3 = N15_M07_F10_K001_3.data['N15_M07_F10_K001_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_4')
    N15_M07_F10_K001_4 = N15_M07_F10_K001_4.data['N15_M07_F10_K001_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_5')
    N15_M07_F10_K001_5 = N15_M07_F10_K001_5.data['N15_M07_F10_K001_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_6')
    N15_M07_F10_K001_6 = N15_M07_F10_K001_6.data['N15_M07_F10_K001_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_7')
    N15_M07_F10_K001_7 = N15_M07_F10_K001_7.data['N15_M07_F10_K001_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_8')
    N15_M07_F10_K001_8 = N15_M07_F10_K001_8.data['N15_M07_F10_K001_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_9')
    N15_M07_F10_K001_9 = N15_M07_F10_K001_9.data['N15_M07_F10_K001_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_10')
    N15_M07_F10_K001_10 = N15_M07_F10_K001_10.data['N15_M07_F10_K001_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_11')
    N15_M07_F10_K001_11 = N15_M07_F10_K001_11.data['N15_M07_F10_K001_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_12')
    N15_M07_F10_K001_12 = N15_M07_F10_K001_12.data['N15_M07_F10_K001_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_13')
    N15_M07_F10_K001_13 = N15_M07_F10_K001_13.data['N15_M07_F10_K001_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_14')
    N15_M07_F10_K001_14 = N15_M07_F10_K001_14.data['N15_M07_F10_K001_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_15')
    N15_M07_F10_K001_15 = N15_M07_F10_K001_15.data['N15_M07_F10_K001_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_16')
    N15_M07_F10_K001_16 = N15_M07_F10_K001_16.data['N15_M07_F10_K001_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_17')
    N15_M07_F10_K001_17 = N15_M07_F10_K001_17.data['N15_M07_F10_K001_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_18')
    N15_M07_F10_K001_18 = N15_M07_F10_K001_18.data['N15_M07_F10_K001_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_19')
    N15_M07_F10_K001_19 = N15_M07_F10_K001_19.data['N15_M07_F10_K001_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_20')
    N15_M07_F10_K001_20 = N15_M07_F10_K001_20.data['N15_M07_F10_K001_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_1')
    N15_M07_F10_KA01_1 = N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_2')
    N15_M07_F10_KA01_2 = N15_M07_F10_KA01_2.data['N15_M07_F10_KA01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_3')
    N15_M07_F10_KA01_3 = N15_M07_F10_KA01_3.data['N15_M07_F10_KA01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_4')
    N15_M07_F10_KA01_4 = N15_M07_F10_KA01_4.data['N15_M07_F10_KA01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_5')
    N15_M07_F10_KA01_5 = N15_M07_F10_KA01_5.data['N15_M07_F10_KA01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_6')
    N15_M07_F10_KA01_6 = N15_M07_F10_KA01_6.data['N15_M07_F10_KA01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_7')
    N15_M07_F10_KA01_7 = N15_M07_F10_KA01_7.data['N15_M07_F10_KA01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_8')
    N15_M07_F10_KA01_8 = N15_M07_F10_KA01_8.data['N15_M07_F10_KA01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_9')
    N15_M07_F10_KA01_9 = N15_M07_F10_KA01_9.data['N15_M07_F10_KA01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_10')
    N15_M07_F10_KA01_10 = N15_M07_F10_KA01_10.data['N15_M07_F10_KA01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_11')
    N15_M07_F10_KA01_11 = N15_M07_F10_KA01_11.data['N15_M07_F10_KA01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_12')
    N15_M07_F10_KA01_12 = N15_M07_F10_KA01_12.data['N15_M07_F10_KA01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_13')
    N15_M07_F10_KA01_13 = N15_M07_F10_KA01_13.data['N15_M07_F10_KA01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_14')
    N15_M07_F10_KA01_14 = N15_M07_F10_KA01_14.data['N15_M07_F10_KA01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_15')
    N15_M07_F10_KA01_15 = N15_M07_F10_KA01_15.data['N15_M07_F10_KA01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_16')
    N15_M07_F10_KA01_16 = N15_M07_F10_KA01_16.data['N15_M07_F10_KA01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_17')
    N15_M07_F10_KA01_17 = N15_M07_F10_KA01_17.data['N15_M07_F10_KA01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_18')
    N15_M07_F10_KA01_18 = N15_M07_F10_KA01_18.data['N15_M07_F10_KA01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_19')
    N15_M07_F10_KA01_19 = N15_M07_F10_KA01_19.data['N15_M07_F10_KA01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_20')
    N15_M07_F10_KA01_20 = N15_M07_F10_KA01_20.data['N15_M07_F10_KA01_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_1')
    N15_M07_F10_KI01_1 = N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_2')
    N15_M07_F10_KI01_2 = N15_M07_F10_KI01_2.data['N15_M07_F10_KI01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_3')
    N15_M07_F10_KI01_3 = N15_M07_F10_KI01_3.data['N15_M07_F10_KI01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_4')
    N15_M07_F10_KI01_4 = N15_M07_F10_KI01_4.data['N15_M07_F10_KI01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_5')
    N15_M07_F10_KI01_5 = N15_M07_F10_KI01_5.data['N15_M07_F10_KI01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_6')
    N15_M07_F10_KI01_6 = N15_M07_F10_KI01_6.data['N15_M07_F10_KI01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_7')
    N15_M07_F10_KI01_7 = N15_M07_F10_KI01_7.data['N15_M07_F10_KI01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_8')
    N15_M07_F10_KI01_8 = N15_M07_F10_KI01_8.data['N15_M07_F10_KI01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_9')
    N15_M07_F10_KI01_9 = N15_M07_F10_KI01_9.data['N15_M07_F10_KI01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_10')
    N15_M07_F10_KI01_10 = N15_M07_F10_KI01_10.data['N15_M07_F10_KI01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_11')
    N15_M07_F10_KI01_11 = N15_M07_F10_KI01_11.data['N15_M07_F10_KI01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_12')
    N15_M07_F10_KI01_12 = N15_M07_F10_KI01_12.data['N15_M07_F10_KI01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_13')
    N15_M07_F10_KI01_13 = N15_M07_F10_KI01_13.data['N15_M07_F10_KI01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_14')
    N15_M07_F10_KI01_14 = N15_M07_F10_KI01_14.data['N15_M07_F10_KI01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_15')
    N15_M07_F10_KI01_15 = N15_M07_F10_KI01_15.data['N15_M07_F10_KI01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_16')
    N15_M07_F10_KI01_16 = N15_M07_F10_KI01_16.data['N15_M07_F10_KI01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_17')
    N15_M07_F10_KI01_17 = N15_M07_F10_KI01_17.data['N15_M07_F10_KI01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_18')
    N15_M07_F10_KI01_18 = N15_M07_F10_KI01_18.data['N15_M07_F10_KI01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_19')
    N15_M07_F10_KI01_19 = N15_M07_F10_KI01_19.data['N15_M07_F10_KI01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_20')
    N15_M07_F10_KI01_20 = N15_M07_F10_KI01_20.data['N15_M07_F10_KI01_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_1')
    N15_M07_F10_KB24_1 = N15_M07_F10_KB24_1.data['N15_M07_F10_KB24_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_2')
    N15_M07_F10_KB24_2 = N15_M07_F10_KB24_2.data['N15_M07_F10_KB24_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_3')
    N15_M07_F10_KB24_3 = N15_M07_F10_KB24_3.data['N15_M07_F10_KB24_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_4')
    N15_M07_F10_KB24_4 = N15_M07_F10_KB24_4.data['N15_M07_F10_KB24_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_5')
    N15_M07_F10_KB24_5 = N15_M07_F10_KB24_5.data['N15_M07_F10_KB24_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_6')
    N15_M07_F10_KB24_6 = N15_M07_F10_KB24_6.data['N15_M07_F10_KB24_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_7')
    N15_M07_F10_KB24_7 = N15_M07_F10_KB24_7.data['N15_M07_F10_KB24_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_8')
    N15_M07_F10_KB24_8 = N15_M07_F10_KB24_8.data['N15_M07_F10_KB24_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_9')
    N15_M07_F10_KB24_9 = N15_M07_F10_KB24_9.data['N15_M07_F10_KB24_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_10')
    N15_M07_F10_KB24_10 = N15_M07_F10_KB24_10.data['N15_M07_F10_KB24_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_11')
    N15_M07_F10_KB24_11 = N15_M07_F10_KB24_11.data['N15_M07_F10_KB24_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_12')
    N15_M07_F10_KB24_12 = N15_M07_F10_KB24_12.data['N15_M07_F10_KB24_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_13')
    N15_M07_F10_KB24_13 = N15_M07_F10_KB24_13.data['N15_M07_F10_KB24_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_14')
    N15_M07_F10_KB24_14 = N15_M07_F10_KB24_14.data['N15_M07_F10_KB24_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_15')
    N15_M07_F10_KB24_15 = N15_M07_F10_KB24_15.data['N15_M07_F10_KB24_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_16')
    N15_M07_F10_KB24_16 = N15_M07_F10_KB24_16.data['N15_M07_F10_KB24_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_17')
    N15_M07_F10_KB24_17 = N15_M07_F10_KB24_17.data['N15_M07_F10_KB24_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_18')
    N15_M07_F10_KB24_18 = N15_M07_F10_KB24_18.data['N15_M07_F10_KB24_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_19')
    N15_M07_F10_KB24_19 = N15_M07_F10_KB24_19.data['N15_M07_F10_KB24_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_20')
    N15_M07_F10_KB24_20 = N15_M07_F10_KB24_20.data['N15_M07_F10_KB24_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_1')
    N15_M07_F10_KB27_1 = N15_M07_F10_KB27_1.data['N15_M07_F10_KB27_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_2')
    N15_M07_F10_KB27_2 = N15_M07_F10_KB27_2.data['N15_M07_F10_KB27_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_3')
    N15_M07_F10_KB27_3 = N15_M07_F10_KB27_3.data['N15_M07_F10_KB27_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_4')
    N15_M07_F10_KB27_4 = N15_M07_F10_KB27_4.data['N15_M07_F10_KB27_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_5')
    N15_M07_F10_KB27_5 = N15_M07_F10_KB27_5.data['N15_M07_F10_KB27_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_6')
    N15_M07_F10_KB27_6 = N15_M07_F10_KB27_6.data['N15_M07_F10_KB27_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_7')
    N15_M07_F10_KB27_7 = N15_M07_F10_KB27_7.data['N15_M07_F10_KB27_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_8')
    N15_M07_F10_KB27_8 = N15_M07_F10_KB27_8.data['N15_M07_F10_KB27_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_9')
    N15_M07_F10_KB27_9 = N15_M07_F10_KB27_9.data['N15_M07_F10_KB27_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_10')
    N15_M07_F10_KB27_10 = N15_M07_F10_KB27_10.data['N15_M07_F10_KB27_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_11')
    N15_M07_F10_KB27_11 = N15_M07_F10_KB27_11.data['N15_M07_F10_KB27_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_12')
    N15_M07_F10_KB27_12 = N15_M07_F10_KB27_12.data['N15_M07_F10_KB27_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_13')
    N15_M07_F10_KB27_13 = N15_M07_F10_KB27_13.data['N15_M07_F10_KB27_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_14')
    N15_M07_F10_KB27_14 = N15_M07_F10_KB27_14.data['N15_M07_F10_KB27_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_15')
    N15_M07_F10_KB27_15 = N15_M07_F10_KB27_15.data['N15_M07_F10_KB27_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_16')
    N15_M07_F10_KB27_16 = N15_M07_F10_KB27_16.data['N15_M07_F10_KB27_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_17')
    N15_M07_F10_KB27_17 = N15_M07_F10_KB27_17.data['N15_M07_F10_KB27_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_18')
    N15_M07_F10_KB27_18 = N15_M07_F10_KB27_18.data['N15_M07_F10_KB27_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_19')
    N15_M07_F10_KB27_19 = N15_M07_F10_KB27_19.data['N15_M07_F10_KB27_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_20')
    N15_M07_F10_KB27_20 = N15_M07_F10_KB27_20.data['N15_M07_F10_KB27_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    合并N15_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F10 = np.append(N15_M07_F10_K001_1, N15_M07_F10_K001_2)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_3)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_4)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_5)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_6)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_7)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_8)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_9)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_10)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_11)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_12)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_13)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_14)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_15)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_16)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_17)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_18)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_19)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F10_Outer = np.append(N15_M07_F10_KA01_1, N15_M07_F10_KA01_2)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_3)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_4)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_5)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_6)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_7)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_8)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_9)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_10)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_11)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_12)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_13)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_14)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_15)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_16)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_17)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_18)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_19)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F10_Inner = np.append(N15_M07_F10_KI01_1, N15_M07_F10_KI01_2)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_3)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_4)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_5)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_6)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_7)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_8)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_9)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_10)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_11)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_12)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_13)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_14)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_15)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_16)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_17)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_18)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_19)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F10_IROR = np.append(N15_M07_F10_KB24_1, N15_M07_F10_KB24_2)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_3)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_4)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_5)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_6)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_7)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_8)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_9)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_10)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_11)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_12)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_13)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_14)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_15)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_16)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_17)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_18)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_19)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F10_ORIR = np.append(N15_M07_F10_KB27_1, N15_M07_F10_KB27_2)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_3)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_4)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_5)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_6)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_7)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_8)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_9)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_10)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_11)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_12)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_13)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_14)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_15)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_16)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_17)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_18)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_19)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_20)

    N15_M07_F10_ALL.append(N15_M07_F10)
    N15_M07_F10_ALL.append(N15_M07_F10_Outer)
    N15_M07_F10_ALL.append(N15_M07_F10_Inner)
    N15_M07_F10_ALL.append(N15_M07_F10_IROR)
    N15_M07_F10_ALL.append(N15_M07_F10_ORIR)

    return N15_M07_F10_ALL
def load_N15_M07_F10_phase_current2_data():
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
    N15_M07_F10_K001_1 = N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][2][2][0].flatten()
    # N15_M07_F10_K001_MCS_1 = N15_M07_F10_K001_1.data[]

    N15_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_2')
    N15_M07_F10_K001_2 = N15_M07_F10_K001_2.data['N15_M07_F10_K001_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_3')
    N15_M07_F10_K001_3 = N15_M07_F10_K001_3.data['N15_M07_F10_K001_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_4')
    N15_M07_F10_K001_4 = N15_M07_F10_K001_4.data['N15_M07_F10_K001_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_5')
    N15_M07_F10_K001_5 = N15_M07_F10_K001_5.data['N15_M07_F10_K001_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_6')
    N15_M07_F10_K001_6 = N15_M07_F10_K001_6.data['N15_M07_F10_K001_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_7')
    N15_M07_F10_K001_7 = N15_M07_F10_K001_7.data['N15_M07_F10_K001_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_8')
    N15_M07_F10_K001_8 = N15_M07_F10_K001_8.data['N15_M07_F10_K001_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_9')
    N15_M07_F10_K001_9 = N15_M07_F10_K001_9.data['N15_M07_F10_K001_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_10')
    N15_M07_F10_K001_10 = N15_M07_F10_K001_10.data['N15_M07_F10_K001_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_11')
    N15_M07_F10_K001_11 = N15_M07_F10_K001_11.data['N15_M07_F10_K001_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_12')
    N15_M07_F10_K001_12 = N15_M07_F10_K001_12.data['N15_M07_F10_K001_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_13')
    N15_M07_F10_K001_13 = N15_M07_F10_K001_13.data['N15_M07_F10_K001_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_14')
    N15_M07_F10_K001_14 = N15_M07_F10_K001_14.data['N15_M07_F10_K001_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_15')
    N15_M07_F10_K001_15 = N15_M07_F10_K001_15.data['N15_M07_F10_K001_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_16')
    N15_M07_F10_K001_16 = N15_M07_F10_K001_16.data['N15_M07_F10_K001_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_17')
    N15_M07_F10_K001_17 = N15_M07_F10_K001_17.data['N15_M07_F10_K001_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_18')
    N15_M07_F10_K001_18 = N15_M07_F10_K001_18.data['N15_M07_F10_K001_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_19')
    N15_M07_F10_K001_19 = N15_M07_F10_K001_19.data['N15_M07_F10_K001_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_20')
    N15_M07_F10_K001_20 = N15_M07_F10_K001_20.data['N15_M07_F10_K001_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_1')
    N15_M07_F10_KA01_1 = N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_2')
    N15_M07_F10_KA01_2 = N15_M07_F10_KA01_2.data['N15_M07_F10_KA01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_3')
    N15_M07_F10_KA01_3 = N15_M07_F10_KA01_3.data['N15_M07_F10_KA01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_4')
    N15_M07_F10_KA01_4 = N15_M07_F10_KA01_4.data['N15_M07_F10_KA01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_5')
    N15_M07_F10_KA01_5 = N15_M07_F10_KA01_5.data['N15_M07_F10_KA01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_6')
    N15_M07_F10_KA01_6 = N15_M07_F10_KA01_6.data['N15_M07_F10_KA01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_7')
    N15_M07_F10_KA01_7 = N15_M07_F10_KA01_7.data['N15_M07_F10_KA01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_8')
    N15_M07_F10_KA01_8 = N15_M07_F10_KA01_8.data['N15_M07_F10_KA01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_9')
    N15_M07_F10_KA01_9 = N15_M07_F10_KA01_9.data['N15_M07_F10_KA01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_10')
    N15_M07_F10_KA01_10 = N15_M07_F10_KA01_10.data['N15_M07_F10_KA01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_11')
    N15_M07_F10_KA01_11 = N15_M07_F10_KA01_11.data['N15_M07_F10_KA01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_12')
    N15_M07_F10_KA01_12 = N15_M07_F10_KA01_12.data['N15_M07_F10_KA01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_13')
    N15_M07_F10_KA01_13 = N15_M07_F10_KA01_13.data['N15_M07_F10_KA01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_14')
    N15_M07_F10_KA01_14 = N15_M07_F10_KA01_14.data['N15_M07_F10_KA01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_15')
    N15_M07_F10_KA01_15 = N15_M07_F10_KA01_15.data['N15_M07_F10_KA01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_16')
    N15_M07_F10_KA01_16 = N15_M07_F10_KA01_16.data['N15_M07_F10_KA01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_17')
    N15_M07_F10_KA01_17 = N15_M07_F10_KA01_17.data['N15_M07_F10_KA01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_18')
    N15_M07_F10_KA01_18 = N15_M07_F10_KA01_18.data['N15_M07_F10_KA01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_19')
    N15_M07_F10_KA01_19 = N15_M07_F10_KA01_19.data['N15_M07_F10_KA01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_20')
    N15_M07_F10_KA01_20 = N15_M07_F10_KA01_20.data['N15_M07_F10_KA01_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_1')
    N15_M07_F10_KI01_1 = N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_2')
    N15_M07_F10_KI01_2 = N15_M07_F10_KI01_2.data['N15_M07_F10_KI01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_3')
    N15_M07_F10_KI01_3 = N15_M07_F10_KI01_3.data['N15_M07_F10_KI01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_4')
    N15_M07_F10_KI01_4 = N15_M07_F10_KI01_4.data['N15_M07_F10_KI01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_5')
    N15_M07_F10_KI01_5 = N15_M07_F10_KI01_5.data['N15_M07_F10_KI01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_6')
    N15_M07_F10_KI01_6 = N15_M07_F10_KI01_6.data['N15_M07_F10_KI01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_7')
    N15_M07_F10_KI01_7 = N15_M07_F10_KI01_7.data['N15_M07_F10_KI01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_8')
    N15_M07_F10_KI01_8 = N15_M07_F10_KI01_8.data['N15_M07_F10_KI01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_9')
    N15_M07_F10_KI01_9 = N15_M07_F10_KI01_9.data['N15_M07_F10_KI01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_10')
    N15_M07_F10_KI01_10 = N15_M07_F10_KI01_10.data['N15_M07_F10_KI01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_11')
    N15_M07_F10_KI01_11 = N15_M07_F10_KI01_11.data['N15_M07_F10_KI01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_12')
    N15_M07_F10_KI01_12 = N15_M07_F10_KI01_12.data['N15_M07_F10_KI01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_13')
    N15_M07_F10_KI01_13 = N15_M07_F10_KI01_13.data['N15_M07_F10_KI01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_14')
    N15_M07_F10_KI01_14 = N15_M07_F10_KI01_14.data['N15_M07_F10_KI01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_15')
    N15_M07_F10_KI01_15 = N15_M07_F10_KI01_15.data['N15_M07_F10_KI01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_16')
    N15_M07_F10_KI01_16 = N15_M07_F10_KI01_16.data['N15_M07_F10_KI01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_17')
    N15_M07_F10_KI01_17 = N15_M07_F10_KI01_17.data['N15_M07_F10_KI01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_18')
    N15_M07_F10_KI01_18 = N15_M07_F10_KI01_18.data['N15_M07_F10_KI01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_19')
    N15_M07_F10_KI01_19 = N15_M07_F10_KI01_19.data['N15_M07_F10_KI01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_20')
    N15_M07_F10_KI01_20 = N15_M07_F10_KI01_20.data['N15_M07_F10_KI01_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_1')
    N15_M07_F10_KB24_1 = N15_M07_F10_KB24_1.data['N15_M07_F10_KB24_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_2')
    N15_M07_F10_KB24_2 = N15_M07_F10_KB24_2.data['N15_M07_F10_KB24_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_3')
    N15_M07_F10_KB24_3 = N15_M07_F10_KB24_3.data['N15_M07_F10_KB24_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_4')
    N15_M07_F10_KB24_4 = N15_M07_F10_KB24_4.data['N15_M07_F10_KB24_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_5')
    N15_M07_F10_KB24_5 = N15_M07_F10_KB24_5.data['N15_M07_F10_KB24_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_6')
    N15_M07_F10_KB24_6 = N15_M07_F10_KB24_6.data['N15_M07_F10_KB24_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_7')
    N15_M07_F10_KB24_7 = N15_M07_F10_KB24_7.data['N15_M07_F10_KB24_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_8')
    N15_M07_F10_KB24_8 = N15_M07_F10_KB24_8.data['N15_M07_F10_KB24_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_9')
    N15_M07_F10_KB24_9 = N15_M07_F10_KB24_9.data['N15_M07_F10_KB24_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_10')
    N15_M07_F10_KB24_10 = N15_M07_F10_KB24_10.data['N15_M07_F10_KB24_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_11')
    N15_M07_F10_KB24_11 = N15_M07_F10_KB24_11.data['N15_M07_F10_KB24_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_12')
    N15_M07_F10_KB24_12 = N15_M07_F10_KB24_12.data['N15_M07_F10_KB24_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_13')
    N15_M07_F10_KB24_13 = N15_M07_F10_KB24_13.data['N15_M07_F10_KB24_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_14')
    N15_M07_F10_KB24_14 = N15_M07_F10_KB24_14.data['N15_M07_F10_KB24_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_15')
    N15_M07_F10_KB24_15 = N15_M07_F10_KB24_15.data['N15_M07_F10_KB24_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_16')
    N15_M07_F10_KB24_16 = N15_M07_F10_KB24_16.data['N15_M07_F10_KB24_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_17')
    N15_M07_F10_KB24_17 = N15_M07_F10_KB24_17.data['N15_M07_F10_KB24_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_18')
    N15_M07_F10_KB24_18 = N15_M07_F10_KB24_18.data['N15_M07_F10_KB24_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_19')
    N15_M07_F10_KB24_19 = N15_M07_F10_KB24_19.data['N15_M07_F10_KB24_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_20')
    N15_M07_F10_KB24_20 = N15_M07_F10_KB24_20.data['N15_M07_F10_KB24_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_1')
    N15_M07_F10_KB27_1 = N15_M07_F10_KB27_1.data['N15_M07_F10_KB27_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_2')
    N15_M07_F10_KB27_2 = N15_M07_F10_KB27_2.data['N15_M07_F10_KB27_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_3')
    N15_M07_F10_KB27_3 = N15_M07_F10_KB27_3.data['N15_M07_F10_KB27_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_4')
    N15_M07_F10_KB27_4 = N15_M07_F10_KB27_4.data['N15_M07_F10_KB27_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_5')
    N15_M07_F10_KB27_5 = N15_M07_F10_KB27_5.data['N15_M07_F10_KB27_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_6')
    N15_M07_F10_KB27_6 = N15_M07_F10_KB27_6.data['N15_M07_F10_KB27_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_7')
    N15_M07_F10_KB27_7 = N15_M07_F10_KB27_7.data['N15_M07_F10_KB27_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_8')
    N15_M07_F10_KB27_8 = N15_M07_F10_KB27_8.data['N15_M07_F10_KB27_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_9')
    N15_M07_F10_KB27_9 = N15_M07_F10_KB27_9.data['N15_M07_F10_KB27_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_10')
    N15_M07_F10_KB27_10 = N15_M07_F10_KB27_10.data['N15_M07_F10_KB27_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_11')
    N15_M07_F10_KB27_11 = N15_M07_F10_KB27_11.data['N15_M07_F10_KB27_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_12')
    N15_M07_F10_KB27_12 = N15_M07_F10_KB27_12.data['N15_M07_F10_KB27_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_13')
    N15_M07_F10_KB27_13 = N15_M07_F10_KB27_13.data['N15_M07_F10_KB27_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_14')
    N15_M07_F10_KB27_14 = N15_M07_F10_KB27_14.data['N15_M07_F10_KB27_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_15')
    N15_M07_F10_KB27_15 = N15_M07_F10_KB27_15.data['N15_M07_F10_KB27_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_16')
    N15_M07_F10_KB27_16 = N15_M07_F10_KB27_16.data['N15_M07_F10_KB27_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_17')
    N15_M07_F10_KB27_17 = N15_M07_F10_KB27_17.data['N15_M07_F10_KB27_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_18')
    N15_M07_F10_KB27_18 = N15_M07_F10_KB27_18.data['N15_M07_F10_KB27_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_19')
    N15_M07_F10_KB27_19 = N15_M07_F10_KB27_19.data['N15_M07_F10_KB27_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_20')
    N15_M07_F10_KB27_20 = N15_M07_F10_KB27_20.data['N15_M07_F10_KB27_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    合并N15_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F10 = np.append(N15_M07_F10_K001_1, N15_M07_F10_K001_2)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_3)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_4)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_5)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_6)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_7)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_8)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_9)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_10)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_11)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_12)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_13)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_14)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_15)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_16)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_17)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_18)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_19)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F10_Outer = np.append(N15_M07_F10_KA01_1, N15_M07_F10_KA01_2)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_3)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_4)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_5)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_6)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_7)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_8)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_9)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_10)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_11)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_12)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_13)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_14)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_15)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_16)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_17)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_18)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_19)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F10_Inner = np.append(N15_M07_F10_KI01_1, N15_M07_F10_KI01_2)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_3)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_4)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_5)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_6)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_7)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_8)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_9)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_10)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_11)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_12)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_13)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_14)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_15)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_16)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_17)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_18)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_19)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F10_IROR = np.append(N15_M07_F10_KB24_1, N15_M07_F10_KB24_2)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_3)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_4)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_5)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_6)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_7)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_8)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_9)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_10)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_11)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_12)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_13)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_14)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_15)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_16)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_17)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_18)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_19)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F10_ORIR = np.append(N15_M07_F10_KB27_1, N15_M07_F10_KB27_2)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_3)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_4)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_5)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_6)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_7)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_8)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_9)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_10)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_11)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_12)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_13)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_14)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_15)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_16)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_17)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_18)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_19)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_20)

    N15_M07_F10_ALL.append(N15_M07_F10)
    N15_M07_F10_ALL.append(N15_M07_F10_Outer)
    N15_M07_F10_ALL.append(N15_M07_F10_Inner)
    N15_M07_F10_ALL.append(N15_M07_F10_IROR)
    N15_M07_F10_ALL.append(N15_M07_F10_ORIR)

    return N15_M07_F10_ALL
def load_N15_M07_F10_Vibration_data():
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
    N15_M07_F10_K001_1 = N15_M07_F10_K001_1.data['N15_M07_F10_K001_1']['Y'][0][0][0][-1][2][0].flatten()
    # N15_M07_F10_K001_MCS_1 = N15_M07_F10_K001_1.data[]

    N15_M07_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_2')
    N15_M07_F10_K001_2 = N15_M07_F10_K001_2.data['N15_M07_F10_K001_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_3')
    N15_M07_F10_K001_3 = N15_M07_F10_K001_3.data['N15_M07_F10_K001_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_4')
    N15_M07_F10_K001_4 = N15_M07_F10_K001_4.data['N15_M07_F10_K001_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_5')
    N15_M07_F10_K001_5 = N15_M07_F10_K001_5.data['N15_M07_F10_K001_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_6')
    N15_M07_F10_K001_6 = N15_M07_F10_K001_6.data['N15_M07_F10_K001_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_7')
    N15_M07_F10_K001_7 = N15_M07_F10_K001_7.data['N15_M07_F10_K001_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_8')
    N15_M07_F10_K001_8 = N15_M07_F10_K001_8.data['N15_M07_F10_K001_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_9')
    N15_M07_F10_K001_9 = N15_M07_F10_K001_9.data['N15_M07_F10_K001_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_10')
    N15_M07_F10_K001_10 = N15_M07_F10_K001_10.data['N15_M07_F10_K001_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_11')
    N15_M07_F10_K001_11 = N15_M07_F10_K001_11.data['N15_M07_F10_K001_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_12')
    N15_M07_F10_K001_12 = N15_M07_F10_K001_12.data['N15_M07_F10_K001_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_13')
    N15_M07_F10_K001_13 = N15_M07_F10_K001_13.data['N15_M07_F10_K001_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_14')
    N15_M07_F10_K001_14 = N15_M07_F10_K001_14.data['N15_M07_F10_K001_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_15')
    N15_M07_F10_K001_15 = N15_M07_F10_K001_15.data['N15_M07_F10_K001_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_16')
    N15_M07_F10_K001_16 = N15_M07_F10_K001_16.data['N15_M07_F10_K001_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_17')
    N15_M07_F10_K001_17 = N15_M07_F10_K001_17.data['N15_M07_F10_K001_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_18')
    N15_M07_F10_K001_18 = N15_M07_F10_K001_18.data['N15_M07_F10_K001_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_19')
    N15_M07_F10_K001_19 = N15_M07_F10_K001_19.data['N15_M07_F10_K001_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F10_K001_20')
    N15_M07_F10_K001_20 = N15_M07_F10_K001_20.data['N15_M07_F10_K001_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_1')
    N15_M07_F10_KA01_1 = N15_M07_F10_KA01_1.data['N15_M07_F10_KA01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_2')
    N15_M07_F10_KA01_2 = N15_M07_F10_KA01_2.data['N15_M07_F10_KA01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_3')
    N15_M07_F10_KA01_3 = N15_M07_F10_KA01_3.data['N15_M07_F10_KA01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_4')
    N15_M07_F10_KA01_4 = N15_M07_F10_KA01_4.data['N15_M07_F10_KA01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_5')
    N15_M07_F10_KA01_5 = N15_M07_F10_KA01_5.data['N15_M07_F10_KA01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_6')
    N15_M07_F10_KA01_6 = N15_M07_F10_KA01_6.data['N15_M07_F10_KA01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_7')
    N15_M07_F10_KA01_7 = N15_M07_F10_KA01_7.data['N15_M07_F10_KA01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_8')
    N15_M07_F10_KA01_8 = N15_M07_F10_KA01_8.data['N15_M07_F10_KA01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_9')
    N15_M07_F10_KA01_9 = N15_M07_F10_KA01_9.data['N15_M07_F10_KA01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_10')
    N15_M07_F10_KA01_10 = N15_M07_F10_KA01_10.data['N15_M07_F10_KA01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_11')
    N15_M07_F10_KA01_11 = N15_M07_F10_KA01_11.data['N15_M07_F10_KA01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_12')
    N15_M07_F10_KA01_12 = N15_M07_F10_KA01_12.data['N15_M07_F10_KA01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_13')
    N15_M07_F10_KA01_13 = N15_M07_F10_KA01_13.data['N15_M07_F10_KA01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_14')
    N15_M07_F10_KA01_14 = N15_M07_F10_KA01_14.data['N15_M07_F10_KA01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_15')
    N15_M07_F10_KA01_15 = N15_M07_F10_KA01_15.data['N15_M07_F10_KA01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_16')
    N15_M07_F10_KA01_16 = N15_M07_F10_KA01_16.data['N15_M07_F10_KA01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_17')
    N15_M07_F10_KA01_17 = N15_M07_F10_KA01_17.data['N15_M07_F10_KA01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_18')
    N15_M07_F10_KA01_18 = N15_M07_F10_KA01_18.data['N15_M07_F10_KA01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_19')
    N15_M07_F10_KA01_19 = N15_M07_F10_KA01_19.data['N15_M07_F10_KA01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F10_KA01_20')
    N15_M07_F10_KA01_20 = N15_M07_F10_KA01_20.data['N15_M07_F10_KA01_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_1')
    N15_M07_F10_KI01_1 = N15_M07_F10_KI01_1.data['N15_M07_F10_KI01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_2')
    N15_M07_F10_KI01_2 = N15_M07_F10_KI01_2.data['N15_M07_F10_KI01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_3')
    N15_M07_F10_KI01_3 = N15_M07_F10_KI01_3.data['N15_M07_F10_KI01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_4')
    N15_M07_F10_KI01_4 = N15_M07_F10_KI01_4.data['N15_M07_F10_KI01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_5')
    N15_M07_F10_KI01_5 = N15_M07_F10_KI01_5.data['N15_M07_F10_KI01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_6')
    N15_M07_F10_KI01_6 = N15_M07_F10_KI01_6.data['N15_M07_F10_KI01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_7')
    N15_M07_F10_KI01_7 = N15_M07_F10_KI01_7.data['N15_M07_F10_KI01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_8')
    N15_M07_F10_KI01_8 = N15_M07_F10_KI01_8.data['N15_M07_F10_KI01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_9')
    N15_M07_F10_KI01_9 = N15_M07_F10_KI01_9.data['N15_M07_F10_KI01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_10')
    N15_M07_F10_KI01_10 = N15_M07_F10_KI01_10.data['N15_M07_F10_KI01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_11')
    N15_M07_F10_KI01_11 = N15_M07_F10_KI01_11.data['N15_M07_F10_KI01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_12')
    N15_M07_F10_KI01_12 = N15_M07_F10_KI01_12.data['N15_M07_F10_KI01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_13')
    N15_M07_F10_KI01_13 = N15_M07_F10_KI01_13.data['N15_M07_F10_KI01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_14')
    N15_M07_F10_KI01_14 = N15_M07_F10_KI01_14.data['N15_M07_F10_KI01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_15')
    N15_M07_F10_KI01_15 = N15_M07_F10_KI01_15.data['N15_M07_F10_KI01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_16')
    N15_M07_F10_KI01_16 = N15_M07_F10_KI01_16.data['N15_M07_F10_KI01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_17')
    N15_M07_F10_KI01_17 = N15_M07_F10_KI01_17.data['N15_M07_F10_KI01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_18')
    N15_M07_F10_KI01_18 = N15_M07_F10_KI01_18.data['N15_M07_F10_KI01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_19')
    N15_M07_F10_KI01_19 = N15_M07_F10_KI01_19.data['N15_M07_F10_KI01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F10_KI01_20')
    N15_M07_F10_KI01_20 = N15_M07_F10_KI01_20.data['N15_M07_F10_KI01_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_1')
    N15_M07_F10_KB24_1 = N15_M07_F10_KB24_1.data['N15_M07_F10_KB24_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_2')
    N15_M07_F10_KB24_2 = N15_M07_F10_KB24_2.data['N15_M07_F10_KB24_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_3')
    N15_M07_F10_KB24_3 = N15_M07_F10_KB24_3.data['N15_M07_F10_KB24_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_4')
    N15_M07_F10_KB24_4 = N15_M07_F10_KB24_4.data['N15_M07_F10_KB24_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_5')
    N15_M07_F10_KB24_5 = N15_M07_F10_KB24_5.data['N15_M07_F10_KB24_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_6')
    N15_M07_F10_KB24_6 = N15_M07_F10_KB24_6.data['N15_M07_F10_KB24_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_7')
    N15_M07_F10_KB24_7 = N15_M07_F10_KB24_7.data['N15_M07_F10_KB24_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_8')
    N15_M07_F10_KB24_8 = N15_M07_F10_KB24_8.data['N15_M07_F10_KB24_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_9')
    N15_M07_F10_KB24_9 = N15_M07_F10_KB24_9.data['N15_M07_F10_KB24_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_10')
    N15_M07_F10_KB24_10 = N15_M07_F10_KB24_10.data['N15_M07_F10_KB24_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_11')
    N15_M07_F10_KB24_11 = N15_M07_F10_KB24_11.data['N15_M07_F10_KB24_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_12')
    N15_M07_F10_KB24_12 = N15_M07_F10_KB24_12.data['N15_M07_F10_KB24_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_13')
    N15_M07_F10_KB24_13 = N15_M07_F10_KB24_13.data['N15_M07_F10_KB24_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_14')
    N15_M07_F10_KB24_14 = N15_M07_F10_KB24_14.data['N15_M07_F10_KB24_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_15')
    N15_M07_F10_KB24_15 = N15_M07_F10_KB24_15.data['N15_M07_F10_KB24_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_16')
    N15_M07_F10_KB24_16 = N15_M07_F10_KB24_16.data['N15_M07_F10_KB24_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_17')
    N15_M07_F10_KB24_17 = N15_M07_F10_KB24_17.data['N15_M07_F10_KB24_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_18')
    N15_M07_F10_KB24_18 = N15_M07_F10_KB24_18.data['N15_M07_F10_KB24_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_19')
    N15_M07_F10_KB24_19 = N15_M07_F10_KB24_19.data['N15_M07_F10_KB24_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F10_KB24_20')
    N15_M07_F10_KB24_20 = N15_M07_F10_KB24_20.data['N15_M07_F10_KB24_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_1')
    N15_M07_F10_KB27_1 = N15_M07_F10_KB27_1.data['N15_M07_F10_KB27_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_2')
    N15_M07_F10_KB27_2 = N15_M07_F10_KB27_2.data['N15_M07_F10_KB27_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_3')
    N15_M07_F10_KB27_3 = N15_M07_F10_KB27_3.data['N15_M07_F10_KB27_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_4')
    N15_M07_F10_KB27_4 = N15_M07_F10_KB27_4.data['N15_M07_F10_KB27_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_5')
    N15_M07_F10_KB27_5 = N15_M07_F10_KB27_5.data['N15_M07_F10_KB27_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_6')
    N15_M07_F10_KB27_6 = N15_M07_F10_KB27_6.data['N15_M07_F10_KB27_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_7')
    N15_M07_F10_KB27_7 = N15_M07_F10_KB27_7.data['N15_M07_F10_KB27_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_8')
    N15_M07_F10_KB27_8 = N15_M07_F10_KB27_8.data['N15_M07_F10_KB27_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_9')
    N15_M07_F10_KB27_9 = N15_M07_F10_KB27_9.data['N15_M07_F10_KB27_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_10')
    N15_M07_F10_KB27_10 = N15_M07_F10_KB27_10.data['N15_M07_F10_KB27_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_11')
    N15_M07_F10_KB27_11 = N15_M07_F10_KB27_11.data['N15_M07_F10_KB27_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_12')
    N15_M07_F10_KB27_12 = N15_M07_F10_KB27_12.data['N15_M07_F10_KB27_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_13')
    N15_M07_F10_KB27_13 = N15_M07_F10_KB27_13.data['N15_M07_F10_KB27_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_14')
    N15_M07_F10_KB27_14 = N15_M07_F10_KB27_14.data['N15_M07_F10_KB27_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_15')
    N15_M07_F10_KB27_15 = N15_M07_F10_KB27_15.data['N15_M07_F10_KB27_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_16')
    N15_M07_F10_KB27_16 = N15_M07_F10_KB27_16.data['N15_M07_F10_KB27_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_17')
    N15_M07_F10_KB27_17 = N15_M07_F10_KB27_17.data['N15_M07_F10_KB27_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_18')
    N15_M07_F10_KB27_18 = N15_M07_F10_KB27_18.data['N15_M07_F10_KB27_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_19')
    N15_M07_F10_KB27_19 = N15_M07_F10_KB27_19.data['N15_M07_F10_KB27_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F10_KB27_20')
    N15_M07_F10_KB27_20 = N15_M07_F10_KB27_20.data['N15_M07_F10_KB27_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    合并N15_M07_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F10 = np.append(N15_M07_F10_K001_1, N15_M07_F10_K001_2)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_3)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_4)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_5)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_6)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_7)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_8)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_9)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_10)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_11)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_12)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_13)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_14)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_15)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_16)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_17)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_18)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_19)
    N15_M07_F10 = np.append(N15_M07_F10, N15_M07_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F10_Outer = np.append(N15_M07_F10_KA01_1, N15_M07_F10_KA01_2)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_3)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_4)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_5)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_6)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_7)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_8)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_9)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_10)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_11)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_12)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_13)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_14)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_15)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_16)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_17)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_18)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_19)
    N15_M07_F10_Outer = np.append(N15_M07_F10_Outer, N15_M07_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F10_Inner = np.append(N15_M07_F10_KI01_1, N15_M07_F10_KI01_2)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_3)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_4)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_5)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_6)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_7)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_8)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_9)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_10)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_11)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_12)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_13)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_14)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_15)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_16)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_17)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_18)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_19)
    N15_M07_F10_Inner = np.append(N15_M07_F10_Inner, N15_M07_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F10_IROR = np.append(N15_M07_F10_KB24_1, N15_M07_F10_KB24_2)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_3)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_4)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_5)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_6)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_7)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_8)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_9)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_10)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_11)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_12)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_13)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_14)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_15)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_16)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_17)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_18)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_19)
    N15_M07_F10_IROR = np.append(N15_M07_F10_IROR, N15_M07_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F10_ORIR = np.append(N15_M07_F10_KB27_1, N15_M07_F10_KB27_2)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_3)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_4)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_5)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_6)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_7)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_8)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_9)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_10)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_11)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_12)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_13)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_14)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_15)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_16)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_17)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_18)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_19)
    N15_M07_F10_ORIR = np.append(N15_M07_F10_ORIR, N15_M07_F10_KB27_20)

    N15_M07_F10_ALL.append(N15_M07_F10)
    N15_M07_F10_ALL.append(N15_M07_F10_Outer)
    N15_M07_F10_ALL.append(N15_M07_F10_Inner)
    N15_M07_F10_ALL.append(N15_M07_F10_IROR)
    N15_M07_F10_ALL.append(N15_M07_F10_ORIR)

    return N15_M07_F10_ALL
def load_N15_M01_F10_phase_current1_data():
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
    N15_M01_F10_K001_1 = N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][1][2][0].flatten()
    # N15_M01_F10_K001_MCS_1 = N15_M01_F10_K001_1.data[]

    N15_M01_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_2')
    N15_M01_F10_K001_2 = N15_M01_F10_K001_2.data['N15_M01_F10_K001_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_3')
    N15_M01_F10_K001_3 = N15_M01_F10_K001_3.data['N15_M01_F10_K001_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_4')
    N15_M01_F10_K001_4 = N15_M01_F10_K001_4.data['N15_M01_F10_K001_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_5')
    N15_M01_F10_K001_5 = N15_M01_F10_K001_5.data['N15_M01_F10_K001_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_6')
    N15_M01_F10_K001_6 = N15_M01_F10_K001_6.data['N15_M01_F10_K001_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_7')
    N15_M01_F10_K001_7 = N15_M01_F10_K001_7.data['N15_M01_F10_K001_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_8')
    N15_M01_F10_K001_8 = N15_M01_F10_K001_8.data['N15_M01_F10_K001_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_9')
    N15_M01_F10_K001_9 = N15_M01_F10_K001_9.data['N15_M01_F10_K001_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_10')
    N15_M01_F10_K001_10 = N15_M01_F10_K001_10.data['N15_M01_F10_K001_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_11')
    N15_M01_F10_K001_11 = N15_M01_F10_K001_11.data['N15_M01_F10_K001_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_12')
    N15_M01_F10_K001_12 = N15_M01_F10_K001_12.data['N15_M01_F10_K001_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_13')
    N15_M01_F10_K001_13 = N15_M01_F10_K001_13.data['N15_M01_F10_K001_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_14')
    N15_M01_F10_K001_14 = N15_M01_F10_K001_14.data['N15_M01_F10_K001_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_15')
    N15_M01_F10_K001_15 = N15_M01_F10_K001_15.data['N15_M01_F10_K001_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_16')
    N15_M01_F10_K001_16 = N15_M01_F10_K001_16.data['N15_M01_F10_K001_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_17')
    N15_M01_F10_K001_17 = N15_M01_F10_K001_17.data['N15_M01_F10_K001_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_18')
    N15_M01_F10_K001_18 = N15_M01_F10_K001_18.data['N15_M01_F10_K001_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_19')
    N15_M01_F10_K001_19 = N15_M01_F10_K001_19.data['N15_M01_F10_K001_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_20')
    N15_M01_F10_K001_20 = N15_M01_F10_K001_20.data['N15_M01_F10_K001_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M01_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_1')
    N15_M01_F10_KA01_1 = N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_2')
    N15_M01_F10_KA01_2 = N15_M01_F10_KA01_2.data['N15_M01_F10_KA01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_3')
    N15_M01_F10_KA01_3 = N15_M01_F10_KA01_3.data['N15_M01_F10_KA01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_4')
    N15_M01_F10_KA01_4 = N15_M01_F10_KA01_4.data['N15_M01_F10_KA01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_5')
    N15_M01_F10_KA01_5 = N15_M01_F10_KA01_5.data['N15_M01_F10_KA01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_6')
    N15_M01_F10_KA01_6 = N15_M01_F10_KA01_6.data['N15_M01_F10_KA01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_7')
    N15_M01_F10_KA01_7 = N15_M01_F10_KA01_7.data['N15_M01_F10_KA01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_8')
    N15_M01_F10_KA01_8 = N15_M01_F10_KA01_8.data['N15_M01_F10_KA01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_9')
    N15_M01_F10_KA01_9 = N15_M01_F10_KA01_9.data['N15_M01_F10_KA01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_10')
    N15_M01_F10_KA01_10 = N15_M01_F10_KA01_10.data['N15_M01_F10_KA01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_11')
    N15_M01_F10_KA01_11 = N15_M01_F10_KA01_11.data['N15_M01_F10_KA01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_12')
    N15_M01_F10_KA01_12 = N15_M01_F10_KA01_12.data['N15_M01_F10_KA01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_13')
    N15_M01_F10_KA01_13 = N15_M01_F10_KA01_13.data['N15_M01_F10_KA01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_14')
    N15_M01_F10_KA01_14 = N15_M01_F10_KA01_14.data['N15_M01_F10_KA01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_15')
    N15_M01_F10_KA01_15 = N15_M01_F10_KA01_15.data['N15_M01_F10_KA01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_16')
    N15_M01_F10_KA01_16 = N15_M01_F10_KA01_16.data['N15_M01_F10_KA01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_17')
    N15_M01_F10_KA01_17 = N15_M01_F10_KA01_17.data['N15_M01_F10_KA01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_18')
    N15_M01_F10_KA01_18 = N15_M01_F10_KA01_18.data['N15_M01_F10_KA01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_19')
    N15_M01_F10_KA01_19 = N15_M01_F10_KA01_19.data['N15_M01_F10_KA01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_20')
    N15_M01_F10_KA01_20 = N15_M01_F10_KA01_20.data['N15_M01_F10_KA01_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M01_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_1')
    N15_M01_F10_KI01_1 = N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_2')
    N15_M01_F10_KI01_2 = N15_M01_F10_KI01_2.data['N15_M01_F10_KI01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_3')
    N15_M01_F10_KI01_3 = N15_M01_F10_KI01_3.data['N15_M01_F10_KI01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_4')
    N15_M01_F10_KI01_4 = N15_M01_F10_KI01_4.data['N15_M01_F10_KI01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_5')
    N15_M01_F10_KI01_5 = N15_M01_F10_KI01_5.data['N15_M01_F10_KI01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_6')
    N15_M01_F10_KI01_6 = N15_M01_F10_KI01_6.data['N15_M01_F10_KI01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_7')
    N15_M01_F10_KI01_7 = N15_M01_F10_KI01_7.data['N15_M01_F10_KI01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_8')
    N15_M01_F10_KI01_8 = N15_M01_F10_KI01_8.data['N15_M01_F10_KI01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_9')
    N15_M01_F10_KI01_9 = N15_M01_F10_KI01_9.data['N15_M01_F10_KI01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_10')
    N15_M01_F10_KI01_10 = N15_M01_F10_KI01_10.data['N15_M01_F10_KI01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_11')
    N15_M01_F10_KI01_11 = N15_M01_F10_KI01_11.data['N15_M01_F10_KI01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_12')
    N15_M01_F10_KI01_12 = N15_M01_F10_KI01_12.data['N15_M01_F10_KI01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_13')
    N15_M01_F10_KI01_13 = N15_M01_F10_KI01_13.data['N15_M01_F10_KI01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_14')
    N15_M01_F10_KI01_14 = N15_M01_F10_KI01_14.data['N15_M01_F10_KI01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_15')
    N15_M01_F10_KI01_15 = N15_M01_F10_KI01_15.data['N15_M01_F10_KI01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_16')
    N15_M01_F10_KI01_16 = N15_M01_F10_KI01_16.data['N15_M01_F10_KI01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_17')
    N15_M01_F10_KI01_17 = N15_M01_F10_KI01_17.data['N15_M01_F10_KI01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_18')
    N15_M01_F10_KI01_18 = N15_M01_F10_KI01_18.data['N15_M01_F10_KI01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_19')
    N15_M01_F10_KI01_19 = N15_M01_F10_KI01_19.data['N15_M01_F10_KI01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_20')
    N15_M01_F10_KI01_20 = N15_M01_F10_KI01_20.data['N15_M01_F10_KI01_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M01_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_1')
    N15_M01_F10_KB24_1 = N15_M01_F10_KB24_1.data['N15_M01_F10_KB24_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_2')
    N15_M01_F10_KB24_2 = N15_M01_F10_KB24_2.data['N15_M01_F10_KB24_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_3')
    N15_M01_F10_KB24_3 = N15_M01_F10_KB24_3.data['N15_M01_F10_KB24_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_4')
    N15_M01_F10_KB24_4 = N15_M01_F10_KB24_4.data['N15_M01_F10_KB24_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_5')
    N15_M01_F10_KB24_5 = N15_M01_F10_KB24_5.data['N15_M01_F10_KB24_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_6')
    N15_M01_F10_KB24_6 = N15_M01_F10_KB24_6.data['N15_M01_F10_KB24_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_7')
    N15_M01_F10_KB24_7 = N15_M01_F10_KB24_7.data['N15_M01_F10_KB24_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_8')
    N15_M01_F10_KB24_8 = N15_M01_F10_KB24_8.data['N15_M01_F10_KB24_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_9')
    N15_M01_F10_KB24_9 = N15_M01_F10_KB24_9.data['N15_M01_F10_KB24_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_10')
    N15_M01_F10_KB24_10 = N15_M01_F10_KB24_10.data['N15_M01_F10_KB24_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_11')
    N15_M01_F10_KB24_11 = N15_M01_F10_KB24_11.data['N15_M01_F10_KB24_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_12')
    N15_M01_F10_KB24_12 = N15_M01_F10_KB24_12.data['N15_M01_F10_KB24_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_13')
    N15_M01_F10_KB24_13 = N15_M01_F10_KB24_13.data['N15_M01_F10_KB24_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_14')
    N15_M01_F10_KB24_14 = N15_M01_F10_KB24_14.data['N15_M01_F10_KB24_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_15')
    N15_M01_F10_KB24_15 = N15_M01_F10_KB24_15.data['N15_M01_F10_KB24_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_16')
    N15_M01_F10_KB24_16 = N15_M01_F10_KB24_16.data['N15_M01_F10_KB24_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_17')
    N15_M01_F10_KB24_17 = N15_M01_F10_KB24_17.data['N15_M01_F10_KB24_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_18')
    N15_M01_F10_KB24_18 = N15_M01_F10_KB24_18.data['N15_M01_F10_KB24_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_19')
    N15_M01_F10_KB24_19 = N15_M01_F10_KB24_19.data['N15_M01_F10_KB24_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_20')
    N15_M01_F10_KB24_20 = N15_M01_F10_KB24_20.data['N15_M01_F10_KB24_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M01_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_1')
    N15_M01_F10_KB27_1 = N15_M01_F10_KB27_1.data['N15_M01_F10_KB27_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_2')
    N15_M01_F10_KB27_2 = N15_M01_F10_KB27_2.data['N15_M01_F10_KB27_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_3')
    N15_M01_F10_KB27_3 = N15_M01_F10_KB27_3.data['N15_M01_F10_KB27_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_4')
    N15_M01_F10_KB27_4 = N15_M01_F10_KB27_4.data['N15_M01_F10_KB27_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_5')
    N15_M01_F10_KB27_5 = N15_M01_F10_KB27_5.data['N15_M01_F10_KB27_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_6')
    N15_M01_F10_KB27_6 = N15_M01_F10_KB27_6.data['N15_M01_F10_KB27_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_7')
    N15_M01_F10_KB27_7 = N15_M01_F10_KB27_7.data['N15_M01_F10_KB27_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_8')
    N15_M01_F10_KB27_8 = N15_M01_F10_KB27_8.data['N15_M01_F10_KB27_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_9')
    N15_M01_F10_KB27_9 = N15_M01_F10_KB27_9.data['N15_M01_F10_KB27_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_10')
    N15_M01_F10_KB27_10 = N15_M01_F10_KB27_10.data['N15_M01_F10_KB27_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_11')
    N15_M01_F10_KB27_11 = N15_M01_F10_KB27_11.data['N15_M01_F10_KB27_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_12')
    N15_M01_F10_KB27_12 = N15_M01_F10_KB27_12.data['N15_M01_F10_KB27_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_13')
    N15_M01_F10_KB27_13 = N15_M01_F10_KB27_13.data['N15_M01_F10_KB27_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_14')
    N15_M01_F10_KB27_14 = N15_M01_F10_KB27_14.data['N15_M01_F10_KB27_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_15')
    N15_M01_F10_KB27_15 = N15_M01_F10_KB27_15.data['N15_M01_F10_KB27_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_16')
    N15_M01_F10_KB27_16 = N15_M01_F10_KB27_16.data['N15_M01_F10_KB27_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_17')
    N15_M01_F10_KB27_17 = N15_M01_F10_KB27_17.data['N15_M01_F10_KB27_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_18')
    N15_M01_F10_KB27_18 = N15_M01_F10_KB27_18.data['N15_M01_F10_KB27_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_19')
    N15_M01_F10_KB27_19 = N15_M01_F10_KB27_19.data['N15_M01_F10_KB27_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M01_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_20')
    N15_M01_F10_KB27_20 = N15_M01_F10_KB27_20.data['N15_M01_F10_KB27_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    合并N15_M01_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M01_F10 = np.append(N15_M01_F10_K001_1, N15_M01_F10_K001_2)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_3)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_4)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_5)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_6)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_7)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_8)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_9)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_10)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_11)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_12)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_13)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_14)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_15)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_16)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_17)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_18)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_19)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M01_F10_Outer = np.append(N15_M01_F10_KA01_1, N15_M01_F10_KA01_2)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_3)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_4)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_5)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_6)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_7)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_8)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_9)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_10)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_11)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_12)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_13)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_14)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_15)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_16)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_17)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_18)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_19)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M01_F10_Inner = np.append(N15_M01_F10_KI01_1, N15_M01_F10_KI01_2)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_3)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_4)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_5)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_6)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_7)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_8)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_9)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_10)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_11)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_12)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_13)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_14)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_15)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_16)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_17)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_18)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_19)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M01_F10_IROR = np.append(N15_M01_F10_KB24_1, N15_M01_F10_KB24_2)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_3)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_4)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_5)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_6)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_7)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_8)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_9)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_10)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_11)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_12)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_13)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_14)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_15)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_16)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_17)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_18)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_19)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M01_F10_ORIR = np.append(N15_M01_F10_KB27_1, N15_M01_F10_KB27_2)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_3)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_4)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_5)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_6)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_7)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_8)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_9)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_10)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_11)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_12)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_13)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_14)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_15)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_16)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_17)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_18)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_19)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_20)

    N15_M01_F10_ALL.append(N15_M01_F10)
    N15_M01_F10_ALL.append(N15_M01_F10_Outer)
    N15_M01_F10_ALL.append(N15_M01_F10_Inner)
    N15_M01_F10_ALL.append(N15_M01_F10_IROR)
    N15_M01_F10_ALL.append(N15_M01_F10_ORIR)

    return N15_M01_F10_ALL
def load_N15_M01_F10_phase_current2_data():
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
    N15_M01_F10_K001_1 = N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][2][2][0].flatten()
    # N15_M01_F10_K001_MCS_1 = N15_M01_F10_K001_1.data[]

    N15_M01_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_2')
    N15_M01_F10_K001_2 = N15_M01_F10_K001_2.data['N15_M01_F10_K001_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_3')
    N15_M01_F10_K001_3 = N15_M01_F10_K001_3.data['N15_M01_F10_K001_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_4')
    N15_M01_F10_K001_4 = N15_M01_F10_K001_4.data['N15_M01_F10_K001_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_5')
    N15_M01_F10_K001_5 = N15_M01_F10_K001_5.data['N15_M01_F10_K001_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_6')
    N15_M01_F10_K001_6 = N15_M01_F10_K001_6.data['N15_M01_F10_K001_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_7')
    N15_M01_F10_K001_7 = N15_M01_F10_K001_7.data['N15_M01_F10_K001_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_8')
    N15_M01_F10_K001_8 = N15_M01_F10_K001_8.data['N15_M01_F10_K001_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_9')
    N15_M01_F10_K001_9 = N15_M01_F10_K001_9.data['N15_M01_F10_K001_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_10')
    N15_M01_F10_K001_10 = N15_M01_F10_K001_10.data['N15_M01_F10_K001_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_11')
    N15_M01_F10_K001_11 = N15_M01_F10_K001_11.data['N15_M01_F10_K001_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_12')
    N15_M01_F10_K001_12 = N15_M01_F10_K001_12.data['N15_M01_F10_K001_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_13')
    N15_M01_F10_K001_13 = N15_M01_F10_K001_13.data['N15_M01_F10_K001_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_14')
    N15_M01_F10_K001_14 = N15_M01_F10_K001_14.data['N15_M01_F10_K001_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_15')
    N15_M01_F10_K001_15 = N15_M01_F10_K001_15.data['N15_M01_F10_K001_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_16')
    N15_M01_F10_K001_16 = N15_M01_F10_K001_16.data['N15_M01_F10_K001_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_17')
    N15_M01_F10_K001_17 = N15_M01_F10_K001_17.data['N15_M01_F10_K001_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_18')
    N15_M01_F10_K001_18 = N15_M01_F10_K001_18.data['N15_M01_F10_K001_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_19')
    N15_M01_F10_K001_19 = N15_M01_F10_K001_19.data['N15_M01_F10_K001_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_20')
    N15_M01_F10_K001_20 = N15_M01_F10_K001_20.data['N15_M01_F10_K001_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M01_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_1')
    N15_M01_F10_KA01_1 = N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_2')
    N15_M01_F10_KA01_2 = N15_M01_F10_KA01_2.data['N15_M01_F10_KA01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_3')
    N15_M01_F10_KA01_3 = N15_M01_F10_KA01_3.data['N15_M01_F10_KA01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_4')
    N15_M01_F10_KA01_4 = N15_M01_F10_KA01_4.data['N15_M01_F10_KA01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_5')
    N15_M01_F10_KA01_5 = N15_M01_F10_KA01_5.data['N15_M01_F10_KA01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_6')
    N15_M01_F10_KA01_6 = N15_M01_F10_KA01_6.data['N15_M01_F10_KA01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_7')
    N15_M01_F10_KA01_7 = N15_M01_F10_KA01_7.data['N15_M01_F10_KA01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_8')
    N15_M01_F10_KA01_8 = N15_M01_F10_KA01_8.data['N15_M01_F10_KA01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_9')
    N15_M01_F10_KA01_9 = N15_M01_F10_KA01_9.data['N15_M01_F10_KA01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_10')
    N15_M01_F10_KA01_10 = N15_M01_F10_KA01_10.data['N15_M01_F10_KA01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_11')
    N15_M01_F10_KA01_11 = N15_M01_F10_KA01_11.data['N15_M01_F10_KA01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_12')
    N15_M01_F10_KA01_12 = N15_M01_F10_KA01_12.data['N15_M01_F10_KA01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_13')
    N15_M01_F10_KA01_13 = N15_M01_F10_KA01_13.data['N15_M01_F10_KA01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_14')
    N15_M01_F10_KA01_14 = N15_M01_F10_KA01_14.data['N15_M01_F10_KA01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_15')
    N15_M01_F10_KA01_15 = N15_M01_F10_KA01_15.data['N15_M01_F10_KA01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_16')
    N15_M01_F10_KA01_16 = N15_M01_F10_KA01_16.data['N15_M01_F10_KA01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_17')
    N15_M01_F10_KA01_17 = N15_M01_F10_KA01_17.data['N15_M01_F10_KA01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_18')
    N15_M01_F10_KA01_18 = N15_M01_F10_KA01_18.data['N15_M01_F10_KA01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_19')
    N15_M01_F10_KA01_19 = N15_M01_F10_KA01_19.data['N15_M01_F10_KA01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_20')
    N15_M01_F10_KA01_20 = N15_M01_F10_KA01_20.data['N15_M01_F10_KA01_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M01_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_1')
    N15_M01_F10_KI01_1 = N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_2')
    N15_M01_F10_KI01_2 = N15_M01_F10_KI01_2.data['N15_M01_F10_KI01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_3')
    N15_M01_F10_KI01_3 = N15_M01_F10_KI01_3.data['N15_M01_F10_KI01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_4')
    N15_M01_F10_KI01_4 = N15_M01_F10_KI01_4.data['N15_M01_F10_KI01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_5')
    N15_M01_F10_KI01_5 = N15_M01_F10_KI01_5.data['N15_M01_F10_KI01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_6')
    N15_M01_F10_KI01_6 = N15_M01_F10_KI01_6.data['N15_M01_F10_KI01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_7')
    N15_M01_F10_KI01_7 = N15_M01_F10_KI01_7.data['N15_M01_F10_KI01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_8')
    N15_M01_F10_KI01_8 = N15_M01_F10_KI01_8.data['N15_M01_F10_KI01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_9')
    N15_M01_F10_KI01_9 = N15_M01_F10_KI01_9.data['N15_M01_F10_KI01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_10')
    N15_M01_F10_KI01_10 = N15_M01_F10_KI01_10.data['N15_M01_F10_KI01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_11')
    N15_M01_F10_KI01_11 = N15_M01_F10_KI01_11.data['N15_M01_F10_KI01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_12')
    N15_M01_F10_KI01_12 = N15_M01_F10_KI01_12.data['N15_M01_F10_KI01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_13')
    N15_M01_F10_KI01_13 = N15_M01_F10_KI01_13.data['N15_M01_F10_KI01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_14')
    N15_M01_F10_KI01_14 = N15_M01_F10_KI01_14.data['N15_M01_F10_KI01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_15')
    N15_M01_F10_KI01_15 = N15_M01_F10_KI01_15.data['N15_M01_F10_KI01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_16')
    N15_M01_F10_KI01_16 = N15_M01_F10_KI01_16.data['N15_M01_F10_KI01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_17')
    N15_M01_F10_KI01_17 = N15_M01_F10_KI01_17.data['N15_M01_F10_KI01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_18')
    N15_M01_F10_KI01_18 = N15_M01_F10_KI01_18.data['N15_M01_F10_KI01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_19')
    N15_M01_F10_KI01_19 = N15_M01_F10_KI01_19.data['N15_M01_F10_KI01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_20')
    N15_M01_F10_KI01_20 = N15_M01_F10_KI01_20.data['N15_M01_F10_KI01_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M01_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_1')
    N15_M01_F10_KB24_1 = N15_M01_F10_KB24_1.data['N15_M01_F10_KB24_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_2')
    N15_M01_F10_KB24_2 = N15_M01_F10_KB24_2.data['N15_M01_F10_KB24_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_3')
    N15_M01_F10_KB24_3 = N15_M01_F10_KB24_3.data['N15_M01_F10_KB24_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_4')
    N15_M01_F10_KB24_4 = N15_M01_F10_KB24_4.data['N15_M01_F10_KB24_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_5')
    N15_M01_F10_KB24_5 = N15_M01_F10_KB24_5.data['N15_M01_F10_KB24_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_6')
    N15_M01_F10_KB24_6 = N15_M01_F10_KB24_6.data['N15_M01_F10_KB24_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_7')
    N15_M01_F10_KB24_7 = N15_M01_F10_KB24_7.data['N15_M01_F10_KB24_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_8')
    N15_M01_F10_KB24_8 = N15_M01_F10_KB24_8.data['N15_M01_F10_KB24_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_9')
    N15_M01_F10_KB24_9 = N15_M01_F10_KB24_9.data['N15_M01_F10_KB24_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_10')
    N15_M01_F10_KB24_10 = N15_M01_F10_KB24_10.data['N15_M01_F10_KB24_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_11')
    N15_M01_F10_KB24_11 = N15_M01_F10_KB24_11.data['N15_M01_F10_KB24_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_12')
    N15_M01_F10_KB24_12 = N15_M01_F10_KB24_12.data['N15_M01_F10_KB24_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_13')
    N15_M01_F10_KB24_13 = N15_M01_F10_KB24_13.data['N15_M01_F10_KB24_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_14')
    N15_M01_F10_KB24_14 = N15_M01_F10_KB24_14.data['N15_M01_F10_KB24_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_15')
    N15_M01_F10_KB24_15 = N15_M01_F10_KB24_15.data['N15_M01_F10_KB24_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_16')
    N15_M01_F10_KB24_16 = N15_M01_F10_KB24_16.data['N15_M01_F10_KB24_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_17')
    N15_M01_F10_KB24_17 = N15_M01_F10_KB24_17.data['N15_M01_F10_KB24_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_18')
    N15_M01_F10_KB24_18 = N15_M01_F10_KB24_18.data['N15_M01_F10_KB24_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_19')
    N15_M01_F10_KB24_19 = N15_M01_F10_KB24_19.data['N15_M01_F10_KB24_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_20')
    N15_M01_F10_KB24_20 = N15_M01_F10_KB24_20.data['N15_M01_F10_KB24_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M01_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_1')
    N15_M01_F10_KB27_1 = N15_M01_F10_KB27_1.data['N15_M01_F10_KB27_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_2')
    N15_M01_F10_KB27_2 = N15_M01_F10_KB27_2.data['N15_M01_F10_KB27_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_3')
    N15_M01_F10_KB27_3 = N15_M01_F10_KB27_3.data['N15_M01_F10_KB27_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_4')
    N15_M01_F10_KB27_4 = N15_M01_F10_KB27_4.data['N15_M01_F10_KB27_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_5')
    N15_M01_F10_KB27_5 = N15_M01_F10_KB27_5.data['N15_M01_F10_KB27_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_6')
    N15_M01_F10_KB27_6 = N15_M01_F10_KB27_6.data['N15_M01_F10_KB27_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_7')
    N15_M01_F10_KB27_7 = N15_M01_F10_KB27_7.data['N15_M01_F10_KB27_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_8')
    N15_M01_F10_KB27_8 = N15_M01_F10_KB27_8.data['N15_M01_F10_KB27_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_9')
    N15_M01_F10_KB27_9 = N15_M01_F10_KB27_9.data['N15_M01_F10_KB27_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_10')
    N15_M01_F10_KB27_10 = N15_M01_F10_KB27_10.data['N15_M01_F10_KB27_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_11')
    N15_M01_F10_KB27_11 = N15_M01_F10_KB27_11.data['N15_M01_F10_KB27_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_12')
    N15_M01_F10_KB27_12 = N15_M01_F10_KB27_12.data['N15_M01_F10_KB27_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_13')
    N15_M01_F10_KB27_13 = N15_M01_F10_KB27_13.data['N15_M01_F10_KB27_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_14')
    N15_M01_F10_KB27_14 = N15_M01_F10_KB27_14.data['N15_M01_F10_KB27_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_15')
    N15_M01_F10_KB27_15 = N15_M01_F10_KB27_15.data['N15_M01_F10_KB27_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_16')
    N15_M01_F10_KB27_16 = N15_M01_F10_KB27_16.data['N15_M01_F10_KB27_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_17')
    N15_M01_F10_KB27_17 = N15_M01_F10_KB27_17.data['N15_M01_F10_KB27_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_18')
    N15_M01_F10_KB27_18 = N15_M01_F10_KB27_18.data['N15_M01_F10_KB27_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_19')
    N15_M01_F10_KB27_19 = N15_M01_F10_KB27_19.data['N15_M01_F10_KB27_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M01_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_20')
    N15_M01_F10_KB27_20 = N15_M01_F10_KB27_20.data['N15_M01_F10_KB27_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    合并N15_M01_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M01_F10 = np.append(N15_M01_F10_K001_1, N15_M01_F10_K001_2)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_3)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_4)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_5)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_6)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_7)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_8)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_9)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_10)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_11)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_12)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_13)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_14)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_15)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_16)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_17)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_18)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_19)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M01_F10_Outer = np.append(N15_M01_F10_KA01_1, N15_M01_F10_KA01_2)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_3)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_4)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_5)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_6)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_7)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_8)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_9)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_10)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_11)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_12)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_13)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_14)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_15)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_16)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_17)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_18)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_19)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M01_F10_Inner = np.append(N15_M01_F10_KI01_1, N15_M01_F10_KI01_2)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_3)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_4)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_5)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_6)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_7)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_8)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_9)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_10)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_11)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_12)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_13)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_14)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_15)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_16)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_17)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_18)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_19)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M01_F10_IROR = np.append(N15_M01_F10_KB24_1, N15_M01_F10_KB24_2)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_3)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_4)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_5)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_6)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_7)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_8)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_9)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_10)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_11)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_12)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_13)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_14)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_15)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_16)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_17)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_18)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_19)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M01_F10_ORIR = np.append(N15_M01_F10_KB27_1, N15_M01_F10_KB27_2)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_3)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_4)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_5)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_6)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_7)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_8)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_9)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_10)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_11)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_12)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_13)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_14)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_15)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_16)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_17)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_18)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_19)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_20)

    N15_M01_F10_ALL.append(N15_M01_F10)
    N15_M01_F10_ALL.append(N15_M01_F10_Outer)
    N15_M01_F10_ALL.append(N15_M01_F10_Inner)
    N15_M01_F10_ALL.append(N15_M01_F10_IROR)
    N15_M01_F10_ALL.append(N15_M01_F10_ORIR)

    return N15_M01_F10_ALL
def load_N15_M01_F10_Vibration_data():
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
    N15_M01_F10_K001_1 = N15_M01_F10_K001_1.data['N15_M01_F10_K001_1']['Y'][0][0][0][-1][2][0].flatten()
    # N15_M01_F10_K001_MCS_1 = N15_M01_F10_K001_1.data[]

    N15_M01_F10_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_2')
    N15_M01_F10_K001_2 = N15_M01_F10_K001_2.data['N15_M01_F10_K001_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_3')
    N15_M01_F10_K001_3 = N15_M01_F10_K001_3.data['N15_M01_F10_K001_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_4')
    N15_M01_F10_K001_4 = N15_M01_F10_K001_4.data['N15_M01_F10_K001_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_5')
    N15_M01_F10_K001_5 = N15_M01_F10_K001_5.data['N15_M01_F10_K001_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_6')
    N15_M01_F10_K001_6 = N15_M01_F10_K001_6.data['N15_M01_F10_K001_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_7')
    N15_M01_F10_K001_7 = N15_M01_F10_K001_7.data['N15_M01_F10_K001_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_8')
    N15_M01_F10_K001_8 = N15_M01_F10_K001_8.data['N15_M01_F10_K001_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_9')
    N15_M01_F10_K001_9 = N15_M01_F10_K001_9.data['N15_M01_F10_K001_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_10')
    N15_M01_F10_K001_10 = N15_M01_F10_K001_10.data['N15_M01_F10_K001_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_11')
    N15_M01_F10_K001_11 = N15_M01_F10_K001_11.data['N15_M01_F10_K001_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_12')
    N15_M01_F10_K001_12 = N15_M01_F10_K001_12.data['N15_M01_F10_K001_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_13')
    N15_M01_F10_K001_13 = N15_M01_F10_K001_13.data['N15_M01_F10_K001_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_14')
    N15_M01_F10_K001_14 = N15_M01_F10_K001_14.data['N15_M01_F10_K001_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_15')
    N15_M01_F10_K001_15 = N15_M01_F10_K001_15.data['N15_M01_F10_K001_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_16')
    N15_M01_F10_K001_16 = N15_M01_F10_K001_16.data['N15_M01_F10_K001_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_17')
    N15_M01_F10_K001_17 = N15_M01_F10_K001_17.data['N15_M01_F10_K001_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_18')
    N15_M01_F10_K001_18 = N15_M01_F10_K001_18.data['N15_M01_F10_K001_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_19')
    N15_M01_F10_K001_19 = N15_M01_F10_K001_19.data['N15_M01_F10_K001_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M01_F10_K001_20')
    N15_M01_F10_K001_20 = N15_M01_F10_K001_20.data['N15_M01_F10_K001_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M01_F10_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_1')
    N15_M01_F10_KA01_1 = N15_M01_F10_KA01_1.data['N15_M01_F10_KA01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_2')
    N15_M01_F10_KA01_2 = N15_M01_F10_KA01_2.data['N15_M01_F10_KA01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_3')
    N15_M01_F10_KA01_3 = N15_M01_F10_KA01_3.data['N15_M01_F10_KA01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_4')
    N15_M01_F10_KA01_4 = N15_M01_F10_KA01_4.data['N15_M01_F10_KA01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_5')
    N15_M01_F10_KA01_5 = N15_M01_F10_KA01_5.data['N15_M01_F10_KA01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_6')
    N15_M01_F10_KA01_6 = N15_M01_F10_KA01_6.data['N15_M01_F10_KA01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_7')
    N15_M01_F10_KA01_7 = N15_M01_F10_KA01_7.data['N15_M01_F10_KA01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_8')
    N15_M01_F10_KA01_8 = N15_M01_F10_KA01_8.data['N15_M01_F10_KA01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_9')
    N15_M01_F10_KA01_9 = N15_M01_F10_KA01_9.data['N15_M01_F10_KA01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_10')
    N15_M01_F10_KA01_10 = N15_M01_F10_KA01_10.data['N15_M01_F10_KA01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_11')
    N15_M01_F10_KA01_11 = N15_M01_F10_KA01_11.data['N15_M01_F10_KA01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_12')
    N15_M01_F10_KA01_12 = N15_M01_F10_KA01_12.data['N15_M01_F10_KA01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_13')
    N15_M01_F10_KA01_13 = N15_M01_F10_KA01_13.data['N15_M01_F10_KA01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_14')
    N15_M01_F10_KA01_14 = N15_M01_F10_KA01_14.data['N15_M01_F10_KA01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_15')
    N15_M01_F10_KA01_15 = N15_M01_F10_KA01_15.data['N15_M01_F10_KA01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_16')
    N15_M01_F10_KA01_16 = N15_M01_F10_KA01_16.data['N15_M01_F10_KA01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_17')
    N15_M01_F10_KA01_17 = N15_M01_F10_KA01_17.data['N15_M01_F10_KA01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_18')
    N15_M01_F10_KA01_18 = N15_M01_F10_KA01_18.data['N15_M01_F10_KA01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_19')
    N15_M01_F10_KA01_19 = N15_M01_F10_KA01_19.data['N15_M01_F10_KA01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M01_F10_KA01_20')
    N15_M01_F10_KA01_20 = N15_M01_F10_KA01_20.data['N15_M01_F10_KA01_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M01_F10_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_1')
    N15_M01_F10_KI01_1 = N15_M01_F10_KI01_1.data['N15_M01_F10_KI01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_2')
    N15_M01_F10_KI01_2 = N15_M01_F10_KI01_2.data['N15_M01_F10_KI01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_3')
    N15_M01_F10_KI01_3 = N15_M01_F10_KI01_3.data['N15_M01_F10_KI01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_4')
    N15_M01_F10_KI01_4 = N15_M01_F10_KI01_4.data['N15_M01_F10_KI01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_5')
    N15_M01_F10_KI01_5 = N15_M01_F10_KI01_5.data['N15_M01_F10_KI01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_6')
    N15_M01_F10_KI01_6 = N15_M01_F10_KI01_6.data['N15_M01_F10_KI01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_7')
    N15_M01_F10_KI01_7 = N15_M01_F10_KI01_7.data['N15_M01_F10_KI01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_8')
    N15_M01_F10_KI01_8 = N15_M01_F10_KI01_8.data['N15_M01_F10_KI01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_9')
    N15_M01_F10_KI01_9 = N15_M01_F10_KI01_9.data['N15_M01_F10_KI01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_10')
    N15_M01_F10_KI01_10 = N15_M01_F10_KI01_10.data['N15_M01_F10_KI01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_11')
    N15_M01_F10_KI01_11 = N15_M01_F10_KI01_11.data['N15_M01_F10_KI01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_12')
    N15_M01_F10_KI01_12 = N15_M01_F10_KI01_12.data['N15_M01_F10_KI01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_13')
    N15_M01_F10_KI01_13 = N15_M01_F10_KI01_13.data['N15_M01_F10_KI01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_14')
    N15_M01_F10_KI01_14 = N15_M01_F10_KI01_14.data['N15_M01_F10_KI01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_15')
    N15_M01_F10_KI01_15 = N15_M01_F10_KI01_15.data['N15_M01_F10_KI01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_16')
    N15_M01_F10_KI01_16 = N15_M01_F10_KI01_16.data['N15_M01_F10_KI01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_17')
    N15_M01_F10_KI01_17 = N15_M01_F10_KI01_17.data['N15_M01_F10_KI01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_18')
    N15_M01_F10_KI01_18 = N15_M01_F10_KI01_18.data['N15_M01_F10_KI01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_19')
    N15_M01_F10_KI01_19 = N15_M01_F10_KI01_19.data['N15_M01_F10_KI01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M01_F10_KI01_20')
    N15_M01_F10_KI01_20 = N15_M01_F10_KI01_20.data['N15_M01_F10_KI01_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M01_F10_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_1')
    N15_M01_F10_KB24_1 = N15_M01_F10_KB24_1.data['N15_M01_F10_KB24_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_2')
    N15_M01_F10_KB24_2 = N15_M01_F10_KB24_2.data['N15_M01_F10_KB24_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_3')
    N15_M01_F10_KB24_3 = N15_M01_F10_KB24_3.data['N15_M01_F10_KB24_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_4')
    N15_M01_F10_KB24_4 = N15_M01_F10_KB24_4.data['N15_M01_F10_KB24_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_5')
    N15_M01_F10_KB24_5 = N15_M01_F10_KB24_5.data['N15_M01_F10_KB24_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_6')
    N15_M01_F10_KB24_6 = N15_M01_F10_KB24_6.data['N15_M01_F10_KB24_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_7')
    N15_M01_F10_KB24_7 = N15_M01_F10_KB24_7.data['N15_M01_F10_KB24_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_8')
    N15_M01_F10_KB24_8 = N15_M01_F10_KB24_8.data['N15_M01_F10_KB24_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_9')
    N15_M01_F10_KB24_9 = N15_M01_F10_KB24_9.data['N15_M01_F10_KB24_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_10')
    N15_M01_F10_KB24_10 = N15_M01_F10_KB24_10.data['N15_M01_F10_KB24_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_11')
    N15_M01_F10_KB24_11 = N15_M01_F10_KB24_11.data['N15_M01_F10_KB24_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_12')
    N15_M01_F10_KB24_12 = N15_M01_F10_KB24_12.data['N15_M01_F10_KB24_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_13')
    N15_M01_F10_KB24_13 = N15_M01_F10_KB24_13.data['N15_M01_F10_KB24_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_14')
    N15_M01_F10_KB24_14 = N15_M01_F10_KB24_14.data['N15_M01_F10_KB24_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_15')
    N15_M01_F10_KB24_15 = N15_M01_F10_KB24_15.data['N15_M01_F10_KB24_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_16')
    N15_M01_F10_KB24_16 = N15_M01_F10_KB24_16.data['N15_M01_F10_KB24_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_17')
    N15_M01_F10_KB24_17 = N15_M01_F10_KB24_17.data['N15_M01_F10_KB24_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_18')
    N15_M01_F10_KB24_18 = N15_M01_F10_KB24_18.data['N15_M01_F10_KB24_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_19')
    N15_M01_F10_KB24_19 = N15_M01_F10_KB24_19.data['N15_M01_F10_KB24_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M01_F10_KB24_20')
    N15_M01_F10_KB24_20 = N15_M01_F10_KB24_20.data['N15_M01_F10_KB24_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M01_F10_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_1')
    N15_M01_F10_KB27_1 = N15_M01_F10_KB27_1.data['N15_M01_F10_KB27_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_2')
    N15_M01_F10_KB27_2 = N15_M01_F10_KB27_2.data['N15_M01_F10_KB27_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_3')
    N15_M01_F10_KB27_3 = N15_M01_F10_KB27_3.data['N15_M01_F10_KB27_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_4')
    N15_M01_F10_KB27_4 = N15_M01_F10_KB27_4.data['N15_M01_F10_KB27_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_5')
    N15_M01_F10_KB27_5 = N15_M01_F10_KB27_5.data['N15_M01_F10_KB27_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_6')
    N15_M01_F10_KB27_6 = N15_M01_F10_KB27_6.data['N15_M01_F10_KB27_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_7')
    N15_M01_F10_KB27_7 = N15_M01_F10_KB27_7.data['N15_M01_F10_KB27_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_8')
    N15_M01_F10_KB27_8 = N15_M01_F10_KB27_8.data['N15_M01_F10_KB27_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_9')
    N15_M01_F10_KB27_9 = N15_M01_F10_KB27_9.data['N15_M01_F10_KB27_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_10')
    N15_M01_F10_KB27_10 = N15_M01_F10_KB27_10.data['N15_M01_F10_KB27_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_11')
    N15_M01_F10_KB27_11 = N15_M01_F10_KB27_11.data['N15_M01_F10_KB27_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_12')
    N15_M01_F10_KB27_12 = N15_M01_F10_KB27_12.data['N15_M01_F10_KB27_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_13')
    N15_M01_F10_KB27_13 = N15_M01_F10_KB27_13.data['N15_M01_F10_KB27_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_14')
    N15_M01_F10_KB27_14 = N15_M01_F10_KB27_14.data['N15_M01_F10_KB27_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_15')
    N15_M01_F10_KB27_15 = N15_M01_F10_KB27_15.data['N15_M01_F10_KB27_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_16')
    N15_M01_F10_KB27_16 = N15_M01_F10_KB27_16.data['N15_M01_F10_KB27_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_17')
    N15_M01_F10_KB27_17 = N15_M01_F10_KB27_17.data['N15_M01_F10_KB27_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_18')
    N15_M01_F10_KB27_18 = N15_M01_F10_KB27_18.data['N15_M01_F10_KB27_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_19')
    N15_M01_F10_KB27_19 = N15_M01_F10_KB27_19.data['N15_M01_F10_KB27_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M01_F10_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M01_F10_KB27_20')
    N15_M01_F10_KB27_20 = N15_M01_F10_KB27_20.data['N15_M01_F10_KB27_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    合并N15_M01_F10数据
    '''
    '''
    NORMAL
    '''
    N15_M01_F10 = np.append(N15_M01_F10_K001_1, N15_M01_F10_K001_2)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_3)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_4)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_5)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_6)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_7)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_8)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_9)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_10)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_11)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_12)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_13)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_14)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_15)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_16)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_17)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_18)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_19)
    N15_M01_F10 = np.append(N15_M01_F10, N15_M01_F10_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M01_F10_Outer = np.append(N15_M01_F10_KA01_1, N15_M01_F10_KA01_2)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_3)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_4)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_5)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_6)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_7)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_8)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_9)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_10)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_11)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_12)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_13)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_14)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_15)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_16)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_17)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_18)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_19)
    N15_M01_F10_Outer = np.append(N15_M01_F10_Outer, N15_M01_F10_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M01_F10_Inner = np.append(N15_M01_F10_KI01_1, N15_M01_F10_KI01_2)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_3)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_4)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_5)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_6)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_7)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_8)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_9)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_10)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_11)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_12)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_13)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_14)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_15)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_16)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_17)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_18)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_19)
    N15_M01_F10_Inner = np.append(N15_M01_F10_Inner, N15_M01_F10_KI01_20)

    '''
    IR+OR
    '''
    N15_M01_F10_IROR = np.append(N15_M01_F10_KB24_1, N15_M01_F10_KB24_2)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_3)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_4)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_5)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_6)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_7)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_8)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_9)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_10)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_11)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_12)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_13)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_14)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_15)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_16)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_17)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_18)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_19)
    N15_M01_F10_IROR = np.append(N15_M01_F10_IROR, N15_M01_F10_KB24_20)
    '''
    OR+IR
    '''
    N15_M01_F10_ORIR = np.append(N15_M01_F10_KB27_1, N15_M01_F10_KB27_2)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_3)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_4)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_5)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_6)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_7)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_8)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_9)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_10)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_11)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_12)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_13)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_14)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_15)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_16)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_17)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_18)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_19)
    N15_M01_F10_ORIR = np.append(N15_M01_F10_ORIR, N15_M01_F10_KB27_20)

    N15_M01_F10_ALL.append(N15_M01_F10)
    N15_M01_F10_ALL.append(N15_M01_F10_Outer)
    N15_M01_F10_ALL.append(N15_M01_F10_Inner)
    N15_M01_F10_ALL.append(N15_M01_F10_IROR)
    N15_M01_F10_ALL.append(N15_M01_F10_ORIR)

    return N15_M01_F10_ALL
def load_N15_M07_F04_phase_current1_data():
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
    N15_M07_F04_K001_1 = N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][1][2][0].flatten()
    # N15_M07_F04_K001_MCS_1 = N15_M07_F04_K001_1.data[]

    N15_M07_F04_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_2')
    N15_M07_F04_K001_2 = N15_M07_F04_K001_2.data['N15_M07_F04_K001_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_3')
    N15_M07_F04_K001_3 = N15_M07_F04_K001_3.data['N15_M07_F04_K001_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_4')
    N15_M07_F04_K001_4 = N15_M07_F04_K001_4.data['N15_M07_F04_K001_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_5')
    N15_M07_F04_K001_5 = N15_M07_F04_K001_5.data['N15_M07_F04_K001_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_6')
    N15_M07_F04_K001_6 = N15_M07_F04_K001_6.data['N15_M07_F04_K001_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_7')
    N15_M07_F04_K001_7 = N15_M07_F04_K001_7.data['N15_M07_F04_K001_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_8')
    N15_M07_F04_K001_8 = N15_M07_F04_K001_8.data['N15_M07_F04_K001_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_9')
    N15_M07_F04_K001_9 = N15_M07_F04_K001_9.data['N15_M07_F04_K001_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_10')
    N15_M07_F04_K001_10 = N15_M07_F04_K001_10.data['N15_M07_F04_K001_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_11')
    N15_M07_F04_K001_11 = N15_M07_F04_K001_11.data['N15_M07_F04_K001_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_12')
    N15_M07_F04_K001_12 = N15_M07_F04_K001_12.data['N15_M07_F04_K001_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_13')
    N15_M07_F04_K001_13 = N15_M07_F04_K001_13.data['N15_M07_F04_K001_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_14')
    N15_M07_F04_K001_14 = N15_M07_F04_K001_14.data['N15_M07_F04_K001_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_15')
    N15_M07_F04_K001_15 = N15_M07_F04_K001_15.data['N15_M07_F04_K001_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_16')
    N15_M07_F04_K001_16 = N15_M07_F04_K001_16.data['N15_M07_F04_K001_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_17')
    N15_M07_F04_K001_17 = N15_M07_F04_K001_17.data['N15_M07_F04_K001_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_18')
    N15_M07_F04_K001_18 = N15_M07_F04_K001_18.data['N15_M07_F04_K001_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_19')
    N15_M07_F04_K001_19 = N15_M07_F04_K001_19.data['N15_M07_F04_K001_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_20')
    N15_M07_F04_K001_20 = N15_M07_F04_K001_20.data['N15_M07_F04_K001_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F04_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_1')
    N15_M07_F04_KA01_1 = N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_2')
    N15_M07_F04_KA01_2 = N15_M07_F04_KA01_2.data['N15_M07_F04_KA01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_3')
    N15_M07_F04_KA01_3 = N15_M07_F04_KA01_3.data['N15_M07_F04_KA01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_4')
    N15_M07_F04_KA01_4 = N15_M07_F04_KA01_4.data['N15_M07_F04_KA01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_5')
    N15_M07_F04_KA01_5 = N15_M07_F04_KA01_5.data['N15_M07_F04_KA01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_6')
    N15_M07_F04_KA01_6 = N15_M07_F04_KA01_6.data['N15_M07_F04_KA01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_7')
    N15_M07_F04_KA01_7 = N15_M07_F04_KA01_7.data['N15_M07_F04_KA01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_8')
    N15_M07_F04_KA01_8 = N15_M07_F04_KA01_8.data['N15_M07_F04_KA01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_9')
    N15_M07_F04_KA01_9 = N15_M07_F04_KA01_9.data['N15_M07_F04_KA01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_10')
    N15_M07_F04_KA01_10 = N15_M07_F04_KA01_10.data['N15_M07_F04_KA01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_11')
    N15_M07_F04_KA01_11 = N15_M07_F04_KA01_11.data['N15_M07_F04_KA01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_12')
    N15_M07_F04_KA01_12 = N15_M07_F04_KA01_12.data['N15_M07_F04_KA01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_13')
    N15_M07_F04_KA01_13 = N15_M07_F04_KA01_13.data['N15_M07_F04_KA01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_14')
    N15_M07_F04_KA01_14 = N15_M07_F04_KA01_14.data['N15_M07_F04_KA01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_15')
    N15_M07_F04_KA01_15 = N15_M07_F04_KA01_15.data['N15_M07_F04_KA01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_16')
    N15_M07_F04_KA01_16 = N15_M07_F04_KA01_16.data['N15_M07_F04_KA01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_17')
    N15_M07_F04_KA01_17 = N15_M07_F04_KA01_17.data['N15_M07_F04_KA01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_18')
    N15_M07_F04_KA01_18 = N15_M07_F04_KA01_18.data['N15_M07_F04_KA01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_19')
    N15_M07_F04_KA01_19 = N15_M07_F04_KA01_19.data['N15_M07_F04_KA01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_20')
    N15_M07_F04_KA01_20 = N15_M07_F04_KA01_20.data['N15_M07_F04_KA01_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F04_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_1')
    N15_M07_F04_KI01_1 = N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_2')
    N15_M07_F04_KI01_2 = N15_M07_F04_KI01_2.data['N15_M07_F04_KI01_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_3')
    N15_M07_F04_KI01_3 = N15_M07_F04_KI01_3.data['N15_M07_F04_KI01_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_4')
    N15_M07_F04_KI01_4 = N15_M07_F04_KI01_4.data['N15_M07_F04_KI01_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_5')
    N15_M07_F04_KI01_5 = N15_M07_F04_KI01_5.data['N15_M07_F04_KI01_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_6')
    N15_M07_F04_KI01_6 = N15_M07_F04_KI01_6.data['N15_M07_F04_KI01_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_7')
    N15_M07_F04_KI01_7 = N15_M07_F04_KI01_7.data['N15_M07_F04_KI01_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_8')
    N15_M07_F04_KI01_8 = N15_M07_F04_KI01_8.data['N15_M07_F04_KI01_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_9')
    N15_M07_F04_KI01_9 = N15_M07_F04_KI01_9.data['N15_M07_F04_KI01_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_10')
    N15_M07_F04_KI01_10 = N15_M07_F04_KI01_10.data['N15_M07_F04_KI01_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_11')
    N15_M07_F04_KI01_11 = N15_M07_F04_KI01_11.data['N15_M07_F04_KI01_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_12')
    N15_M07_F04_KI01_12 = N15_M07_F04_KI01_12.data['N15_M07_F04_KI01_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_13')
    N15_M07_F04_KI01_13 = N15_M07_F04_KI01_13.data['N15_M07_F04_KI01_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_14')
    N15_M07_F04_KI01_14 = N15_M07_F04_KI01_14.data['N15_M07_F04_KI01_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_15')
    N15_M07_F04_KI01_15 = N15_M07_F04_KI01_15.data['N15_M07_F04_KI01_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_16')
    N15_M07_F04_KI01_16 = N15_M07_F04_KI01_16.data['N15_M07_F04_KI01_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_17')
    N15_M07_F04_KI01_17 = N15_M07_F04_KI01_17.data['N15_M07_F04_KI01_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_18')
    N15_M07_F04_KI01_18 = N15_M07_F04_KI01_18.data['N15_M07_F04_KI01_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_19')
    N15_M07_F04_KI01_19 = N15_M07_F04_KI01_19.data['N15_M07_F04_KI01_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_20')
    N15_M07_F04_KI01_20 = N15_M07_F04_KI01_20.data['N15_M07_F04_KI01_20']['Y'][0][0][0][1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F04_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_1')
    N15_M07_F04_KB24_1 = N15_M07_F04_KB24_1.data['N15_M07_F04_KB24_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_2')
    N15_M07_F04_KB24_2 = N15_M07_F04_KB24_2.data['N15_M07_F04_KB24_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_3')
    N15_M07_F04_KB24_3 = N15_M07_F04_KB24_3.data['N15_M07_F04_KB24_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_4')
    N15_M07_F04_KB24_4 = N15_M07_F04_KB24_4.data['N15_M07_F04_KB24_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_5')
    N15_M07_F04_KB24_5 = N15_M07_F04_KB24_5.data['N15_M07_F04_KB24_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_6')
    N15_M07_F04_KB24_6 = N15_M07_F04_KB24_6.data['N15_M07_F04_KB24_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_7')
    N15_M07_F04_KB24_7 = N15_M07_F04_KB24_7.data['N15_M07_F04_KB24_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_8')
    N15_M07_F04_KB24_8 = N15_M07_F04_KB24_8.data['N15_M07_F04_KB24_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_9')
    N15_M07_F04_KB24_9 = N15_M07_F04_KB24_9.data['N15_M07_F04_KB24_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_10')
    N15_M07_F04_KB24_10 = N15_M07_F04_KB24_10.data['N15_M07_F04_KB24_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_11')
    N15_M07_F04_KB24_11 = N15_M07_F04_KB24_11.data['N15_M07_F04_KB24_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_12')
    N15_M07_F04_KB24_12 = N15_M07_F04_KB24_12.data['N15_M07_F04_KB24_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_13')
    N15_M07_F04_KB24_13 = N15_M07_F04_KB24_13.data['N15_M07_F04_KB24_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_14')
    N15_M07_F04_KB24_14 = N15_M07_F04_KB24_14.data['N15_M07_F04_KB24_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_15')
    N15_M07_F04_KB24_15 = N15_M07_F04_KB24_15.data['N15_M07_F04_KB24_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_16')
    N15_M07_F04_KB24_16 = N15_M07_F04_KB24_16.data['N15_M07_F04_KB24_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_17')
    N15_M07_F04_KB24_17 = N15_M07_F04_KB24_17.data['N15_M07_F04_KB24_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_18')
    N15_M07_F04_KB24_18 = N15_M07_F04_KB24_18.data['N15_M07_F04_KB24_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_19')
    N15_M07_F04_KB24_19 = N15_M07_F04_KB24_19.data['N15_M07_F04_KB24_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_20')
    N15_M07_F04_KB24_20 = N15_M07_F04_KB24_20.data['N15_M07_F04_KB24_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F04_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_1')
    N15_M07_F04_KB27_1 = N15_M07_F04_KB27_1.data['N15_M07_F04_KB27_1']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_2')
    N15_M07_F04_KB27_2 = N15_M07_F04_KB27_2.data['N15_M07_F04_KB27_2']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_3')
    N15_M07_F04_KB27_3 = N15_M07_F04_KB27_3.data['N15_M07_F04_KB27_3']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_4')
    N15_M07_F04_KB27_4 = N15_M07_F04_KB27_4.data['N15_M07_F04_KB27_4']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_5')
    N15_M07_F04_KB27_5 = N15_M07_F04_KB27_5.data['N15_M07_F04_KB27_5']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_6')
    N15_M07_F04_KB27_6 = N15_M07_F04_KB27_6.data['N15_M07_F04_KB27_6']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_7')
    N15_M07_F04_KB27_7 = N15_M07_F04_KB27_7.data['N15_M07_F04_KB27_7']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_8')
    N15_M07_F04_KB27_8 = N15_M07_F04_KB27_8.data['N15_M07_F04_KB27_8']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_9')
    N15_M07_F04_KB27_9 = N15_M07_F04_KB27_9.data['N15_M07_F04_KB27_9']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_10')
    N15_M07_F04_KB27_10 = N15_M07_F04_KB27_10.data['N15_M07_F04_KB27_10']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_11')
    N15_M07_F04_KB27_11 = N15_M07_F04_KB27_11.data['N15_M07_F04_KB27_11']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_12')
    N15_M07_F04_KB27_12 = N15_M07_F04_KB27_12.data['N15_M07_F04_KB27_12']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_13')
    N15_M07_F04_KB27_13 = N15_M07_F04_KB27_13.data['N15_M07_F04_KB27_13']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_14')
    N15_M07_F04_KB27_14 = N15_M07_F04_KB27_14.data['N15_M07_F04_KB27_14']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_15')
    N15_M07_F04_KB27_15 = N15_M07_F04_KB27_15.data['N15_M07_F04_KB27_15']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_16')
    N15_M07_F04_KB27_16 = N15_M07_F04_KB27_16.data['N15_M07_F04_KB27_16']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_17')
    N15_M07_F04_KB27_17 = N15_M07_F04_KB27_17.data['N15_M07_F04_KB27_17']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_18')
    N15_M07_F04_KB27_18 = N15_M07_F04_KB27_18.data['N15_M07_F04_KB27_18']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_19')
    N15_M07_F04_KB27_19 = N15_M07_F04_KB27_19.data['N15_M07_F04_KB27_19']['Y'][0][0][0][1][2][0].flatten()
    N15_M07_F04_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_20')
    N15_M07_F04_KB27_20 = N15_M07_F04_KB27_20.data['N15_M07_F04_KB27_20']['Y'][0][0][0][1][2][0].flatten()
    '''
    合并N15_M07_F04数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F04 = np.append(N15_M07_F04_K001_1, N15_M07_F04_K001_2)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_3)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_4)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_5)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_6)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_7)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_8)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_9)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_10)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_11)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_12)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_13)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_14)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_15)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_16)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_17)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_18)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_19)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F04_Outer = np.append(N15_M07_F04_KA01_1, N15_M07_F04_KA01_2)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_3)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_4)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_5)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_6)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_7)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_8)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_9)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_10)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_11)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_12)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_13)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_14)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_15)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_16)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_17)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_18)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_19)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F04_Inner = np.append(N15_M07_F04_KI01_1, N15_M07_F04_KI01_2)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_3)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_4)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_5)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_6)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_7)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_8)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_9)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_10)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_11)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_12)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_13)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_14)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_15)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_16)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_17)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_18)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_19)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F04_IROR = np.append(N15_M07_F04_KB24_1, N15_M07_F04_KB24_2)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_3)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_4)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_5)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_6)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_7)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_8)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_9)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_10)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_11)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_12)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_13)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_14)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_15)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_16)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_17)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_18)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_19)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F04_ORIR = np.append(N15_M07_F04_KB27_1, N15_M07_F04_KB27_2)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_3)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_4)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_5)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_6)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_7)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_8)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_9)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_10)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_11)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_12)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_13)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_14)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_15)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_16)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_17)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_18)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_19)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_20)

    N15_M07_F04_ALL.append(N15_M07_F04)
    N15_M07_F04_ALL.append(N15_M07_F04_Outer)
    N15_M07_F04_ALL.append(N15_M07_F04_Inner)
    N15_M07_F04_ALL.append(N15_M07_F04_IROR)
    N15_M07_F04_ALL.append(N15_M07_F04_ORIR)

    return N15_M07_F04_ALL
def load_N15_M07_F04_phase_current2_data():
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
    N15_M07_F04_K001_1 = N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][2][2][0].flatten()
    # N15_M07_F04_K001_MCS_1 = N15_M07_F04_K001_1.data[]

    N15_M07_F04_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_2')
    N15_M07_F04_K001_2 = N15_M07_F04_K001_2.data['N15_M07_F04_K001_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_3')
    N15_M07_F04_K001_3 = N15_M07_F04_K001_3.data['N15_M07_F04_K001_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_4')
    N15_M07_F04_K001_4 = N15_M07_F04_K001_4.data['N15_M07_F04_K001_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_5')
    N15_M07_F04_K001_5 = N15_M07_F04_K001_5.data['N15_M07_F04_K001_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_6')
    N15_M07_F04_K001_6 = N15_M07_F04_K001_6.data['N15_M07_F04_K001_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_7')
    N15_M07_F04_K001_7 = N15_M07_F04_K001_7.data['N15_M07_F04_K001_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_8')
    N15_M07_F04_K001_8 = N15_M07_F04_K001_8.data['N15_M07_F04_K001_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_9')
    N15_M07_F04_K001_9 = N15_M07_F04_K001_9.data['N15_M07_F04_K001_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_10')
    N15_M07_F04_K001_10 = N15_M07_F04_K001_10.data['N15_M07_F04_K001_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_11')
    N15_M07_F04_K001_11 = N15_M07_F04_K001_11.data['N15_M07_F04_K001_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_12')
    N15_M07_F04_K001_12 = N15_M07_F04_K001_12.data['N15_M07_F04_K001_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_13')
    N15_M07_F04_K001_13 = N15_M07_F04_K001_13.data['N15_M07_F04_K001_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_14')
    N15_M07_F04_K001_14 = N15_M07_F04_K001_14.data['N15_M07_F04_K001_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_15')
    N15_M07_F04_K001_15 = N15_M07_F04_K001_15.data['N15_M07_F04_K001_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_16')
    N15_M07_F04_K001_16 = N15_M07_F04_K001_16.data['N15_M07_F04_K001_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_17')
    N15_M07_F04_K001_17 = N15_M07_F04_K001_17.data['N15_M07_F04_K001_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_18')
    N15_M07_F04_K001_18 = N15_M07_F04_K001_18.data['N15_M07_F04_K001_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_19')
    N15_M07_F04_K001_19 = N15_M07_F04_K001_19.data['N15_M07_F04_K001_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_20')
    N15_M07_F04_K001_20 = N15_M07_F04_K001_20.data['N15_M07_F04_K001_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F04_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_1')
    N15_M07_F04_KA01_1 = N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_2')
    N15_M07_F04_KA01_2 = N15_M07_F04_KA01_2.data['N15_M07_F04_KA01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_3')
    N15_M07_F04_KA01_3 = N15_M07_F04_KA01_3.data['N15_M07_F04_KA01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_4')
    N15_M07_F04_KA01_4 = N15_M07_F04_KA01_4.data['N15_M07_F04_KA01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_5')
    N15_M07_F04_KA01_5 = N15_M07_F04_KA01_5.data['N15_M07_F04_KA01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_6')
    N15_M07_F04_KA01_6 = N15_M07_F04_KA01_6.data['N15_M07_F04_KA01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_7')
    N15_M07_F04_KA01_7 = N15_M07_F04_KA01_7.data['N15_M07_F04_KA01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_8')
    N15_M07_F04_KA01_8 = N15_M07_F04_KA01_8.data['N15_M07_F04_KA01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_9')
    N15_M07_F04_KA01_9 = N15_M07_F04_KA01_9.data['N15_M07_F04_KA01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_10')
    N15_M07_F04_KA01_10 = N15_M07_F04_KA01_10.data['N15_M07_F04_KA01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_11')
    N15_M07_F04_KA01_11 = N15_M07_F04_KA01_11.data['N15_M07_F04_KA01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_12')
    N15_M07_F04_KA01_12 = N15_M07_F04_KA01_12.data['N15_M07_F04_KA01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_13')
    N15_M07_F04_KA01_13 = N15_M07_F04_KA01_13.data['N15_M07_F04_KA01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_14')
    N15_M07_F04_KA01_14 = N15_M07_F04_KA01_14.data['N15_M07_F04_KA01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_15')
    N15_M07_F04_KA01_15 = N15_M07_F04_KA01_15.data['N15_M07_F04_KA01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_16')
    N15_M07_F04_KA01_16 = N15_M07_F04_KA01_16.data['N15_M07_F04_KA01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_17')
    N15_M07_F04_KA01_17 = N15_M07_F04_KA01_17.data['N15_M07_F04_KA01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_18')
    N15_M07_F04_KA01_18 = N15_M07_F04_KA01_18.data['N15_M07_F04_KA01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_19')
    N15_M07_F04_KA01_19 = N15_M07_F04_KA01_19.data['N15_M07_F04_KA01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_20')
    N15_M07_F04_KA01_20 = N15_M07_F04_KA01_20.data['N15_M07_F04_KA01_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F04_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_1')
    N15_M07_F04_KI01_1 = N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_2')
    N15_M07_F04_KI01_2 = N15_M07_F04_KI01_2.data['N15_M07_F04_KI01_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_3')
    N15_M07_F04_KI01_3 = N15_M07_F04_KI01_3.data['N15_M07_F04_KI01_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_4')
    N15_M07_F04_KI01_4 = N15_M07_F04_KI01_4.data['N15_M07_F04_KI01_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_5')
    N15_M07_F04_KI01_5 = N15_M07_F04_KI01_5.data['N15_M07_F04_KI01_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_6')
    N15_M07_F04_KI01_6 = N15_M07_F04_KI01_6.data['N15_M07_F04_KI01_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_7')
    N15_M07_F04_KI01_7 = N15_M07_F04_KI01_7.data['N15_M07_F04_KI01_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_8')
    N15_M07_F04_KI01_8 = N15_M07_F04_KI01_8.data['N15_M07_F04_KI01_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_9')
    N15_M07_F04_KI01_9 = N15_M07_F04_KI01_9.data['N15_M07_F04_KI01_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_10')
    N15_M07_F04_KI01_10 = N15_M07_F04_KI01_10.data['N15_M07_F04_KI01_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_11')
    N15_M07_F04_KI01_11 = N15_M07_F04_KI01_11.data['N15_M07_F04_KI01_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_12')
    N15_M07_F04_KI01_12 = N15_M07_F04_KI01_12.data['N15_M07_F04_KI01_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_13')
    N15_M07_F04_KI01_13 = N15_M07_F04_KI01_13.data['N15_M07_F04_KI01_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_14')
    N15_M07_F04_KI01_14 = N15_M07_F04_KI01_14.data['N15_M07_F04_KI01_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_15')
    N15_M07_F04_KI01_15 = N15_M07_F04_KI01_15.data['N15_M07_F04_KI01_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_16')
    N15_M07_F04_KI01_16 = N15_M07_F04_KI01_16.data['N15_M07_F04_KI01_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_17')
    N15_M07_F04_KI01_17 = N15_M07_F04_KI01_17.data['N15_M07_F04_KI01_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_18')
    N15_M07_F04_KI01_18 = N15_M07_F04_KI01_18.data['N15_M07_F04_KI01_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_19')
    N15_M07_F04_KI01_19 = N15_M07_F04_KI01_19.data['N15_M07_F04_KI01_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_20')
    N15_M07_F04_KI01_20 = N15_M07_F04_KI01_20.data['N15_M07_F04_KI01_20']['Y'][0][0][0][2][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F04_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_1')
    N15_M07_F04_KB24_1 = N15_M07_F04_KB24_1.data['N15_M07_F04_KB24_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_2')
    N15_M07_F04_KB24_2 = N15_M07_F04_KB24_2.data['N15_M07_F04_KB24_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_3')
    N15_M07_F04_KB24_3 = N15_M07_F04_KB24_3.data['N15_M07_F04_KB24_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_4')
    N15_M07_F04_KB24_4 = N15_M07_F04_KB24_4.data['N15_M07_F04_KB24_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_5')
    N15_M07_F04_KB24_5 = N15_M07_F04_KB24_5.data['N15_M07_F04_KB24_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_6')
    N15_M07_F04_KB24_6 = N15_M07_F04_KB24_6.data['N15_M07_F04_KB24_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_7')
    N15_M07_F04_KB24_7 = N15_M07_F04_KB24_7.data['N15_M07_F04_KB24_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_8')
    N15_M07_F04_KB24_8 = N15_M07_F04_KB24_8.data['N15_M07_F04_KB24_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_9')
    N15_M07_F04_KB24_9 = N15_M07_F04_KB24_9.data['N15_M07_F04_KB24_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_10')
    N15_M07_F04_KB24_10 = N15_M07_F04_KB24_10.data['N15_M07_F04_KB24_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_11')
    N15_M07_F04_KB24_11 = N15_M07_F04_KB24_11.data['N15_M07_F04_KB24_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_12')
    N15_M07_F04_KB24_12 = N15_M07_F04_KB24_12.data['N15_M07_F04_KB24_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_13')
    N15_M07_F04_KB24_13 = N15_M07_F04_KB24_13.data['N15_M07_F04_KB24_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_14')
    N15_M07_F04_KB24_14 = N15_M07_F04_KB24_14.data['N15_M07_F04_KB24_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_15')
    N15_M07_F04_KB24_15 = N15_M07_F04_KB24_15.data['N15_M07_F04_KB24_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_16')
    N15_M07_F04_KB24_16 = N15_M07_F04_KB24_16.data['N15_M07_F04_KB24_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_17')
    N15_M07_F04_KB24_17 = N15_M07_F04_KB24_17.data['N15_M07_F04_KB24_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_18')
    N15_M07_F04_KB24_18 = N15_M07_F04_KB24_18.data['N15_M07_F04_KB24_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_19')
    N15_M07_F04_KB24_19 = N15_M07_F04_KB24_19.data['N15_M07_F04_KB24_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_20')
    N15_M07_F04_KB24_20 = N15_M07_F04_KB24_20.data['N15_M07_F04_KB24_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F04_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_1')
    N15_M07_F04_KB27_1 = N15_M07_F04_KB27_1.data['N15_M07_F04_KB27_1']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_2')
    N15_M07_F04_KB27_2 = N15_M07_F04_KB27_2.data['N15_M07_F04_KB27_2']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_3')
    N15_M07_F04_KB27_3 = N15_M07_F04_KB27_3.data['N15_M07_F04_KB27_3']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_4')
    N15_M07_F04_KB27_4 = N15_M07_F04_KB27_4.data['N15_M07_F04_KB27_4']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_5')
    N15_M07_F04_KB27_5 = N15_M07_F04_KB27_5.data['N15_M07_F04_KB27_5']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_6')
    N15_M07_F04_KB27_6 = N15_M07_F04_KB27_6.data['N15_M07_F04_KB27_6']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_7')
    N15_M07_F04_KB27_7 = N15_M07_F04_KB27_7.data['N15_M07_F04_KB27_7']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_8')
    N15_M07_F04_KB27_8 = N15_M07_F04_KB27_8.data['N15_M07_F04_KB27_8']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_9')
    N15_M07_F04_KB27_9 = N15_M07_F04_KB27_9.data['N15_M07_F04_KB27_9']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_10')
    N15_M07_F04_KB27_10 = N15_M07_F04_KB27_10.data['N15_M07_F04_KB27_10']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_11')
    N15_M07_F04_KB27_11 = N15_M07_F04_KB27_11.data['N15_M07_F04_KB27_11']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_12')
    N15_M07_F04_KB27_12 = N15_M07_F04_KB27_12.data['N15_M07_F04_KB27_12']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_13')
    N15_M07_F04_KB27_13 = N15_M07_F04_KB27_13.data['N15_M07_F04_KB27_13']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_14')
    N15_M07_F04_KB27_14 = N15_M07_F04_KB27_14.data['N15_M07_F04_KB27_14']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_15')
    N15_M07_F04_KB27_15 = N15_M07_F04_KB27_15.data['N15_M07_F04_KB27_15']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_16')
    N15_M07_F04_KB27_16 = N15_M07_F04_KB27_16.data['N15_M07_F04_KB27_16']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_17')
    N15_M07_F04_KB27_17 = N15_M07_F04_KB27_17.data['N15_M07_F04_KB27_17']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_18')
    N15_M07_F04_KB27_18 = N15_M07_F04_KB27_18.data['N15_M07_F04_KB27_18']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_19')
    N15_M07_F04_KB27_19 = N15_M07_F04_KB27_19.data['N15_M07_F04_KB27_19']['Y'][0][0][0][2][2][0].flatten()
    N15_M07_F04_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_20')
    N15_M07_F04_KB27_20 = N15_M07_F04_KB27_20.data['N15_M07_F04_KB27_20']['Y'][0][0][0][2][2][0].flatten()
    '''
    合并N15_M07_F04数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F04 = np.append(N15_M07_F04_K001_1, N15_M07_F04_K001_2)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_3)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_4)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_5)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_6)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_7)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_8)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_9)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_10)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_11)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_12)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_13)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_14)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_15)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_16)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_17)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_18)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_19)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F04_Outer = np.append(N15_M07_F04_KA01_1, N15_M07_F04_KA01_2)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_3)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_4)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_5)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_6)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_7)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_8)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_9)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_10)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_11)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_12)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_13)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_14)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_15)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_16)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_17)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_18)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_19)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F04_Inner = np.append(N15_M07_F04_KI01_1, N15_M07_F04_KI01_2)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_3)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_4)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_5)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_6)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_7)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_8)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_9)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_10)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_11)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_12)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_13)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_14)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_15)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_16)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_17)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_18)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_19)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F04_IROR = np.append(N15_M07_F04_KB24_1, N15_M07_F04_KB24_2)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_3)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_4)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_5)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_6)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_7)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_8)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_9)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_10)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_11)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_12)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_13)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_14)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_15)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_16)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_17)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_18)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_19)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F04_ORIR = np.append(N15_M07_F04_KB27_1, N15_M07_F04_KB27_2)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_3)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_4)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_5)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_6)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_7)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_8)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_9)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_10)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_11)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_12)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_13)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_14)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_15)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_16)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_17)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_18)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_19)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_20)

    N15_M07_F04_ALL.append(N15_M07_F04)
    N15_M07_F04_ALL.append(N15_M07_F04_Outer)
    N15_M07_F04_ALL.append(N15_M07_F04_Inner)
    N15_M07_F04_ALL.append(N15_M07_F04_IROR)
    N15_M07_F04_ALL.append(N15_M07_F04_ORIR)

    return N15_M07_F04_ALL
def load_N15_M07_F04_Vibration_data():
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
    N15_M07_F04_K001_1 = N15_M07_F04_K001_1.data['N15_M07_F04_K001_1']['Y'][0][0][0][-1][2][0].flatten()
    # N15_M07_F04_K001_MCS_1 = N15_M07_F04_K001_1.data[]

    N15_M07_F04_K001_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_2')
    N15_M07_F04_K001_2 = N15_M07_F04_K001_2.data['N15_M07_F04_K001_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_3')
    N15_M07_F04_K001_3 = N15_M07_F04_K001_3.data['N15_M07_F04_K001_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_4')
    N15_M07_F04_K001_4 = N15_M07_F04_K001_4.data['N15_M07_F04_K001_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_5')
    N15_M07_F04_K001_5 = N15_M07_F04_K001_5.data['N15_M07_F04_K001_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_6')
    N15_M07_F04_K001_6 = N15_M07_F04_K001_6.data['N15_M07_F04_K001_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_7')
    N15_M07_F04_K001_7 = N15_M07_F04_K001_7.data['N15_M07_F04_K001_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_8')
    N15_M07_F04_K001_8 = N15_M07_F04_K001_8.data['N15_M07_F04_K001_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_9')
    N15_M07_F04_K001_9 = N15_M07_F04_K001_9.data['N15_M07_F04_K001_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_10')
    N15_M07_F04_K001_10 = N15_M07_F04_K001_10.data['N15_M07_F04_K001_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_11')
    N15_M07_F04_K001_11 = N15_M07_F04_K001_11.data['N15_M07_F04_K001_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_12')
    N15_M07_F04_K001_12 = N15_M07_F04_K001_12.data['N15_M07_F04_K001_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_13')
    N15_M07_F04_K001_13 = N15_M07_F04_K001_13.data['N15_M07_F04_K001_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_14')
    N15_M07_F04_K001_14 = N15_M07_F04_K001_14.data['N15_M07_F04_K001_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_15')
    N15_M07_F04_K001_15 = N15_M07_F04_K001_15.data['N15_M07_F04_K001_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_16')
    N15_M07_F04_K001_16 = N15_M07_F04_K001_16.data['N15_M07_F04_K001_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_17')
    N15_M07_F04_K001_17 = N15_M07_F04_K001_17.data['N15_M07_F04_K001_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_18')
    N15_M07_F04_K001_18 = N15_M07_F04_K001_18.data['N15_M07_F04_K001_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_19')
    N15_M07_F04_K001_19 = N15_M07_F04_K001_19.data['N15_M07_F04_K001_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_K001_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/normal/K001/N15_M07_F04_K001_20')
    N15_M07_F04_K001_20 = N15_M07_F04_K001_20.data['N15_M07_F04_K001_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    2.Outer Fault
    '''
    # KA01
    N15_M07_F04_KA01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_1')
    N15_M07_F04_KA01_1 = N15_M07_F04_KA01_1.data['N15_M07_F04_KA01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_2')
    N15_M07_F04_KA01_2 = N15_M07_F04_KA01_2.data['N15_M07_F04_KA01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_3')
    N15_M07_F04_KA01_3 = N15_M07_F04_KA01_3.data['N15_M07_F04_KA01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_4')
    N15_M07_F04_KA01_4 = N15_M07_F04_KA01_4.data['N15_M07_F04_KA01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_5')
    N15_M07_F04_KA01_5 = N15_M07_F04_KA01_5.data['N15_M07_F04_KA01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_6')
    N15_M07_F04_KA01_6 = N15_M07_F04_KA01_6.data['N15_M07_F04_KA01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_7')
    N15_M07_F04_KA01_7 = N15_M07_F04_KA01_7.data['N15_M07_F04_KA01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_8')
    N15_M07_F04_KA01_8 = N15_M07_F04_KA01_8.data['N15_M07_F04_KA01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_9')
    N15_M07_F04_KA01_9 = N15_M07_F04_KA01_9.data['N15_M07_F04_KA01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_10')
    N15_M07_F04_KA01_10 = N15_M07_F04_KA01_10.data['N15_M07_F04_KA01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_11')
    N15_M07_F04_KA01_11 = N15_M07_F04_KA01_11.data['N15_M07_F04_KA01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_12')
    N15_M07_F04_KA01_12 = N15_M07_F04_KA01_12.data['N15_M07_F04_KA01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_13')
    N15_M07_F04_KA01_13 = N15_M07_F04_KA01_13.data['N15_M07_F04_KA01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_14')
    N15_M07_F04_KA01_14 = N15_M07_F04_KA01_14.data['N15_M07_F04_KA01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_15')
    N15_M07_F04_KA01_15 = N15_M07_F04_KA01_15.data['N15_M07_F04_KA01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_16')
    N15_M07_F04_KA01_16 = N15_M07_F04_KA01_16.data['N15_M07_F04_KA01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_17')
    N15_M07_F04_KA01_17 = N15_M07_F04_KA01_17.data['N15_M07_F04_KA01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_18')
    N15_M07_F04_KA01_18 = N15_M07_F04_KA01_18.data['N15_M07_F04_KA01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_19')
    N15_M07_F04_KA01_19 = N15_M07_F04_KA01_19.data['N15_M07_F04_KA01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KA01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KA01/N15_M07_F04_KA01_20')
    N15_M07_F04_KA01_20 = N15_M07_F04_KA01_20.data['N15_M07_F04_KA01_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    InnerRaceFault
    '''
    # KI01
    N15_M07_F04_KI01_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_1')
    N15_M07_F04_KI01_1 = N15_M07_F04_KI01_1.data['N15_M07_F04_KI01_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_2')
    N15_M07_F04_KI01_2 = N15_M07_F04_KI01_2.data['N15_M07_F04_KI01_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_3')
    N15_M07_F04_KI01_3 = N15_M07_F04_KI01_3.data['N15_M07_F04_KI01_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_4')
    N15_M07_F04_KI01_4 = N15_M07_F04_KI01_4.data['N15_M07_F04_KI01_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_5')
    N15_M07_F04_KI01_5 = N15_M07_F04_KI01_5.data['N15_M07_F04_KI01_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_6')
    N15_M07_F04_KI01_6 = N15_M07_F04_KI01_6.data['N15_M07_F04_KI01_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_7')
    N15_M07_F04_KI01_7 = N15_M07_F04_KI01_7.data['N15_M07_F04_KI01_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_8')
    N15_M07_F04_KI01_8 = N15_M07_F04_KI01_8.data['N15_M07_F04_KI01_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_9')
    N15_M07_F04_KI01_9 = N15_M07_F04_KI01_9.data['N15_M07_F04_KI01_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_10')
    N15_M07_F04_KI01_10 = N15_M07_F04_KI01_10.data['N15_M07_F04_KI01_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_11')
    N15_M07_F04_KI01_11 = N15_M07_F04_KI01_11.data['N15_M07_F04_KI01_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_12')
    N15_M07_F04_KI01_12 = N15_M07_F04_KI01_12.data['N15_M07_F04_KI01_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_13')
    N15_M07_F04_KI01_13 = N15_M07_F04_KI01_13.data['N15_M07_F04_KI01_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_14')
    N15_M07_F04_KI01_14 = N15_M07_F04_KI01_14.data['N15_M07_F04_KI01_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_15')
    N15_M07_F04_KI01_15 = N15_M07_F04_KI01_15.data['N15_M07_F04_KI01_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_16')
    N15_M07_F04_KI01_16 = N15_M07_F04_KI01_16.data['N15_M07_F04_KI01_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_17')
    N15_M07_F04_KI01_17 = N15_M07_F04_KI01_17.data['N15_M07_F04_KI01_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_18')
    N15_M07_F04_KI01_18 = N15_M07_F04_KI01_18.data['N15_M07_F04_KI01_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_19')
    N15_M07_F04_KI01_19 = N15_M07_F04_KI01_19.data['N15_M07_F04_KI01_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KI01_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KI01/N15_M07_F04_KI01_20')
    N15_M07_F04_KI01_20 = N15_M07_F04_KI01_20.data['N15_M07_F04_KI01_20']['Y'][0][0][0][-1][2][0].flatten()

    '''
    IR+OR Fault
    '''
    # KB24
    N15_M07_F04_KB24_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_1')
    N15_M07_F04_KB24_1 = N15_M07_F04_KB24_1.data['N15_M07_F04_KB24_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_2')
    N15_M07_F04_KB24_2 = N15_M07_F04_KB24_2.data['N15_M07_F04_KB24_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_3')
    N15_M07_F04_KB24_3 = N15_M07_F04_KB24_3.data['N15_M07_F04_KB24_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_4')
    N15_M07_F04_KB24_4 = N15_M07_F04_KB24_4.data['N15_M07_F04_KB24_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_5')
    N15_M07_F04_KB24_5 = N15_M07_F04_KB24_5.data['N15_M07_F04_KB24_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_6')
    N15_M07_F04_KB24_6 = N15_M07_F04_KB24_6.data['N15_M07_F04_KB24_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_7')
    N15_M07_F04_KB24_7 = N15_M07_F04_KB24_7.data['N15_M07_F04_KB24_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_8')
    N15_M07_F04_KB24_8 = N15_M07_F04_KB24_8.data['N15_M07_F04_KB24_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_9')
    N15_M07_F04_KB24_9 = N15_M07_F04_KB24_9.data['N15_M07_F04_KB24_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_10')
    N15_M07_F04_KB24_10 = N15_M07_F04_KB24_10.data['N15_M07_F04_KB24_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_11')
    N15_M07_F04_KB24_11 = N15_M07_F04_KB24_11.data['N15_M07_F04_KB24_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_12')
    N15_M07_F04_KB24_12 = N15_M07_F04_KB24_12.data['N15_M07_F04_KB24_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_13')
    N15_M07_F04_KB24_13 = N15_M07_F04_KB24_13.data['N15_M07_F04_KB24_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_14')
    N15_M07_F04_KB24_14 = N15_M07_F04_KB24_14.data['N15_M07_F04_KB24_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_15')
    N15_M07_F04_KB24_15 = N15_M07_F04_KB24_15.data['N15_M07_F04_KB24_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_16')
    N15_M07_F04_KB24_16 = N15_M07_F04_KB24_16.data['N15_M07_F04_KB24_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_17')
    N15_M07_F04_KB24_17 = N15_M07_F04_KB24_17.data['N15_M07_F04_KB24_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_18')
    N15_M07_F04_KB24_18 = N15_M07_F04_KB24_18.data['N15_M07_F04_KB24_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_19')
    N15_M07_F04_KB24_19 = N15_M07_F04_KB24_19.data['N15_M07_F04_KB24_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB24_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB24/N15_M07_F04_KB24_20')
    N15_M07_F04_KB24_20 = N15_M07_F04_KB24_20.data['N15_M07_F04_KB24_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    OR+IR Fault
    '''
    # KB27
    N15_M07_F04_KB27_1 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_1')
    N15_M07_F04_KB27_1 = N15_M07_F04_KB27_1.data['N15_M07_F04_KB27_1']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_2 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_2')
    N15_M07_F04_KB27_2 = N15_M07_F04_KB27_2.data['N15_M07_F04_KB27_2']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_3 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_3')
    N15_M07_F04_KB27_3 = N15_M07_F04_KB27_3.data['N15_M07_F04_KB27_3']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_4 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_4')
    N15_M07_F04_KB27_4 = N15_M07_F04_KB27_4.data['N15_M07_F04_KB27_4']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_5 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_5')
    N15_M07_F04_KB27_5 = N15_M07_F04_KB27_5.data['N15_M07_F04_KB27_5']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_6 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_6')
    N15_M07_F04_KB27_6 = N15_M07_F04_KB27_6.data['N15_M07_F04_KB27_6']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_7 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_7')
    N15_M07_F04_KB27_7 = N15_M07_F04_KB27_7.data['N15_M07_F04_KB27_7']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_8 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_8')
    N15_M07_F04_KB27_8 = N15_M07_F04_KB27_8.data['N15_M07_F04_KB27_8']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_9 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_9')
    N15_M07_F04_KB27_9 = N15_M07_F04_KB27_9.data['N15_M07_F04_KB27_9']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_10 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_10')
    N15_M07_F04_KB27_10 = N15_M07_F04_KB27_10.data['N15_M07_F04_KB27_10']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_11 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_11')
    N15_M07_F04_KB27_11 = N15_M07_F04_KB27_11.data['N15_M07_F04_KB27_11']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_12 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_12')
    N15_M07_F04_KB27_12 = N15_M07_F04_KB27_12.data['N15_M07_F04_KB27_12']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_13 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_13')
    N15_M07_F04_KB27_13 = N15_M07_F04_KB27_13.data['N15_M07_F04_KB27_13']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_14 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_14')
    N15_M07_F04_KB27_14 = N15_M07_F04_KB27_14.data['N15_M07_F04_KB27_14']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_15 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_15')
    N15_M07_F04_KB27_15 = N15_M07_F04_KB27_15.data['N15_M07_F04_KB27_15']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_16 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_16')
    N15_M07_F04_KB27_16 = N15_M07_F04_KB27_16.data['N15_M07_F04_KB27_16']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_17 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_17')
    N15_M07_F04_KB27_17 = N15_M07_F04_KB27_17.data['N15_M07_F04_KB27_17']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_18 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_18')
    N15_M07_F04_KB27_18 = N15_M07_F04_KB27_18.data['N15_M07_F04_KB27_18']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_19 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_19')
    N15_M07_F04_KB27_19 = N15_M07_F04_KB27_19.data['N15_M07_F04_KB27_19']['Y'][0][0][0][-1][2][0].flatten()
    N15_M07_F04_KB27_20 = read_data_one_subject(
        'D:/BaiduNetdiskDownload/德国帕德博恩轴承数据集/KB27/N15_M07_F04_KB27_20')
    N15_M07_F04_KB27_20 = N15_M07_F04_KB27_20.data['N15_M07_F04_KB27_20']['Y'][0][0][0][-1][2][0].flatten()
    '''
    合并N15_M07_F04数据
    '''
    '''
    NORMAL
    '''
    N15_M07_F04 = np.append(N15_M07_F04_K001_1, N15_M07_F04_K001_2)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_3)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_4)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_5)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_6)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_7)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_8)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_9)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_10)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_11)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_12)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_13)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_14)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_15)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_16)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_17)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_18)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_19)
    N15_M07_F04 = np.append(N15_M07_F04, N15_M07_F04_K001_20)

    '''
    Outer
    '''
    # KA01
    N15_M07_F04_Outer = np.append(N15_M07_F04_KA01_1, N15_M07_F04_KA01_2)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_3)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_4)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_5)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_6)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_7)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_8)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_9)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_10)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_11)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_12)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_13)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_14)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_15)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_16)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_17)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_18)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_19)
    N15_M07_F04_Outer = np.append(N15_M07_F04_Outer, N15_M07_F04_KA01_20)

    '''
    Inner
    '''
    # KI01
    N15_M07_F04_Inner = np.append(N15_M07_F04_KI01_1, N15_M07_F04_KI01_2)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_3)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_4)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_5)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_6)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_7)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_8)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_9)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_10)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_11)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_12)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_13)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_14)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_15)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_16)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_17)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_18)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_19)
    N15_M07_F04_Inner = np.append(N15_M07_F04_Inner, N15_M07_F04_KI01_20)

    '''
    IR+OR
    '''
    N15_M07_F04_IROR = np.append(N15_M07_F04_KB24_1, N15_M07_F04_KB24_2)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_3)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_4)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_5)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_6)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_7)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_8)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_9)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_10)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_11)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_12)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_13)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_14)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_15)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_16)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_17)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_18)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_19)
    N15_M07_F04_IROR = np.append(N15_M07_F04_IROR, N15_M07_F04_KB24_20)
    '''
    OR+IR
    '''
    N15_M07_F04_ORIR = np.append(N15_M07_F04_KB27_1, N15_M07_F04_KB27_2)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_3)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_4)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_5)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_6)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_7)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_8)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_9)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_10)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_11)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_12)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_13)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_14)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_15)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_16)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_17)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_18)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_19)
    N15_M07_F04_ORIR = np.append(N15_M07_F04_ORIR, N15_M07_F04_KB27_20)

    N15_M07_F04_ALL.append(N15_M07_F04)
    N15_M07_F04_ALL.append(N15_M07_F04_Outer)
    N15_M07_F04_ALL.append(N15_M07_F04_Inner)
    N15_M07_F04_ALL.append(N15_M07_F04_IROR)
    N15_M07_F04_ALL.append(N15_M07_F04_ORIR)

    return N15_M07_F04_ALL



