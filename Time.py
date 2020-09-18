# 计算间隔时间，单位：秒
import time

t1 = time.perf_counter()
print(time.perf_counter()-t1)

# get epoch 
import time

print(time.gmtime(0))
print(time.gmtime()) # UTC 
print(time.localtime()) #local time