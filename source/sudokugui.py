import tkFileDialog
import tkMessageBox
from tkFont import Font
from Tkinter import Button
from Tkinter import Canvas
from Tkinter import Frame
from Tkinter import StringVar
from Tkinter import Label
from Tkinter import Menu
from Tkinter import Menubutton
from Tkinter import PhotoImage
from Tkinter import Radiobutton
from Tkinter import Toplevel

from main import Interface
from sudokuinteractive import SudokuInteractive


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
		if self.__class__.__name__ == "SudokuGUIUtilities":
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
	"""Class containing methos to build confg.outputType settings."""
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
		Toplevel.__init__(self, **kwargs)
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
		Frame.__init__(self, master)
		self.pack()
		self._createWidgets()
	
	def run(self):
		"""Starts the graphical User Interface for the PAC Sudoku game."""
		print "\n\nStarting the graphical user interface ..."
		self.master.title("PAC Sudoku")
		self.master.minsize(362, 462)
		self.mainloop()
		
	def start_interactive_mode(self):
		"""Initializes the interactive mode for solving sudokus.
		
		A new Sudokuinteractive instance is created since which will
		be handled all interactive actions.
		
		Additionally 2 new event bindings will be used:
		Left Mouse Button: For selecting a square in the sudoku field.
		Key Pressed: For populating the selected square.
		
		"""
		self.reset_interactive()
		self.interactive = SudokuInteractive(self.input_matrix.first_matrix)
		self.sudoku_canvas.bind("<Button-1>", self._init_update_square)
		self.bind_all("<Key>", self.play_action_set.update_square_action)

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

	def reset_interactive(self):
		"""Terminates interactive mode.
		
		Instance attribute interactive is set to None and events created by
		start_interactive_mode are disabled.
		
		Also violation and currently_editing instance attributes are reset.
		
		"""
		if self.interactive is not None:
			del(self.interactive)
			self.violation = False
			self.currently_editing = None
			self.interactive = None
			self.sudoku_canvas.unbind("<Button-1>")
			self.unbind_all("<Key>")
	
	def _createWidgets(self):
		"""Calls the gui_builder methods to build the PAC Sudoku GUI"""
		self.gui_builder.build_gui_frames()
		self.gui_builder.build_top_frame_content()
		self.gui_builder.build_main_frame_content()
		self.gui_builder.build_bottom_frame_content()

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
			command=self.gui.quit
		)
		self.gui.quit_button.pack(side="right")
		self.gui.solve_button = Button(
			self.gui.bottom_frame,
			text="Solve",
			width=24,
			command=self.gui.solve_action_set.solve_action
		)
		self.gui.solve_button.pack(side="right")


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
			text="0:00",
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
		if self.gui.export_sudoku_to_file(file):
			tkMessageBox.showinfo(
				"Export Solution",
				"SUccessfully exported solution to:\n %s" % file
			)
		else:
			tkMessageBox.showerror(
				"Error Exporting Solution",
				"Unable to export solution to:\n%s" % file
			)
	

class SudokuGUISettingsActionSet(SudokuGUIUtilities):
	"""Class containing action commands for changing config settings."""
	def edit_settings_action(self):
		"""Opens the Edit Settings dialog to edit each config setting."""
		settings_dialog = SudokuGUISettingsDialog(self.gui)
		settings_dialog.title("PAC Sudoku Settings")
		settings_dialog.geometry("250x200+30+30")
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
	def update_square_action(self, event):
		"""Fills in a digit typed using the keyboard to a selected square.
		
		This method also handles case if an invalid key is typed.
		
		If the key typed is "Escape", clear the square being edited.
		
		If the last key pressed, solved the sudoku, terminate interactive mode
		and throw a info message box to congratulate the user for solving the
		sudoku. 
		
		"""
		target = self.gui.currently_editing
		row = self.gui.current_square_y
		column = self.gui.current_square_x
		if event.keysym in '123456789':
			digit = int(event.keysym)
		elif event.keysym == 'Escape':
			self.gui.interactive.matrix.first_matrix[row][column] = 0
			self.gui.violation = False
			self.gui.sudoku_canvas.itemconfig(
				self.gui.currently_editing,
				image=self.gui.empty_square
			)
			self.gui.currently_editing = None
			return None
		else: return None
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
			tkMessageBox.showinfo(
				"Sudoku Solved",
				"Congratulations!\n\nYou have solved the Sudoku!"
			)
			self.gui.reset_interactive()
	
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
		"""Saves current status of sudoku and resets the canvas.
		
		NOT YET IMPLEMENTED!
		
		"""
		tkMessageBox.showwarning(
			"Not Implemented",
			"Save state not yet implemented!"
		)

