from Tkinter import *
from tkFont import Font
import tkMessageBox
import tkFileDialog

from main import Interface

class SudokuGraphicalUserInterface(Interface, Frame):
	"""GUI class for the PAC Sudoku game."""
	def __init__(self, config_file_handler, master=None):
		self.config_file = config_file_handler
		Interface.__init__(self, config_file_handler)
		Frame.__init__(self, master)
		self.pack()
		self._createWidgets()
	
	def run(self):
		"""Starts the graphical User Interface for the PAC Sudoku game."""
		print "\n\nStarting the graphical user interface ..."
		
		self.master.title(
			"PAC Sudoku - Difficulty: %s" % self.config.difficultyLevel
		)
		self.master.minsize(360, 400)
		self.mainloop()
		
	def _generate_action(self):
		if self.generate_sudoku():
			self._build_squares_from_input_matrix()
			self._start_interactive_mode()
		else:
			tkMessageBox.showerror(
				"Error Generating Sudoku",
				"Unsupported Algorithm!"
			)

	def _solve_action(self):
		if self.config.outputType == 'Console':
			self._print_solution_action()
		else:
			self._export_solution_action()
	
	def _load_action(self):
		extension = self.config.inputType
		file = tkFileDialog.askopenfilename(
			defaultextension='.' + extension,
			filetypes=[(extension + " Files", extension)],
			title="Load Sudoku File"
		)
		if self.load_sudoku_from_file(file):
			self._build_squares_from_input_matrix()
			self._start_interactive_mode()
		else:
			tkMessageBox.showerror(
				"Error Loading Sudoku From File",
				"Invalid Sudoku!"
			)

	def _save_settings_action(self):
		if self.save_config_to_file(self.config_file):
			tkMessageBox.showinfo(
				"Save Settings",
				"SUccessfully saved settings."
			)
		else:
			tkMessageBox.showerror(
				"Error Saving Settings",
				"Unable to save settings!"
			)

	def _export_solution_action(self):
		file = tkFileDialog.asksaveasfilename(
			defaultextension=".TXT",
			filetypes=[("TXT Files", "TXT")],
			title="Export Solution"
		)
		solved = self.solve_sudoku()

		if self.export_sudoku_to_file(file):
			tkMessageBox.showinfo(
				"Export Solution",
				"SUccessfully exported solution to:\n %s" % file
			)
		elif not solved:
			tkMessageBox.showinfo(
				"Sudoku not Loaded",
				"Please load or generate a Sudoku first."
			)
		else:
			tkMessageBox.showerror(
				"Error Exporting Solution",
				"Unable to export solution to %s!" % file
			)
	
	def _restart_action(self):
			tkMessageBox.showwarning(
				"Not Implemented",
				"Sudoku Interactive Class not yet implemented!"
			)

	def _save_state_action(self):
			tkMessageBox.showwarning(
				"Not Implemented",
				"Sudoku Interactive Class not yet implemented!"
			)


	def _get_hint_action(self):
			tkMessageBox.showwarning(
				"Not Implemented",
				"Sudoku Interactive Class not yet implemented!"
			)


	def _start_interactive_mode(self):
			tkMessageBox.showwarning(
				"Not Implemented",
				"Sudoku Interactive Class not yet implemented!"
			)

	
	def _edit_settings_action(self):
			tkMessageBox.showwarning(
				"Not Implemented",
				"Sudoku Settings Class not yet implemented!"
			)


	def _print_solution_action(self):
		if self.solve_sudoku():
			for i in range(9):
				for j in range(9):
					digit_input = self.input_matrix.first_matrix[i][j]
					digit_output = self.output_matrix.first_matrix[i][j]
					if digit_input:
						self.sudoku_canvas.create_image(
							40 * j + 22,
							40 * i + 22,
							image=self.list_fix_squares[digit_input]
						)
					else:
						self.sudoku_canvas.create_image(
							40 * j + 22,
							40 * i + 22,
							image=self.list_open_squares[digit_output]
						)
		else:
			tkMessageBox.showinfo(
				"Sudoku not Loaded",
				"Please load or generate a Sudoku first."
			)

	def _createWidgets(self):
		self._build_gui_frames()
		self._build_top_frame_content()
		self._build_main_frame_content()
		self._build_bottom_frame_content()

	def _build_gui_frames(self):
		self.top_frame = Frame(self, width=360, height=16)
		self.top_frame.pack(side="top")
		self.main_frame = Frame(self, width=360, height=392)
		self.main_frame.pack()
		self.icon_frame = Frame(self.main_frame, width=360, height=32)
		self.icon_frame.pack(side="top")
		self.sudoku_frame = Frame(self.main_frame, width=360, height=360)
		self.sudoku_frame.pack(side="bottom")
		self.bottom_frame = Frame(self, width=360, height=24)
		self.bottom_frame.pack(side="bottom")
	
	def _build_top_frame_content(self):
		self._build_file_menu()
		self._build_settings_menu()
		self._build_solve_menu()

	def _build_main_frame_content(self):
		self._build_icon_frame_content()
		self._build_sudoku_frame_content()

	def _build_icon_frame_content(self):
		self._build_load_icon()
		self._build_generate_icon()
		self._build_restart_icon()
		self._build_hint_icon()
		self.time_label = Label(
			self.icon_frame,
			text="0:00",
			font=Font(size=30)
		)
		self.time_label.pack(side="right")

	def _build_sudoku_frame_content(self):
		self.empty_square = PhotoImage(file="../resource/empty.gif")
		self._build_open_squares()
		self._build_fix_squares()
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
		
	def _build_bottom_frame_content(self):
		self.quit_button = Button(
			self.bottom_frame,
			text="Quit",
			width=24,
			command=self.quit
		)
		self.quit_button.pack(side="right")
		
		self.solve_button = Button(
			self.bottom_frame,
			text="Solve",
			width=24,
			command=self._solve_action
		)
		self.solve_button.pack(side="right")

	def _build_file_menu(self):
		self.play_menu_button = Menubutton(self.top_frame, text="Play")
		self.play_menu = Menu(self.play_menu_button)
		self.play_menu.add_command(
			label="Generate",
			underline=0,
			command=self._generate_action
		)
		self.play_menu.add_command(
			0,
			label="Load from file",
			underline=0,
			command=self._load_action
		)
		self.play_menu.add_command(
			label="Restart",
			underline=0,
			command=self._restart_action
		)
		self.play_menu.add_command(
			label="Save current state",
			underline=0,
			command=self._save_state_action
		)
		self.play_menu.add_command(
			label="Hint",
			underline=0,
			command=self._get_hint_action
		)
		self.play_menu_button["menu"] = self.play_menu
		self.play_menu_button.pack(side="left")
		
	def _build_generate_icon(self):
		self.icon_generate = PhotoImage(file="../resource/generate.gif")
		self.icon_generate_button = Button(
			self.icon_frame,
			image=self.icon_generate,
			width=32,
			height=32,
			command=self._generate_action
		)
		self.icon_generate_button.pack(side="left")

	def _build_restart_icon(self):
		self.icon_restart = PhotoImage(file="../resource/restart.gif")
		self.icon_restart_button = Button(
			self.icon_frame,
			image=self.icon_restart,
			width=32,
			height=32,
			command=self._restart_action
		)
		self.icon_restart_button.pack(side="left")

	def _build_fix_squares(self):
		self.list_fix_squares = [self.empty_square]
		for i in range(1, 10):
			self.list_fix_squares.append(
				PhotoImage(file="../resource/fix_" + str(i) + ".gif")
			)

	def _build_open_squares(self):
		self.list_open_squares = [self.empty_square]
		for i in range(1, 10):
			self.list_open_squares.append(
				PhotoImage(file="../resource/" + str(i) + ".gif")
			)

	def _build_squares_from_input_matrix(self):
			for i in range(9):
				for j in range(9):
					self.sudoku_canvas.create_image(
						40 * j + 22,
						40 * i + 22,
						image=self.list_fix_squares[
							self.input_matrix.first_matrix[i][j]
						]
					)

	def _build_load_icon(self):
		self.icon_load = PhotoImage(file="../resource/load.gif")
		self.icon_load_button = Button(
			self.icon_frame,
			image=self.icon_load,
			width=32,
			height=32,
			command=self._load_action
		)
		self.icon_load_button.pack(side="left")

	def _build_hint_icon(self):
		self.icon_hint = PhotoImage(file="../resource/hint.gif")
		self.icon_hint_button = Button(
			self.icon_frame,
			image=self.icon_hint,
			width=32,
			height=32,
			command=self._get_hint_action
		)
		self.icon_hint_button.pack(side="left")

	def _build_settings_menu(self):
		self.settings_menu_button = Menubutton(
			self.top_frame,
			text="Settings"
		)
		self.settings_menu = Menu(self.settings_menu_button)
		self.settings_menu.add_command(
			label="Edit settings",
			underline=0,
			command=self._edit_settings_action
		)
		self.settings_menu.add_command(
			label="Save settings",
			underline=0,
			command=self._save_settings_action
		)
		self.settings_menu_button["menu"] = self.settings_menu
		self.settings_menu_button.pack(side="left")
	
	def _build_solve_menu(self):
		self.solve_menu_button = Menubutton(
			self.top_frame,
			text="Solve"
		)
		self.solve_menu = Menu(self.solve_menu_button)
		self.solve_menu.add_command(
			label="Show Solution",
			underline=0,
			command=self._print_solution_action
		)
		self.solve_menu.add_command(
			label="Export Solution",
			underline=0,
			command=self._export_solution_action
		)
		self.solve_menu_button["menu"] = self.solve_menu
		self.solve_menu_button.pack(side="left")

