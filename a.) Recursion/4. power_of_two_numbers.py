def pow(n, m):
    # Base case: if m is 0, return 1 (any number raised to power 0 is 1)
    if m == 0:
        return 1
    # Recursive case: multiply n by pow(n, m - 1) to compute n^m
    return n * pow(n, m - 1)

# Test the function
print(pow(2, 4))  # Output: 16
