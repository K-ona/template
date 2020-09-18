# 1: write json file

import json

cla_dict = {0: 'daisy', 1: 'dandelion', 2: 'roses', 3: 'sunflower', 4: 'tulips'}

# 将dict转化为str
json_str = json.dumps(cla_dict, indent=4) 

with open('class_indices.json', 'w') as json_file:
    # 写到文件中去
    json_file.write(json_str)
    json_file.close()

# 2: load json file

# json.load（）用于读取json数据
data4=json.load(open('class_indices.json'))

# type: dict
print(data4)  