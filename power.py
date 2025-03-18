def power(b,e):
    i=1
    res=b
    while(i<e):
        res=res*b
        i=i+1
    print(res)

num=int(input("enter the base number:"))
exp=int(input("Enter the exponent:"))
power(num,exp)
        
        
