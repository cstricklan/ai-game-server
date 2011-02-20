#!/usr/bin/python

import sys

title	= "TicTacToe"
version	= "0.9"

board   = [0,0,0,0,0,0,0,0,0]

# Check for a winning condition
# Return conditions:
#   0 = Game still playing
#   1 = Winner found
#   2 = Tie
def endOfGameCheck():
	# Tie
	if (board.count(0) == 0): return 2
	# Horizontal	
	for i in range(0,7,3):
		if ((board[0+i]!=0) & (board[0+i] == board[1+i]) & (board[1+i] == board[2+i])): return 1
	# Vertical
	for i in range(0,3):
		if ((board[0+i]!=0) & (board[0+i] == board[3+i]) & (board[3+i] == board[6+i])): return 1
	# Diagonal
	if ((board[0]!=0) & (board[0] == board[4] ) & (board[4] == board[8])): return 1
	if ((board[2]!=0) & (board[2] == board[4] ) & (board[4] == board[6])): return 1
		
	return 0

# Validate and process a player's move
def processMove(player,move):

	global board

	# Check for an invalid move...
	if ((move < 0) | (move > 8)): 		return 1
	if (board[move] != 0): 			return 1
	if ((player != 1) & (player != 2)): 	return 1

	# Make the move now that everything has been validated...
	board[move] = player;

	# Print the game board
	print board	
	return 0;

# Main game loop
def main(argv):

	# Validate the command line...
	if (len(sys.argv) != 3):
		sys.exit("ERROR: Two player bots must be specified!")

	# Print the game header and start the game...
	print "%s(%s) -  %s(X) vs %s(O)" % (title, version, sys.argv[1], sys.argv[2])
	print board
	
	# Process moves until the game is over... 
	player = 0; endstate = 0
	while ( not endstate ):
		move = int(input())
		if (player == 1): player = 2
		else: player = 1
		if ( processMove(player,move) == 1 ): endstate = 3
		endstate = endOfGameCheck()

	# Game is over, print the results...
	if   endstate == 1: print("%dW") % (player)	# Somebody won
	elif endstate == 2: print("0")			# Tie
	elif endstate == 3: print("%dF") % (player)	# Tomfoolery
	else: print("Somebody crossed the beams...Time to panic!")

if __name__ == "__main__": 
	main(sys.argv[1:])
