import numpy as np

# 原始一维数据
data = np.array([1, 2, 3, 4, 5, 6])

# 将一维数据升为2维，第一维度为数据长度，第二维度为1
temp = data.reshape((len(data), 1))
data = temp
print(data)

# import numpy as np
#
# # 原始一维数据
# data = np.array([1, 2, 3, 4, 5, 6])
#
# # 将一维数据升为2维，第一维度为数据长度，第二维度为1
# data_2d = np.reshape(data, (len(data), 1))
#
# print(data_2d)