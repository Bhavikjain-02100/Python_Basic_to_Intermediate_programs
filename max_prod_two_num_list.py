def max_product(nums):
    if len(nums) < 2:
        return None
    nums.sort(reverse=True)
    return max(nums[0] * nums[1], nums[-1] * nums[-2])

input_list = [1, 5, 3, 7, 9]
result = max_product(input_list)
print(result)
