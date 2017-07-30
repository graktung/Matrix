class Matrix:
	'''
	CREATE MATRIX
	- To create a Matrix
		matrix = Matrix([values in row 1], [values in row 2])
	Note:
		- Rows must be list
		- Not require the same width of the rows,
		the shorter rows will be filled by zero tails
	- To create an empty Matrix
		matrix = Matrix([])
	GET VALUE MATRIX
		matrix[rows, column]
		also support slicing
	'''
	def __init__(self, *matrix):
		self.matrix = []
		try:
			if len(matrix) == 1 and matrix[0] == []:
				self.shape = (0, 0)
			else:
				# (numRow, numColumn)
				self.shape  = (len(matrix), len(max(matrix, key=len)))
		except TypeError:
			raise TypeError('Type of row must be list')
		for row in matrix:
			if not(isinstance(row, list)):
				raise TypeError("Type of row must be list not %r" %(type(row).__name__))
			if not(len(row) < self.shape[1]):
				self.matrix.append(row)
			else:
				# generate zero tail [1, 2] + [0, 0] to balance width
				self.matrix.append(row + [0] * (self.shape[1] - len(row)))
	def __repr__(self):
		'''format follow by
		Matrix ROWxCOLUMN
		[X, X, X]
		[X, X, X]
		[X, X, X]
		'''
		result = 'Matrix %dx%d\n' %(self.shape[0], self.shape[1])
		for row in self.matrix[:-1]:
			result += str(row) + '\n'
		result += str(self.matrix[-1])
		return result
	def __str__(self):
		'''format follow by
		[X, X, X]
		[X, X, X]
		[X, X, X]
		'''
		result = ''
		for row in self.matrix[:-1]:
			result += str(row) + '\n'
		result += str(self.matrix[-1])
		return result
	def __len__(self):
		# return the number of rows
		return self.shape[0]
	def __getitem__(self, index):
		# [index] or [index:index]
		if not isinstance(index, tuple):
			idx, idxx = index, None
		else:
			idx, idxx = index
		# first pick
		if isinstance(idx, int):
			try:
				result = [self.matrix[idx]]
			except IndexError:
				raise IndexError('Matrix index out of range')
		# or first slice
		elif isinstance(idx, slice):
			if self.matrix[idx] == []:
				result = [[]]
			else:
				result = self.matrix[idx]
		else:
			raise TypeError('Matrix indices must be integers or slices, not %s'\
			 %(type(idx).__name__))
		if idxx is not None:
			# if not a specific cor in matrix then slice follow by column
			if isinstance(idxx, slice):
				for i in range(len(result)):
					result[i] = result[i][idxx]
			# else, return a value in cor x, y in matrix
			elif isinstance(idxx, int):
				for i in range(len(result)):
					result[i] = [result[i][idxx]]
			else:
				raise TypeError('Matrix indices must be integers or slices, not %s'\
				 %(type(idxx).__name__))				
		return Matrix(*result)
	def __iter__(self):
		return iter(self.matrix)
	def isSquareMatrix(self):
		return self.shape[0] == self.shape[1]
	def getPrimaryDiagonal(self):
		if not(self.isSquareMatrix()):
			raise TypeError('Matrix must be a square matrix')
		primaryDiagonal = []
		for i in range(len(self.matrix)):
			primaryDiagonal.append(self.matrix[i][i])
		return Matrix(primaryDiagonal)
	def getSecondaryDiagonal(self):
		if not(self.isSquareMatrix()):
			raise TypeError('Matrix must be a square matrix')
		secondaryDiagonal = []
		for i in range(len(self.matrix)):
			secondaryDiagonal.append(self.matrix[i][-(i + 1)])
		return Matrix(secondaryDiagonal)
	@property
	def T(self):
		# get transition matrix
		T = [[] for i in range(self.shape[1])]
		for row in self.matrix:
			for i in range(self.shape[1]):
				T[i].append(row[i])
		return Matrix(*T)
