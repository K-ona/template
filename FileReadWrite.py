# case 1: write json file

import json

cla_dict = {0: 'daisy', 1: 'dandelion', 2: 'roses', 3: 'sunflower', 4: 'tulips'}

# 将dict转化为str
json_str = json.dumps(cla_dict, indent=4) 

with open('class_indices.json', 'w') as json_file:
    # 写到文件中去
    json_file.write(json_str)
    json_file.close()

# case 2: load json file

# json.load（）用于读取json数据
data4=json.load(open('class_indices.json'))

# type: dict
print(data4)  

# case 3: write csv file
import csv
import random

with open('data.csv','w', newline='') as fp:
    writer = csv.writer(fp, delimiter = ' ')#先传入文件句柄
    writer.writerow(['x','y','z'])#然后写入
    for _ in range(300):
        x = random.gauss(0, 1)
        y = random.gauss(0, 1)
        z = x + y - x * y / (1.414 + random.gauss(0, 1))
        writer.writerow((x,y,z))#按行写入
    fp.close()

# case 4: read csv file
import pandas as pd 
df = pd.read_csv('data.csv')
print(df)

import csv
with open('data.csv','r',encoding = 'utf8') as fp:
    reader = csv.reader(fp)
    for row in reader:
        print(row)

