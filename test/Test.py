import numpy as np
import torch
import math

data = torch.from_numpy(np.random.random(size=(10, 10))) * 10
print(data.size())
print(data.unsqueeze(-2).size())
pass