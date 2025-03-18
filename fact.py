def fact(n):
    res=1
    count=n
    while(count>0):
        res=res*n
        n-=1
        count-=1
        print(res)
    
numb=int(input("enter the number:"))
fact(numb)

