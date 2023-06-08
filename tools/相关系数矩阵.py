import numpy as np
from scipy.spatial.distance import euclidean
from scipy.stats import pearsonr
from scipy.io import loadmat
import matplotlib.pyplot as plt
import pywt
import numpy as np
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

def Confusion_matrix_plt(confusion):
    # confusion = np.array(([91,0,0],[0,92,1],[0,0,95]))
    # 热度图，后面是指定的颜色块，可设置其他的不同颜色
    plt.imshow(confusion, cmap=plt.cm.Reds)
    # ticks 坐标轴的坐标点
    # label 坐标轴标签说明
    indices = range(len(confusion))
    # 第一个是迭代对象，表示坐标的显示顺序，第二个参数是坐标轴显示列表
    # plt.xticks(indices, [0, 1, 2])
    # plt.yticks(indices, [0, 1, 2])
    plt.xticks(indices, ['OR', 'IR', 'ORIR', 'IROR', 'NORMAL'])
    plt.yticks(indices, ['OR', 'IR', 'ORIR', 'IROR', 'NORMAL'])

    plt.colorbar()
    # plt.clim(0, 100)
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('1-L')

    # plt.rcParams两行是用于解决标签不能显示汉字的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 显示数据
    # All = np.sum(confusion)
    for first_index in range(len(confusion)):  # 第几行
        for second_index in range(len(confusion)):  # 第几列
            plt.text(second_index, first_index, '{:.2f}'.format(confusion[first_index][second_index]), va='center',
                     ha='center', fontsize=10)
            # x应该为cows列 y为rws行
            # plt.text(second_index, first_index, round((confusion[first_index][second_index] / All * 100), 3), va='center', ha='center',
            #          fontsize=10)
    # 在matlab里面可以对矩阵直接imagesc(confusion)
    # 显示
    plt.show()

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
    # print("=======================X======================")
    # print(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['X'])
    # print("=======================Y======================")
    # print(N09_M07_F10_K001_1.data['N09_M07_F10_K001_1']['Y'][0][0][0])
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
    # 生成5个时间序列
    ts1 = s15[:2560*4]
    ts2 = s25[:2560*4]
    ts3 = s35[:2560*4]
    ts4 = s45[:2560*4]
    ts5 = s55[:2560*4]

    # 计算相关系数
    corr_matrix = np.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            corr, _ = pearsonr(eval(f"ts{i+1}"), eval(f"ts{j+1}"))
            corr_matrix[i, j] = corr
    print("相关系数矩阵：")
    print(corr_matrix)
    ALL = np.sum(np.abs(corr_matrix))
    Mean_Correlation_Coefficient = ALL / 25
    print("平均相关系数：")
    print(Mean_Correlation_Coefficient)

    # 计算欧氏距离
    # dist_matrix = np.zeros((5, 5))
    # for i in range(5):
    #     for j in range(5):
    #         dist = euclidean(eval(f"ts{i+1}"), eval(f"ts{j+1}"))
    #         dist_matrix[i, j] = dist
    # print("欧氏距离矩阵：")
    # print(dist_matrix)

    Confusion_matrix_plt(corr_matrix)