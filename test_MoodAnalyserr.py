import pytest
from MoodAnalyserr import MoodAnalyserr
from CustomExceptionClass import MoodAnalyseException
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
               
           