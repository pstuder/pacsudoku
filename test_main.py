import unittest
from os import remove

from main import Interface
from io import FileHandlerXML, FileHandlerTXT, FileHandlerCSV


class TestInterface(unittest.TestCase):
	def setUp(self):
		self.xml_content1 = [
				"<config>" +
					"<inputType>CSV</inputType>" +
					"<outputType>Console</outputType>" +
					"<defaultAlgorithm>Norvig</defaultAlgorithm>" +
					"<difficultyLevel>Medium</difficultyLevel>" +
				"</config>"
		]
		self.xml_content2 = [
				"<config>" +
					"<inputType>TXT</inputType>" +
					"<outputType>File</outputType>" +
					"<defaultAlgorithm>XAlgorithm</defaultAlgorithm>" +
					"<difficultyLevel>High</difficultyLevel>" +
				"</config>"
		]

		self.xml_file1 = "config1.xml"
		self.xml_file2 = "config2.xml"
		
		with open(self.xml_file1, 'w') as rawfile:
			rawfile.write(self.xml_content1[0])
		with open(self.xml_file2, 'w') as rawfile:
			rawfile.write(self.xml_content2[0])
		
		self.file_handler_xml1 = FileHandlerXML(self.xml_file1)
		self.file_handler_xml2 = FileHandlerXML(self.xml_file2)

		self.expected_tuple_from_file = ("CSV", "Console",\
										"Norvig", "Medium")
		self.expected_tuple_default = ("TXT", "Console",\
										"Backtracking", "Low")
		
		self.sudoku_import_csv = "sudoku.csv"
 		self.sudoku_import_txt = "sudoku.txt"
		self.sudoku_export = "export.txt"

		with open(self.sudoku_import_csv, 'w') as rawfile:			
			rawfile.write('4,0,0,0,0,0,8,0,5\n')
			rawfile.write('0,3,0,0,0,0,0,0,0\n')
			rawfile.write('0,0,0,7,0,0,0,0,0\n')
			rawfile.write('0,2,0,0,0,0,0,6,0\n')
			rawfile.write('0,0,0,0,8,0,4,0,0\n')
			rawfile.write('0,0,0,0,1,0,0,0,0\n')
			rawfile.write('0,0,0,6,0,3,0,7,0\n')
			rawfile.write('5,0,0,2,0,0,0,0,0\n')
			rawfile.write('1,0,4,0,0,0,0,0,0\n')

		with open(self.sudoku_import_txt, 'w') as rawfile:
 			rawfile.write("400000805\n")
 			rawfile.write("030000000\n")
 			rawfile.write("000700000\n")
 			rawfile.write("020000060\n")
 			rawfile.write("000080400\n")
 			rawfile.write("000010000\n")
 			rawfile.write("000603070\n")
 			rawfile.write("500200000\n")
 			rawfile.write("104000000\n")

	def tearDown(self):
		self.file_handler_xml1.file.close()
		self.file_handler_xml2.file.close()
 		try:
 			remove(self.xml_file1)
		except:
			pass
  		try:
 			remove(self.xml_file2)
		except:
			pass
		try:
 			remove(self.sudoku_import_csv)
		except:
			pass
 		try:
 			remove(self.sudoku_import_txt)
		except:
			pass
 		try:
 			remove(self.sudoku_export)
		except:
			pass

	def test_interface_instance_created_with_config_instance_from_file(self):
		actual_interface = Interface(self.file_handler_xml1)
		actual_tuple_from_file = (
			actual_interface.config.inputType,
			actual_interface.config.outputType,
			actual_interface.config.defaultAlgorithm,
			actual_interface.config.difficultyLevel
		)
		self.assertEqual(
			self.expected_tuple_from_file,
			actual_tuple_from_file
		)
	
	def test_interface_instance_created_if_io_error_in_file_handler(self):
		self.file_handler_xml1.reopen('w')
		actual_interface = Interface(self.file_handler_xml1)
		actual_tuple_default = (
			actual_interface.config.inputType,
			actual_interface.config.outputType,
			actual_interface.config.defaultAlgorithm,
			actual_interface.config.difficultyLevel
		)
		self.assertEqual(self.expected_tuple_default, actual_tuple_default)
		
	def test_resetting_input_matrix(self):
		interface = Interface(self.file_handler_xml1)
		interface.input_matrix = "dummy"
		interface._reset_input_matrix()
		self.assertEqual(None, interface.input_matrix)

	def test_resetting_input_matrix_if_none(self):
		interface = Interface(self.file_handler_xml2)
		interface._reset_input_matrix()
		self.assertEqual(None, interface.input_matrix)

	def test_resetting_output_matrix(self):
		interface = Interface(self.file_handler_xml1)
		interface.output_matrix = "dummy"
		interface._reset_output_matrix()
		self.assertEqual(None, interface.output_matrix)

	def test_resetting_output_matrix_if_none(self):
		interface = Interface(self.file_handler_xml2)
		interface._reset_output_matrix()
		self.assertEqual(None, interface.output_matrix)

	def test_resetting_algorithm(self):
		interface = Interface(self.file_handler_xml1)
		interface.algorithm = "dummy"
		interface._reset_algorithm()
		self.assertEqual(None, interface.algorithm)

	def test_resetting_algorithm_if_none(self):
		interface = Interface(self.file_handler_xml2)
		interface._reset_algorithm()
		self.assertEqual(None, interface.algorithm)

	def test_set_same_algorithm(self):
		interface = Interface(self.file_handler_xml1)
		expected_algorithm = interface.config.defaultAlgorithm
		interface._set_algorithm()
		actual_algorithm = interface.algorithm.__class__.__name__
		self.assertEqual(expected_algorithm, actual_algorithm)

	def test_set_new_algorithm(self):
		interface = Interface(self.file_handler_xml2)
		expected_algorithm = "Norvig"
		interface.config.defaultAlgorithm = expected_algorithm
		interface._set_algorithm()
		actual_algorithm = interface.algorithm.__class__.__name__
		self.assertEqual(expected_algorithm, actual_algorithm)

	def test_set_algorithm_raises_type_error_if_invalid(self):
		interface = Interface(self.file_handler_xml1)
		interface.config.defaultAlgorithm = "MyAlgorithm"
		self.assertRaises(TypeError, interface._set_algorithm)

	def test_update_config_input_type(self):
		interface = Interface(self.file_handler_xml1)
		self.assertTrue(interface.update_config_input_type("TXT"))

	def test_update_config_input_type_if_invalid(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(interface.update_config_input_type("DAT"))

	def test_update_config_output_type(self):
		interface = Interface(self.file_handler_xml1)
		self.assertTrue(interface.update_config_output_type("File"))

	def test_update_config_output_type_if_invalid(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(interface.update_config_output_type("Network"))

	def test_update_config_default_algorithm(self):
		interface = Interface(self.file_handler_xml1)
		self.assertTrue(
			interface.update_config_default_algorithm("XAlgorithm")
		)

	def test_update_config_default_algorithm_if_invalid(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(
			interface.update_config_default_algorithm("MyAlgorithm")
		)

	def test_update_config_difficulty_level(self):
		interface = Interface(self.file_handler_xml1)
		self.assertTrue(interface.update_config_difficulty_level("High"))

	def test_update_config_difficulty_level_if_invalid(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(interface.update_config_difficulty_level("Easy"))

	def test_save_config_to_file_returns_true_if_valid(self):
		interface = Interface(self.file_handler_xml1)
		self.file_handler_xml1.reopen('w')
		self.assertTrue(interface.save_config_to_file(self.file_handler_xml1))

	def test_save_config_to_file_returns_false_if_invalid(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(
			interface.save_config_to_file(self.file_handler_xml2)
		)

	def test_load_sudoku_returns_true_for_valid_matrix_in_csv(self):
		interface = Interface(self.file_handler_xml1)
		self.assertTrue(
			interface.load_sudoku_from_file(self.sudoku_import_csv)
		)

	def test_load_sudoku_returns_true_for_valid_matrix_in_txt(self):
		interface = Interface(self.file_handler_xml2)
		self.assertTrue(
			interface.load_sudoku_from_file(self.sudoku_import_txt)
		)

	def test_load_sudoku_returns_false_if_matrix_has_no_valid_format(self):
		interface = Interface(self.file_handler_xml1)
		self.assertFalse(
			interface.load_sudoku_from_file(self.sudoku_import_txt)
		)

	def test_load_sudoku_matrix_raises_exception_if_unexpected_type(self):
		interface = Interface(self.file_handler_xml2)
		interface.config.inputType = "DAT"
		self.assertRaises(TypeError, interface.load_sudoku_from_file, "")

	def test_solve_sudoku_returns_false_if_no_matrix_loaded(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(interface.solve_sudoku())

	def test_solve_sudoku_returns_false_if_unsupported_algorithm(self):
		interface = Interface(self.file_handler_xml1)
		interface.load_sudoku_from_file(self.sudoku_import_txt)
		interface.config.defaultAlgorithm = "MyAlgorithm"
		self.assertFalse(interface.solve_sudoku())

	def test_solve_sudoku_returns_true_if_solved(self):
		interface = Interface(self.file_handler_xml1)
		interface.load_sudoku_from_file(self.sudoku_import_txt)
		self.assertTrue(interface.solve_sudoku())

	def test_generate_sudoku_returns_false_if_unsupported_algorithm(self):
		interface = Interface(self.file_handler_xml2)
		interface.config.defaultAlgorithm = "MyAlgorithm"
		self.assertFalse(interface.generate_sudoku())

#	def test_generate_sudoku_returns_true_if_matrix_generated(self):
#		interface = Interface(self.file_handler_xml1)
#		self.assertTrue(interface.generate_sudoku())

	def test_export_sudoku_returns_true_if_valid_file_path(self):
		interface = Interface(self.file_handler_xml1)
		interface.load_sudoku_from_file(self.sudoku_import_csv)	
		interface.solve_sudoku()
		self.assertTrue(interface.export_sudoku_to_file(self.sudoku_export))

	def test_export_sudoku_returns_false_if_invalid_file_path(self):
		interface = Interface(self.file_handler_xml1)
		interface.load_sudoku_from_file(self.sudoku_import_csv)
		interface.solve_sudoku()
		self.assertFalse(interface.export_sudoku_to_file("/test/no"))

	def test_export_sudoku_returns_false_if_no_matrix_loaded(self):
		interface = Interface(self.file_handler_xml2)
		self.assertFalse(interface.export_sudoku_to_file(self.sudoku_export))


if __name__ == "__main__":
	unittest.main()
