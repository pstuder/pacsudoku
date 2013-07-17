import time
import unittest
from sys import path
path.append("../source")

from sudokuinteractive import SudokuInteractive
from validmatrix import MatrixHandler

class Test_sudoku_interactive(unittest.TestCase):

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

        
        self.sudoku_interactive=SudokuInteractive(self.start_matrix)
        
        self.solved_matrix= [[4, 1, 7, 3, 6, 9, 8, 2, 5], 
                             [6, 3, 2, 1, 5, 8, 9, 4, 7], 
                             [9, 5, 8, 7, 2, 4, 3, 1, 6], 
                             [8, 2, 5, 4, 3, 7, 1, 6, 9],
                             [7, 9, 1, 5, 8, 6, 4, 3, 2], 
                             [3, 4, 6, 9, 1, 2, 7, 5, 8], 
                             [2, 8, 9, 6, 4, 3, 5, 7, 1], 
                             [5, 7, 3, 2, 9, 1, 6, 8, 4], 
                             [1, 6, 4, 8, 7, 5, 2, 9, 3]]
        
        self.one_per_solved_matrix= [[4, 1, 7, 3, 6, 9, 8, 2, 5], 
                                     [6, 3, 2, 1, 5, 8, 9, 4, 7], 
                                     [9, 5, 8, 7, 2, 4, 3, 1, 6], 
                                     [8, 2, 5, 4, 3, 7, 1, 6, 9],
                                     [7, 9, 0, 5, 8, 6, 4, 3, 2], 
                                     [3, 4, 6, 9, 1, 2, 7, 5, 8], 
                                     [2, 8, 9, 6, 4, 3, 5, 7, 1], 
                                     [5, 7, 3, 2, 9, 1, 6, 8, 4], 
                                     [1, 6, 4, 8, 7, 5, 2, 9, 3]]
        self.sudoku_one_per_solve=SudokuInteractive(self.one_per_solved_matrix)
        
        self.changed_matrix = [[4,3,0,0,0,0,8,0,5],
                               [0,3,0,0,0,0,0,0,0],
                               [0,0,0,7,0,0,0,0,0],
                               [0,2,0,0,0,0,0,6,0],
                               [0,0,0,0,8,0,4,0,0],
                               [0,0,0,0,1,0,0,0,0],
                               [0,0,0,6,0,3,0,7,0],
                               [5,0,0,2,0,0,0,0,0],
                               [1,0,4,0,0,0,0,0,0]]
        
        self.duplicate_values_matrix = [[4,3,4,0,0,0,8,0,5],
                                        [0,3,0,0,7,0,0,0,0],
                                        [0,0,0,7,0,0,0,5,0],
                                        [0,2,0,0,0,0,0,6,0],
                                        [0,0,0,0,8,1,4,0,0],
                                        [0,0,2,0,1,0,0,0,6],
                                        [0,5,0,6,0,3,0,7,0],
                                        [5,0,0,2,0,0,0,0,7],
                                        [1,0,4,0,3,0,0,0,0]]
    def test_SudokuInteractive_det_matrix_return_a_matrix(self):   
        self.assertTrue(is_equal_to(self.sudoku_interactive.matrix.first_matrix,self.start_matrix))
    
    def test_SudokuInteractive_det_matrix_return_a_solved_matrix(self):   
        self.assertTrue(is_equal_to(self.sudoku_interactive.solved.first_matrix,self.solved_matrix))
    
    def test_change_value_in_cell_row_0_column_1_value_3(self):   
        self.sudoku_interactive.change_value_in_cell(0, 1, 3)
        self.assertTrue(is_equal_to(self.sudoku_interactive.matrix.first_matrix,self.changed_matrix))
    
    def test_is_solved_return_false_if_actual_matrix_is_distinct_to_solved_matrix(self):
        self.sudoku_interactive.change_value_in_cell(0, 1, 3)
        self.assertFalse(self.sudoku_interactive.sudoku_is_solved())
    
    def test_is_solved_return_true_if_the_last_value_is_filled_and_matrix_is_equal_to_solved_matrix(self):
        self.sudoku_one_per_solve.change_value_in_cell(4, 2, 1)
        self.assertTrue(self.sudoku_one_per_solve.sudoku_is_solved())

    def test_solve_one_return_the_matrix_with_one_cell_solved(self):
        actual_count=zero_count(self.sudoku_interactive.matrix.first_matrix)
        self.sudoku_interactive.solve_one()
        expected_value=actual_count-1
        self.assertEqual(expected_value,zero_count(self.sudoku_interactive.matrix.first_matrix))

    def test_return_list_of_rows_duplicated(self):
        actual_sudoku=SudokuInteractive(self.duplicate_values_matrix)
        actual_value=actual_sudoku.duplicate_value_in_row()
        expected_value="Row 0\n"
        self.assertEqual(expected_value,actual_value)

    def test_return_list_of_columns_duplicated(self):
        actual_sudoku=SudokuInteractive(self.duplicate_values_matrix)
        actual_value=actual_sudoku.duplicate_value_in_column()
        expected_value="Column 1\nColumn 2\n"
        self.assertEqual(expected_value,actual_value)
        
    def test_return_list_of_duplicated_values(self):
        actual_sudoku=SudokuInteractive(self.duplicate_values_matrix)
        actual_value=actual_sudoku.duplicate_values()
        expected_value="Row 0\nColumn 1\nColumn 2\nQuadrant 1\nQuadrant 2\n"+\
        "Quadrant 3\nQuadrant 4\nQuadrant 5\nQuadrant 6\nQuadrant 7\n"+\
        "Quadrant 8\nQuadrant 9\n"
        self.assertEqual(expected_value,actual_value)

    def test_game_start_is_current_time(self):
        actual_sudoku=SudokuInteractive(self.duplicate_values_matrix)
        self.assertEqual(type(actual_sudoku.game_start()),float)
    
    def test_game_time_is_returned_when_the_game_is_solved(self):
        actual_sudoku=SudokuInteractive(self.solved_matrix)
        start=actual_sudoku.game_start()
        game_time=actual_sudoku.game_time(start)
        self.assertEqual(type(game_time),float)
    
    
        
def is_equal_to(mat1,mat2):
    is_equal=True
    for i in range(len(mat1)):
        for j in range(len(mat1)):
            if mat1[i][j]!=mat2[i][j]:
                is_equal=False
    return is_equal

def zero_count(table):
    """Return a int value with the count of zeros of a matrix. """
    rows=len(table)
    columns=len(table[0])
    zero_count=0
    for i in range(rows):
        for j in range(columns):
            if table[i][j]==0:
                zero_count+=1
    return zero_count    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()