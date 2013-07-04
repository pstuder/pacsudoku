
import csv
from validmatrix import MatrixHandler
from config import Configfile
from xml.dom import minidom

class FileHandler:
	
	def __init__(self, file, mode='r'):
		self.file_name = file
		try:
			self.file = open(self.file_name, mode)
		except:
			print "\nUnable to open file in '%s' mode.\n" % mode
			self.file_name = file.split('.')[0] + '_new.' + file.split('.')[1]
			
			print "Creating a new file %s and open in 'w' mode."\
				% self.file_name
			self.file = open(self.file_name, 'w')
	
	def reopen(self, mode):
		if not self.file.closed:
			self.file.close()
		self.file = open(self.file_name, mode)

class FileHandlerTXT(FileHandler):
	def __init__(self, file, mode='r'):
		FileHandler.__init__(self, file, mode)
		
	def export(self, matrix):
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
		
	def importmatrix(self):
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
		self.xmldoc = minidom.parse(self.file)
	
	def parseconfig(self):
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

class FileHandlerCSV(FileHandler):
	def __init__(self, file, mode='r'):
		FileHandler.__init__(self, file, mode)
	
	def importfile(self):
		selfmatrix=[]
		with self.file as f:
			reader = csv.reader(f)
			for row in reader:
				selfmatrix.append(row)
		return selfmatrix
	

	