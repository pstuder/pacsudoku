
"""Module for the algorithms to be used for solving a Sudoku."""

from copy import deepcopy
from itertools import product

from validmatrix import MatrixHandler


class Algorithm:
	"""Common abstract class for sudoku algorithms."""
	def __init__(self, matrixhandler):
		"""Initializes a new algorithm instance.
		
		The following instance attributes are created:
		output_matrix -- exact copy of input sudoku to be solved.
		
		The following instances for default structures used by any algorithm
		are also created:
		_digits -- '123456789'
		_rows -- 'ABCDEFGHI'
		_columns -- same as _digits

		"""
		self.output_matrix = deepcopy(matrixhandler)
		
		self._digits = '123456789'
		self._rows = 'ABCDEFGHI'
		self._columns = self._digits
		
	def solve(self):
		"""Raises NotImplementedError, since this is an absract class."""
		raise NotImplementedError("Can't solve if not a specific algorithm!")

	def cross(self, first_elements, second_elements):
		"""Returns cross of first_elements with each of second_elements"""
		return [first + second for first in first_elements
								for second in second_elements]
	
	def some(self, sequence):
		"""Return first element of seq that is true.

		Useful for quick pick-ups and verifications for elements != '' or 0.
		If all elements of the sequence are '' or 0, return False.

		"""
		for element in sequence:
			if element:
				return element
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
		self._units = {}
		self._peers = {}
		self._squares = []
		self._values = {}
		self.construct_data_structures()
		self.construct_units_and_peers()

	def solve(self):
		"""Try to solve output_matrix sudoku using Peter Norvig algorithm.
		
		Return output matrixhandler with the sudoku solved.
		Return None, if sudoku has no solution.
		"""
		grid = self._to_grid()
		result_grid = self._search(self._construct_possible_values_grid(grid))
		if not isinstance(result_grid, bool):
			return self._to_matrix(result_grid)
		else:
			del(self.output_matrix)
			return None
	
	def construct_data_structures(self):
		"""Constructs default data structures used by Norvig algorithm.
		
		Two data structures are used:
		_squares -- ['A1', 'A2' ..., 'B1', 'B2', ... , 'I9']
		_values -- {'A1': '123456789', ... 'I9': '123456789'}

		"""
		self._squares = self.cross(self._rows, self._columns)
		self._values = dict((s, self._columns) for s in self._squares)

	def construct_units_and_peers(self):
		"""Constructs dictionaries containing each fields influence.
		
		Fields can be influenced by its row, column and quadrant it belongs.
		Norvig will use two types of dictionaries for this purpose:
		_units -- {'A1': [[row], [column], [quadrant]], ... }
		_peers -- {'A1': set(row, column, quadrant), ... }

		"""
		unitlist = (
			[self.cross(self._rows, c) for c in self._columns] +
			[self.cross(r, self._columns) for r in self._rows] +
			[
				self.cross(rs, cs)
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
			str(c) for lines in self.output_matrix.first_matrix
						for c in lines
		]
		return dict(zip(self._squares, chars))
	
	def _to_matrix(self, grid):
		"""Returns a new matrix handler from grid converted to a matrix."""
		self.output_matrix.first_matrix = []
		for letter in self._rows:
			self.output_matrix.first_matrix.append(
				[
					int(grid[field]) for field in self._squares
										if field[0] == letter
				]
			)
		return self.output_matrix
	
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
		
		return self.some(
			self._search(
				self._assign(values.copy(), field, digit)
			) for digit in values[field]
		)


class XAlgorithm(Algorithm):
	"""XAlgorithm is a solution with the Exact cover solution. """
	
	def solve_sudoku(self, size):
		""" Solve a sudoku of an specific size.
		
		uses the following methods:
		- costruct_x.
		- costruct_y.
		- exact_cover.
		- select_proper_value.
		- return_exit_mat.
		"""
		input_row, input_column = size
		matrix_lenght = input_row * input_column
		list_of_x = self.costruct_x(matrix_lenght)
		list_of_y = dict()
		list_of_y = self.costruct_y(matrix_lenght, input_row, input_column, list_of_y)
		list_of_x, list_of_y = self.exact_cover(list_of_x, list_of_y)
		self.select_proper_value(list_of_x, list_of_y)
		exit_mat = self.return_exit_mat(list_of_x, list_of_y)
		if exit_mat == []:
			return None
		else:
			return exit_mat
		
	
	def return_exit_mat(self, list_x, list_y):
		""" Return a matrix that will be returned by the method solve_sudoku. """
		exit_mat = []
		for solution in self.solve_list(list_x, list_y, []):
			for (row, column, lenght) in solution:
				self.output_matrix.first_matrix[row][column] = lenght
			exit_mat = self.output_matrix.first_matrix
		return exit_mat
		
	def select_proper_value(self, list_x, list_y):
		""" Return the actual XAlgorithm value after select the columns
		using the method select.
		"""
		try:
			
			for i, row in enumerate(self.output_matrix.first_matrix):
				for j, lenght in enumerate(row):
					if lenght != 0:
						self.select(list_x, list_y, (i, j, lenght))
			return self
		except:
			return None
		
	def costruct_x(self, matrix_lenght):
		""" Return the initial list of tuples of X list. """
		row_column = self.first_list("rc", matrix_lenght, 0, matrix_lenght)
		row_number = self.first_list("rn", matrix_lenght, 1, matrix_lenght+1)
		column_number = self.first_list("cn", matrix_lenght, 1, matrix_lenght+1)
		block_number = self.first_list("bn", matrix_lenght, 1, matrix_lenght+1)
		return row_column+row_number+column_number+block_number
				
				
	def first_list(self, text, matrix_lenght1, start, matrix_lenght2):
		""" Return the initial list of values. """
		initial_list = []
		for row_column in product(
								 range(matrix_lenght1), 
								 range(start, matrix_lenght2)):
			initial_list.append((text, row_column))
		return initial_list
		
	def costruct_y(self, matrix_lenght, input_row, input_column, list_y):
		""" Return the initial list of tuples of Y list.	"""

		for row, column, lenght in product(
									range(matrix_lenght), 
									range(matrix_lenght), 
									range(1, matrix_lenght + 1)):
			box_number = (row // input_row) * input_row + (column // input_column) 
			list_y[(row, column, lenght)] =[
					 						("rc", (row, column)),
			  						   		("rn", (row, lenght)), 
			  						   		("cn", (column, lenght)), 
			  			  			   		("bn", (box_number, lenght))
			  			  			  	   ]
		return list_y
					
	def solve(self):
		""" Execute the solve_sudoku method with a size of 3X3 
		and returns a MatrixHandler type with the solution. 
		"""
		return_matrix_handler = self.solve_sudoku((3, 3))
		if return_matrix_handler != None and return_matrix_handler != []:
			return MatrixHandler(return_matrix_handler)
		else:
			del(self.output_matrix)
			return None

				
	def exact_cover(self, list_x, list_y):
		"""	Returns the exact cover list needed to work. """
		list_x = {location: set() for location in list_x}
		for i, row in list_y.items():
			for location in row:
				list_x[location].add(i)
		return list_x, list_y

	def solve_list(self, list_x, list_y, solution):
		""" Returns the list that will be used to solve the sudoku. """
		if not list_x:
			yield list(solution)
		else:
			column_position = min(list_x, 
								  key = lambda column_position: 
								  len(list_x[column_position]))
			for row_position in list(list_x[column_position]):
				solution.append(row_position)
				cols = self.select(list_x, list_y, row_position)
				for solved in self.solve_list(list_x, list_y, solution):
					yield solved
				self.unselect(list_x, list_y, row_position, cols)
				solution.pop()
			
	def select(self, list_x, list_y, row_position):
		""" Select the actual column to work. """
		cols = []
		for j in list_y[row_position]:
			for i in list_x[j]:
				for k in list_y[i]:
					if k != j:
						list_x[k].remove(i)
			cols.append(list_x.pop(j))
		return cols

	def unselect(self, list_x, list_y, row_position, columns):
		""" Unselect the actual column. """
		for j in reversed(list_y[row_position]):
			list_x[j] = columns.pop()
			for i in list_x[j]:
				for k in list_y[i]:
					if k != j:
						list_x[k].add(i)



class Backtracking(Algorithm):
	
	def num_used_in_submatrix(self, x, y, num):
		"""Verify if tentative number is not repeated in Sub matrix."""
		row = (x/3) * 3
		column = (y/3) * 3
		for i in range(0, 3):
			for j in range(0, 3):
				if self.output_matrix.first_matrix[i+row][j+column] == num:
					return True
		return False
	
	def num_used_in_column(self, column, num):
		"""Verify if tentative number is not repeated in Column."""
		for j in range(0, 9):
			if self.output_matrix.first_matrix[j][column] == num:
				return True
		return False

	def num_used_in_row(self, row, num):
		"""Verify if tentative number is not repeated in row."""
		for i in range(0, 9):
			if self.output_matrix.first_matrix[row][i] ==  num:
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
				if self.output_matrix.first_matrix[i][j] == 0:
					return True, i, j
		return False, i, j

	def solve_backtracking(self):
		"""Solve Sudoku with backtracking algorithm recursive."""
		row = 0
		column = 0
		flag, row, column = self.find_unassigned_location(row, column)
		if flag != True:
			return True
		for num in range(1, 10):
			if self.num_no_conflicts(row, column, num) == True:
				self.output_matrix.first_matrix[row][column] = num
				if self.solve_backtracking() == True:
					return True
				self.output_matrix.first_matrix[row][column] = 0
		return False

	def solve(self):
		"""Returns Sudoku matrix solved."""
				
		if self.solve_backtracking() == True:
			return self.output_matrix
		else:
			del(self.output_matrix)
			return None