'''
Write a function to compute the nth Fibonacci number using a recursive approach. 
The Fibonacci sequence is defined as follows:

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1

'''
def nthFibonacci(n):
    # Base case: if n is 0, the Fibonacci number is 0
    if n == 0: 
        return 0
    
    # Base case: if n is 1, the Fibonacci number is 1
    if n == 1: 
        return 1

    # Recursive case: return the sum of the previous two Fibonacci numbers
    return nthFibonacci(n - 1) + nthFibonacci(n - 2)

# Example test case: Calculate the 6th Fibonacci number
print(nthFibonacci(6))  # Output should be 8
