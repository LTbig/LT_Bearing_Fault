import time
import matplotlib.pyplot as plt
from read_fault_data_PU_N15_M07_F04_phase_current import ready_data
from torch.utils.data import random_split
from torch.utils.data import DataLoader, Dataset
from torch.utils.tensorboard import SummaryWriter
import torch.nn.functional as F
import torch
from torch import nn
import numpy as np
import torch.utils.checkpoint as checkpoint
from timm.models.layers import DropPath, to_2tuple, trunc_normal_


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
        for second_index in range(len(confusion[first_index])):  # 第几列
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
    # temp = data[i][0].reshape(40, 64)
    temp = data[i][0].reshape(224, 224)
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
dataloader = DataLoader(Train_dataset, shuffle=True, batch_size=16, drop_last=True)
test_loader = DataLoader(Test_dataset, shuffle=True, batch_size=16, drop_last=True)


class Mlp(nn.Module):
    def __init__(self, in_features, hidden_features=None, out_features=None, act_layer=nn.GELU, drop=0.):
        super().__init__()
        out_features = out_features or in_features
        hidden_features = hidden_features or in_features
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.act = act_layer()
        self.fc2 = nn.Linear(hidden_features, out_features)
        self.drop = nn.Dropout(drop)

    def forward(self, x):
        x = self.fc1(x)
        x = self.act(x)
        x = self.drop(x)
        x = self.fc2(x)
        x = self.drop(x)
        return x


