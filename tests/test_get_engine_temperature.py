from src.sample.car import *
from unittest.mock import *
from unittest import TestCase, main


class test_Car_getEngineTemperature(TestCase):
    @patch.object(Car, 'getEngineTemperature')
    def test_temperature_engine_positive(self, mock_method):
        # prepare mock
        mock_method.return_value = "70C temperature engine is ok"
        # testing
        test_object = Car()
        result = test_object.getEngineTemperature()
        self.assertEqual("70C temperature engine is ok", result)

    @patch.object(Car, 'getEngineTemperature')
    def test_temperature_engine_too_high(self, mock_method):
        # prepare mock
        mock_method.return_value = "100C temperature engine is too high"
        # testing
        test_object = Car()
        result = test_object.getEngineTemperature()
        self.assertEqual("100C temperature engine is too high", result)

    @patch.object(Car, 'getEngineTemperature')
    def test_temperature_engine_too_low(self, mock_method):
        # prepare mock
        mock_method.return_value = "30C temperature engine is too low"
        # testing
        test_object = Car()
        result = test_object.getEngineTemperature()
        self.assertEqual("30C temperature engine is too low", result)


if __name__ == '__main__':
    main()
