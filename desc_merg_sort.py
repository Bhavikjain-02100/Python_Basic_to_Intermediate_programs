def desc_merg(ls1,ls2):
    merge_ls=[]
    i,j=0,0
    while i<len(ls1) and j<len(ls2):
        if ls1[i]<ls2[j]:
            merge_ls.append(ls1[i])
            i+=1
        else:
            merge_ls.append(ls2[j])
            j+=1
    while i<len(ls1):
        merge_ls.append(ls1[i])
        i+=1
    while j<len(ls2):
        merge_ls.append(ls2[j])
        j+=1
    print(merge_ls)

list1=[7,5,3,1]
list2=[8,6,4,2]
desc_merg(list1,list2)