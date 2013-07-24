import time
import tkFileDialog
import tkMessageBox
from datetime import datetime
from datetime import timedelta
from tkFont import Font
from Tkinter import Button
from Tkinter import Canvas
from Tkinter import Entry
from Tkinter import Frame
from Tkinter import IntVar
from Tkinter import Label
from Tkinter import Menu
from Tkinter import Menubutton
from Tkinter import PhotoImage
from Tkinter import Radiobutton
from Tkinter import StringVar
from Tkinter import Toplevel

from main import Interface
from sudokuinteractive import SudokuInteractive
from validmatrix import MatrixHandler


class SudokuGUIMemoryUtilities():
	"""Abstrac Class for the Sudoku GUI Memory utilites"""
	def __init__(self, sudoku_memory_gui, sudoku_gui):
		"""Initializes the Sudoku GUI Memory utility.
		
		Raises NotImplementedError if attempting to initialize
		since abstrac class.
		
		Creates the following instance attribute:
		gui -- A reference to the Sudoku GUI.
		memory_gui -- A reference to the Sudoku Memory GUI.
		
		"""
		if self.__class__.__name__ == "SudokuGUIMemoryUtilities":
			raise NotImplementedError("Can't instance from abstract class!")
		self.gui = sudoku_gui
		self.memory_gui = sudoku_memory_gui


class GUIMemoryMainFrameBuilder(SudokuGUIMemoryUtilities):
	"""Class containing methos to build memory main frame."""
	def __init__(self, sudoku_memory_gui, sudoku_gui):
		"""Initializes a new sudoku gui memory main frame builder.
		
		It first creates the instance attributes of SudokuGUIMemoryUtilities.
		Additionally it creates instance attributes for sudoku_memory_gui.
		
		"""
		SudokuGUIMemoryUtilities.__init__(
			self,
			sudoku_memory_gui,
			sudoku_gui
		)
		self.memory_gui.memory_radio_buttons = []
		self.memory_gui.memory_int_var = IntVar()
		self.memory_gui.memory_int_var.set(1)
		
	def build_main_frame(self):
		"""Builds the main frame for the list of memory entries."""
		self.memory_gui.main_frame = Frame(
			self.memory_gui
		)
		self.memory_gui.main_frame.pack(side="top")
			
	def build_list(self):
		"""Builds dinamically the list of memory entries."""
		for item in self.gui.interactive.memory.keys():
			memory_tuple = self.gui.interactive.memory[item]
			memory_text = "(" + str(item) + ") Name: " + memory_tuple[3] +\
							"; Time: " + str(memory_tuple[0])
			self.memory_gui.memory_radio_buttons.append(
				Radiobutton(
					self.memory_gui.main_frame,
					text=memory_text,
					value=item,
					variable=self.memory_gui.memory_int_var
				)
			)
		for radio_button in self.memory_gui.memory_radio_buttons:
			radio_button.pack()


class GUIMemoryBottomFrameBuilder(SudokuGUIMemoryUtilities):
	"""Class containing methos to build memory bottom frame."""
	def build_bottom_frame(self):
		"""Builds the frame for the buttons of the memory UI."""
		self.memory_gui.bottom_frame = Frame(
			self.memory_gui
		)
		self.memory_gui.bottom_frame.pack(side="bottom")
	
	def build_bottom_frame_buttons(self, mode):
		"""Builds the buttons for the bottom frame of the memory UI."""
		if mode:
			self.memory_gui.load_button = Button(
				self.memory_gui.bottom_frame,
				text="Load",
				width=12,
				command=self.memory_gui.load_entry
			)
			self.memory_gui.load_button.pack(side="left")
		else:
			self.gui.sudoku_canvas.unbind_all("<Key>")
			self.memory_gui.memory_name_string_var = StringVar()
			self.memory_gui.name_label = Label(
				self.memory_gui.bottom_frame,
				text="Name"
			)
			self.memory_gui.name_label.pack(side="left")
			self.memory_gui.name_entry = Entry(
				self.memory_gui.bottom_frame,
				textvariable=self.memory_gui.memory_name_string_var,
				width=12
			)
			self.memory_gui.name_entry.pack(side="left")
			self.memory_gui.save_button = Button(
				self.memory_gui.bottom_frame,
				text="Save",
				width=12,
				command=self.memory_gui.save_entry
			)
			self.memory_gui.save_button.pack(side="left")
		self.memory_gui.cancel_button = Button(
			self.memory_gui.bottom_frame,
			text="Cancel",
			width=12,
			command=self.memory_gui.cancel_memory
		)
		self.memory_gui.cancel_button.pack(side="left")


class SudokuGUIMemoryBuilder(SudokuGUIMemoryUtilities):
	"""Class containing methos to build the PAC Sudoku Memory GUI."""
	def __init__(self, sudoku_memory_gui, sudoku_gui, mode):
		"""Initializes a new sudoku gui memory builder.
		
		It first creates instance attributes of SudokuGUIMemoryUtilities.
		Additionally it creates the following instance attributes:
		main_frame_builder -- Set of methods for building the main frame
		mode -- Mode to build: For loading or saving
		
		"""
		SudokuGUIMemoryUtilities.__init__(
			self,
			sudoku_memory_gui,
			sudoku_gui
		)
		self.mode = mode
		self.main_frame_builder = GUIMemoryMainFrameBuilder(
			sudoku_memory_gui, sudoku_gui
		)
		self.bottom_frame_builder = GUIMemoryBottomFrameBuilder(
			sudoku_memory_gui, sudoku_gui
		)

	def build_frames(self):
		"""Builds all the frames for the Sudoku GUI Memory dialog."""
		self.main_frame_builder.build_main_frame()
		self.main_frame_builder.build_list()
		self.bottom_frame_builder.build_bottom_frame()
		self.bottom_frame_builder.build_bottom_frame_buttons(self.mode)


