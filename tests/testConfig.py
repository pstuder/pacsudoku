import unittest
from config import Configfile

class test_configfile(unittest.TestCase):
    def setUp(self):
        self.default_config_file=Configfile()
      
    def test_configfile_exists(self):
        self.assertTrue(self.default_config_file) 
    
    def test_default_inputType_is_TXT(self):
        self.assertEqual(self.default_config_file.inputType,"TXT")             

    def test_default_outputType_is_Console(self):
        self.assertEqual(self.default_config_file.outputType,"Console")             
    
    def test_default_defaultAlgorithm_is_Backtracking(self):
        self.assertEqual(self.default_config_file.defaultAlgorithm,"Backtracking")
    
    def test_default_difficultyLevel_is_LOW(self):
        self.assertEqual(self.default_config_file.difficultyLevel,"Low")
    
    def test_load_config_file_with_input_type_CSV(self):
        personal_configfile=Configfile("CSV", "Console","Backtracking","Low")
        self.assertEqual(personal_configfile.inputType,"CSV")
    
    def test_load_config_file_with_output_type_File(self):
        personal_configfile=Configfile("TXT", "File","Backtracking","Low")
        self.assertEqual(personal_configfile.outputType,"File")    

    def test_load_config_file_with_Default_Algorithm_Peter_Novigs(self):
        personal_configfile=Configfile("TXT", "Console","Norvig","Low")
        self.assertEqual(personal_configfile.defaultAlgorithm,"Norvig")         

    def test_load_config_file_with_difficultyLevel_Medium(self):
        personal_configfile=Configfile("TXT", "Console","Backtracking","Medium")
        self.assertEqual(personal_configfile.difficultyLevel,"Medium")   
    
    def test_load_config_file_does_not_allow_values_distinct_to_TXT_and_CSV(self):
        personal_configfile=Configfile("DOC", "Console","Backtracking","Low")
        self.assertEqual(personal_configfile.inputType,"TXT")         
    
    def test_load_config_file_does_not_allow_values_distinct_to_Console_and_File(self):
        personal_configfile=Configfile("TXT", "Printer","Backtracking","Low")
        self.assertEqual(personal_configfile.outputType,"Console")        
    
    def test_load_config_file_does_not_allow_values_distinct_to_Backtracking_Peter_Novigs_or_Other_values(self):
        personal_configfile=Configfile("TXT", "Console","MyAlgorithm","Low")
        self.assertEqual(personal_configfile.defaultAlgorithm,"Backtracking")

    def test_load_config_file_does_not_allow_values_distinct_to_Difficult_level_just_allow_High_Medium_Low_values(self):
        personal_configfile=Configfile("TXT", "Console","Backtracking","Hard")
        self.assertEqual(personal_configfile.difficultyLevel,"Low")
                      
if __name__ == "__main__":
    unittest.main() 