import config
import io
import validmatrix
import solver

class Interface():
	def __init__(self, config_file_handler):
		try:
			self.config = config_file_handler.read_config_file()
		except IOError:
			self.config = config.Configfile()
		except:
			raise
		self.input_matrix = None
		self.output_matrix = None
		self.algorithm = None
	
	def _reset_input_matrix(self):
		if self.input_matrix != None:
			del(self.input_matrix)
			self.input_matrix = None
	
	def _reset_output_matrix(self):
		if self.output_matrix != None:
			del(self.output_matrix)
			self.output_matrix = None
	
	def _reset_algorithm(self):
		if self.algorithm != None:
			del(self.algorithm)
			self.algorithm = None
	
	def _set_algorithm(self):
		if self.algorithm.__class__.__name__ != self.config.defaultAlgorithm:
			del(self.algorithm)
			if self.config.defaultAlgorithm == "Backtracking":
				raise ImplementationError
			elif self.config.defaultAlgorithm == "Norvig":
				self.algorithm = solver.Norvig(self.input_matrix)
			elif self.config.defaultAlgorithm == "Other":
				raise ImplementationError
			else:
				raise TypeError

	def update_config_inputType(self, new_inputType):
		if self.config.validateInputType(new_inputType,\
										self.config.supported_inputTypes):
			self.config.inputType = new_inputType
			return True
		return False
	
	def update_config_outputType(self, new_outputType):
		if self.config.validateInputType(new_outputType,\
									self.config.supported_outputTypes):
			self.config.outputType = new_outputType
			return True
		return False
	
	def update_config_defaultAlgorithm(self, new_defaultAlgorithm):
		if self.config.validateInputType(new_defaultAlgorithm,\
									self.config.supported_defaultAlgorithms):
			self.config.defaultAlgorithm = new_defaultAlgorithm
			return True
		return False
	
	def update_config_difficultyLevel(self, new_difficultyLevel):
		if self.config.validateInputType(new_difficultyLevel,\
									self.config.supported_difficultyLevels):
			self.config.difficultyLevel = new_difficultyLevel
			return True
		return False
	
	def save_config_to_file(self, config_file_handler):
		try:
			config_file_handler.create_config_file(self.config)
			return True
		except IOError:
			return False
		except:
			raise
	
	def load_sudoku_from_file(self, file):
		self._reset_input_matrix()
		if self.config.inputType == 'CSV':
			file_handler = io.FileHandlerCSV(file)
		elif self.config.inputType == 'TXT':
			file_handler = io.FileHandlerTXT(file)
		else:
			raise TypeError("Unexpected Type: %s" % self.config.inputType)
		
		matrix = file_handler.import_file()
		self.input_matrix = validmatrix.MatrixHandler(matrix)
		return self.input_matrix.validate()
	
	def export_sudoku_to_file(self, file):
		if self.input_matrix == None:
			return False
		try:
			file_handler = io.FileHandlerTXT(file, 'w')
			file_handler.export_file(self.input_matrix.first_matrix)
			return True
		except IOError:
			return False
		except:
			raise
	
	def solve_sudoku(self):
		if self.input_matrix == None:
			return False
		self._reset_output_matrix()
		try:
			self._set_algorithm()
		except:
			return False
		self.output_matrix = self.algorithm.solve()
		return self.output_matrix != None
	
	def generate_sudoku(self):
		self._reset_input_matrix()
		self.input_matrix = validmatrix.MatrixHandler([])
		try:
			self._set_algorithm()
		except:
			return False
		while True:
			self.input_matrix.generator(self.config.difficultyLevel)
			if self.algorithm.solve() != None:
				break
		return True
