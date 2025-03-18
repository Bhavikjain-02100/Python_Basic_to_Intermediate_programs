def miss_val(ls):
    temp_ls=[]
    start=ls[0]
    while start<=ls[-1]:
        temp_ls.append(start)
        start+=1

    for i in temp_ls:
        if i not in ls:
            print(i)

lis=[1,2,3,5]
miss_val(lis)
