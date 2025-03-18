from functools import reduce

lis=[1,2,3,4,5]
sum=reduce(lambda x,y: x+y, lis)
squ=list(map(lambda x: x**2, lis))
even=list(filter(lambda x:x%2==0, lis))

print("sum: ",sum," squ: ",squ," even: ",even)

def tempo(a,b=10,*argus,**kargus):
    print("")
    print("Positional: ",a)
    print(f"named: {b}")
    print("Variable-Length arguments:")
    for i in argus:
        print("  ",i)
    print("key arguments:")
    for i in kargus.items() :
        print("  ", i)
tempo(5)
tempo(1,b=6)
tempo(1,2,3,5,6,7,8)
tempo(1,2,34,7,56,key1=56,key2=45)