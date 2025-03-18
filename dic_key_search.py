def key_search(d,key):
    if k in d:
        return d[key]
    else:
        return 'key not found'
dict={'name': 'Alice', 'age': 25, 'city': 'New York'}
k='country'
print(key_search(dict,k))