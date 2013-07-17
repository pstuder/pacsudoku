from copy import deepcopy
import os
import random
import time

from validmatrix import MatrixHandler
from solver import Norvig

class SudokuInteractive():
    
    def __init__(self,matrix):
        self.matrix=MatrixHandler(deepcopy(matrix))
        self.solved=Norvig(self.matrix).solve()
        self.coppy=deepcopy(matrix)
    
    def is_equal_to(self,mat2):
        is_equal=True
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j]!=mat2[i][j]:
                    is_equal=False
        return is_equal
                    
    def change_value_in_cell(self, row,column,value):
        self.matrix.first_matrix[row][column]=value
        
    def sudoku_is_solved(self):
        if self.is_equal_to(self.solved.first_matrix):
            return True
        else:
            return False
    
    def solve_one(self):
        input_list=[]
        for i in range(len(self.matrix.first_matrix)):
            for j in range(len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][j]==0:
                    input_list.append((i,j))
        rand=random.randint(0,len(input_list)-1)
        x,y = input_list[rand]
        self.matrix.first_matrix[x][y]=self.solved.first_matrix[x][y]
        
    def duplicate_values(self):
        return self.duplicate_value_in_row() + self.duplicate_value_in_column()
             
    def duplicate_value_in_row(self):
        dup_list=""
        for i in range(len(self.matrix.first_matrix)):
            if len(self.duplicate_list_row(i))!=0:
                dup_list= dup_list + "Row "+ str(i) + "\n"
        return dup_list 
                  
    def duplicate_list_row(self,row):
        return_list=""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1,len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[row][i]==self.matrix.first_matrix[row][j] and i!=j and self.matrix.first_matrix[row][i]!=0:
                    return_list=return_list + str(self.matrix.first_matrix[row][i])
        return return_list
    
    def duplicate_value_in_column(self):
        dup_list=""
        actual_list=""
        for i in range(len(self.matrix.first_matrix)):
            actual_list=self.duplicate_list_column(i)
            if len(actual_list)!=0:
                dup_list= dup_list + "Column "+ str(i) + "\n" 
        return dup_list 
                  
    def duplicate_list_column(self,column):
        return_list=""
        for i in range(len(self.matrix.first_matrix)):
            for j in range(i+1,len(self.matrix.first_matrix)):
                if self.matrix.first_matrix[i][column]==self.matrix.first_matrix[j][column] and self.matrix.first_matrix[i][column]!=0:
                    return_list=return_list + str(self.matrix.first_matrix[i][column])
        return return_list
    
    def game_start(self):
        return time.clock()
            
    def game_time(self,start_time):
        if self.sudoku_is_solved()==True:
            return time.clock()-start_time
        
