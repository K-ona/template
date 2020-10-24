from ltp import LTP
import os

# path = r'D:\Data\small'
# print(os.path.isfile(path))

ltp = LTP(r'D:\Data\small') # 默认加载 Small 模型

seg, hidden = ltp.seg(["他叫汤姆去拿外衣。"])
print( ltp.pos(hidden))
print( ltp.ner(hidden))
print( ltp.srl(hidden))
print( ltp.dep(hidden))
print( ltp.sdp(hidden))