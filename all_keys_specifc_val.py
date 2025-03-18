def key_by_values(d,ele):
    keys=[]
    for key, value in d.items():
        if value==ele:
            keys.append(key)
    return keys
dict={'a':1,'b':2,'c':1,'d':3}
val=1
print(key_by_values(dict,val))