def fun(lst,find):
    indices=[]
    start=0
    for _ in range(0,7):
        ind=lst.index(find,start)
        indices.append(ind)
        start+=1
    print(indices) #if indices else None
lis=[1,2,3,2,5,4,2,6]
f=2
fun(lis,f)