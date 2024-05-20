def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1

    # Recursive case: return n multiplied by the result of factorial of n - 1
    return n * factorial(n - 1) 

# Test the function with an example input
print(factorial(5))


# Output: 120 (5 * 4 * 3 * 2 * 1)

# Code Comments:
# The factorial function calculates the factorial of a given non-negative integer.
# It uses recursion to compute the factorial.
# - Base Case: If n is 0 or 1, the factorial is 1.
# - Recursive Case: For any other value of n, it returns n multiplied by the factorial of (n - 1).
#   This process continues until the base case is reached.
# The function is then tested with an example input (factorial(5)) to verify its correctness.
