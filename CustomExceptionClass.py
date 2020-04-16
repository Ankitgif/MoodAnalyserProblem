class MoodAnalyseException(Exception):
    
    def __init__(self,message):
        self.message = message
        #super().__init__(message)