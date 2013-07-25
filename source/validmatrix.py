"""validmatrix contents the MatrixHandler class used for all required to handle a matrix. """
import random 
from copy import deepcopy

class MatrixHandler:
	"""MatrixHandler
		MatrixHandelr class will create a Matrix attribute to get sudoku structure game
		this matrix will be validated if there are numbers between 0 to 9, not repeated
		numbers in rows, columns and sub squares.
		
	"""
	def __init__(self, frst_matrix):
		""" Construct first_matrix."""
		self.first_matrix = frst_matrix
	
	
	def length_sublist(self):
		"""Calculate the length of each sublist if length is equal to 9."""
		for i in range(len(self.first_matrix)):
			if len(self.first_matrix[i]) != 9:
				return False
		return True
	
	
	def length_matrix(self):
		"""Return if length of matrix is equal to 9x9."""
		if len(self.first_matrix) == 9 and self.length_sublist() == True:
			return True
		return False
	
	def correct_lines(self):
		"""Verify if numbers in rows are between 1 and 9."""
		for i in range(0, 9):
			for j in range(0, 9):
				if not (self.first_matrix[i][j] >= 0 and self.first_matrix[i][j] <= 9):
					return False
		return True
	
	def correct_columns(self):
		"""Verify if numbers in columns are between 1 and 9."""
		for i in range(0, 9):
			for j in range(0, 9):
				if not (self.first_matrix[j][i] >= 0 and self.first_matrix[j][i] <= 9):
					return False
		return True
		
	def repeatednumberscolumns(self):
		"""Verify if number from 1 to 9 in columns are not repeated."""
		for i in range(0, 9):
			listcolumn = self.first_matrix[0: 9][i]
			for j in range(1, 9):
				if listcolumn.count(j) > 1:
					return False
		return True
		
	def repeatednumbersline(self):
		"""Verify if number from 1 to 9 in rows are not repeated."""
		for i in range(0, 9):
			listline = self.first_matrix[i][0: 9]
			for j in range(1, 9):
				if listline.count(j) > 1:
					return False
		
		return True
	
	def minimatrixtolist (self, mini_matrix):
		"""Creates a list with sub matrix values."""
		listmatrix = []
		for i in range(0, 3):
			for j in range(0, 3):
				listmatrix.append(mini_matrix[i][j])
		return listmatrix
	
	def countlistmatrix(self, mini_matrix):
		"""Count repeated numbers in list created from sub matrix."""
		listmatrix = self.minimatrixtolist(mini_matrix)
		for j in range(1, 9):
			if listmatrix.count(j) > 1:
				return False
		return True
	
	def submatrixvalidnumbers(self, mini_matrix):
		"""Verify if numbers in sub matrix are between 1 and 9."""
		for i in range(0, 3):
			for j in range(0, 3):
				if not (mini_matrix[i][j] >= 0 and mini_matrix[i][j] <= 9):
					return False
		return True
	
	def submatrix(self, line, column):
		"""Creates a matrix with each sub matrix."""
		minmatrix = [[0, 0, 0], 
				[0, 0, 0], 
				[0, 0, 0]]
		row = (line/3) * 3
		col = (column/3) * 3
		for selected_row in range(0, 3):
			for selected_column in range(0, 3):
				minmatrix[selected_row][selected_column] = \
				          self.first_matrix[selected_row+row][selected_column+col]
		return minmatrix
	
	
	def valid_submatrix_numbers(self):
		"""Verify if numbers in sub matrix are between 0 to 9."""
		for i in range (0, 3):
			for j in range (0, 3):
				if self.submatrixvalidnumbers(self.submatrix(i*3, j*3)) != True :
					return False
		return True
	
	
	def valid_submatrix_repeated(self):
		"""Verify if numbers in sub matrix are not repeated."""
		for i in range (0, 3):
			for j in range (0, 3):
				if self.countlistmatrix(self.submatrix(i*3, j*3)) != True:
					return False
		return True
	
	def validate(self):
		"""Verify if first sudoku matrix is valid or not."""
		if self.length_matrix() == True:
			if self.correct_lines() == True and \
								self.correct_columns() == True and \
								self.repeatednumberscolumns() == True and \
								self.repeatednumbersline() == True and \
								self.valid_submatrix_numbers() == True and \
								self.valid_submatrix_repeated() == True:
				return True
		return False
	
