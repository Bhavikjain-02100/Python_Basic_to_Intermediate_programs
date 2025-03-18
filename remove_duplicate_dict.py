lis=[{"a":1},{"b":2},{"a":1},{"c":3}]

def remove_duplicate_dicts(ls):
    temp_ls=[]
    for i in ls:
        if i not in temp_ls:
            temp_ls.append(i)
    print(temp_ls)

remove_duplicate_dicts(lis)