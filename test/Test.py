import numpy as np
import torch
import math
from collections import defaultdict

d = defaultdict(int)
d[('sds', 'sas')] = 2
d[('sds', 'ss')] = 3
print(d)
print(set([x[0] for x in list(d.items())]))
