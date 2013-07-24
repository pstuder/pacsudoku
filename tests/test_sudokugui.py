import unittest
from datetime import datetime
from datetime import timedelta
from os import remove
from Tkinter import Frame
from Tkinter import IntVar
from Tkinter import StringVar

import sudokugui
from config import Configfile
from inout import FileHandlerXML
from main import Interface
from validmatrix import MatrixHandler


class DummyInteractive():
	def __init__(self):
		self.memory = {1:(1,"120","100","test1"), 2:(2,"006","406","test2")}


class DummyCanvas(Frame):
	def __init__(self):
		Frame.__init__(self, None)


class DummyMemoryUI(Frame):
	def __init__(self):
		Frame.__init__(self, None)


class DummySettingsUI(Frame):
	def __init__(self):
		Frame.__init__(self, None)


class DummySudokuUI(Frame):
	def __init__(self):
		Frame.__init__(self, None)
		self.config = Configfile()
		self.interactive = DummyInteractive()
		self.sudoku_canvas = DummyCanvas()


class TestSudokuGUIMemory(unittest.TestCase):
	def setUp(self):
		self.dummy_sudoku_ui = DummySudokuUI()
		self.dummy_memory_ui = DummyMemoryUI()

	def test_cant_instance_abstract_gui_memory_utilities_class(self):
		self.assertRaises(
			NotImplementedError,
			sudokugui.SudokuGUIMemoryUtilities,
			self.dummy_memory_ui,
			self.dummy_sudoku_ui
			)

	def test_instance_gui_memory_main_frame_builder(self):
		gui_memory_builder = sudokugui.GUIMemoryMainFrameBuilder(
			self.dummy_memory_ui,
			self.dummy_sudoku_ui
		)
		actual_memory_builder_tuple = (
			gui_memory_builder.gui,
			gui_memory_builder.memory_gui
		)
		self.assertEqual(
			actual_memory_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_memory_ui)
		)
		try:
			self.assertEqual(
				self.dummy_memory_ui.memory_radio_buttons,
				[]
			)
			self.assertTrue(
				isinstance(
					self.dummy_memory_ui.memory_int_var,
					IntVar
				)
			)
		except:
			assert False

	def test_instance_gui_memory_bottom_frame_builder(self):
		gui_memory_builder = sudokugui.GUIMemoryBottomFrameBuilder(
			self.dummy_memory_ui,
			self.dummy_sudoku_ui
		)
		actual_memory_builder_tuple = (
			gui_memory_builder.gui,
			gui_memory_builder.memory_gui
		)
		self.assertEqual(
			actual_memory_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_memory_ui)
		)

	def test_instance_gui_memory_builder(self):
		gui_memory_builder = sudokugui.SudokuGUIMemoryBuilder(
			self.dummy_memory_ui,
			self.dummy_sudoku_ui,
			0
		)
		actual_memory_builder_tuple = (
			gui_memory_builder.gui,
			gui_memory_builder.memory_gui,
			gui_memory_builder.mode
		)
		self.assertEqual(
			actual_memory_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_memory_ui, 0)
		)
		self.assertTrue(
			isinstance(
				gui_memory_builder.main_frame_builder,
				sudokugui.GUIMemoryMainFrameBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_memory_builder.bottom_frame_builder,
				sudokugui.GUIMemoryBottomFrameBuilder
			)
		)

	def test_instance_gui_memory_dialog_load_mode(self):
		gui_memory_dialog = sudokugui.SudokuGUIMemoryDialog(
			self.dummy_sudoku_ui,
			1
		)
		self.assertTrue(
			isinstance(
				gui_memory_dialog.memory_builder,
				sudokugui.SudokuGUIMemoryBuilder
			)
		)
		self.assertEqual(gui_memory_dialog.memory_builder.mode, 1)
		self.assertEqual(self.dummy_sudoku_ui, gui_memory_dialog.gui)
	
	def test_instance_gui_memory_dialog_save_mode(self):
		gui_memory_dialog = sudokugui.SudokuGUIMemoryDialog(
			self.dummy_sudoku_ui,
			0
		)
		self.assertTrue(
			isinstance(
				gui_memory_dialog.memory_builder,
				sudokugui.SudokuGUIMemoryBuilder,
			)
		)
		self.assertEqual(gui_memory_dialog.memory_builder.mode, 0)
		self.assertEqual(self.dummy_sudoku_ui, gui_memory_dialog.gui)
		try:
			self.assertTrue(
				isinstance(
					gui_memory_dialog.memory_name_string_var,
					StringVar
				)
			)
		except:
			assert False


