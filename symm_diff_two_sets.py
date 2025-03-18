def symm_diff(set1, set2):
    return set1 ^ set2

set1 = {1, 2, 3}
set2 = {2, 3, 4, 5}
result = symm_diff(set1, set2)
print(result)
