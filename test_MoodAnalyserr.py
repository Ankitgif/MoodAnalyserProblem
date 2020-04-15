import pytest
from MoodAnalyserr import MoodAnalyserr
class Test_MoodAnalyserrTest:

    def test_givenMessage_WhenSad_ShouldReturnSad(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("This is a sad message")
        assert mood == 'SAD'

    def test_givenMessage_WhenHappy_ShouldReturnHappy(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("This is a happy message")
        assert mood == 'HAPPY'

    def test_givenMessage_WhenNone_ShouldReturnHappy(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood(None)
        assert mood == 'HAPPY'        