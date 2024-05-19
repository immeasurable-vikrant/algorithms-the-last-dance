"""
Sum of First n natural numbers
"""

# I/P - 5
# O/P - 1 + 2 + 3 + 4 + 5

def sum_first_n_natural_numbers(n):
    if n == 1: 
        return 1
    return n + sum_first_n_natural_numbers(n - 1)
print(sum_first_n_natural_numbers(5))