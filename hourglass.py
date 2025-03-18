def patt(n):
    start=1
    spaces=n//2
    for i in range(0,n+1):
        for k in range(0,spaces):
            print(" ",end="")
        for j in range(0,start):
            print("*",end=" ")
        print(" ")
    if i<(n//2):
        spaces-=1
        start+=1
    else:
        spaces+=1
        start-=1
num=int(input("Enter a numbr:"))
patt(num)
