'''Given an array of numbers, write a recursive function to determine if the array is 
sorted in non-decreasing order. The function should return True if the array is sorted, 
and False otherwise.'''


def is_array_sorted(nums, idx=1):
    # Base case: if we have checked all elements, the array is sorted
    if idx == len(nums):
        return True
    
    # If the current element is smaller than the previous, array is not sorted
    if nums[idx] < nums[idx - 1]:
        return False
    
    # Recursively check the next element
    return is_array_sorted(nums, idx + 1)

# Test cases
print(is_array_sorted([1, 8, 10, 23, 10]))  # Output: False
print(is_array_sorted([1, 2, 3, 4, 5]))     # Output: True
print(is_array_sorted([10, 20, 30]))        # Output: True
print(is_array_sorted([5, 4, 3, 2, 1]))     # Output: False