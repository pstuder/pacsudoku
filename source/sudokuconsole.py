from copy import deepcopy
import os, time
import sys
from datetime import datetime
from datetime import timedelta

from main import Interface
from validmatrix import MatrixHandler
from sudokuinteractive import SudokuInteractive


from inout import FileHandlerXML, FileHandlerTXT, FileHandlerCSV

class SudokuConsoleUserInterface(Interface):
	"""Console class for the PAC Sudoku game."""
	def __init__(self,config_file_handler):
		Interface.__init__(self, config_file_handler)
		self.config_file_handler = config_file_handler
		self.time=0
		
		
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
			self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
			self.time = self.interactive.game_start()
			self.interactivegame("")
		else:
			self.sudokumenu()
		

	def gamesolved(self):
		
		if self.solve_sudoku() == True:
			print('\n**************************************')
			print( "           SUDOKU GAME           ")
			print('**************************************')
			print(' ')
			self.interactive.solved.printmatrix()
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
			self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
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
		#self.header("SUDOKU GAME  ")
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
			self.gamesolved()
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
			print('*********************************************')
			os._exit(0)
							
		else:
			print (" Please Choose a valid number from the given choices" + "\n")
			print ('')
			print ('********************************************** ')
			time.sleep(1.5)

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
	
		default_game_selected.sudokumenu()

