class Configfile():
    supported_inputTypes = ["TXT", "CSV"]
    supported_outputTypes = ["Console", "File"]
    supported_defaultAlgorithms = ["Backtracking", "Norvig", "XAlgorithm"]
    supported_difficultyLevels = ["High","Medium", "Low"]

    def __init__(self,inputType="TXT",outputType="Console",defaultAlgorithm="Backtracking",difficultyLevel="Low"):
        """ This is a constructor of a Configfile class."""
        if self.validateInputType(inputType,self.supported_inputTypes)==True:
            self.inputType=inputType
        else:
            self.inputType= "TXT"
        
        if self.validateInputType(outputType,self.supported_outputTypes)==True:
            self.outputType=outputType
        else:
            self.outputType="Console"
            
        if self.validateInputType(defaultAlgorithm,self.supported_defaultAlgorithms)==True:    
            self.defaultAlgorithm=defaultAlgorithm
        else:
            self.defaultAlgorithm="Backtracking"
            
        if self.validateInputType(difficultyLevel,self.supported_difficultyLevels)==True:
            self.difficultyLevel=difficultyLevel
        else:
            self.difficultyLevel="Low"
        
    def validateInputType(self,inputtype, formats):
        status=False
        for a in range(len(formats)):
            if inputtype==formats[a]:
                status=True
                break 
            else:
                status=False
        return status
