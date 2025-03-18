def modify_tuple(t, num):
    lst = list(t)
    lst.append(num)
    return tuple(lst)

tup= (1, 2, 3, 4)
mod_num= 5
new = modify_tuple(tup, mod_num)
print(f"Original tuple: {tup}")
print(f"New tuple: {new}")
