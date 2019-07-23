X = 9
A = 4
B = 2
P = 1


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

puzzle1 = [0 , 0, 0, A ,0], \
		  [X , 0, 0, 0 ,0], \
		  [P , B, 0, 0 ,0], \
		  [X , 0, 0, X ,0], \
		  [0 , 0, 0, 0 ,0]

p1 = Puzzle(puzzle1)
p1.prettyPrint()
print p1.playerPosition
