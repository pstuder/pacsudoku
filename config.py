class Configfile():
    def __init__(self,inputType="TXT",outputType="Console",defaultAlgorithm="Backtracking",difficultyLevel="Low"):
        """ This is a constructor of a Configfile class."""
        if self._validateInputType(inputType,["TXT","CSV"])==True:
            self.inputType=inputType
        else:
            self.inputType= "TXT"
        
        if self._validateInputType(outputType,["Console","File"])==True:
            self.outputType=outputType
        else:
            self.outputType="Console"
            
        if self._validateInputType(defaultAlgorithm,["Backtracking","Peter Norvig","Other"])==True:    
            self.defaultAlgorithm=defaultAlgorithm
        else:
            self.defaultAlgorithm="Backtracking"
            
        if self._validateInputType(difficultyLevel,["High","Medium","Low"])==True:
            self.difficultyLevel=difficultyLevel
        else:
            self.difficultyLevel="Low"
        
    def _validateInputType(self,inputtype, formats):
        status=False
        for a in range(len(formats)):
            if inputtype==formats[a]:
                status=True
                break 
            else:
                status=False
        return status
    
    def _create_XML_file(self,inputtype,outputtype,defaultAlgorithm,difficultyLevel):
        newfile=open("config.xml",'w')
        newfile.write("<config>")
        newfile.write("    <inputType>"+ inputtype+"</inputType>")
        newfile.write("    <outputType>"+ outputtype+"</outputType>")
        newfile.write("    <defaultAlgorithm>"+ defaultAlgorithm+"</defaultAlgorithm>")
        newfile.write("    <difficultyLevel>"+ difficultyLevel+"</difficultyLevel>")
        newfile.write("</config>")
        newfile.close()        