import ast

def bond(ls):
    rows=len(ls)
    cols=len(ls[0])
    temp_ls=[]

    for i in range(cols):
        temp_ls.append(ls[0][i])

    for i in range(0,rows):
        if ls[i][cols-1] not in temp_ls:
            temp_ls.append(ls[i][cols-1])

    if rows>1:
        for i in range(cols-1,-1,-1):
            if ls[rows-1][i] not in temp_ls:
                temp_ls.append(ls[rows-1][i])

    if cols>1:
        for i in range(0,3):
            if ls[i][0] not in temp_ls:
                temp_ls.append(ls[i][0])

    print(temp_ls)

data=ast.literal_eval(input(""))
bond(data)