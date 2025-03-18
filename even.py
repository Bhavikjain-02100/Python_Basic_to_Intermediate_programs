def even(n):
    num=0
    res=0
    while(num<n):
        num+=1
        if(num%2==0):
            res=res+num
            print(num,"+")
    print(res)
numb=int(input("Enter the number: "))
even(numb)
