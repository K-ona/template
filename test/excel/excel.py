from typing import Pattern
import xlrd as xd
from xlutils.copy import copy

# find all substr indices of str
def find_all_substr(str, sub):
    sub_index = [-1]
    while str.find(sub, sub_index[-1] + 1) != -1:
        sub_index.append(str.find(sub, sub_index[-1] + 1))

    return sub_index[1:]

path = 'test/excel/test.xls'
target_path = 'test/excel/target.xls'

filedata = xd.open_workbook(path)

print(str(filedata.sheet_names()))

data = filedata.sheet_by_index(0)

Wb = copy(filedata)
target_file = Wb.get_sheet(0)

nrows = data.nrows
ncols = data.ncols
print(nrows, ncols)

# for i in range(ncols):
#     print(i,data.col_values(colx=i,start_rowx=0, end_rowx=2))

pattern = ['url redirect', '©', '<IMAGE SRC', '>']

for i in range(100):
    row_content =  data.row_values(rowx=i)
    content = row_content[5]
    # url redirect
    if content.find(pattern[0]) != -1:
        print('url redirect: ', content)
        continue
    # only copyright
    elif content.find(pattern[1]) < 5 and content.find(pattern[1]) > -1:
        print('only copyright', content)
        continue
    # has img
    elif content.find(pattern[2]) != -1:
        start_ind = find_all_substr(content, pattern[2])
        for start in start_ind:
            if content.find(pattern[3], start) != -1:
                content = content[0:start] + content[content.find(pattern[3], start):]
        print('without img: ', content)
    # content with copyright
    elif content.find(pattern[1]) != -1:
        content = content[0:content.find(pattern[1])]
        print('without copyright: ', content)

    for j in range(ncols):
        target_file.write(i, j, row_content[j])
    target_file.write(i, 5, content)
    print('write data into file line is {}, modified data is : {}'.format(i, content))

Wb.save(target_path)
