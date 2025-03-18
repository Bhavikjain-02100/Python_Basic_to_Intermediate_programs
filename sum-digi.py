def add_d(n):
    while(n>=10):
        n=sum(int(digits) for digits in str(n))
    return n
numb=int(input("enter the number:"))
res=add_d(numb)
print(res)
