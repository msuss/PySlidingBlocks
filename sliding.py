import copy

X = 9
A = 4
B = 2
P = 1

LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)

board0 = [[0 , 0, 0, 0, A ,0], \
		  [X , 0, 0, 0, 0 ,0], \
		  [P , B, 0, 0, 0 ,0], \
		  [X , 0, 0, 0, X ,0], \
		  [0 , 0, 0, 0, 0 ,0]]

board1 = [[0 , 0, 0, X, 0 ,0], \
		  [X , 0, 0, X, B ,A], \
		  [P , B, 0, 0, 0 ,0], \
		  [X , 0, 0, 0, X ,X], \
		  [0 , 0, 0, 0, 0 ,0]]

board2 = [[0 , 0, 0, 0, 0 ,0], \
		  [X , 0, A, 0, 0 ,X], \
		  [P , B, 0, 0, 0 ,0], \
		  [0 , 0, 0, 0, 0 ,X], \
		  [0 , 0, X, 0, 0 ,0]]

board3 = [[0 , 0, 0, 0, 0 ,0], \
		  [X , 0, 0, 0, A ,0], \
		  [P , 0, 0, 0, 0 ,0], \
		  [0 , B, 0, 0, 0 ,B], \
		  [X , X, X, 0, 0 ,0]]

board4 = [[0 , 0, 0, 0, 0, X, 0, 0, 0, 0], \
		  [0 , 0, A, 0, 0, 0, 0, X, 0, X], \
		  [0 , 0, 0, X, 0, 0, 0, 0, 0, 0], \
		  [P , 0, 0, 0, B, 0, 0, 0, X, 0], \
		  [0 , 0, 0, 0, 0, 0, 0, 0, 0, 0], \
		  [0 , 0, 0, 0, 0, 0, 0, 0, X, 0], \
		  [0 , 0, 0, 0, X, 0, X, 0, 0, 0]]

board5 = [[0 , 0, 0, 0, X, 0, 0, 0, 0, 0], \
		  [0 , 0, 0, 0, 0, 0, 0, X, 0, X], \
		  [0 , 0, 0, X, 0, 0, 0, 0, 0, 0], \
		  [P , 0, 0, 0, B, 0, 0, 0, X, 0], \
		  [0 , 0, 0, 0, 0, X, 0, 0, 0, 0], \
		  [0 , 0, 0, 0, 0, 0, 0, 0, X, 0], \
		  [X , 0, 0, 0, X, A, X, 0, 0, 0]]

boards = [board0, board1, board2, board3, board4, board5]

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

	def reset(self):
		self.board = copy.deepcopy(self.initBoard)
		self.playerPosition = self.initPlayerPos

	def prettyPrint(self):
		for line in self.board:
			lineString = ""
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
			print lineString
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



# # push block to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player to the right
# p1.movePlayer(RIGHT)
# p1.prettyPrint()

# #move player up to the goal
# p1.movePlayer(UP)
# p1.prettyPrint()

boardNum = raw_input()

board = boards[int(boardNum)]

puzzle = Puzzle(board)
puzzle.prettyPrint()

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
	
	if direction:
		finished = puzzle.movePlayer(direction)
	puzzle.prettyPrint()

