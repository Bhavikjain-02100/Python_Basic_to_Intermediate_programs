def permutations(arr):
    if len(arr) == 1:
        return [arr]
    perms = []
    for i in range(len(arr)):
        m = arr[i]
        rem_lst = arr[:i] + arr[i + 1:]
        for p in permutations(rem_lst):
            perms.append([m] + p)
    return perms

input_list = ['a', 'b', 'c']
result = permutations(input_list)
result = [tuple(p) for p in result]
print(result)
