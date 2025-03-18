def remove_list(n):
    lst=[1,2,3,3,4,5]
    print(lst.index(2))
    for i in lst:
        if n in lst:
            lst.remove(n)
    print(lst)
inp=int(input("Enter any number from first five natural number:`"))
remove_list(inp)