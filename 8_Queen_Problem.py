from __future__ import print_function
N = 8
left_diagonal = [0] * 30
right_diagonal = [0] * 30
column = [0] * 30

def print_Solution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j], end = " ")
		print()
 
def solve_8_Queen_Util(board, col):
    if (col >= N):
        return True
    for i in range(N):
        if ((left_diagonal[i - col + N - 1] != 1 and right_diagonal[i + col] != 1) and column[i] != 1):
            board[i][col] = 1
            left_diagonal[i - col + N - 1] = right_diagonal[i + col] = column[i] = 1
            if (solve_8_Queen_Util(board, col + 1)):
                return True
            board[i][col] = 0 
            left_diagonal[i - col + N - 1] = right_diagonal[i + col] = column[i] = 0
            return False

def solve_8_Queen():
	board = [[0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
	         [0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0]]
	if (solve_8_Queen_Util(board, 0) == False):
		print_function("Solution does not exist")
		return False
	print_Solution(board)
	return True
solve_8_Queen()

