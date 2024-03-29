import copy
from slideUtils import *


class Puzzle:

	def __init__(self, board):
		
		if not isinstance(board, list) or len(board) == 0:
		 	raise ValueError("Give me a board, doofus")
		self.playerPosition = (-1,-1)
		self.board = board
		for row, line in enumerate(self.board):
			for col, cell in enumerate(line):
				if cell == P:
					self.playerPosition = (row, col)
					break
			if not self.playerPosition == (-1, -1):
				break
		self.rows = len(board)
		self.cols = len(board[0])

		self.initBoard = copy.deepcopy(self.board)
		self.initPlayerPos = self.playerPosition
		self.moveCount = 0

	def reset(self):
		self.board = copy.deepcopy(self.initBoard)
		self.playerPosition = self.initPlayerPos
		self.moveCount = 0

	def prettyPrint(self):
		borderString = "--"
		for _ in range(self.cols):
			borderString += "--"

		print borderString
		for line in self.board:
			lineString = "|"
			for cell in line:
				if cell == X:
					lineString += "X "
				elif cell == B:
					lineString += "B "
				elif cell == A:
					lineString += "A "
				elif cell == P:
					lineString += "P "
				else:
					lineString += ". "
			lineString += "|"
			print lineString
		print borderString

	def outOfBounds(self, position):
	 	if (position[0] < 0 or position[0] >= self.rows) or (position[1] < 0 or position[1] >= self.cols):
	 		return True

	def isOpen(self, position):
		r = position[0]
		c = position[1]
		return not self.outOfBounds(position) and (self.board[r][c] == 0 or  self.board[r][c] == A)

	def moveObject(self, origPosition, direction, isPlayer = False):
		currentCell = origPosition
		adjCell = (currentCell[0] + direction[0], currentCell[1] + direction[1])
		moved = False
		while self.isOpen(adjCell):
			currentCell = adjCell
			if (self.board[currentCell[0]][currentCell[1]] == A and isPlayer):
				print "You Win!"
				self.board[currentCell[0]][currentCell[1]] = self.board[origPosition[0]][origPosition[1]]
				self.board[origPosition[0]][origPosition[1]] = 0
				self.moveCount += 1
				return (True, True)
			adjCell = (currentCell[0] + direction[0], currentCell[1] + direction[1])
		if not currentCell == origPosition:
			self.board[currentCell[0]][currentCell[1]] = self.board[origPosition[0]][origPosition[1]]
			self.board[origPosition[0]][origPosition[1]] = 0
			moved = True
			self.moveCount +=1
		if (isPlayer):
			self.playerPosition = currentCell
		return (False, moved)


	def movePlayer(self, direction):
		adjCell = (self.playerPosition[0] + direction[0], self.playerPosition[1] + direction[1])
	 	if self.outOfBounds(adjCell):
	 		return (False, False)
	 	elif self.board[adjCell[0]][adjCell[1]] == B:
	 	 	return self.moveObject(adjCell, direction)
	 	else:
	 		return self.moveObject(self.playerPosition, direction, True)

print



# # push block to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player up to the goal
# p1.movePlayer(UP)
# p1.prettyPrint()

print "Pick a board 0 - " + str(len(boards) - 1) + ":"
boardNum = raw_input()

board = boards[int(boardNum)]

puzzle = Puzzle(board)
puzzle.prettyPrint()
print

finished = False

while not finished:
	direction = None
	inp = raw_input()
	if inp == 'a':
		direction = LEFT
	elif inp == 'd':
		direction = RIGHT
	elif inp == 's':
		direction = DOWN
	elif inp == 'w':
		direction = UP
	elif inp == 'q':
		finished = True
	elif inp == 'r':
		puzzle.reset()
		print "RESET"
	
	if direction:
		finished, moved = puzzle.movePlayer(direction)
		if moved:
			print directionToString(direction)
		else:
			print "No move"

	puzzle.prettyPrint()
	print "Moves: " + str(puzzle.moveCount)

	print