class SudokuGUIMemoryDialog(Toplevel):
	"""GUI class for the PAC Sudoku Memory Dialog."""
	def __init__(self, sudoku_gui, mode, **kwargs):
		"""Builds and initializes the GUI as a top level UI.
		
		First, the TopLevel instance attributes are created, additionally
		the following instance attributes are created:
		memory_builder -- Set of methods for building the PAC Sudoku GUI
		gui -- Instance of the main Sudoku Game GUI.
		
		"""
		Toplevel.__init__(self, sudoku_gui, **kwargs)
		self.memory_builder = SudokuGUIMemoryBuilder(self, sudoku_gui, mode)
		self.gui = sudoku_gui
		self.mode = mode
		self._createWidgets()
	
	def load_entry(self):
		"""Loads currently selected memory slot and exits memory UI."""
		memory_slot = self.memory_int_var.get()
		if self.gui.continue_interactive_mode(memory_slot):
			self.grab_release()
			self.destroy()
		else:
			tkMessageBox.showinfo(
				"No status saved",
				"There is no sudoku game saved in this position."
			)
		
	def save_entry(self):
		"""Save to currently selected memory slot and exits memory UI."""
		memory_slot = self.memory_int_var.get()
		memory_name = self.memory_name_string_var.get()
		if memory_name == "":
			tkMessageBox.showinfo(
				"Type a name",
				"Pelase type a name before saving."
			)
			return None
		self.gui.interactive.save_game(
			self.gui.last_game_start,
			memory_slot,
			memory_name
		)
		tkMessageBox.showinfo(
			"Status saved",
			"Status of current play successfully saved\n" +
			"at position {0} as '{1}'".format(memory_slot, memory_name)
			
		)
		self.grab_release()
		self.destroy()
		self.gui.reset_interactive()
		self.gui.reset_display()

	def cancel_memory(self):
		if self.mode == 0:
			self.gui.sudoku_canvas.bind_all(
				"<Key>",
				self.gui.play_action_set.update_square_action
			)
		self.destroy()
		
	def _createWidgets(self):
		"""Calls the gui_builder methods to build the memory GUI"""
		self.memory_builder.build_frames()


class SudokuGUISettingsUtilities():
	"""Abstrac Class for the Sudoku GUI Settings utilites"""
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes the Sudoku GUI settings utility.
		
		Raises NotImplementedError if attempting to initialize
		since abstrac class.
		
		Creates the following instance attribute:
		gui -- A reference to the Sudoku GUI.
		settings_gui --
		
		"""
		if self.__class__.__name__ == "SudokuGUISettingsUtilities":
			raise NotImplementedError("Can't instance from abstract class!")
		self.gui = sudoku_gui
		self.settings_gui = sudoku_settings_gui


class SudokuGUISettingsBuilder(SudokuGUISettingsUtilities):
	"""Class containing methos to build the PAC Sudoku GUI."""
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes a new sudoku gui settings builder.
		
		It first creates instance attributes of SudokuGUISettingsUtilities.
		Additionally it creates the following instance attributes:
		input_type_builder -- Set of methods for building input type
		output_type_builder -- Set of methods for building output type
		default_algorithm_builder -- Set of methods for building algorithm
		difficulty_level_builder -- Set of methods for building difficulty
		bottom_frame_builder -- Set of methods for building the bottom frame
		
		"""
		SudokuGUISettingsUtilities.__init__(
			self,
			sudoku_settings_gui,
			sudoku_gui
		)
		self.input_type_builder = GUISettingsInputTypeBuilder(
			sudoku_settings_gui, sudoku_gui
		)
		self.output_type_builder = GUISettingsOutputTypeBuilder(
			sudoku_settings_gui, sudoku_gui
		)
		self.default_algorithm_builder = GUISettingsDefaultAlgorithmBuilder(
			sudoku_settings_gui, sudoku_gui
		)
		self.difficulty_level_builder = GUISettingsDifficultyLevelBuilder(
			sudoku_settings_gui, sudoku_gui
		)
		self.bottom_frame_builder = GUISettingsBottomFrameBuilder(
			sudoku_settings_gui, sudoku_gui
		)
	
	def build_main_frame(self):
		"""Builds all the frames for the Sudoku GUI Settings dialog."""
		self.input_type_builder.build_input_type_frame()
		self.input_type_builder.build_input_type_radio_buttons()
		self.output_type_builder.build_output_type_frame()
		self.output_type_builder.build_output_type_radio_buttons()
		self.default_algorithm_builder.build_default_algorithm_frame()
		self.default_algorithm_builder.build_default_algorithm_radio_buttons()
		self.difficulty_level_builder.build_difficulty_level_frame()
		self.difficulty_level_builder.build_difficulty_level_radio_buttons()
		self.bottom_frame_builder.build_bottom_frame()
		self.bottom_frame_builder.build_bottom_frame_buttons()

class GUISettingsInputTypeBuilder(SudokuGUISettingsUtilities):
	"""Class containing methos to build confg.inputType settings."""
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes a new sudoku gui settings input type builder.
		
		It first creates the instance attributes of SudokuGUISettingsUtilities.
		Additionally it creates instance attributes for settings_gui.
		
		"""
		SudokuGUISettingsUtilities.__init__(
			self,
			sudoku_settings_gui,
			sudoku_gui
		)
		self.settings_gui.input_type_radio_buttons = []
		self.settings_gui.input_type_string_var = StringVar()
		self.settings_gui.input_type_string_var.set(self.gui.config.inputType)
		
	def build_input_type_frame(self):
		"""Builds the frame for the input type settings."""
		self.settings_gui.input_type_frame = Frame(
			self.settings_gui,
			width=300,
			height=32
		)
		self.settings_gui.input_type_frame.pack(side="top")
		self.settings_gui.input_type_label = Label(
			self.settings_gui.input_type_frame,
			text="Input Type:",
		)
		self.settings_gui.input_type_label.pack(side="top")
		self.settings_gui.input_type_buttons_frame = Frame(
			self.settings_gui.input_type_frame,
			width=300,
			height=16
		)
		self.settings_gui.input_type_buttons_frame.pack(side="bottom")
	
	def build_input_type_radio_buttons(self):
		"""Builds dinamically the supported input types radio buttons."""
		for item in self.gui.config.supported_inputTypes:
			self.settings_gui.input_type_radio_buttons.append(
				Radiobutton(
					self.settings_gui.input_type_buttons_frame,
					text=item,
					value=item,
					variable=self.settings_gui.input_type_string_var,
					command=self.settings_gui.update_input_type_config
				)
			)
		for radio_button in self.settings_gui.input_type_radio_buttons:
			radio_button.pack(side="left")


class GUISettingsOutputTypeBuilder(SudokuGUISettingsUtilities):
	"""Class containing methods to build confg.outputType settings."""
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes a new sudoku gui settings output type builder.
		
		It first creates the instance attributes of SudokuGUISettingsUtilities.
		Additionally it creates instance attributes for settings_gui.
		
		"""
		SudokuGUISettingsUtilities.__init__(
			self,
			sudoku_settings_gui,
			sudoku_gui
		)
		self.settings_gui.output_type_radio_buttons = []
		self.settings_gui.output_type_string_var = StringVar()
		self.settings_gui.output_type_string_var.set(
			self.gui.config.outputType
		)
		
	def build_output_type_frame(self):	
		"""Builds the frame for the output type settings."""
		self.settings_gui.output_type_frame = Frame(
			self.settings_gui,
			width=300,
			height=32
		)
		self.settings_gui.output_type_frame.pack(side="top")
		self.settings_gui.output_type_label = Label(
			self.settings_gui.output_type_frame,
			text="Output Type:",
		)
		self.settings_gui.output_type_label.pack(side="top")
		self.settings_gui.output_type_buttons_frame = Frame(
			self.settings_gui.output_type_frame,
			width=300,
			height=16
		)
		self.settings_gui.output_type_buttons_frame.pack(side="bottom")
	
	def build_output_type_radio_buttons(self):
		"""Builds dinamically the supported output types radio buttons."""
		for item in self.gui.config.supported_outputTypes:
			self.settings_gui.output_type_radio_buttons.append(
				Radiobutton(
					self.settings_gui.output_type_buttons_frame,
					text=item,
					value=item,
					variable=self.settings_gui.output_type_string_var,
					command=self.settings_gui.update_output_type_config
				)
			)
		for radio_button in self.settings_gui.output_type_radio_buttons:
			radio_button.pack(side="left")


