lis=[[1,2,3],[4,5,6],[7,8,9]]
temp_ls=[]
j=0
while j<len(lis):
    for i in range(len(lis)-1,-1,-1):
        temp_ls.append(lis[i][j])
        j+=1

print(temp_ls)