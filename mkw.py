lst={'a':10,'b':20,'c':'ht'}
sum=0
for j in lst.values():
    if str(j).isnumeric():
        sum+=j
    else:
        print("Value false")
print(sum)