import pandas as pd
import json

with open('fres2_final_constructed1.txt', 'r') as fd:
    data_list = json.loads(fd.read())
    fd.close()

# print(data_list)

df = pd.DataFrame(data_list, columns=['entid', 'CaseType'])
df.to_csv('111.csv')
# res = pd.read_csv(r'D:\WechatDocument\WeChat Files\wxid_sh2f60h1a0l922\FileStorage\File\2021-07\fsdownload\Online_Data\test_data\test_data.csv')
# print(res.head())
# print(df)

# res['CaseType'] = ''
# print(res)
# for i, item in enumerate(res):
#     if 