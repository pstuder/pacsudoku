import unittest
import csv
from os import remove, path
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
 		
 		self.txt_content_expected = [  "417369825\n",\
 										"632158947\n",\
 										"958724316\n",\
 										"825437169\n",\
 										"791586432\n",\
 										"346912758\n",\
 										"289643571\n",\
 										"573291684\n",\
 										"164875293\n"  ]

 		self.file_actual = "export_actual.txt"
 		self.file_expected = "export_expected.txt"

		with open(self.file_expected, 'w') as rawfile:
			for row in self.txt_content_expected:
				rawfile.write(row)

 		self.content_sudoku_import = [ "400000805\n",\
 										"030000000\n",\
 										"000700000\n",\
 										"020000060\n",\
 										"000080400\n",\
 										"000010000\n",\
 										"000603070\n",\
 										"500200000\n",\
 										"104000000\n" ]

 		self.file_sudoku_import = "sudoku_import.txt"
 		
		with open(self.file_sudoku_import, 'w') as rawfile:
			for row in self.content_sudoku_import:
				rawfile.write(row)
		
 		self.file_import = FileHandlerTXT(self.file_sudoku_import,'r')
 	
 	def tearDown(self):
 		self.file_import.file.close()
 		try:
 			remove(self.file_expected)
		except:
			pass
 		try:
			remove(self.file_actual)
		except:
			pass
 		try:
			remove(self.file_sudoku_import)
		except:
			pass
	
 	def test_export_matrix_to_txt(self):
 		txthandler = FileHandlerTXT(self.file_actual,'w')
 		txthandler.export_file(self.matrix)
 		with open(self.file_actual) as file:
 			txt_content_actual = file.readlines()
 		self.assertEqual(self.txt_content_expected,txt_content_actual)
	
 	def test_export_txt_and_close(self):
 		txthandler = FileHandlerTXT(self.file_actual, 'w')
 		txthandler.export_file(self.matrix)
 		self.assertTrue(txthandler.file.closed)
	
 	def test_exporting_to_txt_file_in_read_mode(self):
 		txthandler = FileHandlerTXT(self.file_expected)
 		self.assertRaises(IOError, txthandler.export_file, self.matrix)
 	
	# -----------------------------------------------------------------

	def test_file_to_import_is_not_empty(self):
		notemptyfile = self.file_import.not_empty()
		self.assertEqual(True, notemptyfile)
		
	def test_file_imported_will_create_a_list_with_9_elements(self):
		listlenght = len(self.file_import.import_file())
		self.assertEqual(9, listlenght)
		
	def test_file_import_will_creat_a_9x9_matrix(self):
		matrix_imported =self.file_import.import_file()
		matrix_expected = [[4,0,0,0,0,0,8,0,5],[0,3,0,0,0,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,2,0,0,0,0,0,6,0],[0,0,0,0,8,0,4,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,6,0,3,0,7,0],[5,0,0,2,0,0,0,0,0],[1,0,4,0,0,0,0,0,0]]
		self.assertEqual(matrix_imported, matrix_expected)

class TestFileHandlerXML(unittest.TestCase):
	def setUp(self):
		self.expected_xml_content = ["<config>\n",\
					"    <inputType>CSV</inputType>\n",\
					"    <outputType>Console</outputType>\n",\
					"    <defaultAlgorithm>Norvig</defaultAlgorithm>\n",\
					"    <difficultyLevel>Medium</difficultyLevel>\n",\
									"</config>"]
		
		self.expected_tuple = ("CSV", "Console", "Norvig", "Medium")
		self.expected_config = Configfile()
		self.custom_config = Configfile(*self.expected_tuple)
		
		self.file_expected = "config_expected.xml"
		self.file_actual = "config_actual.xml"
		
		with open(self.file_expected, 'w') as rawfile:
			for row in self.expected_xml_content:
				rawfile.write(row)
	
 	def tearDown(self):
 		try:
 			remove(self.file_expected)
		except:
			pass
 		try:
			remove(self.file_actual)
		except:
			pass
	
 	def test_parse_config_in_write_mode(self):
 		xmlhandler = FileHandlerXML(self.file_actual, 'w')
 		self.assertRaises(IOError,	xmlhandler.read_config_file)
	
	def test_config_instance_is_created(self):
		xmlhandler = FileHandlerXML(self.file_expected)
		actual_config = xmlhandler.read_config_file()
		self.assertEqual(self.expected_tuple,\
			(actual_config.inputType, actual_config.outputType,\
			actual_config.defaultAlgorithm, actual_config.difficultyLevel))
		
	def test_config_file_is_created(self):
		xmlhandler = FileHandlerXML(self.file_actual,'w')
		xmlhandler.create_config_file(self.custom_config)
		with open(self.file_actual) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual(actual_xml_content, self.expected_xml_content)

 	def test_save_config_and_close(self):
 		xmlhandler = FileHandlerXML(self.file_actual, 'w')
 		xmlhandler.create_config_file(self.custom_config)
 		self.assertTrue(xmlhandler.file.closed)
 		
 	def test_save_config_in_read_mode(self):
 		xmlhandler = FileHandlerXML(self.file_expected)
 		self.assertRaises(IOError,\
			xmlhandler.create_config_file, self.custom_config)

class TestFileHandler(unittest.TestCase):
	def setUp(self):
		self.file_valid = "valid_file.txt"
		self.file_invalid = "invalid_file.txt"
		self.file_invalid_expected = "invalid_file_new.txt"
		self.file_in_valid_dir = path.abspath("myfile")
		self.file_in_invalid_dir = "/non-existent/myfile"
		self.valid_dir = path.abspath(".")
		self.expected_mode = "r"
		
		with open(self.file_valid, 'w') as file:
			file.write('')
 	
	def tearDown(self):
		try:
			remove(self.file_valid)
		except:
			pass
		try:
			remove(self.file_invalid_expected)
		except:
			pass
		try:
			remove(self.file_in_valid_dir)
		except:
			pass
	
	def test_open_valid_file(self):
		actual_handler = FileHandler(self.file_valid)
		self.assertEqual(self.file_valid, actual_handler.file_name)
	
	def test_open_invalid_file(self):
		actual_handler = FileHandler(self.file_invalid)
		self.assertEqual(self.file_invalid_expected, actual_handler.file_name)
	
	def test_open_valid_dir(self):
		actual_handler = FileHandler(self.file_in_valid_dir)
		self.assertEqual(self.valid_dir, actual_handler.file_dir)
	
	def test_open_invalid_dir(self):
		self.assertRaises(IOError, FileHandler, self.file_in_invalid_dir)
	
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
		
		self.input_file=FileHandlerCSV(self.file_valid,"r")
 	
 	def tearDown(self):
 		self.input_file.file.close()
 		try:
 			remove(self.file_valid)
		except:
			pass
	
	def test_CSV_file_returns_the_content_in_a_matrix(self):
		expected_result=[[4,0,0,0,0,0,8,0,5]\
						,[0,3,0,0,0,0,0,0,0]\
						,[0,0,0,7,0,0,0,0,0]\
						,[0,2,0,0,0,0,0,6,0]\
						,[0,0,0,0,8,0,4,0,0]\
						,[0,0,0,0,1,0,0,0,0]\
						,[0,0,0,6,0,3,0,7,0]\
						,[5,0,0,2,0,0,0,0,0]\
						,[1,0,4,0,0,0,0,0,0]]
		self.assertEqual(expected_result, self.input_file.import_file())

if __name__ == "__main__":
	unittest.main()
