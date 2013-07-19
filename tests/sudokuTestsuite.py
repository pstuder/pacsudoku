import unittest

from sys import path
from coverage import coverage

path.append("../source")
cov=coverage(omit=["test*.py"])
cov.start()

from test_inout import TestFileHandler
from test_inout import TestFileHandlerCSV
from test_inout import TestFileHandlerTXT
from test_inout import TestFileHandlerXML
from test_solver import TestAlgorithm
from test_solver import TestNorvigAlgorithm
from test_solver import TestXAlgorithm
from test_solver import TestBacktrackingAlgorithm
from testConfig import test_configfile
from testvalidmatrix import TestLine
from test_main import TestInterface
from test_pacsudoku import TestPACSudokuScript
from test_sudokuinteractive import Test_sudoku_interactive

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

    unittest.TextTestRunner(verbosity=2).run(suite)
    cov.stop()
    cov.save()
    cov.html_report(directory='../../covhtml')
