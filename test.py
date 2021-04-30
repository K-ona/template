def split_text_with_whitespace(text):
    res = []
    text = text.strip()

    tmp = ''
    for ch in text:
        if u'\u4e00' <= ch <= u'\u9fff' or ch == ' ' or ch == 'の':
            if tmp != '':
                res.append(tmp)
                tmp = ''
            res.append(ch)
        else:
            tmp += ch
    if tmp != '':
        res.append(tmp)

    return res

print(split_text_with_whitespace("玩狼人杀吗/你爱玩狼人杀   这个挺好玩的   狼人杀挺好玩的"))