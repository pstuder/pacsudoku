import unittest
from os import remove
from sys import path

path.append("../source")

from main import Interface
from sudokuconsole import SudokuConsoleUserInterface 
from inout import FileHandlerXML, FileHandlerTXT, FileHandlerCSV

class TestSudokuConsoleUserInterface(unittest.TestCase):
    
    def setUp(self):
        self.default_file_content = [
                "<config>" +
                    "<inputType>TXT</inputType>" +
                    "<outputType>Console</outputType>" +
                    "<defaultAlgorithm>Backtracking</defaultAlgorithm>" +
                    "<difficultyLevel>Low</difficultyLevel>" +
                "</config>"
        ]
        
        self.xml_default_file = "config_default.xml"
        
        with open(self.xml_default_file, 'w') as rawfile:
            rawfile.write(self.default_file_content[0])
    

        
        self.default_file_handler_xml = FileHandlerXML(self.xml_default_file)

        self.expected_tuple_from_default_file = ("TXT", "Console",\
                                        "Backtracking", "Low")
        
        
        
    def test_default_game_should_print_default_config_values_in_Console(self):
        default_game_selected = SudokuConsoleUserInterface(self.default_file_handler_xml)
        defaul_tuple_from_file = (
            default_game_selected.config.inputType,
            default_game_selected.config.outputType,
            default_game_selected.config.defaultAlgorithm,
            default_game_selected.config.difficultyLevel)
        self.assertEqual(self.expected_tuple_from_default_file, defaul_tuple_from_file)
    
    def test_option_1_return_default_configuration(self):
        default_game_selected = SudokuConsoleUserInterface(self.default_file_handler_xml)
        self.assertEqual('1', '1', default_game_selected.sudokumenu(""))
        
        
if __name__ == "__main__":
    unittest.main()
    