import random 

class MatrixHandler:
    
    def __init__(self,frst_matrix):
        self.first_matrix = frst_matrix
    
        
    def lenght_sublist(self):
        flag = True
        for i in range(len(self.first_matrix)):
            if (len(self.first_matrix[i])) != 9:
                flag = False
        return flag
    
    
    def lenght_matrix(self):
        if len(self.first_matrix) == 9 and self.lenght_sublist() == True :
            return True
        else:
            return False
     
    
    
    def correct_lines(self):
        if self.lenght_matrix() == True:
            for i in range(0,9):
                for j in range(0,9):
                    if self.first_matrix[i][j]>=0 and self.first_matrix[i][j] <= 9:
                        flag = True
                    else:
                        flag = False
            return flag
        else:
            return False
        
    
    def correct_columns(self):
        if self.lenght_matrix() == True:
            for i in range(0,9):
                for j in range(0,9):
                    if self.first_matrix[j][i]>=0 and self.first_matrix[j][i] <= 9:
                        flag = True
                    else:
                        return False
            return flag
        else:
            return False
    def repeatednumberscolumns(self):
       flag = True
       for i in range(0,9):
            listcolumn = self.first_matrix[0:9][i]
            for j in range(1,9):
                if listcolumn.count(j)>1:
                    flag = False
                    break
       return flag
        
    def repeatednumbersline(self):
        flag = True
        for i in range(0,9):
            listline = self.first_matrix[i][0:9]
            for j in range(1,9):
                if listline.count(j)>1:
                    flag = False
                    break
        return flag
    
    def minimatrixtolist (self,mini_matrix):
        listmatrix = []
        for i in range(0,3):
            for j in range(0,3):
                listmatrix.append(mini_matrix[i][j])
        return listmatrix
    
    def countlistmatrix(self,mini_matrix):
        listmatrix = self.minimatrixtolist(mini_matrix)
        flag = True
        for j in range(1,9):
                if listmatrix.count(j)>1:
                    flag = False
                    break
        return flag
    
    def submatrixvalidnumbers(self,mini_matrix):
        flag= True
        for i in range(0,3):
            for j in range(0,3):
                if mini_matrix[i][j] >=0 and mini_matrix[i][j]<=9:
                    flag = True
                else:
                    flag = False
                    break
        return flag
    
    def submatrix(self,line,column):
        minmatrix = []
        j,endj = column
        i,endi = line
        for x in range(i,endi):
            minmatrix.append(self.first_matrix[x][j:endj])
        return minmatrix
    
    def valid_submatrix_numbers(self):
       if self.lenght_matrix() == True:
            mini_matrix=True
            if mini_matrix != self.countlistmatrix(self.submatrix((0,3),(0,3))) :
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((0,3),(3,6))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((0,3),(6,9))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((3,6),(0,3))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((3,6),(3,6))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((3,6),(6,9))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((6,9),(0,3))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((6,9),(3,6))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.countlistmatrix(self.submatrix((6,9),(6,9))):
                mini_matrix = False
                return mini_matrix
            return mini_matrix
       else:
            return False
      
    def valid_submatrix_repeated(self):
        if self.lenght_matrix() == True:
            mini_matrix=True
            if mini_matrix != self.submatrixvalidnumbers(self.submatrix((0,3),(0,3))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.submatrixvalidnumbers(self.submatrix((0,3),(3,6))):
                mini_matrix = False
                return mini_matrix
            if  mini_matrix != self.submatrixvalidnumbers(self.submatrix((0,3),(6,9))):
                mini_matrix = False
                return mini_matrix
            if  mini_matrix != self.submatrixvalidnumbers(self.submatrix( (3,6),(0,3))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.submatrixvalidnumbers(self.submatrix((3,6),(3,6))):
                mini_matrix = False
                return mini_matrix
            if  mini_matrix != self.submatrixvalidnumbers(self.submatrix((3,6),(6,9))):
                mini_matrix = False
                return mini_matrix
            if  mini_matrix != self.submatrixvalidnumbers(self.submatrix( (6,9),(0,3))):
                mini_matrix = False
                return mini_matrix
            if mini_matrix != self.submatrixvalidnumbers(self.submatrix((6,9),(3,6))):
                mini_matrix = False
                return mini_matrix
            if  mini_matrix != self.submatrixvalidnumbers(self.submatrix((6,9),(6,9))):
                mini_matrix = False
                return mini_matrix
            return mini_matrix
        else:
            return False
        
    
    def validate(self):
        flag = True
        if self.lenght_matrix() == True:
            if self.correct_lines() != True:
                flag = False
                return flag
            if self.correct_columns()!= True:
                flag = False
                return flag
            if self.repeatednumberscolumns() != True:
                flag = False
                return flag
            if self.repeatednumbersline() != True:
                flag = False
                return flag
            if self.valid_submatrix_numbers() !=True:
                flag = False
                return flag
            if self.valid_submatrix_repeated() !=True:
                flag = False
                return flag
            return flag
        else:
            return False
# *******************************************        
# Ariel
# ******************************************* 
    def generator(self,level):   
        self.createBlankTable()
        self.fillSubSquare(1)
        self.fillSubSquare(5)
        self.fillSubSquare(9)
        self.fillPosibilities()
        self.HideCells(level)
                 
        #return self
        
    def createBlankTable(self):
        self.first_matrix =[[0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0,0]]
   
    def fillSubSquare(self,square=1):
        available_values =[1,2,3,4,5,6,7,8,9]
        small_rows = self.getSmallRows(square)
        small_columns = self.getSmallColumns(square)
        
        for i in small_rows:
            for j in small_columns:
                available_values_lenght = len(available_values)
                random_value = random.randint(0,available_values_lenght-1)
                self.first_matrix[i][j]=available_values[random_value]
                available_values.remove(available_values[random_value])
        return self
        
    def getSmallRows(self,square):
        if square==1 or square==2 or square==3:
            return [0,1,2]
        elif square==4 or square==5 or square==6:
            return [3,4,5]
        elif square==7 or square ==8 or square ==9:
            return [6,7,8]
    
    def getSmallColumns(self,square):
        if square==1 or square==4 or square==7 :
            return [0,1,2]
        elif square==2 or square==5 or square==8:
            return [3,4,5]
        elif square==3 or square ==6 or square ==9:
            return [6,7,8]    
    
       

    def fillPosibilities(self):
        counter=0
        while self.countZeroQuantity()!=0 and counter<=200:
            counter+=1
            a=self.inmediateFill()
            for i in range(2,7):    
                self.matrix=self.fillCellWithNPosible_values(i)
        return self
    
    def inmediateFill(self):
        is_filled = 0
        rows=len(self.first_matrix)
        columns=len(self.first_matrix[0])
        for i in range(rows):
            for j in range(columns):
                if self.first_matrix[i][j]==0:
                    posible_values = self.posibleValuesList(i,j)
                    if len(posible_values)==1:
                        self.first_matrix[i][j]=posible_values[0]
                        is_filled=1
        return is_filled
        
    def posibleValuesList(self,row,column):
        list1 =self.posibleVerticalValues(row,column)
        list2 =self.posibleHorizontalValues(row,column)
        list3 =self.posibleSubSquareValues(row,column)
        list1 =self.invertValues(list1)
        list2 =self.invertValues(list2)
        list3 =self.invertValues(list3)
        completeList=list1+list2+list3
        imposible_values_list=[]
        for i in range(1,9): 
            if i in completeList:
                imposible_values_list.append(i)
        posible_values_list = self.invertValues(imposible_values_list)
        return posible_values_list
        
    def posibleVerticalValues(self,row,column):
        available_values =[1,2,3,4,5,6,7,8,9]
        rows =len(self.first_matrix)
        for i in range(rows):
            if i!=row:
                value=self.first_matrix[i][column] 
                if value in available_values: 
                    available_values.remove(value) 
        return available_values
       
    def posibleHorizontalValues(self,row,column):
        available_values =[1,2,3,4,5,6,7,8,9]
        columns =len(self.first_matrix[0])
        for i in range(columns):
            if i!=column:
                value=self.first_matrix[row][i] 
                if value in available_values: 
                    available_values.remove(value) 
        return available_values
        
    def posibleSubSquareValues(self,row,column):
        available_values =[1,2,3,4,5,6,7,8,9]
        square = self.getSquare(row,column)
        small_rows = self.getSmallRows(square)
        small_columns = self.getSmallColumns(square)
        initial_value_of_study_point=self.first_matrix[row][column]
        self.first_matrix[row][column]='study'
        for i in small_rows:
            for j in small_columns:
                if self.first_matrix[i][j]!='study':
                    value=self.first_matrix[i][j]
                    if value in available_values:
                        available_values.remove(value)
        self.first_matrix[row][column]=initial_value_of_study_point 
        return available_values
        
    def getSquare(self,row,column):
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
            
           
    def invertValues(self,posible_values):
        imposible_valuess=[]
        for i in range(1,9): 
            if not(i in posible_values):
                imposible_valuess.append(i)
        return imposible_valuess
        
    def fillCellWithNPosible_values(self,n):
        rows=len(self.first_matrix)
        columns=len(self.first_matrix[0])
        for i in range(rows):
            for j in range(columns):
                if self.first_matrix[i][j]==0: 
                    posible_valuess = self.posibleValuesList(i,j)
                    if len(posible_valuess)==n:
                        self.first_matrix[i][j]=self.getOneFromList(posible_valuess)
        return self  
        
    def getOneFromList(self,input_list):
        """ Get one element of a list randomically """
        list_lenght = len(input_list)
        return input_list[random.randint(0,list_lenght-1)]
    
    def HideCells(self,dificult_level):
        """ Put zeros to some cells in order to generate the initial status of a sudoku game """
        if dificult_level=="Low":
            max_num_zeros = 35
        elif dificult_level =="Medium":
            max_num_zeros = 39
        elif dificult_level =="High":
            max_num_zeros = 42
        else:
            max_num_zeros = 35
        zerosinserted=0
        counter=0
        rows=len(self.first_matrix)
        columns=len(self.first_matrix[0])
        while (max_num_zeros>zerosinserted and counter<10000):
            counter+=1
            row=random.randint(0,rows-1)
            column=random.randint(0,columns-1)
            if self.first_matrix[row][column]!=0:
                if len(self.posibleValuesList(row,column))==1:
                    self.first_matrix[row][column]=0
                    zerosinserted=self.countZeroQuantity()
        if counter==10000 and dificult_level=="Low" and zerosinserted>35:
            self.generator(dificult_level)
        if counter==10000 and dificult_level=="Medium" and (zerosinserted<36 or zerosinserted>39):
            self.generator(dificult_level)
        if counter==10000 and dificult_level=="High" and zerosinserted<42 or dificult_level=="High" and zerosinserted<42:
            self.generator(dificult_level)
        return self
        
    def countZeroQuantity(self):
        """ Count the zeros quantity of a matrix """
        rows=len(self.first_matrix)
        columns=len(self.first_matrix[0])
        zero_quantity=0
        for i in range(rows):
            for j in range(columns):
                if self.first_matrix[i][j]==0:
                    zero_quantity+=1
        return zero_quantity
        
    def printmatrix(self):
        """ Print the matrix in PRD format """
        chain=""
        if len(self.first_matrix)>0:
            for i in range(len(self.first_matrix)):    
                for j in range(len(self.first_matrix)):        
                    if j%3==0 and j!=0:
                        chain=chain + "| "
                    chain=chain + str(self.first_matrix[i][j]) +"   "
                if (i+1)%3==0 and i!=0 and (i+1)!=9:
                    chain=chain + "\n-------------------------------------"
                chain=chain + "\n"
        print chain
        return chain    

