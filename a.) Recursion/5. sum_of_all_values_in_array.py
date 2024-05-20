def sum_of_all_values_inside_array(nums, idx=0):
    # Base case: If idx has reached the length of the array, return 0
    if len(nums) == idx:
        return 0
    
    # Recursive case:
    # Return the sum of the current element and the sum of the rest of the elements
    return nums[idx] + sum_of_all_values_inside_array(nums, idx + 1)

# Test the function with an example array [1, 2, 3, 4, 5]
print(sum_of_all_values_inside_array([1, 2, 3, 4, 5]))

