import matplotlib.pyplot as plt
import numpy as np


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
    plt.xticks(indices, ['OR', 'IR', 'NORMAL'])
    plt.yticks(indices, ['OR', 'IR', 'NORMAL'])

    plt.colorbar()
    # plt.clim(0, 100)
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.title('3-L')

    # plt.rcParams两行是用于解决标签不能显示汉字的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 显示数据
    All = np.sum(confusion)
    for first_index in range(len(confusion)):  # 第几行
        for second_index in range(len(confusion)):  # 第几列
            plt.text(second_index, first_index, int(confusion[first_index][second_index]), va='center', ha='center',
                     fontsize=10)
            # x应该为cows列 y为rws行
            # plt.text(second_index, first_index, round((confusion[first_index][second_index] / All * 100), 3), va='center', ha='center',
            #          fontsize=10)
    # 在matlab里面可以对矩阵直接imagesc(confusion)
    # 显示
    plt.show()


def get_paramer_matrix(matrix):
    All = np.sum(matrix)

    OR_TP = matrix[0, 0] / All
    OR_FP = (matrix[1, 0] + matrix[2, 0]) / All
    OR_FN = (matrix[0, 1] + matrix[0, 2]) / All
    OR_TN = 1 - OR_TP - OR_FP - OR_FN
    OR_precision = OR_TP / (OR_TP + OR_FP)
    OR_recall = OR_TP / (OR_TP + OR_FN)
    OR_F1 = 2 * OR_precision * OR_recall / (OR_precision + OR_recall)

    print("==========OR result==========")
    print(f'OR_TP:{OR_TP}')
    print(f'OR_FP:{OR_FP}')
    print(f'OR_TN:{OR_TN}')
    print(f'OR_FN:{OR_FN}')
    print(f'OR_precision:{OR_precision}')
    print(f'OR_recall:{OR_recall}')
    print(f'OR_F1:{OR_F1}')

    IR_TP = matrix[1, 1] / All
    IR_FP = (matrix[0, 1] + matrix[2, 1]) / All
    IR_FN = (matrix[1, 0] + matrix[1, 2]) / All
    IR_TN = 1 - IR_TP - IR_FP - IR_FN
    IR_precision = IR_TP / (IR_TP + IR_FP)
    IR_recall = IR_TP / (IR_TP + IR_FN)
    IR_F1 = 2 * IR_precision * IR_recall / (IR_precision + IR_recall)

    print("==========IR result==========")
    print(f'IR_TP:{IR_TP}')
    print(f'IR_FP:{IR_FP}')
    print(f'IR_TN:{IR_TN}')
    print(f'IR_FN:{IR_FN}')
    print(f'IR_precision:{IR_precision}')
    print(f'IR_recall:{IR_recall}')
    print(f'IR_F1:{IR_F1}')

    NORMAL_TP = matrix[2, 2] / All
    NORMAL_FP = (matrix[0, 2] + matrix[1, 2]) / All
    NORMAL_FN = (matrix[2, 0] + matrix[2, 1]) / All
    NORMAL_TN = 1 - NORMAL_TP - NORMAL_FP - NORMAL_FN
    NORMAL_precision = NORMAL_TP / (NORMAL_TP + NORMAL_FP)
    NORMAL_recall = NORMAL_TP / (NORMAL_TP + NORMAL_FN)
    NORMAL_F1 = 2 * NORMAL_precision * NORMAL_recall / (NORMAL_precision + NORMAL_recall)

    print("==========NORMAL result==========")
    print(f'NORMAL_TP:{NORMAL_TP}')
    print(f'NORMAL_FP:{NORMAL_FP}')
    print(f'NORMAL_TN:{NORMAL_TN}')
    print(f'NORMAL_FN:{NORMAL_FN}')
    print(f'NORMAL_precision:{NORMAL_precision}')
    print(f'NORMAL_recall:{NORMAL_recall}')
    print(f'NORMAL_F1:{NORMAL_F1}')


if __name__ == '__main__':
    confusion = np.array(([91, 22, 0],
                          [24, 92, 1],
                          [14, 1, 95]))
    Confusion_matrix_plt(confusion)
    get_paramer_matrix(confusion)
    # import torch
    # confusion2 = torch.zeros(3, 3)
    # Confusion_matrix_plt(confusion2)
