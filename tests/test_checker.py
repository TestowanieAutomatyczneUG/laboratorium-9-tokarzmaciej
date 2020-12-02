from src.sample.checker import *
from unittest.mock import *
from unittest import TestCase, main


class test_checker(TestCase):
    def test_reminder_turn_on(self):
        test_object = Checker()
        test_object.environment.getTime = Mock(name="getTime")
        test_object.environment.getTime.return_value = 20
        test_object.environment.wavWasPlayed = Mock(name="wavWasPlayed")
        test_object.environment.wavWasPlayed.return_value = True
        test_object.environment.playWavFile = Mock(name="playWavFile")
        test_object.environment.playWavFile.return_value = test_object.environment.wavWasPlayed()
        result = test_object.remainder("file")
        self.assertEqual(True, result)

    def test_reminder_time_turn_off(self):
        test_object = Checker()
        test_object.environment.getTime = Mock(name="getTime")
        test_object.environment.getTime.return_value = 15
        test_object.environment.resetWav = Mock(name="resetWav")
        test_object.environment.resetWav.return_value = False
        result = test_object.remainder("file")
        self.assertEqual(False, result)


if __name__ == '__main__':
    main()
