from validmatrix import MatrixHandler

class Algorithm:
	
	def __init__(self, matrixhandler):
        #Instance to matrix handler used as input for any algorithm.
		self._input_matrix = matrixhandler
		
		# Default structures to be used by any algorithm:
		# digits, rows and columns
		self._digits = '123456789'
		self._rows = 'ABCDEFGHI'
		self._columns = self._digits
		
		# Default fields and values for any algorithm as:
		# squares = ['A1', 'A2' ..., 'B1', 'B2', ... , 'I9']
		# values = {'A1':'123456789', ... 'I9':'123456789'}
		self._squares = self._cross(self._rows, self._columns)
		self._values = dict((s, self._columns) for s in self._squares)
		
		# Don't use this. It is a constructor for "self._units". See next.
		self._unitlist = ([self._cross(self._rows, c) for c in self._columns] +
			[self._cross(r, self._columns) for r in self._rows] +
			[self._cross(rs, cs) for rs in ('ABC','DEF','GHI')
			for cs in ('123','456','789')])
		
		# Field influenced by rows, columns and quadrants
		# will be saved in two types of dictionaries:
		# units = {'A1': [[row], [column], [quadrant]], ... }
		# peers = {'A1': set(row, column, quadrant), ... }
		self._units = dict((s, [u for u in self._unitlist if s in u])
			for s in self._squares)
		self._peers = dict((s, set(sum(self._units[s], [])) - set([s]))
			for s in self._squares)
		
	def solve(self, algorithm_type):
		"""
		solve(algorithm_type) -> matrixhandler
		
		Try to solve the input matrixhandler using algorithm_type.
		Return output matrixhandler with the solution or return None,
		If sudoku has no solution.
		"""
		raise ImplementationError("Not yet implemented!")

	def _cross(self, A, B):
		"""
		_cross(A, B) -> List
		
		Cross elements of A sequence with each element in B sequence and return
		a list with all combinations.
		"""
		return [a + b for a in A for b in B]
	
	def _some(self, sequence):
		"""
		_some(sequence) -> element
		
		Return first element of seq that is true.
		Useful for quick pick-ups and verifications for elements != '' or 0.
		If all elements of the sequence are '' or 0, return False.
		"""
		for element in sequence:
			if element: return element
		return False

class Norvig(Algorithm):
	
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
	
	def _to_grid(self):
		"""
		_to_grid()
		
		Convert input_matrix to a grid structure: {'A1':'<digit>', ...}
		"""
		chars = [str(c) for lines in self._input_matrix.first_matrix\
															for c in lines]
		return dict(zip(self._squares, chars))
	
	def _to_matrix(self, grid):
		"""
		_to_matrix(grid) -> matrixhandler
		
		Convert given grid to a matrix and return it as a new matrixhandler.
		"""
		matrix = []
		for letter in self._rows:
			matrix.append([int(grid[field]) for field in\
									self._squares if field[0]==letter])
		
		return MatrixHandler(matrix)
	
	def _construct_possible_values_grid(self, grid):
		"""
		_construct_possible_values_grid(grid) -> values
		
		Use grid to build and return values with possible values for a field:
		{'A1':'12', ... 'I9':'3469'}
		"""
		values = dict((field, self._digits) for field in self._squares)
		for field, digit in grid.items():
			if digit in self._digits and not self._assign(values, field, digit):
				return False
		return values
	
	def _assign(self, grid, field, digit):
		"""
		_assign(grid, field, digit) -> values
		
		Use grid and attempt to eliminate all other digits in grid which result
		in a violation until only the possible values for the field remain.
		
		Return values after finished eliminating other digits successfully.
		Return False if a contradiction has been found during elimination.
		"""
		other_values = grid[field].replace(digit, '')
		if all(self._eliminate(grid, field, odigt) for odigt in other_values):
			return grid
		else:
			return False
	
	def _eliminate(self, grid, field, digit):
		"""
		_eliminate(grid, field, digit) -> values
		
		Use grid and attempt to eliminate digit from field. Consider case:
		(1) If field is reduced to one digit, eliminate this digit from peers
		(2) If unit is reduced to only one place for digit, assign it there
		
		Return values, same as grid, but with digit eliminated in field
		Return False if a contradiction has been found.
		"""
		if digit not in grid[field]:
			return grid ## Already eliminated
		grid[field] = grid[field].replace(digit,'')
		
		# (1) If field is reduced to one value val,
		#     then eliminate val from the peers.
		if len(grid[field]) == 0:
			return False ## Contradiction: removed last value
		elif len(grid[field]) == 1:
			val = grid[field]
			if not all(self._eliminate(grid, peer, val)\
											for peer in self._peers[field]):
				return False
		
		# (2) If unit is reduced to only one place for digit,
		#     then put it there.
		for unit in self._units[field]:
			dplaces = [field for field in unit if digit in grid[field]]
			if len(dplaces) == 0:
				return False ## Contradiction: no place for this value
			elif len(dplaces) == 1:
				# d can only be in one place in unit; assign it there
				if not self._assign(grid, dplaces[0], digit):
					return False
		return grid
	
	def _search(self, values):
		"""
		_search(values) -> grid
		
		Search in values for fields with more than one digit, attempt to assign
		arbitrarily one of the digits to that field, if no contradiction found.
		
		Repeat until each field has only one digit.
		
		Return grid if successfully reduced all fields to one digit (sudoku
		has been solved).
		
		Return False if contradiction found (sudoku is unsolvable).
		"""
		if values is False:
			return False ## Failed earlier
		if all(len(values[field]) == 1 for field in self._squares):
			return values ## Solved!
		
		## Chose the unfilled field with the fewest possibilities
		npos, field = min((len(values[field]), field)\
						for field in self._squares if len(values[field]) > 1)
		
		return self._some(self._search(self._assign(values.copy(),\
									field, digit)) for digit in values[field])

