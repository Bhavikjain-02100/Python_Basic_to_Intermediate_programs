def optimized_bubble_sort(arr):
    n = len(arr)
    passes = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        passes += 1
        if not swapped:
            break
    return arr, passes

input_list = [5, 1, 4, 2, 8]
sorted_list, num_passes = optimized_bubble_sort(input_list)
print(f"Sorted list: {sorted_list}, {num_passes} passes")
