#!/usr/bin/python

import sys
import random

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
		while (1):
			move = random.randint(0,8)
			if board[move] == 0 : break
		print move


if __name__ == "__main__": 
	main()
