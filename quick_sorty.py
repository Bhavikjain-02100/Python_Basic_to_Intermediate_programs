def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        p = arr[len(arr) // 2]
        left = [x for x in arr if x < p]
        middle = [x for x in arr if x == p]
        right = [x for x in arr if x > p]
        return quicksort(left) + middle + quicksort(right)

input_list = [3, 6, 8, 10, 1, 2, 1]
sorted_list = quicksort(input_list)
print(sorted_list)
