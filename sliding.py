X = 9
A = 4
B = 2
P = 1

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

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

	def prettyPrint(self):
		for line in self.board:
			print line
		print 

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
		while self.isOpen(adjCell):
			currentCell = adjCell
			if (self.board[currentCell[0]][currentCell[1]] == A and isPlayer):
				print "You Win!"
				self.board[currentCell[0]][currentCell[1]] = self.board[origPosition[0]][origPosition[1]]
				self.board[origPosition[0]][origPosition[1]] = 0
				return True
			adjCell = (currentCell[0] + direction[0], currentCell[1] + direction[1])
		if not currentCell == origPosition:
			self.board[currentCell[0]][currentCell[1]] = self.board[origPosition[0]][origPosition[1]]
			self.board[origPosition[0]][origPosition[1]] = 0
		if (isPlayer):
			self.playerPosition = currentCell
		return False


	def movePlayer(self, direction):
		adjCell = (self.playerPosition[0] + direction[0], self.playerPosition[1] + direction[1])
	 	if self.outOfBounds(adjCell):
	 		return
	 	elif self.board[adjCell[0]][adjCell[1]] == B:
	 	 	return self.moveObject(adjCell, direction)
	 	else:
	 		return self.moveObject(self.playerPosition, direction, True)

print

puzzle1 = [[0 , 0, 0, A ,0], \
		  [X , 0, 0, 0 ,0], \
		  [P , B, 0, 0 ,0], \
		  [X , 0, 0, X ,0], \
		  [0 , 0, 0, 0 ,0]]

p1 = Puzzle(puzzle1)
p1.prettyPrint()

# # push block to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player up to the goal
# p1.movePlayer(UP)
# p1.prettyPrint()

finished = False

while not finished:
	direction = None
	inp = raw_input()
	if inp == 'A':
		direction = LEFT
	elif inp == 'D':
		direction = RIGHT
	elif inp == 'S':
		direction = DOWN
	elif inp == 'W':
		direction = UP
	elif inp == 'Q':
		finished = True
	
	if direction:
		finished = p1.movePlayer(direction)
		p1.prettyPrint()


