def find_index(lst, element):
    return [i for i, x in enumerate(lst) if x == element] or None

list = [1, 2, 3, 2, 4, 2, 5]
element= 2
print(find_index(list, element))
