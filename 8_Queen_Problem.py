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
 