class TestSudokuGUISettings(unittest.TestCase):
	def setUp(self):
		self.dummy_sudoku_ui = DummySudokuUI()
		self.dummy_settings_ui = DummySettingsUI()
			
	def test_cant_instance_abstract_gui_settings_utilities_class(self):
		self.assertRaises(
			NotImplementedError,
			sudokugui.SudokuGUISettingsUtilities,
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
			)

	def test_instance_gui_settings_input_type_builder(self):
		gui_settings_builder = sudokugui.GUISettingsInputTypeBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_settings_builder_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertEqual(
			actual_settings_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)
		try:
			self.assertEqual(
				self.dummy_settings_ui.input_type_radio_buttons,
				[]
			)
			self.assertTrue(
				isinstance(
					self.dummy_settings_ui.input_type_string_var,
					StringVar
				)
			)
		except:
			assert False

	def test_instance_gui_settings_output_type_builder(self):
		gui_settings_builder = sudokugui.GUISettingsOutputTypeBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_settings_builder_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertTrue(
			actual_settings_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)
		try:
			self.assertEqual(
				self.dummy_settings_ui.output_type_radio_buttons,
				[]
			)
			self.assertTrue(
				isinstance(
					self.dummy_settings_ui.output_type_string_var,
					StringVar
				)
			)
		except:
			assert False

	def test_instance_gui_settings_default_algorithm_builder(self):
		gui_settings_builder = sudokugui.GUISettingsDefaultAlgorithmBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_settings_builder_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertEqual(
			actual_settings_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)
		try:
			self.assertEqual(
				self.dummy_settings_ui.default_algorithm_radio_buttons,
				[]
			)
			self.assertTrue(
				isinstance(
					self.dummy_settings_ui.default_algorithm_string_var,
					StringVar
				)
			)
		except:
			assert False

	def test_instance_gui_settings_difficulty_level_builder(self):
		gui_settings_builder = sudokugui.GUISettingsDifficultyLevelBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_settings_builder_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertEqual(
			actual_settings_builder_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)
		try:
			self.assertEqual(
				self.dummy_settings_ui.difficulty_level_radio_buttons,
				[]
			)
			self.assertTrue(
				isinstance(
					self.dummy_settings_ui.difficulty_level_string_var,
					StringVar
				)
			)
		except:
			assert False

	def test_instance_gui_settings_bottom_frame_builder(self):
		gui_settings_builder = sudokugui.GUISettingsBottomFrameBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_gui_settings_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertEqual(
			actual_gui_settings_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)

	def test_instance_gui_settings_builder(self):
		gui_settings_builder = sudokugui.SudokuGUISettingsBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
		)
		actual_gui_settings_tuple = (
			gui_settings_builder.gui,
			gui_settings_builder.settings_gui
		)
		self.assertEqual(
			actual_gui_settings_tuple,
			(self.dummy_sudoku_ui, self.dummy_settings_ui)
		)

		self.assertTrue(
			isinstance(
				gui_settings_builder.input_type_builder,
				sudokugui.GUISettingsInputTypeBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_settings_builder.output_type_builder,
				sudokugui.GUISettingsOutputTypeBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_settings_builder.default_algorithm_builder,
				sudokugui.GUISettingsDefaultAlgorithmBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_settings_builder.difficulty_level_builder,
				sudokugui.GUISettingsDifficultyLevelBuilder
			)
		)
	
	def test_instance_gui_settings_dialog(self):
		gui_settings_dialog = sudokugui.SudokuGUISettingsDialog(
			self.dummy_sudoku_ui
		)
		self.assertTrue(
			isinstance(
				gui_settings_dialog.settings_builder,
				sudokugui.SudokuGUISettingsBuilder
			)
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_settings_dialog.gui)
		

