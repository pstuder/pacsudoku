import unittest
import csv
from validmatrix import MatrixHandler
from io import FileHandler, FileHandlerXML, FileHandlerTXT,FileHandlerCSV
from config import Configfile

class TestFileHandlerTXT(unittest.TestCase):
 	def setUp(self):
 		self.matrix = [[4, 1, 7, 3, 6, 9, 8, 2, 5],\
 						[6, 3, 2, 1, 5, 8, 9, 4, 7],\
 						[9, 5, 8, 7, 2, 4, 3, 1, 6],\
 						[8, 2, 5, 4, 3, 7, 1, 6, 9],\
 						[7, 9, 1, 5, 8, 6, 4, 3, 2],\
 						[3, 4, 6, 9, 1, 2, 7, 5, 8],\
 						[2, 8, 9, 6, 4, 3, 5, 7, 1],\
 						[5, 7, 3, 2, 9, 1, 6, 8, 4],\
 						[1, 6, 4, 8, 7, 5, 2, 9, 3]]
 		
 		with open("export_expected.txt") as file:
 			self.txt_content_expected = file.readlines()
 		
 		self.file_actual = "export_actual.txt"
 		self.file_import = FileHandlerTXT("sudoku_import.txt",'r')
 	
 	def test_export_matrix_to_txt(self):
 		txthandler = FileHandlerTXT(self.file_actual,'w')
 		txthandler.export(self.matrix)
 		with open(self.file_actual) as file:
 			txt_content_actual = file.readlines()
 		
 		self.assertEqual(self.txt_content_expected,txt_content_actual)
 
 	def test_export_txt_and_close(self):
 		txthandler = FileHandlerTXT(self.file_actual, 'w')
 		txthandler.export(self.matrix)
 		self.assertTrue(txthandler.file.closed)
 		
 	def test_exporting_to_txt_file_in_read_mode(self):
 		txthandler = FileHandlerTXT(self.file_actual)
 		self.assertRaises(IOError, txthandler.export, self.matrix)
 		
 	#-------------------------------------------
 	
		
	def test_file_to_import_is_not_empty(self):
		notemptyfile = self.file_import.not_empty()
		self.assertEqual(True, notemptyfile)
		
	def test_file_imported_will_create_a_list_with_9_elements(self):
		listlenght = len(self.file_import.importmatrix())
		self.assertEqual(9, listlenght)
		
class TestFileHandlerXML(unittest.TestCase):
	def setUp(self):
		self.expected_config = Configfile()
	
	def test_config_instance_is_created(self):
		xmlhandler = FileHandlerXML("config_expected.xml")
		actual_config = xmlhandler.parseconfig()
		self.assertEqual(('CSV', 'Console', 'Peter Norvig', 'Medium'),\
			(actual_config.inputType, actual_config.outputType,\
			actual_config.defaultAlgorithm, actual_config.difficultyLevel))
		
		

class TestFileHandler(unittest.TestCase):
	def setUp(self):
		self.file_valid = "valid_file.txt"
		with open(self.file_valid, 'w') as file:
			file.write('')
		
		self.file_invalid = "invalid_file.txt"
		self.file_invalid_expected = "invalid_file_new.txt"
		self.expected_mode = "r"
	
	def test_open_valid_file(self):
		actual_handler = FileHandler(self.file_valid)
		self.assertEqual(self.file_valid, actual_handler.file.name)
	
	def test_open_invalid_file(self):
		actual_handler = FileHandler(self.file_invalid)
		self.assertEqual(self.file_invalid_expected, actual_handler.file.name)
	
	def test_reopening(self):
		handler = FileHandler(self.file_valid, 'w')
		handler.reopen(self.expected_mode)
		actual_mode = handler.file.mode
		self.assertEqual(self.expected_mode, actual_mode)

class TestFileHandlerCSV(unittest.TestCase):
	def setUp(self):
		self.file_valid = "valid_file.csv"
		with open(self.file_valid, 'w') as file1:			
			file1.write('4,0,0,0,0,0,8,0,5\n')
			file1.write('0,3,0,0,0,0,0,0,0\n')
			file1.write('0,0,0,7,0,0,0,0,0\n')
			file1.write('0,2,0,0,0,0,0,6,0\n')
			file1.write('0,0,0,0,8,0,4,0,0\n')
			file1.write('0,0,0,0,1,0,0,0,0\n')
			file1.write('0,0,0,6,0,3,0,7,0\n')
			file1.write('5,0,0,2,0,0,0,0,0\n')
			file1.write('1,0,4,0,0,0,0,0,0\n')
		file1.close()
		#file_handler_internal=FileHandler("valid_file.csv","r")
		self.input_file=FileHandlerCSV("valid_file.csv","r")
		self.file_invalid = "invalid_file.csv"
		self.file_invalid_expected = "invalid_file_new.csv"
		self.expected_mode = "r"
	
	def test_CSV_file_retirns_the_content_in_a_matrix(self):
		expected_result=[['4','0','0','0','0','0','8','0','5'],['0','3','0','0','0','0','0','0','0'],['0','0','0','7','0','0','0','0','0'],['0','2','0','0','0','0','0','6','0'],['0','0','0','0','8','0','4','0','0'],['0','0','0','0','1','0','0','0','0'],['0','0','0','6','0','3','0','7','0'],['5','0','0','2','0','0','0','0','0'],['1','0','4','0','0','0','0','0','0']]
		self.assertEqual(expected_result, self.input_file.importfile())

if __name__ == "__main__":
	unittest.main()
