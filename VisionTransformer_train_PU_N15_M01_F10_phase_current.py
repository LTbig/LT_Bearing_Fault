import time
import matplotlib.pyplot as plt
from read_fault_data_PU_N15_M01_F10_phase_current import ready_data
from torch.utils.data import random_split
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
import torch.nn.functional as F
import torch
from torch import nn
import numpy as np
from einops import rearrange, repeat
from einops.layers.torch import Rearrange


def Confusion_matrix_plt(confusion, epoch):
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
    # 每1轮的混淆矩阵的标题
    plt.title('Confusion matrix_{}'.format(epoch))

    # plt.rcParams两行是用于解决标签不能显示汉字的问题
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 显示数据
    # All = np.sum(confusion)
    for first_index in range(len(confusion)):  # 第几行
        for second_index in range(len(confusion)):  # 第几列
            # plt.text(first_index, second_index, round((confusion[first_index][second_index] / All * 100), 3), va='center', ha='center',
            #          fontsize=10)
            plt.text(second_index, first_index, int(confusion[first_index][second_index]), va='center', ha='center',
                     fontsize=10)
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

    print(f'Macro-F1:{(OR_F1 + IR_F1 + NORMAL_F1) / 3}')


data = ready_data()  # 读取数据集

# 将数据升为2维数据
temp = []
for i in range(len(data)):
    # temp = data[i][0].reshape(24, 36)
    # temp = data[i][0].reshape(32, 32)
    temp = data[i][0].reshape(40, 64)
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
class PU_Dataset(Dataset):
    def __init__(self, data):
        self.len = len(data)
        self.x_data = torch.from_numpy(np.array(list(map(lambda x: x[0:-1], data)), dtype=np.float32))
        self.y_data = torch.from_numpy(np.array(list(map(lambda x: x[-1], data)), dtype=np.float32)).squeeze().long()

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len


Train_dataset = PU_Dataset(list(train_dataset))  # 训练集dataloader构造
Test_dataset = PU_Dataset(list(test_dataset))  # 测试集dataloader构造
dataloader = DataLoader(Train_dataset, shuffle=True, batch_size=128, drop_last=True)
test_loader = DataLoader(Test_dataset, shuffle=True, batch_size=128, drop_last=True)


# helpers

def pair(t):
    return t if isinstance(t, tuple) else (t, t)


# classes

class PreNorm(nn.Module):
    def __init__(self, dim, fn):
        super().__init__()
        self.norm = nn.LayerNorm(dim)
        self.fn = fn

    def forward(self, x, **kwargs):
        return self.fn(self.norm(x), **kwargs)


class FeedForward(nn.Module):
    def __init__(self, dim, hidden_dim, dropout=0.):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, dim),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.net(x)


class Attention(nn.Module):
    def __init__(self, dim, heads=8, dim_head=64, dropout=0.):
        super().__init__()
        inner_dim = dim_head * heads
        project_out = not (heads == 1 and dim_head == dim)

        self.heads = heads
        self.scale = dim_head ** -0.5

        self.attend = nn.Softmax(dim=-1)
        self.to_qkv = nn.Linear(dim, inner_dim * 3, bias=False)

        self.to_out = nn.Sequential(
            nn.Linear(inner_dim, dim),
            nn.Dropout(dropout)
        ) if project_out else nn.Identity()

    def forward(self, x):
        qkv = self.to_qkv(x).chunk(3, dim=-1)  ## 对tensor张量分块 x :1 197 1024   qkv 最后是一个元祖，tuple，长度是3，每个元素形状：1 197 1024
        q, k, v = map(lambda t: rearrange(t, 'b n (h d) -> b h n d', h=self.heads), qkv)

        dots = torch.matmul(q, k.transpose(-1, -2)) * self.scale

        attn = self.attend(dots)

        out = torch.matmul(attn, v)
        out = rearrange(out, 'b h n d -> b n (h d)')
        return self.to_out(out)


class Transformer(nn.Module):
    def __init__(self, dim, depth, heads, dim_head, mlp_dim, dropout=0.):
        super().__init__()
        self.layers = nn.ModuleList([])
        for _ in range(depth):
            self.layers.append(nn.ModuleList([
                PreNorm(dim, Attention(dim, heads=heads, dim_head=dim_head, dropout=dropout)),
                PreNorm(dim, FeedForward(dim, mlp_dim, dropout=dropout))
            ]))

    def forward(self, x):
        for attn, ff in self.layers:
            x = attn(x) + x
            x = ff(x) + x
        return x


