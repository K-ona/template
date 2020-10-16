def find_all_substr(str, sub):
    sub_index = [-1]
    while str.find(sub, sub_index[-1] + 1) != -1:
        sub_index.append(str.find(sub, sub_index[-1] + 1))

    return sub_index[1:]

print(find_all_substr('sdadsadasdsadsagdgd', 'a'))