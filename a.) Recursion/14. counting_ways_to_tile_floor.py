"""
Given a floor of size m x n, where both m and n are positive integers and 2 ≤ m, 
count the number of ways to tile the given floor using 1 x n tiles. Each tile can 
either be placed horizontally or vertically. Your task is to determine the total 
number of unique ways to tile the entire floor.

Function Signature:
def count_ways_to_tile_floor(m: int, n: int) -> int:

Input:
- m (int): The number of rows of the floor (2 ≤ m)
- n (int): The number of columns of the floor

Output:
- int: The number of unique ways to tile the entire floor

"""
def count_ways_to_tile_floor(m: int, n: int) -> int:
    # Base cases
    if m < n:
        return 1
    if m == n:
        return 2
    
    # Recursive cases
    horizontally_positioned = count_ways_to_tile_floor(m - 1, n)
    vertically_positioned = count_ways_to_tile_floor(m - n, n)
    
    return horizontally_positioned + vertically_positioned

# Example usage:
print(count_ways_to_tile_floor(3, 2))  # Output should be 3
print(count_ways_to_tile_floor(4, 2))  # Output should be 5

        