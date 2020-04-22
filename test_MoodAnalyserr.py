import pytest
from MoodAnalyserr import MoodAnalyserr
from CustomExceptionClass import MoodAnalyseException
from MoodAnalyserFactory import MoodAnalyserFactory
class Test_MoodAnalyserrTest:

    def test_givenMessage_WhenSad_ShouldReturnSad(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("This is a sad message")
        assert mood == 'SAD'

    def test_givenMessage_WhenHappy_ShouldReturnHappy(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("This is a happy message")
        assert mood == 'HAPPY'

    def test_givenMessage_WhenNone_ShouldThrowCustomException(self):
        try:
            moodAnalyser = MoodAnalyserr()
            mood = moodAnalyser.analyseMood(None)
            

        except Exception as exception:
            assert exception.message == "Please enter proper message"                           
               
    def test_givenMoodAnalyserClass_WhenProper_ShouldReturnObject(self):
        moodAnalyserFactory = MoodAnalyserFactory()
        moodAnalyserr = moodAnalyserFactory.create_Object("I am in a happy mood") 
        mood = moodAnalyserr.analyseMood()
        assert mood == 'HAPPY'      

    def test_givenMoodAnalyserClass_WhenProper_ShouldReturnObjectt(self):
        
        moodAnalyserr1 = MoodAnalyserFactory.createMoodAnalyser("I am in a happy mood") 
        moodAnalyser2 = MoodAnalyserr("I am in a happy mood")
        assert moodAnalyserr1 == moodAnalyser2

    def test_givenNone_thenCalled_defaultContructor_ReturnObject(self):
        
        moodAnalyserr1 = MoodAnalyserFactory.createMoodAnalyser() 
        moodAnalyser2 = MoodAnalyserr()
        assert moodAnalyserr1 == moodAnalyser2

    def test_givenMessage_WhenNone_ShouldThrowSpecialisedException(self):
        
        moodAnalyser = MoodAnalyserr()
        try:
            moodAnalyser.analyseMood(None)    
        except Exception as exception:
            assert type(exception) == MoodAnalyseException     

    def test_givenMessage_WhenEmpty_ShouldThrowCustomException(self):
        try:
            moodAnalyser = MoodAnalyserr()
            mood = moodAnalyser.analyseMood("")
            
        except Exception as exception:
            assert exception.message == "Please enter proper message"   



