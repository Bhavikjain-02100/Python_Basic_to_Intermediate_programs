def uni(ls):
    temp_ls=[]
    for i in range(0,len(ls)):
        if ls[i] in temp_ls:
            i+=1
        else:
            temp_ls.append(ls[i])
    print(len(temp_ls))

lis=[1,2,3,4,4,5]
uni(lis)