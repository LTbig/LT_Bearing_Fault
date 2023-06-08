import torch
import torch.nn as nn

# 假设我们有一个展平的序列，形状为(batch_size, seq_length)
input_seq = torch.randn((32, 100))

# 添加分类标记，即在序列开头添加一个特殊的标记
cls_token = torch.randn((1, input_seq.shape[1]))
input_seq_with_cls = torch.cat([cls_token, input_seq], dim=0)

# 定义一个Embedding层，将每个整数标记映射到一个向量表示
vocab_size = 10000  # 假设我们的词汇表大小为10000
embedding_size = 1  # 假设我们想要每个标记映射到一个256维的向量表示
embedding = nn.Embedding(vocab_size, embedding_size)

# 将输入序列传递给Embedding层，得到每个标记的向量表示
embedded_seq = embedding(input_seq_with_cls.long())

# 现在我们可以将embedded_seq送入模型进行进一步处理