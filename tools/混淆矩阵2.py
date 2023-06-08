import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

confusion = np.array(([91, 22, 0],
                      [24, 92, 1],
                      [14, 1, 95]))

# 绘制混淆矩阵
fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(confusion, cmap='Blues')

# 添加标签
ax.set_xticks(np.arange(len(confusion)))
ax.set_yticks(np.arange(len(confusion)))
ax.set_xticklabels(['0', '1', '2'])
ax.set_yticklabels(['0', '1', '2'])

# 在矩阵中添加数值标签
for i in range(len(confusion)):
    for j in range(len(confusion)):
        text = ax.text(j, i, confusion[i, j], ha='center', va='center', color='w')

# 添加标题和轴标签
ax.set_title('Confusion Matrix')
ax.set_xlabel('Predicted Label')
ax.set_ylabel('True Label')

# 添加颜色条
plt.colorbar(im)

# 显示图形
plt.show()