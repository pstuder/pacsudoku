from itertools import product

from validmatrix import MatrixHandler


class Algorithm:
	"""Common abstract class for sudoku algorithms."""
	def __init__(self, matrixhandler):
		"""Initializes a new algorithm instance.
		
		The following instance attributes are created:
		_input_matrix -- matrixhandler containing the input sudoku to be solved.
		
		The following instances for default structures used by any algorithm
		are also created:
		_digits -- '123456789'
		_rows -- 'ABCDEFGHI'
		_columns -- same as _digits

		"""
		self._input_matrix = matrixhandler
		
		self._digits = '123456789'
		self._rows = 'ABCDEFGHI'
		self._columns = self._digits
		
	def solve(self):
		"""Raises NotImplementedError, since this is an absract class."""
		raise NotImplementedError("Can't solve if not a specific algorithm!")

	def _cross(self, A, B):
		"""Returns cross elements in A with each element in B"""
		return [a + b for a in A for b in B]
	
	def _some(self, sequence):
		"""Return first element of seq that is true.

		Useful for quick pick-ups and verifications for elements != '' or 0.
		If all elements of the sequence are '' or 0, return False.

		"""
		for element in sequence:
			if element: return element
		return False


class Norvig(Algorithm):
	"""Algorithm class for solving Sudokus using Peter Norvig algorithm"""
	def __init__(self, matrixhandler):
		"""Initializes a new Norvig algorithm instance.
		
		It calls the Algorithm initializator and additionally adds the
		following instance attributes:
		_squares -- ['A1', 'A2' ..., 'B1', 'B2', ... , 'I9']
		_values -- {'A1': '123456789', ... 'I9': '123456789'}
		_units -- {'A1': [[row], [column], [quadrant]], ... }
		_peers -- {'A1': set(row, column, quadrant), ... }

		"""
		Algorithm.__init__(self, matrixhandler)
		self._construct_default_data_structures()
		self._construct_units_and_peers()

	def solve(self):
		"""
		solve() -> matrixhandler
		
		Try to solve the input matrixhandler sudoku using Peter Norvig algorithm.
		
		Return output matrixhandler with the sudoku solved
		Return None, if sudoku has no solution.
		"""
		grid = self._to_grid()
		result_grid = self._search(self._construct_possible_values_grid(grid))
		if not isinstance(result_grid, bool):
			return self._to_matrix(result_grid)
		else:
			return None
	
	def _construct_default_data_structures(self):
		"""Constructs default data structures used by Norvig algorithm.
		
		Two data structures are used:
		_squares -- ['A1', 'A2' ..., 'B1', 'B2', ... , 'I9']
		_values -- {'A1': '123456789', ... 'I9': '123456789'}

		"""
		self._squares = self._cross(self._rows, self._columns)
		self._values = dict((s, self._columns) for s in self._squares)

	def _construct_units_and_peers(self):
		"""Constructs dictionaries containing each fields influence.
		
		Fields can be influenced by its row, column and quadrant it belongs.
		Norvig will use two types of dictionaries for this purpose:
		_units -- {'A1': [[row], [column], [quadrant]], ... }
		_peers -- {'A1': set(row, column, quadrant), ... }

		"""
		unitlist = (
			[self._cross(self._rows, c) for c in self._columns] +
			[self._cross(r, self._columns) for r in self._rows] +
			[
				self._cross(rs, cs)
					for rs in ('ABC','DEF','GHI')
						for cs in ('123','456','789')
			]
		)
		self._units = dict(
			(s, [u for u in unitlist if s in u]) for s in self._squares
		)
		self._peers = dict(
			(s, set(sum(self._units[s], [])) - set([s]))
				for s in self._squares
		)

	def _to_grid(self):
		"""Returns input_matrix as a grid dictionary.
		
		The structure is: {'A1':'<digit>', ...}

		"""
		chars = [
			str(c) for lines in self._input_matrix.first_matrix
						for c in lines
		]
		return dict(zip(self._squares, chars))
	
	def _to_matrix(self, grid):
		"""Returns a new matrix handler from grid converted to a matrix."""
		matrix = []
		for letter in self._rows:
			matrix.append(
				[
					int(grid[field]) for field in self._squares
										if field[0]==letter
				]
			)
		return MatrixHandler(matrix)
	
	def _construct_possible_values_grid(self, grid):
		"""Returns a dictionary grid with possible values for fields in grid.
		
		Dictionary grid will have the following format:
		{'A1':'12', ... 'I9':'3469'}

		"""
		values = dict((field, self._digits) for field in self._squares)
		for field, digit in grid.items():
			if digit in self._digits and (not
			self._assign(values, field, digit)):
				return False
		return values
	
	def _assign(self, grid, field, digit):
		"""Returns values after finished removing other digits successfully.
		
		Use grid and attempt to eliminate all other digits in grid which
		result in a violation until only the possible values for the field
		remain.
		
		Return False if a contradiction has been found during elimination.
		
		"""
		other_values = grid[field].replace(digit, '')
		if all(self._eliminate(grid, field, odigt) for odigt in other_values):
			return grid
		else:
			return False
	
	def _eliminate(self, grid, field, digit):
		"""Return values, same as grid, but with digit eliminated in field.
		
		Use grid and attempt to eliminate digit from field. Consider case:
		(1) If field is reduced to one digit, eliminate this digit from peers
		(2) If unit is reduced to only one place for digit, assign it there
		
		Return False if a contradiction has been found.
		"""
		if digit not in grid[field]:
			return grid									# Already eliminated
		grid[field] = grid[field].replace(digit,'')
		
		# (1) If field is reduced to one value val,
		#     then eliminate val from the peers.
		if len(grid[field]) == 0:
			return False 				# Contradiction: removed last value
		elif len(grid[field]) == 1:
			val = grid[field]
			if not all(
				self._eliminate(
					grid, peer, val
				) for peer in self._peers[field]
			):
				return False
		
		# (2) If unit is reduced to only one place for digit,
		#     then put it there.
		for unit in self._units[field]:
			dplaces = [field for field in unit if digit in grid[field]]
			if len(dplaces) == 0:
				return False		# Contradiction: no place for this value
			elif len(dplaces) == 1:
				if not self._assign(grid, dplaces[0], digit):
					return False
		return grid
	
	def _search(self, values):
		"""Return grid if successfully reduced all fields to one digit.
		
		Search in values for fields with more than one digit, attempt to assign
		arbitrarily one of the digits to that field, if no contradiction found.
		
		Repeat until each field has only one digit (sudoku has been solved).
		
		Return False if contradiction found (sudoku is unsolvable).
		
		"""
		if values is False:
			return False									# Failed earlier
		if all(len(values[field]) == 1 for field in self._squares):
			return values											# Solved!
		
		npos, field = min(
			(len(values[field]), field) for field in self._squares
											if len(values[field]) > 1
		)
		
		return self._some(
			self._search(
				self._assign(values.copy(), field, digit)
			) for digit in values[field]
		)
		

