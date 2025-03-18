def mut_str(a,i):
    new_str=""
    for j in range(0,len(a)):
        if j==i:
            new_str+=""
        else:
            new_str+=a[j]
    print(new_str)
ab=input("Enter a string:")
ind=int(input("Enter a index:"))
mut_str(ab,ind)
