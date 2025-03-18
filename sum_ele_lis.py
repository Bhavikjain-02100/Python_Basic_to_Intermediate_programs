import ast
def sum_l(ls):
    res=0
    temp_ls=[]
    for i in ls:
        res+=i
        temp_ls.append(res)
    print(temp_ls)

data=ast.literal_eval(input(""))
sum_l(data)