class XAlgorithm(Algorithm):
	
	def solve_sudoku(self, size):
		"""
		solve_sudoku(size) -> matrix
		
		solve a sudoku of an specific size
		
		uses the following methods:
		- costruct_x
		- costruct_y
		- exact_cover
		- select_proper_value
		- return_exit_mat
		
		"""
		Row, Column = size
		matrix_lenght = Row * Column
		list_of_X=self.costruct_x(matrix_lenght)
		list_of_Y = dict()
		list_of_Y=self.costruct_y(matrix_lenght,Row,Column,list_of_Y)
		list_of_X, list_of_Y = self.exact_cover(list_of_X, list_of_Y)
		self.select_proper_value(list_of_X,list_of_Y)
		exit_mat=self.return_exit_mat(list_of_X,list_of_Y)
		if exit_mat==[]:
			return None
		else:
			return exit_mat
		
	
	def return_exit_mat(self,X,Y):
		"""
		return_exit_mat(X,Y) -> matrix
		
		return_exit_mat return a matrix that will be returned by the method solve_sudoku
		
		"""
		exit_mat=[]
		for solution in self.solve_list(X, Y, []):
			for (row, column, lenght) in solution:
				self._input_matrix.first_matrix[row][column] = lenght
			exit_mat=self._input_matrix.first_matrix
		return exit_mat
		
	def select_proper_value(self,X,Y):
		"""
		select_proper_value(X,Y) -> XAlgorithm
		
		select_proper_value return the actual XAlgorithm value after select the columns
		using the method select
		
		"""
		try:
			
			for i, row in enumerate(self._input_matrix.first_matrix):
				for j, lenght in enumerate(row):
					if lenght!=0:
						self.select(X, Y, (i, j, lenght))
			return self
		except:
			return None
		
	def costruct_x(self,matrix_lenght):
		"""
		costruct_x(matrix_lenght) -> List of tuples
		costruct_x return the initial list of tuples
		
		"""
		a=self.first_list("rc",matrix_lenght,0,matrix_lenght)
		b=self.first_list("rn",matrix_lenght,1,matrix_lenght+1)
		c=self.first_list("cn",matrix_lenght,1,matrix_lenght+1)
		d=self.first_list("bn",matrix_lenght,1,matrix_lenght+1)
		return a+b+c+d
				
				
	def first_list(self,text,matrix_lenght1,start,matrix_lenght2):
		list=[]
		for rc in product(range(matrix_lenght1), range(start,matrix_lenght2)):
			list.append((text, rc))
		return list
		
	def costruct_y(self,matrix_lenght,Row,Column,Y):
		"""
		costruct_y(matrix_lenght) -> List of tuples
		costruct_y return the initial list of tuples
		
		"""

		for row, column, lenght in product(range(matrix_lenght), range(matrix_lenght), range(1, matrix_lenght + 1)):
			b = (row // Row) * Row + (column // Column) # Box number
			Y[(row, column, lenght)] =[("rc", (row, column)),("rn", (row, lenght)), ("cn", (column, lenght)), ("bn", (b, lenght))]
		return Y
					
	def solve(self):
		"""
		solve()->MatrixHandler
		solve execute the solve_sudoku method with a size of 3X3 and returns a MatrixHandler type with the solution 
		
		"""
		return_MatrixHandler=self.solve_sudoku((3,3))
		if return_MatrixHandler!=None and return_MatrixHandler!=[]:
			return MatrixHandler(return_MatrixHandler)
		else:
			return None

				
	def exact_cover(self,X, Y):
		"""
		exact_cover(X,Y)->X,Y
		Returns the exact cover list needed to work
		
		"""
		X = {j: set() for j in X}
		for i, row in Y.items():
			for j in row:
				X[j].add(i)
		return X, Y

	def solve_list(self, X, Y, solution):
		"""
		solve_list(X,Y)
		Returns the list thar will be used to solve the sudoku
		
		"""
		if not X:
			yield list(solution)
		else:
			c = min(X, key=lambda c: len(X[c]))
			for r in list(X[c]):
				solution.append(r)
				cols = self.select(X, Y, r)
				for s in self.solve_list(X, Y, solution):
					yield s
				self.deselect(X, Y, r, cols)
				solution.pop()
			
	def select(self,X, Y, r):
		"""
		select(X,Y,r)-> Cols
		select the actual column to work
		
		"""
		cols = []
		for j in Y[r]:
			for i in X[j]:
				for k in Y[i]:
					if k != j:
						X[k].remove(i)
			cols.append(X.pop(j))
		return cols

	def deselect(self,X, Y, r, cols):
		"""
		desselect(X,Y,r,cols)
		disselect the actual column 
		
		"""
		for j in reversed(Y[r]):
			X[j] = cols.pop()
			for i in X[j]:
				for k in Y[i]:
					if k != j:
						X[k].add(i)



class Backtracking(Algorithm):
	
	def num_used_in_submatrix(self, x, y, num):
		"""
		Verify if tentative number is not repeated
		in Sub matrix.
		
		"""
		row = (x/3) * 3
		column = (y/3) * 3
		for i in range(0, 3):
			for j in range(0, 3):
				if self._input_matrix.first_matrix[i+row][j+column] == num:
					return True
		return False
	
	def num_used_in_column(self, column, num):
		"""
		Verify if tentative number is not repeated
		in Column.
		
		"""
		for j in range(0, 9):
			if self._input_matrix.first_matrix[j][column] == num:
				return True
		return False

	def num_used_in_row(self, row, num):
		"""
		Verify if tentative number is not repeated
		in row.
		
		"""
		for i in range(0, 9):
			if self._input_matrix.first_matrix[row][i] ==  num:
				return True
		return False

	def num_no_conflicts(self, row, column, num):
		"""
		Join all function and return True or False
		if number doesn't have any problem.
		
		"""
		return self.num_used_in_row(row, num) != True and \
			self.num_used_in_column(column, num) != True and \
			self.num_used_in_submatrix(row, column, num) != True

	def find_unassigned_location(self, row, column):
		#Find any cell with 0.
		for i in range(row, 9):
			for j in range(column, 9):
				if self._input_matrix.first_matrix[i][j] == 0:
					return True, i, j
		return False, i, j

	def solve_backtracking(self):
		"""
		Solve Sudoku with backtracking algorithm recursive.
		
		"""
		row = 0
		column = 0
		flag, row, column = self.find_unassigned_location(row, column)
		if flag != True:
			return True
		for num in range(1, 10):
			if self.num_no_conflicts(row, column, num) == True:
				self._input_matrix.first_matrix[row][column] = num
				if self.solve_backtracking() == True:
					return True
				self._input_matrix.first_matrix[row][column] = 0
		return False

	def solve(self):
		"""
		Returns Sudoku matrix solved.
		
		"""
		if self.solve_backtracking() == True:
			return MatrixHandler(self._input_matrix.first_matrix)
		else:
			return None