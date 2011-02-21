#!/usr/bin/python

import sys

DEBUG = 0

# Keep track of player id
player = 0

# Determine if a player is one move from victory
# Returns	(player,winning_move)
#		(0,0)	if nobody is about to win
#		(1,x)	if next move is a win for us
#		(2,x)	if next move is a win for them 
def nextMoveWin(board):
	# Define all winning vectors
	winVec = [ [0,1,2],[3,4,5],[6,7,8],	# Horizontal
		   [0,3,6],[1,4,7],[2,5,8],	# Vertical
		   [0,4,8],[2,4,6] ]		# Diagonal

	# Be sure to check for all possible good guy victories before checking losses
	for x in winVec:
		y = (board[x[0]]), (board[x[1]]), (board[x[2]])
		if y.count(0) == 1:
			if (y.count(player) == 2): return (1,x[y.index(0)])
	for x in winVec:
		y = (board[x[0]]), (board[x[1]]), (board[x[2]])
		if y.count(0) == 1:
			if (y.count(player) == 0): return (2,x[y.index(0)])

	# Nothing exciting happening...
	return (0,0) 

# Determine the value of taking the specified square
def rateSquare(pos,board):
	
	# Don't bother if the square is already taken
	if board[pos] != 0: return -9

	# Find all the related squares to determine value
	vec = []
	if   pos == 0: vec = [1,2,3,6,4,8]
	elif pos == 1: vec = [0,2,4,7]
	elif pos == 2: vec = [0,1,5,8,4,6]
	elif pos == 3: vec = [0,6,4,5]	
	elif pos == 4: vec = [0,1,2,3,5,6,7,8]	
	elif pos == 5: vec = [2,8,3,4]
	elif pos == 6: vec = [0,3,7,8,2,4]	
	elif pos == 7: vec = [6,8,1,4]	
	elif pos == 8: vec = [0,4,2,5,6,7]	
	else: print ("Invalid position requested (%d)") % (pos)

	# Calculate the score based using the related squares
	score = 0
	for x in vec:
		if   board[x] == 0: continue
		elif board[x] == player: score += 1
		else: score -= 1
	return score

# Determine the square values on the board
def rateBoard(board):
	vec = [0,0,0,0,0,0,0,0,0]
	for i in range(0,9):
		vec[i] = rateSquare(i,board)
	if DEBUG: 
		print "Score Vector: "
		print vec
	return vec.index(max(vec))

# Select and return the best available move
def chooseMove(board):

	# Check for a victory on next move...
	check = nextMoveWin(board)
	if DEBUG: print "Next Move Win Check: %d at %d" % (check[0], check[1])
	if (check[0] == 1): return check[1]
	if (check[0] == 2): return check[1]
	
	# Always choose the middle if it's available...
	if board[4] == 0: return 4

	# No forced move, so just pick a good one	
	return rateBoard(board)

# Main game loop
def main():
	global player
	while (1):
		
		# Read board, exit if game is over
		board = input()
		try: 
			if (len(board) != 9): break
		except TypeError: 
			break

		# Identify our player id if it hasn't already been set
		if player == 0:
			if board.count(1) == 0:	player = 1
			else:			player = 2

		# Choose a new random location and issue the move
		print chooseMove(board)

if __name__ == "__main__": 
	main()
