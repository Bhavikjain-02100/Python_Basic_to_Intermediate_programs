import ast

def poss(lst, n):
    def combo(c_val, start):
        if len(c_val)==n:
            result.append(c_val[:])
            return
        for i in range(start, len(lst)):
            c_val.append(lst[i])
            combo(c_val, i + 1)
            c_val.pop()
    result=[]
    combo([], 0)
    print(result)

data=ast.literal_eval(input(""))
poss(data[0],data[1])