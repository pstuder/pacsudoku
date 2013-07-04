import unittest
import random
#~ import validmatrix 
from validmatrix import MatrixHandler


class TestLine(unittest.TestCase):
    def setUp(self):
        self.start_matrix = [[4,0,0,0,0,0,8,0,5],[0,3,0,0,0,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,2,0,0,0,0,0,6,0],[0,0,0,0,8,0,4,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,6,0,3,0,7,0],[5,0,0,2,0,0,0,0,0],[1,0,4,0,0,0,0,0,0]]
        #self.start_matrix = [[4,0,4,0,8,0,8,0,5],[0,3,3,0,3,0,3,0,0],[0,4,0,7,0,0,0,0,0],[0,2,0,0,0,0,0,6,0],[0,0,0,0,8,0,4,0,0],[0,0,0,0,1,0,0,0,0],[0,0,0,6,0,3,0,7,0],[5,0,0,2,0,0,0,0,0],[1,0,4,0,0,0,0,0,0]]
        
        self.matrix = MatrixHandler(self.start_matrix)
        self.matrizexpected=matrixForPrint()
        self.input_matrix=MatrixHandler([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
      
        
    def test_matrix_lenght_is_9x9(self):
        valid_lenght = self.matrix.lenght_matrix()
        self.assertEqual(True, valid_lenght)
    
    def test_lines_should_have_numbers_between_0_9(self):
        valid_lines = self.matrix.correct_lines()
        self.assertEqual(True, valid_lines)
    
    def test_columns_should_have_numbers_between_0_9(self):
        valid_columns = self.matrix.correct_columns()
        self.assertEqual(True, valid_columns)
    
    def test_submatrix_should_have_numbers_between_0_9(self):
        valid_submatrix = self.matrix.valid_submatrix_numbers()
        self.assertEqual(True, valid_submatrix)
        
    def test_lines_content_not_repeated_numbers_between_1_9(self):
        valid_line =self.matrix.repeatednumbersline()
        self.assertEqual(True, valid_line)
        
    def test_columns_content_not_repeated_numbers_between_1_9(self):
        valid_column = self.matrix.repeatednumberscolumns()
        self.assertEqual(True, valid_column)
        
    def test_submatrix_content_not_repeated_numbers_between_1_9(self):
        valid_minimatrix = self.matrix.valid_submatrix_repeated()
        self.assertEqual(True, valid_minimatrix)
    
    def test_valid_should_return_True_if_matrix_is_valid(self):
        valid = self.matrix.validate()
        self.assertEqual(True,valid)
        

        
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
    
    