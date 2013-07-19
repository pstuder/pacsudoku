import unittest
from sys import path
from Tkinter import Frame
from Tkinter import StringVar

path.append("../source")

import sudokugui
from config import Configfile

class DummySudokuUI(Frame):
	def __init__(self):
		Frame.__init__(self, None)
		self.config = Configfile()

class DummySettingsUI(Frame):
	def __init__(self):
		Frame.__init__(self, None)

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

	def test_instances_of_gui_settings_builder_instance(self):
		gui_settings_builder = sudokugui.SudokuGUISettingsBuilder(
			self.dummy_settings_ui,
			self.dummy_sudoku_ui
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


if __name__ == "__main__":
	unittest.main() 