s = '’s minister is'
tmp = ''
for c in s:
    if 'a' < c < 'z' or 'A' < c < 'Z':
        tmp += c
    else:
        tmp += '_'

print(tmp)