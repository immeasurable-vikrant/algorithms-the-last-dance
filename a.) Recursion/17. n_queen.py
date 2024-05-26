import random

def is_safe(board, row, col):
    # Check left side for existing queens
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def n_queen(board, row):
    if row == len(board):
        return True
    
    for _ in range(len(board)):  # Loop for number of columns
        col = random.randint(0, len(board) - 1)  # Generate random column index
        if is_safe(board, row, col):
            board[row][col] = 1
            if n_queen(board, row + 1):
                return True
            board[row][col] = 0
    
    return False

def print_solution(board):
    for row in board:
        print(row)

# Example usage:
n = 4  # Size of the chessboard
board = [[0] * n for _ in range(n)]  # Initialize empty chessboard
if n_queen(board, 0):
    print_solution(board)
else:
    print("Solution does not exist")
