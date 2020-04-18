from MoodAnalyserr import MoodAnalyserr
class MoodAnalyserFactory():

    # def __init__(self,message):
    #     self.message = message

    def create_Object(self,message):
        myObj = MoodAnalyserr(message)
        #mood = myObj.analyseMood("I am in a happy mood")
        return myObj

    @staticmethod
    def createMoodAnalyser(message):
        moodAnalyserr = MoodAnalyserr(message)
        return moodAnalyserr
        
      




