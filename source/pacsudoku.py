import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from os import path
from xml.parsers.expat import ExpatError

from inout import FileHandlerXML
from sudokuconsole import SudokuConsoleUserInterface
from sudokugui import SudokuGraphicalUserInterface


class SudokuArgumentParser(ArgumentParser):
	"""Argument Parser for the PAC Sudoku game."""
	def __init__(self):
		"""Initializes a sudoku argument parser instance.
		
		Uses RawDescriptionHelpFormatter as formatter class for epilog.
		epilog contains the information about the project and its authors.
		Construct parser using the following optional arguments:
		-g, --gui -- To start sudoku game in GUI mode.
		-c XML, --config XML -- To use XML file as config.
		
		If optional arguments are not specified, game will start in console
		mode and will use default 'config.xml' file.
		
		If the config file specified (or default config.xml) does not exist,
		create a new empty file.
		
		To save config to this file use main.Interface.save_config_to_file
		attribute method.

		"""
		ArgumentParser.__init__(
			self,
			formatter_class=RawDescriptionHelpFormatter,
			prog="pacsudoku",
			description="Play PAC Sudoku using console or user interface.",
			epilog=textwrap.dedent('''\
				
				----------------------------------------------------
				Sudoku project developed in Python. It features:
				
				- Load sudoku from TXT or CSV
				- Solve interactively using console or UI
				- Get hints during play
				- Export solution to TXT or display in console
				- Solver supporting 3 algorithms:
				    * Backtracking
				    * Peter Novig
				    * X Algorithm
				
				Authors: Ariel Dorado, Claudia Mercado, Pablo Studer
				----------------------------------------------------
				
			''')
		)
		self.add_argument(
			'-c',
			'--config',
			metavar= 'XML',
			default='config.xml',
			help="XML Config File to be used. Defaults to 'config.xml'"
			
		)
		self.add_argument(
			'-g',
			'--gui',
			help="Launch PAC Sudoku grapical user interface",
			action="store_true"
		)


if __name__ == "__main__":
	parser = SudokuArgumentParser()
	args = parser.parse_args()
	config_file_name = args.config
	if path.exists(config_file_name):
		try:
			config_file_handler = FileHandlerXML(config_file_name)
		except ExpatError:
			config_file_handler = FileHandlerXML(config_file_name, 'w')
	else:
		config_file_handler = FileHandlerXML(config_file_name, 'w')
	if args.gui:
		pacsudoku = SudokuGraphicalUserInterface(config_file_handler)
	else:
		pacsudoku = SudokuConsoleUserInterface(config_file_handler)	
	
	# Run the game!
	pacsudoku.run()

