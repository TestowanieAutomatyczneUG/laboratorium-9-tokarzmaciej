from src.sample.car import *
from unittest.mock import *
from unittest import TestCase, main


class test_Car_driveTo(TestCase):
    @patch.object(Car, 'driveTo')
    def test_driveTo(self, mock_method):
        # prepare mock
        destination = "my home"
        mock_method.return_value = ("drive to %s" % destination)
        # testing
        test_object = Car()
        result = test_object.driveTo(destination)
        self.assertEqual("drive to my home", result)


if __name__ == '__main__':
    main()
