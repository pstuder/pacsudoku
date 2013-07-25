"""config module."""
class Configfile():
    """Config file class.
    Define the config file structure
    """
    supported_inputTypes = ["TXT", "CSV"]
    supported_outputTypes = ["Console", "File"]
    supported_defaultAlgorithms = [
                                "Backtracking", 
                                "Norvig", "XAlgorithm"
                                ]
    supported_difficultyLevels = ["High", "Medium", "Low"]

    def __init__(
                 self,inputType="TXT",outputType="Console",
                 defaultAlgorithm="Backtracking",difficultyLevel="Low"):
        """ This is a constructor of a Configfile class.
        
            The following instance attributes are created:
            inputType -- Define the default file input type. 
                          If it is not defined, 
                          the  default value is TXT.
            outputType -- Define the default output type. 
                           If it is not defined, 
                           the  default value is Console.
            defaultAlgorithm -- Define the default algorithm that 
                                 will be used to solve 
                                 a SUDOKU. If it is not defined, 
                                 the  default value is Backtracking.
            difficultyLevel -- Define the difficult level of a SUDOKU game. 
                                If it is not defined, 
                                the  default value is Low.
        """
        if self.validateInputType(inputType, self.supported_inputTypes)==True:
            self.inputType = inputType
        else:
            self.inputType = "TXT"
        
        if self.validateInputType(outputType, self.supported_outputTypes)==True:
            self.outputType = outputType
        else:
            self.outputType = "Console"
            
        if self.validateInputType(defaultAlgorithm,
                                  self.supported_defaultAlgorithms)==True:    
            self.defaultAlgorithm = defaultAlgorithm
        else:
            self.defaultAlgorithm = "Backtracking"
            
        if self.validateInputType(difficultyLevel,
                                  self.supported_difficultyLevels)==True:
            self.difficultyLevel = difficultyLevel
        else:
            self.difficultyLevel = "Low"

        
    def validateInputType(self, inputtype, formats):
        """
        Validate each input of position Configfile class
        
        The defined parameters means:
        input_type -- Define the parameter input type
        format_list -- List of possible values for each type.
        """
        status = False
        for position in range(len(formats)):
            if inputtype == formats[position]:
                status = True
                break 
            else:
                status = False
        return status


