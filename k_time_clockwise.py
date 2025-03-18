import ast

def k_cl(ls, k):
    for f in range(k):
        temp_ls = []
        for i in range(len(ls[0])):
            sm = []
            for j in range(len(ls) - 1, -1, -1):
                sm.append(ls[j][i])
            temp_ls.append(sm)
        ls = temp_ls
    print(ls)
# k_cl([[1,2,3],[4,5,6],[7,8,9]],2)
data = ast.literal_eval(input(""))
k_cl(data[0], data[1])