class ViT(nn.Module):
    def __init__(self, *, image_size, patch_size, num_classes, dim, depth, heads, mlp_dim, pool='cls', channels,
                 dim_head=64, dropout=0., emb_dropout=0.):
        super().__init__()
        image_height, image_width = pair(image_size)  ## 224*224
        patch_height, patch_width = pair(patch_size)  ## 16 * 16

        assert image_height % patch_height == 0 and image_width % patch_width == 0, 'Image dimensions must be divisible by the patch size.'

        num_patches = (image_height // patch_height) * (image_width // patch_width)
        patch_dim = channels * patch_height * patch_width
        assert pool in {'cls', 'mean'}, 'pool type must be either cls (cls token) or mean (mean pooling)'

        self.to_patch_embedding = nn.Sequential(
            Rearrange('b c (h p1) (w p2) -> b (h w) (p1 p2 c)', p1=patch_height, p2=patch_width),
            nn.Linear(patch_dim, dim),
        )

        self.pos_embedding = nn.Parameter(torch.randn(1, num_patches + 1, dim))
        self.cls_token = nn.Parameter(torch.randn(1, 1, dim))
        self.dropout = nn.Dropout(emb_dropout)

        self.transformer = Transformer(dim, depth, heads, dim_head, mlp_dim, dropout)
        self.pool = pool
        self.to_latent = nn.Identity()

        self.mlp_head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_classes)
        )

    def forward(self, img):
        x = self.to_patch_embedding(img)  ## img 1 3 224 224  输出形状x : 1 196 1024
        b, n, _ = x.shape  ##

        cls_tokens = repeat(self.cls_token, '() n d -> b n d', b=b)
        x = torch.cat((cls_tokens, x), dim=1)
        x += self.pos_embedding[:, :(n + 1)]
        x = self.dropout(x)

        x = self.transformer(x)
        x = x.mean(dim=1) if self.pool == 'mean' else x[:, 0]

        x = self.to_latent(x)
        # x = self.mlp_head(x)
        return x


model = ViT(
    image_size=(40, 64),
    patch_size=(8, 8),
    channels=1,
    num_classes=10,
    dim=1024,
    depth=6,
    heads=12,
    mlp_dim=2048,
    dropout=0.1,
    emb_dropout=0.1
)

# 准备好GPU设备
Device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(torch.cuda.is_available())

# 将模型丢到GPU设备中
model = model.to(Device)

# 损失函数 交叉熵损失
criterion = nn.CrossEntropyLoss().to(Device)

# 优化器
learning_rate = 1e-3
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate, momentum=0.9)

# 学习率围为0.0001
# optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)

# 构造损失列表用于画图
epoch_list = []
loss_list = []
train_acc_list = []
test_acc_list = []

train_correct = 0
train_total = 0

# 添加Tensorboard 记录训练过程中的一些参数指标的变化趋势
writer = SummaryWriter('./logs')


# 定义测试集测试函数,并绘制混淆矩阵Confusion_matrix
def test():
    global test_acc
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
    writer.add_scalar("Test_loss:", total_test_loss, epoch)
    test_acc = 100 * correct / total
    if test_acc > 98.5:
        torch.save(model, './models/CAR_{}.pth'.format(test_acc))
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
        # 每1轮打印一次训练的准确率
    if epoch % 1 == 0:
        probability, predicted = torch.max(y_pred.data, dim=1)
        train_total += y_pred.size(0)
        train_correct += (predicted == y_data).sum().item()
        epoch_list.append(epoch)
        train_acc = 100 * train_correct / train_total
        train_acc_list.append(train_acc)
        print('=' * 10, epoch, '=' * 10)
        print('loss:', loss.item())
        print(f'accuracy on train set:{train_acc} ')
        writer.add_scalar("Train_acc:", train_acc, epoch)
        test()


#  训练和测试开始
start = time.time()
for epoch in range(201):
    Confusion_matrix = np.zeros([3, 3])
    train(epoch)
    if epoch % 100 == 0:
        Confusion_matrix_plt(Confusion_matrix, epoch=epoch)
get_paramer_matrix(Confusion_matrix)
end = time.time()
print("cost time:", end - start)

# 打印准确率
print("平均准确率:", np.mean(np.array(test_acc_list)))
print("标准差:", np.std(np.array(test_acc_list)))
print("最低准确率:", np.min(np.array(test_acc_list)))
print("最高准确率:", np.max(np.array(test_acc_list)))

# 绘图
plt.plot(epoch_list, train_acc_list, label='train_Acc')
plt.plot(epoch_list, test_acc_list, label='test_Acc')
plt.ylabel('Accuracy')
plt.xlabel('epoch')
plt.legend()
plt.show()
