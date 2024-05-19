def sum_of_all_values_inside_array(nums, idx = 0):
        if(len(nums) == idx):
                return 0
        return nums[idx] + sum_of_all_values_inside_array(nums, idx + 1)

print(sum_of_all_values_inside_array([1, 2, 3, 4, 5]))
