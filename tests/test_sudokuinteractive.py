import ast
import time
import unittest

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
        self.matrix = [
            [4, 1, 7, 0, 6, 9, 8, 2, 5],
            [6, 3, 2, 1, 5, 8, 9, 4, 7],
            [9, 5, 8, 7, 2, 4, 3, 1, 6],
            [8, 2, 5, 4, 3, 7, 1, 6, 9],
            [7, 9, 1, 5, 8, 6, 4, 3, 2],
            [3, 4, 6, 9, 1, 2, 7, 5, 8],
            [2, 8, 9, 6, 4, 3, 5, 7, 1],
            [5, 7, 3, 2, 9, 1, 6, 8, 4],
            [1, 6, 4, 8, 7, 5, 2, 9, 3]
        ]
        
        self.txt_content_expected = ["Time:0.101974412949 \n",
            "417069825\n",
            "632158947\n",
            "958724316\n",
            "825437169\n",
            "791586432\n",
            "346912758\n",
            "289643571\n",
             "573291684\n",
             "164875293\n"
             ]
        self.one_per_solved_matrix= [[4, 1, 7, 3, 6, 9, 8, 2, 5], 
                                     [6, 3, 2, 1, 5, 8, 9, 4, 7], 
                                     [9, 5, 8, 7, 2, 4, 3, 1, 6], 
                                     [8, 2, 5, 4, 3, 7, 1, 6, 9],
                                     [7, 9, 0, 5, 8, 6, 4, 3, 2], 
                                     [3, 4, 6, 9, 1, 2, 7, 5, 8], 
                                     [2, 8, 9, 6, 4, 3, 5, 7, 1], 
                                     [5, 7, 3, 2, 9, 1, 6, 8, 4], 
                                     [1, 6, 4, 8, 7, 5, 2, 9, 3]]
        
        self.txt_expected_in_pos_1="{1: (0.3981760950066201, [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], 'one per solve'), 2: (0.0, '', '', 'Name2'), 3: (0.0, '', '', 'Name3'), 4: (0.0, '', '', 'Name4'), 5: (0.0, '', '', 'Name5')}"
        self.txt_expected_in_pos_2="{1: (0.0, '', '', 'name1'), 2: (0.9589521154226227, [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], 'one per solve'), 3: (0.0, '', '', 'Name3'), 4: (0.0, '', '', 'Name4'), 5: (0.0, '', '', 'Name5')}"
        self.txt_expected_in_pos_3="{1: (0.0, '', '', 'name1'), 2: (0.0, '', '', 'Name2'), 3: (1.0002711936853625, [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], 'one per solve'), 4: (0.0, '', '', 'Name4'), 5: (0.0, '', '', 'Name5')}"
        self.txt_expected_in_pos_4="{1: (0.0, '', '', 'name1'), 2: (0.0, '', '', 'Name2'), 3: (0.0, '', '', 'Name3'), 4: (1.0894356684998994, [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], 'one per solve'), 5: (0.0, '', '', 'Name5')}"
        self.txt_expected_in_pos_5="{1: (0.0, '', '', 'name1'), 2: (0.0, '', '', 'Name2'), 3: (0.0, '', '', 'Name3'), 4: (0.0, '', '', 'Name4'), 5: (1.201720260536038, [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], [[4, 1, 7, 3, 6, 9, 8, 2, 5], [6, 3, 2, 1, 5, 8, 9, 4, 7], [9, 5, 8, 7, 2, 4, 3, 1, 6], [8, 2, 5, 4, 3, 7, 1, 6, 9], [7, 9, 0, 5, 8, 6, 4, 3, 2], [3, 4, 6, 9, 1, 2, 7, 5, 8], [2, 8, 9, 6, 4, 3, 5, 7, 1], [5, 7, 3, 2, 9, 1, 6, 8, 4], [1, 6, 4, 8, 7, 5, 2, 9, 3]], 'one per solve')}"

        

        self.file_actual = "saved_game.sv"
        self.file_expected = "saved_game_test.sv"

        with open(self.file_expected, 'w') as rawfile:
            for row in self.txt_expected_in_pos_3:
                rawfile.write(row)
        
        file_game=open("../savegame/savegame.sv","w") 
        file_game.write("")
        file_game.close()
        
           
    def tearDown(self):
        try:
            remove(self.file_expected)
        except:
            pass
        try:
            remove(self.file_actual)
        except:
            pass
        try:
            remove("../savegame/savegame.sv")
        except:
            pass
       
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
    
    def test_game_restart_is_current_time(self):
        actual_sudoku=SudokuInteractive(self.duplicate_values_matrix)
        self.assertEqual(type(actual_sudoku.game_restart()),float)
    
    def test_game_restart_change_the_game_to_initial_status(self):
        actual_sudoku=SudokuInteractive(self.start_matrix)
        actual_sudoku.solve_one()
        actual_sudoku.game_restart()
        self.assertEqual(self.start_matrix, actual_sudoku.matrix)
            
    def test_initial_status_matrix_is_not_the_actual_matrix_value_after_solve_one_cell(self):
        actual_sudoku=SudokuInteractive(self.start_matrix)
        actual_sudoku.solve_one()
        self.assertNotEqual(self.start_matrix, actual_sudoku.matrix)

    def test_save_game_save_a_matrix_in_pos_1(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=1
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_save_game_save_a_name_in_pos_1(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=1
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_name, actual_name)
        
    def test_save_game_save_a_matrix_in_pos_2(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=2
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)
        
    def test_save_game_save_a_name_in_pos_2(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=2
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_name, actual_name)
        
    def test_save_game_save_a_matrix_in_pos_3(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=3
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_save_game_save_a_name_in_pos_3(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=3
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_name, actual_name)
    
    def test_save_game_save_a_matrix_in_pos_4(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=4
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)
    
    def test_save_game_save_a_name_in_pos_4(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=4
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_name, actual_name)
    
    def test_save_game_save_a_matrix_in_pos_5(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=5
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)
        actual_time,actual_matrix,actual_first_matrix,actual_name=recuperate_actual_position[pos]
        recuperate_expected_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_expected_position[pos]        
        self.assertEqual(expected_matrix, actual_matrix)
    
    def test_save_game_save_a_name_in_pos_5(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=5
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        current_game=1
        game_name="one per solve"
        with open("../savegame/savegame.sv") as in_file:
            txt_content_actual =in_file.readline()
        in_file.close()
        recuperate_actual_position=recover_values_from_file(txt_content_actual)

        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]

        
        self.assertEqual(expected_name, actual_name)

    def test_that_load_game_from_memory_position_1_restore_a_matrix_stored_in_pos_1(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=1
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        
        actual_time,actual_matrix,actual_first_matrixv,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_that_load_game_from_memory_position_2_restore_a_matrix_stored_in_pos_2(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=2
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        
        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_that_load_game_from_memory_position_3_restore_a_matrix_stored_in_pos_3(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=3
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        
        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_that_load_game_from_memory_position_4_restore_a_matrix_stored_in_pos_4(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=4
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_that_load_game_from_memory_position_5_restore_a_matrix_stored_in_pos_5(self):
        actual_sudoku=SudokuInteractive(self.one_per_solved_matrix)
        pos=5
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0.101974412949,pos,"one per solve")
        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual(expected_matrix, actual_matrix)

    def test_that_load_game_empty(self):
        actual_sudoku=SudokuInteractive([])
        pos=3
        if pos==1:
            verif_file=self.txt_expected_in_pos_1
        if pos==2:
            verif_file=self.txt_expected_in_pos_2
        if pos==3:
            verif_file=self.txt_expected_in_pos_3
        if pos==4:
            verif_file=self.txt_expected_in_pos_4
        if pos==5:
            verif_file=self.txt_expected_in_pos_5
        actual_sudoku.save_game(0,pos,"")
        actual_time,actual_matrix,actual_first_matrix,actual_name=actual_sudoku.load_game(pos)
        recuperate_position=recover_values_from_file(verif_file)
        expected_time,expected_matrix,expected_first_matrix,expected_name=recuperate_position[pos]
        self.assertEqual([], actual_matrix)

def convert_to_matrix(matrix):
    if len(matrix)>3:
        output_mat=[]
        for i in range(0,len(matrix)-8):
            row_mat=[]
            for j in range(i,i+9):
                row_mat.append(int(matrix[j]))
            if (i)%9==0 or i==0:
                output_mat.append(row_mat)
        return output_mat
          
def recover_values_from_file(file_imported):
    memory={}
    if file_imported !=[]:
        memory1=file_imported
        dictionary=ast.literal_eval(memory1)
        for i in range(1,6):
            memory[i]=dictionary[i]
        return memory
                    
    
        
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

