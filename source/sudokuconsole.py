"""This module implements the SudokuConsoleUserInterface. 
Used to play sudoku from console.
"""
from copy import deepcopy
from datetime import datetime
from inout import FileHandlerXML
import os, time
from os import path


from main import Interface
from sudokuinteractive import SudokuInteractive
from validmatrix import MatrixHandler

class SudokuConsoleUserInterface(Interface):
	"""Console class for the PAC Sudoku game.
		
		Creates main manu to play Sudoku and user will able to
		import a game form txt or csv files, generate a game, change settings,
		save and load a game, solve Sudoku interactive etc.
		
	"""
	def __init__(self, config_file_handler):
		Interface.__init__(self, config_file_handler)
		self.config_file_handler = config_file_handler
		self.time = 0
		self.recovered_time = 0
		self.loaded_game = False
		self.blank_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 0]]
		
	def importgame(self):
		""" Import a game form a TXT file or CSC file displaying matrix in console."""
		self.header(" IMPORT GAME  ")
		print'Default file format ', self.config.inputType
		path_txt_file = raw_input("Insert Path: " )
		sizepath = len(path_txt_file)
		extensionfile = path_txt_file[sizepath-3:]
		print(' ')
		while self.load_sudoku_from_file(path_txt_file) == False or\
		 	extensionfile.upper() != self.config.inputType:
			path_txt_file = raw_input("Insert valid Path: " )
			sizepath = len(path_txt_file)
			extensionfile = path_txt_file[sizepath-3:]
			print extensionfile
		self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
		self.time = self.interactive.game_start()
		self.interactivegame("")
	
	def gameoutput(self):
		"""
			Select if game will be displaying in Console 
			or will be exported according config file and calls
			gamesolved() which print matrix solved in Console or
			calls outputgametofile() to export game solved in a file.
		"""
		if self.config.outputType == 'Console':
			self.gamesolved()
		self.outputgametofile()
		
	def gamesolved(self):
		"""Print Sudoku solved in console."""
		if self.solve_sudoku() == True:
			self.header(" SUDOKU GAME  ")
			self.output_matrix.printmatrix()
			print(' ')
			print'Game message:     '
			print'Game solved by ', self.config.defaultAlgorithm, ' algorithm.'
			print(' ')
			print('        1) Save Game')
			print('        2) Return to main menu')
			print(' ')
			print(' Please select from the following options: ')
			choicegamesolved = raw_input(" ")
			if choicegamesolved == '1':
				self.outputgametofile()
			else:
				self.sudokumenu("")
		else:
			self.sudokumenu("Sudoku unsolvable, generate another.")
	
	def outputgametofile(self):
		"""Export game solved to file."""
		self.header(" EXPORT GAME SOLVED ")
		print(' ')
		print('Type file name to export game solved:')
		exportpath = raw_input(" ")
		
		if self.export_sudoku_to_file(exportpath) == True:
			print(' ')
			print'Game was exported correctly in: \n', path.abspath(exportpath)
			print(' ')
			self.sudokumenu("")
		else:
			print('Game was not saved, because path not exists or access permissions, try again please')
			self.gamesolved()
			
			
			
	def generategame(self):
		"""Generates a Sudoku game."""
		self.mesage("Please wait until the game will be generated. ")
		if self.generate_sudoku() == True:
			self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
			self.time = self.interactive.game_start()
			self.interactivegame("")
		else:
			self.sudokumenu("Sudoku unsolvable, generate another.")
	
	def changesettings(self):
		"""Change settings menu."""
		self.configfilesettings()
		print(" ")
		settings_menu = '        1) Change Settings\n'+\
						'        2) Return to main menu\n'
						
		print(" ")
		print(' Please select from the following options: ')
		print(" ")
		self.menu(settings_menu)
		
		choiceconfigfile = raw_input(" ")
		
		if choiceconfigfile == '1':
			print(" ")
			print "Select a letter to change settings"
			choicesetting = raw_input(" ")
			print(" ")
			if choicesetting == 'a':
				self.savesettings("TXT")
			
			if choicesetting == 'b':
				self.savesettings("CSV")
			
			if choicesetting == 'c':
				self.savesettings("Console")
			
			if choicesetting == 'd':
				self.savesettings("File")
			
			if choicesetting == 'e':
				self.savesettings("Backtracking")
			
			if choicesetting == 'f':
				self.savesettings("Norvig")
			
			if choicesetting == 'g':
				self.savesettings("XAlgorithm")
			if choicesetting == 'h':
				self.savesettings("Low")
			if choicesetting == 'i':
				self.savesettings("Medium")
			
			if choicesetting == 'j':
				self.savesettings("High")
		else:
			self.sudokumenu("")
		
		
	def savesettings(self, valueset):
		"""Change default values with custom values."""
		self.configfilesettings()
		print(' ')
		input_menu = '        1) Save\n'+\
				'        2) Return to main menu\n'
		
		print(' Please select from the following options ')
		print(' ')
		self.menu(input_menu)
		choicesettings = raw_input(" ")
		
		if choicesettings == '1':
			if self.update_config_input_type(valueset) != False:
				self.config.inputType = valueset
			if  self.update_config_output_type(valueset) != False:
				self.config.outputType = valueset
			if self.update_config_default_algorithm(valueset) != False:
				self.config.defaultAlgorithm = valueset
			if self.update_config_difficulty_level(valueset) != False:
				self.config.difficultyLevel = valueset
			if self.save_config_to_file(self.config_file_handler) == True:
					print(' ')
					print('Settings were saved correctly ')
					self.changesettings()
					print(' ')
					
		else:
			self.sudokumenu('Settings were not saved correctly, please try again ')
	
	
	def configfilesettings(self):
		"""Display config values set by default an allow to change them."""
		self.header(" CHANGE SETTINGS  ")
		print('')
		print('1) Input File Type')
		if self.config.inputType == 'TXT':
			print 'a) (x)', self.config.inputType
			print('b) ( ) CSV')
		else:
			print('a) () TXT')
			print 'b) (x)', self.config.inputType
		print('')
		
		print('2) Output Type') 
		if self.config.outputType == 'Console':
			print'c) (x)', self.config.outputType
			print('d) ( ) File')
		else:
			print('c) ( ) Console')
			print'd) (x)', self.config.outputType
		
		print('')
		print('3) Algorithm')
		if self.config.defaultAlgorithm == 'Backtracking':
			print 'e) (x)', self.config.defaultAlgorithm
			print('f) ( ) Norvig')
			print('g) ( ) XAlgorithm')
		elif self.config.defaultAlgorithm == 'Norvig':
			print('e) ( ) Backtracking')
			print 'f) (x)', self.config.defaultAlgorithm
			print('g) ( ) XAlgorithm')
		else:
			print('e) ( ) Backtracking')
			print('f) ( ) Norvig')
			print 'g) (x)', self.config.defaultAlgorithm
		
		print('')
		print('4) Difficult Level')
		if self.config.difficultyLevel == 'Low':
			print 'h) (x)', self.config.difficultyLevel
			print('i) ( ) Medium')
			print('j) ( ) High')
		elif  self.config.difficultyLevel == 'Medium':
			print('h) ( ) Low')
			print 'i) (x)', self.config.difficultyLevel
			print('j) ( ) High')
		else:
			print('h) ( ) Low')
			print('i) ( ) Medium')
			print'j) (x)', self.config.difficultyLevel
		
	def interactivegame(self, input_mesage):
		"""Interactive module menu. """
		self.set_time()
		self.interactive.matrix.printmatrix()
		self.body(input_mesage)
		print(' Please select from the following options: ')
		choiceinteractive = raw_input(" ")
		if choiceinteractive not in ['1', '2', '3', '4', '5', '6']:
			self.interactivegame("Select the proper option")
		if choiceinteractive == '1':
			self.gamesolved()
		elif choiceinteractive == '2':
			self.changecellvalue()
		elif choiceinteractive == '3':
			if self.interactive.matrix.zero_count(
										self.interactive.matrix.first_matrix
										) != 0:
				position_x, position_y = self.interactive.solve_one() 
				msg = "Solved position: " + str(position_x) + "," + str(position_y)
			else:
				msg = "Solved SUDOKU "
			self.interactivegame(msg)
		elif choiceinteractive == '4':
			self.savegame("")
		elif choiceinteractive == '5':
			self.restartgame()
		else:
			self.sudokumenu("")
		
	def sudokumenu(self, input_message):
		"""Print main menu for PacSudoku game"""
		self.bmatrix = MatrixHandler(self.blank_matrix)
		self.loaded_game = False
		self.header("PACSUDOKU  ")	
		self.bmatrix.printmatrix()
		print('')
		print('               MENU                    ')
		input_menu =	'        1) Import Game\n'+\
				'        2) Load Saved Game\n'+\
				'        3) Generate Game\n'+\
				'        4) Change Settings\n'+\
				'        5) Exit\n'
		self.mesage(input_message)
		self.menu(input_menu)
		print(' ')
		print(' Please select from the previous options ')
		choice = raw_input(" ")
		if choice not in ['1', '2', '3', '4', '5']:
			self.sudokumenu("Select the proper option")
		if choice == "1":
			self.importgame()
		elif choice == "2":
			self.mesage("Load Saved Game")
			self.loaded_game = True
			self.load_game_from_memory("")        
		elif choice == "3":
			self.generategame()
		elif choice == "4":
			self.changesettings()
		else:
			self.header("End Game  ")	
			os._exit(0)
							
