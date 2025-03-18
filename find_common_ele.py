def find_common_element(ls1,ls2):
    res_ls=[]
    for i in ls1:
        if i in ls2:
            res_ls.append(i)
    print(res_ls)

lis1=[1,2,3,4]
lis2=[3,4,5,6]
find_common_element(lis1,lis2)