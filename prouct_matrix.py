a=[1,2,3,4]
res=[]
pro=1
for i in range(0,4):
    pro*=a[i]
for j in range(0,4):
    ans=int(pro/a[j])
    res.append(ans)
print(res)