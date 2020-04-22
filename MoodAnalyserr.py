from CustomExceptionClass import MoodAnalyseException
class MoodAnalyserr:

    def __init__(self,message=None):
        self.message = message

    def analyseMood(self,message=None):
        try:
            if message == None:
                message = self.message

            if message.__contains__("sad"):
                return "SAD" 
            else:
                return "HAPPY"    
        
        except AttributeError:
            raise MoodAnalyseException("Please enter proper message")

    def __eq__(self,other):
        return self.message == other.message          
