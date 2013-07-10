import sys

#sys.path.append("../source")

import unittest

from coverage import coverage
cov=coverage(omit=["test*.py"])
cov.start()

from test_io import TestFileHandler, TestFileHandlerCSV, TestFileHandlerTXT, TestFileHandlerXML
from test_solver import TestAlgorithm,TestNorvigAlgorithm
from testConfig import test_configfile
from testvalidmatrix import TestLine
from test_main import TestInterface

if __name__=="__main__":
    suite=unittest.TestSuite()
    #Module io
    suite.addTest(unittest.makeSuite(TestFileHandlerTXT))
    suite.addTest(unittest.makeSuite(TestFileHandlerXML))
    suite.addTest(unittest.makeSuite(TestFileHandlerCSV))
    suite.addTest(unittest.makeSuite(TestFileHandler))
    #Module solver
    suite.addTest(unittest.makeSuite(TestAlgorithm))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
     
    #Module config
    suite.addTest(unittest.makeSuite(test_configfile))
     
    #Module validmatrix
    suite.addTest(unittest.makeSuite(TestLine))
     
    #Module main
    suite.addTest(unittest.makeSuite(TestInterface))
     
     
     
     

    unittest.TextTestRunner(verbosity=2).run(suite)
    cov.stop()
    cov.save()
    cov.html_report(directory='../../covhtml')
