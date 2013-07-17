from copy import deepcopy
import os
import random
import time

from validmatrix import MatrixHandler
from solver import Norvig

class SudokuInteractive():
    
    def __init__(self,matrix):
        """Initializes a new algorithm instance.
        - matrix receive a MatrixHandler instance of a input matrix  
        - solved Handle the input matrix solved
        - copy Take a copy of initial matrix
        """
        self.matrix=MatrixHandler(deepcopy(matrix))
        self.solved=Norvig(self.matrix).solve()
        self.copy=deepcopy(matrix)
    
    def is_equal_to(self,mat2):
        """ Compare two matrix 
        if all elements of a matrix are equal, return true.  
        """
        is_equal=True
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j]!=mat2[i][j]:
                    is_equal=False
        return is_equal
                    
    def change_value_in_cell(self, row,column,value):
        """ Change a value in a specific cell delimited be row and column. """
        self.matrix.first_matrix[row][column]=value
        
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
        input_list=[]
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j]==0:
                    input_list.append((i,j))
        rand=random.randint(0,len(input_list)-1)
        x,y = input_list[rand]
        self.matrix.first_matrix[x][y]=self.solved.first_matrix[x][y]
        return x,y
        
    def duplicate_values(self):
        """ Return the duplicate values in rows and columns. """
        return_list=""
        return_list=self.duplicate_value_in_row() +self.duplicate_value_in_column()
        return_list=return_list+self.duplicate_value_in_sub_square()
        return return_list 
            
             
    def duplicate_value_in_row(self):
        """ Return the duplicate values in rows. """
        dup_list=""
        for i in range(len(self.matrix.first_matrix)):
            if len(self.duplicate_list_row(i))!=0:
                dup_list= dup_list + "Row "+ str(i) + "\n"
        return dup_list 
                  
    def duplicate_list_row(self,row):
        """ Return the duplicate values in one row. """
        return_list=""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1,len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[row][i]==self.matrix.first_matrix[row][j] and i!=j and self.matrix.first_matrix[row][i]!=0:
                    return_list=return_list + str(self.matrix.first_matrix[row][i])
        return return_list
    
    def duplicate_value_in_column(self):
        """ Return the duplicate values in columns. """
        dup_list=""
        actual_list=""
        for i in range(len(self.matrix.first_matrix)):
            actual_list=self.duplicate_list_column(i)
            if len(actual_list)!=0:
                dup_list= dup_list + "Column "+ str(i) + "\n" 
        return dup_list 
                  
    def duplicate_list_column(self,column):
        """ Return the duplicate values in one column. """
        return_list=""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1,len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][column]==self.matrix.first_matrix[j][column] and self.matrix.first_matrix[i][column]!=0:
                    return_list=return_list + str(self.matrix.first_matrix[i][column])
        return return_list
    
    def duplicate_value_in_sub_square(self):
        """ Return the duplicate values in sub squares. """
        dup_list=""
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(0,2,0,2) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(0,2,3,5) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(0,2,6,8) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(3,5,0,2) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(3,5,3,5) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(3,5,6,8)
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(6,8,0,2) 
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(6,8,3,5)
        dup_list= dup_list + self.duplicate_value_in_one_sub_square(6,8,6,8)
        return dup_list
        
    def duplicate_value_in_one_sub_square(self,x1,x2,y1,y2):
        """ Return the duplicate values in one sub square. """
        dup_list=""
        available_values =[1,2,3,4,5,6,7,8,9]
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                value=self.matrix.first_matrix[i][j]
                if value!=0: 
                    if value in available_values:
                        available_values.remove(value) 
                    else:
                        dup_list= "Quadrant "+ str(self.get_quadrant(i,j)) + "\n"
        return dup_list 
       
    
    def get_quadrant(self,row,column):
        """Return a sub square where a row and column point in a matrix. """
        if row <=2 and column<=2:
            return 1
        elif row <=5 and column<=2:
            return 4
        elif row <=8 and column<=2:
            return 7
        elif row <=2 and column<=5:
            return 2
        elif row <=5 and column<=5:
            return 5
        elif row <=8 and column<=5:
            return 8
        elif row <=2 and column<=8:
            return 3
        elif row <=5 and column<=8:
            return 6
        elif row <=8 and column<=8:
            return 9
    
        
    def game_start(self):
        """ Return the current time. """
        return time.clock()
            
    def game_time(self,start_time):
        """ Return the completed game time if the game is solved. """
        if self.sudoku_is_solved()==True:
            return time.clock()-start_time
        