#*******************************************************************+
#ariel
#*******************************************************************+
	def return_h_m_s(self):
		"""Convert time format hh:mm:ss. """
		dif_time = time.clock()-self.time
		if self.loaded_game == True:
			dif_time = dif_time + self.recovered_time
		if dif_time < 0:
			dif_time = dif_time * (-1)		
		if (dif_time//60) >= 1:
			second = dif_time-60 * (dif_time//60)
		else:
			second = dif_time
		if ((dif_time/60) // 60) >= 1:
			minute = dif_time/60 - 60 * ((dif_time/60) // 60)
		else:
			minute = dif_time/60
		hour = minute/60
		return dif_time, hour, minute, second

	def set_time(self):
		"""Update the time in the sudoku menu header. """
		dif_time, hour, minute, second = self.return_h_m_s()
		start_time = datetime(1900, 1, 1, int(hour), int(minute), int(second))
		start_time_format = start_time.strftime("%H:%M:%S")
		self.header("SUDOKU GAME  "+ start_time_format)
		
	def changecellvalue(self):
		"""Change one cell value. 
		Solicit a row, column and the new value 
		in order to interact with the user.
		"""
		if self.interactive.matrix.zero_count(
										self.interactive.matrix.first_matrix
										) != 0:
			row, colum, value = self.get_row_column_value()
			self.interactive.change_value_in_cell(row, colum, value)
			self.input_matrix.first_matrix = self.interactive.matrix
			if self.interactive.matrix.zero_count(
										self.interactive.matrix.first_matrix
										) == 0:
				msg = "Solved SUDOKU "
			else:
				dup = self.interactive.duplicate_values()
				if len(dup) != 0:
					msg = "Filled position: "+\
										 str(row)+\
										 ","+str(colum)+\
										 "\nDuplicate values in: \n"+dup
				else:
					msg = "Filled position: " + str(row) +"," + str(colum)
		else:
			msg = "Solved SUDOKU " 
		self.interactivegame(msg)
	
	def restartgame(self):
		"""Restart the current sudoku game. """
		interactive_matrix = deepcopy(self.interactive.copy)
		del(self.interactive)
		self.interactive = SudokuInteractive(interactive_matrix)
		self.time = self.interactive.game_start()
		self.interactivegame("Game restarted")
		
	def savegame(self, input_mesage):
		"""Save the current sudoku game. """
		dif_time, hour, minute, second = self.return_h_m_s()
		start_time = datetime(1900, 1, 1, int(hour), int(minute), int(second))
		start_time_format = start_time.strftime("%H:%M:%S")
		self.header("SUDOKU GAME  " + start_time_format)
		self.interactive.matrix.printmatrix()
		print(' ')
		input_menu = ' Game message: \n'+\
					  '        1) Save in available position\n'+\
					  '        2) Choose a memory position\n'+\
					  '        3) Return to previous menu\n'
		self.print_memory_positions()			  
		self.mesage(input_mesage)
		self.menu(input_menu)
		print(' Please select from the following options: ')
		choiceinteractive = raw_input(" ")
		if choiceinteractive not in ['1', '2', '3']:
			self.savegame("Select the proper option")
		if choiceinteractive == '1':
			self.save_game_in_available_position(dif_time)
		elif choiceinteractive == '2':
			self.save_in_memory(dif_time)
		elif choiceinteractive == '3':
			self.interactivegame("")
			
	def save_game_in_available_position(self, dif_time):
		"""Save the current sudoku game in available memory location. 
		The started time, position and name are required. 
		"""
		saved = False
		for i in range(1, 6):			  
			actual_tuple = self.interactive.memory[i]
			actual_time, actual_matrix, \
				actual_first_matrix, name = actual_tuple
			if actual_time == 0.0:
				self.interactive.save_game(dif_time, i, "saved game")
				self.savegame("Game saved in position " + str(i))
				saved = True
				break
		if saved == False:
			self.savegame("No available memory positions,"+ 
			"please choose the option 2")
					
	def print_memory_positions(self):
		"""Print the memory positions. """
		print "Memory position    Name               "
		print "**************************************"
		for i in range(1, 6):			  
			actual_tuple = self.interactive.memory[i]
			actual_time, actual_matrix, \
					actual_first_matrix, name = actual_tuple
			print " " + str(i) + "                " + name	
			
	def save_in_memory(self, dif_time):
		"""Save the current sudoku game in specific memory location. 
		The started time, position and name are required. 
		"""
		pos = int(raw_input("Select memory position: "))
		name = raw_input("Insert a game Name: ")
		self.interactive.save_game(dif_time, pos, name)
		self.savegame("Game saved in position " + str(pos))
	
	def load_game_from_memory(self, msg):
		"""Load the current sudoku game from memory location. """
		self.interactive = SudokuInteractive(self.blank_matrix)
		print "Memory position    Name               "
		print "**************************************"
		filled_positions = []
		for i in range(1, 6):			  
			actual_tuple = self.interactive.memory[i]
			actual_time, actual_matrix, first_matrix, name = actual_tuple
			if actual_time != 0.0:
				filled_positions.append(i)
			print " " + str(i) + "                " + name
		print "**************************************"
		print "Press 6 to return to Main menu"
		self.mesage(msg)
		pos = raw_input("Select memory position: ")
		if pos not in ['1', '2', '3', '4', '5', '6']:
			self.load_game_from_memory("Select the proper memory position")
		if int(pos) == 6:
			self.sudokumenu("")
		else:
			if int(pos) not in filled_positions:
				self.load_game_from_memory("This memory position is empty,"\
										   "please select again"
										  )
			else:
				self.start_recovered_game(int(pos))
		
	def start_recovered_game(self, pos):
		"""Start new instance of interactive with the recovered game. """
		actual_time, output_mat, \
					first_matrix, \
					name = self.interactive.load_game(int(pos))
		del(self.interactive)
		self.recovered_time = actual_time
		self.time = time.clock()
		self.interactive = SudokuInteractive(output_mat)
		self._reset_input_matrix()
		self.input_matrix = MatrixHandler(first_matrix)
		self.output_matrix = MatrixHandler(output_mat)
		self.interactive.copy = deepcopy(first_matrix)
		self.loaded_game = True
		self.interactivegame("")
		
	def mesage(self, mesage):
		"""Print a message. """
		print "**************************************"
		print mesage
		print "**************************************"

	def get_row_column_value(self):
		"""Get the row, column and the new value from the user. """
		row = int(raw_input("Enter the row: "))
		column = int(raw_input("Enter the column: "))
		value = int(raw_input("Enter the value: "))
		return (row, column, value)
	
	def header(self, text):
		"""Print the header message. """
		print('**************************************')
		print('              '+text+'               ')
		print('**************************************')
	
	def body(self, input_mesage):
		"""Print the body. """
		print(' ')
		input_menu = ' Game message: \n'+\
					  '        1) Solve Game\n'+\
					  '        2) Change cell value\n'+\
					  '        3) Hint\n'+\
					  '        4) Save Game\n'+\
					  '        5) Restart Game\n'+\
					  '        6) Return to main menu\n'
		self.mesage(input_mesage)
		self.menu(input_menu)
	
	def menu(self, input_menu):
		"""Print menu options. """
		print input_menu
		print '**************************************'
							
	def run(self):
		"""Starts the console user interface for the PAC Sudoku game."""
		print "\n\nStarting the console user interface ..."
		default_file_handler_xml = FileHandlerXML("config.xml","w")
		default_game_selected = SudokuConsoleUserInterface(
													default_file_handler_xml
													)
		choose = 0
		default_game_selected.sudokumenu("")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  