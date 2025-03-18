def find_mode(ls):
    ls.sort()
    dict={}
    for i in ls:
        temp=ls.count(i)
        dict[i]=temp
    max_f=max(dict.values())
    max_items=[]
    for k, v in dict.items():
        if v==max_f:
            max_items.append(k)
    if len(max_items)>1:
        res=ls[0]
    else:
        res=max(dict,key=dict.get)
    print(res)

lis=[1,1,3,3,3,7,7,7,9,9]
find_mode(lis)