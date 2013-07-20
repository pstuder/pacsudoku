from copy import deepcopy
import os, time
import sys
from datetime import datetime
from datetime import timedelta

from main import Interface
from validmatrix import MatrixHandler
from sudokuinteractive import SudokuInteractive


class SudokuConsoleUserInterface(Interface):
	"""Console class for the PAC Sudoku game."""
	def __init__(self,config_file_handler):
		Interface.__init__(self, config_file_handler)
		self.config_file_handler = config_file_handler
		
		
	def blankmatrix(self):
		blankmatrix = [[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0],
					[0,0,0,0,0,0,0,0,0]]
		return MatrixHandler(blankmatrix)
	
	
	def importgame(self):
		print('\n**************************************')
		print( "           IMPORT GAME           ")
		print('**************************************')
		print(' ')
		print'Default file format ', self.config.supported_inputTypes[0]
		path_txt_file = raw_input("Insert Path: " )
		print(' ')
		while self.load_sudoku_from_file(path_txt_file) == False and self.load_sudoku_from_file(path_txt_file)== True:
			path_txt_file = path_txt_file = raw_input("Insert Path: " )
		self.solvegame()
	
	def solvegame(self):
		print('\n**************************************')
		print( "           SUDOKU GAME           ")
		print('**************************************')
		print(' ')
		self.input_matrix.printmatrix()
		print(' ')
		print('               MENU                    ')
		print(' ')
		print('        1) Solve Game')
		print('        2) Play Interactive Game')
		print('        3) Return to main menu')
		print(' ')
		print(' Please select from the following options: ')
		choicesolve = raw_input(" ")
		if choicesolve == '1':
			self.gamesolved()
		elif choicesolve == '2':
			self.interactivegame()
		else:
			self.sudokumenu()
		

	def gamesolved(self):
		
		if self.solve_sudoku() == True:
			print('\n**************************************')
			print( "           SUDOKU GAME           ")
			print('**************************************')
			print(' ')
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
				self.savegame()
			else:
				self.sudokumenu()
		else:
			print(' ')
			print("Sudoku unsolvable, generate another.")
			print(' ')
			self.sudokumenu()
	
	def generategame(self):
		if self.generate_sudoku() == True:
			self.solvegame()
		else:
			print("Sudoku unsolvable, generate another.")
			self.sudokumenu()
	
	def changesettings(self):
		print('\n**************************************')
		print('            CHANGE SETTINGS             ')
		print('**************************************')
		print('')
		print('')
		print('Input File Type')
		if self.config.inputType == 'TXT':
			print '1) -',self.config.inputType
			print('2) CSV')
		else:
			print('1) TXT')
			print '2) -',self.config.inputType
		print('')
		new_input_type = raw_input('Type new Input Type: ')
		
		print('')
		print('Output Type') 
		if self.config.outputType == 'Console':
			print'1) -',self.config.outputType
			print('2) File')
		else:
			print('1) Console')
			print'2) -',self.config.outputType
		print('')
		new_output_type = raw_input('Type new Output Type: ')
		
		print('')
		print('Algorithm')
		if self.config.defaultAlgorithm == 'Backtracking':
			print '1) -',self.config.defaultAlgorithm
			print('2) Norvig')
			print('3) XAlgorithm')
		elif self.config.defaultAlgorithm == 'Norvig':
			print('1) Backtracking')
			print '2) -',self.config.defaultAlgorithm
			print('3) XAlgorithm')
		else:
			print('1) Backtracking')
			print('2) Norvig')
			print '3) -',self.config.defaultAlgorithm
		
		print('')		
		new_default_algorithm = raw_input('Type new Algorithm Type: ')
		
		print('')
		print('Difficult Level')
		
		if self.config.difficultyLevel == 'Low':
			print '1) -',self.config.difficultyLevel
			print('2) Medium')
			print('3) High')
		elif  self.config.difficultyLevel == 'Medium':
			print('1) Low')
			print '2) -',self.config.difficultyLevel
			print('3) High')
		else:
			print('1) Low')
			print('2) Medium')
			print'3) -',self.config.difficultyLevel
		print('')		
		new_difficulty_level = raw_input('Type new Level Type: ')
		
		print(' ')
		print('        1) Save')
		print('        2) Return to main menu')
		print(' ')
		print(' Please select from the following options: ')
		choicesettings = raw_input(" ")
		
		if choicesettings == '1':
			self.savesettings(new_input_type, new_output_type, new_default_algorithm, new_difficulty_level)
		else:
			yes_no = raw_input('You will lost any change in settings. Continue?(yes/no): ')
			if yes_no == 'yes':
				self.sudokumenu()
			else:
				print(' New settings will be saved ')
				self.savesettings(new_input_type, new_output_type, new_default_algorithm, new_difficulty_level)
				
	
	def savesettings(self, new_input_type, new_output_type, new_default_algorithm, new_difficulty_level):
		if self.update_config_input_type(new_input_type) == True or\
			self.update_config_output_type(new_output_type) == True or\
			self.update_config_default_algorithm(new_default_algorithm) == True or\
			self.update_config_difficulty_level(new_difficulty_level) == True:
				if self.save_config_to_file(self.config_file_handler) == True:
					print('Settings were saved correctly ')
		else:
			print('Settings were not saved correctly, please try again ')
		self.sudokumenu()
	
	def interactivegame(self):
		self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
		time = self.interactive.game_start()
		start_time = datetime(1900,1,1,0,0,int(time))
		start_time_format = start_time.strftime("%H:%M:%S")
		print('\n**************************************')
		print '           SUDOKU GAME      ', start_time_format
		print('**************************************')
		print(' ')
		self.input_matrix.printmatrix()
		print(' ')
		print(' Game message: ')
		print(' ')
		print('        1) Solve Game')
		print('        2) Change cell value')
		print('        3) Hint')
		print('        4) Save Game')
		print('        5) Restart Game')
		print('        6) Return to main menu')
		print(' ')
		print(' Please select from the following options: ')
		choiceinteractive = raw_input(" ")
		if choiceinteractive == '1':
			self.gamesolved()
		elif choiceinteractive == '2':
			self.changecellvalue()
		elif choiceinteractive == '3':
			print"Hint....."
		elif choiceinteractive == '4':
			self.savegame()
		elif choiceinteractive == '5':
			self.restartgame()
		else:
			self.sudokumenu()
		
		
	def sudokumenu(self):
		self.bmatrix = self.blankmatrix()
				
		print('\n**************************************')
		print('              PACSUDOKU                  ')
		print('**************************************')
		print('')
		self.bmatrix.printmatrix()
		print('')
		print('               MENU                    ')
		print('          1) Import Game')
		print('	  2) Load Saved Game')
		print('	  3) Generate Game')
		print('	  4) Change Settings')
		print('	  5) Exit')
		print('')
		print(' Please select from the following options: ')
		choice = raw_input(" ")
		print ('')
		if choice == "1":
			self.importgame()
			time.sleep(10)
		elif choice == "2":
			print('\n********************************************')
			print('                Load Saved Game                ')
			print('**********************************************')    
			time.sleep(1.5)
		elif choice == "3":
			self.generategame()
			time.sleep(20)
		elif choice == "4":
			self.changesettings()
			time.sleep(20)
		elif choice == "5":
				
			print('\n********************************************')
			print('             End Game			              ')
			print('**********************************************')
			os._exit(0)
							
		else:
			print (" Please Choose a valid number from the given choices" + "\n")
			print ('')
			print ('********************************************** ')
			time.sleep(1.5)
	
	
	def run(self):
		"""Starts the console user interface for the PAC Sudoku game."""
		print "\n\nStarting the console user interface ..."