class TestSudokuGUI(unittest.TestCase):
	def setUp(self):
		self.dummy_sudoku_ui = DummySudokuUI()
		self.xml_content = [
				"<config>" +
					"<inputType>CSV</inputType>" +
					"<outputType>Console</outputType>" +
					"<defaultAlgorithm>Norvig</defaultAlgorithm>" +
					"<difficultyLevel>Medium</difficultyLevel>" +
				"</config>"
		]
		self.xml_file = "config.xml"
		with open(self.xml_file, 'w') as rawfile:
			rawfile.write(self.xml_content[0])
		self.file_handler_xml = FileHandlerXML(self.xml_file)
		self.expected_tuple_from_file = ("CSV", "Console",\
										"Norvig", "Medium")
	
	def tearDown(self):
		self.file_handler_xml.file.close()
 		try:
 			remove(self.xml_file)
		except:
			pass

	def test_cant_instance_abstract_sudoku_gui_utilities_class(self):
		self.assertRaises(
			NotImplementedError,
			sudokugui.SudokuGUIUtilities,
			self.dummy_sudoku_ui
			)
	
	def test_instance_sudoku_gui_solve_action_set(self):
		gui_action_set = sudokugui.SudokuGUISolveActionSet(
			self.dummy_sudoku_ui
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_action_set.gui)

	def test_instance_sudoku_gui_settings_action_set(self):
		gui_action_set = sudokugui.SudokuGUISettingsActionSet(
			self.dummy_sudoku_ui
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_action_set.gui)

	def test_instance_sudoku_gui_play_action_set(self):
		gui_action_set = sudokugui.SudokuGUIPlayActionSet(
			self.dummy_sudoku_ui
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_action_set.gui)

	def test_instance_sudoku_gui_menu_builder(self):
		gui_builder = sudokugui.SudokuGUIMenuBuilder(self.dummy_sudoku_ui)
		self.assertEqual(self.dummy_sudoku_ui, gui_builder.gui)
	
	def test_instance_sudoku_gui_icon_frame_builder(self):
		gui_builder = sudokugui.SudokuGUIIconFrameBuilder(
			self.dummy_sudoku_ui
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_builder.gui)

	def test_instance_sudoku_gui_squares_builder(self):
		gui_builder = sudokugui.SudokuGUISquaresBuilder(self.dummy_sudoku_ui)
		self.assertEqual(self.dummy_sudoku_ui, gui_builder.gui)

	def test_instance_sudoku_gui_main_frame_builder(self):
		gui_builder = sudokugui.SudokuGUIMainFrameBuilder(
			self.dummy_sudoku_ui
		)
		self.assertEqual(self.dummy_sudoku_ui, gui_builder.gui)
		self.assertTrue(
			isinstance(
				gui_builder.icon_frame_builder,
				sudokugui.SudokuGUIIconFrameBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_builder.sudoku_squares_builder,
				sudokugui.SudokuGUISquaresBuilder
			)
		)
		
	def test_instance_sudoku_gui_builder(self):
		gui_builder = sudokugui.SudokuGUIBuilder(self.dummy_sudoku_ui)
		self.assertEqual(self.dummy_sudoku_ui, gui_builder.gui)
		self.assertTrue(
			isinstance(
				gui_builder.menu_builder,
				sudokugui.SudokuGUIMenuBuilder
			)
		)
		self.assertTrue(
			isinstance(
				gui_builder.main_frame_builder,
				sudokugui.SudokuGUIMainFrameBuilder
			)
		)
		
	def test_instance_sudoku_gui(self):
		sudoku_gui = sudokugui.SudokuGraphicalUserInterface(
			self.file_handler_xml
		)
		self.assertTrue(
			isinstance(
				sudoku_gui.config,
				Configfile
			)
		)
		actual_tuple_from_file = (
			sudoku_gui.config.inputType,
			sudoku_gui.config.outputType,
			sudoku_gui.config.defaultAlgorithm,
			sudoku_gui.config.difficultyLevel
		)
		self.assertEqual(
			self.expected_tuple_from_file,
			actual_tuple_from_file
		)
		self.assertTrue(
			isinstance(
				sudoku_gui.solve_action_set,
				sudokugui.SudokuGUISolveActionSet
			)
		)
		self.assertTrue(
			isinstance(
				sudoku_gui.settings_action_set,
				sudokugui.SudokuGUISettingsActionSet
			)
		)
		self.assertTrue(
			isinstance(
				sudoku_gui.play_action_set,
				sudokugui.SudokuGUIPlayActionSet
			)
		)
		self.assertTrue(
			isinstance(
				sudoku_gui.gui_builder,
				sudokugui.SudokuGUIBuilder
			)
		)
		self.assertEqual(sudoku_gui.config_file, self.file_handler_xml)
		self.assertTrue(sudoku_gui.interactive is None)
		self.assertFalse(sudoku_gui.violation)
		self.assertTrue(sudoku_gui.currently_editing is None)
		self.assertTrue(sudoku_gui.timer < datetime(1900, 1, 1, 0, 0, 0, 1))
		td = timedelta(seconds=1)
		expected_timedelta_tuple = (td.days, td.seconds, td.microseconds)
		actual_timedelta_tuples = (
			sudoku_gui._timer_increment.days,
			sudoku_gui._timer_increment.seconds,
			sudoku_gui._timer_increment.microseconds
		)
		self.assertTrue(expected_timedelta_tuple, actual_timedelta_tuples)

