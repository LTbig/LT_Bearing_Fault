import time
import matplotlib.pyplot as plt
# from read_fault_data_single import ready_data
from read_fault_data_CWRU_48Khz_0hp_DEFE import ready_data
from torch.utils.data import random_split
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
import torch.nn.functional as F
import torch
from torch import nn
import numpy as np

'''
定义全局的超参数
'''
bs, ic, image_h, image_w = 32, 1, 24, 36
patch_size = 6
model_dim = 36  # model_dim 是输出通道数目=卷积核数量
max_num_token = 32  # 设置一个最大的token值
num_classes = 10  # 定义一个输出类别的大小
patch_depth = patch_size * patch_size * ic
# 初始化权重
weight = torch.randn(patch_depth, model_dim)  # model_dim 是输出通道数目,patch_depth是卷积核的面积乘以输入通道数


def Confusion_matrix_plt(confusion, epoch):
    # confusion = np.array(([91,0,0],[0,92,1],[0,0,95]))
    # 热度图，后面是指定的颜色块，可设置其他的不同颜色
    plt.imshow(confusion, cmap=plt.cm.Blues)
    # ticks 坐标轴的坐标点
    # label 坐标轴标签说明
    indices = range(len(confusion))
    # 第一个是迭代对象，表示坐标的显示顺序，第二个参数是坐标轴显示列表
    # plt.xticks(indices, [0, 1, 2])
    # plt.yticks(indices, [0, 1, 2])
    plt.xticks(indices, ['bl007', 'bl014', 'bl021', 'in007', 'in014',
                         'in021', 'ou007', 'ou014', 'ou021', 'normal'])
    plt.yticks(indices, ['bl007', 'bl014', 'bl021', 'in007', 'in014',
                         'in021', 'ou007', 'ou014', 'ou021', 'normal'])

    plt.colorbar()

    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    # 每1轮的混淆矩阵的标题
    plt.title('Confusion matrix_{}'.format(epoch))

    # plt.rcParams两行是用于解决标签不能显示汉字的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 显示数据
    for first_index in range(len(confusion)):  # 第几行
        for second_index in range(len(confusion[first_index])):  # 第几列
            plt.text(first_index, second_index, int(confusion[first_index][second_index]), va='center', ha='center',
                     fontsize=10)
    # 在matlab里面可以对矩阵直接imagesc(confusion)
    # 显示
    plt.show()


# convert image to embedding vector sequence
def Image2emb_naive(image, patch_size, weight):
    patch = F.unfold(image, kernel_size=patch_size, stride=patch_size). \
        transpose(-1, -2)  # transpose(-1, -2) 将最后1维和倒数第2维交换
    patch = patch.to(Device)
    weight = weight.to(Device)
    patch_embeding = patch @ weight
    # print("patch.shape:", patch.shape)  # 24 x 36 其中 24 = (24 * 36)/(6 * 6) 分块后的数目; 36 = (6 * 6) * 1 每1块的大小 这里只包含1个通道
    return patch_embeding


def Token_embedding(patch_embedding):
    cls_token_embedding = torch.randn(bs, 1, model_dim, requires_grad=True)
    cls_token_embedding = cls_token_embedding.to(Device)
    token_embedding = torch.cat((cls_token_embedding, patch_embedding), dim=1)
    return token_embedding


def Position_embedding(token_embedding):
    position_embedding_table = torch.randn(max_num_token, model_dim, requires_grad=True)
    seq_len = token_embedding.shape[1]
    # print("seq_len:", seq_len)
    position_embedding = torch.tile(position_embedding_table[:seq_len], [token_embedding.shape[0], 1, 1])
    position_embedding = position_embedding.to(Device)
    token_embedding += position_embedding
    return token_embedding


data = ready_data()  # 读取数据集

# 将数据升为2维数据
temp = []
for i in range(len(data)):
    temp = data[i][0].reshape(24, 36)
    data[i][0] = temp
temp = []

print("data length:", len(data))

train_len = int(len(data) * 0.8)
print("train_len:", train_len)  # 计算训练集长度
test_len = int(len(data)) - train_len  # 计算测试集长度
print("test_len:", test_len)

# 随机划分训练集和测试集

train_dataset, test_dataset = random_split(dataset=data, lengths=[train_len, test_len])


# 轴承数据集读取
class CWRU_Dataset(Dataset):
    def __init__(self, data):
        self.len = len(data)
        self.x_data = torch.from_numpy(np.array(list(map(lambda x: x[0:-1], data)), dtype=np.float32))
        self.y_data = torch.from_numpy(np.array(list(map(lambda x: x[-1], data)), dtype=np.float32)).squeeze().long()

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


