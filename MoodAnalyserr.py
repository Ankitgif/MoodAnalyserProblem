from CustomExceptionClass import MoodAnalyseException
class MoodAnalyserr:

    def analyseMood(self,message):
        try:

            if message.__contains__("sad"):
                return "SAD"
            else:
                return "HAPPY"    
        
        except Exception as e:
            raise MoodAnalyseException("Please enter proper message")
