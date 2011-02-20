#!/usr/bin/python

import sys
import random

def chooseMove(board):

	# Always choose the middle if it's available...
	if board[4] == 0: return 4

# Main game loop
def main():

	random.seed()

	while (1):
		
		# Read board, exit if game is over
		board = input()
		try: 
			if (len(board) != 9): break
		except TypeError: 
			break

		# Choose a new random location and issue the move
		print chooseMove(board)


if __name__ == "__main__": 
	main()
