class Configfile():
    supported_input_type_list = ["TXT", "CSV"]
    supported_output_type_list = ["Console", "File"]
    supported_default_algorithm_list = [
                                "Backtracking", 
                                "Norvig", "XAlgorithm"
                                ]
    supported_difficulty_level_list = ["High","Medium", "Low"]

    def __init__(
                 self,input_type="TXT",output_type="Console",
                 default_algorithm="Backtracking",difficulty_level="Low"):
        """ This is a constructor of a Configfile class.
        
            The following instance attributes are created:
            input_type -- Define the default file input type. 
                          If it is not defined, 
                          the  default value is TXT.
            output_type -- Define the default output type. 
                           If it is not defined, 
                           the  default value is Console.
            default_algorithm -- Define the default algorithm that 
                                 will be used to solve 
                                 a SUDOKU. If it is not defined, 
                                 the  default value is Backtracking.
            difficulty_level -- Define the difficult level of a SUDOKU game. 
                                If it is not defined, 
                                the  default value is Low.
        """
        if self.validate_input_type(
                        input_type, self.supported_input_type_list)==True:
            self.input_type=input_type
        else:
            self.input_type= "TXT"
        
        if self.validate_input_type(
                        output_type,self.supported_output_type_list)==True:
            self.output_type=output_type
        else:
            self.output_type="Console"
            
        if self.validate_input_type(
                        default_algorithm,
                        self.supported_default_algorithm_list)==True:    
            self.default_algorithm=default_algorithm
        else:
            self.default_algorithm="Backtracking"
            
        if self.validate_input_type(
                        difficulty_level,
                        self.supported_difficulty_level_list)==True:
            self.difficulty_level=difficulty_level
        else:
            self.difficulty_level="Low"
        
    def validate_input_type(self,input_type, format_list):
        """
        Validate each input of a Configfile class
        
        The defined parameters means:
        input_type -- Define the parameter input type
        format_list -- List of possible values for each type.
        """
        status=False
        for a in range(len(format_list)):
            if input_type==format_list[a]:
                status=True
                break 
            else:
                status=False
        return status

