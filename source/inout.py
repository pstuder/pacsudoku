import csv
from os import path
from xml.dom import minidom

from validmatrix import MatrixHandler
from config import Configfile


class FileHandler:
	"""Common File Handler class for file specific tasks"""
	def __init__(self, file, mode='r'):
		"""Initializes a new File Handler
		
		The following instance attributes are created:
		file_dir -- Absolute path of the directory where the file resides
		file_name -- The file name
		file -- The file object using file and mode (default 'r')
		
		If file can't be opened in mode, a new file, with name file_new
		is created and reopened in mode.
		
		Raise IOError if directory does not exist.

		"""
		dir_name = path.dirname(file)
		if not dir_name:
			dir_name = "."
		if path.exists(dir_name):
			self.file_dir = path.abspath(dir_name)
			self.file_name = path.basename(file)
			try:
				self.file = open(file, mode)
			except IOError:
				splitted_file_name = self.file_name.rsplit('.', 1)
				self.file_name = splitted_file_name[0] + '_new'
				if len(splitted_file_name) > 1:
					self.file_name += '.' + splitted_file_name[1]
				self.file = open(self.file_dir + '/' + self.file_name, 'w')
				self.reopen(mode)
		else:
			raise IOError("Path not found")
	
	def reopen(self, mode):
		"""Closes current file, if open, and reopens file in new mode"""
		if not self.file.closed:
			self.file.close()
		self.file = open(self.file.name, mode)


class FileHandlerTXT(FileHandler):
	"""File Handler specific for operation on TXT files."""
	def export_file(self, matrix):
		"""Exports matrix to current TXT file.
		
		Raises IOError if file is open for writing.
		
		"""
		if 'r' in self.file.mode:
			raise IOError("File not open for writing")
		else:
			for row in matrix:
				line = ''
				for digit in row:
					line += str(digit)
				line += '\n'
				self.file.write(line)
			self.file.close()

	def not_empty(self):
		"""
		Verify if file to import is not empty.
		
		"""
		file_imported = self.file.read()
		if file_imported != "":
			return True
		self.file.close()
		return False
		
	def import_file(self):
		"""
		Creates Sudoku matrix with values imported from
		TXT file.
		
		"""
		file_imported = self.file.readlines()
		linematrix = []
		matrix = []
		exception_lower_chars = 'abcdefghijklmnopqrstuvwxyz'
		exception_caption_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.file.close()
		for line in file_imported:
			linematrix.append(line.rstrip())
		for i in  range(len(linematrix)):
			row = linematrix[i]
			rowint = []
			for j in range(len(row)):
				if row[j] in (exception_lower_chars + exception_caption_chars):
					pass
				else:
					rowint.append(int(row[j]))
			matrix.append(rowint)
		return matrix


class FileHandlerXML(FileHandler):
	"""File Handler specific for operation on XML files."""
	def __init__(self, file, mode='r'):
		"""Initializes a new XML File Handler.
		
		It first calls parent FileHandler initializator. Additionally
		it creates a minidom parsed XML document instance: xmldoc.
		
		"""
		FileHandler.__init__(self, file, mode)
		if 'r' in self.file.mode:
			self.xmldoc = minidom.parse(self.file)
	
	def read_config_file(self):
		"""Returns a new Configfile using current file values as input.
		
		Raises IOError if current file is open for writing.
		
		"""
		if 'w' in self.file.mode:
			raise IOError("File not open for reading")
		input_type = str(
			self.xmldoc.getElementsByTagName('inputType')[0].\
															childNodes[0].\
																nodeValue
		)
		output_type = str(
			self.xmldoc.getElementsByTagName('outputType')[0].\
															childNodes[0].\
																nodeValue
		)
		default_algorithm = str(
			self.xmldoc.getElementsByTagName('defaultAlgorithm')[0].\
															childNodes[0].\
																nodeValue
		)
		difficulty_level = str(
			self.xmldoc.getElementsByTagName('difficultyLevel')[0].\
															childNodes[0].\
																nodeValue
		)
		config = Configfile(input_type, output_type,
							default_algorithm, difficulty_level)
		return config

	def create_config_file(self, config):
		"""Creates a new config file using config values.
		
		Raises IOError if current file is open for reading.
		
		"""
		if 'r' in self.file.mode:
			raise IOError("File not open for writing")
		self.file.write("<config>\n")
		
		self.file.write(
			"    <inputType>" +
			config.inputType +
			"</inputType>\n"
		)
		self.file.write(
			"    <outputType>" +
			config.outputType +
			"</outputType>\n"
		)
		self.file.write(
			"    <defaultAlgorithm>" +
			config.defaultAlgorithm +
			"</defaultAlgorithm>\n"
		)
		self.file.write(
			"    <difficultyLevel>" +
			config.difficultyLevel +
			"</difficultyLevel>\n"
		)
		
		self.file.write("</config>")
		self.file.close()

class FileHandlerCSV(FileHandler):
	def import_file(self):
		selfmatrix=[]
		selfmatrixaux=[]
		with self.file as f:
			reader = csv.reader(f)
			if reader!="":
				for row in reader:
					for a in range(len(row)):
						selfmatrixaux.append(int(row[a]))
					selfmatrix.append(selfmatrixaux)
					selfmatrixaux=[]
		return selfmatrix

