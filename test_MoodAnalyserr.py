import pytest
from MoodAnalyserr import MoodAnalyserr
class Test_MoodAnalyserrTest:

    def test_givenMessage_WhenSad_ShouldReturnSad(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("This is a sad message")
        assert mood == 'SAD'