"Fcatorial"

def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1) 
print(factorial(5))
# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)
# 1 * 1