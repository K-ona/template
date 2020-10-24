from typing import Pattern
import xlrd as xd
import xlwt
import langid
import os
from os import path
import re

# find all substr indices of str
def find_all_substr(str, sub):
    sub_index = [-1]
    while str.find(sub, sub_index[-1] + 1) != -1:
        sub_index.append(str.find(sub, sub_index[-1] + 1))

    return sub_index[1:]

source_path = 'test/excel/1.xls'
target_path = 'test/excel/target/1.xls'

filedata = xd.open_workbook(source_path)
print(str(filedata.sheet_names()))

data = filedata.sheet_by_index(0)

Wb = xlwt.Workbook()
target_file = Wb.add_sheet('data')

nrows = data.nrows
ncols = data.ncols
print(nrows, ncols)

# for i in range(ncols):
#     print(i,data.col_values(colx=i,start_rowx=0, end_rowx=2))

pattern = ['url redirect', '©', 'IMAGE SRC', '>']

row = 0
for i in range(nrows):
    row_content =  data.row_values(rowx=i)
    content = row_content[5]
    # url redirect
    if content.find(pattern[0]) != -1:
        # print('url redirect: ', content)
        continue
    # only copyright
    elif content.find(pattern[1]) < 5 and content.find(pattern[1]) > -1:
        # print('only copyright', content)
        continue
    # has img
    elif content.find(pattern[2]) != -1:
        content = re.sub(r'<?IMAGE SRC.*>?', '', content)
           
        # print('without img: ', content)
    # content with copyright
    elif content.find(pattern[1]) != -1:
        content = content[0:content.find(pattern[1])]
        # print('without copyright: ', content)
    # not en or zh
    elif langid.classify(content)[0] != 'en' and langid.classify(content)[0] != 'zh':
        continue

    for j in range(ncols):
        if j == 5:
            target_file.write(row, j, content)
        else:   
            target_file.write(row, j, row_content[j])
    
    row += 1
    # print('write data into file line is {}, modified data is : {}'.format(i, content))
print('row == {}'.format(row))
Wb.save(target_path)