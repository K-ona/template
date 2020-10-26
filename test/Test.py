from ltp import LTP
from os import path
import langid
import xlrd as xd
import xlwt
import re
import time

ltp = LTP(r'D:\Data\base')
source_path = path.join('excel', 'test_speed.xls')
print(source_path)

file = xd.open_workbook(source_path)

filedata = file.sheet_by_index(0)

nrows = filedata.nrows
ncols = filedata.ncols
print("nrows = {}, ncols = {}".format(nrows, ncols))

pattern = ['url redirect', '©', 'IMAGE SRC', '>']

t1 = time.perf_counter()
for row in range(nrows):
    row_content = filedata.row_values(rowx = row)
    content = row_content[5]

    # not en or zh
    if langid.classify(content)[0] != 'en' and langid.classify(content)[0] != 'zh':
        continue
    # url redirect
    if content.find(pattern[0]) != -1:
        # print('url redirect: ', content)
        continue
    # only copyright
    if content.find(pattern[1]) < 5 and content.find(pattern[1]) > -1:
        # print('only copyright', content)
        continue
    # has img or other html labels
    if content.find(pattern[2]) != -1:
        content = re.sub(r'<?IMAGE SRC.*>?', '', content)
        content = re.sub(r'<.*>', '', content)
        # print('without img: ', content)
        
    # content with copyright
    if content.find(pattern[1]) != -1:
        content = content[0:content.find(pattern[1])]
        # print('without copyright: ', content)

    seg, hidden = ltp.seg([content])
    pos = ltp.pos(hidden)
    dep = ltp.dep(hidden)
print((time.perf_counter()-t1) / 60)