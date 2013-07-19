import unittest
from sys import argv
from os import remove, path
from subprocess import Popen, PIPE

from pacsudoku import SudokuArgumentParser, main


class TestPACSudokuScript(unittest.TestCase):
	def setUp(self):
		self.default_output = "" +\
			"\r\n\r\nStarting the console user interface ...\r\n" +\
		""
		self.expected_gui_output = "" +\
			"\r\n\r\nStarting the graphical user interface ...\r\n" +\
		""
		self.expected_help_output = "" +\
			"usage: pacsudoku [-h] [-c XML] [-g]\r\n" +\
			"\r\n" +\
			"Play PAC Sudoku using console or user interface.\r\n" +\
			"\r\n" +\
			"optional arguments:\r\n" +\
			"  -h, --help            show this help message and exit\r\n" +\
			"  -c XML, --config XML  XML Config File to be used. " +\
									"Defaults to 'config.xml'\r\n" +\
			"  -g, --gui             Launch PAC Sudoku grapical user " +\
									"interface\r\n" +\
			"\r\n" +\
			"----------------------------------------------------\r\n" +\
			"Sudoku project developed in Python. It features:\r\n" +\
			"\r\n" +\
			"- Load sudoku from TXT or CSV\r\n" +\
			"- Solve interactively using console or UI\r\n" +\
			"- Get hints during play\r\n" +\
			"- Export solution to TXT or display in console\r\n" +\
			"- Solver supporting 3 algorithms:\r\n" +\
			"    * Backtracking\r\n" +\
			"    * Peter Novig\r\n" +\
			"    * X Algorithm\r\n" +\
			"\r\n" +\
			"Authors: Ariel Dorado, Claudia Mercado, Pablo Studer\r\n" +\
			"----------------------------------------------------\r\n" +\
		""
		self.expected_xml_content = [
			"<config>\n",
			"    <inputType>CSV</inputType>\n",
			"    <outputType>Console</outputType>\n",
			"    <defaultAlgorithm>Norvig</defaultAlgorithm>\n",
			"    <difficultyLevel>Medium</difficultyLevel>\n",
			"</config>"
		]
		self.expected_tuple = ("CSV", "Console", "Norvig", "Medium")
		self.my_config_file = "my_config.xml"
		self.invalid_config_file = "invalid_config.xml"
		self.empty_config_file = "empty_config.xml"
		self.default_config_file = "config.xml"
		with open(self.my_config_file, 'w') as rawfile:
			for row in self.expected_xml_content:
				rawfile.write(row)
		with open(self.empty_config_file, 'w') as rawfile:
			pass

	def tearDown(self):
 		try:
 			remove(self.my_config_file)
		except:
			pass
 		try:
 			remove(self.invalid_config_file)
		except:
			pass
 		try:
 			remove(self.empty_config_file)
		except:
			pass
 		try:
 			remove(self.default_config_file)
		except:
			pass

	def test_sudoku_argument_parser_class_default(self):
		parser = SudokuArgumentParser()
		actual_arguments = parser.parse_args()
		self.assertEqual(self.default_config_file, actual_arguments.config)
		self.assertFalse(actual_arguments.gui)
		
	def test_sudoku_argument_parser_class_with_arguments(self):
		expected_config_metavar = "other.xml"
		argv.append("-g")
		argv.append("-c")
		argv.append(expected_config_metavar)
		parser = SudokuArgumentParser()
		actual_arguments = parser.parse_args()
		argv.pop()
		argv.pop()
		argv.pop()
		self.assertEqual(expected_config_metavar, actual_arguments.config)
		self.assertTrue(actual_arguments.gui)
		
	def test_main_with_valid_config_file(self):
		argv.append("-c")
		argv.append(self.my_config_file)
		main()
		with open(self.my_config_file) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual(self.expected_xml_content, actual_xml_content)
		argv.pop()
		argv.pop()

	def test_run_game_since_cmd_line_with_valid_config_file(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py",
				"-c",
				self.my_config_file
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.default_output, actual_output)

	def test_main_with_invalid_config_file(self):
		argv.append("-c")
		argv.append(self.invalid_config_file)
		main()
		with open(self.invalid_config_file) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual([], actual_xml_content)
		argv.pop()
		argv.pop()

	def test_run_game_since_cmd_line_with_invalid_config_file(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py",
				"-c",
				self.invalid_config_file
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.default_output, actual_output)
		
	def test_main_with_empty_config_file(self):
		argv.append("-c")
		argv.append(self.empty_config_file)
		main()
		with open(self.empty_config_file) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual([], actual_xml_content)
		argv.pop()
		argv.pop()

	def test_run_game_since_cmd_line_with_empty_config_file(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py",
				"-c",
				self.empty_config_file
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.default_output, actual_output)
		
	def test_main_with_no_arguments(self):
		main()
		with open(self.default_config_file) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual([], actual_xml_content)
	
	def test_run_game_since_cmd_line_with_no_arguments(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py"
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.default_output, actual_output)
		
	def test_main_with_gui_argument(self):
		argv.append("-g")
		main()
		with open(self.default_config_file) as rawfile:
			actual_xml_content = rawfile.readlines()
		self.assertEqual([], actual_xml_content)
		argv.pop()
	
	def test_launch_game_with_argument_gui(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py",
				"-g"
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.expected_gui_output, actual_output)
		
	def test_show_help(self):
		proc = Popen(
			[
				"python",
				"../source/pacsudoku.py",
				"-h"
			],
			stdout=PIPE,
			shell=True
		)
		(actual_output, actual_err) = proc.communicate()
		self.assertEqual(None, actual_err)
		self.assertEqual(self.expected_help_output, actual_output)