Train_dataset = CWRU_Dataset(list(train_dataset))  # 训练集dataloader构造
Test_dataset = CWRU_Dataset(list(test_dataset))  # 测试集dataloader构造
dataloader = DataLoader(Train_dataset, shuffle=True, batch_size=bs, drop_last=True)
test_loader = DataLoader(Test_dataset, shuffle=True, batch_size=bs, drop_last=True)


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # Transformer层
        self.TransformerEncoderLayer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=2)
        self.TransformerEncoder = nn.TransformerEncoder(encoder_layer=self.TransformerEncoderLayer, num_layers=6)
        # 全连接层
        self.linear_layer = nn.Linear(model_dim, num_classes)

    def forward(self, x):
        # step1 convert image to embedding vector sequence
        x = Image2emb_naive(x, patch_size=patch_size, weight=weight)
        # step2 prepend cls token embedding
        x = Token_embedding(x)
        # step3 add position embedding
        x = Position_embedding(x)
        # step4 embedding to Transformer Encoder
        x = self.TransformerEncoder(x)
        # step5 do classification
        x = x[:, 0, :]
        x = self.linear_layer(x)
        return x


model = Net()
print("model:\n", model)

# 准备好GPU设备
Device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(Device)
print(torch.cuda.is_available())

# 将模型丢到GPU设备中
model = model.to(Device)

# 损失函数 交叉熵损失
criterion = nn.CrossEntropyLoss().to(Device)

# 优化器
# learning_rate = 1e-4
# optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

# 学习率围为0.0001
optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# 构造损失列表用于画图
epoch_list = []
loss_list = []
train_acc_list = []
test_acc_list = []

train_correct = 0
train_total = 0

# 添加Tensorboard 记录训练过程中的一些参数指标的变化趋势
writer = SummaryWriter('../logs')


# 定义测试集测试函数,并绘制混淆矩阵Confusion_matrix
def test():
    global test_acc, Confusion_matrix
    Confusion_matrix = np.zeros([10, 10])
    correct = 0
    total = 0
    # 记录测试时的损失函数
    total_test_loss = 0
    with torch.no_grad():
        for data in test_loader:
            feature, labels = data
            feature, labels = feature.to(Device), labels.to(Device)
            # batch_size = len(feature)
            # outputs = model(feature, batch_size)
            outputs = model(feature)
            loss = criterion(outputs, labels)
            total_test_loss = total_test_loss + loss.item()
            probability, predicted = torch.max(outputs.data, dim=1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            for i, j in zip(predicted, labels):
                Confusion_matrix[i][j] += 1
    print(f'Test_loss:{(total_test_loss)}', )
    writer.add_scalar("Test_loss:", total_test_loss, epoch)
    test_acc = 100 * correct / total
    if test_acc > 97:
        torch.save(model, './models/CNN_{}.pth'.format(test_acc))
    writer.add_scalar("Test_acc:", test_acc, epoch)
    test_acc_list.append(test_acc)
    print(f'accuracy on test set:{(test_acc)}')


# 定义训练集训练函数
def train(epoch):
    train_correct = 0
    train_total = 0
    # 记录训练的次数
    global loss, train_acc
    for data in dataloader:
        x_data, y_data = data
        x_data, y_data = x_data.to(Device), y_data.to(Device)
        # batch_size = len(x_data)
        # y_pred = model(x_data, batch_size)
        y_pred = model(x_data)
        loss = criterion(y_pred, y_data)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        writer.add_scalar("Train_loss:", loss.item(), epoch)
        # 每10轮打印一次训练的准确率
    if epoch % 10 == 0:
        probability, predicted = torch.max(y_pred.data, dim=1)
        train_total += y_pred.size(0)
        train_correct += (predicted == y_data).sum().item()
        epoch_list.append(epoch)
        train_acc = 100 * train_correct / train_total
        train_acc_list.append(train_acc)
        print('=' * 10, epoch // 10, '=' * 10)
        print('train loss:', loss.item())
        print(f'accuracy on train set:{train_acc} ')
        writer.add_scalar("Train_acc:", train_acc, epoch * 10)
        test()


#  训练和测试开始
start = time.time()
for epoch in range(401):
    train(epoch)
    if epoch % 100 == 0:
        Confusion_matrix_plt(Confusion_matrix, epoch=epoch)

end = time.time()
print("cost time:", end - start)

# 打印准确率
print("平均准确率:", np.mean(np.array(test_acc_list)))
print("标准差:", np.std(np.array(test_acc_list)))
print(("最低准确率:", np.min(np.array(test_acc_list))))
print("最高准确率:", np.max(np.array(test_acc_list)))

# 绘图
plt.plot(epoch_list, train_acc_list, label='train_Acc')
plt.plot(epoch_list, test_acc_list, label='test_Acc')
plt.ylabel('Accuracy')
plt.xlabel('epoch')
plt.legend()
plt.show()
