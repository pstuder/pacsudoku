import unittest
import random

from validmatrix import MatrixHandler


class TestLine(unittest.TestCase):
    
    def setUp(self):
        self.start_matrix = [[4,0,0,0,0,0,8,0,5],
                             [0,3,0,0,0,0,0,0,0],
                             [0,0,0,7,0,0,0,0,0],
                             [0,2,0,0,0,0,0,6,0],
                             [0,0,0,0,8,0,4,0,0],
                             [0,0,0,0,1,0,0,0,0],
                             [0,0,0,6,0,3,0,7,0],
                             [5,0,0,2,0,0,0,0,0],
                             [1,0,4,0,0,0,0,0,0]]
        
        self.repeated_values = [[1,2,3,4,5,6,7,8,0],
                            [0,0,2,0,0,0,0,0,2],
                            [0,9,2,1,4,0,0,0,3],
                            [0,0,3,0,0,0,7,0,4],
                            [0,0,0,0,7,0,0,0,5],
                            [0,0,0,7,0,0,3,0,6],
                            [0,0,0,0,1,0,0,0,7],
                            [0,0,1,0,0,2,8,0,8],
                            [0,0,0,0,0,0,0,0,9]]
        
        self.invalid_numbers = [[1,2,3,4,5,10,7,8,0],
                            [0,0,2,0,0,0,15,0,2],
                            [0,9,2,1,4,0,0,0,3],
                            [0,0,3,0,20,0,7,0,4],
                            [0,0,0,0,7,-1,0,0,5],
                            [0,0,-9,7,0,0,3,0,6],
                            [0,0,0,0,1,0,0,0,7],
                            [0,0,1,0,0,2,8,0,8],
                            [0,0,0,0,0,0,0,0,9]]
        
        self.invalid_length = [[2,3,5,8,3],
                               [4,6,8,8,9,3],
                               [1],
                               [1,2,5,8]]
        
        self.matrix_invalid_numbers = MatrixHandler(self.invalid_numbers)
        self.matrix_repeated_numbers = MatrixHandler(self.repeated_values)
        self.matrix_invalid_length = MatrixHandler(self.invalid_length)
        self.matrix = MatrixHandler(self.start_matrix)
        self.matrizexpected = matrixForPrint()
        
        self.input_matrix = MatrixHandler([[1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9],
                                         [1,2,3,4,5,6,7,8,9]])
      
    def test_matrix_length_is_9x9(self):
        valid_length = self.matrix.length_matrix()
        self.assertEqual(True, valid_length)
    
    def test_False_is_returned_if_matrix_is_not_9x9(self):
        invalid_length = self.matrix_invalid_length.length_matrix()
        self.assertFalse(invalid_length)
    
    
    def test_lines_should_have_numbers_between_0_9(self):
        valid_lines = self.matrix.correct_lines()
        self.assertEqual(True, valid_lines)
    
    def test_lines_should_return_False_if_numbers_grather_than_or_less_than_0_to_9(self):
        valid_lines = self.matrix_invalid_numbers.correct_lines()
        self.assertFalse(valid_lines)
        
    def test_columns_should_have_numbers_between_0_9(self):
        valid_columns = self.matrix.correct_columns()
        self.assertEqual(True, valid_columns)
    
    def test_columns_should_return_False_if_numbers_are_not_between_0_9(self):
        valid_columns = self.matrix_invalid_numbers.correct_columns()
        self.assertFalse(valid_columns)
    
    def test_submatrix_should_have_numbers_between_0_9(self):
        valid_submatrix = self.matrix.valid_submatrix_numbers()
        self.assertEqual(True, valid_submatrix)
        
    def test_submatrix_should_retur_False_if_numbers_are_not_between_0_9(self):
        valid_submatrix = self.matrix_invalid_numbers.valid_submatrix_numbers()
        self.assertFalse(valid_submatrix)
        
    def test_lines_content_not_repeated_numbers_between_1_9(self):
        valid_line = self.matrix.repeatednumbersline()
        self.assertEqual(True, valid_line)
        
    def test_lines_content_should_return_False_if_there_are_repeated_numbers_between_1_9(self):
        valid_line = self.matrix_repeated_numbers.repeatednumbersline()
        self.assertFalse(valid_line)
                         
    def test_columns_content_not_repeated_numbers_between_1_9(self):
        valid_column = self.matrix.repeatednumberscolumns()
        self.assertEqual(True, valid_column)
        
    def test_columns_content_should_return_False_if_there_are_repeated_numbers_between_1_9(self):
        valid_column = self.matrix_repeated_numbers.repeatednumberscolumns()
        self.assertFalse(valid_column)
        
    def test_submatrix_content_not_repeated_numbers_between_1_9(self):
        valid_minimatrix = self.matrix.valid_submatrix_repeated()
        self.assertEqual(True, valid_minimatrix)
    
    def test_submatrix_content_should_return_False_if_there_are_repeated_numbers_between_1_9(self):
        valid_minimatrix = self.matrix_repeated_numbers.valid_submatrix_repeated()
        self.assertFalse(valid_minimatrix)
    
    def test_valid_should_return_True_if_matrix_is_valid(self):
        valid = self.matrix.validate()
        self.assertEqual(True,valid)
        
    def test_valid_should_return_False_if_matrix_is_not_valid(self):
        valid = self.matrix_invalid_length.validate()
        self.assertFalse(valid)
        
# *******************************************        
# Ariel
# *******************************************     
    
        
    def testHideCells_is_equal_to_35_when_the_dificult_level_is_Low(self):
        input_matrix=MatrixHandler([])
        input_matrix.generator("Low")
        actual_result= input_matrix.countZeroQuantity()
        self.assertTrue(actual_result>=1 and actual_result<=35)

    def testHideCells_is_equal_to_39_when_the_dificult_level_is_Medium(self):
        input_matrix=MatrixHandler([])
        input_matrix.generator("Medium")
        actual_result=input_matrix.countZeroQuantity()
        self.assertTrue(actual_result>=36 and actual_result<=39)

    def testHideCells_is_equal_to_42_when_the_dificult_level_is_High(self):
        input_matrix=MatrixHandler([])
        input_matrix.generator("High")
        actual_result =input_matrix.countZeroQuantity()
        self.assertTrue(actual_result>=42)
        
    def test_printmatrix_format(self):
        actual_result=self.input_matrix.printmatrix()
        self.assertEqual(self.matrizexpected,actual_result)
        
def matrixForPrint():
    matrix=[[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
    chain=""
    for i in range(len(matrix)):    
        for j in range(len(matrix)):        
            if j%3==0 and j!=0:
                #~ print"|"
                chain=chain + "| "
            chain=chain + str(matrix[i][j]) +"   "
        if (i+1)%3==0 and i!=0 and (i+1)!=9:
            chain=chain + "\n-------------------------------------"
        chain=chain + "\n"
    return chain

        
if __name__ == '__main__':
    unittest.main()
    
    