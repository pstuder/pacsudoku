import csv
from validmatrix import MatrixHandler
from config import Configfile
from xml.dom import minidom
from os import path

class FileHandler:
	def __init__(self, file, mode='r'):
		dir_name = path.dirname(file)
		if not dir_name:
			dir_name = "."
		if path.exists(dir_name):
			self.file_dir = path.abspath(dir_name)
			self.file_name = path.basename(file)
			try:
				self.file = open(file, mode)
			except:
				splitted_file_name = self.file_name.rsplit('.', 1)
				self.file_name = splitted_file_name[0] + '_new'
				if len(splitted_file_name) > 1:
					self.file_name += '.' + splitted_file_name[1]
				self.file = open(self.file_dir + '/' + self.file_name, 'w')
				self.reopen(mode)
		else:
			raise IOError("Path not found")
	
	def reopen(self, mode):
		if not self.file.closed:
			self.file.close()
		self.file = open(self.file.name, mode)

class FileHandlerTXT(FileHandler):
	def export_file(self, matrix):
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
		#file_to_import = open(self.file, 'r')
		file_imported = self.file.read()
		if file_imported != "":
			return True
		else:
			return False
		self.file.close()
		
	def import_file(self):
		#file_to_import = open(self.file, 'r')
		file_imported = self.file.readlines()
		linematrix = []
		matrix = []
		self.file.close()
		for line in file_imported:
			linematrix.append(line.rstrip())
		for i in  range(len(linematrix)):
			row = linematrix[i]
			rowint=[]
			for j in range(len(row)):
				if row[j] in ['a','b','c','d','e','f','g','h','a','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','S','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
					pass
				else:
					rowint.append(int(row[j]))
			matrix.append(rowint)
		return matrix
	
class FileHandlerXML(FileHandler):
	def __init__(self, file, mode='r'):
		FileHandler.__init__(self, file, mode)
		if 'r' in self.file.mode:
			self.xmldoc = minidom.parse(self.file)
	
	def read_config_file(self):
		if 'w' in self.file.mode:
			raise IOError("File not open for reading")
		inputType = str(self.xmldoc.\
			getElementsByTagName('inputType')[0].childNodes[0].nodeValue)
		outputType = str(self.xmldoc.\
			getElementsByTagName('outputType')[0].childNodes[0].nodeValue)
		defaultAlgorithm = str(self.xmldoc.\
			getElementsByTagName('defaultAlgorithm')[0].childNodes[0].nodeValue)
		difficultyLevel = str(self.xmldoc.\
			getElementsByTagName('difficultyLevel')[0].childNodes[0].nodeValue)
		config = Configfile(inputType, outputType,\
			defaultAlgorithm, difficultyLevel)
		return config

	def create_config_file(self, config):
		if 'r' in self.file.mode:
			raise IOError("File not open for writing")
		self.file.write("<config>\n")
		self.file.write("    <inputType>" + config.inputType +
                                "</inputType>\n")
		self.file.write("    <outputType>" + config.outputType +
                                "</outputType>\n")
		self.file.write("    <defaultAlgorithm>" + config.defaultAlgorithm +
                                "</defaultAlgorithm>\n")
		self.file.write("    <difficultyLevel>" + config.difficultyLevel +
                                "</difficultyLevel>\n")
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