class GUISettingsDefaultAlgorithmBuilder(SudokuGUISettingsUtilities):
	"""Class containing methos to build confg.defaultAlgorithm settings."""
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes a new sudoku gui settings default algorithm builder.
		
		It first creates the instance attributes of SudokuGUISettingsUtilities.
		Additionally it creates instance attributes for settings_gui.
		
		"""
		SudokuGUISettingsUtilities.__init__(
			self,
			sudoku_settings_gui,
			sudoku_gui
		)
		self.settings_gui.default_algorithm_radio_buttons = []
		self.settings_gui.default_algorithm_string_var = StringVar()
		self.settings_gui.default_algorithm_string_var.set(
			self.gui.config.defaultAlgorithm
		)
		
	def build_default_algorithm_frame(self):	
		"""Builds the frame for the default algorithm settings."""
		self.settings_gui.default_algorithm_frame = Frame(
			self.settings_gui,
			width=300,
			height=32
		)
		self.settings_gui.default_algorithm_frame.pack(side="top")
		self.settings_gui.default_algorithm_label = Label(
			self.settings_gui.default_algorithm_frame,
			text="Default Algorithm:",
		)
		self.settings_gui.default_algorithm_label.pack(side="top")
		self.settings_gui.default_algorithm_buttons_frame = Frame(
			self.settings_gui.default_algorithm_frame,
			width=300,
			height=16
		)
		self.settings_gui.default_algorithm_buttons_frame.pack(side="bottom")
	
	def build_default_algorithm_radio_buttons(self):
		"""Builds dinamically the supported algorithms radio buttons."""
		for item in self.gui.config.supported_defaultAlgorithms:
			self.settings_gui.default_algorithm_radio_buttons.append(
				Radiobutton(
					self.settings_gui.default_algorithm_buttons_frame,
					text=item,
					value=item,
					variable=self.settings_gui.default_algorithm_string_var,
					command=self.settings_gui.update_default_algorithm_config
				)
			)
		for radio_button in self.settings_gui.default_algorithm_radio_buttons:
			radio_button.pack(side="left")


class GUISettingsDifficultyLevelBuilder(SudokuGUISettingsUtilities):
	def __init__(self, sudoku_settings_gui, sudoku_gui):
		"""Initializes a new sudoku gui settings difficulty level builder.
		
		It first creates the instance attributes of SudokuGUISettingsUtilities.
		Additionally it creates instance attributes for settings_gui.
		
		"""
		SudokuGUISettingsUtilities.__init__(
			self,
			sudoku_settings_gui,
			sudoku_gui
		)
		self.settings_gui.difficulty_level_radio_buttons = []
		self.settings_gui.difficulty_level_string_var = StringVar()
		self.settings_gui.difficulty_level_string_var.set(
			self.gui.config.difficultyLevel
		)
		
	def build_difficulty_level_frame(self):	
		"""Builds the frame for the difficulty level settings."""
		self.settings_gui.difficulty_level_frame = Frame(
			self.settings_gui,
			width=300,
			height=32
		)
		self.settings_gui.difficulty_level_frame.pack(side="top")
		self.settings_gui.difficulty_level_label = Label(
			self.settings_gui.difficulty_level_frame,
			text="Difficulty Level:",
		)
		self.settings_gui.difficulty_level_label.pack(side="top")
		self.settings_gui.difficulty_level_buttons_frame = Frame(
			self.settings_gui.difficulty_level_frame,
			width=300,
			height=16
		)
		self.settings_gui.difficulty_level_buttons_frame.pack(side="bottom")
	
	def build_difficulty_level_radio_buttons(self):
		"""Builds dinamically the supported difficulty level radio buttons."""
		for item in self.gui.config.supported_difficultyLevels:
			self.settings_gui.difficulty_level_radio_buttons.append(
				Radiobutton(
					self.settings_gui.difficulty_level_buttons_frame,
					text=item,
					value=item,
					variable=self.settings_gui.difficulty_level_string_var,
					command=self.settings_gui.update_difficulty_level_config
				)
			)
		for radio_button in self.settings_gui.difficulty_level_radio_buttons:
			radio_button.pack(side="left")


class GUISettingsBottomFrameBuilder(SudokuGUISettingsUtilities):
	"""Class containing methos to build settings bottom frame."""
	def build_bottom_frame(self):
		"""Builds the frame for the buttons of the settings UI."""
		self.settings_gui.bottom_frame = Frame(
			self.settings_gui,
			width=300,
			height=24
		)
		self.settings_gui.bottom_frame.pack(side="bottom")
	
	def build_bottom_frame_buttons(self):
		"""Builds the buttons for the bottom frame of the settings UI."""
		self.settings_gui.save_button = Button(
			self.settings_gui.bottom_frame,
			text="Save",
			width=12,
			command=self.settings_gui.save_and_exit
		)
		self.settings_gui.save_button.pack(side="left")
		self.settings_gui.close_button = Button(
			self.settings_gui.bottom_frame,
			text="Close",
			width=12,
			command=self.settings_gui.destroy
		)
		self.settings_gui.close_button.pack(side="left")
		

class SudokuGUISettingsDialog(Toplevel):
	"""GUI class for the PAC Sudoku Settings."""
	def __init__(self, sudoku_gui, **kwargs):
		"""Builds and initializes the GUI as a top level UI.
		
		First, the TopLevel instance attributes are created, additionally
		the following instance attributes are created:
		settings_builder -- Set of methods for building the PAC Sudoku GUI
		gui -- Instance of the main Sudoku Game GUI.
		
		"""
		Toplevel.__init__(self, sudoku_gui, **kwargs)
		self.settings_builder = SudokuGUISettingsBuilder(self, sudoku_gui)
		self.gui = sudoku_gui
		self._createWidgets()
		
	def save_and_exit(self):
		"""Save settings to currently loaded .xml config file and exits."""
		self.grab_release()
		self.destroy()
		self.gui.settings_action_set.save_settings_action()

	def update_input_type_config(self):
		"""Updates config input type with value set since radio buttons."""
		self.gui.update_config_input_type(
			self.input_type_string_var.get()
		)

	def update_output_type_config(self):
		"""Updates config output type with value set since radio buttons."""
		self.gui.update_config_output_type(
			self.output_type_string_var.get()
		)

	def update_default_algorithm_config(self):
		"""Updates config algorithm with value set since radio buttons."""
		self.gui.update_config_default_algorithm(
			self.default_algorithm_string_var.get()
		)

	def update_difficulty_level_config(self):
		"""Updates config difficulty with value set since radio buttons."""
		self.gui.update_config_difficulty_level(
			self.difficulty_level_string_var.get()
		)

	def _createWidgets(self):
		"""Calls the gui_builder methods to build the Settings GUI"""
		self.settings_builder.build_main_frame()


class SudokuGUIUtilities():
	"""Abstrac Class for the Sudoku GUI utilites"""
	def __init__(self, sudoku_gui):
		"""Initializes the Sudoku GUI utility.
		
		Raises NotImplementedError if attempting to initialize
		since abstrac class.
		
		Creates the following instance attribute:
		gui -- A reference to the Sudoku GUI.
		
		"""
		if self.__class__.__name__ == "SudokuGUIUtilities":
			raise NotImplementedError("Can't instance from abstract class!")
		self.gui = sudoku_gui


class SudokuGUISolveActionSet(SudokuGUIUtilities):
	"""Class containing action commands for solving the sudoku."""
	def solve_action(self):
		"""Solves currently loaded sudoku according to gui.config.outputType.
		
		If outputType is Console, terminate interactive mode and print/draw
		solution to canvas.
		
		Otherwise export solution to file, but continue interactive mode.
		
		"""
		if self.gui.config.outputType == 'Console':
			self.print_solution_action()
		else:
			self.export_solution_action()
	
	def print_solution_action(self):
		"""Prints/draws gui.output_matrix to sudoku canvas.
		
		If gui.input_matrix has not been loaded, throw Info message box
		and alert user no sudoku has been loaded.
		
		"""
		if self.gui.solve_sudoku():
			for i in range(9):
				for j in range(9):
					digit_input = self.gui.input_matrix.first_matrix[i][j]
					digit_output = self.gui.output_matrix.first_matrix[i][j]
					if digit_input:
						self.gui.sudoku_canvas.create_image(
							40 * j + 22,
							40 * i + 22,
							image=self.gui.list_fix_squares[digit_input]
						)
					else:
						self.gui.sudoku_canvas.create_image(
							40 * j + 22,
							40 * i + 22,
							image=self.gui.list_open_squares[digit_output]
						)
			self.gui.reset_interactive()
		else:
			tkMessageBox.showinfo(
				"Sudoku not Loaded",
				"Please load or generate a Sudoku first."
			)

	def export_solution_action(self):
		"""Exports gui.output_matrix to a TXT file.
		
		Throws file browser dialog to allow user to export solution to file.
		
		If gui.input_matrix has not been loaded, throw Info message box
		and alert user no sudoku has been loaded.
		
		"""
		if not self.gui.solve_sudoku():
			tkMessageBox.showinfo(
				"Sudoku not Loaded",
				"Please load or generate a Sudoku first."
			)
			return None
		file = tkFileDialog.asksaveasfilename(
			defaultextension=".TXT",
			filetypes=[("TXT Files", "TXT")],
			title="Export Solution"
		)
		if file == "":
			return None
		elif self.gui.export_sudoku_to_file(file):
			tkMessageBox.showinfo(
				"Export Solution",
				"SUccessfully exported solution to:\n %s" % file
			)
		else:
			tkMessageBox.showerror(
				"Error Exporting Solution",
				"Unable to export solution to:\n%s" % file +
				"\nEither the path does not exist or " +
				"you do not have enough privileges."
			)


class SudokuGUISettingsActionSet(SudokuGUIUtilities):
	"""Class containing action commands for changing config settings."""
	def edit_settings_action(self):
		"""Opens the Edit Settings dialog to edit each config setting."""
		screen_x = self.gui.winfo_pointerx() - 100
		screen_y = self.gui.winfo_pointery() - 20
		screen_geometry = "250x200+{0}+{1}".format(screen_x, screen_y)
		settings_dialog = SudokuGUISettingsDialog(self.gui)
		settings_dialog.title("PAC Sudoku Settings")
		settings_dialog.geometry(screen_geometry)
		settings_dialog.transient(self.gui)
		settings_dialog.grab_set()

	def save_settings_action(self):
		"""Saves gui.config settings to loaded .xml config file."""
		if self.gui.save_config_to_file(self.gui.config_file):
			tkMessageBox.showinfo(
				"Save Settings",
				"SUccessfully saved settings."
			)
		else:
			tkMessageBox.showerror(
				"Error Saving Settings",
				"Unable to save settings!"
			)


class SudokuGUIPlayActionSet(SudokuGUIUtilities):
	"""Class containing action commands for the sudoku interactive mode."""
	LOAD = 1
	SAVE = 0
	
	def update_square_action(self, event):
		"""Fills in a digit typed using the keyboard to a selected square.
		
		This method also handles case if an invalid key is typed.
		
		If the key typed is "Escape", clear the square being edited.
		
		If the last key pressed, solved the sudoku, terminate interactive mode
		and throw a info message box to congratulate the user for solving the
		sudoku. 
		
		"""
		if event.keysym not in '123456789' and event.keysym != 'Escape':
			return None
		target = self.gui.currently_editing
		row = self.gui.current_square_y
		column = self.gui.current_square_x
		if event.keysym in '123456789':
			digit = int(event.keysym)
		else:
			self.gui.interactive.matrix.first_matrix[row][column] = 0
			self.gui.violation = False
			self.gui.sudoku_canvas.itemconfig(
				self.gui.currently_editing,
				image=self.gui.empty_square
			)
			self.gui.currently_editing = None
			return None
		if self.gui.currently_editing is not None:
			self.gui.interactive.change_value_in_cell(row, column, digit)
		else:
			tkMessageBox.showinfo(
				"Select Square",
				"Pelase select a square first."
			)
			return None
		duplicates = self.gui.interactive.duplicate_values()
		self.gui.violation = duplicates != ""
		if self.gui.violation:
			tkMessageBox.showwarning(
				"Violation",
				"Duplicate values found in:\n%s" % duplicates
			)
			target_list_squares = self.gui.list_error_squares
		else:
			target_list_squares = self.gui.list_open_squares
			self.gui.currently_editing = None
		self.gui.sudoku_canvas.itemconfig(
			target,
			image=target_list_squares[digit]
		)
		if self.gui.interactive.sudoku_is_solved():
			time = self.gui.interactive.game_time(self.gui.last_game_start)
			self.gui.reset_interactive()
			tkMessageBox.showinfo(
				"Sudoku Solved",
				"Congratulations!\n\nYou have solved the Sudoku!\n" +
				"Time: %s seconds." % int(time)
			)
	
	def generate_action(self):
		"""Randomly generate a new sudoku and start interactive mode.
		
		Some times gui.input_matrix.generator finishes loading an invalid
		sudoku. If this happens throw error message box and ask user to try
		again.
		
		"""
		if not self.gui.generate_sudoku():
			tkMessageBox.showerror(
				"Error Generating Sudoku",
				"Unsupported Algorithm!"
			)
			return None
		if not self.gui.solve_sudoku():
			tkMessageBox.showerror(
				"Generator Error",
				"Generator took too long, please try again or load from file."
			)
			return None
		self.gui.build_squares_from_input_matrix()
		self.gui.start_interactive_mode()

	def load_action(self):
		"""Import sudoku form file, suing gui.config.inputType as file format.
		
		Throw file dialog to allow user to import a new sudoku from file.
		
		If the sudoku imported is invalid, throw error message box stating
		that the file contains an invalid sudoku.
		
		"""
		extension = self.gui.config.inputType
		file = tkFileDialog.askopenfilename(
			defaultextension='.' + extension,
			filetypes=[(extension + " Files", extension)],
			title="Load Sudoku File"
		)
		if file == "":
			return None
		if self.gui.load_sudoku_from_file(file):
			self.gui.build_squares_from_input_matrix()
			self.gui.start_interactive_mode()
		else:
			tkMessageBox.showerror(
				"Error Loading Sudoku From File",
				"Invalid Sudoku!"
			)

	def restart_action(self):
		"""Terminates current interactive mode and restarts the same game."""
		if self.gui.input_matrix is not None:
			self.gui.build_squares_from_input_matrix()
			self.gui.start_interactive_mode()

	def get_hint_action(self):
		"""Automatically solves one number in the sudoku canvas.
		
		This method updates gui.interactive.matrix with one solved number.
		
		If not in interactive mode, throw info message box asking to load
		a sudoku first.
		
		If only one field remains to be filled in, don't solve, ask the user
		to fill it instead.
		
		"""
		if self.gui.violation:
			tkMessageBox.showinfo(
				"Violation Detected",
				"Please fix violation first."
			)
			return None
		if self.gui.interactive is None:
			tkMessageBox.showinfo(
				"Load Sudoku",
				"Please load/generate a new Sudoku."
			)
			return None
		row, column = self.gui.interactive.solve_one()
		if not self.gui.interactive.sudoku_is_solved():
			self.gui.sudoku_canvas.itemconfig(
				self.gui.square_item_matrix[row][column],
				image=self.gui.list_hint_squares[
					self.gui.interactive.matrix.first_matrix[row][column]
				]
			)
		else:
			self.gui.interactive.matrix.first_matrix[row][column] = 0
			tkMessageBox.showinfo(
				"No more hints",
				"There is only one field left. You can fill it yourself!"
			)

	def save_state_action(self):
		"""Saves current status of sudoku and resets the canvas."""
		if self.gui.interactive is not None:
			screen_x = self.gui.winfo_pointerx() - 100
			screen_y = self.gui.winfo_pointery() - 20
			screen_geometry = "396x144+{0}+{1}".format(screen_x, screen_y)
			memory_dialog = SudokuGUIMemoryDialog(self.gui, self.SAVE)
			memory_dialog.title("Save Game")
			memory_dialog.geometry(screen_geometry)
			memory_dialog.transient(self.gui)
			memory_dialog.grab_set()
		else:
			tkMessageBox.showinfo(
				"No sudoku loaded",
				"Please start a new game before saving current state."
			)

	def load_state_action(self):
		"""Terminate current interactive mode and load a saved game."""
		screen_x = self.gui.winfo_pointerx() - 100
		screen_y = self.gui.winfo_pointery() - 20
		screen_geometry = "256x128+{0}+{1}".format(screen_x, screen_y)
		if self.gui.interactive is None:
			self.gui.interactive = SudokuInteractive([])
		self.gui.interactive.recover_values_from_file()
		memory_dialog = SudokuGUIMemoryDialog(self.gui, self.LOAD)
		memory_dialog.title("Select Saved Game")
		memory_dialog.geometry(screen_geometry)
		memory_dialog.transient(self.gui)
		memory_dialog.grab_set()

class SudokuGUIBuilder(SudokuGUIUtilities):
	"""Class containing methos to build the PAC Sudoku GUI."""
	def __init__(self, sudoku_gui):
		"""Initializes a new sudoku gui builder.
		
		It first creates the instance attributes of SudokuGUIUtilities.
		Additionally it creates the following instance attributes:
		menu_builder -- Set of methods for building the menu
		main_frame_builder -- Set of methods for building the main frame
		
		"""
		SudokuGUIUtilities.__init__(self, sudoku_gui)
		self.menu_builder = SudokuGUIMenuBuilder(sudoku_gui)
		self.main_frame_builder = SudokuGUIMainFrameBuilder(sudoku_gui)
	
	def build_gui_frames(self):
		"""Creates all the frames needed for grouping the widgets."""
		self.gui.top_frame = Frame(
			self.gui,
			width=360,
			height=16
		)
		self.gui.top_frame.pack(side="top")
		self.gui.main_frame = Frame(
			self.gui,
			width=360,
			height=392
		)
		self.gui.main_frame.pack()
		self.gui.icon_frame = Frame(
			self.gui.main_frame,
			width=360,
			height=32
		)
		self.gui.icon_frame.pack(side="top")
		self.gui.sudoku_frame = Frame(
			self.gui.main_frame,
			width=360,
			height=360
		)
		self.gui.sudoku_frame.pack(side="bottom")
		self.gui.bottom_frame = Frame(
			self.gui,
			width=360,
			height=24
		)
		self.gui.bottom_frame.pack(side="bottom")
	
	def build_top_frame_content(self):
		"""Builds the menu bar in the top frame."""
		self.menu_builder.build_play_menu()
		self.menu_builder.build_settings_menu()
		self.menu_builder.build_solve_menu()

	def build_main_frame_content(self):
		"""Builds the icons and the sudoku canvas in the main frame."""
		self.main_frame_builder.build_icon_frame_content()
		self.main_frame_builder.build_sudoku_frame_content()

	def build_bottom_frame_content(self):
		"""Builds the Solve and Quit button in the bottom frame."""
		self.gui.quit_button = Button(
			self.gui.bottom_frame,
			text="Quit",
			width=24,
			command=self.gui._quit_handler
		)
		self.gui.quit_button.pack(side="right")
		self.gui.solve_button = Button(
			self.gui.bottom_frame,
			text="Solve",
			width=24,
			command=self.gui.solve_action_set.solve_action
		)
		self.gui.solve_button.pack(side="right")


class SudokuGUIMenuBuilder(SudokuGUIUtilities):
	"""Class containing methos to build the main menu action commands."""
	def build_play_menu(self):
		"""Build the action commands for the Play menu."""
		self.gui.play_menu_button = Menubutton(self.gui.top_frame, text="Play")
		self.gui.play_menu = Menu(self.gui.play_menu_button)
		self.gui.play_menu.add_command(
			label="Generate",
			underline=0,
			command=self.gui.play_action_set.generate_action
		)
		self.gui.play_menu.add_command(
			0,
			label="Load from file",
			underline=0,
			command=self.gui.play_action_set.load_action
		)
		self.gui.play_menu.add_command(
			label="Restart",
			underline=0,
			command=self.gui.play_action_set.restart_action
		)
		self.gui.play_menu.add_command(
			label="Save current state",
			underline=0,
			command=self.gui.play_action_set.save_state_action
		)
		self.gui.play_menu.add_command(
			label="Load saved state",
			underline=0,
			command=self.gui.play_action_set.load_state_action
		)
		self.gui.play_menu.add_command(
			label="Hint",
			underline=0,
			command=self.gui.play_action_set.get_hint_action
		)
		self.gui.play_menu_button["menu"] = self.gui.play_menu
		self.gui.play_menu_button.pack(side="left")
		
	def build_settings_menu(self):
		"""Build the action commands for the Settings menu."""
		self.gui.settings_menu_button = Menubutton(
			self.gui.top_frame,
			text="Settings"
		)
		self.gui.settings_menu = Menu(self.gui.settings_menu_button)
		self.gui.settings_menu.add_command(
			label="Edit settings",
			underline=0,
			command=self.gui.settings_action_set.edit_settings_action
		)
		self.gui.settings_menu.add_command(
			label="Save settings",
			underline=0,
			command=self.gui.settings_action_set.save_settings_action
		)
		self.gui.settings_menu_button["menu"] = self.gui.settings_menu
		self.gui.settings_menu_button.pack(side="left")
	
	def build_solve_menu(self):
		"""Build the action commands for the Solve menu."""
		self.gui.solve_menu_button = Menubutton(
			self.gui.top_frame,
			text="Solve"
		)
		self.gui.solve_menu = Menu(self.gui.solve_menu_button)
		self.gui.solve_menu.add_command(
			label="Show Solution",
			underline=0,
			command=self.gui.solve_action_set.print_solution_action
		)
		self.gui.solve_menu.add_command(
			label="Export Solution",
			underline=0,
			command=self.gui.solve_action_set.export_solution_action
		)
		self.gui.solve_menu_button["menu"] = self.gui.solve_menu
		self.gui.solve_menu_button.pack(side="left")


class SudokuGUIMainFrameBuilder(SudokuGUIUtilities):
	"""Class containing methos to build the PAC Sudoku Main Frame content."""
	def __init__(self, sudoku_gui):
		"""Initializes a new sudoku gui main frame builder.
		
		It first creates the instance attributes of SudokuGUIUtilities.
		Additionally it creates the following instance attributes:
		icon_frame_builder -- Set of methods for building the icon bar
		sudoku_squares_builder -- Set of methods for building square images
		
		"""
		SudokuGUIUtilities.__init__(self, sudoku_gui)
		self.icon_frame_builder = SudokuGUIIconFrameBuilder(sudoku_gui)
		self.sudoku_squares_builder = SudokuGUISquaresBuilder(sudoku_gui)
	
	def build_icon_frame_content(self):
		"""Builds the icons and the icon bar in the icon frame."""
		self.icon_frame_builder.build_load_icon()
		self.icon_frame_builder.build_generate_icon()
		self.icon_frame_builder.build_restart_icon()
		self.icon_frame_builder.build_hint_icon()
		self.gui.time_label = Label(
			self.gui.icon_frame,
			text=self.gui.timer.strftime("%H:%M:%S"),
			font=Font(size=30)
		)
		self.gui.time_label.pack(side="right")

	def build_sudoku_frame_content(self):
		"""Builds the sudoku canvas and all images needed for a square."""
		self.gui.empty_square = PhotoImage(file="../resource/empty.gif")
		self.gui.edit_empty = PhotoImage(file="../resource/edit_empty.gif")
		self.sudoku_squares_builder.build_open_squares()
		self.sudoku_squares_builder.build_fix_squares()
		self.sudoku_squares_builder.build_error_squares()
		self.sudoku_squares_builder.build_hint_squares()
		self.sudoku_squares_builder.build_edit_squares()
		self.gui.sudoku_canvas = Canvas(
			self.gui.sudoku_frame,
			width=360,
			height=360,
			bg="white"
		)
		self.gui.sudoku_canvas.pack(side="top")
		self.gui.sudoku_canvas.create_line(122, 0, 122, 362, width=2)
		self.gui.sudoku_canvas.create_line(242, 0, 242, 362, width=2)
		self.gui.sudoku_canvas.create_line(0, 122, 362, 122, width=2)
		self.gui.sudoku_canvas.create_line(0, 242, 362, 242, width=2)


class SudokuGUIIconFrameBuilder(SudokuGUIUtilities):
	"""Class containing methos to build the icons for the PAC Sudoku."""
	def build_load_icon(self):
		"""Build the icon for the Load action in the icon bar."""
		self.gui.icon_load = PhotoImage(file="../resource/load.gif")
		self.gui.icon_load_button = Button(
			self.gui.icon_frame,
			image=self.gui.icon_load,
			width=32,
			height=32,
			command=self.gui.play_action_set.load_action
		)
		self.gui.icon_load_button.pack(side="left")

	def build_generate_icon(self):
		"""Build the icon for the Generate action in the icon bar."""
		self.gui.icon_generate = PhotoImage(file="../resource/generate.gif")
		self.gui.icon_generate_button = Button(
			self.gui.icon_frame,
			image=self.gui.icon_generate,
			width=32,
			height=32,
			command=self.gui.play_action_set.generate_action
		)
		self.gui.icon_generate_button.pack(side="left")

	def build_restart_icon(self):
		"""Build the icon for the Restart action in the icon bar."""
		self.gui.icon_restart = PhotoImage(file="../resource/restart.gif")
		self.gui.icon_restart_button = Button(
			self.gui.icon_frame,
			image=self.gui.icon_restart,
			width=32,
			height=32,
			command=self.gui.play_action_set.restart_action
		)
		self.gui.icon_restart_button.pack(side="left")

	def build_hint_icon(self):
		"""Build the icon for the Hint action in the icon bar."""
		self.gui.icon_hint = PhotoImage(file="../resource/hint.gif")
		self.gui.icon_hint_button = Button(
			self.gui.icon_frame,
			image=self.gui.icon_hint,
			width=32,
			height=32,
			command=self.gui.play_action_set.get_hint_action
		)
		self.gui.icon_hint_button.pack(side="left")


class SudokuGUISquaresBuilder(SudokuGUIUtilities):
	"""Class containing methos to build the sudoku canvas square images."""
	def build_open_squares(self):
		"""Build square images for all squares that are editable."""
		self.gui.list_open_squares = [self.gui.empty_square]
		for i in range(1, 10):
			self.gui.list_open_squares.append(
				PhotoImage(file="../resource/" + str(i) + ".gif")
			)
	
	def build_fix_squares(self):
		"""Build square images for all squares that are fixed."""
		self.gui.list_fix_squares = [self.gui.empty_square]
		for i in range(1, 10):
			self.gui.list_fix_squares.append(
				PhotoImage(file="../resource/fix_" + str(i) + ".gif")
			)

	def build_error_squares(self):
		"""Build square images for all squares that contain a violation."""
		self.gui.list_error_squares = [self.gui.empty_square]
		for i in range(1, 10):
			self.gui.list_error_squares.append(
				PhotoImage(file="../resource/error_" + str(i) + ".gif")
			)

	def build_hint_squares(self):
		"""Build square images for all squares that were filled with hints."""
		self.gui.list_hint_squares = [self.gui.empty_square]
		for i in range(1, 10):
			self.gui.list_hint_squares.append(
				PhotoImage(file="../resource/hint_" + str(i) + ".gif")
			)

	def build_edit_squares(self):
		"""Build square images for all squares that are selected for edit."""
		self.gui.list_edit_squares = [self.gui.edit_empty]
		for i in range(1, 10):
			self.gui.list_edit_squares.append(
				PhotoImage(file="../resource/edit_" + str(i) + ".gif")
			)


class SudokuGraphicalUserInterface(Interface, Frame):
	"""GUI class for the PAC Sudoku game."""
	def __init__(self, config_file_handler, master=None):
		"""Builds and initializes the GUI as a Interface type if instance.
		
		First, the Interface instance attributes are created, additionally
		the following instance attributes are created:
		solve_action_set -- Set of methods for the solve menu actions
		settings_action_set -- Set of methods for the settings menu actions
		play_action_set -- Set of methods for the play menu actions
		gui_builder -- Set of methods for building the PAC Sudoku GUI
		config_file -- XMLFileHandler object with the config file loaded
		interactive -- Sudokuinteractive initialized as None
		violation -- Violation flag set to False
		currently_editing -- Canvas image ID of a square initialized as None
		timer -- Sudoku timer
		_timer_increment -- Used to increment by 1 second the timer
		
		"""
		Interface.__init__(self, config_file_handler)
		self.solve_action_set = SudokuGUISolveActionSet(self)
		self.settings_action_set = SudokuGUISettingsActionSet(self)
		self.play_action_set = SudokuGUIPlayActionSet(self)
		self.gui_builder = SudokuGUIBuilder(self)
		self.config_file = config_file_handler
		self.interactive = None
		self.violation = False
		self.currently_editing = None
		self.timer = datetime(1900,1,1)
		self._timer_increment = timedelta(seconds=1)
		Frame.__init__(self, master)
		self.pack()
		self._createWidgets()
	
	def run(self):
		"""Starts the graphical User Interface for the PAC Sudoku game."""
		print "\n\nStarting the graphical user interface ..."
		self.master.title("PAC Sudoku")
		self.master.minsize(362, 462)
		self.master.protocol("WM_DELETE_WINDOW", self._quit_handler)
		self.mainloop()
		
	def start_interactive_mode(self):
		"""Initializes the interactive mode for solving sudokus.
		
		A new Sudokuinteractive instance is created since which will
		be handled all interactive actions.
		
		Additionally 2 new event bindings will be used:
		Left Mouse Button: For selecting a square in the sudoku field.
		Key Pressed: For populating the selected square.
		
		And one new instance attribute is created:
		last_game_start -- Records the start time of the new game.
		
		"""
		self.reset_interactive()
		self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
		self.sudoku_canvas.bind("<Button-1>", self._init_update_square)
		self.sudoku_canvas.bind_all(
			"<Key>",
			self.play_action_set.update_square_action
		)
		self.last_game_start = self.interactive.game_start()
		self._init_update_time()

	def continue_interactive_mode(self, memory_pos):
		"""Initializes the interactive mode for saved sudokus.
		
		Any Sudokuinteractive instance need to be reset, afterwards
		memory.pos will be read from interactive.memory to get time
		and input matrix. Interactive.matrix will also be restored
		according to memory data.
		
		"""
		previous_time, interactive_matrix, input_matrix, name =\
										self.interactive.load_game(memory_pos)
		if not interactive_matrix:
			return False
		self._reset_input_matrix()
		self.input_matrix = MatrixHandler(input_matrix)
		self.reset_interactive()
		self.interactive = SudokuInteractive(input_matrix)
		del(self.interactive.matrix)
		self.interactive.matrix = MatrixHandler(interactive_matrix)
		self.build_squares_from_interactive_matrix()
		self.sudoku_canvas.bind("<Button-1>", self._init_update_square)
		self.sudoku_canvas.bind_all(
			"<Key>",
			self.play_action_set.update_square_action
		)
		self.last_game_start = time.clock() - previous_time
		self.timer += timedelta(seconds=int(previous_time))
		self._init_update_time()
		return True

	def build_squares_from_input_matrix(self):
		"""Draws a new sudoku from input_matrix and starts interactive mode.
		
		Once a sudoku has been loaded or generated, draw the sudoku canvas
		with fix squares for the numbers fix numbers in input_matrix using
		small GIF images built by gui_builder. The zeroes are left blank.
		
		This method also creates a new instance attribute:
		square_item_matrix -- 9x9 matrix containing all canvas image item IDs
		
		"""
		self.square_item_matrix = []
		for i in range(9):
			current_square_item_list = []
			for j in range(9):
				current_square_item_list.append(
					self.sudoku_canvas.create_image(
						40 * j + 22,
						40 * i + 22,
						image=self.list_fix_squares[
							self.input_matrix.first_matrix[i][j]
						]
					)
				)
			self.square_item_matrix.append(current_square_item_list)

	def build_squares_from_interactive_matrix(self):
		"""Draws a saved sudoku and starts interactive mode.
		
		Once a sudoku has been loaded or generated, draw the sudoku canvas
		with fix squares for the numbers fix numbers in input_matrix and 
		draw open numbers for the numbers in saved sudoku using
		interactive.matrix.
		
		This method also creates a new instance attribute:
		square_item_matrix -- 9x9 matrix containing all canvas image item IDs
		
		"""
		self.square_item_matrix = []
		for i in range(9):
			current_square_item_list = []
			for j in range(9):
				input_value = self.input_matrix.first_matrix[i][j]
				interactive_value = self.interactive.matrix.first_matrix[i][j]
				if input_value:
					target_square = self.list_fix_squares[input_value]
				else:
					target_square = self.list_open_squares[interactive_value]
				current_square_item_list.append(
					self.sudoku_canvas.create_image(
						40 * j + 22,
						40 * i + 22,
						image=target_square
					)
				)
			self.square_item_matrix.append(current_square_item_list)

	def reset_interactive(self):
		"""Terminates interactive mode.
		
		Instance attribute interactive is set to None and events created by
		start_interactive_mode are disabled.
		
		Also violation and currently_editing instance attributes are reset.
		
		"""
		if self.interactive is not None:
			self._reset_time()
			del(self.interactive)
			self.violation = False
			self.currently_editing = None
			self.interactive = None
			self.sudoku_canvas.unbind("<Button-1>")
			self.sudoku_canvas.unbind_all("<Key>")
	
	def reset_display(self):
		self._reset_input_matrix()
		self.sudoku_canvas.destroy()
		self.sudoku_canvas = Canvas(
			self.sudoku_frame,
			width=360,
			height=360,
			bg="white"
		)
		self.sudoku_canvas.pack(side="top")
		self.sudoku_canvas.create_line(122, 0, 122, 362, width=2)
		self.sudoku_canvas.create_line(242, 0, 242, 362, width=2)
		self.sudoku_canvas.create_line(0, 122, 362, 122, width=2)
		self.sudoku_canvas.create_line(0, 242, 362, 242, width=2)
		self.timer = datetime(1900,1,1)
		self.time_label.configure(text=self.timer.strftime("%H:%M:%S"))

	def _createWidgets(self):
		"""Calls the gui_builder methods to build the PAC Sudoku GUI"""
		self.gui_builder.build_gui_frames()
		self.gui_builder.build_top_frame_content()
		self.gui_builder.build_main_frame_content()
		self.gui_builder.build_bottom_frame_content()

	def _reset_time(self):
		"""Resets the sudoku timer."""
		try:
			self.after_cancel(self._job)
			del(self._job)
		except:
			pass
		del(self.timer)
		self.timer = datetime(1900,1,1)
	
	def _init_update_square(self, event):
		"""Starts the process to update a clicked square in the sudoku canvas.
		
		This method is launched with the Left Mouse Button event in
		interactive mode.
		
		The clicked square will be updated with a edit_* image corresponding:
		edit_empty -- If the user did not add a number to it.
		edit_number -- If the user previously add a number to it.
		
		If a previous square was highlighted for edit, turn it back to:
		blank -- If the user did not add any number to it
		number -- If the user add a number to it
		
		If a violation is found, or the game is not in interactive mode, or
		the user is trying to update a fix square, this method won't do
		anything.
		
		"""
		if self.violation:
			return None
		if self.interactive is None:
			return None
		self._set_clicked_square_position_in_canvas()
		row = self.current_square_y
		column = self.current_square_x
		if self.input_matrix.first_matrix[row][column] != 0:
			return None
		to_edit = self.square_item_matrix[row][column]
		current_digit = self.interactive.matrix.first_matrix[row][column]
		if self.currently_editing is not None:
			self.sudoku_canvas.itemconfig(
				self.currently_editing,
				image=self.list_open_squares[self.last_digit]
			)
		self.currently_editing = to_edit
		self.last_digit = current_digit
		self.sudoku_canvas.itemconfig(
			to_edit,
			image=self.list_edit_squares[current_digit]
		)

	def _init_update_time(self):
		"""Starts the process to update timer each second."""
		self.time_label.configure(text=self.timer.strftime("%H:%M:%S"))
		self.timer += self._timer_increment
		self._job = self.after(1000, self._init_update_time)
	
	def _set_clicked_square_position_in_canvas(self):
		"""Set square coordinates in the canvas after clicking on one.
		
		Two new instance attributes are created:
		current_square_x -- column in the sudoku canvas of clicked square
		current_square_y -- row in the sudoku canvas of clicked square
		
		"""
		pionterx = self.sudoku_canvas.winfo_pointerx()
		piontery = self.sudoku_canvas.winfo_pointery()
		rootx = self.sudoku_canvas.winfo_rootx()
		rooty = self.sudoku_canvas.winfo_rooty()
		self.current_square_x = (pionterx - rootx)//40
		self.current_square_y = (piontery - rooty)//40
	
	def _quit_handler(self):
		"""Handler for verifying if changes to config should be saved."""
		selection = False
		if self.config_changes_not_saved(self.config_file):
			selection = tkMessageBox.askyesno(
				"Changes to Config settings not saved",
				"Changes to config settings have not been saved.\n" +
				"Would you like to save settings before closing?"
			)
		if selection:
			self.settings_action_set.save_settings_action()
		self.quit()


