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
        self.interactive_console=SudokuConsoleUserInterface(self.default_file_handler_xml)
        
        
    def test_default_game_should_print_default_config_values_in_Console(self):
        default_game_selected = SudokuConsoleUserInterface(self.default_file_handler_xml)
        defaul_tuple_from_file = (
            default_game_selected.config.inputType,
            default_game_selected.config.outputType,
            default_game_selected.config.defaultAlgorithm,
            default_game_selected.config.difficultyLevel)
        self.assertEqual(self.expected_tuple_from_default_file, defaul_tuple_from_file)
    
    def test_that_the_mesage_is_dislayed_with_massege_format(self):
        input_mesage="Example message"
        self.assertEqual(mesage(input_mesage), self.interactive_console.mesage(input_mesage))

    def test_that_the_mesage_is_dislayed_with_header_format(self):
        input_mesage="Example message"
        self.assertEqual(mesage(input_mesage), self.interactive_console.header(input_mesage))
        
    def test_that_the_return_h_m_s_return_the_current_time_as_float(self):
        current_time,h,m,s=self.interactive_console.return_h_m_s()
        self.assertEqual(type(current_time), float)
        
    def test_that_the_return_h_m_s_return_the_seconds_lower_or_equal_to_60(self):
        current_time,h,m,s=self.interactive_console.return_h_m_s()
        self.assertTrue(s<=60)
        
    def test_that_the_return_h_m_s_return_the_minutes_lower_or_equal_to_60(self):
        current_time,h,m,s=self.interactive_console.return_h_m_s()
        self.assertTrue(m<=60)
            
    def test_that_the_return_h_m_s_return_the_hours_type_is_float(self):
        current_time,h,m,s=self.interactive_console.return_h_m_s()
        self.assertEqual(type(h),float)
    
    def test_that_the_return_h_m_s_return_the_hours_type_is_float_when_is_loaded_is_true(self):
        self.interactive_console.loaded_game==True
        current_time,h,m,s=self.interactive_console.return_h_m_s()
        self.assertEqual(type(h),float)


    def test_option_1_return_default_configuration(self):
        default_game_selected = SudokuConsoleUserInterface(self.default_file_handler_xml)
        self.assertIsInstance(default_game_selected,SudokuConsoleUserInterface)

    #===========================================================================
    # def test_option_1_return_default_configuration(self):
    #     default_game_selected = SudokuConsoleUserInterface(self.default_file_handler_xml)
    #     self.assertEqual('1', '1', default_game_selected.sudokumenu(""))
    #===========================================================================

    
def mesage(mesage):
    print "**************************************"
    print mesage
    print "**************************************"
    
        
if __name__ == "__main__":
    unittest.main()
    