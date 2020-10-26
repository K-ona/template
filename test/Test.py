from ltp import LTP
from os import mkdir, path
from stanfordcorenlp import StanfordCoreNLP as SCNLP

import json
import langid
import xlrd as xd
import xlwt
import re
import time

# 参数为模型所在文件夹
nlp_ch = LTP(r'D:\Data\base')
nlp_en = SCNLP(r'D:\Python\stanford-corenlp-4.1.0')

source_path = path.join('excel', 'test_speed.xls')
print(source_path)

file = xd.open_workbook(source_path)
filedata = file.sheet_by_index(0)

nrows = filedata.nrows
ncols = filedata.ncols
print("nrows = {}, ncols = {}".format(nrows, ncols))

t1 = time.perf_counter()

# tmp
filename = 'test'

data_zh = []
targetzhfile_path = 'target/zh'
data_en = []
targetenfile_path = 'target/en'

for row in range(nrows)[1:]:
    row_content = filedata.row_values(rowx = row)
    content = row_content[5]

    # not en or zh
    if langid.classify(content)[0] == 'zh':
        seg, hidden = nlp_ch.seg([content])
        pos = nlp_ch.pos(hidden)
        dep = nlp_ch.dep(hidden)[0]
        data_zh.append(dep)
        print('nlp with Chinese')
    else :
        dep = nlp_en.dependency_parse(content)
        data_en.append(dep)
        print('nlp with English')

    print('file : row = {}'.format(row))
    
data_zh = json.dumps(data_zh)
data_en = json.dumps(data_en)

if not path.exists(targetzhfile_path):
    mkdir(targetzhfile_path)
    with open(path.join(targetzhfile_path, filename + '.txt'), 'w') as fd:
        for str in data_zh:
            fd.write(str)
        fd.close()

if not path.exists(targetenfile_path):
    mkdir(targetenfile_path)
    with open(path.join(targetenfile_path, filename + '.txt'), 'w') as fd:
        for str in data_en:
            fd.write(str)
        fd.close()

print((time.perf_counter()-t1) / 60)