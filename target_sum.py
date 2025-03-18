import ast

def pair_sum(ls,target_sum):
    s=set()
    p=set()
    for i in ls:
        j=target_sum-i
        if j in s:
            p.add((min(i,j),max(i,j)))
        s.add(i)
    return len(p)

data=ast.literal_eval(input(""))
pair_sum(data)