def window_partition(x, window_size):
    """
    Args:
        x: (B, H, W, C)
        window_size (int): window size

    Returns:
        windows: (num_windows*B, window_size, window_size, C)
    """
    B, H, W, C = x.shape
    x = x.view(B, H // window_size, window_size, W // window_size, window_size, C)
    windows = x.permute(0, 1, 3, 2, 4, 5).contiguous().view(-1, window_size, window_size, C)
    return windows


def window_reverse(windows, window_size, H, W):
    """
    Args:
        windows: (num_windows*B, window_size, window_size, C)
        window_size (int): Window size
        H (int): Height of image
        W (int): Width of image

    Returns:
        x: (B, H, W, C)
    """
    B = int(windows.shape[0] / (H * W / window_size / window_size))## 输入进来wind形状是 64 7 7  96
    x = windows.view(B, H // window_size, W // window_size, window_size, window_size, -1)
    x = x.permute(0, 1, 3, 2, 4, 5).contiguous().view(B, H, W, -1)
    return x


## 2.
class WindowAttention(nn.Module):
    r""" Window based multi-head self attention (W-MSA) module with relative position bias.
    It supports both of shifted and non-shifted window.

    Args:
        dim (int): Number of input channels.
        window_size (tuple[int]): The height and width of the window.
        num_heads (int): Number of attention heads.
        qkv_bias (bool, optional):  If True, add a learnable bias to query, key, value. Default: True
        qk_scale (float | None, optional): Override default qk scale of head_dim ** -0.5 if set
        attn_drop (float, optional): Dropout ratio of attention weight. Default: 0.0
        proj_drop (float, optional): Dropout ratio of output. Default: 0.0
    """

    def __init__(self, dim, window_size, num_heads, qkv_bias=True, qk_scale=None, attn_drop=0., proj_drop=0.):

        super().__init__()
        self.dim = dim
        self.window_size = window_size  # Wh, Ww
        self.num_heads = num_heads
        head_dim = dim // num_heads
        self.scale = qk_scale or head_dim ** -0.5

        # define a parameter table of relative position bias
        self. relative_position_bias_table = nn.Parameter(
            torch.zeros((2 * window_size[0] - 1) * (2 * window_size[1] - 1), num_heads))  # 2*Wh-1 * 2*Ww-1, nH

        # get pair-wise relative position index for each token inside the window
        coords_h = torch.arange(self.window_size[0])
        coords_w = torch.arange(self.window_size[1])
        coords = torch.stack(torch.meshgrid([coords_h, coords_w]))  # 2, Wh, Ww
        coords_flatten = torch.flatten(coords, 1)  # 2, Wh*Ww
        relative_coords = coords_flatten[:, :, None] - coords_flatten[:, None, :]  # 2, Wh*Ww, Wh*Ww
        relative_coords = relative_coords.permute(1, 2, 0).contiguous()  # Wh*Ww, Wh*Ww, 2
        relative_coords[:, :, 0] += self.window_size[0] - 1  # shift to start from 0
        relative_coords[:, :, 1] += self.window_size[1] - 1
        relative_coords[:, :, 0] *= 2 * self.window_size[1] - 1
        relative_position_index = relative_coords.sum(-1)  # Wh*Ww, Wh*Ww
        self.register_buffer("relative_position_index", relative_position_index)

        self.qkv = nn.Linear(dim, dim * 3, bias=qkv_bias)
        self.attn_drop = nn.Dropout(attn_drop)
        self.proj = nn.Linear(dim, dim)
        self.proj_drop = nn.Dropout(proj_drop)

        trunc_normal_(self.relative_position_bias_table, std=.02)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, x, mask=None):
        """
        Args:
            x: input features with shape of (num_windows*B, N, C)
            mask: (0/-inf) mask with shape of (num_windows, Wh*Ww, Wh*Ww) or None
        """
        B_, N, C = x.shape## x输入形状是 64 49 96 ；对应到每个维度就是B是64，N是49，C是96
        qkv = self.qkv(x).reshape(B_, N, 3, self.num_heads, C // self.num_heads).permute(2, 0, 3, 1, 4)
        q, k, v = qkv[0], qkv[1], qkv[2]  # make torchscript happy (cannot use tensor as tuple)

        q = q * self.scale
        attn = (q @ k.transpose(-2, -1))

        relative_position_bias = self.relative_position_bias_table[self.relative_position_index.view(-1)].view(
            self.window_size[0] * self.window_size[1], self.window_size[0] * self.window_size[1], -1)  # Wh*Ww,Wh*Ww,nH
        relative_position_bias = relative_position_bias.permute(2, 0, 1).contiguous()  # nH, Wh*Ww, Wh*Ww
        attn = attn + relative_position_bias.unsqueeze(0)

        if mask is not None:
            nW = mask.shape[0]
            attn = attn.view(B_ // nW, nW, self.num_heads, N, N) + mask.unsqueeze(1).unsqueeze(0)
            attn = attn.view(-1, self.num_heads, N, N)
            attn = self.softmax(attn)
        else:
            attn = self.softmax(attn)

        attn = self.attn_drop(attn)

        x = (attn @ v).transpose(1, 2).reshape(B_, N, C)
        x = self.proj(x)
        x = self.proj_drop(x)
        return x

    def extra_repr(self) -> str:
        return f'dim={self.dim}, window_size={self.window_size}, num_heads={self.num_heads}'

    def flops(self, N):
        # calculate flops for 1 window with token length of N
        flops = 0
        # qkv = self.qkv(x)
        flops += N * self.dim * 3 * self.dim
        # attn = (q @ k.transpose(-2, -1))
        flops += self.num_heads * N * (self.dim // self.num_heads) * N
        #  x = (attn @ v)
        flops += self.num_heads * N * N * (self.dim // self.num_heads)
        # x = self.proj(x)
        flops += N * self.dim * self.dim
        return flops


class SwinTransformerBlock(nn.Module):
    r""" Swin Transformer Block.

    Args:
        dim (int): Number of input channels.
        input_resolution (tuple[int]): Input resulotion.
        num_heads (int): Number of attention heads.
        window_size (int): Window size.
        shift_size (int): Shift size for SW-MSA.
        mlp_ratio (float): Ratio of mlp hidden dim to embedding dim.
        qkv_bias (bool, optional): If True, add a learnable bias to query, key, value. Default: True
        qk_scale (float | None, optional): Override default qk scale of head_dim ** -0.5 if set.
        drop (float, optional): Dropout rate. Default: 0.0
        attn_drop (float, optional): Attention dropout rate. Default: 0.0
        drop_path (float, optional): Stochastic depth rate. Default: 0.0
        act_layer (nn.Module, optional): Activation layer. Default: nn.GELU
        norm_layer (nn.Module, optional): Normalization layer.  Default: nn.LayerNorm
    """

    def __init__(self, dim, input_resolution, num_heads, window_size=7, shift_size=0,
                 mlp_ratio=4., qkv_bias=True, qk_scale=None, drop=0., attn_drop=0., drop_path=0.,
                 act_layer=nn.GELU, norm_layer=nn.LayerNorm):
        super().__init__()
        self.dim = dim
        self.input_resolution = input_resolution
        self.num_heads = num_heads
        self.window_size = window_size
        self.shift_size = shift_size
        self.mlp_ratio = mlp_ratio
        if min(self.input_resolution) <= self.window_size:
            # if window size is larger than input resolution, we don't partition windows
            self.shift_size = 0
            self.window_size = min(self.input_resolution)
        assert 0 <= self.shift_size < self.window_size, "shift_size must in 0-window_size"

        self.norm1 = norm_layer(dim)
        self.attn = WindowAttention(
            dim, window_size=to_2tuple(self.window_size), num_heads=num_heads,
            qkv_bias=qkv_bias, qk_scale=qk_scale, attn_drop=attn_drop, proj_drop=drop)

        self.drop_path = DropPath(drop_path) if drop_path > 0. else nn.Identity()
        self.norm2 = norm_layer(dim)
        mlp_hidden_dim = int(dim * mlp_ratio)
        self.mlp = Mlp(in_features=dim, hidden_features=mlp_hidden_dim, act_layer=act_layer, drop=drop)
        ## 3.mask
        if self.shift_size > 0:
            # calculate attention mask for SW-MSA
            H, W = self.input_resolution
            img_mask = torch.zeros((1, H, W, 1))  # 1 H W 1
            h_slices = (slice(0, -self.window_size),
                        slice(-self.window_size, -self.shift_size),
                        slice(-self.shift_size, None))## 生成一个元祖，第0个元素 slice(0, -7, None) 第1个元素slice(-7, -3, None) 第2个元素slice(-3, None, None) 每个元素三个分别代表 start step stop
            w_slices = (slice(0, -self.window_size),
                        slice(-self.window_size, -self.shift_size),
                        slice(-self.shift_size, None))
            cnt = 0
            for h in h_slices:
                for w in w_slices:
                    img_mask[:, h, w, :] = cnt
                    cnt += 1

            mask_windows = window_partition(img_mask, self.window_size)  # nW, window_size, window_size, 1
            mask_windows = mask_windows.view(-1, self.window_size * self.window_size)
            attn_mask = mask_windows.unsqueeze(1) - mask_windows.unsqueeze(2)
            attn_mask = attn_mask.masked_fill(attn_mask != 0, float(-100.0)).masked_fill(attn_mask == 0, float(0.0))
        else:
            attn_mask = None

        self.register_buffer("attn_mask", attn_mask)

    def forward(self, x):
        H, W = self.input_resolution## 输入的x形状是:1 3136 96 得到H是56 W是56
        B, L, C = x.shape## 这个是B是1，L是seq_len等于3136，C是通道数为96
        assert L == H * W, "input feature has wrong size"

        shortcut = x
        x = self.norm1(x)
        x = x.view(B, H, W, C)## 从1 3136 96 转为  1 56 56 96  注意这个时候就从输入的一维那种向量转为了特征图，也就是一维3136，到了一个二维特征图 56 56 ，对应到原始图片是224 224

        # cyclic shift
        if self.shift_size > 0:
            shifted_x = torch.roll(x, shifts=(-self.shift_size, -self.shift_size), dims=(1, 2))
        else:
            shifted_x = x

        # partition windows
        x_windows = window_partition(shifted_x, self.window_size) ## 64 7 7 96  # nW*B, window_size, window_size, C
        x_windows = x_windows.view(-1, self.window_size * self.window_size, C) ## 64 49 96 ；64是bs乘以每个图片的窗口，49是一个窗口中的有多少个元素，对应到NLP中，就是有多少个单词，96是通道数，对应到NLP就是每个单词的维度  # nW*B, window_size*window_size, C

        # W-MSA/SW-MSA
        attn_windows = self.attn(x_windows, mask=self.attn_mask)## attn_windows 64 49 96，和trm没区别哈，长度49不变，toen维度96没变；  # nW*B, window_size*window_size, C

        # merge windows
        attn_windows = attn_windows.view(-1, self.window_size, self.window_size, C)
        shifted_x = window_reverse(attn_windows, self.window_size, H, W)  # B H' W' C

        # reverse cyclic shift
        if self.shift_size > 0:
            x = torch.roll(shifted_x, shifts=(self.shift_size, self.shift_size), dims=(1, 2))
        else:
            x = shifted_x
        x = x.view(B, H * W, C)

        # FFN
        x = shortcut + self.drop_path(x)
        x = x + self.drop_path(self.mlp(self.norm2(x)))

        return x

    def extra_repr(self) -> str:
        return f"dim={self.dim}, input_resolution={self.input_resolution}, num_heads={self.num_heads}, " \
               f"window_size={self.window_size}, shift_size={self.shift_size}, mlp_ratio={self.mlp_ratio}"

    def flops(self):
        flops = 0
        H, W = self.input_resolution
        # norm1
        flops += self.dim * H * W
        # W-MSA/SW-MSA
        nW = H * W / self.window_size / self.window_size
        flops += nW * self.attn.flops(self.window_size * self.window_size)
        # mlp
        flops += 2 * H * W * self.dim * self.dim * self.mlp_ratio
        # norm2
        flops += self.dim * H * W
        return flops


class PatchMerging(nn.Module):
    r""" Patch Merging Layer.

    Args:
        input_resolution (tuple[int]): Resolution of input feature.
        dim (int): Number of input channels.
        norm_layer (nn.Module, optional): Normalization layer.  Default: nn.LayerNorm
    """

    def __init__(self, input_resolution, dim, norm_layer=nn.LayerNorm):
        super().__init__()
        self.input_resolution = input_resolution
        self.dim = dim
        self.reduction = nn.Linear(4 * dim, 2 * dim, bias=False)
        self.norm = norm_layer(4 * dim)

    def forward(self, x):
        """
        x: B, H*W, C
        """
        H, W = self.input_resolution #
        B, L, C = x.shape ## 输入进来x为1 3136 96
        assert L == H * W, "input feature has wrong size"
        assert H % 2 == 0 and W % 2 == 0, f"x size ({H}*{W}) are not even."

        x = x.view(B, H, W, C) ## 这里x变为了 1 56 56  96

        x0 = x[:, 0::2, 0::2, :]  # B H/2 W/2 C ## x0形状为1 28 28 96
        x1 = x[:, 1::2, 0::2, :]  # B H/2 W/2 C ## x1形状为1 28 28 96
        x2 = x[:, 0::2, 1::2, :]  # B H/2 W/2 C## ## x2形状为1 28 28 96
        x3 = x[:, 1::2, 1::2, :]  # B H/2 W/2 C ## ## x3形状为1 28 28 96
        x = torch.cat([x0, x1, x2, x3], -1)  # B H/2 W/2 4*C  ## x为1 28 28 384
        x = x.view(B, -1, 4 * C)  # B H/2*W/2 4*C ## 1 784 384

        x = self.norm(x)
        x = self.reduction(x) # 1 784 192

        return x

    def extra_repr(self) -> str:
        return f"input_resolution={self.input_resolution}, dim={self.dim}"

    def flops(self):
        H, W = self.input_resolution
        flops = H * W * self.dim
        flops += (H // 2) * (W // 2) * 4 * self.dim * 2 * self.dim
        return flops


class BasicLayer(nn.Module):
    """ A basic Swin Transformer layer for one stage.

    Args:
        dim (int): Number of input channels.
        input_resolution (tuple[int]): Input resolution.
        depth (int): Number of blocks.
        num_heads (int): Number of attention heads.
        window_size (int): Local window size.
        mlp_ratio (float): Ratio of mlp hidden dim to embedding dim.
        qkv_bias (bool, optional): If True, add a learnable bias to query, key, value. Default: True
        qk_scale (float | None, optional): Override default qk scale of head_dim ** -0.5 if set.
        drop (float, optional): Dropout rate. Default: 0.0
        attn_drop (float, optional): Attention dropout rate. Default: 0.0
        drop_path (float | tuple[float], optional): Stochastic depth rate. Default: 0.0
        norm_layer (nn.Module, optional): Normalization layer. Default: nn.LayerNorm
        downsample (nn.Module | None, optional): Downsample layer at the end of the layer. Default: None
        use_checkpoint (bool): Whether to use checkpointing to save memory. Default: False.
    """

    def __init__(self, dim, input_resolution, depth, num_heads, window_size,
                 mlp_ratio=4., qkv_bias=True, qk_scale=None, drop=0., attn_drop=0.,
                 drop_path=0., norm_layer=nn.LayerNorm, downsample=None, use_checkpoint=False):

        super().__init__()
        self.dim = dim
        self.input_resolution = input_resolution
        self.depth = depth
        self.use_checkpoint = use_checkpoint

        # build blocks
        self.blocks = nn.ModuleList([
            SwinTransformerBlock(dim=dim, input_resolution=input_resolution,
                                 num_heads=num_heads, window_size=window_size,
                                 shift_size=0 if (i % 2 == 0) else window_size // 2,
                                 mlp_ratio=mlp_ratio,
                                 qkv_bias=qkv_bias, qk_scale=qk_scale,
                                 drop=drop, attn_drop=attn_drop,
                                 drop_path=drop_path[i] if isinstance(drop_path, list) else drop_path,
                                 norm_layer=norm_layer)
            for i in range(depth)])

        # patch merging layer
        if downsample is not None:
            self.downsample = downsample(input_resolution, dim=dim, norm_layer=norm_layer)
        else:
            self.downsample = None

    def forward(self, x):
        for blk in self.blocks:
            if self.use_checkpoint:
                x = checkpoint.checkpoint(blk, x)
            else:
                x = blk(x)
        if self.downsample is not None:
            x = self.downsample(x)
        return x

    def extra_repr(self) -> str:
        return f"dim={self.dim}, input_resolution={self.input_resolution}, depth={self.depth}"

    def flops(self):
        flops = 0
        for blk in self.blocks:
            flops += blk.flops()
        if self.downsample is not None:
            flops += self.downsample.flops()
        return flops


## 1. patchembedding的实现
class PatchEmbed(nn.Module):
    r""" Image to Patch Embedding

    Args:
        img_size (int): Image size.  Default: 224.
        patch_size (int): Patch token size. Default: 4.
        in_chans (int): Number of input image channels. Default: 3.
        embed_dim (int): Number of linear projection output channels. Default: 96.
        norm_layer (nn.Module, optional): Normalization layer. Default: None
    """

    def __init__(self, img_size=224, patch_size=4, in_chans=3, embed_dim=96, norm_layer=None):
        super().__init__()
        img_size = to_2tuple(img_size)
        patch_size = to_2tuple(patch_size)
        patches_resolution = [img_size[0] // patch_size[0], img_size[1] // patch_size[1]]
        self.img_size = img_size
        self.patch_size = patch_size
        self.patches_resolution = patches_resolution
        self.num_patches = patches_resolution[0] * patches_resolution[1]

        self.in_chans = in_chans
        self.embed_dim = embed_dim

        self.proj = nn.Conv2d(in_chans, embed_dim, kernel_size=patch_size, stride=patch_size)
        if norm_layer is not None:
            self.norm = norm_layer(embed_dim)
        else:
            self.norm = None

    def forward(self, x):
        B, C, H, W = x.shape # B是1  C3 H224  W224
        # FIXME look at relaxing size constraints
        assert H == self.img_size[0] and W == self.img_size[1], \
            f"Input image size ({H}*{W}) doesn't match model ({self.img_size[0]}*{self.img_size[1]})."
        x = self.proj(x).flatten(2).transpose(1, 2)  # B Ph*Pw C  1 3136 96  3136就是我们的56*56 压扁
        if self.norm is not None:
            x = self.norm(x)
        return x

    def flops(self):
        Ho, Wo = self.patches_resolution
        flops = Ho * Wo * self.embed_dim * self.in_chans * (self.patch_size[0] * self.patch_size[1])
        if self.norm is not None:
            flops += Ho * Wo * self.embed_dim
        return flops


class SwinTransformer(nn.Module):
    r""" Swin Transformer
        A PyTorch impl of : `Swin Transformer: Hierarchical Vision Transformer using Shifted Windows`  -
          https://arxiv.org/pdf/2103.14030

    Args:
        img_size (int | tuple(int)): Input image size. Default 224
        patch_size (int | tuple(int)): Patch size. Default: 4
        in_chans (int): Number of input image channels. Default: 3
        num_classes (int): Number of classes for classification head. Default: 1000
        embed_dim (int): Patch embedding dimension. Default: 96
        depths (tuple(int)): Depth of each Swin Transformer layer.
        num_heads (tuple(int)): Number of attention heads in different layers.
        window_size (int): Window size. Default: 7
        mlp_ratio (float): Ratio of mlp hidden dim to embedding dim. Default: 4
        qkv_bias (bool): If True, add a learnable bias to query, key, value. Default: True
        qk_scale (float): Override default qk scale of head_dim ** -0.5 if set. Default: None
        drop_rate (float): Dropout rate. Default: 0
        attn_drop_rate (float): Attention dropout rate. Default: 0
        drop_path_rate (float): Stochastic depth rate. Default: 0.1
        norm_layer (nn.Module): Normalization layer. Default: nn.LayerNorm.
        ape (bool): If True, add absolute position embedding to the patch embedding. Default: False
        patch_norm (bool): If True, add normalization after patch embedding. Default: True
        use_checkpoint (bool): Whether to use checkpointing to save memory. Default: False
    """

    def __init__(self, img_size=224, patch_size=4, in_chans=1, num_classes=3,
                 embed_dim=96, depths=[2, 2, 6, 2], num_heads=[3, 6, 12, 24],
                 window_size=7, mlp_ratio=4., qkv_bias=True, qk_scale=None,
                 drop_rate=0., attn_drop_rate=0., drop_path_rate=0.1,
                 norm_layer=nn.LayerNorm, ape=False, patch_norm=True,
                 use_checkpoint=False, **kwargs):
        super().__init__()

        self.num_classes = num_classes
        self.num_layers = len(depths)
        self.embed_dim = embed_dim
        self.ape = ape
        self.patch_norm = patch_norm
        self.num_features = int(embed_dim * 2 ** (self.num_layers - 1))
        self.mlp_ratio = mlp_ratio

        # split image into non-overlapping patches
        self.patch_embed = PatchEmbed(
            img_size=img_size, patch_size=patch_size, in_chans=in_chans, embed_dim=embed_dim,
            norm_layer=norm_layer if self.patch_norm else None)
        num_patches = self.patch_embed.num_patches
        patches_resolution = self.patch_embed.patches_resolution
        self.patches_resolution = patches_resolution

        # absolute position embedding
        if self.ape:
            self.absolute_pos_embed = nn.Parameter(torch.zeros(1, num_patches, embed_dim))
            trunc_normal_(self.absolute_pos_embed, std=.02)

        self.pos_drop = nn.Dropout(p=drop_rate)

        # stochastic depth
        dpr = [x.item() for x in torch.linspace(0, drop_path_rate, sum(depths))]  # stochastic depth decay rule

        # build layers
        self.layers = nn.ModuleList()
        for i_layer in range(self.num_layers):
            layer = BasicLayer(dim=int(embed_dim * 2 ** i_layer),
                               input_resolution=(patches_resolution[0] // (2 ** i_layer),
                                                 patches_resolution[1] // (2 ** i_layer)),
                               depth=depths[i_layer],
                               num_heads=num_heads[i_layer],
                               window_size=window_size,
                               mlp_ratio=self.mlp_ratio,
                               qkv_bias=qkv_bias, qk_scale=qk_scale,
                               drop=drop_rate, attn_drop=attn_drop_rate,
                               drop_path=dpr[sum(depths[:i_layer]):sum(depths[:i_layer + 1])],
                               norm_layer=norm_layer,
                               downsample=PatchMerging if (i_layer < self.num_layers - 1) else None,
                               use_checkpoint=use_checkpoint)
            self.layers.append(layer)

        self.norm = norm_layer(self.num_features)
        self.avgpool = nn.AdaptiveAvgPool1d(1)
        self.head = nn.Linear(self.num_features, num_classes) if num_classes > 0 else nn.Identity()

        self.apply(self._init_weights)

    def _init_weights(self, m):
        if isinstance(m, nn.Linear):
            trunc_normal_(m.weight, std=.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.constant_(m.bias, 0)
        elif isinstance(m, nn.LayerNorm):
            nn.init.constant_(m.bias, 0)
            nn.init.constant_(m.weight, 1.0)

    @torch.jit.ignore
    def no_weight_decay(self):
        return {'absolute_pos_embed'}

    @torch.jit.ignore
    def no_weight_decay_keywords(self):
        return {'relative_position_bias_table'}

    def forward_features(self, x):
        x = self.patch_embed(x)
        if self.ape:
            x = x + self.absolute_pos_embed
        x = self.pos_drop(x)

        for layer in self.layers:
            x = layer(x)

        x = self.norm(x)  # B L C
        x = self.avgpool(x.transpose(1, 2))  # B C 1
        x = torch.flatten(x, 1)
        return x

    def forward(self, x):
        x = self.forward_features(x)
        x = self.head(x)
        return x

    def flops(self):
        flops = 0
        flops += self.patch_embed.flops()
        for i, layer in enumerate(self.layers):
            flops += layer.flops()
        flops += self.num_features * self.patches_resolution[0] * self.patches_resolution[1] // (2 ** self.num_layers)
        flops += self.num_features * self.num_classes
        return flops


model = SwinTransformer()
# print("model:\n", model)


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
    global test_acc, Confusion_matrix
    Confusion_matrix = np.zeros([3, 3])
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
    if test_acc > 98:
        torch.save(model, './models/SwinTransformer_{}.pth'.format(test_acc))
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
for epoch in range(401):
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
