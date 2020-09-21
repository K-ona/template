# 稀疏初始化
# torch.nn.init.sparse_(tensor, sparsity, std=0.01)
import torch
import torch.nn as nn

tensor = torch.tensor([ [1, 2, 3],
                        [2, 3, 4],
                        [4, 5, 6] ], dtype=torch.float)

# 从正态分布N～（0. std）中进行稀疏化，使每一个column有一部分为0
# sparsity 每一个column稀疏的比例，即为0的比例

nn.init.sparse_(tensor, sparsity=0.1)
print(tensor)
