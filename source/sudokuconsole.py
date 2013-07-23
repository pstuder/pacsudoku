from copy import deepcopy
import os, time
from os import path
import sys
from datetime import datetime
from datetime import timedelta

from main import Interface
from validmatrix import MatrixHandler
from sudokuinteractive import SudokuInteractive


from inout import FileHandlerXML, FileHandlerTXT, FileHandlerCSV

class SudokuConsoleUserInterface(Interface):
	"""Console class for the PAC Sudoku game.
		
		Creates main manu to play Sudoku and user will able to
		import a game form txt or csv files, generate a game, change settings,
		save and load a game, solve Sudoku interactive etc.
		
	"""
	def __init__(self,config_file_handler):
		Interface.__init__(self, config_file_handler)
		self.config_file_handler = config_file_handler
		self.time=0
		
		
	def blankmatrix(self):
		""" Creates an empty matrix to print in console initializing game."""
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
		if self.generate_sudoku() == True:
			self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
			self.time = self.interactive.game_start()
			self.interactivegame("")
		else:
			self.sudokumenu("Sudoku unsolvable, generate another.")
	
	def configfilesettings(self):
		"""Display config values set by default an allow to change them."""
		self.header(" CHANGE SETTINGS  ")
		print('')
		print('1) Input File Type')
		if self.config.inputType == 'TXT':
			print '(x)',self.config.inputType
			print('( ) CSV')
		else:
			print('() TXT')
			print '(x)',self.config.inputType
		print('')
		
		print('2) Output Type') 
		if self.config.outputType == 'Console':
			print'(x)',self.config.outputType
			print('( ) File')
		else:
			print('( ) Console')
			print'(x)',self.config.outputType
		
		print('')
		print('3) Algorithm')
		if self.config.defaultAlgorithm == 'Backtracking':
			print '(x)',self.config.defaultAlgorithm
			print('( ) Norvig')
			print('( ) XAlgorithm')
		elif self.config.defaultAlgorithm == 'Norvig':
			print('( ) Backtracking')
			print '(x)',self.config.defaultAlgorithm
			print('( ) XAlgorithm')
		else:
			print('( ) Backtracking')
			print('( ) Norvig')
			print '(x)',self.config.defaultAlgorithm
		
		print('')
		print('4) Difficult Level')
		if self.config.difficultyLevel == 'Low':
			print '(x)',self.config.difficultyLevel
			print('( ) Medium')
			print('( ) High')
		elif  self.config.difficultyLevel == 'Medium':
			print('( ) Low')
			print '(x)',self.config.difficultyLevel
			print('( ) High')
		else:
			print('( ) Low')
			print('( ) Medium')
			print'(x)',self.config.difficultyLevel
		print(' ')
		print('        1)Change Settings')
		print('        2) Return to main menu')
		print(' ')
		print(' Please select from the following options: ')
		choiceconfigfile = raw_input(" ")
		
		if choiceconfigfile == '1':
			
			self.changesettings(self.inputtype(), self.outputtype(), self.algorithmsolve(), self.difficultlevel())
		else:
			self.sudokumenu("")
		
		
	def changesettings(self, inputtype, outputtype, algorithmsolve, difficultlevel):
		"""Change default values with custom values."""
		input_menu='        1) Save\n'+\
				'        2) Return to main menu\n'
		self.menu(input_menu)
		print(' Please select from the following options ')
		choicesettings = raw_input(" ")
		if choicesettings == '1':
			if inputtype != '':
				self.config.inputType = inputtype
			if outputtype !='':
				self.config.outputType = outputtype
			if algorithmsolve != '':
				self.config.defaultAlgorithm = algorithmsolve
			if difficultlevel != '':
				self.config.difficultyLevel = difficultlevel
			if self.save_config_to_file(self.config_file_handler) == True:
					print('Settings were saved correctly ')
		else:
			print('Settings were not saved correctly, please try again ')
			print(' ')
		self.sudokumenu("")
		
						
	def inputtype(self):
		"""Read new in put type value to change later in config file."""
		print('')
		print('1) Input File Type')
		print('')
		return raw_input('Type new Input Type: ')
		
	
	def outputtype(self):
		"""Read new out put type value to change later in config file."""
		print('')
		print('2) Output Type') 
		print('')
		return raw_input('Type new Output Type: ')
	
	def algorithmsolve(self):
		"""Read new algorithm name to change later in config file."""
		print('')
		print('3) Algorithm')
		return raw_input('Type new Algorithm Type: ')
	
	def difficultlevel(self):
		"""Read new difficult level to change later in config file."""
		print('')
		print('4) Difficult Level')
		print('')		
		return raw_input('Type new Level Type: ')
	
	def interactivegame(self,input_mesage):
		dif_time=time.clock()-self.time
		if (dif_time//60)>=1:
			s=dif_time-60*(dif_time//60)
		else:
			s=dif_time
		if (dif_time//60//60)>=1:
			s=dif_time/60-60*(dif_time//60//60)
		else:
			m=dif_time/60
		h=m/60
		start_time = datetime(1900,1,1,int(h),int(m),int(s))
		start_time_format = start_time.strftime("%H:%M:%S")
		self.header("SUDOKU GAME  "+ start_time_format)
		
		self.interactive.matrix.printmatrix()
		print(' ')
		input_menu=' Game message: \n'+\
					  '        1) Solve Game\n'+\
					  '        2) Change cell value\n'+\
					  '        3) Hint\n'+\
					  '        4) Save Game\n'+\
					  '        5) Restart Game\n'+\
					  '        6) Return to main menu\n'
		self.mesage(input_mesage)
		self.menu(input_menu)
		print(' Please select from the following options: ')
		choiceinteractive = raw_input(" ")
		if choiceinteractive not in ['1','2','3','4','5','6']:
			self.interactivegame("Select the proper option")
		if choiceinteractive == '1':
			self.gameoutput()
		elif choiceinteractive == '2':
			
			self.changecellvalue()
		elif choiceinteractive == '3':
			if self.interactive.matrix.zero_count(self.interactive.matrix.first_matrix)!=0:
				x,y=self.interactive.solve_one() 
				msg="Solved position: "+ str(x)+","+str(y)
			else:
				msg="Solved SUDOKU "
			self.interactivegame(msg)
		elif choiceinteractive == '4':
			self.savegame()
		elif choiceinteractive == '5':
			self.restartgame()
		else:
			self.sudokumenu("")
	
			 
			
		
	def sudokumenu(self,input_message):
		"""Print main menu for PacSudoku game"""
		self.bmatrix = self.blankmatrix()
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
		if choice not in ['1','2','3','4','5']:
			self.sudokumenu("Select the proper option")
			
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
			self.configfilesettings()
			time.sleep(20)
		else:
			self.header("End Game  ")	
			os._exit(0)
							
		

#*******************************************************************+
#ariel
#*******************************************************************+
	def changecellvalue(self):
		#self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
		if self.interactive.matrix.zero_count(self.interactive.matrix.first_matrix)!=0:
			row,colum,value=self.get_row_column_value()
			self.interactive.change_value_in_cell(row,colum,value)
			
			self.input_matrix.first_matrix=self.interactive.matrix
			if self.interactive.matrix.zero_count(self.interactive.matrix.first_matrix)==0:
				msg="Solved SUDOKU "
			else:
				dup=self.interactive.duplicate_values()
				if len(dup)!=0:
					msg="Filled position: "+ str(row)+","+str(colum)+"\nDuplicate values in: \n"+dup
				else:
					msg="Filled position: "+ str(row)+","+str(colum)
		else:
			msg="Solved SUDOKU " 
		self.interactivegame(msg)
		
	
	def restartgame(self):
		interactive_matrix=deepcopy(self.interactive.copy)
		del(self.interactive)
		self.interactive = SudokuInteractive(interactive_matrix)
		self.time = self.interactive.game_start()
		self.interactivegame("Game restarted")
		
		
		
		#self.input_matrix.printmatrix()
	def mesage(self,mesage):
		print "**************************************"
		print mesage
		print "**************************************"

	def get_row_column_value(self):
		row = int(raw_input("Enter the row: "))
		column = int(raw_input("Enter the column: "))
		value = int(raw_input("Enter the value: "))
		return (row,column,value)
	
	def header(self,text):
		print('**************************************')
		print('              '+text+'               ')
		print('**************************************')
	
	def body(self,matrix):
		matrix.printmatrix()
		
	def menu(self,input_menu):
		print input_menu
		print '**************************************'
				
	
		
		
	def run(self):
		"""Starts the console user interface for the PAC Sudoku game."""
		print "\n\nStarting the console user interface ..."

		default_file_handler_xml = FileHandlerXML("config.xml","w")
		default_game_selected = SudokuConsoleUserInterface(default_file_handler_xml)
		choose=0
	
		default_game_selected.sudokumenu("")

