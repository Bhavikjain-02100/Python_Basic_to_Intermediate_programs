import ast

def n_k(lst,k):
    n=len(lst)
    maxi=n//k
    dict={}
    temp_ls=[]
    for i in lst:
        dict[i] = dict.get(i, 0) + 1
    for i,count in dict.items():
        if count>maxi:
            temp_ls.append(i)
    return temp_ls if temp_ls else 0

data=ast.literal_eval(input(""))
print(n_k(data[0],data[1]))