# Define a function named sum_of_digits that takes a single argument 'num'
def sum_of_digits(num):
    # Base case: If 'num' is 0, return 0 (the sum of digits of 0 is 0)
    if num == 0:
        return 0
    # Recursive case:
    # Calculate the sum of the last digit of 'num' (num % 10) 
    # and call the sum_of_digits function recursively with the remaining digits (num // 10)
    return num % 10 + sum_of_digits(num // 10)

# Call the sum_of_digits function with an example number, 1234
print(sum_of_digits(1234))