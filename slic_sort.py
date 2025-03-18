lst=['may','a','peace']
for i in range(len(lst)):
    for j in range(len(lst)):
        if( len(lst[i])>len(lst[j])):
            lst[i],lst[j]=lst[j],lst[i]
print(lst)

