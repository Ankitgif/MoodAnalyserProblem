import pytest
from MoodAnalyserr import MoodAnalyserr
class Test_MoodAnalyserrTest:

    def test_givenMessage_WhenSad_ShouldReturnSad(self):
        moodAnalyser = MoodAnalyserr()
        mood = moodAnalyser.analyseMood("I am in sad mood")
        assert mood == 'SAD'