# *******************************************        
# Ariel
# ******************************************* 
	def fill_square(self, table, square=1):
		"""Fill random values in a selected sub square of a table. """
		available_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		small_rows = self.return_small_rows(square)
		small_columns = self.return_small_columns(square)
		for i in small_rows:
			for j in small_columns:
				lenght = len(available_values)
				random_value = random.randint(0, lenght-1)
				table[i][j] = available_values[random_value]
				available_values.remove(available_values[random_value])
	
	
	def create_blank_table(self):
		"""Return a 9X9 table initialized with zeros. """
		return [[0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0], 
			   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
	
	def zero_count(self, table):
		"""Return a int value with the count of zeros of a matrix. """
		rows = len(table)
		columns = len(table[0])
		zero_count = 0
		for i in range(rows):
			for j in range(columns):
				if table[i][j] == 0:
					zero_count += 1
		return zero_count	   
	
	def return_small_rows(self, square):
		"""Return a sub divided list of rows of a matrix. """
		if square == 1 or square == 2 or square == 3 :
			return [0, 1, 2]
		elif square == 4 or square == 5 or square == 6:
			return [3, 4, 5]
		elif square == 7 or square == 8 or square == 9:
			return [6, 7, 8]
	
	def return_small_columns(self, square):
		"""Return a sub divided list of columns of a matrix. """
		if square == 1 or square == 4 or square == 7 :
			return [0, 1, 2]
		elif square == 2 or square == 5 or square == 8:
			return [3, 4, 5]
		elif square == 3 or square == 6 or square == 9:
			return [6, 7, 8] 
	
	
	def square_return(self, row, column):
		"""Return a sub square where a row and column point in a matrix. """
		if row <= 2 and column <= 2:
			square = 1
		elif row <= 5 and column <= 2:
			square = 4
		elif row <= 8 and column <= 2:
			square = 7
		elif row <= 2 and column <= 5:
			square = 2
		elif row <= 5 and column <= 5:
			square = 5
		elif row <= 8 and column <= 5:
			square = 8
		elif row <= 2 and column <= 8:
			square = 3
		elif row <= 5 and column <= 8:
			square = 6
		elif row <= 8 and column <= 8:
			square = 9
		return square
	
	
	def return_posible_vertical_values(self, table, row, column):
		"""Return a list of possible vertical values. """
		available_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		rows = len(table)
		for i in range(rows):
			if i != row:
				value = table[i][column] 
				if value in available_values: 
					available_values.remove(value) 
		return available_values

	def posible_horizontal_values(self, table, row, column):
		"""Return a list of possible horizontal values. """
		available_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		columns = len(table[0])
		for i in range(columns):
			if i != column:
				value = table[row][i] 
				if value in available_values: 
					available_values.remove(value) 
		return available_values
	
	def return_posible_square_values(self, table, row, column):
		"""Return a list of possible values of a sub square. """
		available_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		square = self.square_return(row, column)
		small_rows = self.return_small_rows(square)
		small_columns = self.return_small_columns(square)
		initial_study_point_value = table[row][column]
		table[row][column] = 'estudio'
		for i in small_rows:
			for j in small_columns:
				if table[i][j] != 'estudio':
					value = table[i][j]
					if value in available_values:
						available_values.remove(value)
		table[row][column] = initial_study_point_value 
		return available_values
	
	def return_inverted_values(self, posible_values):
		"""Return a inverted values list of possible values. """
		imposible_values = []
		for i in range(1, 10):
			if not(i in posible_values):
				imposible_values.append(i)
		return imposible_values
	
	def return_total_posible_values(self, table, row, column):
		"""Return a complete values list of possible values. """
		list1 = self.return_posible_vertical_values(table, row, column)
		list2 = self.posible_horizontal_values(table, row, column)
		list3 = self.return_posible_square_values(table, row, column)
		list1 = self.return_inverted_values(list1)
		list2 = self.return_inverted_values(list2)
		list3 = self.return_inverted_values(list3)
		complete_list = list1 + list2 + list3
		imposible_values_list = []
		for i in range(1, 10):
			if i in complete_list:
				imposible_values_list.append(i)
		posible_values_list = self.return_inverted_values(
												imposible_values_list)
		return posible_values_list
	
	def fill_inmediate_values(self, table):
		"""Fill the table with unique possible values. """
		filled = 0
		rows = len(table)
		columns = len(table[0])
		for i in range(rows):
			for j in range(columns):
				if table[i][j] == 0:
					posible_values = self.return_total_posible_values(
																table, i, j)
					if len(posible_values) == 1:
						table[i][j] = posible_values[0]
						filled = 1
		return filled
	
	def return_one_from_list(self, input_list):
		"""Return a random value from list. """
		lenght = len(input_list)
		return input_list[random.randint(0, lenght-1)]
	
	def fill_cell_with_n_posible_values(self, table, n_posible_values):
		"""Fill a cell of a table with N possible values. """
		rows = len(table)
		columns = len(table[0])
		for i in range(rows):
			for j in range(columns):
				if table[i][j] == 0:	  
					posible_valuess = self.return_total_posible_values(
															table, i, j)
					if len(posible_valuess) == n_posible_values:
						table[i][j] = self.return_one_from_list(
															posible_valuess)
					return 1
		return 0
	
	def fill_posibilities(self, table):
		"""Fill the possible values of a table. """
		counter = 0
		while self.zero_count(table) != 0 and counter <= 200:
			counter += 1
			self.fill_inmediate_values(table)
			for i in range(2, 7):    
				self.fill_cell_with_n_posible_values(table, i)


	def hide_cells(self, table, level):
		"""Fill cells with zeros in random order. """
		if level == "Low":
			zero_quantity = 35
		elif level == "Medium":
			zero_quantity = 39
		elif level == "High":
			zero_quantity = 42
		else:
			zero_quantity = 35
		inserted_zeros = self.zero_count(table)
		counter = 0
		rows = len(table)
		columns = len(table[0])
		while (zero_quantity > inserted_zeros and counter < 10000):
			counter += 1
			row = random.randint(0, rows-1)
			column = random.randint(0, columns-1)
			if table[row][column] != 0:
				if len(self.return_total_posible_values(table, row, column)) == 1:
					table[row][column] = 0
					if self.is_valid(table, inserted_zeros)!=True:
						table = deepcopy(table)
					inserted_zeros = self.zero_count(table)
	
	def is_valid(self, sudoku, zeros):
		"""Verified if a sudoku game is valid. """
		sudoku_copy = deepcopy(sudoku)
		counter = 0
		while self.zero_count(sudoku_copy) != 0 and counter <= zeros:
			counter += 1
			self.fill_inmediate_values(sudoku_copy)
			for i in range(2, 7):    
				self.fill_cell_with_n_posible_values(sudoku_copy, i)
				
		if self.zero_count(sudoku_copy) == 0:
			return True
		else:
			return False
		
	def generator(self, level):    
		"""Generate a new SUDOKU game. """
		sudoku = self.create_blank_table()
		count = self.zero_count(sudoku)
		while count != 0:
			sudoku = self.create_blank_table()
			self.fill_square(sudoku, 1)
			self.fill_square(sudoku, 5)
			self.fill_square(sudoku, 9)
			self.fill_posibilities(sudoku)
			count = self.zero_count(sudoku)
		if level == "Low":
			sudoku = self.exact_sudoku_dificult_matrix(35, sudoku, level)
		elif level == "Medium":
			sudoku = self.exact_sudoku_dificult_matrix(39, sudoku, level)
		elif level == "High":
			sudoku = self.exact_sudoku_dificult_matrix(42, sudoku, level)
		else:
			sudoku = self.exact_sudoku_dificult_matrix(35, sudoku, level)
		
		self.first_matrix = sudoku
		
	
	def exact_sudoku_dificult_matrix(self, limit, sudoku, level):
		"""Create a matrix with the required zeros according to difficult. """
		while self.zero_count(sudoku) != limit:
			sudoku = self.create_blank_table()
			self.fill_square(sudoku, 1)
			self.fill_square(sudoku, 5)
			self.fill_square(sudoku, 9)
			self.fill_posibilities(sudoku)
			self.hide_cells(sudoku, level)
			self.zero_count(sudoku)
		return sudoku

		
	def printmatrix(self):
		""" Print the matrix in PRD format """
		chain = ""
		if len(self.first_matrix)>0:
			for i in range(len(self.first_matrix)):    
				for j in range(len(self.first_matrix)):        
					if j % 3 == 0 and j != 0:
						chain = chain + "| "
					chain = chain + str(self.first_matrix[i][j]) + "   "
				if (i+1) % 3 == 0 and i != 0 and (i+1) != 9:
					chain = chain + "\n-------------------------------------"
				chain = chain + "\n"
		print chain
		return chain    

