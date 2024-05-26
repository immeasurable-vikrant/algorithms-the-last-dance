def unique_path(m, n, i = 0, j = 0):
        if i == m - 1 or j == n - 1:
                return 1
        if i == m or j == n:
                return 0
        
        rightMovement = unique_path(m, n, i, j + 1)
        downMovement = unique_path(m, n, i + 1, j)
        
        return rightMovement + downMovement

# m = 0
# n = 0
# m = 3
# n = 3

print(unique_path(m , n))