# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)

import os

target_dir = os.getcwd()

instances = []
for root, dirs, fnames in os.walk(target_dir, followlinks=True):
    print(root, dirs, fnames)
    for fname in fnames:
        path = os.path.join(root, fname) 
        if is_valid_file(path):       # 可以自己定义的函数
            instances.append(paths)

# 对于下面这种结构，root，dirs，fnames的输出依次如下所示
# test
#   test
#       2.txt
#   1.txt
# test.py

# D:\Document\template ['test'] ['test.py']
# D:\Document\template\test ['test'] ['1.txt']
# D:\Document\template\test\test [] ['2.txt']