import os 
import sys

# 获取当前工作区的目录
# eg.  D:\Document\template> python -u "d:\Document\template\test.py"
#      输出: D:\Document\template

print(os.getcwd())  

# sys.path[0]为当前py文件所在目录
# eg.  D:\Document\template> python -u "d:\Document\template\test.py"
#      输出: d:\\Document\\template
# 该path列表其他元素是其他系统目录
print(sys.path[0])

