a=[[1,2,3],[4,5,6],[7,8,9]]
new_ls=[]

for i in range(len(a)):
    sm=[]
    for j in range(len(a)-1,-1,-1   ):
        sm.append(a[j][i])
    new_ls.append(sm)
print(new_ls)