"""sudokuinteractive module 
contains SudokuInteractive class with interactive methods. 
"""
from copy import deepcopy
import random
import time
import ast

from validmatrix import MatrixHandler
from solver import Norvig

class SudokuInteractive():
    """SudokuInteractive class.
    Define methods to play a interactive sudoku game.
    """
    def __init__(self, matrix):
        """Initializes a new algorithm instance.
        - matrix receive a MatrixHandler instance of a input matrix  
        - solved Handle the input matrix solved
        - copy Take a copy of initial matrix
        """
        self.matrix = MatrixHandler(deepcopy(matrix))
        self.solved = Norvig(self.matrix).solve()
        self.copy = deepcopy(matrix)
        self.memory = {}
        input_file = "../savegame/savegame.sv"
        
        input_file = open(input_file, "r")
        file_imported = input_file.readlines()
        input_file.close()
        if file_imported != []:
            self.memory = self.recover_values_from_file()
        else: 
            self.memory = {1:(0.0, "", "", "name1"), 
                    2:(0.0, "", "", "Name2"), 
                    3:(0.0, "", "", "Name3"), 
                    4:(0.0, "", "", "Name4"),
                    5:(0.0, "", "", "Name5")}
            input_file_name = "../savegame/savegame.sv"
            input_file = open(input_file_name, "w")
            input_file.write(str(self.memory))
            input_file.close()
        

    
    def is_equal_to(self, mat2):
        """ Compare two matrix 
        if all elements of a matrix are equal, return true.  
        """
        is_equal = True
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j] != mat2[i][j]:
                    is_equal = False
        return is_equal
                    
    def change_value_in_cell(self, row, column, value):
        """ Change a value in a specific cell delimited be row and column. """
        self.matrix.first_matrix[row][column] = value
        
    def sudoku_is_solved(self):
        """ Return True if a sudoku game is solved. """
        if self.is_equal_to(self.solved.first_matrix):
            return True
        else:
            return False
    
    def solve_one(self):
        """ Solve one cell of unsolved cells. 
        This method is used for generate hints.
        """
        input_list = []
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j] == 0:
                    input_list.append((i, j))
        rand = random.randint(0, len(input_list)-1)
        randomic_x, randomic_y = input_list[rand]
        self.matrix.first_matrix[randomic_x][randomic_y] = \
                        self.solved.first_matrix[randomic_x][randomic_y]
        return randomic_x, randomic_y
        
    def duplicate_values(self):
        """ Return the duplicate values in rows and columns. """
        return_list = ""
        return_list = self.duplicate_value_in_row()+\
                      self.duplicate_value_in_column()
        return_list = return_list + self.duplicate_value_in_sub_square()
        return return_list 
            
             
    def duplicate_value_in_row(self):
        """ Return the duplicate values in rows. """
        dup_list = ""
        for i in range(len(self.matrix.first_matrix)):
            if len(self.duplicate_list_row(i))!= 0:
                dup_list = dup_list + "Row "+ str(i) + "\n"
        return dup_list 
                  
    def duplicate_list_row(self, row):
        """ Return the duplicate values in one row. """
        return_list = ""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1, len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[row][i] == \
                         self.matrix.first_matrix[row][j] \
                         and i != j \
                         and self.matrix.first_matrix[row][i] != 0:
                    return_list = return_list + \
                                  str(self.matrix.first_matrix[row][i])
        return return_list
    
    def duplicate_value_in_column(self):
        """ Return the duplicate values in columns. """
        dup_list = ""
        actual_list = ""
        for i in range(len(self.matrix.first_matrix)):
            actual_list = self.duplicate_list_column(i)
            if len(actual_list) != 0:
                dup_list = dup_list + "Column " + str(i) + "\n" 
        return dup_list 
                  
    def duplicate_list_column(self, column):
        """ Return the duplicate values in one column. """
        return_list = ""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1, len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][column] == \
                        self.matrix.first_matrix[j][column]\
                        and self.matrix.first_matrix[i][column] != 0:
                    return_list = return_list + \
                                  str(self.matrix.first_matrix[i][column])
        return return_list
    
    def duplicate_value_in_sub_square(self):
        """ Return the duplicate values in sub squares. """
        dup_list = ""
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(0, 2, 0, 2) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(0, 2, 3, 5) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(0, 2, 6, 8) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(3, 5, 0, 2) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(3, 5, 3, 5) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(3, 5, 6, 8)
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(6, 8, 0, 2) 
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(6, 8, 3, 5)
        dup_list = dup_list + \
                   self.duplicate_in_one_subsquare(6, 8, 6, 8)
        return dup_list
        
    def duplicate_in_one_subsquare(self, x_one, x_two, y_one, y_two):
        """ Return the duplicate values in one sub square. """
        dup_list = ""
        available_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in range(x_one, x_two+1):
            for j in range(y_one, y_two+1):
                value = self.matrix.first_matrix[i][j]
                if value != 0: 
                    if value in available_values:
                        available_values.remove(value) 
                    else:
                        dup_list = "Quadrant "+ str(self.get_quadrant(i, j))\
                                    + "\n"
        return dup_list 
       
    
    def get_quadrant(self, row, column):
        """Return a sub square where a row and column point in a matrix. """
        if row <= 2 and column <= 2:
            quadrant = 1
        elif row <= 5 and column <= 2:
            quadrant = 4
        elif row <= 8 and column <= 2:
            quadrant = 7
        elif row <= 2 and column <= 5:
            quadrant = 2
        elif row <= 5 and column <= 5:
            quadrant = 5
        elif row <= 8 and column <= 5:
            quadrant = 8
        elif row <= 2 and column <= 8:
            quadrant = 3
        elif row <= 5 and column <= 8:
            quadrant = 6
        elif row <= 8 and column <= 8:
            quadrant = 9
        return quadrant
    
        
    def game_start(self):
        """ Return the current time. """
        return time.clock()
            
    def game_time(self, start_time):
        """ Return the completed game time if the game is solved. """
        if self.sudoku_is_solved() == True:
            return time.clock()-start_time
    
    def game_restart(self):
        """ Return the current time. """
        self.matrix = self.copy
        return time.clock()
    
    def save_game(self, game_start_time, memory_position, game_name):
        """Save interactive game in specific memory position 
        also allows to the user to set a name to the game.  
        """
        self.memory = self.recover_values_from_file()
        memory = self.recover_values_from_file()
        matrix_for_save = self.matrix.first_matrix
        input_file_name = "../savegame/savegame.sv"
        input_file = open(input_file_name, "w")
        actual_time = time.clock()-game_start_time
        for i in range(1, 6):
            if memory_position == i:
                memory[i] = (
                             actual_time, matrix_for_save, \
                             self.copy, game_name
                            )
        input_file.write(str(memory))
        input_file.close()
   
    def recover_values_from_file(self):
        """Recover values from the stored memory structure. """
        input_file = "../savegame/savegame.sv"
        input_file = open(input_file, "r")
        file_imported = input_file.readlines()
        input_file.close()
        if file_imported != []:
            memory1 = file_imported[0]
            dictionary = ast.literal_eval(memory1)
            for i in range(1, 6):
                self.memory[i] = dictionary[i]
        return self.memory

    def load_game(self, memory_position):
        """Load one game from the stored position. """
        self.memory = self.recover_values_from_file()
        actual_time, matrix, \
            first_matrix, game_name = self.memory[memory_position]
        if matrix:
            del(self.matrix) 
            self.matrix = MatrixHandler(matrix)
        return float(actual_time), matrix, first_matrix, game_name
