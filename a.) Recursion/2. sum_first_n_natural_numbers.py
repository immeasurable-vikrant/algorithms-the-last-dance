# Define a function to calculate the sum of the first n natural numbers recursively.

def sum_first_n_natural_numbers(n):
    # Base case: If n is 1, return 1 (the sum of the first natural number).
    if n == 1: 
        return 1
    # Recursive case: Calculate the sum of the first n natural numbers by adding n to the sum of the first (n-1) natural numbers.
    return n + sum_first_n_natural_numbers(n - 1)

# Test the function with input 5.
print(sum_first_n_natural_numbers(5))
