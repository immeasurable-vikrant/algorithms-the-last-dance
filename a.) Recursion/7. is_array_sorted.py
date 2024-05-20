def is_array_sorted(nums, idx = 1):
        if idx == len(nums):
                return
        if nums[idx] < nums[idx - 1]:
                return False

        is_array_sorted(nums, idx + 1)
        return True
        
print(is_array_sorted([1, 8, 10, 23, 10])) 