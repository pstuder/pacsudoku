import unittest
from coverage import coverage
from pylint import lint
from sys import path

path.append("../source")
cov=coverage(omit=["test*.py"])
cov.start()

from test_inout import TestFileHandler
from test_inout import TestFileHandlerCSV
from test_inout import TestFileHandlerTXT
from test_inout import TestFileHandlerXML
from test_main import TestInterface
from test_pacsudoku import TestPACSudokuScript
from test_solver import TestAlgorithm
from test_solver import TestNorvigAlgorithm
from test_solver import TestXAlgorithm
from test_solver import TestBacktrackingAlgorithm
from test_sudokuinteractive import Test_sudoku_interactive
from test_sudokugui import TestSudokuGUIMemory
from test_sudokugui import TestSudokuGUISettings
from test_sudokugui import TestSudokuGUI
from testConfig import test_configfile
from testvalidmatrix import TestLine

if __name__=="__main__":
    suite=unittest.TestSuite()

    # Module inout
    suite.addTest(unittest.makeSuite(TestFileHandlerTXT))
    suite.addTest(unittest.makeSuite(TestFileHandlerXML))
    suite.addTest(unittest.makeSuite(TestFileHandlerCSV))
    suite.addTest(unittest.makeSuite(TestFileHandler))

    # Module solver
    suite.addTest(unittest.makeSuite(TestAlgorithm))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestXAlgorithm))
    suite.addTest(unittest.makeSuite(TestBacktrackingAlgorithm))
     
    # Module config
    suite.addTest(unittest.makeSuite(test_configfile))
     
    # Module validmatrix
    suite.addTest(unittest.makeSuite(TestLine))
     
    # Module main
    suite.addTest(unittest.makeSuite(TestInterface))
     
    # Module pacsudoku
    suite.addTest(unittest.makeSuite(TestPACSudokuScript))
    
    # Module sudoku_interactive
    suite.addTest(unittest.makeSuite(Test_sudoku_interactive))

    # Module sudokugui
    suite.addTest(unittest.makeSuite(TestSudokuGUIMemory))
    suite.addTest(unittest.makeSuite(TestSudokuGUISettings))
    suite.addTest(unittest.makeSuite(TestSudokuGUI))

    unittest.TextTestRunner(verbosity=2).run(suite)
    cov.stop()
    cov.save()
    cov.html_report(directory='../../covhtml')
    
    lint.Run([
        '--output-format=html', '--files-output=y', '--reports=n',
        'config', 'inout', 'main', 'pacsudoku', 'solver', 'sudokuconsole',
        'sudokugui', 'sudokuinteractive', 'validmatrix'
    ])
