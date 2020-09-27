#导入相关包
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
# %matplotlib inline
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置加载的字体名
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
sns.set_style('white')   #设置图形背景样式为white

df = pd.read_csv('./cook.csv') 
df['难度'] = df['用料数'].apply(lambda x:'简单'if x < 5 else ('一般' if x < 15 else '较难')) #增加难度字段
df = df[['菜谱','用料','用料数','难度','菜系','评分','用户']] #选择需要的列
df.sample(5)  #查看数据集的随机5行数据

#distplot()输出直方图，默认拟合出密度曲线
plt.figure(figsize=(10, 6)) #设置画布大小
rate = df['评分']
sns.histplot(rate,color="salmon",bins=20) #参数color样式为salmon，bins参数设定数据片段的数量
plt.show()