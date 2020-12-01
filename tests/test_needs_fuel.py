from src.sample.car import *
from unittest.mock import *
from unittest import TestCase, main


class test_Car_needFuel(TestCase):
    @patch.object(Car, 'needsFuel')
    def test_fuel_method_lack(self, mock_method):
        # prepare mock
        mock_method.return_value = False
        # testing
        test_object = Car()
        result = test_object.needsFuel()
        self.assertEqual(False, result)

    @patch.object(Car, 'needsFuel')
    def test_fuel_method_full(self, mock_method):
        # prepare mock
        mock_method.return_value = True
        # testing
        test_object = Car()
        result = test_object.needsFuel()
        self.assertEqual(True, result)


if __name__ == '__main__':
    main()
