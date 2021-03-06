
"""Module for the interface controller."""

import config
import inout
import validmatrix
import solver

class Interface():
	"""Common command interface for console and UI."""
	def __init__(self, config_file_handler):
		"""Initializes a new interface.
		
		The following instance attributes are created:
		config -- config instance using config_file_handler
		input_matrix -- Input matrix initialized as None
		output_matrix -- Output matrix initialized as None
		algorithm -- Algorithm to be used, initialized as None
		
		If config_file_handler is incorrect, use default config.

		"""
		try:
			self.config = config_file_handler.read_config_file()
		except IOError:
			self.config = config.Configfile()
		self.input_matrix = None
		self.output_matrix = None
		self.algorithm = None
	
	def _reset_input_matrix(self):
		"""Deletes current input_matrix, if any, and sets it to None."""
		if self.input_matrix is not None:
			del(self.input_matrix)
			self.input_matrix = None
	
	def _reset_output_matrix(self):
		"""Deletes current output_matrix, if any, and sets it to None."""
		if self.output_matrix is not None:
			del(self.output_matrix)
			self.output_matrix = None
	
	def _reset_algorithm(self):
		"""Deletes current algorithm, if any, and sets it to None."""
		if self.algorithm is not None:
			del(self.algorithm)
			self.algorithm = None
	
	def _set_algorithm(self):
		"""Sets/updates algorithm with algorithm type defined in config.
		
		Raises TypeError if algorithm not supported.
		
		"""
		del(self.algorithm)
		if self.config.defaultAlgorithm == "Backtracking":
			self.algorithm = solver.Backtracking(self.input_matrix)
		elif self.config.defaultAlgorithm == "Norvig":
			self.algorithm = solver.Norvig(self.input_matrix)
		elif self.config.defaultAlgorithm == "XAlgorithm":
			self.algorithm = solver.XAlgorithm(self.input_matrix)
		else:
			raise TypeError

	def update_config_input_type(self, new_input_type):
		"""Returns True if config updated with new_input_type."""
		if self.config.validateInputType(
			new_input_type,
			self.config.supported_inputTypes
			):
			self.config.inputType = new_input_type
			return True
		return False
	
	def update_config_output_type(self, new_output_type):
		"""Returns True if config updated with new_output_type."""
		if self.config.validateInputType(
			new_output_type,
			self.config.supported_outputTypes
			):
			self.config.outputType = new_output_type
			return True
		return False
	
	def update_config_default_algorithm(self, new_default_algorithm):
		"""Returns True if config updated with new_default_algorithm."""
		if self.config.validateInputType(
			new_default_algorithm,
			self.config.supported_defaultAlgorithms
			):
			self.config.defaultAlgorithm = new_default_algorithm
			return True
		return False
	
	def update_config_difficulty_level(self, new_difficulty_level):
		"""Returns True if config updated with new_difficulty_level."""
		if self.config.validateInputType(
			new_difficulty_level,
			self.config.supported_difficultyLevels
			):
			self.config.difficultyLevel = new_difficulty_level
			return True
		return False
	
	def save_config_to_file(self, config_file_handler):
		"""Returns True if config saved to config_file_handler.file"""
		try:
			config_file_handler.reopen('w')
			config_file_handler.create_config_file(self.config)
			return True
		except IOError:
			return False
	
	def config_changes_not_saved(self, config_file_handler):
		"""Returns True if config settings differ from config_file_handler"""
		try:
			config_file_handler.reopen('r')
			file_config = config_file_handler.read_config_file()
		except AttributeError:
			return True
		return (
			self.config.inputType != file_config.inputType or
			self.config.outputType != file_config.outputType or
			self.config.defaultAlgorithm != file_config.defaultAlgorithm or
			self.config.difficultyLevel != file_config.difficultyLevel
		)
	
	def load_sudoku_from_file(self, file_name):
		"""Returns True if file saved to input_matrix as a valid Sudoku game.
		
		Raises TypeError if config, by any reason, is set with an unexpected
		type.
		
		"""
		self._reset_input_matrix()
		if self.config.inputType == 'CSV':
			file_handler = inout.FileHandlerCSV(file_name)
		elif self.config.inputType == 'TXT':
			file_handler = inout.FileHandlerTXT(file_name)
		else:
			raise TypeError("Unexpected Type: %s" % self.config.inputType)
		
		matrix = file_handler.import_file()
		self.input_matrix = validmatrix.MatrixHandler(matrix)
		return self.input_matrix.validate()
	
	def export_sudoku_to_file(self, file_name):
		"""Returns True if output_matrix successfully exported to file."""
		if self.output_matrix is None:
			return False
		try:
			file_handler = inout.FileHandlerTXT(file_name, 'w')
			file_handler.export_file(self.output_matrix.first_matrix)
			return True
		except IOError:
			return False
	
	def solve_sudoku(self):
		"""Returns True if Sudoku successfully solved.
		
		The Sudoku stored in input_matrix is used with algorithm. If
		the solution is a matrix, it will get stored to output_matrix.
		If the solution is None, False is returned.
		
		"""
		if self.input_matrix is None:
			return False
		self._reset_output_matrix()
		try:
			self._set_algorithm()
		except TypeError:
			return False
		self.output_matrix = self.algorithm.solve()
		return self.output_matrix is not None
	
	def generate_sudoku(self):
		"""Returns True if successfully generated valid Sudoku game.

		Generator will use Norvig algorithm to create a matrix and
		will store it to input_matrix.first_matrix.
		
		Returns False if a failure has been detected in the process
		of generating a sudoku game.
		
		"""
		self._reset_input_matrix()
		self.input_matrix = validmatrix.MatrixHandler([])
		temp_default_algorithm = self.config.defaultAlgorithm
		self.config.defaultAlgorithm = "Norvig"
		try:
			while True:
				self.input_matrix.generator(self.config.difficultyLevel)
				self._set_algorithm()
				if self.algorithm.solve() is not None:
					break
			self.config.defaultAlgorithm = temp_default_algorithm
			self._set_algorithm()
		except TypeError:
			return False
		return True

	def printmatrix(self):
				""" Print the matrix in PRD format """
				chain=""
				if len(self.input_matrix.first_matrix)>0:
					for i in range(len(self.input_matrix.first_matrix)):    
						for j in range(len(self.input_matrix.first_matrix)):        
							if j%3==0 and j!=0:
								chain=chain + "| "
							chain=chain + str(self.input_matrix.first_matrix[i][j]) +"   "
						if (i+1)%3==0 and i!=0 and (i+1)!=9:
							chain=chain + "\n-------------------------------------"
						chain=chain + "\n"
				print chain
				return chain  
